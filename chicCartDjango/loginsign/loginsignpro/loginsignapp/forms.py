from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    mobile=forms.IntegerField()
    address=forms.CharField(max_length=100)
    email=forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
    def clean_mobile_number(self):
        mobile = self.cleaned_data['mobile']
        cleaned_mobile_number = ''.join(filter(str.isdigit, mobile))
        if len(cleaned_mobile_number) < 10:
            raise forms.ValidationError("Mobile number should have at least 10 digits.")
        return cleaned_mobile_number