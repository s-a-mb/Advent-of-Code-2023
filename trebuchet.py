nums = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8, 
    "nine" : 9
}

def calibrate(input):
    output = ""
    last = ""
    check = False
    string = ""
    temp = ""
    for char in input:
        string += char
        for key, val in nums.items():
            if key in string:
                #print(string)
                if check is True:
                    last = str(val)
                else:
                    output = str(val)
                    check = True    
                temp = string.replace(str(key), '' + str(key)[-1])
                string = temp
                
        if char.isnumeric() and check is True:
            last = char
        if char.isnumeric() and check is False:
            output = char
            check = True
    
    if last == "":
        output += output
    else:
        output += last

    #print(output)
    return output

file1 = open('trebuchet.txt', 'r')

sum = 0

for line in file1:
    sum += int(calibrate(line.strip()))

print(sum)