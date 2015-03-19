from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import ScpForm, GridftpForm, WgetForm
from measureTools.libs import scpTool, gridftpTool, wgetTool
from .models import Scp

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
		return HttpResponseRedirect('/')

	return render_to_response("scp_tool.html", 
                                locals(), 
                                context_instance=RequestContext(request))

def gridftp_tool(request):
	gridftp_form = GridftpForm(request.POST or None)

	if gridftp_form.is_valid():
		ip_remoto = gridftp_form.cleaned_data['ip_remoto']
		tamanho = gridftp_form.cleaned_data['tamanho']
		limite = gridftp_form.cleaned_data['limite']
		pasta_des = gridftp_form.cleaned_data['pasta_des']
		pasta_ori = gridftp_form.cleaned_data['pasta_ori']
		fluxo = gridftp_form.cleaned_data['fluxo']
		pasta_resultado = gridftp_form.cleaned_data['pasta_resultado']
		gridftpTool.gridftpTool(ip_remoto,tamanho,limite,pasta_ori,pasta_des,fluxo,pasta_resultado)
		return HttpResponseRedirect('/')

	return render_to_response("gridftp_tool.html", 
                                locals(), 
                                context_instance=RequestContext(request))

def wget_tool(request):
	wget_form = WgetForm(request.POST or None)

	if wget_form.is_valid():
		ip_remoto = wget_form.cleaned_data['ip_remoto']
		tamanho = wget_form.cleaned_data['tamanho']
		limite = wget_form.cleaned_data['limite']
		pasta_des = wget_form.cleaned_data['pasta_des']
		pasta_resultado = wget_form.cleaned_data['pasta_resultado']
		wgetTool.wgetTool(ip_remoto,tamanho,limite,pasta_des,pasta_resultado)
		return HttpResponseRedirect('/')

	return render_to_response("wget_tool.html", 
                                locals(), 
                                context_instance=RequestContext(request))

def data_scp(request):
	scp_all_entries = Scp.objects.all()
	return render_to_response("data_scp.html", 
                                locals(), 
                                context_instance=RequestContext(request))
