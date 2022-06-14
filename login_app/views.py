from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index_su(request):
    return render(request, 'index_su.html')

@login_required
def account_redirect(request):
    if request.user.is_superuser:
        return redirect('login_app:index_su')
    else:
        return redirect('login_app:index')