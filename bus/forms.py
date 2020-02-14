from django import forms

class registerform(forms.Form):
    name=forms.CharField(label='Your name',max_length=10,widget=forms.TextInput(attrs={'class':'input100','placeholder':'Your Name',}))
    email=forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'input100','placeholder':'Email'}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'input100','placeholder':'User Name'}))
    password=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class':'input100','placeholder':'Password'}))
    confirmpass = forms.CharField(label='Confirm Password', widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Confirm Password'}))