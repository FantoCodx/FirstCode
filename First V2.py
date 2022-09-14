from imp import init_builtin
from mimetypes import init


higher_nr = 100
lower_nr = 50
number = input('inserte numero: ')

meio = int(number) <= higher_nr and int(number) >= lower_nr

if meio == True:
    print(number + ' esta no meio')
if meio != True:
    print(number + ' nao esta no meio')
    