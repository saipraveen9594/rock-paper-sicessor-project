# this program is for developing rock paper scissor game
# importing random and tkinter modules

import random
import tkinter

ram = []

def get_winner(call):
    if random.random()<=(1/3):
        throw = 'rock'
    elif(1/3)<random.random()<=(2/3):
        throw = 'scissors'
    else:
        throw ='paper'
        
    if(throw == 'rock' and call =='paper') or (throw == 'paper' and call == 'scissors') \
      or(throw == 'scissors' and call == 'rock'):
        ram.append('W')
        result = 'won'
    elif throw == call:
        ram.append('D')
        result = 'draw'
    else:
        ram.append('L')
        result = 'lost'
        
    global output
    output.config(text='computer choise:'+throw+'\n'+result)
    
def pass_s():
    get_winner('scissors')
    
def pass_r():
    get_winner('rock')
    
def pass_p():
    get_winner('paper')
    
    
window = tkinter.Tk()

scissors = tkinter.Button(window,text='scissors',bg='#ff9999',padx=10,pady=5,command=pass_s,width=20)
rock = tkinter.Button(window,text='rock',bg='#80ff80',padx=10,pady=5,command=pass_r,width=20)
paper = tkinter.Button(window,text='paper',bg='#3399ff',padx=10,pady=5,command=pass_p,width=20)
output = tkinter.Label(window,width=20,fg='red',text='what is your call?')

scissors.pack(side='left')
rock.pack(side='left')
paper.pack(side='left')
output.pack(side='right')
window.mainloop()

for i in ram:print(i,end='')
if ram.count('L')>ram.count('W'):
    result='\nloose the series.'
elif ram.count('L')==ram.count('W'):
    result='\nSeries ended in a draw.'
else:
    result='\n you win the series.'
    
print(result)
    