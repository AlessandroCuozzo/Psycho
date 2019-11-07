#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
############################################
############################################
## EXPERIMENTAL PSYCHOLOGY - PAIRS - OOP  ##
############################################
############################################
Created on Mon Aug 26 22:01:53 2019

@author: cuozzo
"""

class Pair:
    
    """
    ############
    PAIR CLASS
    ############
    
    CREATE PAIR CLASS CONTAINING 
    
    - **Constructor Input**:
           :word: the french word which is string -> [key from the constants 'dico' dictionnary]
           :translate: the translated string of the word [value from the constants 'dico' dictionnary]
           :attempt: the number of attempt the user will do to achieve a correct translation (starts at zero)
           :wordL: length of the french word
           :translateL: length of the translate word
           :drop: boolean (True or False). Default = False -> will become True once the user decides to drop the pair after a success
           :fail: integer [zero by default] => the number of times the user failed the word pair test
           :success: integer [zero by default] => the number of times the user gives the right answer
           :newTest: boolean [True or False] => Default = False => True when the user will decide to test again the word pair
           :newLearn: boolean [True or False] => Default = False => True when the user will decide to learn again the word pair
           :allUserResponses: dictionnary {1:'', 2:'', 3:'', 4:'', 5:''} that will save all responses attempted by the user 
    
    - **General properties of the person**: 

    """
        
    def __init__(self,word,translate):      
        """
        Constructor of the Pair class
        This function is automatically called when a Pair object is created.
        """    
        # ---------------------- #
        # properties of the pair #
        # ---------------------- #
        self.word = word
        self.translate = translate
        self.attempt = 0 # the number of times the user attempts a response (no matter if failed or succeeded)
        self.user_response = '' # the response the the user will give
        #self.wordL = len(word) # length of the word
        #self.translateL = len(translate) # length of the correct translated word
        #self.user_responseL = len(self.user_response) # length of the user response
        self.drop = False # will become True once the user decides to drop the pair after a success
        self.fail = 0 # the number of times the user failed the word pair test
        self.success = 0 # the number of times the user gives the right answer
        self.test = 0 # maximum 2 times
        self.learn = 0 # maximum 2 times
        self.maxTest = 3 # This value may change during the program according to the user performance -> flexible threshold
        self.maxLearn = 2 # This value will never change -> fixed threshold 
        self.newTest = False # True when the user will decide to test again the word pair
        self.newLearn = False # True when the user will decide to learn again the word pair
        self.allUserResponses = {} # dictionnary that will save all responses attempted by the user 
        
    def addResponse(self,user_response,turn): # call this function every time the user does another translation attempt for the current pair     
        """
        - **Input**:
            :user_response: the answer attempted by the user
            :turn: in which turn of the main loop are we
        """        
        self.attempt += 1 # the user performs a new attempt
        self.user_response = user_response.lower().strip() # on set tous les caractères en minuscule ET on enlève les éventuels espaces au début et à la fin du mot (pour réduire les éventuels biais dus aux erreurs de frappe)
        #self.user_responseL = len(self.user_response) 
        self.allUserResponses[turn] = self.user_response # save the response in the responses dictionnary to keep track
        
    def resetResponse(self):      
        """
        Reset the user response for a new test / attempt
        """
        self.user_response = ''
        #self.user_responseL = len(self.user_response)
        
    def checkAnswer(self):       
        """
        Check if the user's response is correct
        """
        if self.translate == self.user_response:
            return True
        else:
            return False
        
    def addLearn(self,turn):
        """
        Fill the allUserResponses with **LEARN** for the actual turn
        - **Input**:
            :turn: in which turn of the main loop are we
        """
        self.allUserResponses[turn] = '**LEARN**' # save the response in the responses dictionnary to keep track
        
    def addDrop(self,turn):
        """
        Fill the allUserResponses with **DROPPED** for the actual turn
        - **Input**:
            :turn: in which turn of the main loop are we
        """
        self.allUserResponses[turn] = '**DROPPED**' # save the response in the responses dictionnary to keep track
        
    def addFinish(self,turn):
        """
        Fill the allUserResponses with **FINISHED** for the actual turn
        - **Input**:
            :turn: in which turn of the main loop are we
        """
        self.allUserResponses[turn] = '**FINISHED**' # save the response in the responses dictionnary to keep track
        
    def addFail(self):   
        """
        1) Actualize the number of failure for the word pair.
        2) Set the pair word for another testing.
        3) Increases the threshold of maximum testing if the user did not have have a single correct answer yet.
        """
        self.fail += 1 # Actualize the number of failure for the word pair.
        self.newTest = True # after a wrong answer, the user will have to try again ; we want him to give the correct answer at least once !
        if self.success==0: # If the user did not have have a single correct answer yet
            self.maxTest += 1 # increases the threshold of maximum testing
    
    def addSuccess(self):     
        """
        Actualize the number of success for the word pair
        """
        self.success += 1
        
    def choice(self,user_choice):       
        """
        function called when the user will choose to drop, learn or test again a word pair -> only if the user response translation is correct
        - **Input**:
            :user_response: the answer attempted by the user
            :turn: in which turn of the main loop are we
        """
        if user_choice == 'test':
            self.newTest = True
        elif user_choice =='drop':
            self.drop = True
        else: # user_choice == 'learn'
            self.newLearn = True
    
    def setTest(self):       
        """
        set lest = test + 1
        """       
        self.test += 1 #  The threshold is maxTest
        
    def setLearn(self):       
        """
        reset Learn = learn + 1
        """       
        self.learn += 1 # The threshold is maxLearn