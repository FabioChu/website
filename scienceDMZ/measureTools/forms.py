from django import forms
from .models import scpTool, gridftpTool, wgetTool

class ScpForm(forms.ModelForm):
	class Meta:
		model = scpTool
		fields = ('ip_remoto', 'tamanho', 'limite', 'pasta_ori', 'pasta_des', 'pasta_resultado')

class GridftpForm(forms.ModelForm):
	class Meta:
		model = gridftpTool
		fields = ('ip_remoto', 'tamanho', 'limite', 'pasta_ori', 'pasta_des', 'fluxo', 'pasta_resultado')

class WgetForm(forms.ModelForm):
	class Meta:
		model = wgetTool
		fields = ('ip_remoto', 'tamanho', 'limite', 'pasta_des', 'pasta_resultado')
