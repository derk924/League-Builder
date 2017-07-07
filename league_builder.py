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


	sharks = experienced_players[:experienced_players_per_team]
	dragons = experienced_players[experienced_players_per_team: experienced_players_per_team*2]
	raptors = experienced_players[experienced_players_per_team*2:]

	for player in non_experienced_players:
		if len(sharks) != number_of_players_per_team:
			sharks.append(player)
		if len(dragons) != number_of_players_per_team:
			dragons.append(player)
		if len(raptors) != number_of_players_per_team:
			raptors.append(player)

	save_to_file(sharks,dragons,raptors)

def save_to_file(sharks, dragons, raptors):

	with open('teams.txt', 'a') as file:
		file.seek(0)
		file.truncate()

		file.write('Sharks Team:\n============\n\n')
		for player in sharks:
			row = player['name'] + ', ' + player['experience'] + ', ' + player['guardian'] + '\n'
			file.write(row)


		file.write('\n\nDragon Team:\n============\n\n')
		for player in dragons:
			row = player['name'] + ', ' + player['experience'] + ', ' + player['guardian'] + '\n'
			file.write(row)


		file.write('\n\nRaptors Team:\n============\n\n')
		for player in raptors:
			row = player['name'] + ', ' + player['experience'] + ', ' + player['guardian'] + '\n'
			file.write(row)

	all_players = sharks + dragons + raptors
	create_welcome_letters(all_players)


def create_welcome_letters(all_players):

	for player in all_players:
		#print(player['name'].lower())
		name = player['name'].lower()
		#print(name.index(' '))
		index = name.index(' ')
		name = name[:index] + '_' + name[index+1:]
		print(name)




read_csv_file() 

