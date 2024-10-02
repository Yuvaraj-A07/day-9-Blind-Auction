from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the secret auction program")
auction_list = {}
yes=True
while(yes):
  name=input("what is your name?:")
  bid=int(input("what's your bid?: $"))
  auction_list[name]=bid
  others=input("Are there any other bidders? Type 'yes' or 'no'\n")
  if(others=='yes'):
    yes=True
    clear()
  else:
    clear()
    key_list=list(auction_list.keys())
    value_list=list(auction_list.values())
    win_bid=max(auction_list.values())
    win_name=value_list.index(win_bid)
    
    print(f"The winner is {key_list[win_name]} with a bid of ${win_bid}")
    yes=False
