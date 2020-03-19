#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
############################################
############################################
EXPERIMENTAL PSYCHOLOGY - RETRIEVAL PRACTICE
############################################
############################################
Created on Tue Aug 13 15:42:22 2019

@author: p17620
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


# ------------------------------------------------------------------------------------------------- #
# Function that will be called every time the user needs to press a key to pass to the next display #
# Double while loop                                                                                 #
# ------------------------------------------------------------------------------------------------- #
def userResponse(response, done, qpos, size, disp, image, multi):
    """
    function called when the user will choose to drop, learn or test again a word pair -> only if the user response translation is correct
    - **Input**:
        :response: the user resonse (empty string at beginning)
        :done: boolean (True / False) -> False at beginning
        :qpos: text position for user response
        :size: text size for user response
        :disp: the psychopy display screen
        :image: the stimulus image
        :multi: multiple display ? boolean (True or False)
    """
    
    # --------------------------------------- #
    # WHILE THE WELCOME MESSAGE IS NOT PASSED #
    # --------------------------------------- #
    while len(response)==0: # while the user has not taped anything yet
        response = '' # the response written by the user - On commence avec une chaîne vide
        respstim = TextStim(disp, text='', pos=qpos, height=size) # stimulus texte  
        qstim = ImageStim(disp, image=image)
        qstim.draw() # dessiner la question
        if multi==True:
            qstim2.draw()
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
            


# ----------------------------------- #
# WELCOME - Initial & Visual settings #
# ----------------------------------- # 
feedback = True # can be set to True or False
firstLetter = True # can be set to True or False
disp = Window (size=DISPSIZE, units='pix', fullscr=True) # créer une fenêtre pour montrer des choses à l'écran => unité est en Pixel
#size = 24 # text size # 36
size = 36 # text size # 36
color = 'darkblue' # text color
color2 = 'crimson' # text color
color3 = 'green' # text color
space = '\t\t\t\t' # space between the word and its translation when learning
learnTime = 1 # time to given to memorize one pair word
loadTime = 0.01 # time for spychopy displaying
qpos = (0,int(DISPSIZE[1]*-0.2)) # position de la question
qpos2 = (int(DISPSIZE[0]*-0.02),int(DISPSIZE[1]*-0.02)) # position de la question
qpos3 = (int(DISPSIZE[0]*-0.2),int(DISPSIZE[1]*-0.05)) # position de la question
qpos4 = (int(DISPSIZE[0]*-0.03),int(DISPSIZE[1]*-0.015)) # position de la question
qpos5 = (int(DISPSIZE[0]*0.05),int(DISPSIZE[1]*-0.15)) # position de la question
userResponse('', False, qpos, size, disp, 'images/img1.gif', False) # call the userResponse -> double while loop to save the user traped response

# ----------------------------------- #
# SETTING FOR THE PRE-TEST            #
# WHILE THE PRE-TEST IS NOT SUCCEEDED #
# ----------------------------------- #
response = '' # the response attempted by the user - On commence avec une réponse vide
while response != pretest: # while the answer is not correct
    response = '' # the response written by the user - On commence avec une chaîne vide
    respstim = TextStim(disp, text='', pos=qpos, height=size, color=color) # stimulus texte  
    qstim = ImageStim(disp, image='images/img2.gif')
    qstim.draw() # dessiner la question
    disp.flip() # passer au screen au suivant -> on met la question par-dessus
    core.wait(0.01) # delay of 10 seconds before passing to the learning phase
    response, done = tapeAnswer(response, False, False) # While loop to taping the entire answer

    # ------------------------------------------------------- #
    # CHECK IF THE PRETEST IS SUCCEEDED OR NOT                #
    # DISPLAY A MESSAGE TO THE USER ACCORDING TO THE ANSWER   #
    # ------------------------------------------------------- #
    if response==pretest: # if the answer is correct 
        userResponse('', False, qpos, size, disp, 'images/img3.gif', False) # call the userResponse -> double while loop to save the user traped response
    else: # if the answer is NOT correct 
        userResponse('', False, qpos, size, disp, 'images/img4.gif', False) # call the userResponse -> double while loop to save the user traped response
    
        
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
userResponse('', False, qpos, size, disp, 'images/img5.gif', False) # call the userResponse -> double while loop to save the user traped response
for pair in LISTE: # pour chaque pair de mot
    learn = pair.word+space+pair.translate # le mot en français + 3 tabs (espacements + la traduction)
    qstim = ImageStim(disp, image='images/img10.gif')
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

"""
# -------------------------- #
# testing phase instructions #
# -------------------------- # 
question = 'Vous aurez 10 secondes pour traduire chaque mot.' # créer une question
qstim = TextStim(disp, text=question, pos=qpos, height=size) # stimulus texte / 24 pixels
qstim.draw() # dessiner la question
disp.flip() # passer au screen au suivant -> on met la question par-dessus
core.wait(5) # delay of 10 seconds before passing to the learning phase
"""

# ----------------------------------------------------------------------------------- #
# FIRST MAIN LOOP - THIS STEP IS REPEATED UNTIL THE USER IS DONE WITH EVERY WORD PAIR #
# ----------------------------------------------------------------------------------- # 
i = 0
while len(CORRECT_SET)<len(LISTE): # Until the user gives the correct answer to every pair at least once 
    i += 1 # number of turns of the loop => i will be reused to know at which turn of the loop we are for each response (to save in the results)
    
    # ------------------------------------------------------------------------- #
    # SECOND MAIN LOOP - FOR EACH WORD                                          #
    # Check if the user previously decided to drop, learn or test the word pair #
    # ------------------------------------------------------------------------- #
    shuffle(LISTE)
    for pair in LISTE: # pour chaque pair de mot
        if pair.drop==True or (pair.newTest==True and pair.test==pair.maxTest) or (pair.newLearn==True and pair.learn==pair.maxLearn): # if we are done with the present pair
            CORRECT_SET.add(pair.word) # we add it in the set containing all pairs we won't have to deal with again
            if pair.drop == True: # if the user decided to drop the word pair during the previous loop turn
                pair.addDrop(i) # Fill the pair object allUserResponses attribute with **DROPPED** for the actual turn -> will actually do the same for each remaining turns
            else: # if the user is done with this pair word, but it did not drop it -> he 'finished'
                pair.addFinish(i) # Fill the pair object allUserResponses attribute with **FINISHED** for the actual turn -> will actually do the same for each remaining turns
        else: # if the user did NOT decide to drop the word pair during the previous loop turn
            
            # ---------------------- #
            # LEARNING THE PAIR WORD #
            # ---------------------- #
            if pair.newLearn==True and pair.learn<pair.maxLearn: # the user chose to learn this pair after its first correct answer AND if he has not reached the learning threshold yet
                learn = pair.word+space+pair.translate # le mot en français + 3 tabs (espacements + la traduction)
                learn = pair.word+space+pair.translate # le mot en français + 3 tabs (espacements + la traduction)
                qstim = ImageStim(disp, image='images/img10.gif')
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
                print(response)
                qstim = ImageStim(disp, image='images/img11.gif') # stimulus image
                qstim2 = TextStim(disp, text=pair.word, pos=qpos3, height=size, color=color) # stimulus texte
                respstim = TextStim(disp, text=response, pos=qpos, height=size, color=color) # boite réponse (to be completed by the user)
                respstim.setText(response) # actualiser la user response => 1ère lettre en majuscule
                qstim.draw() # dessiner la pair de mots (image)
                qstim2.draw() # dessiner la pair de mots (image)
                respstim.draw() # Draw the translation response
                disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
                core.wait(loadTime) # delay of 10 seconds before passing to the next pair
                DLT = False # Drop / Learn / Test
                pair.setTest() # actualize the test property of the pair object
                response, done = tapeAnswer(response, False, True) # While loop to taping the entire answer
                 
                # ------------------------------------------------------ #
                # ADD THE USER RESPONSE IN THE PAIR OBJECT               #
                # CHECK IF WE ARE STILL IN THE FIRST TEST FOR THIS PAIR  #
                # SHOW THE RESPONSE AND CORRECT ANSWER TO THE USER       #
                # ------------------------------------------------------ #
                pair.addResponse(response,i) # add the user response in the pair object (no matter if the response is correct or wrong)
                
                """
                if pair.firstTest == False: # If it is the very first time the user gives the correct answer
                    if feedback==True: # Does the subject benefits of a feed back after an answer ?
                        check = 'traduction = '+pair.translate+u'\n votre réponse = '+pair.user_response+'\n\n' # créer une question
                        #qpos= (0, int(DISPSIZE[1]*0.2)) # position de la question
                        #qstim = TextStim(disp, text=check, pos=qpos, height=24) # stimulus texte
                        #qstim.draw() # dessiner la question
                        #disp.flip() # passer au screen au suivant -> on met la question par-dessus
                        #core.wait(2) # delay of 10 seconds before passing to the learning phase
                    else: # In case this is not the first test
                        check = '' # we set an empty string for check -> we need it to display both the user answer and the Bravo/Wrong phrase in the same screen
                """
                
                # ------------------------------------------------------------------ #
                # RESPONSE CHECK - WHAT ACTION THE SUBJECT WILL CHOOSE ?             #
                # CHECK IF THE USER RESPONSE IS CORRECT OR WRONG                     #
                # CHECK IF WE DECIDED TO GIVE A FEEDBACK OR NOT                      #
                # ADD SUCCESS OR FAILURE IN THE WORD PAIR OBJECT ACCORDING TO CHECK  #
                # ------------------------------------------------------------------ #
                if pair.checkAnswer()==False: # if the answer is NOT correct 
                    pair.addFail() # fail = fail + 1 | => Will also set the word pair for a new test | => increases the threshold of maximum testing
                    if feedback==True: # Does the subject benefits of a feed back after an answer ?
                        image = 'images/img17.gif' # Ooups image
                        qstim = ImageStim(disp, image=image) # stimulus image
                        qstim2 = TextStim(disp, text=pair.word+space+pair.translate, pos=qpos4, height=size, color=color) # stimulus texte
                        qstim3 = TextStim(disp, text=pair.user_response, pos=qpos5, height=size, color=color2) # stimulus texte
                        #check += u'Vous n\'avez malheureusement pas écrit le bon mot.' # Add Wrong to check
                        #qstim = TextStim(disp, text=check, pos=qpos, height=size) # stimulus texte
                        qstim.draw() # dessiner la question (image)
                        qstim2.draw() # dessiner la question (pair de mot)
                        qstim3.draw() # dessiner la question (user response)
                        disp.flip() # passer au screen au suivant -> on met la question par-dessus
                        userResponse('', False, qpos, size, disp, image, True) # call the userResponse -> double while loop to save the user traped response
                        #core.wait(5) # delay of 10 seconds before passing to the learning phase
                    
                else: # if the answer is correct 
                    pair.addSuccess() # success = success + 1    
                    if feedback==True: # Does the subject benefits of a feed back after an answer ?
                        image = 'images/img18.gif' # Bravo image
                        qstim = ImageStim(disp, image=image) # stimulus image
                        qstim2 = TextStim(disp, text=pair.word+space+pair.translate, pos=qpos4, height=size, color=color) # stimulus texte
                        qstim3 = TextStim(disp, text=pair.user_response, pos=qpos5, height=size, color=color2) # stimulus texte
                        #check += u'Bravo ! Vous avez écrit correctement le bon mot.' # Add Bravo to check
                        #qstim = TextStim(disp, text=check, pos=qpos, height=size) # stimulus texte
                        qstim.draw() # dessiner la question (image)
                        qstim2.draw() # dessiner la question (pair de mot)
                        qstim3.draw() # dessiner la question (user response)
                        disp.flip() # passer au screen au suivant -> on met la question par-dessus
                        userResponse('', False, qpos, size, disp, image, True) # call the userResponse -> double while loop to save the user traped response
                        #core.wait(5) # delay of 10 seconds before passing to the learning phase
                    
                    
                    # --------------------------------------------------------------- #
                    # CASE IF IT IS THE FIRST TIME THE USER GIVES THE CORRECT ANSWER  #
                    # FOURTH MAIN LOOP ; WHILE THE CHOICE CANNOT BE INTERPRETED       #
                    # let the user choose what he wants do to : Test / Learn / Drop   #
                    # --------------------------------------------------------------- # 
                    if pair.firstTest == False: # If it is the very first time the user gives the correct answer
                        choose = 'test=1\t\t\tlearn=2\t\t\tdrop=3' # L'utilisateur choisit s'il veut drop, learn ou test       
                        choice = '' # the chocie selected by the user - On commence avec une chaîne vide
                        while choice not in code_choice.keys(): # while the choice is not one understood by thze program (other than 1,2 or 3)
                            choice = '' # the chocie selected by the user - On commence avec une chaîne vide
                            choicestim = TextStim(disp, text='', height=size) # stimulus texte  
                            qstim = TextStim(disp, text=choose, pos=qpos, height=size) # stimulus texte
                            qstim.draw() # dessiner la question
                            disp.flip() # passer au screen au suivant -> on met la question par-dessus
                            core.wait(loadTime) # delay of 10 seconds before passing to the learning phase
                            
                            # ----------------------------------------------------------- #
                            # THE USER WILL CHOOSE TO TEST, LEARN AGAIN OR DROP THZE PAIR #
                            # FIFTTH MAIN LOOP - WHILE THE USER'S CHOICE IS NOT DONE      #
                            # Check for keypresses                                        #
                            # ----------------------------------------------------------- # 
                            while not DLT: # loop DLT done == True
                                resplist = waitKeys (maxWait=float('inf'), keyList=None, timeStamped=True)
                                key, presstime = resplist[0] # use only the first in the returned list of keypresses -> resplist[0] is the first element in the resplist list   
                                if len(key) == 1: # Check si la longeur de la réponse (len) = 1
                                    choice += key #Ajouter la lettre tapée à la réponse
                                elif key == 'space': # Check if key is the space bar
                                    choice += ' ' # ajoute un espace
                                elif key == 'backspace' and len(choice) > 0: # Check if the key's name was backspace AND si la réponse a au moins une lettre
                                    choice = choice[0:-1] # remove last character of the response
                                if key == 'return': # if the key was non of the above, check si c'est enter
                                    DLT = True # set DLT to True
                                choicestim.setText(choice) # update the response stimulus
                                qstim.draw() # RE-dessiner la question car elle va disparaitre avec flip
                                choicestim.draw() # dessiner le stimulus réponse
                                disp.flip() # update the monitor
                                core.wait(loadTime) # add a little lag to avoid little freez and/or bug
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
qstim = ImageStim(disp, image='images/img8.gif')
qstim.draw() # dessiner la question
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

#with open('retrieval_practice_results_'+str(datetime.now())+'.csv') as f: # open a CSV file to write the results
with open('retrieval_practice_results.csv','w') as f: # open a CSV file to write the results -> 'w' is for 'write' -> we do not open an existing file, but create a new one
    response_header = '\t'.join(['response'+str(i+1) for i in range(I)]) # I is equal to the last iteration of the main while loop => gives one big string containing tabs (\t) thanks to the join function
    f.write('word\ttranslation\t'+response_header+'\t1st_attempt\t1st_success\t1st_failure\tattempt\tsuccess\tfailure\n') # write the header of the table
    for pair in LISTE: # pour chaque pair de mot
        AUR = '\t'.join([pair.allUserResponses[i+1] for i in range(I)]) # AUR = all user responses for this word pair
        f.write(pair.word+'\t'+pair.translate+'\t'+AUR+'\t'+str(pair.firstAttempt)+'\t'+str(pair.firstSuccess)+'\t'+str(pair.firstFail)+'\t'+str(pair.attempt)+'\t'+str(pair.success)+'\t'+str(pair.fail)+'\n') # write all results for the word pair in a row

 
#################
#################
#  FINAL TEST   #
#################
#################
        
