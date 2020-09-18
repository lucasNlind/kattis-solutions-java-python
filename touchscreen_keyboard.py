keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']

def letter_to_coordinate(letter):
    rtn = []
    if letter in keyboard[0]:
        rtn.append(0)
        rtn.append(keyboard[0].index(letter))
    elif letter in keyboard[1]:
        rtn.append(1)
        rtn.append(keyboard[1].index(letter))
    elif letter in keyboard[2]:
        rtn.append(2)
        rtn.append(keyboard[2].index(letter))  
    return rtn

def alphabetical_sort(my_list):
    k = 0
    while k < len(my_list) - 1:
        if my_list[k][0] == my_list[k + 1][0] and my_list[k][1] > my_list[k + 1][1]:
            temp = my_list[k]
            my_list[k] = my_list[k + 1]
            my_list[k + 1] = temp
        k += 1
    return my_list

final = []
cases = int(input())

while cases > 0:
    word, entries = input().split()
    entries = int(entries)
    wordList = list(word)
    pairs = []
    finalC = 0

    while entries > 0:
        sum = 0
        i = 0
        case = input()
        for c in case:
            letter_OG = letter_to_coordinate(wordList[i])
            letter_case = letter_to_coordinate(c)
            sum += abs(letter_OG[0] - letter_case[0]) + abs(letter_OG[1] - letter_case[1])
            i += 1
        pairs.append([sum, case])
        sortosi = sorted(pairs)
        sortosi = alphabetical_sort(sortosi)
        entries -= 1
    final.append(sortosi)
    cases -= 1

for casio in range(len(final)):
    for el in final[casio]:
        print(el[1] + " " + str(el[0]))

