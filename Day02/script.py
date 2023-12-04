# Open input text file and put into array of strings
f = open("input.txt", "r")
lines = f.readlines()
listOfLines = []

# Strips the newline character and the "Game ID:" part
for line in lines:
    listOfLines.append((line.split(":")[1]).strip())

# Q1
red = 12
green = 13
blue = 14
cubesSum = red + green + blue

# return idSum as answer
idSum = 0

curID = 1
# NOTE: Game ID starts at 1, not 0
# EXAMPLE: '4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue'
for x in range(len(listOfLines)):
    games = listOfLines[x].split(";")
    print(games)