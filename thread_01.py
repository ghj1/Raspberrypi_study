import threading



def first_func(age):
    while True:
        print('I am first child.', age)
    return

def second_func(age):
    while True:
        print('I am second child.', age)
    return

if __name__ =='__main__':
    first = threading.Thread(target= first_func, args=(5,)) 
    second = threading.Thread(target=second_func, args=(3,)) 
    first.start()
    second.start()
    first.join()
    second.join()


    while True:
        print('I am parent')
    pass