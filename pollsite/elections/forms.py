from .models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
    prvkey = -1;
    pubkey = -1;
    
    def set_prvkey(self, prvkey):
        self.prvkey = prvkey
        
    def set_pubkey(self, pubkey):
        self.pubkey = pubkey

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('key',)