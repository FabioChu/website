from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import ScpForm
from measureTools.libs import scpTool

# Create your views here.

def scp_tool(request):
	scp_form = ScpForm(request.POST or None)

	if scp_form.is_valid():
		ip_remoto = scp_form.cleaned_data['ip_remoto']
		tamanho = scp_form.cleaned_data['tamanho']
		limite = scp_form.cleaned_data['limite']
		pasta_des = scp_form.cleaned_data['pasta_des']
		pasta_ori = scp_form.cleaned_data['pasta_ori']
		pasta_resultado = scp_form.cleaned_data['pasta_resultado']
		scpTool.scpTool(ip_remoto,tamanho,limite,pasta_ori,pasta_des,pasta_resultado)
		return HttpResponseRedirect('/main/')

	return render_to_response("scp_tool.html", 
                                locals(), 
                                context_instance=RequestContext(request))