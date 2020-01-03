from random import randint

class Deck():
	
	def __init__(self):
		self.Cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]*4

	def Return_Card(self):
		x=randint(1,14)

		while(x not in self.Cards):
			x=randint(1,14)

		self.Cards.remove(x)

		print("The Card taken from the deck was {}".format(x))

		return x

class Hand():

	def __init__(self):
		
		self.In_Hand=[]

	def Add_Card(self,x):
		
		self.In_Hand.append(x)
		self.In_Hand.sort()

	def Sum(self):
        
		sum=0

		for i in self.In_Hand:
			if((i==10) or (i==11) or (i==12)):
				sum+=10

			elif(i==13):
				if(sum+10>21):
					sum+=1
				else:
					sum+=10

			else:
				sum+=i

		return sum

class Player_Balance():

	def __init__(self):
		self.Balance=0

	def Add_Balance(self,x):
		self.Balance+=x

	def Bid(self,x):

		if(self.Balance>=x):
			self.Balance-=x
			return True

		else:
			print("Not Enough Balance.")
			return False

PBalance=Player_Balance()

b=int(input("How much money do you want to add to your balance ?"))
PBalance.Add_Balance(b)


while True:

	print(f"Your current Balance is : {PBalance.Balance}")

	print("How much do you want to bid ?")

	x=int(input())


	while(not(PBalance.Bid(x))):
		print("Do you want to add more balance ? (Y/N)")
		y=input()

		if(y.upper()=='Y'):
			print("How much balance do you want to add ?")
			z=int(input())

			PBalance.Add_Balance(z)
			print(f"Your current Balance is : {PBalance.Balance}")

		x=int(input("How much do you want to bid ?"))

	print(f"Your current Balance is : {PBalance.Balance}")

	Game_Deck=Deck()

	Player_Hand=Hand()

	Computer_Hand=Hand()

	print("Drawing the player's hand from the deck :")

	Player_Hand.Add_Card(Game_Deck.Return_Card())

	Player_Hand.Add_Card(Game_Deck.Return_Card())

	print(f"The current sum of the Player's hand is : {Player_Hand.Sum()}")

	print("\n"*3)

	print("Drawing the computer's hand from the deck :")

	Computer_Hand.Add_Card(Game_Deck.Return_Card())
	print("The other card taken out for the computer is hidden.")

	print(f"The current known sum of the computer's hand is : {Computer_Hand.Sum()}")

	Player_Lost=0



	print("Player's Turn:")

	while(Player_Hand.Sum()<=Computer_Hand.Sum()):
		print("You can't stay. Drawing Card.")
		Player_Hand.Add_Card(Game_Deck.Return_Card())
		print(f"The current sum of the Player's hand is : {Player_Hand.Sum()}")
		print("\n"*3)

	while True:

		print("Do you want to Hit or Stay ? (H/S)")

		z=input()

		if(z.upper()=='H'):
			Player_Hand.Add_Card(Game_Deck.Return_Card())

			print(f"The current sum of the Player's hand is : {Player_Hand.Sum()}")
			print("\n"*3)

			if(Player_Hand.Sum()>21):
				Player_Lost=1
				break

		if(z.upper()=='S'):
			print(f"The final sum of the Player's hand is : {Player_Hand.Sum()}")
			print("\n"*3)
			break

	if(Player_Lost==1):
		print("BUST : Player Loses")
		k=input("Do you want to play again ? (Y/N)")

		if(k.upper()=='Y'):
			continue

		else:
			break

	print("For the hidden card in computer's hand :")
	Computer_Hand.Add_Card(Game_Deck.Return_Card())
	print(f"The current sum of the computer's hand is : {Computer_Hand.Sum()}")
	print("\n"*3)

	if(Computer_Hand.Sum()>Player_Hand.Sum()):
		print("Computer wins.")
		k=input("Do you want to play again ? (Y/N)")

		if(k.upper()=='Y'):
			continue

		else:
			break

	while(Computer_Hand.Sum()<=Player_Hand.Sum()):
		print("The computer is drawing card.")
		Computer_Hand.Add_Card(Game_Deck.Return_Card())
		print(f"The current sum of the Computer's hand is : {Computer_Hand.Sum()}")
	
	print("\n"*3)

	if(Computer_Hand.Sum()>21):
		print("Computer BUSTS : Player Wins")
		PBalance.Add_Balance(2*x)
		k=input("Do you want to play again ? (Y/N)")

		if(k.upper()=='Y'):
			continue

		else:
			break

	else:
		print("Computer wins.")
	
		k=input("Do you want to play again ? (Y/N)")

		if(k.upper()=='Y'):
			continue

		else:
			break

















