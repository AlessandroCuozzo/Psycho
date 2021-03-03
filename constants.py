#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#############################################
#############################################
# EXPERIMENTAL PSYCHOLOGY - CONSTANTS & VAR #
#############################################
#############################################
Created on Tue Aug 13 15:39:01 2019

@author: Cuozzo, Tardif (p42299, p17620)
"""

"""
# ---------------------- #
# MONITOR SIZE - Windows #
# ---------------------- #
import ctypes # import ctypes module
user32 = ctypes.windll.user32 # Get infos on the user
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # a tuple containing monitor resolution
width = str(screensize[0]) # string value of width screen resolution
height = str(screensize[1]) # string value of height screen resolution

# ------------------------------- #
# MONITOR SIZE - Windows / Ubuntu #
# ------------------------------- #
from screeninfo import get_monitors # PyPI downloaded module to automatically get the monitor resolution | pip install screeninfo [from terminal]

width = str(get_monitors()[0]).split(',')[2].split('=')[1] # string value of width screen resolution
height = str(get_monitors()[0]).split(',')[3].split('=')[1] # string value of width screen resolution
"""

"""
# ------------------ #
# MONITOR SIZE - Mac #
# ------------------ #
import AppKit # Python module in Mac | pip install AppKit (from terminal)
listMonitors = [(screen.frame().size.width, screen.frame().size.height) for screen in AppKit.NSScreen.screens()] # list of all eventual monitors
monitor = listMonitors[0] # first monitor
width = str(monitor)[0] # string value of width screen resolution
height = str(monitor)[1] # string value of height screen resolution
"""

# --------------------- #
# MONITOR SIZE - Ubuntu #
# --------------------- #
import subprocess

def get_screen_resolution():
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0] # call a bash command to get monitor infos (Ubuntu)
    # output = subprocess.Popen("system_profiler SPDisplaysDataType | awk '/Resolution/{print $2, $3, $4}'",shell=True, stdout=subprocess.PIPE).communicate()[0] # call a bash command to get monitor infos (Mac)
    resolution = output.split()[0].split(b'x') # isolate monitor size / resolution (Linux)
    # resolution = str(output).split("'")[1].split('\\n')[0].split(' x ') # isolate monitor size / resolution (Mac)
    return {'width': resolution[0], 'height': resolution[1]} # dictionnary of resolution

width = int(get_screen_resolution()['width']) # integer value of width screen resolution
height = int(get_screen_resolution()['height']) # integer value of height screen resolution


DISPSIZE = (width, height) # (1366, 768) # (1440, 900) -> the maximum screen size allowed depends on the computer
#DISPSIZE = (1366, 768)

#FGC = (0,5,0.1,0.8)
#BGC = (-0.2,-0.5,-1)



# ------------------------------------- #
# Mots Hongrois - 1ère lettre Majuscule #
# ------------------------------------- #


dicoF = {'Poulet': 'Csirke',
 'Fromage': 'Sajt',
 'Poivre': 'Bors',
 'Glace': 'Fagyi',
 'Eau': 'Viz',
 'Loup': 'Farkas',
 'Baleine': 'Cet',
 'Marcher': 'Menni',
 'Courir': 'Rohan',
 'Aboyer': 'Ugat',
 'Page': 'Oldal',
 'Stylo': 'Toll',
 'Apprendre': 'Tanulni',
 'Oeil': 'Szem',
 'Cheveux': 'Haj',
}

#dicoF = {'Poulet': 'Csirke'}

"""
dico = {'Poulet': 'Csirke',
 'Fromage': 'Sajt',
 'Poivre': 'Bors',
 'Glace': 'Fagyi',
 'Eau': 'Viz',
 'Loup': 'Farkas',
 'Baleine': 'Cet',
 'Marcher': 'Menni',
 'Courir': 'Rohan',
 'Aboyer': 'Ugat',
 'Page': 'Oldal',
 'Stylo': 'Toll',
 'Apprendre': 'Tanulni',
 'Oeil': 'Szem',
 'Cheveux': 'Haj',
 'Nez': 'Orr',
 'Argent': 'Penz',
 'Gagner': 'Nyer',
 'Perdre': 'Veszt',
 'Homme': 'Ember',
 'Enfant': 'Gyerek',
 'Chambre': 'Szoba',
 'Table': 'Asztal',
 'Cuisine': 'Konyha',
 'Dormir': 'Aludni',
 u'Médecin': 'Orvos',
 'Soldat': 'Katona',
 'Cuisinier': 'Kukta',
 'Billet': 'Yegy',
 'Train': 'Vonat',
 'Chemise': 'Ing',
 'Mettre': 'Tesz',
 'Veste': 'Dzseki',
 'Magasin': 'Bolt',
 u'Marché': 'Piac',
 'Conduire': 'Vezet',
 u'Océan': 'Tenger',
 u'Tempête': 'Vihar',
 'Pousser': 'Nyom',
 'Respirer': 'Lehel'
}
"""

dico = {}
for key in dicoF.keys():
    value = dicoF[key]
    dico[value] = key
    
# ------------------------------ #
# Mots Hongrois - tout minuscule #
# ------------------------------ #

"""
dico = {'poulet': 'csirke',
 'fromage': 'sajt',
 'poivre': 'bors',
 'glace': 'fagyi',
 'eau': 'viz',
'loup': 'farkas',
 'baleine': 'cet',
 'marcher': 'menni',
 'courir': 'rohan',
 'aboyer': 'ugat',
 'page': 'oldal',
 'stylo': 'toll',
 'apprendre': 'tanulni',
 'oeil': 'szem',
 'cheveux': 'haj',
 'nez': 'orr',
 'argent': 'penz',
 'gagner': 'nyer',
 'perdre': 'veszt',
 'homme': 'ember',
 'enfant': 'gyerek',
 'chambre': 'szoba',
 'table': 'asztal',
 'cuisine': 'konyha',
 'dormir': 'aludni',
 u'médecin': 'orvos',
 'soldat': 'katona',
 'cuisinier': 'kukta',
 'billet': 'yegy',
 'train': 'vonat',
 'chemise': 'ing',
 'mettre': 'tesz',
 'veste': 'dzseki',
 'magasin': 'bolt',
 u'marché': 'piac',
 'conduire': 'vezet',
 u'océan': 'tenger',
 u'tempête': 'vihar',
 'pousser': 'nyom',
 'respirer': 'lehel'
}

"""

# --------------- #
# Animaux Anglais #
# --------------- #

"""
dico = {'chat': 'cat', # ascii codec -> ça bug avec les accents
        'chien': 'dog',
        'loup': 'wolf',
        'renard': 'fox'}

dico = {'chat': 'cat', # ascii codec -> ça bug avec les accents
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

# ---------------- #
# prétest & choice #
# ---------------- #

pretest = 'Train' # crocodile | Train = Vonat (Hongrois) 
code_choice = {'1':'learn', '2':'test', '3':'drop'}
code_choice_reverse={}
for duo in code_choice:
    code_choice_reverse[code_choice[duo]]=duo

results = {}
