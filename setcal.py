


print("""
      1.    Union
      2.    intersection
      3.    Difference
      4.    Symmetric Difference
      5.    Subset
      6.    Superset
      7.    Exit
      """
   )

Dat_one = ('Ade','Bayo','Dele','Sege','Toyo')
Dat_two = ('Ola','Ade', 'Matthew' ,'Ishola','Toyo')


Data_one = set(Dat_one)
Data_two = set(Dat_two)

option = input('enter your type data>>>   ')
if option == '1':
        result = Data_one.union(Data_two)
        print("Union:", result)
elif option == '2':
        result = Data_one.intersection(Data_two)
        print("Intersection:", result)
elif option == '3':
        result = Data_one.difference(Data_two)
        print("Difference:", result)
elif option== '4':
        result = Data_one.symmetric_difference(Data_two)
        print("Symmetric Difference:", result)
elif option == '5':
        if Data_one.issubset(Data_two):
            print("Set 1 is a subset of Set 2")
        else:
            print("Set 1 is not a subset of Set 2")
elif option == '6':
        if Data_one.issuperset(Data_two):
            print("Set 1 is a superset of Set 2")
        else:
            print("Set 1 is not a superset of Set 2")
elif option == '7':
    exit()
else:
        print("Invalid choice")

