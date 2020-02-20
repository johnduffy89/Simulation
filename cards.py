import random


def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        j = random.randint(0,i+1)
        arr[i],arr[j] = arr[j, arr[i]



        value = str(j)
        if(i == 0):
            suit = "spade"
        if(j==11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        elif(j == 1):
            value = "A"
       

def deal():
    deck = []
    suit = ["♠", "♥", "♣", "♦"]
    f= {1:"A", 11: "J", 12: "Q", 13: "K"}
    for i in range(4):
        for j in range(1,14):                       
            deck.append(f"{value}{suits[i]}")
    return d


    cards = deal()
    print("Before Shuffle: ")
    print(cards)


    shuffle (cards)
    print("After Shuffle:")
    print (cards)
