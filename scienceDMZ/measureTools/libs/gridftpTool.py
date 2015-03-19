#!/usr/bin/python

import sys, time, subprocess, os, csv, re

def comandoSSH(usuario,ip_remoto,cmd):
	ssh_obj = subprocess.Popen(["ssh", usuario + "@" + ip_remoto , cmd],
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE)

	saida = ssh_obj.communicate()
	if saida[1] != "":
		print saida[1]
	return saida

def getGridftp(path_arquivos,copia_atual,usuario,ip_remoto,cmd_gridftp):
	print "Iniciando a copia " + str(copia_atual) 

	saida_gridftp = comandoSSH(usuario,ip_remoto,cmd_gridftp)

	regex_velocidade = "[\d.]* [\w]*/sec avg"
	lista_velocidade = re.findall(regex_velocidade,saida_gridftp[0])
	velocidade       = lista_velocidade[len(lista_velocidade) - 1]
	velocidade       = velocidade.replace(" avg", "")
	velocidade 		 = conversorMbits(velocidade)

	regex_tempo = "[\d]*m[\d.]*s"
	lista_tempo = re.findall(regex_tempo,saida_gridftp[1])
	tempo       = lista_tempo[0]

	criarCsvGridftp(path_arquivos,tempo,velocidade)
	criarTxtGridftp(path_arquivos,saida_gridftp[0],saida_gridftp[1],copia_atual)

def criarCsvGridftp(path_arquivos,tempo,velocidade):
	path_arquivo_csv = path_arquivos + ".csv"
	data             = time.strftime('%Y%m%d')

 	c = csv.writer(open(path_arquivo_csv,"a"))
	if (os.stat(path_arquivo_csv).st_size == 0):
		c.writerow(['data','tempo','velocidade'])
	c.writerow([data,tempo,velocidade])

def criarTxtGridftp(path_arquivos,dados,tempos,copia_atual):
	data             = time.strftime('%Y%m%d')
	path_arquivo_txt = path_arquivos + "_" + str(copia_atual) + "_" + data + ".txt"

 	f = open(path_arquivo_txt,"w")
	f.write(dados)
	f.write(tempos)
	f.close

def conversorMbits(velocidade):
	numero = float(re.search('[\d.]*',velocidade).group(0))
	
	if velocidade[-6] == "G":
		numero = numero*1024
	elif velocidade[-6] == "k":
		numero = numero/1024

	if velocidade[-5] == "B":
		numero = numero*8

	return str(numero) + " Mb/sec"

def gridftpTool(ip_remoto,tamanho,limite,pasta_ori,pasta_des,fluxo,pasta_resultado):
	tipo     = "gridftp_ftp"
	usuario  = "root"
	porta    = "2811"
	data     = time.strftime('%Y%m%d')

	pasta_resultado = pasta_resultado + "/resultados_" + tamanho
	pasta           = tamanho + "/" + fluxo
	arquivo         = "resultado_" + tipo + "_" + tamanho + "_" + fluxo + "_" + data
	path_arquivos   = pasta_resultado + "/" + tipo + "/" + "resultado_" + tipo + "_" + tamanho + "_" + fluxo

	print "\nCriando pasta remota para envio de arquivos ...\n"

	cmd_ssh = "if [ ! -d " + pasta_des + "/" + pasta + " ] ; then mkdir -p " + pasta_des + "/" + pasta + " ; fi"
	subprocess.check_call(['ssh',usuario + "@" + ip_remoto,cmd_ssh])

	print "\nCriando pastas locais para salvar os resultados\n"

	if not os.path.exists(pasta_resultado + "/" + tipo):
	  os.makedirs(pasta_resultado + "/" + tipo)

	for i in range (1,int(limite)+1):
		cmd_gridftp = "time /usr/bin/globus-url-copy -vb -p " + fluxo + " file://" + pasta_ori + "/" + tamanho + "_file ftp://" + ip_remoto + ":" + str(porta) + pasta_des + "/" + pasta + "/" + tamanho + "_file_" + str(i)
		getGridftp(path_arquivos,i,usuario,ip_remoto,cmd_gridftp)

	print "\nRemovendo a pasta remota\n"

	cmd_ssh = "rm -rf " + pasta_des + "/" + tamanho
	subprocess.check_call(['ssh',usuario + "@" + ip_remoto,cmd_ssh])

	print "\nOs resultados podem ser acessados em: " + path_arquivos + ".csv\n"

	print "\nFim ...\n"