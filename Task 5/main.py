import random
hearts=['AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH']
spades=['AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS']
diamonds=['AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD']
clubs=['AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC']

all_cards=hearts+spades+diamonds+clubs

random.shuffle(all_cards)

print("""
Creating pack of cards ...
Shuffling and Dealing ...\n""")

# print(all_cards,end="")



print("East--> {}".format(all_cards[0:52:4]))
print("West--> {}".format(all_cards[1:52:4]))
print("North--> {}".format(all_cards[2:52:4]))
print("South--> {}".format(all_cards[3:52:4]))


print("Looking for the Ace of Spades ...")

index=all_cards.index("AS")
# print(index)


if index in range(0,52,4):
    print("East player has it!")
elif index in range(1,52,4):
    print("West player has it!")
elif index in range(2,52,4):
    print("North player has it!")
else:
    print("South player has it!")