import csv

def read_csv_file():
	players = []
	with open('soccer_players.csv') as file_object:
		rows = csv.DictReader(file_object, delimiter = ',')
		for row in rows:
			player = {'name':'', 'height':'', 'experience':'', 'guardian':''}
			player['name'] = row['Name']
			player['height'] = row['Height (inches)']
			player['experience'] = row['Soccer Experience']
			player['guardian'] = row['Guardian Name(s)']

			players.append(player)


read_csv_file() 

