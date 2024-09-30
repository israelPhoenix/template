import threading
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth.forms import PasswordResetForm
from .models import User


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    username = forms.CharField(
        max_length=150
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )


# create form user
class UserForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )

    email = forms.EmailField(
        label=_("Email est requis."),
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre email'
        })
    )
    gender = forms.ChoiceField(
        label=_('Genre'),
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'gender',
            'name': 'gender'
        }),
        required=True,
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom'
        })
    )
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre prénom'
        })
    )
    lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom de famille'
        })
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre numéro de téléphone'
        })
    )
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre pays'
        })
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre ville'
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre adresse'
        })
    )
    date_of_birth = forms.CharField(
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Entrez votre date de naissance'
        })
    )
    def clean_email(self):
        form_email = self.cleaned_data['email'].lower()
        try:
            user_instance = self.instance.admin  # Récupérer l'instance de l'utilisateur associée à l'objet en cours
            db_email = user_instance.email.lower()  # Récupérer l'adresse e-mail actuelle de l'utilisateur
        except AttributeError:
            # Ignorer si l'attribut admin n'existe pas dans l'instance
            pass

        return form_email

    class Meta:
        model = User
        fields = ['name', 'firstname', 'lastname', 'email', 'phone', 'gender',
                  'date_of_birth', 'country', 'city', 'address']

        # widgets = {
        #     'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        # }


# edit form user
class UserEditForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )

    email = forms.EmailField(
        label=_("Email est requis."),
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre email'
        })
    )
    gender = forms.ChoiceField(
        label=_('Genre'),
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'gender',
            'name': 'gender'
        }),
        required=False
    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom'
        })
    )
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre prénom'
        })
    )
    lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom de famille'
        })
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre numéro de téléphone'
        })
    )
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre pays'
        })
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre ville'
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre adresse'
        })
    )
    # date_of_birth = forms.CharField(
    #     required=False,
    #     widget=forms.DateInput(attrs={
    #         'class': 'form-control',
    #         'type': 'date',
    #         'placeholder': 'Entrez votre date de naissance'
    #     })
    # )

    def clean_email(self):
        form_email = self.cleaned_data['email'].lower()
        try:
            user_instance = self.instance.admin  # Récupérer l'instance de l'utilisateur associée à l'objet en cours
            db_email = user_instance.email.lower()  # Récupérer l'adresse e-mail actuelle de l'utilisateur

        except AttributeError:
            # Ignorer si l'attribut admin n'existe pas dans l'instance
            pass

        return form_email

    class Meta:
        model = User
        fields = ['name', 'firstname', 'lastname', 'email', 'phone', 'gender',
                   'country', 'city', 'address']


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    new_password1 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    new_password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    def clean_current_password(self, *args, **kwargs):
        current_password = self.cleaned_data.get('current_password')

        if not self.user.check_password(current_password):
            raise forms.ValidationError("Incorrect password")

        return current_password

    def clean_new_password1(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError("Password mismatch")

        return new_password1


class SendEmailForm(PasswordResetForm, threading.Thread):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            threading.Thread.__init__(self)

            for field in self.fields:
                self.fields[field].widget.attrs.update({"class": "form-control"})

        def clean_email(self):
            if not User.objects.filter(email__iexact=self.cleaned_data.get('email')).exists():
                raise forms.ValidationError("The email is not registered")

            return self.cleaned_data.get('email')

        def run(self) -> None:
            return super().send_mail(
                self.subject_template_name,
                self.email_template_name,
                self.context,
                self.from_email,
                self.to_email,
                self.html_email_template_name, 
            )
            
        def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name):
            self.subject_template_name = subject_template_name
            self.email_template_name = email_template_name
            self.context = context
            self.from_email = from_email
            self.to_email = to_email
            self.html_email_template_name = html_email_template_name
            
            self.start()


class ResetPasswordConfirmForm(forms.Form):
    new_password1 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    new_password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    def clean_new_password1(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')
        
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password mismatch")

        return new_password1

    def save(self, commit=True, *args, **kwargs):
        self.user.set_password(self.cleaned_data.get('new_password1'))

        if commit:
            self.user.save()

        return self.user