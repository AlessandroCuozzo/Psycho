#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
#############################################
#############################################
# EXPERIMENTAL PSYCHOLOGY - CONSTANTS & VAR #
#############################################
#############################################
Created on Tue Aug 13 15:39:01 2019

@author: p17620
"""

DISPSIZE = (1366, 768) # (1440, 900) -> the maximum screen size allowed depends on the computer

FGC = (0,5,0.1,0.8)
BGC = (-0.2,-0.5,-1)

dico = {'chat': 'cat', # ascii codec -> ça bug avec les accents
        'chien': 'dog',
        'loup': 'wolf',
        'renard': 'fox'}

"""
{'chat': 'cat', # ascii codec -> ça bug avec les accents
        'chien': 'dog',
        'loup': 'wolf',
        'renard': 'fox',
        'souris': 'mouse',
        'tortue': 'turtle',
        'poisson': 'fish',
        'oiseau': 'bird',
        'lapin': 'rabbit',
        'grenouille': 'frog',
        'crapaud': 'toad',
        'tigre': 'tiger',
        'chauve-souris': 'bat',
        u'araignée': 'spider',
        'fourmille': 'ant',
        u'guêpe': 'wasp',
        'abeille': 'bee',
        'poulpe': 'octopus',
        'baleine': 'whale',
        'serpent': 'snake',
        u'hérisson': 'hedgehog',     
        'singe': 'monkey',
        u'âne': 'donkey',
        'cheval': 'horse'
        }
"""

pretest = 'crocodile' 
code_choice = {'1':'test', '2':'learn', '3':'drop'}
code_choice_reverse={}
for duo in code_choice:
    code_choice_reverse[code_choice[duo]]=duo

results = {}
