# write your code here
memory = 0
def add_operation(x, y):
    return x + y
def subtract_operation(x, y):
    return x - y
def multiplication_operation(x, y):
    return x * y
def divide_operation(x ,y):
    return x / y
def check(v1,v2,v3):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*'or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)
    
def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    else:
        return False
def operation():
    global memory
    start_operation_1 = True
    while start_operation_1:
        operation = ['*','-','/', '+']
        print("Enter an equation")
        x,oper,y = input().split()
        result = 0
        if x == 'M':
            x = str(memory)
        if y == 'M':
            y = str(memory)
        if isinstance(x, (int, float)) or isinstance(y, (int,float)):
            print("Do you even know what numbers are? Stay focused!")
            continue
        else:
            if isinstance(x, int):
                x = int(x)
            else:
                x = float(x)
            if isinstance(y, int):
                y = int(y)
            else:
                y = float(y)
        check(x,y,oper)
        if oper not in operation:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue
        if oper == '/' and y == 0:
            print("Yeah... division by zero. Smart move...")
            continue
        
        if oper == '+':
            result =  add_operation(x, y)
        elif oper == '-':
            result = subtract_operation(x ,y)
        elif oper == '*':
            result = multiplication_operation(x, y)
        elif oper == '/':
            result = divide_operation(x ,y)

        print(result)
        start_operation_2 = True
        while start_operation_2:
            start_operation_3 = False
            print("Do you want to store the result? (y / n):")
            answer = input()
            msg_ = {10: "Are you sure? It is only one digit! (y / n)",
                11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
                   12: "Last chance! Do you really want to embarrass yourself? (y / n)"}
            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    start_operation_4_inside = True
                    while start_operation_4_inside:
                        print(f'{msg_[msg_index]}')
                        ans_4 = input()
                        if ans_4 == 'y':
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                memory = result
                                start_operation_4_inside = False
                        elif ans_4 == 'n':
                            start_operation_4_inside = False
                        else:
                            continue
                elif is_one_digit(result) == False and answer == 'y':
                    memory = result
                    start_operation_4_inside = False
                start_operation_3 = True
            elif answer == 'n':
                start_operation_3 = True
            else:
                continue
            while start_operation_3:
                print('Do you want to continue calculations? (y / n):')
                ans = input()
                if ans == 'y':
                    start_operation_2 = False
                    start_operation_3 = False
                elif ans == 'n':
                    start_operation_1 = False
                    start_operation_2 = False
                    start_operation_3 = False
                else:
                    continue

operation()

