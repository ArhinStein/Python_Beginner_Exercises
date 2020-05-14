players = ['Charles', 'Martin', 'Micheal', 'Flavio', 'Dinho']
print(players[0:3])
print(players[2:])
print(players[:2])
print(players[:])

#Looping Through a Slice
#We are looping through same list above
print("This is the best of the of the best:")
for player in players[-3:]:
    print(player.upper())