



import trolly
trelloKey = "YOUR_KEY"
trelloToken = "YOU_TOKEN"
client = trolly.client.Client(trelloKey, trelloToken)
for myboard in client.get_boards():
	print('board: '+ myboard.name+'\n');
	for mylist in myboard.get_lists():
		print('\t'+'list:'+mylist.name+'\n');
    	for card in mylist.get_cards():
    		info = card.get_card_information();
    		print('\t\t'+info['name']+'\n');
    		#print('\t\t'+info['name']+' - '+ info['desc']+'\n');
