from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time


def Task1():
    sys_is_num=False
    system=0
    print("Write the size of the key")
    while sys_is_num!=True:
        system=input()
        if system.isnumeric():
            sys_is_num=True
        else:
            print("Wrong value, try again")
    number=2**int(system)
    print(f'number of unique keys {number}')

def Task2():
    sys_is_num = False
    system = 0
    print("Write the size of the key")
    while sys_is_num != True:
        system = input()
        if system.isnumeric():
            sys_is_num = True
        else:
            print("Wrong value, try again")
    key=RSA.generate(int(system))
    print(key)

def Task3():
    sys_is_num = False
    system = 0
    print("Write the size of the key")
    while sys_is_num != True:
        system = input()
        if system.isnumeric():
            sys_is_num = True
        else:
            print("Wrong value, try again")
    key = RSA.generate(int(system))
    start_time = time.time()
    nkey=0
    while nkey!=key:
        key=key+1
    print(f'Key {nkey} time to find {time.time()-start_time}')

Task1()
Task2()
Task3()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
