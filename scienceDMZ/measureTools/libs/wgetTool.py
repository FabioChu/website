import sys
import subprocess
import os
import re
import shutil

"""
****************************************

Nome: get_download_speed

Descricao: Funcao para adquirir a velocidade de download dada uma string

Parametros: output_line - string que contenha velocidade no formato [dd,d *B/s]

Saida: string com a velocidade de donwload em MB/s

****************************************
"""
def get_download_speed(output_line):

	speed = re.search('\d+,\d+ \w+\/s', output_line)

	if speed:
		return speed.group(0)
	else :
		print 'ERRO na leitura da velocidade'
		return '00.0 MB/s'


"""
****************************************

Nome: get_download_speed

Descricao: Funcao para adquirir o tempo de download dada uma string

Parametros: output_line - string que contenha tempo de download em horas, minutos e segundos

Saida: string com o tempo de download da mesma forma da entrada

****************************************
"""
def get_download_time_elapsed(output_line) :

	time = re.search('(\d+(,?\d*s|m|h) )+', output_line)

	if time:
		return time.group(0)
	else :
		print 'ERRO na leitura do tempo'
		return '0s'

"""
****************************************

Nome: remove_files

Descricao: Funcao que remove um diretorio e seus arquivos ou um arquivo

Parametros: path_files - string caminho do arquivo 

Saida: True se sucesso e False se acontecer erro

****************************************
"""

def remove_files(path_files) :

	if os.path.isdir(path_files):
		try:
			shutil.rmtree(path_files)
			return True
		except:
			print "Nao foi possivel remover o diretorio " + path_files
			return False
	else :
		try:
			os.remove(path_files)
			return True
		except:
			print "Nao foi possivel remover o arquivo " + path_files
			return False


"""
****************************************

Name: get_last_line

Descricao: Funcao que devolve a ultima linha de um texto

Parametros:	name_file - string que contem o nome do arquivo

Saida: string com a ultima linha do texto

****************************************
"""

def get_last_line(name_file):
	text_file = open(name_file, 'r')
	lineList = text_file.readlines()
	text_file.close()
	last_line = lineList[-1]
	print last_line
	#It's necessary to remove the last caractere(EOL) or will not be possible to scan the string using regex
	last_line = last_line[:-1]
	return last_line

"""
****************************************

Name: converte_byte_bit

Descricao: Converte um valor de velocidade de byte para bit

Parametros: speed_byte - string que contem a velocidade em MB/s

Saida: string com a velocidade em Mb/s

****************************************
"""

def converte_byte_bit(speed_byte) :

	speed_bit = re.search('\d+,\d+', speed_byte)

	if speed_bit:
		speed_bit = speed_bit.group(0)

		speed_bit = speed_bit.replace(',', '.')

		speed_bit = str (float(speed_bit) * 8.0)
	
		speed_bit = speed_bit.replace('.', ',')

		return speed_bit
	else :
		print 'Erro na conversao de byte para bit'
		return '0,0'


"""
****************************************

Name: list_to_file

Descricao: Escreve o conteudo de uma lista em um arquivo

Parametros:	input_list - uma lista contendo uma lista de elementos
			name_of_file - string com o nome do arquivo

Saida: True se sucesso e False em caso de erro

****************************************
"""

def list_to_file(input_list, name_file) :
	output_file = open(name_file, 'w')

	for sub_list in input_list:
		for content in sub_list:
			output_file.write("%s	" % content)
		output_file.write("\n")


"""
****************************************
Programa principal
****************************************
"""
def wgetTool(ip_remoto,tamanho,limite,folder_des,pasta_resultado):

	user = "sdmz"
	tipo = "wget"

	arquivo="resultado_" + tipo + "_" + tamanho
	folder = tamanho
	pasta_resultado= pasta_resultado + "/resultados_" + tamanho

	host_name = user + "@" + ip_remoto
	ssh_mkdir = "if [ ! -d " + folder_des + "/" + folder + " ] ; then mkdir -p " + folder_des + "/" + folder + " ; fi"

	try: 
		ssh = subprocess.Popen(['ssh', host_name, "%s"%(ssh_mkdir)])
		ssh.communicate()
	except subprocess.CalledProcessError:
		print "Erro na conexao ssh"
		exit()


	if not os.path.isdir(pasta_resultado) :
		os.makedirs(pasta_resultado)
	if not os.path.isdir(pasta_resultado + "/" +tipo) :
		os.makedirs(pasta_resultado + "/" +tipo)
	if not os.path.isdir(folder_des + "/" + folder) :
		os.makedirs(folder_des + "/" + folder)


	remove_files(pasta_resultado + '/' + tipo + "*.txt")

	lista_tempo_velocidade = []

	#converter para Mbit
	for i in range(limite) :
		print "iniciando copia =", i
		wget = subprocess.Popen(['wget', '-O', folder_des+"/"+folder+"/"+tamanho+"_file_"+str(i), '-m', "ftp://"+ip_remoto+"/"+tamanho+"_file", '-o', 'output.txt'])
		wget.communicate()

		last_line = get_last_line('output.txt')
		tempo = get_download_time_elapsed(last_line)
		velocidade = get_download_speed(last_line)
		velocidade = converte_byte_bit(velocidade)
		lista_tempo_velocidade.append([tempo, velocidade])

	arquivo_saida = pasta_resultado + "/" + tipo + "/" + arquivo + ".csv"

	list_to_file(lista_tempo_velocidade, arquivo_saida )

	print "Removendo os arquivos auxiliares"

	remove_files(folder_des + "/" + ip_remoto + "/")
	remove_files(folder_des + "/" + folder + "/")
	remove_files(ip_remoto + "/")
	remove_files('output.txt')


	print "Os resultados estao disponiveis em " + pasta_resultado + "/" + tipo + "/" + arquivo + ".csv"

	resultado = open(pasta_resultado + "/" + tipo + "/" + arquivo + ".csv",'r')
	print resultado.read()
	resultado.close()