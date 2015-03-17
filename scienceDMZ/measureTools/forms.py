from django import forms
from .models import scpTool

class ScpForm(forms.ModelForm):
	class Meta:
		model = scpTool
		fields = ('ip_remoto', 'tamanho', 'limite', 'pasta_ori', 'pasta_des', 'pasta_resultado')
