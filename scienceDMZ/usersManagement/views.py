from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from .forms import UserProfileForm, UserForm

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
		messages.success(request, 'Profile created.')

	return render_to_response("register.html", 
                                locals(), 
                                context_instance=RequestContext(request))