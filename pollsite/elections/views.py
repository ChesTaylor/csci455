from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template, RequestContext
from .models import Candidate
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserForm, UserProfileForm


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

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			# Now we save the UserProfile model instance.
			profile.save()

			# Update our variable to tell the template registration was successful.
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

    # Render the template depending on the context.
	return render_to_response('elections/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)
			
def index(request):
	candidates = Candidate.objects.all()
	halfsize = (candidates.count() // 2) + 1
	template = loader.get_template('elections/index.html')
	context = {
		'candidates': candidates,
		'halfsize': halfsize,
	}
	return HttpResponse(template.render(context, request))

def detail(request, candidate_id):
	return HttpResponse("You're looking at candidate %s." % candidate_id)

def results(request, candidate_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % candidate_id)

def vote(request, candidate_id):
	return HttpResponse("You're voting on question %s." % candidate_id)
