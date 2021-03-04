def age(birth, death):
    if death > birth:
        return death - birth
    else:
        return 0

def middle_age(ages, number):
    mid = 0
    for i in range(number):
        mid += ages[i]
    return mid / number


composers = []
compos_ages = []

num = 0
sum = 0

while True:
    
    answer = input("\nDo you want to enter info about new composer?\nPlease write 'no' if you don't\nor write any symbols if you want:\n")
    if answer == 'no': 
        break

    composers.append([0]*4)
    print(f'\nComposer №{num + 1}')
    composers[num][0] = input('First Name: ')
    composers[num][1] = input('Last Name: ')
    composers[num][2] = int(input('Year of birth: '))
    composers[num][3] = int(input('Year of death: '))

    compos_ages.append([0])
    compos_ages[num] = int(age(composers[num][2], composers[num][3]))

    num += 1


if num == 0:
    print("You don't give any information ಠ.ಠ")
else:
    print('\nInfo about composers:')
    for i in range(num):
        print(f'First Name: {composers[i][0]},\tLast Name: {composers[i][1]},\tAge: {compos_ages[i]}')
    print(f'\nMiddle age of composers is {round(middle_age(compos_ages, num), 1)}\n')

    print("\nDictionary results:\n")
    compos_dict = dict()
    for i in range(num):
        compos_dict[composers[i][0]] = [composers[i][1], composers[i][2], composers[i][3], compos_ages[i]]
    for key, val in compos_dict.items():
        print(key, val)
    
