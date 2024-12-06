#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"

def createDeck():
  deck=[]
  for rank in ranks:
    for suit in suits:
      deck.append(rank + suit)
  return deck

def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1


if __name__ == "__main__":
  main()
ranks = "A23456789TJQK"
suits = "CDHS"

def createDeck():
  cardlist = [ranks[i]+suits[j] for i in range(len(ranks)) for j in range (len(suits))]
  return cardlist

def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1


if __name__ == "__main__":
  main()