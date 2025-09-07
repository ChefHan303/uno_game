'''
author: Ethan Han
UNO game
creates a game of uno between the user and a CPUs
'''

import random

#combined list of all the player's decks
user_decks = []
#includes the user's names and their respective deck
complete_user_decks = []

#other gerneal variables
COLORS = ["Red","Blue","Yellow","Green"]
NUMBERS = list(range(10))
SPECIAL_CARDS = ["plus_two","plus_four","wild"]
uno_deck = []



#runs the actual games
def game_loop():
	num_players_left = len(user_decks)
	starting_position, starting_card = game_setup()

	while num_of_players >= num_players_left:




#creates a new list that'll contain the player's name and their respective deck
def add_names():
	for i in range(len(user_decks)):
		name = input(f"player number: {i}.\nPlease enter your name:")
		player_data = (name, user_decks[i])
		complete_user_decks.append(player_data)
	


#creates the uno deck of cards
def create_deck():

	#adds the colored cards to the deck
	for color in COLORS:
		for number in NUMBERS:
			card = (color, number)
			uno_deck.append(card)

	#adds the wild cards to the deck
	for special_card in SPECIAL_CARDS:
		card = ("Black", special_card)
		uno_deck.append(card)


#sets up the fist player and card of the game
def game_setup():
	starting_position = random.randint(0, num_of_players-1)
	starting_card = uno_deck[random.randint(0,len(uno_deck) -1)]
	if starting_card[0] == "Black":
		starting_card = uno_deck[random.randint(0,len(uno_deck) -1)]
	return starting_position, starting_card



#will generate a starting hand for the user and the computers
def create_hands():
	global num_of_players
	num_of_players = eval(input("How many players are playing?: "))

	for i in range(num_of_players):
		temp_deck = []
		#shuffles deck once before dealing to each player
		random.shuffle(uno_deck)

		for j in range(7):
	 		rand_num = random.randint(0, len(uno_deck) - 1)
	 		temp_deck.append(uno_deck[rand_num])

		user_decks.append(temp_deck)


	







def play_game():
	create_deck()
	create_hands()
	add_names()
	game_loop()




play_game()


#finished making the deck of uno cards and making each individual player's hands.
#and setting up who the first to play player is and the starting card
#now need to work on making the game loop

