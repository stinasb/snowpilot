import os

def run():
    email = "stinabogsti@gmail.com"
    name = "stinasb"
    address = "https://github.com/stinasb/snowpilot.git"
    SendeMappe= '/home/pi/Documents/SendeMappe'
    os.system(f'git config --global user.email {email}')
    os.system(f'git config --global user.name {name}')
    os.system(f'cd {SendeMappe} && git add . && git commit -m "Nye Målinger" && git pull && git push')
    
    print("program ended succesfully")

run()