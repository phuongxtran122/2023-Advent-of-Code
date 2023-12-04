f = open("input-q1.txt", "r")
lines = f.readlines()
listOfLines = []
# Strips the newline character
for line in lines:
    listOfLines.append(line.strip())
# print(listOfLines[1])

numbersList = {
        "one": "1", 
        "two" : "2", 
        "three" : "3", 
        "four" : "4", 
        "five" : "5", 
        "six" : "6", 
        "seven" : "7", 
        "eight" : "8", 
        "nine" : "9"
    }


# ---------------PART 1 --------------------- #
result = 0
for x in range(len(listOfLines)):
    digits = ""
    isWord = ""
    print("Word: ", (listOfLines[x]))
    for letter in listOfLines[x]:
        # if int, add it to digits and reset word
        if (letter.isdigit()):
        
            digits += letter
            isWord = ""
        else:
            isWord +=letter
            for key in numbersList:
                if key in isWord:
                    digits += numbersList[key]
                    isWord = ""
                    break
    print("--Digits: ", (digits, int(digits[0]+digits[len(digits)-1])))
    result += int(digits[0]+digits[len(digits)-1]) 
    # listOfLines[x] = digits

# result = 0
# for x in listOfLines:
#     # print("This is the number:" + (x[0]+x[len(x)-1]))
#     result1 = result
#     result += int(x[0]+x[len(x)-1]) 
#     # print("%d + %d = %d" % (result1,int(x[0]+x[len(x)-1]), result)) 

print(result)
    

