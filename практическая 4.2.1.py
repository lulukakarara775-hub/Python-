def variant2_task1():
    try:
        num = int(input())
        if num < 0:
            pass 
        elif num > 100:
            print("*")
        else:
            print("*" * num)
    except ValueError:
        pass 
