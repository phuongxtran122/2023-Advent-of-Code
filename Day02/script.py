import re
# Open input text file and put into array of strings
f = open("input.txt", "r")
lines = f.readlines()
listOfLines = []

# Strips the newline character and the "Game ID:" part
for line in lines:
    listOfLines.append((line.split(":")[1]).strip())

# --------------------------------- Q1 ----------------------------------------
# Find if these games are valid by checking if the number of cubes are more
# than the cubes available.
# Cubes available:
# red = 12
# green = 13
# blue = 14
# cubesSum = red + green + blue

# # return idSum as answer
# idSum = 0

# curID = 1
# # NOTE: Game ID starts at 1, not 0
# # EXAMPLE: '4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue'
# for x in range(len(listOfLines)):
#     games = listOfLines[x].split("; ")
#     for y in range(len(games)):
#         # ['4 red, 5 blue, 9 green', '7 green, 7 blue, 3 red'...etc]
#         colors = games[y].split(", ")
#         print (colors)
#         temp_red = 0
#         temp_green = 0
#         temp_blue = 0
#         for color in colors:
#             if ('red' in color):
#                 temp_red += int(re.search(r'\d+', color).group())
#                 if (temp_red > red):
#                     break
#             elif ('green' in color):                
#                 temp_green += int(re.search(r'\d+', color).group())
#                 if (temp_green > green):
#                     break
#             elif ('blue' in color):
#                 temp_blue += int(re.search(r'\d+', color).group())
#                 if (temp_blue > blue):
#                     break
#         total = temp_blue+temp_green+temp_red
#         if (temp_blue > blue or temp_red > red or temp_green > green or total > cubesSum):
#             break
#         if len(games)-1 == y:   
#             idSum += curID 
#     print ("Current Game ID:", curID)
#     print("Sum of Valid games:",idSum)
#     print ("---------------------------")
#     curID += 1

# --------------------------------- Q2 ----------------------------------------
# Find the least amount of cubes needed to play a game. Multiple the color
# cubes and add together.
total = 0
for x in range(len(listOfLines)):
    games = listOfLines[x].split("; ")
    temp_red = []
    temp_green = []
    temp_blue = []        
    for y in range(len(games)):
        # ['4 red, 5 blue, 9 green', '7 green, 7 blue, 3 red'...etc]
        colors = games[y].split(", ")
        print (colors)
        for color in colors:
            if ('red' in color):
                temp_red.append(int(re.search(r'\d+', color).group()))
                
            elif ('green' in color):                
                temp_green.append(int(re.search(r'\d+', color).group()))
                
            elif ('blue' in color):
                temp_blue.append(int(re.search(r'\d+', color).group()))
    if not temp_red:
        temp_red.append(0)
    if not temp_green:
        temp_green.append(0)
    if not temp_blue:
        temp_blue.append(0)
    total += max(temp_red) * max(temp_green) * max(temp_blue)   
    print("Red:",temp_red, "--->", max(temp_red))
    print("Green:",temp_green, "--->", max(temp_green))
    print("Blue:",temp_blue, "--->", max(temp_blue))
    print ("Total:", total)
    print ("---------------------------")

