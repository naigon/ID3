
import csv, math

def main():
	with open('beach.csv') as f:
		dados = csv.reader(f, delimiter=',')
		
		#lista com cada atributo e as ocorrencias dos respectivos rotulos
		days = []
		outlooks = []
		temperatures = []
		humiditys = []
		winds = [] 
		beachs = []
		
		#listas com os rotulos possiveis de cada atributo
		v_outlook = ['Sunny','Overcast','Rain','','','','','','','','','','','','']
		v_temperature = ['Hot','Mild','Cool','','','','','','','','','','','','']
		v_humidity = ['High','Normal','Null','','','','','','','','','','',''] 
		v_wind = ['Weak','Strong','Null','','','','','','','','','','','','']
		v_beach = ['Yes','No','','','','','','','','','','','','','']#classe
		
		for row in dados:
			day = row[0]
			outlook = row[1]
			temperature = row[2]
			humidity = row[3]
			wind = row[4]
			beach = row[5]
			
			days.append(day)
			outlooks.append(outlook)
			temperatures.append(temperature)
			humiditys.append(humidity)
			winds.append(wind)
			beachs.append(beach)
		
		n_exemplos = len(days) - 1
		tam = 3
		#listas que irao armazenar a ocorrencia de cada um dos rotulos nos atributos
		ocorrencia_r_outlook = list(range(tam))
		ocorrencia_r_temperature = list(range(tam))
		ocorrencia_r_humidity = list(range(tam))
		ocorrencia_r_wind = list(range(tam))
		ocorrencia_r_beach = list(range(tam))
		
		for i in range(tam):
			ocorrencia_r_outlook[i] = outlooks.count(v_outlook[i])
			ocorrencia_r_temperature[i] = temperatures.count(v_temperature[i])
			ocorrencia_r_humidity[i] = humiditys.count(v_humidity[i])
			ocorrencia_r_wind[i] = winds.count(v_wind[i])
			ocorrencia_r_beach[i] = beachs.count(v_beach[i])
		
		#entropia exemplos
		count_y = beachs.count(v_beach[0])#ocorrencias de 'Yes'
		count_n = beachs.count(v_beach[1])#ocorrencias de 'No'
		entropia_exemplos = -ocorrencia_r_beach[0]/n_exemplos * math.log(ocorrencia_r_beach[0]/n_exemplos, 2) - ocorrencia_r_beach[1]/n_exemplos * math.log(ocorrencia_r_beach[1]/n_exemplos, 2)
		
		print ('\nEntropia dos Exemplos: ' , round(entropia_exemplos,6))
		
		#calculo do ganho para a escolha do atributo de decisão(raiz da arvore)
		ganho_wind = ganho(entropia_exemplos, winds,v_wind, ocorrencia_r_wind, n_exemplos, beachs)
		ganho_outlook = ganho(entropia_exemplos, outlooks, v_outlook, ocorrencia_r_outlook, n_exemplos, beachs)
		ganho_humidity = ganho(entropia_exemplos, humiditys, v_humidity, ocorrencia_r_humidity, n_exemplos, beachs)
		ganho_temperature = ganho(entropia_exemplos,temperatures,v_temperature,ocorrencia_r_temperature,n_exemplos,beachs)
		
		print('Ganho atributo Wind: ', round(ganho_wind,6))
		print('Ganho atributo Humidity: ', round(ganho_humidity,6))
		print('Ganho atributo Temperature: ', round(ganho_temperature,6))
		print('Ganho atributo Outlook: ', round(ganho_outlook,6))

def calc_entropia(atributo_alvo, rotulo_alvo, ocorrencia_rotulo, classes):
	n_ocorrencias = list(range(2))
	n_ocorrencias = ocorrencias_classe(atributo_alvo, rotulo_alvo, classes)
	entropia = -n_ocorrencias[0]/ocorrencia_rotulo * math.log((n_ocorrencias[0]/ocorrencia_rotulo) if (n_ocorrencias[0]/ocorrencia_rotulo) > 0 else 1, 2) - n_ocorrencias[1]/ocorrencia_rotulo * math.log((n_ocorrencias[1]/ocorrencia_rotulo) if (n_ocorrencias[1]/ocorrencia_rotulo)>0 else 1, 2)
	entropia = round(entropia,6)
	return entropia

#função que faz a contagem, pra cada rotulo, quantos 'Yes' e 'No' possuem
def ocorrencias_classe(atributo_alvo, rotulo_atributo, classes):
	ocorrencia = list(range(2))
	ocorrencia[0] = 0
	ocorrencia[1] = 0
	for i in range(len(atributo_alvo)):
		if atributo_alvo[i]==rotulo_atributo and classes[i]=='Yes':
			ocorrencia[0] = ocorrencia[0] + 1
		elif atributo_alvo[i]==rotulo_atributo and classes[i]=='No':
			ocorrencia[1] = ocorrencia[1] + 1
	return ocorrencia

def cria_arvore(rotulo1, rotulo2, rotulo3, rotulo4, rotulo_raiz, classes):#incompleto
	if classes.count('Yes') == 14:
		resposta = list(range(2))
		resposta[0] = rotulo_raiz
		resposta[1] = 'Yes'
		return resposta
	elif classes.count('No') == 14:
		resposta = list(range(2))
		resposta[0] = rotulo_raiz
		resposta[1] = 'No'
		return resposta

def ganho(entropia, atributo,valores_rotulo, ocorrencias_rotulo, n_exemplos, classes):
	ganho = entropia
	laco = 0
	if valores_rotulo[2]=='Null':
		laco = 2
	else:
		laco = 3
	for i in range(laco):
		ganho -= ocorrencias_rotulo[i]/n_exemplos * calc_entropia(atributo, valores_rotulo[i], ocorrencias_rotulo[i], classes)
	return round(ganho,6)

main()
