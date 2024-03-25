score = 0
test = {
    '1': {'question': 'what is the capital city of Gombe a) Kano b) Kanuri c) Gombe d) Ibadan', 'answer': 'c'},
    '2': {'question': 'what is the capital city of Lagos a) Ikeja b) Ketu c) Oworo d) Alimosho', 'answer': 'a'},
    '3': {'question': 'what is the capital city of Nigeria a) Lagos b) Gombe c) Abuja d) Ibadan', 'answer': 'c'},
    '4': {'question': 'what is the capital city of Oyo a) Kano b) Kanuri c) Gombe d) Ibadan', 'answer': 'd'},
    '5': {'question': 'what is the capital city of Kano a) Kano b) Kanuri c) Gombe d) Ibadan', 'answer': 'a'},
    '6': {'question': 'what is the capital city of Ondo a) Akure b) Dutse c) Enugu d) Osogbo', 'answer': 'a'},
    '7': {'question': 'what is the capital city of Jigawa a) Akure b) Dutse c) Enugu d) Osogbo', 'answer': 'b'},
    '8': {'question': 'what is the capital city of Enugu a) Akure b) Dutse c) Enugu d) Osogbo', 'answer': 'c'},
    '9': {'question': 'what is the capital city of Osun a) Akure b) Dutse c) Enugu d) Osogbo', 'answer': 'd'},
    '10': {'question': 'what is the capital city of Imo a) Akure b) Dutse c) Enugu d) Owerri', 'answer': 'd'}
}
total_questions = len(test)
for number, question in test.items():
    print(question['question'])
    option = input('Input your answer>>> ')
    if option == "":
        print('Kindly input your option')
    elif option.lower() == question['answer']:
        score += 1
print(f'Your score = {score}/{total_questions}')
