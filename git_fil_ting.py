import os

def run():
    email = "stinabogsti@gmail.com"
    name = "stinasb"
    
    SendeMappe= '/home/pi/Documents/SendeMappe'
    
    os.system(f'git config --global user.email {email}')
    os.system(f'git config --global user.name {name}')
    
    os.system(f'cd {SendeMappe} && git add . && git commit -m "Nye Målinger" && git pull && git push && "stinasb" && "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"')
    
    print("program ended succesfully")

run()