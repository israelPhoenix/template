from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
# from app_Public import forms

class Login(TemplateView):
    template_name= 'public/pages/login.html'
    # form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request, self.template_name, {'form': form, 'message': message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                # condition of admin
                if user.user_type == '0':
                    messages.success(request, "vous venez de vous connectez avec successé")
                    return redirect('dashboard_admin')

                # condition of accountant
                elif user.user_type == '1':
                    messages.success(request, "vous venez de vous connectez avec successé")
                    return redirect('accountant')

                # condition of secretary
                elif user.user_type == '2':
                    messages.success(request, "vous venez de vous connectez avec successé")
                    return redirect('dashborard_sec')

                # condition of teacher
                elif user.user_type == '3':
                    messages.success(request, "vous venez de vous connectez avec successé")
                    return redirect('teacher_dashboard')
                # condition of student
                elif user.user_type == '4':
                    messages.success(request, "vous venez de vous connectez avec successé")
                    return redirect('dashboard_student')
                # if there is any error of the password or username
                else:
                    messages.error(request, "mot de passe ou email est incorrete")
                    return redirect("login")
            else:
                message = 'Invalid'

        return render(
            request, self.template_name, context={'form': form, 'message': message}

        )

class LogoutView(View):
    def get(self, request):
        if request.user != None:
            logout(request)
        return redirect("home")



