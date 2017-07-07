import csv

# function below is for reading form CSV file and then assign data 
# extracted to players list

def read_csv_file(file_object):
	players = [] # a list for all players
	
	rows = csv.DictReader(file_object, delimiter = ',')
	for row in rows:
		player = {'name':'', 'height':'', 'experience':'', 'guardian':''}
		player['name'] = row['Name']
		player['height'] = row['Height (inches)']
		player['experience'] = row['Soccer Experience']
		player['guardian'] = row['Guardian Name(s)']

		players.append(player)

	count_experpienced_players(players)

#---------------------------------------------------------------------------------#

# function below receives a list of all players and then finds the experienced players
# and adds them to a new list called experienced_players. Also if a player does not have
# then it will be added to the non_experienced_players list

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

	divide_players(experienced_players, non_experienced_players, players)

#---------------------------------------------------------------------------------#
#function below divide players equally and adds then to three lists (sharks, dragons and raptors)

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
		elif len(dragons) != number_of_players_per_team:
			dragons.append(player)
		else:
			raptors.append(player)

	save_to_file(sharks,dragons,raptors)

#---------------------------------------------------------------------------------#
#function below saves information about players in team.txt file

def save_to_file(sharks, dragons, raptors):

	with open('teams.txt', 'a') as file:
		file.seek(0) # start from the begining of the files
		file.truncate() # remove all data from a file

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
	create_welcome_letters(all_players, sharks, dragons, raptors)

#---------------------------------------------------------------------------------#
# function below creates a welcome letter for each player

def create_welcome_letters(all_players, sharks, dragons, raptors):

	for player in all_players:
		name = player['name'].lower() # name of the player 
		index = name.index(' ') # to find the index of the space between first and last name
		#create a file name using player's name
		file_name = name[:index] + '_' + name[index+1:] + '.txt'

		team_name = ''

		if player in sharks:
			team_name = 'Sharks'

		if player in dragons:
			team_name = 'Dragons'

		if player in raptors:
			team_name = 'Raptors'

		header = 'Dear ' + player['guardian'] + ',\n'
		body = 'We would like to inform you that ' + player['name'] + ' has joined the ' + team_name + ' and the first practice will be  on July 07, 2017\n'
		end = '\nThank you,\nYoussef'

		letter =  header + body + end
		with open(file_name, 'w') as file_object:
			file_object.write(letter)
	
#---------------------------------------------------------------------------------#

if __name__ == "__main__":
    with open('soccer_players.csv') as file_object:
        read_csv_file(file_object) 



