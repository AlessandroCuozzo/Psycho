#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
############################################
############################################
EXPERIMENTAL PSYCHOLOGY - RETRIEVAL PRACTICE
############################################
############################################
Created on Fri Mar 20 08:26:46 2020

@author: Cuozzo, Tardif (p42299, p17620)
"""
from constants import DISPSIZE, dico, code_choice, code_choice_reverse, pretest # import the pre-determined constants
from pairs import Pair # import the Pair class with its methods
from psychopy.visual import Window, TextStim, ImageStim
from psychopy.event import waitKeys
from psychopy import core
from random import shuffle # the random module allows to use many hazard-related functions
from datetime import datetime

###################
###################
#    FUNCTIONS    #
###################
###################

# ------------------------------------------------------------------ #
# Function that will be called to enter the user identification data #
# Double while loop                                                  #
# ------------------------------------------------------------------ #
def whoAmI(response, done, qpos, image):
    """
    Function that will be called to enter the user identification data
    - **Input**:
        :response: the user resonse (empty string at beginning)
        :done: boolean (True / False) -> False at beginning
        :qpos: text position for user response
        :image: the stimulus image
    """
    
    # --------------------------------------- #
    # WHILE THE WELCOME MESSAGE IS NOT PASSED #
    # --------------------------------------- #
    while len(response)==0: # while the user has not taped anything yet
        response = '' # the response written by the user - On commence avec une chaîne vide
        respstim = TextStim(disp, text='', pos=qpos, height=size, color=color) # stimulus texte  
        qstim = ImageStim(disp, image=image)
        qstim.draw() # dessiner la question
        disp.flip() # passer au screen au suivant -> on met la question par-dessus
        core.wait(loadTime) # delay of 10 seconds before passing to the learning phase
        done = False
        
        # ----------------------------------- #
        # WHILE THE USER'S ANSWER IS NOT DONE #
        # Check for keypresses                #
        # ----------------------------------- # 
        while not done: # loop until done == True
            resplist = waitKeys(maxWait=float('inf'), keyList=None, timeStamped=True)
            key, presstime = resplist[0] # use only the first in the returned list of keypresses -> resplist[0] is the first element in the resplist list   
            if len(key) == 1: # Check si la longeur de la réponse (len) = 1
                response += key #Ajouter la lettre tapée à la réponse => on ne tient pas compte des touches pour les majuscules ni de la touche escape
            elif key == 'space': # Check if key is the space bar
                response += ' ' # ajoute un espace
            elif key == 'backspace' and len(response) > 0: # Check if the key's name was backspace AND si la réponse a au moins une lettre
                response = response[0:-1] #remove last character of the response
            if key == 'return': # if the key was non of the above, check si c'est enter
                done = True # set done to True
            respstim.setText(response.capitalize()) # actualiser la user response => 1ère lettre en majuscule
            qstim.draw() # réafficher la question stimulus (image)
            respstim.draw() # réafficher la réponse au stimulus
            disp.flip() # update the monitor
            core.wait(loadTime) # add a little lag to avoid little freez and/or bug

    return response.capitalize() # 1ère lettre en majuscule

# ------------------------------------------------------------------------------------------------- #
# Function that will be called every time the user needs to press a key to pass to the next display #
# Double while loop                                                                                 #
# ------------------------------------------------------------------------------------------------- #
def userResponse(response, done, qpos, image):
    """
    Function that will be called every time the user needs to press a key to pass to the next display
    - **Input**:
        :response: the user resonse (empty string at beginning)
        :done: boolean (True / False) -> False at beginning
        :qpos: text position for user response
        :image: the stimulus image
    """
    
    # --------------------------------------- #
    # WHILE THE WELCOME MESSAGE IS NOT PASSED #
    # --------------------------------------- #
    while len(response)==0: # while the user has not taped anything yet
        response = '' # the response written by the user - On commence avec une chaîne vide
        respstim = TextStim(disp, text='', pos=qpos, height=size) # stimulus texte  
        qstim = ImageStim(disp, image=image)
        qstim.draw() # dessiner la question
        disp.flip() # passer au screen au suivant -> on met la question par-dessus
        core.wait(loadTime) # delay of 10 seconds before passing to the learning phase
        done = False
    
        # ----------------------------------- #
        # WHILE THE USER'S ANSWER IS NOT DONE #
        # Check for keypresses                #
        # ----------------------------------- # 
        while not done: # loop until done == True
            resplist = waitKeys(maxWait=float('inf'), keyList=None, timeStamped=True)
            key, presstime = resplist[0] # use only the first in the returned list of keypresses -> resplist[0] is the first element in the resplist list   
            response += key #Ajouter la lettre tapée à la réponse
            done = True # set done to True
            qstim.draw() # réafficher la question stimulus
            respstim.draw() # réafficher la réponse au stimulus
            disp.flip() # update the monitor
            core.wait(loadTime) # add a little lag to avoid little freez and/or bug

# --------------------------------------------------------------------------- #
# Function that will be called every time the user is still taping his answer #
# Single while loop                                                           #
# --------------------------------------------------------------------------- #
def tapeAnswer(response, done, realTest):

    """
    Function that will be called every time the user is still taping his answer
    - **Input**:
        :response: the user resonse (empty string at beginning)
        :done: boolean (True / False) -> False at beginning
        :test: boolean (True or False)
        
    - **outpu**:
        :response: the user response
        :done: True or false
    """
    
    # ----------------------------------- #
    # WHILE THE USER'S ANSWER IS NOT DONE #
    # Check for keypresses                #
    # ----------------------------------- # 
    while not done: # loop until done == True
        resplist = waitKeys(maxWait=float('inf'), keyList=None, timeStamped=True)
        key, presstime = resplist[0] # use only the first in the returned list of keypresses -> resplist[0] is the first element in the resplist list   
        if len(key) == 1: # Check si la longeur de la réponse (len) = 1
            response += key #Ajouter la lettre tapée à la réponse => on ne tient pas compte des touches pour les majuscules ni de la touche escape
        elif key == 'space': # Check if key is the space bar
            response += ' ' # ajoute un espace
        elif key == 'backspace' and len(response) > 0: # Check if the key's name was backspace AND si la réponse a au moins une lettre
            response = response[0:-1] #remove last character of the response
        if key == 'return': # if the key was non of the above, check si c'est enter
            done = True # set done to True
        respstim.setText(response.capitalize()) # actualiser la user response => 1ère lettre en majuscule
        qstim.draw() # réafficher la question stimulus (image)
        if realTest==True: # if we are testing (not pretesting)
            qstim2.draw() # réafficher la question stimuls (texte)
        respstim.draw() # réafficher la réponse au stimulus
        disp.flip() # update the monitor
        core.wait(loadTime) # add a little lag to avoid little freez and/or bug

    return response.capitalize(), done # 1ère lettre en majuscule

"""    
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
""" 

##################
##################
#    PRE-TEST    #
##################
##################

# ------------------------- #
# Initial & Visual settings #
# ------------------------- # 
feedback = True # can be set to True or False
firstLetter = False # can be set to True or False
disp = Window (size=DISPSIZE, units='pix', fullscr=True) # créer une fenêtre pour montrer des choses à l'écran => unité est en Pixel
#size = 24 # text size # 36
size = 36 # text size # 36
color = 'darkblue' # text color
color2 = 'crimson' # text color
color3 = 'green' # text color
space = '\t\t\t\t' # space between the word and its translation when learning
learnTime = 10 # time given to memorize one pair word
loadTime = 0.01 # time for spychopy displaying
X = int(DISPSIZE[0]) # axe des X pour l'écran
Y = int(DISPSIZE[1]) # axe des Y pour l'écran


# Linux
qpos = (X*0,Y*-0.2) # position de la question
#qpos2 = (X*-0.02,Y*-0.02) # position de la question
qpos3 = (X*-0.2,Y*-0.05) # position de la question
#qpos4 = (X*-0.03,Y*-0.015) # position de la question
#qpos5 = (X*0.05,Y*-0.15) # position de la question
#qpos6 = (X*-0.03,Y*0.02) # position de la question
#qpos7 = (X*-0.02,Y*0.25) # position de la question
#qpos8 = (X*0.3,Y*-0.35) # position de la question
#qpos9 = (X*0.3,Y*-0.25) # position de la question

"""
# Mac
qpos = (X*0.5,Y*-0.2) # position de la question
#qpos2 = (X*0.18,Y*-0.02) # position de la question
qpos3 = (X*0.18,Y*-0.05) # position de la question
#qpos4 = (X*0.18,Y*-0.015) # position de la question
#qpos5 = (X*0.25,Y*-0.15) # position de la question
#qpos6 = (X*0.18,Y*0.02) # position de la question
#qpos7 = (X*0.18,Y*0.25) # position de la question
#qpos8 = (X*0.5,Y*-0.35) # position de la question
#qpos9 = (X*0.5,Y*-0.25) # position de la question

# Windows
qpos = (X*0.1,Y*-0.2) # position de la question
#qpos2 = (X*0,Y*-0.02) # position de la question
qpos3 = (X*-0.1,Y*-0.05) # position de la question
#qpos4 = (X*0,Y*-0.015) # position de la question
#qpos5 = (X*0.1,Y*-0.15) # position de la question
#qpos6 = (X*0,Y*0.02) # position de la question
#qpos7 = (X*0,Y*0.25) # position de la question
#qpos8 = (X*0.3,Y*-0.35) # position de la question
"""

# ------------------------------------------ #
# WHO AM I - HELLO                           #
# Tape ID, age, gender and degre of the user #
# ------------------------------------------ # 
userResponse('', False, qpos, 'images/Bonjour.gif') # call the userResponse -> double while loop to save the user taped response
ID = whoAmI('', False, qpos, 'images/ID.gif') # call the whoAmI -> double while loop to save the user taped response
image = 'images/Age.gif'
AGE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user taped response
while AGE.isdigit()==False: # only accept decimals | can isdecimal() in python3
    AGE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user taped response
image = 'images/Sexe.gif'
SEXE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user taped response
while SEXE!='G' and SEXE!='F': # do not accept another answer
    SEXE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user taped response
DEGRE = whoAmI('', False, qpos, 'images/Degre.gif') # call the whoAmI -> double while loop to save the user taped response
userResponse('', False, qpos, 'images/Hello.gif') # call the userResponse -> double while loop to save the user taped response

# ----------------------------------- #
# SETTING FOR THE PRE-TEST            #
# WHILE THE PRE-TEST IS NOT SUCCEEDED #
# ----------------------------------- #
response = '' # the response attempted by the user - On commence avec une réponse vide
while response != pretest: # while the answer is not correct
    response = '' # the response written by the user - On commence avec une chaîne vide
    respstim = TextStim(disp, text='', pos=qpos, height=size, color=color) # stimulus texte  
    qstim = ImageStim(disp, image='images/TradVonat.gif')
    qstim.draw() # dessiner la question
    disp.flip() # passer au screen au suivant -> on met la question par-dessus
    core.wait(loadTime) # delay of 10 seconds before passing to the learning phase
    response, done = tapeAnswer(response, False, False) # While loop to taping the entire answer

    # ------------------------------------------------------- #
    # CHECK IF THE PRETEST IS SUCCEEDED OR NOT                #
    # DISPLAY A MESSAGE TO THE USER ACCORDING TO THE ANSWER   #
    # ------------------------------------------------------- #
    if response==pretest: # if the answer is correct 
        userResponse('', False, qpos, 'images/BravoVonat.gif') # call the userResponse -> double while loop to save the user taped response
    else: # if the answer is NOT correct 
        userResponse('', False, qpos, 'images/OupsVonat.gif') # call the userResponse -> double while loop to save the user taped response

"""    
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
""" 


#################
#################
#  FINAL TEST   #
#################
#################

# --------------------------------- #
# CREATE ALL THE WORD PAIRS OBJECTS #
# --------------------------------- # 
LISTE = [] # empty list which will contain all the pair objects
CORRECT_SET = set() # empty set in which we will add every string word when correctly translated by the user 
for pair in dico: # pour chaque pair de mots présente dans le dictionnaire du fichier 'constants'
    LISTE.append(Pair(pair,dico[pair])) # pair is the dico key (french word) ; dico[pair] is the value of the key (corresponding translated word)
shuffle(LISTE) # mélange la liste de mots -> ordre au hasard

# --------------------------------------------------------------- #
# FIRST MAIN LOOP - FOR EACH WORD                                 #
# CHECK IF WE DECIDED TO GIVE THE TRANSLATION FIRST LETTER OR NOT #
# --------------------------------------------------------------- #
for pair in LISTE: # pour chaque pair de mot
    response = ''
    if firstLetter==True: # Do we give the student the first letter of the translation ?
        response += pair.translate[0] # le mot en français => avec la 1ère lettre du mot comme indice
    qstim = ImageStim(disp, image='images/Test.gif') # stimulus image
    qstim2 = TextStim(disp, text=pair.word, pos=qpos3, height=size, color=color) # stimulus texte
    respstim = TextStim(disp, text=response, pos=qpos, height=size, color=color) # boite réponse (to be completed by the user)
    respstim.setText(response) # actualiser la user response => 1ère lettre en majuscule
    qstim.draw() # dessiner la pair de mots (image)
    qstim2.draw() # dessiner la pair de mots (image)
    respstim.draw() # Draw the translation response
    disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
    core.wait(loadTime) # delay of 10 seconds before passing to the next pair
    pair.setTest() # actualize the test property of the pair object
    response, done = tapeAnswer(response, False, True) # While loop to taping the entire answer
    
    # ------------------------------------------------------------------ #
    # ADD THE USER RESPONSE IN THE PAIR OBJECT                           #
    # RESPONSE CHECK - RESPONSE IS WRONG                                 #
    # ADD FAILURE IN THE WORD PAIR OBJECT                                #
    # CHECK IF WE DECIDED TO GIVE A FEEDBACK AFTER THE FIRST TEST OR NOT #
    # CHECK IF FIRST TEST OR NOT - ENVENTUALLY DISPLAY FEEDBACK          #
    # ------------------------------------------------------------------ #
    pair.addResponse(response,0) # add the user response in the pair object (no matter if the response is correct or wrong)
    if pair.checkAnswer()==False: # if the answer is NOT correct 
        pair.addFail() # fail = fail + 1
        if feedback==True : # Does the subject benefits of a feed back after an answer ?
            image = 'images/OupsEmpty.gif' # Ooups image
            qstim = ImageStim(disp, image=image) # stimulus image
            qstim.draw() # dessiner la question (image)
            disp.flip() # passer au screen au suivant -> on met la question par-dessus
            userResponse('', False, qpos, image) # call the userResponse -> double while loop to save the user taped response
            core.wait(loadTime) # let psychopy breath...
    
    # ------------------------------------------------------------------ #
    # RESPONSE CHECK - RESPONSE IS CORRECT                               #
    # ADD SUCCESS IN THE WORD PAIR OBJECT                                #
    # CHECK IF WE DECIDED TO GIVE A FEEDBACK AFTER THE FIRST TEST OR NOT #
    # CHECK IF FIRST TEST OR NOT - ENVENTUALLY DISPLAY FEEDBACK          #
    # ------------------------------------------------------------------ #
    else: # if the answer is correct 
        pair.addSuccess() # success = success + 1    
        if feedback==True: # Does the subject benefits of a feed back after an answer ?
            image = 'images/BravoEmpty.gif' # Ooups image
            qstim = ImageStim(disp, image=image) # stimulus image
            qstim.draw() # dessiner la question (image)
            disp.flip() # passer au screen au suivant -> on met la question par-dessus
            userResponse('', False, qpos, image) # call the userResponse -> double while loop to save the user taped response
            core.wait(loadTime) # let psychopy breath...
            
# ----------------------------------------- #
# ENDING : DISPLAY A THANK YOU MESSAGE      #
# SAVE THE NUMBER OF TURNS FOR THE RESULTS  #
# THEN CLOSE THE DISPLAY                    #
# ----------------------------------------- # 
qstim = ImageStim(disp, image='images/Merci.gif') # thank you image
qstim.draw() # afficher le message image
disp.flip() # passer au screen au suivant -> on met la question par-dessus
core.wait(learnTime) # delay of 10 seconds before passing to the learning phase       
disp.close() # close the display 

"""    
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
"""

#################
#################
# SAVE RESULTS  #
#################
#################

with open('retrieval_practice_results_final_test'+ID+'_'+AGE+'_'+SEXE+'_'+DEGRE+'_'+str(datetime.now())+'.csv', 'w') as f: # open a CSV file to write the results
#with open('retrieval_practice_results_final_test.csv','w') as f: # open a CSV file to write the results -> 'w' is for 'write' -> we do not open an existing file, but create a new one
    f.write('word\ttranslation\tresponse\tsuccess\tfailure\n') # write the header of the table
    for pair in LISTE: # pour chaque pair de mot
        f.write(pair.word+'\t'+pair.translate+'\t'+pair.user_response+'\t'+str(pair.firstSuccess)+'\t'+str(pair.firstFail)+'\n') # write all results for the word pair in a row
    f.write(ID+'\n') # add the identification number of the user
    f.write(AGE+'\n') # add the age of the user
    f.write(SEXE+'\n') # add the gender of the user
    f.write(DEGRE+'\n') # add the scholar degree of the user
