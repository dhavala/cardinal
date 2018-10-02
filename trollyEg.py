


trelloKey = "33dc558719319edbe1819e9bb185d746"
trelloToken = "ecc1c9a94ef618b832be000f7b74c5e05779d44cef0101ce16a2c2631bcd9d9a"


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
