from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from .forms import UserProfileForm, UserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def main(request):
	return render_to_response("main.html", 
                                locals(), 
                                context_instance=RequestContext(request))

def register(request):
	user_form = UserForm(request.POST or None)
	profile_form = UserProfileForm(request.POST or None)

	if user_form.is_valid() and profile_form.is_valid():
		user = user_form.save()
		user.set_password(user.password)
		user.save()
		profile = profile_form.save(commit=False)
		profile.user = user
		profile.save()
		return HttpResponseRedirect('/main/')

	return render_to_response("register.html", 
                                locals(), 
                                context_instance=RequestContext(request))

def user_login(request):
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			login(request, user)
			return HttpResponseRedirect('/main/')
		else:
			messages.info(request,"Invalid login details: {0}, {1}".format(username, password))

	return render_to_response("main.html", 
							locals(), 
							context_instance=RequestContext(request))

def user_logout(request):
	logout(request)
	print 'oi'
	return HttpResponseRedirect('/main/')
	return render_to_response("main.html", 
							locals(), 
							context_instance=RequestContext(request))