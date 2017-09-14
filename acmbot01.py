#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:52:39 2017

@author: prawigya
"""

#Deploying a chatterbot to train the slackbot

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#Let's name the bot as ACMBot

acmbot =ChatBot("ACMBot", read_only=False, #set read_only as False if you want to train the bot while chatting.
                logicaladapters=[
                        "chatterbot.logic.TimeLogicAdapter",        #the chatterbot is aware of time.
                        "chatterbot.logic.MathematicalEvaluation",  #for mathematical operations
                        ],
                        input_adapter="chatterbot.input.VariableInputTypeAdapter",
                        output_adapter="chatterbot.output.OutputAdapter",
                        filter="chatterbot.filters.RepetitiveResponseFilter",
                        
                )




acmbot.set_trainer(ListTrainer) #ACM bot has been trainerd with chatterbot.corpus.english, to add basic conversations. Refer to all the training conversations in the acmbot_corpus file.

acmbot.train([ #sample conversation to train the chatterbot.
        '''
        'What are the departments / divisions in ACM?',
        'ACM consists of Technical, Management, Design and Editorial Department.',
        'What is Technical Department?',
        'Technical Department is where team ACM grinds it gears to come up with ideas and then implements them to make projects tackling real world problems. The widespread domains of the technical team focus on different applications of software development and bring them together to develop applications and softwares with real world implementation.',
        'What is Management Department?',
        ''
        '''
        ])


#Executing the chatterbot by running an infinite loop that terminates on KeyBoard Interrupt <Ctrl + C> ; EOF Error or System Exit.
while True:
    try:
        n=input()
        print(acmbot.get_response(n))
    except(KeyboardInterrupt,EOFError,SystemExit):
        break



    
        




