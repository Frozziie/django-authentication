from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

from .forms import SignUpForm


#----------------------------------------------#
#//////////////////////////////////////////////#
#----------------------------------------------#

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper


def home(request):
    count = User.objects.count()
    return render(request, 'core/home.html', {
        'count': count
    })


@login_excluded(home)
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/registration/signup.html', {
        'form': form
    })

        
@login_required
def secret_page(request):
    return render(request, 'core/secret.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'core/secret.html'


