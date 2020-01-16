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
        :word: the that the user will try to translate
        :translate: the correct translation of the word

    - **General properties of the pair**: 
        :word: the french word which is string -> [key from the constants 'dico' dictionnary]
        :translate: the translated string of the word [value from the constants 'dico' dictionnary]
        :firstTest: Boolean -> Will be True once the user gives the first correct answer (False by default)
        :firstAttempt: The number of times the user needed to answer correctly to the very 1st test
        :firstSuccess: The number of times the user succeeded to the first test -> will never be higher than 1 at the current version of this program
        :firstFail: The number of times the user failed before giving its first correct answer
        :attempt: the number of attempt the user will do to achieve a correct translation (starts at zero)
        :wordL: length of the french word
        :translateL: length of the translate word
        :drop: boolean (True or False). Default = False -> will become True once the user decides to drop the pair after a success
        :fail: integer [zero by default] => the number of times the user failed the word pair test
        :success: integer [zero by default] => the number of times the user gives the right answer
        :maxTest: maximum number of times the user will be tested after having chosen to be
        :maxLearn: maximum number of times the user will learn again a word pair after having chosen it
        :newTest: boolean [True or False] => Default = False => True when the user will decide to test again the word pair
        :newLearn: boolean [True or False] => Default = False => True when the user will decide to learn again the word pair
        :allUserResponses: dictionnary {} that will save all responses attempted by the user 
    
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
        self.firstTest = False # Will be True once the user gives the first correct answer
        self.firstAttempt = 0 # The number of times the user needed to answer correctly to the very 1st test
        self.firstSuccess = 0 # The number of times the user succeeded to the first test -> will never be higher than 1 at the current version of this program
        self.firstFail = 0 # The number of times the user failed before giving its first correct answer
        self.attempt = 0 # the number of times the user attempts a response (no matter if failed or succeeded) | WARNING: not taking into account the very forst test that enables the user to make his choice between Test / Learn / Drop
        self.user_response = '' # the response the the user will give
        #self.wordL = len(word) # length of the word
        #self.translateL = len(translate) # length of the correct translated word
        #self.user_responseL = len(self.user_response) # length of the user response
        self.drop = False # will become True once the user decides to drop the pair after a success
        self.fail = 0 # the number of times the user failed the word pair test
        self.success = 0 # the number of times the user gives the right answer
        self.test = 0 # maximum 2 times
        self.learn = 0 # maximum 2 times
        self.maxTest = 2 # this value will never change -> fixed threshold
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
        if self.firstTest==True: # if we are already in the step following the user's choice
            self.attempt += 1 # the user performs a new attempt
        else: # if the user did not give a correct answer yet
            self.firstAttempt += 1 # actualize the first attempt counter
        self.user_response = user_response.lower().strip() # on set tous les caractères en minuscule ET on enlève les éventuels espaces au début et à la fin du mot (pour réduire les éventuels biais dus aux erreurs de frappe)
        #self.user_responseL = len(self.user_response) 
        self.allUserResponses[turn] = "**TEST** "+self.user_response # save the response in the responses dictionnary to keep track
        
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
        """
        if self.firstTest==True: # if we are already in the step following the user's choice
            self.fail += 1 # Actualize the number of failure(s) for the word pair.
        else: # if the user still did not have a single correct answer yet
            self.firstFail += 1 # Actualize the number of 1st failure(s) for the word pair.
        self.newTest = True # after a wrong answer, the user will have to try again ; we want him to give the correct answer at least once !
    
    def addSuccess(self):     
        """
        Actualize the number of success for the word pair
        """
        if self.firstTest==True: # if we are already in the step following the user's choice
            self.success += 1
        else: # if the user still did not have a single correct answer yet
            self.firstSuccess += 1
        
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
        if self.firstTest==True: # if we are already testing AFTER the user's choice
            self.test += 1 #  The threshold is maxTest
        
    def setLearn(self):       
        """
        set Learn = learn + 1
        """       
        self.learn += 1 # The threshold is maxLearn
        
    def setFirstTest(self):
        """
        Set the firstTest attribute True once the user has answered correctly for the first time
        """
        self.firstTest = True