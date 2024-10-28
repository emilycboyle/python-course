x = 5
def square_number(x):
    return x**2

def is_odd(x):
    if x %2 == 0:
        return False 
    else:
        return True

if __name__ == '__main__':
    y = square_number(x)
    if is_odd(y):
        print('odd')   
    print(y)



