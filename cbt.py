score = 0
test = (
  ('c', '1. what is the capital city of Gombe a) Kano b) Kanuri c) Gombe d) Ibadan'),
  ('a', '2. what is the capital city of Lagos a) Ikeja b) Ketu c) Oworo d) Alimosho'),
  ('c', '3. what is the capital city of Nigeria a) Lagos b) Gombe c) Abuja d) Ibadan'),
  ('d', '4. what is the capital city of Oyo a) Kano b) Kanuri c) Gombe d) Ibadan'),
  ('a', '5. what is the capital city of Kano a) Kano b) Kanuri c) Gombe d) Ibadan'),
  ('a', '6. what is the capital city of Ondo a) Akure b) Dutse c) Enugu d) Osogbo'),
  ('b', '7. what is the capital city of Jigawa a) Akure b) Dutse c) Enugu d) Osogbo'),
  ('c', '8. what is the capital city of Enugu a) Akure b) Dutse c) Enugu d) Osogbo'),
  ('d', '9. what is the capital city of Osun a) Akure b) Dutse c) Enugu d) Osogbo'),
  ('d', '10. what is the capital city of Imo a) Akure b) Dutse c) Enugu d) Owerri'),
    
 )
for answer , question in test :
    total_question = len(test)
    print(question)
    option = input('input your answer>>> ')
    if option == " " :
     print('Kindly input your option')
    elif option == answer :
     score =+1
print(f'your score = {score}/{total_question}')
    
    