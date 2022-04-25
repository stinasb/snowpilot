import os
import time

def run():
    email = "stinabogsti@gmail.com"
    name = "stinasb"
    
    SendeMappe= '/home/pi/Documents/SendeMappe'
    
    os.system(f'git config --global user.email {email}')
    os.system(f'git config --global user.name {name}')
    
    os.system(f'cd {SendeMappe}')
    time.sleep(1)
    os.system('git add .')
    time.sleep(1)
    os.system('git commit -m "Nye Målinger"')
    time.sleep(1)
    os.system('git pull')
    time.sleep(1)
    os.system('git push ')
    
    print("program ended succesfully")

run()