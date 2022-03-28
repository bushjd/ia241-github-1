'''
lab 5
'''

#3.1
alien_color= 'yellow'

if alien_color == 'green':
    print('you have earned 5 points')
    
#3.2
alien_color= 'red'

if alien_color == 'green':
    print('you have earned 5 points')
    
else:
    print('you have earned 10 points')
    
#3.3
favorite_fruits = ['pineapple', 'orange', 'apple' ]

if 'pineapple' in favorite_fruits: 
    print('Wow, you really like pineapple')
    
if 'orange' in favorite_fruits:
    print('Wow, you really like Oranges')
    
if 'apple' in favorite_fruits:
    print ('Wow, you really like apples')
    
#3.4
age = 30


if age <= 10:
    print('Person is a Kid')
elif 10<age<=20 :
    print('Person is a teenager')
else:
    print('Person is an adult')
    
    if age>65:
        print('Person is an elder')
