from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
# Create your views here.

@login_required
def change_password(request):
    import pdb; pdb.set_trace()
    newpassword = request.POST.get("newpassword")
    renewpasssword = request.POST.get("renewpasssword")
    username=request.user.username
    if newpassword == renewpasssword:
        if request.method == 'GET':
            form = ChangePasswordForm()
        else:
            u = User.objects.get(username__exact=username)
            u.set_password(newpassword)
            u.save()
            return redirect('/users/account')
    else:
        return redirect('/change/password/')
    return render(request,'changepassword.html', {'form': form,})