"""
You are going to write a program that will mark a spot with an X.

Your job is to write a program that allows you to mark a square on 
the map using a two-digit system. The first digit is the vertical
column number and the second digit is the horizontal row number.

So if user input 23 to mark, which is 2nd column and 3rd row...
 then it actually means map[2][1]
"""


#basic and input
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


#Code to achive same

position = str(position)
first = int(position[0])
sec = int(position[1])
map[sec -1][first -1] = "X"


print(f"{row1}\n{row2}\n{row3}")

