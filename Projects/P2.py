#begining
carti_points = 0
nettspend_points = 0

answer = input("Would you rather play A)play fortnite, or B)play basketball?\n")
if answer == "A" :
    nettspend_points += 1
elif answer == "B":
    carti_points += 1


answer = input("Would you rather A)skip drivers ed, or B)learn how to drive normally\n")
if answer == "A" :
    nettspend_points += 1
elif answer == "B":
    carti_points += 1


#middle
answer = input("Would you rather A)do money spreads, or B)be smart with your money?\n")
if answer == "A" :
    nettspend_points += 1
elif answer == "B":
    carti_points += 1

answer = input("Would you rather A)meet kendrick lamar, or B)meet drake?\n")
if answer == "B" :
    nettspend_points += 1
elif answer == "A":
    carti_points += 1

answer = input("Would you rather A)Watch skibidi toilet, or B)watch basketball highlights?\n")
if answer == "A" :
    nettspend_points += 1
elif answer == "B":
    carti_points += 1


if carti_points > nettspend_points:
    print("you are a carti fan!")
elif nettspend_points > carti_points:
    print("you are a nettspend fan!")
#end