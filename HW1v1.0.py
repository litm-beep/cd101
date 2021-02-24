composers=[]
num = int(input('\nEnter the number of composers: '))
for i in range(num):
    composers.append([0]*5)
    print(f'\nEnter info about composer №{i + 1}')
    composers[i][0] = input('First Name: ')
    composers[i][1] = input('Last Name: ')
    composers[i][2] = int(input('Year of birth: '))
    composers[i][3] = int(input('Year of death: '))
    composers[i][4] = composers[i][3] - composers[i][2]

mean_age = 0
print('\nInfo about composers:')
for i in range(num):
    mean_age += composers[i][4]
    print(f'First Name: {composers[i][0]},\tLast Name: {composers[i][1]},\tAge: {composers[i][4]}')
print(f'\nMean age of composers is {mean_age/num}')