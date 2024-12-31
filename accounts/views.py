from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        if self.request.user.department == 'MD':
            return reverse('job_orders:md_dashboard') 
        elif self.request.user.department == 'FM':
            return reverse('job_orders:fm_dashboard')
        elif self.request.user.department == 'Sales':
            return reverse('job_orders:sales_dashboard')
        else:
            return reverse('home')

def logout_view(request):
    logout(request)
    return redirect('login')