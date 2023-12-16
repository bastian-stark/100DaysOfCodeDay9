#Secret Bidding Auction App

#Intro
print('Welcome to the secret bidding auction!')
bidDict = {}

def newEntry():
    """Create new user entry"""
    name = input('Enter name: ')
    bidPrice = input('Enter Bid Price: $')
    bidDict[name] = bidPrice
    return bidDict

bidDict = newEntry()
auctionStatus = 0
#Begin auction
while auctionStatus == 0:
    #Add users to auction
    cont = input('Would you like to add another bidder? (y/n) ')
    if cont.lower() == "y":
        bidDict = newEntry()
    elif cont.lower() == "n":
        auctionStatus += 1
    else:
        print('Invalid response.')

#Compare bids
highest = ["name", "0"]
for key in bidDict:
    if int(bidDict[key]) > int(highest[1]):
        highest[0] = key
        highest[1] = bidDict[key]

print(f'Winner is {highest[0]}!')
