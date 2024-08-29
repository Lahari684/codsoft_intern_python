Game=["Rock","Paper","Scissors"]
for i in Game:
    print(i)
print("Please select single option each from the above list")
p1=input("P1 Enter your option : ")
p2=input("P2 Enter your option : ")
if p1=="Paper" and p2=="Rock":
    print("P1 won")
elif p1=="Paper" and p2=="Scissors":
    print("P2 won")
elif p1=="Rock" and p2=="Paper":
    print("P2 won")
elif p1=="Rock" and p2=="Scissors":
    print("P1 won")
elif p1=="Scissors" and p2=="Paper":
    print("P1 won")
elif p1=="Scissors" and p2=="Rock":
    print("P2 won")
elif p1 and p2 =="Rock":
    print("Not valid")
elif p1 and p2 =="Paper":
    print("Not valid")
elif p1 and p2 =="Scissors":
    print("Not valid")
