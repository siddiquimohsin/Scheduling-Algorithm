import os
from pathlib import Path
import termcolor

print('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X')
print('                 WELCOME TO SCHEDULING ALGORITHM                     ')
print('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X')
print('\n')
print('1.Priority Algorithm \n2.RoundRobin \n3.SJF Preemptive')
print('\n')

while(True):
    in1=input('Choose your Algorithm(1-3): ')
    if in1 =='1':
        os.system('clear')
        termcolor.cprint('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X','green')
        termcolor.cprint('                 YOU CHOOSE PRIORITY ALGORITHM                       ','green')
        termcolor.cprint('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X','green')
        os.system(f'python3 {Path.cwd()}/Priority.py')
        break
    elif in1 =='2':
        os.system('clear')
        termcolor.cprint('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X','green')
        termcolor.cprint('                   YOU CHOOSE ROUND ROBIN ALGORITHM                       ','green')
        termcolor.cprint('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X','green')
        os.system(f'python3 {Path.cwd()}/RoundRobin.py')
        break
    elif in1 =='3':
        os.system('clear')
        termcolor.cprint('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X','green')
        termcolor.cprint('               YOU CHOOSE SJF PREEMPTIVE ALGORITHM                       ','green')
        termcolor.cprint('X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X','green')
        os.system(f'python3 {Path.cwd()}/SJFPreemptive.py')
        break
    else:
        termcolor.cprint("Please Enter correct input",'red')
        print('\n')
    

