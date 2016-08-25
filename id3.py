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
		v_outlook = ['Sunny','Overcast','Rain']
		v_temperature = ['Hot','Mild','Cool']
		v_humidity = ['High','Normal'] 
		v_wind = ['Weak','Strong']
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
		
		count_y = beachs.count('Yes')
		count_n = beachs.count('No')
		entropia_exemplos = -count_y/n_exemplos * math.log(count_y/n_exemplos, 2) - count_n/n_exemplos * math.log(count_n/n_exemplos, 2)
		print ('Entropia dos exemplos: ' , entropia_exemplos)
		entropia_wind = entropia(winds, n_exemplos, beachs)
		
def calc_entropia(atributo_alvo, valores_atributo, n_exemplos, classes):
	tam = len(valores_atributo)
	count = list(range(tam))
	for i in range(tam):
		count[i] = atributo_alvo.count(valores_atributo[i])
######################################################################
	return 


def calc_ganho(entropia, atributo_alvo, valores_atributo, n_exemplos):

	for i in range(tam):
		count[i] = atributo_alvo.count(valores_atributo[i])
	for i in range(tam):
		desconto = -count[i]/n_exemplos * entropia(count[i], count[i], n_exemplos)
	ganho = entropia - desconto
	return ganho
		



main()
