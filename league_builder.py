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

	count_experpienced_players(players)

def count_experpienced_players(players):

	#number_of_experienced_players = 0
	experienced_players = []
	non_experienced_players = []

	for player in players:
		if player['experience'] == 'YES':
			#number_of_experienced_players += 1
			experienced_players.append(player)
		else:
			non_experienced_players.append(player)

	#print(number_of_experienced_players)
	divide_players(experienced_players, non_experienced_players, players)

def divide_players(experienced_players, non_experienced_players, players):

	NUMBER_OF_TEAMS = 3
	number_of_players_per_team = int(len(players) / NUMBER_OF_TEAMS)
	experienced_players_per_team = int(len(experienced_players) / NUMBER_OF_TEAMS)

	#print(number_of_players_per_team)
	#print(experienced_players_per_team)

	sharks = experienced_players[0:experienced_players_per_team]
	dragons = experienced_players[experienced_players_per_team: experienced_players_per_team*2]
	raptors = experienced_players[experienced_players_per_team*2:]

	print(sharks)
	print('---------------------------------------')
	print(dragons)
	print('---------------------------------------')
	print(raptors)





read_csv_file() 

