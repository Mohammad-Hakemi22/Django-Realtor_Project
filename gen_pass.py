import random
import string


def user_input():
    x = int(input('enter lenght of password\n'))
    y = int(input('degree of hardly password:\n1=easy(min char=4)\t2=medium(min char=8)\t3=hard(min char=12)\n'))
    genarate_pass(x, y)


def genarate_pass(n, m):
    if m == 1:
        if n >= 4:
            s = ''.join(random.SystemRandom().choice(string.digits)
                        for _ in range(n))
            write_file(s)
        else:
            print('easy password must have min 4 char !')
            write_file(0)
    if m == 2:
        if n >= 8:
            s = ''.join(random.SystemRandom().choice(string.ascii_uppercase +
                                                     string.digits + string.ascii_lowercase) for _ in range(n))
            write_file(s)
        else:
            print('easy password must have min 8 char !')
            write_file(0)
    if m == 3:
        if n >= 12:
            l = '!@#$%^&*()_+=-/.,?><;|"'
            s = ''.join(random.SystemRandom().choice(string.ascii_uppercase +
                                                     string.digits + string.ascii_lowercase + l) for _ in range(n))
            write_file(s)
        else:
            print('easy password must have min 12 char !')
            write_file(0)


def write_file(x):
    if x == 0:
        pass
    else:
        try:
            with open('password.txt', 'w') as f:
                f.write(str(x))
                print('password created in password.txt and save in history')
            with open('password_history.txt', 'a') as f1:
                f1.write(str(x)+'\n')
        except BaseException as e:
            print("error on write in file\n", e)


def show_hist():
    print('\n'+'--'*20)
    try:
        with open('password_history.txt', 'r') as f:
            x = f.readlines()
            i = 1
            for l in x:
                print(str(i)+'. '+l)
                i += 1
    except BaseException as e:
        print("error on read of file\n", e)
    print('\n'+'--'*20)


def menu():
    flag = True
    while flag:
        print('\n'+'--'*20)
        print('\nEnter one option:\n1.show password(s) history\n2.creat a new password\npress 0 to exit\n')
        x = int(input())
        if x == 0:
            flag = False
        elif x == 1:
            show_hist()
        elif x == 2:
            user_input()
        else:
            print('enter valid option !!\n')
        print('\n'+'--'*20)


if __name__ == "__main__":
    menu()
