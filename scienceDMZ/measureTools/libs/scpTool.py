#!/usr/bin/python

import subprocess, re, sys, time, csv, os
from measureTools.models import Scp

def executa_scp(cmd):
	p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout = []
	while True:
		line = p.stdout.readline()
		stdout.append(line)
		if line == '' and p.poll != None:
			break
	return ''.join(stdout)

def tamanho_em_bits(tamanho):
	if tamanho == '128M':
		return 128*8
	elif tamanho == '1G':
		return 1024*8
	elif tamanho == '10G':
		return 10240*8
	else:
		return 0

def criarCsvGridftp(path_arquivo_csv,data,velocidade,tamanho):
 	c = csv.writer(open(path_arquivo_csv,"a"))
	if (os.stat(path_arquivo_csv).st_size == 0):
		c.writerow(['data','velocidade'])
	c.writerow([data,velocidade])
	s = Scp(data=data ,velocidade=velocidade, tamanho=tamanho)
	s.save()

def scpTool(ip_remoto,tamanho,limite,pasta_ori,pasta_des,pasta_resultado):
	tipo     = "scp"
	usuario  = "root"
	data     = time.strftime('%d/%m/%Y')

	print "\nCriando pasta remota para envio de arquivos ...\n"
	
	cmd_ssh = "if [ ! -d " + pasta_des + "/" + tamanho + " ] ; then mkdir -p " + pasta_des + "/" + tamanho + " ; fi"

	subprocess.check_call(['ssh',usuario + "@" + ip_remoto,cmd_ssh])

	print "\nCriando pasta local para os resultados ...\n"

	if not os.path.exists(pasta_resultado + "/resultados_" + tamanho):
	  os.makedirs(pasta_resultado + "/resultados_" + tamanho)

	print "\nExecutando o scp e salvando em um csv...\n"

	path_arquivo_csv = pasta_resultado + "/resultados_" + tamanho + "/resultado_" + tipo + "_" + tamanho + ".csv"
	cmd = "scp -v " + pasta_ori + "/" + tamanho + "_file " + usuario + "@" + ip_remoto + ":" + pasta_des + "/" + tamanho + "/" + tamanho + "_file"
	regex_tempo = '[\d.]{1,}'
	regex_linha_tempo = 'Transferred:[\w ,.]*'

	retorno_scp = executa_scp(cmd)
	lista_tempo = re.findall(regex_linha_tempo,retorno_scp)
	if not lista_tempo:
		print retorno_scp
		exit()
	tempo = re.findall(regex_tempo,lista_tempo[0])
	velocidade = tamanho_em_bits(tamanho)/float(tempo[len(tempo) - 1])
	velocidade = str(float('{0:.2f}'.format(velocidade))) + " Mb/s"
	criarCsvGridftp(path_arquivo_csv,data,velocidade,tamanho)

	print "\nRemovendo o arquivo remoto\n"

	cmd_ssh = "rm -rf " + pasta_des + "/" + tamanho 
	subprocess.check_call(['ssh',usuario + "@" + ip_remoto,cmd_ssh])

	print "\nResulatados podem ser vistos em " + path_arquivo_csv