#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
############################################
############################################
EXPERIMENTAL PSYCHOLOGY - RETRIEVAL PRACTICE
############################################
############################################
Created on Tue Aug 13 15:42:22 2019

@author: Cuozzo, Tardif (p42299, p17620) 
"""
#import time # import the time modules 
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
def userResponse(response, done, qpos, image, multi):
    """
    Function that will be called every time the user needs to press a key to pass to the next display
    - **Input**:
        :response: the user resonse (empty string at beginning)
        :done: boolean (True / False) -> False at beginning
        :qpos: text position for user response
        :image: the stimulus image
        :multi: multiple display ? integer (1, 2 or 3)
    """
    
    # --------------------------------------- #
    # WHILE THE WELCOME MESSAGE IS NOT PASSED #
    # --------------------------------------- #
    while len(response)==0: # while the user has not taped anything yet
        response = '' # the response written by the user - On commence avec une chaîne vide
        respstim = TextStim(disp, text='', pos=qpos, height=size) # stimulus texte  
        qstim = ImageStim(disp, image=image)
        qstim.draw() # dessiner la question
        if multi>=2: # at least diferent stimuli
            qstim2.draw()
        if multi==3: # 3 diferent stimuli
            qstim3.draw()
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
        :realTest: boolean (True or False)
        
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
firstLetter = True # can be set to True or False
disp = Window (size=DISPSIZE, units='pix', fullscr=True) # créer une fenêtre pour montrer des choses à l'écran => unité est en Pixel
#size = 24 # text size # 36
size = 36 # text size # 36
color = 'darkblue' # text color
color2 = 'crimson' # text color
color3 = 'green' # text color
space = '\t\t\t\t' # space between the word and its translation when learning
learnTime = 5 # time given to memorize one pair word
loadTime = 0.01 # time for spychopy displaying
qpos = (0,int(DISPSIZE[1]*-0.2)) # position de la question
qpos2 = (int(DISPSIZE[0]*-0.02),int(DISPSIZE[1]*-0.02)) # position de la question
qpos3 = (int(DISPSIZE[0]*-0.2),int(DISPSIZE[1]*-0.05)) # position de la question
qpos4 = (int(DISPSIZE[0]*-0.03),int(DISPSIZE[1]*-0.015)) # position de la question
qpos5 = (int(DISPSIZE[0]*0.05),int(DISPSIZE[1]*-0.15)) # position de la question
qpos6 = (int(DISPSIZE[0]*-0.03),int(DISPSIZE[1]*0.02)) # position de la question
qpos7 = (int(DISPSIZE[0]*-0.02),int(DISPSIZE[1]*0.25)) # position de la question
qpos8 = (int(DISPSIZE[0]*0.3),int(DISPSIZE[1]*-0.35)) # position de la question

# ------------------------------------------ #
# WHO AM I - HELLO                           #
# Tape ID, age, gender and degre of the user #
# ------------------------------------------ # 
userResponse('', False, qpos, 'images/Bonjour.gif', 1) # call the userResponse -> double while loop to save the user traped response
ID = whoAmI('', False, qpos, 'images/ID.gif') # call the whoAmI -> double while loop to save the user traped response
image = 'images/Age.gif'
AGE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user traped response
while AGE.isdigit()==False: # only accept decimals | can isdecimal() in python3
    AGE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user traped response
image = 'images/Sexe.gif'
SEXE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user traped response
while SEXE!='G' and SEXE!='F': # do not accept another answer
    SEXE = whoAmI('', False, qpos, image) # call the whoAmI -> double while loop to save the user traped response
DEGRE = whoAmI('', False, qpos, 'images/Degre.gif') # call the whoAmI -> double while loop to save the user traped response
userResponse('', False, qpos, 'images/Hello.gif', 1) # call the userResponse -> double while loop to save the user traped response

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
        userResponse('', False, qpos, 'images/BravoVonat.gif', 1) # call the userResponse -> double while loop to save the user traped response
    else: # if the answer is NOT correct 
        userResponse('', False, qpos, 'images/OupsVonat.gif', 1) # call the userResponse -> double while loop to save the user traped response
    
        
"""    
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
""" 

    
####################
####################
# REAL TEST BEGINS #
####################
####################
        
# --------------------------------- #
# CREATE ALL THE WORD PAIRS OBJECTS #
# --------------------------------- # 
LISTE = [] # empty list which will contain all the pair objects
CORRECT_SET = set() # empty set in which we will add every string word when correctly translated by the user 
for pair in dico: # pour chaque pair de mots présente dans le dictionnaire du fichier 'constants'
    LISTE.append(Pair(pair,dico[pair])) # pair is the dico key (french word) ; dico[pair] is the value of the key (corresponding translated word)
shuffle(LISTE) # mélange la liste de mots -> ordre au hasard

# -------------- #
# LEARNING PHASE #
# -------------- #
userResponse('', False, qpos, 'images/15paires.gif', 1) # call the userResponse -> double while loop to save the user traped response
for pair in LISTE: # pour chaque pair de mot
    learn = pair.word+space+pair.translate # le mot en français + 3 tabs (espacements + la traduction)
    qstim = ImageStim(disp, image='images/Learn.gif')
    qstim2 = TextStim(disp, text=learn, pos=qpos2, height=size, color=color) # stimulus texte
    qstim.draw() # dessiner la pair de mots (image)
    qstim2.draw() # dessiner la pair de mots (texte)
    disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
    core.wait(learnTime) # delay of 10 seconds before passing to the next pair


"""    
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
""" 

#################
#################
# TESTING PHASE #
#################
#################

# ----------------------------------------------------------------------------------- #
# FIRST MAIN LOOP - THIS STEP IS REPEATED UNTIL THE USER IS DONE WITH EVERY WORD PAIR #
# ----------------------------------------------------------------------------------- # 
i = 0
while len(CORRECT_SET)<len(LISTE): # Until the user gives the correct answer to every pair at least once 
    i += 1 # number of turns of the loop => i will be reused to know at which turn of the loop we are for each response (to save in the results)
    
    # ------------------------------------------------------------------------- #
    # SHUFFLE THE PAIRS ORDER                                                   #
    # SECOND MAIN LOOP - FOR EACH WORD                                          #
    # Check if the user previously decided to drop, learn or test the word pair #
    # ------------------------------------------------------------------------- #
    shuffle(LISTE)
    for pair in LISTE: # pour chaque pair de mot
        if pair.drop==True or (pair.newTest==True and pair.test==pair.maxTest) or (pair.newLearn==True and pair.learn==pair.maxLearn): # if we are done with the present pair
            CORRECT_SET.add(pair.word) # we add it in the set containing all pairs we won't have to deal with again
            if pair.drop==True: # if the user decided to drop the word pair during the previous loop turn
                pair.addDrop(i) # Fill the pair object allUserResponses attribute with **DROPPED** for the actual turn -> will actually do the same for each remaining turns
            else: # if the user is done with this pair word, but it did not drop it -> he 'finished'
                pair.addFinish(i) # Fill the pair object allUserResponses attribute with **FINISHED** for the actual turn -> will actually do the same for each remaining turns
        else: # if the user did NOT decide to drop the word pair during the previous loop turn
            
            # ---------------------- #
            # LEARNING THE PAIR WORD #
            # ---------------------- #
            if pair.newLearn==True and pair.learn<pair.maxLearn: # the user chose to learn this pair after its first correct answer AND if he has not reached the learning threshold yet
                learn = pair.word+space+pair.translate # le mot en français + 3 tabs (espacements + la traduction)
                qstim = ImageStim(disp, image='images/Learn.gif')
                qstim2 = TextStim(disp, text=learn, pos=qpos2, height=size, color=color) # stimulus texte
                qstim.draw() # dessiner la pair de mots (image)
                qstim2.draw() # dessiner la pair de mots (texte)
                disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
                core.wait(learnTime) # delay of 10 seconds before passing to the next pair
                pair.addLearn(i) # Fill the pair object allUserResponses attribute with **LEARN** for the actual turn
                pair.setLearn() # # actualize the learn property of the pair object
                     
            # --------------------------------------------------------------- #
            # TESTING THE PAIR WORD                                           #
            # CHECK IF WE DECIDED TO GIVE THE TRANSLATION FIRST LETTER OR NOT #
            # --------------------------------------------------------------- #
            elif (pair.newLearn==False and pair.newTest==True and pair.test<pair.maxTest) or i==1: # If the user chose to test agin the pair word after its first correct answer AND if he has not reached the learning threshold yet OR If it is the very first time (first turn of the main while loop)
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
                # CHECK IF FIRST TEST OR NOT                                         #
                # DISPLAY FEEDBACK                                                   #
                # ------------------------------------------------------------------ #
                pair.addResponse(response,i) # add the user response in the pair object (no matter if the response is correct or wrong)
                if pair.checkAnswer()==False: # if the answer is NOT correct 
                    pair.addFail() # fail = fail + 1 | => Will also set the word pair for a new test | => increases the threshold of maximum testing
                    if feedback==True or pair.firstTest==False or (feedback==True and pair.firstTest==True): # Does the subject benefits of a feed back after an answer ?
                        if pair.firstTest==False: # the first test always benefits of the full feed-back
                            image = 'images/Oups.gif' # Ooups image - full feedback
                            text = pair.word+space+pair.translate # word pair
                            text2 = pair.user_response # answer written by the user
                        else: # Only message saying 'Ouups
                            image = 'images/OupsEmpty.gif' # Ooups image
                            text = '' # empty string
                            text2 = '' # empty string
                        qstim = ImageStim(disp, image=image) # stimulus image
                        qstim2 = TextStim(disp, text=text, pos=qpos4, height=size, color=color) # stimulus texte
                        qstim3 = TextStim(disp, text=text2, pos=qpos5, height=size, color=color2) # stimulus texte
                        qstim.draw() # dessiner la question (image)
                        qstim2.draw() # dessiner la question (pair de mot)
                        qstim3.draw() # dessiner la question (user response)
                        disp.flip() # passer au screen au suivant -> on met la question par-dessus
                        userResponse('', False, qpos, image, 3) # call the userResponse -> double while loop to save the user traped response
                        core.wait(loadTime) # let psychopy breath...
                    
                # ------------------------------------------------------------------ #
                # RESPONSE CHECK - RESPONSE IS CORRECT                               #
                # ADD SUCCESS IN THE WORD PAIR OBJECT                                #
                # CHECK IF WE DECIDED TO GIVE A FEEDBACK AFTER THE FIRST TEST OR NOT #
                # CHECK IF FIRST TEST OR NOT                                         #
                # DISPLAY FEEDBACK                                                   #
                # ------------------------------------------------------------------ #
                else: # if the answer is correct 
                    pair.addSuccess() # success = success + 1    
                    if feedback==True or pair.firstTest==False or (feedback==True and pair.firstTest==True): # Does the subject benefits of a feed back after an answer ?
                        if pair.firstTest==False: # the first test always benefits of the full feed-back
                            image = 'images/Bravo.gif' # Bravo image - full feedback
                            text = pair.word+space+pair.translate # word pair
                        else: # Only message saying 'Bravo'
                             image = 'images/BravoEmpty.gif' # Ooups image
                             text = '' # empty string
                        qstim = ImageStim(disp, image=image) # stimulus image
                        qstim2 = TextStim(disp, text=text, pos=qpos6, height=size, color=color3) # stimulus texte
                        qstim3 = TextStim(disp, text='', pos=qpos, height=size, color=color2) # stimulus texte
                        qstim.draw() # dessiner la question (image)
                        qstim2.draw() # dessiner la question (pair de mot)
                        qstim3.draw() # dessiner la question (user response)
                        disp.flip() # passer au screen au suivant -> on met la question par-dessus
                        userResponse('', False, qpos, image, 3) # call the userResponse -> double while loop to save the user traped response
                        core.wait(loadTime) # let psychopy breath...
                    
                    # --------------------------------------------------------------- #
                    # CASE IF IT IS THE FIRST TIME THE USER GIVES THE CORRECT ANSWER  #
                    # THIRD MAIN LOOP ; WHILE THE CHOICE CANNOT BE INTERPRETED        #
                    # let the user choose what he wants do to : Test / Learn / Drop   #
                    # --------------------------------------------------------------- # 
                    if pair.firstTest == False: # If it is the very first time the user gives the correct answer
                        image = 'images/Choix.gif' # Bravo + choice image
                        choice = '' # the chocie selected by the user - On commence avec une chaîne vide
                        DLT = False # Drop / Learn / Test
                        while choice not in code_choice.keys(): # while the choice is not one understood by thze program (other than 1,2 or 3)
                            choicestim = TextStim(disp, text='', height=size) # stimulus texte  
                            qstim = ImageStim(disp, image=image) # stimulus image
                            qstim2 = TextStim(disp, text=pair.word+space+pair.translate, pos=qpos7, height=size, color=color3) # stimulus texte
                            respstim = TextStim(disp, text='', pos=qpos8, height=size, color=color) # stimulus texte
                            qstim.draw() # dessiner la question (image)
                            qstim2.draw() # dessiner la question (pair de mot)
                            respstim.draw() # dessiner la question (user response)
                            disp.flip() # passer au screen au suivant -> on met la question par-dessus
                            core.wait(loadTime) # let psychopy breath...        
                            choice, DLT = tapeAnswer(choice, DLT, True) # tapeAnswer function
                            
                            # --------------------- #
                            # CHECK CHOICE VALIDITY #
                            # --------------------- # 
                            if choice in code_choice.keys(): # if the choice is compatible the dictionnary key
                                pair.choice(code_choice[choice]) # Actualize the properties of the pair word
                            else: # if the kes is not compatible
                                DLT = False # We have to continue the while loop   
                        pair.setFirstTest() # Change firstTest attribute of the pair True
                        
# ----------------------------------------- #
# ENDING : DISPLAY A THANK YOU MESSAGE      #
# SAVE THE NUMBER OF TURNS FOR THE RESULTS  #
# THEN CLOSE THE DISPLAY                    #
# ----------------------------------------- # 
I = i # we save the number of turns the while loop did   
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

with open('retrieval_practice_results_'+ID+'_'+AGE+'_'+SEXE+'_'+DEGRE+'_'+str(datetime.now())+'.csv', 'w') as f: # open a CSV file to write the results
#with open('retrieval_practice_results.csv','w') as f: # open a CSV file to write the results -> 'w' is for 'write' -> we do not open an existing file, but create a new one
    response_header = '\t'.join(['response'+str(i+1) for i in range(I)]) # I is equal to the last iteration of the main while loop => gives one big string containing tabs (\t) thanks to the join function
    f.write('word\ttranslation\t'+response_header+'\t1st_attempt\t1st_success\t1st_failure\tattempt\tsuccess\tfailure\n') # write the header of the table
    for pair in LISTE: # pour chaque pair de mot
        AUR = '\t'.join([pair.allUserResponses[i+1] for i in range(I)]) # AUR = all user responses for this word pair
        f.write(pair.word+'\t'+pair.translate+'\t'+AUR+'\t'+str(pair.firstAttempt)+'\t'+str(pair.firstSuccess)+'\t'+str(pair.firstFail)+'\t'+str(pair.attempt)+'\t'+str(pair.success)+'\t'+str(pair.fail)+'\n') # write all results for the word pair in a row
    f.write(ID+'\n') # add the identification number of the user
    f.write(AGE+'\n') # add the age of the user
    f.write(SEXE+'\n') # add the gender of the user
    f.write(DEGRE+'\n') # add the scholar degree of the user
 
