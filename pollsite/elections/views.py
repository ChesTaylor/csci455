from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template, RequestContext
from .models import Candidate
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .forms import UserForm, UserProfileForm

from bigchaindb import Bigchain
import hashlib
b = Bigchain() # shhh don't tell about the global object and they won't notice

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/elections/login')

def user_login(request):
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/elections/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Elections account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render_to_response('elections/login.html', {}, context)

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			prvkey, pubkey = b.generate_keys()
			user.set_prvkey(prvkey)
			user.setpubkey(pubkey)
			user.save()

			# Update our variable to tell the template registration was successful.
			registered = True
			return HttpResponseRedirect('/elections/login')
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

    # Render the template depending on the context.
	return HttpResponseRedirect(user.pubkey)
	return render_to_response('elections/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)
			
def index(request):
	user = request.user
	candidates = Candidate.objects.all()
	halfsize = (candidates.count() // 2) + 1
	template = loader.get_template('elections/index.html')
	context = {
		'candidates': candidates,
		'halfsize': halfsize,
		'user': user,
	}
	return HttpResponse(template.render(context, request))

def detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'elections/detail.html', {'candidate': candidate})

def results(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    payload = {'choice': candidate_id}
    payload_hash = hashlib.sha3_256(payload).hexdigest()
    txs = b.get_tx_by_payload_hash(payload_hash) # TODO: display these
    return render(request, 'elections/results.html', {'candidate': candidate})

def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    try:
        selected_choice = candidate.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'elections/detail.html', {
            'candidate': candidate,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        digital_asset_payload = {'choice': candidate_id}
        prv, pub = request.user.privkey, request.user.pubkey
        tx = b.create_transaction(b.me, pub, None, 'CREATE', payload=digital_asset_payload)
        tx_signed = b.sign_transaction(tx, b.me_private)
        b.write_transaction(tx_signed)

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect('/elections/' + candidate_id + '/results/')
