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
    
    def save(self):
            
        def set_pubkey(pubkey):
            self.pubkey = pubkey

        def set_prvkey(prvkey):
            self.prvkey = prvkey

        ret = super().save()
        ret.set_prvkey = set_prvkey
        ret.set_pubkey = set_pubkey
        return ret

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('key',)