ansOne, ansTwo,ansThree,ansFour,ansFive =0,0,0,0,0

print("Set 1: (1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31)")
setOne = input("Is your birthday in this set\n").upper()
if setOne == "Y":
	ansOne =1

print("Set 2: (2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31)")
setTwo = input("Is your birthday in this set\n").upper()
if setTwo == "Y":
	ansTwo =1

print("Set 3: (4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31)")

setThree = input("Is your birthday in this set\n").upper()
if setThree == "Y":
	ansThree =1

print("Set 4: (8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31)")
setFour = input("Is your birthday in this set\n").upper()
if setFour == "Y":
	ansFour =1

print("Set 5: (16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31)")
setFive = input("Is your birthday in this set\n").upper()
if setFive == "Y":
	ansFive =1

ans = ((2**0)*ansOne + (2**1)*ansTwo + (2**2)*ansThree + (2**3)*ansFour + (2**4)*ansFive)
print(ans)
