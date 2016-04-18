from .models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def save(self):
            
        def set_pubkey(user, pubkey):
            user.pubkey = pubkey

        def set_prvkey(user, prvkey):
            user.prvkey = prvkey

        ret = super().save()
        ret.prvkey = -1
        ret.pubkey = -1
        ret.set_prvkey = set_prvkey
        ret.set_pubkey = set_pubkey
        return ret

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('key',)