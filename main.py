print('Welcome to the secret bidding auction!')
bidDict = {}

def newEntry():
    name = input('Enter name: ')
    bidPrice = input('Enter Bid Price: $')
    bidDict[name] = bidPrice
    return bidDict

bidDict = newEntry()

auctionStatus = 0
while auctionStatus == 0:
    cont = input('Would you like to add another bidder? (y/n) ')
    if cont.lower() == "y":
        bidDict = newEntry()
    elif cont.lower() == "n":
        auctionStatus += 1
    else:
        print('Invalid response.')

highest = ["name", "0"]
for key in bidDict:
    if int(bidDict[key]) > int(highest[1]):
        highest[0] = key
        highest[1] = bidDict[key]

print(f'Winner is {highest[0]}!')