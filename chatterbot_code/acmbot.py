#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:40:27 2017

@author: prawigya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:09:45 2017

@author: prawigya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:40:20 2017

@author: prawigya
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

acmbotb=ChatBot("ACMVITbot",read_only=False ,
                logic_adapters=['chatterbot.logic.BestMatch',
                                {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                                 'threshold': 0.65,
                                 'default_response' : 'I am sorry, but I can only answer questions related to ACM.'
                                 }
                                ],                
                input_adapter = 'chatterbot.input.VariableInputTypeAdapter',
                output_adapter = 'chatterbot.output.OutputAdapter',
                filter = 'chatterbot.filters.RepetitiveResponseFilter'
                )
acmbotb.set_trainer(ListTrainer)
acmbotb.train(
        ['Hello',
         'Hi',
         'Hello',
         'Okay',
         'Okay :)'
         
                
                
                
                ]
        
        )
"""Asking for the username"""
#name_counter. nc
#chat_counter. c
nc=0
c=0
#The bot will ask for the name three times, if the user denies their name more than three times, the bot will stop asking

def negatives(name):
    if ('No' in name or 'no' in name or 'naah' in name or 'nope' in name or 'dont' in name):
        return True
    else:
        return False

def positives(name):
    if ('Yes' in name or 'yes' in name or 'yup' in name or 'Yeah' in name or 'yeah' in name):
        return True
    else:
        return False
    
def check_sent(name):
    if('name' in name or 'is' in name):
            return True

def check_sent_name(name):
    return name[(name.index('is')+1)].split()
    
    
while True:
    try:
        n=input()
        c+=1            
        print(acmbotb.get_response(n))
        """ Asking for the Username """
        if(c%3==0 and nc==0):
            print('May I know your name? :)')
            name=input().split()
            #Checking if the user says 'My name is . . .'
            if check_sent(name):
                name=(check_sent_name(name))
                print('Hello ',name[0])
            elif negatives(name):
                print('Umm okay :/')
                nc=1
            elif positives(name):
                print('Please enter your name:')
                name=input().split()
                if check_sent(name):
                    name=check_sent_name(name)
                else:
                    name=input().split()
                print('Hello ', name[0])
                    
            elif(len(name)>2):
                while True:
                    print('Are you sure that is your name?')
                    check_name = input()
                    if positives(check_name):
                        print('Hello ', name[0])
                        nc=1
                        break
                    elif negatives(check_name):
                        print('Would you mind telling your name again?')
                        check_name2=input().split()
                        if check_sent(check_name2):
                            name=(check_sent_name(name))
                            print('Hello ',name[0])                            
                            nc=1
                            break
                        elif positives(check_name2):
                            print('Please tell your name')
                            name=input().split()
                            if check_sent(name):
                                name=(check_sent_name(name))
                            print('Hello ',name[0])
                            nc=1
                            break
                        elif negatives(check_name2):
                            print('Okay nevermind :p')
                            break
                        else:
                            name=check_name2
                            print('Hello ',check_name2[0])
                            nc=1
                            break
           
            else:
                print('Hello ',name[0])
                nc=1
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
        
            
