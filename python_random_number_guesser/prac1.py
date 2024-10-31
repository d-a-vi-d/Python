import random
random_max = int(input('Obergrenze der Zufallszahl >> '))
print('____________________________')
random_number = random.randrange(random_max)
top = random_max
bottom = 0
while True:
#    number = input('Gib mir eine Zahl zwischen ' + str(bottom) + ' und ' + str(top) + ' >> ')
    number = round((top + bottom)/2, ndigits=None)
    print(number)
    print('____________________________')
    try:
            if int(number) == int(random_number):
                print('Macher!', number, 'war die gesuchte Zahl!')
                break
            elif int(number) > int(random_number):
                print('Nicht so viellll!!')
                top = number
            elif int(number) < int(random_number):
                print('Gib mir meehhhrrr!!')
                bottom = number
    except:
            print('Du hast an Scheiß gebaut, probiers nu moi!')