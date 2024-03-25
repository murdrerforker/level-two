def input_set():
    elements = input("Enter elements separated by commas: ").split(',')
    return set(elements)

def set_calculator():
    print("Set Calculator")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Symmetric Difference")
    print("5. Subset")
    print("6. Superset")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '7':
        return

    set1 = ('Ade', 'Bayo' , 'Dele', 'Sege', 'Toyo')
    set2 = ('Ola', 'Ade', 'Matthew' , 'Ishola' , 'Toyo')

    if choice == '1':
        result = set1.union(set2)
        print("Union:", result)
    elif choice == '2':
        result = set1.intersection(set2)
        print("Intersection:", result)
    elif choice == '3':
        result = set1.difference(set2)
        print("Difference:", result)
    elif choice == '4':
        result = set1.symmetric_difference(set2)
        print("Symmetric Difference:", result)
    elif choice == '5':
        if set1.issubset(set2):
            print("Set 1 is a subset of Set 2")
        else:
            print("Set 1 is not a subset of Set 2")
    elif choice == '6':
        if set1.issuperset(set2):
            print("Set 1 is a superset of Set 2")
        else:
            print("Set 1 is not a superset of Set 2")
    else:
        print("Invalid choice")

    set_calculator()

set_calculator()
