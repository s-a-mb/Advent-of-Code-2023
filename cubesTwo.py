
def powers(input):
    red = 0
    blue = 0
    green = 0
    red_min = 0
    blue_min = 0
    green_min = 0

    i = 0
    line_sum = ""
    while (input[5+i].isnumeric()):
        line_sum += input[5+i]
        i+=1
    
    string = ""

    input = input.replace("Game " + line_sum + ": ", '')

    for char in input:

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
            red_min = max(red, red_min)

        if 'green' in string:
            i = 0
            green_temp = ""
            while (string[i].isnumeric()):
                green_temp += string[i]
                i+=1
            green += int(green_temp)
            string = ""
            green_min = max(green_min, green)

        if 'blue' in string:
            i = 0
            blue_temp = ""
            while (string[i].isnumeric()):
                blue_temp += string[i]
                i+=1
            blue += int(blue_temp)
            string = ""
            blue_min = max(blue, blue_min)

    power = red_min * blue_min * green_min
    return power

file1 = open('cubes.txt', 'r')

sum = 0
for line in file1:

    sum += int(powers(line.strip()))

print(sum)