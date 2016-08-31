
import csv, math

def main():
	with open('beach.csv') as f:
		dados = csv.reader(f, delimiter=',')
		days = []
		outlooks = []
		temperatures = []
		humiditys = []
		winds = [] 
		beachs = []
		v_outlook = ['Sunny','Overcast','Rain','','','','','','','','','','','','']
		v_temperature = ['Hot','Mild','Cool','','','','','','','','','','','','']
		v_humidity = ['High','Normal','','','','','','','','','','','',''] 
		v_wind = ['Weak','Strong','','','','','','','','','','','','','']
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
		
		count_y = beachs.count(v_beach[0])
		count_n = beachs.count(v_beach[1])
		entropia_exemplos = -ocorrencia_r_beach[0]/n_exemplos * math.log(ocorrencia_r_beach[0]/n_exemplos, 2) - ocorrencia_r_beach[1]/n_exemplos * math.log(ocorrencia_r_beach[1]/n_exemplos, 2)
		
		print ('\nEntropia dos Exemplos: ' , round(entropia_exemplos,6))
		
		'''
		print(v_outlook,ocorrencia_r_outlook)
		print(v_temperature,ocorrencia_r_temperature)
		print(v_humidity,ocorrencia_r_humidity)
		print(v_wind,ocorrencia_r_wind)
		print(v_beach,ocorrencia_r_beach)
		'''
		
		print('Ganho atributo Wind :',round(entropia_exemplos - ((ocorrencia_r_wind[0]/n_exemplos)*calc_entropia(winds, v_wind[0], ocorrencia_r_wind[0], beachs)) - ((ocorrencia_r_wind[1]/n_exemplos)*calc_entropia(winds, v_wind[1], ocorrencia_r_wind[1], beachs)),6))
		
		print('Ganho atributo Humidity: ',round(entropia_exemplos - ((ocorrencia_r_humidity[0]/n_exemplos)*calc_entropia(humiditys, v_humidity[0], ocorrencia_r_humidity[0], beachs)) - ((ocorrencia_r_humidity[1]/n_exemplos)*calc_entropia(humiditys, v_humidity[1], ocorrencia_r_humidity[1], beachs)),6))
		
		print('Ganho atributo Temperature :',round(entropia_exemplos - ((ocorrencia_r_temperature[0]/n_exemplos)*calc_entropia(temperatures, v_temperature[0], ocorrencia_r_temperature[0], beachs)) - ((ocorrencia_r_wind[1]/n_exemplos)*calc_entropia(temperatures, v_temperature[1], ocorrencia_r_temperature[1], beachs)) - ((ocorrencia_r_temperature[2]/n_exemplos)*calc_entropia(temperatures, v_temperature[2], ocorrencia_r_temperature[2], beachs)),6))
		
		print('Ganho atributo Outlook :',round(entropia_exemplos - ((ocorrencia_r_outlook[0]/n_exemplos) * calc_entropia(outlooks, v_outlook[0], ocorrencia_r_outlook[0], beachs)) - ((ocorrencia_r_outlook[1]/n_exemplos) * calc_entropia(outlooks, v_outlook[1], ocorrencia_r_outlook[1], beachs)) - ((ocorrencia_r_outlook[2]/n_exemplos) * calc_entropia(outlooks, v_outlook[2], ocorrencia_r_outlook[2], beachs)),6))
		
		
def calc_entropia(atributo_alvo, rotulo_atributo, ocorrencia_rotulo, classes):
	count_pos = 0
	count_neg = 0
	
	for i in range(len(atributo_alvo)):
		if atributo_alvo[i]==rotulo_atributo and classes[i]=='Yes':
			count_pos = count_pos + 1
		elif atributo_alvo[i]==rotulo_atributo and classes[i]=='No':
			count_neg = count_neg + 1
			
	entropia = -count_pos/ocorrencia_rotulo * math.log((count_pos/ocorrencia_rotulo) if (count_pos/ocorrencia_rotulo) > 0 else 1, 2) - count_neg/ocorrencia_rotulo * math.log((count_neg/ocorrencia_rotulo) if (count_neg/ocorrencia_rotulo)>0 else 1, 2)
	entropia = round(entropia,6)
	return entropia



main()
