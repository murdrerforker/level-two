weight = (input('enter your weight in lbs or kg>>>   '))
if weight.endswith('kg') :
    s_weight = weight.split('kg')
    
    in_pounds = (weight * 2.204,'lbs')
    print(in_pounds)
elif weight.endswith('lbs') :
    in_kg = (weight * 0.450,'kg')
    print(in_kg)





# in_kg = 0.453592 * weight



# print(in_kg,'kg')