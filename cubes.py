RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

color = {
    'red' : 3,
    'blue' : 4,
    'green' : 5
}

def possible(input):
    red = 0
    blue = 0
    green = 0

    i = 0
    line_sum = ""
    while (input[5+i].isnumeric()):
        line_sum += input[5+i]
        i+=1
    
    string = ""

    temp = input.replace("Game " + line_sum + ": ", '')

    for char in temp:

        if char == ';':
            red = 0
            blue = 0
            green = 0
            continue

        if char == ',' or char == ' ':
            continue
        string += char

        if 'red' in string:
            i = 0
            red_temp = ""
            while (string[i].isnumeric()):
                red_temp += string[i]
                i+=1
            red += int(red_temp)
            string = ""

        if 'green' in string:
            i = 0
            green_temp = ""
            while (string[i].isnumeric()):
                green_temp += string[i]
                i+=1
            green += int(green_temp)
            string = ""

        if 'blue' in string:
            i = 0
            blue_temp = ""
            while (string[i].isnumeric()):
                blue_temp += string[i]
                i+=1
            blue += int(blue_temp)
            string = ""

        print("red: " + str(red) + " blue: " + str(blue) + " green: " + str(green))

        if int(red) > RED_MAX or int(green) > GREEN_MAX or int(blue) > BLUE_MAX:
            line_sum = 0
            return line_sum
    
    return line_sum

file1 = open('cubes.txt', 'r')

sum = 0
for line in file1:

    sum += int(possible(line.strip()))

print(sum)