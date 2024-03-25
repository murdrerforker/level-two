name = {
    'first name': 'seun',
    'second name': 'ayo',
    'last name': 'ologuneru'
}

user_input = input('ENTER THE CORRESPONDING NAME: ')

if user_input in name.values():  
    for key, value in name.items():
        if user_input == value:
            print('Corresponding name:', key)
            break 
else:
    print('404!!!')

