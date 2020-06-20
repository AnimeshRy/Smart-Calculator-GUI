import re

print('Simple calculator')
print("type quit to exit\n")

previous = 0
run = True


def performmath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("enter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("bye bitch")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performmath()
