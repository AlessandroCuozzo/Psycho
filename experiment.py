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
from constants import DISPSIZE, dico, code_choice, code_choice_reverse # import the pre-determined constants
from pairs import Pair # import the Pair class with its methods
from psychopy.visual import Window, TextStim
from psychopy.event import waitKeys
from psychopy import core
from random import shuffle # the random module allows to use many hazard-related functions
from datetime import datetime


# --------------------------------- #
# Create all the word pairs objects #
# --------------------------------- # 
LISTE = [] # empty list which will contain all the pair objects
for pair in dico: # pour chaque pair de mots présente dans le dictionnaire du fichier 'constants'
    LISTE.append(Pair(pair,dico[pair])) # pair is the dico key (french word) ; dico[pair] is the value of the key (corresponding translated word)
shuffle(LISTE) # mélange la liste de mots -> ordre au hasard


# --------------- #
# visual settings #
# --------------- # 
disp = Window (size=DISPSIZE, units='pix', fullscr=True) # créer une fenêtre pour montrer des choses à l'écran => unité est en Pixel
question = 'Vous aurez 10 secondes pour apprendre chaque pair de mots' # créer une question
qpos= (0, int(DISPSIZE[1]*0.2)) # position de la question
qstim = TextStim(disp, text=question, pos=qpos, height=24) # stimulus texte
qstim.draw() # dessiner la question
disp.flip() # passer au screen au suivant -> on met la question par-dessus
core.wait(5) # delay of 10 seconds before passing to the learning phase


##################
##################
# LEARNING PHASE #
##################
##################
for pair in LISTE: # pour chaque pair de mot
    learn = pair.word+'\t\t\t'+pair.translate # le mot en français + 3 tabs (espacements + la traduction)
    qpos= (0, int(DISPSIZE[1]*0.2)) # position de la question
    qstim = TextStim(disp, text=learn, pos=qpos, height=24) # stimulus texte
    qstim.draw() # dessiner la pair de mots
    disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
    core.wait(5) # delay of 10 seconds before passing to the next pair


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

# -------------------------- #
# testing phase instructions #
# -------------------------- # 
question = 'Vous aurez 10 secondes pour traduire chaque mot' # créer une question
qpos= (0, int(DISPSIZE[1]*0.2)) # position de la question
qstim = TextStim(disp, text=question, pos=qpos, height=24) # stimulus texte / 24 pixels
qstim.draw() # dessiner la question
disp.flip() # passer au screen au suivant -> on met la question par-dessus
core.wait(5) # delay of 10 seconds before passing to the learning phase

# --------------------------------------------------------------- #
# FIRST MAIN LOOP - THE STEP 2 CAN BE REPEATED AT MAXIMUM 5 TIMES #
# --------------------------------------------------------------- # 
for i in range(5): # i will be reused to know at which turn of the loop we are for each response (to save in the results)

    # ------------------------------------------------------------------------- #
    # SECOND MAIN LOOP - FOR EACH WORD                                          #
    # Check if the user previously decided to drop, learn or test the word pair #
    # ------------------------------------------------------------------------- #
    shuffle(LISTE)
    for pair in LISTE: # pour chaque pair de mot
        if pair.drop == True: # if the user decided to drop the word pair during the previous loop turn
            pair.addDrop(i+1) # Fill the pair object allUserResponses attribute with **DROPPED** for the actual turn -> will actually do the same for each remaining turns
        else: # if the user did NOT decide to drop the word pair during the previous loop turn
            
            # ---------------------- #
            # LEARNING THE PAIR WORD #
            # ---------------------- #
            if pair.newLearn == True and pair.newTest == False and i>0: # the user chose to learn this pair and not test it during the previous loop turn OR if it is not the very first loop turn
                qstim = TextStim(disp, text=learn, pos=qpos, height=24) # stimulus texte
                qstim.draw() # dessiner la pair de mots
                disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
                core.wait(5) # delay of 10 seconds before passing to the next pair
                pair.addLearn(i+1) # Fill the pair object allUserResponses attribute with **LEARN** for the actual turn
                pair.resetNewLearn() # reset the pair newTLearn property to False
                pair.setNewTestAfterLearn() # If the user has decided to learn the word pair, we must still set the newTest for the next loop turn
                
            
            
            # --------------------- #
            # TESTING THE PAIR WORD #
            # --------------------- #
            else: # the user chose to test the word pair   
                pair.resetResponse() # reset the response for a new attempt
                test = pair.word+'\t\t 1ere lettre = '+pair.translate[0] # le mot en français
                qstim = TextStim(disp, text=test, pos=qpos, height=24) # stimulus texte
                qstim.draw() # dessiner la pair de mots
                disp.flip() # passer au screen au suivant -> on met la pair de mots par-dessus
                core.wait(0.01) # delay of 10 seconds before passing to the next pair
                respstim = TextStim(disp, text='', height=24) # boite réponse (to be completed by the user)
                response = '' # the response attempted by the user - On commence avec une réponse vide
                done = False # On commence undone (sujet n'a pas terminé, i.e. n'a pas fait enter)
                DLT = False # Drop / Learn / Test
                pair.resetNewTest() # reset the pair newTest property to False
        
                # ----------------------------------------------------- #
                # THIRD MAIN LOOP - WHILE THE USER'S ANSWER IS NOT DONE #
                # Check for keypresses                                  #
                # ----------------------------------------------------- # 
                while not done: # loop until done == True
                    resplist = waitKeys (maxWait=float('inf'), keyList=None, timeStamped=True)
                    key, presstime = resplist[0] # use only the first in the returned list of keypresses -> resplist[0] is the first element in the resplist list   
                    if len(key) == 1: # Check si la longeur de la réponse (len) = 1
                        response += key #Ajouter la lettre tapée à la réponse
                    elif key == 'space': # Check if key is the space bar
                        response += ' ' # ajoute un espace
                    elif key == 'backspace' and len(response) > 0: # Check if the key's name was backspace AND si la réponse a au moins une lettre
                        response = response[0:-1] #remove last character of the response
                    if key == 'return': # if the key was non of the above, check si c'est enter
                        done = True # set done to True
                    respstim.setText(response) # actualiser la user response
                    qstim.draw() # réafficher la question stimulus
                    respstim.draw() # réafficher la réponse au stimulus
                    disp.flip() # update the monitor
                    core.wait(0.01) # add a little lag to avoid little freez and/or bug
        
                # ------------------------------------------------------ #
                # ADD THE USER USER RESPONSE IN THE PAIR OBJECT          #
                # RESPONSE CHECK - WHAT ACTION THE SUBJECT WILL CHOOSE ? #
                # SHOW THE RESPONSE AND CORRECT ANSWER TO THE USER       #
                # ------------------------------------------------------ #
                pair.addResponse(response,i+1) # add the user response in the pair object (no matter if the response is correct or wrong)
                check = 'traduction = '+pair.translate+'\n votre reponse = '+pair.user_response # créer une question
                qpos= (0, int(DISPSIZE[1]*0.2)) # position de la question
                qstim = TextStim(disp, text=check, pos=qpos, height=24) # stimulus texte
                qstim.draw() # dessiner la question
                disp.flip() # passer au screen au suivant -> on met la question par-dessus
                core.wait(2) # delay of 10 seconds before passing to the learning phase
        
                # ------------------------------------------------------------- #
                # CHECK IF THE USER RESPONSE IS CORRECT OR WRONG                #
                # let the user choose what he wants do to : Test / Learn / Drop # 
                # ------------------------------------------------------------- #
                if pair.checkAnswer()==True: # if the answer is correct
                    pair.addSuccess() # success = success + 1
                    choose = 'test=1\t\t\tlearn=2\t\t\tdrop=3' # L'utilisateur choisit s'il veut drop, learn ou test
                    qstim = TextStim(disp, text=choose, pos=qpos, height=24) # stimulus texte
                    qstim.draw() # dessiner la question
                    disp.flip() # passer au screen au suivant -> on met la question par-dessus
                    core.wait(0.01) # delay of 10 seconds before passing to the learning phase
            
                    # ----------------------------------------------------------- #
                    # THE USER WILL CHOOSE TO TEST, LEARN AGAIN OR DROP THZE PAIR #
                    # FOURTH MAIN LOOP - WHILE THE USER'S CHOICE IS NOT DONE      #
                    # Check for keypresses                                        #
                    # ----------------------------------------------------------- # 
                    choice = '' # the chocie selected by the user - On commence avec une chaîne vide
                    choicestim = TextStim(disp, text='', height=24) # stimulus texte
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
                        core.wait(0.01) # add a little lag to avoid little freez and/or bug
                    pair.choice(code_choice[choice]) # Actualize the properties of the pair word
                    
                # ----------------------------- #
                # CASE IF THE RESPONSE IS WRONG #
                # ----------------------------- # 
                else:
                    pair.addFail() # fail = fail + 1
                    """
                    to implement here:
                    display some message to the user ?
                    What do we do if the answer is wrong right off the bat ? Do we make it learn 
                    ACTUALLY : WHEN THE USER IS WRONG, THE PROGRAMM AUTOMATICALLY MAKES HIM LEARN AGAIN
                    DO WE STICK WITH THAT ?
                    """
            
disp.close() # close the display 
            

#################
#################
# SAVE RESULTS  #
#################
#################
#with open('retrieval_practice_results_'+str(datetime.now())+'.csv') as f: # open a CSV file to write the results
with open('retrieval_practice_results.csv','w') as f: # open a CSV file to write the results -> 'w' is for 'write' -> we do not open an existing file, but create a new one
    f.write('word\ttranslation\tresponse1\tresponse2\tresponse3\tresponse4\tresponse5\tattempts\tsuccesses\tfailures\n') # write the header of the table
    for pair in LISTE: # pour chaque pair de mot
        f.write(pair.word+'\t'+pair.translate+'\t'+pair.allUserResponses[1]+'\t'+pair.allUserResponses[2]+'\t'+pair.allUserResponses[3]+'\t'+pair.allUserResponses[4]+'\t'+pair.allUserResponses[5]+'\t'+str(pair.attempt)+'\t'+str(pair.success)+'\t'+str(pair.fail)+'\n') # write all results for the word pair in a row
        
#################
#################
#  FINAL TEST   #
#################
#################
        
