#A program that selects a card from a deck and adds it to a list

#Strings for output
heart = ' of hearts'
club = ' of clubs'
diomond = ' of diamonds'
spade = ' of spades'

ace = 'ace'
jack = 'jack'
queen = 'queen'
king = 'king'

yourHand = '\nYour hand is now: '
errorMsg = '\nYour entry was out of bounds. Please try again. '

#lists for hands and deck
handArray = []
cardArray = [ ace + heart , '2' + heart, '3' + heart, '4' + heart,
             '5' + heart, '6' + heart, '7' + heart, '8' + heart,
             '9' + heart, '10' + heart, jack + heart, queen + heart, king + heart,
              ace + club, '2' + club, '3' + club, '4' + club,
             '5' + club, '6' + club, '7' + club, '8' + club,
             '9' + club, '10' + club, jack + club, queen + club, king + club,
              ace + diomond , '2' + diomond, '3' + diomond, '4' + diomond,
             '5' + diomond, '6' + diomond, '7' + diomond, '8' + diomond,
             '9' + diomond, '10' + diomond, jack + diomond, queen + diomond, king + diomond,
              ace + spade , '2' + spade, '3' + spade, '4' + spade,
             '5' + spade, '6' + spade, '7' + spade, '8' + spade,
             '9' + spade, '10' + spade, jack + spade, queen + spade, king + spade,
              ]
#counter
choiseCount = 0

#Main loop
while True:

    #Validate input, add to hand, print as set to avoid duplicate cards
    try:
        cardChoise = int(input("\nPlease choose an integer between 1 - 52. Press 0 to exit. "))
    
        if cardChoise == 0:#End program

            break

        elif cardChoise > 52 or cardChoise < -52:#Out of bounds

            print(errorMsg)

        elif cardChoise < 0 and cardChoise > -53: #Remove card from hand

            tempCard = cardArray[(abs(cardChoise) - 1)]
            print('Removing', tempCard)
            handArray.remove(tempCard)
        #elif cardChoise < -53:

        #    print(errorMsg)
                        
        else:
            if cardArray[cardChoise - 1] in handArray:
                print('\n Card already in hand')
                continue

            handArray.append(cardArray[cardChoise - 1])
            choiseCount = choiseCount + 1
        
        print(set(handArray))

    except ValueError:
        print(errorMsg)
        
