

def calculator(first, second):
    print(first+second)

def printer(text):
    print(text)


from calculator import printer, calculator

calculator(2,4)

printer("AAA")