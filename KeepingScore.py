'''
A = 4
K = 3
Q = 2
J = 1
void = 3
singleton = 2
doubleton = 1
'''

suits = {"D": "Clubs", "H": "Diamonds", "S": "Hearts"}
royals = {"A": 4, "K": 3, "Q": 2, "J": 1}
pointsBasedOnLength = {"0": 3, "1": 2, "2": 1}

hand = input()
print(f"Cards Dealt   Points")
cardsInSuit = []
suitPoints = 0
totalPoints = 0
for i in range(1, 17):
    currentLetter = hand[i]
    cardsInSuit.append(currentLetter)
    if currentLetter in royals.keys():
        suitPoints += royals[currentLetter] # adding points if the current letter is A, K, Q, or J
    elif currentLetter in suits.keys(): # checking if the suit has changed
        cardsInSuit.pop()
        if str(len(cardsInSuit)) in pointsBasedOnLength.keys():
            suitPoints += pointsBasedOnLength[str(len(cardsInSuit))]
        totalPoints += suitPoints
        print(f"{suits[currentLetter]}  {" ".join(cardsInSuit)}  {suitPoints}")
        cardsInSuit.clear()
        suitPoints = 0

if str(len(cardsInSuit)) in pointsBasedOnLength.keys():
            suitPoints += pointsBasedOnLength[str(len(cardsInSuit))]    
print(f"Spades {" ".join(cardsInSuit)}  {suitPoints}")
totalPoints += suitPoints
print(f"  Total {totalPoints}")