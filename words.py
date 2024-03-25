number = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
    '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

user= input('Enter your number: ')


word = " ".join(number[digit] for digit in user if digit in number) 

print('Number in words:', word)
