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

	experpienced_players(players)

def experpienced_players(players):

	number_of_experienced_players = 0

	for player in players:
		if player['experience'] == 'YES':
			number_of_experienced_players += 1

	print(number_of_experienced_players)




read_csv_file() 

