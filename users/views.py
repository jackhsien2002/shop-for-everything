from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from .forms import SignUpForm

class SignUpView(View):
    template_name='users/signup.html'
    class_form=SignUpForm
    
    def get(self,request):
        form = self.class_form()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form=self.class_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signup_success'))
        return render(request, self.template_name, {'form':form})

class SignUpSuccessView(View):
    template_name='users/signup_success.html'
    def get(self, request):
        return render(request, self.template_name)