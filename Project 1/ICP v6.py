import sys,os
from distutils.util import strtobool

#######################################Extra Function####################################



#=======================================================================================#
#                            !!!! WARNING !!!!                                          #
#                                                                                       #
#  THE CLASS -- "colors" use the "ESC" KEY                                              #
#  !!!!Do not edit or save the function below !!!!                                      #
#If you have edited the code below, please redownload the file to prevent logical error.# 
#                                                                                       #color code:
class colors:
    black = 'echo|set /p="[30m'                                                      #0
    dark_red = 'echo|set /p="[31m'                                                   #1
    dark_green = 'echo|set /p="[32m'                                                 #2
    dark_yellow = 'echo|set /p="[33m'                                                #3
    dark_blue = 'echo|set /p="[34m'                                                  #4
    dark_magenta = 'echo|set /p="[35m'                                               #5
    dark_cyan = 'echo|set /p="[36m'                                                  #6
    gray = 'echo|set /p="[37m'                                                       #7
    
    red = 'echo|set /p="[91m'                                                        #8
    green = 'echo|set /p="[92m'                                                      #9
    yellow = 'echo|set /p="[93m'                                                     #a
    blue = 'echo|set /p="[94m'                                                       #b
    magenta = 'echo|set /p="[95m'                                                    #c
    cyan = 'echo|set /p="[96m'                                                       #d
    white = 'echo|set /p="[97m'                                                      #e
    
    reset = 'echo|set /p="[0m'
    
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
    
    b_black = '[40m"'
    bd_red = '[41m"'
    bd_green = '[42m"'
    bd_yellow = '[43m"'
    bd_blue = '[44m"'
    bd_magenta = '[45m"'
    bd_cyan = '[46m"'
    b_gray = '[47m"'
    
    b_red = '[101m"'
    b_green = '[102m"'
    b_yellow = '[103m"'
    b_blue = '[104m"'
    b_magenta = '[105m"'
    b_cyan = '[106m"'
    b_white = '[107m"'

def color(arg1):
    if ospass:  
        if arg1 == "error" : os.system(colors.red + b_black)
        if arg1 == "warn": os.system(colors.yellow + b_black)
        if arg1 == "reset": 
            if set_text == '0':
                if set_bg == '0': os.system(colors.black + colors.b_black)
                if set_bg == '1': os.system(colors.black + colors.bd_red)
                if set_bg == '2': os.system(colors.black + colors.bd_green)
                if set_bg == '3': os.system(colors.black + colors.bd_yellow)
                if set_bg == '4': os.system(colors.black + colors.bd_blue)
                if set_bg == '5': os.system(colors.black + colors.bd_magenta)
                if set_bg == '6': os.system(colors.black + colors.bd_cyan)
                if set_bg == '7': os.system(colors.black + colors.b_gray)
                if set_bg == '8': os.system(colors.black + colors.b_red)
                if set_bg == '9': os.system(colors.black + colors.b_green)
                if set_bg == 'a': os.system(colors.black + colors.b_yellow)
                if set_bg == 'b': os.system(colors.black + colors.b_blue)
                if set_bg == 'c': os.system(colors.black + colors.b_magenta)
                if set_bg == 'd': os.system(colors.black + colors.b_cyan)
                if set_bg == 'e': os.system(colors.black + colors.b_white)
            if set_text == '1':
                if set_bg == '0': os.system(colors.dark_red + colors.b_black)
                if set_bg == '1': os.system(colors.dark_red + colors.bd_red)
                if set_bg == '2': os.system(colors.dark_red + colors.bd_green)
                if set_bg == '3': os.system(colors.dark_red + colors.bd_yellow)
                if set_bg == '4': os.system(colors.dark_red + colors.bd_blue)
                if set_bg == '5': os.system(colors.dark_red + colors.bd_magenta)
                if set_bg == '6': os.system(colors.dark_red + colors.bd_cyan)
                if set_bg == '7': os.system(colors.dark_red + colors.b_gray)
                if set_bg == '8': os.system(colors.dark_red + colors.b_red)
                if set_bg == '9': os.system(colors.dark_red + colors.b_green)
                if set_bg == 'a': os.system(colors.dark_red + colors.b_yellow)
                if set_bg == 'b': os.system(colors.dark_red + colors.b_blue)
                if set_bg == 'c': os.system(colors.dark_red + colors.b_magenta)
                if set_bg == 'd': os.system(colors.dark_red + colors.b_cyan)
                if set_bg == 'e': os.system(colors.dark_red + colors.b_white) 
            if set_text == '2':
                if set_bg == '0': os.system(colors.dark_green + colors.b_black)
                if set_bg == '1': os.system(colors.dark_green + colors.bd_red)
                if set_bg == '2': os.system(colors.dark_green + colors.bd_green)
                if set_bg == '3': os.system(colors.dark_green + colors.bd_yellow)
                if set_bg == '4': os.system(colors.dark_green + colors.bd_blue)
                if set_bg == '5': os.system(colors.dark_green + colors.bd_magenta)
                if set_bg == '6': os.system(colors.dark_green + colors.bd_cyan)
                if set_bg == '7': os.system(colors.dark_green + colors.b_gray)
                if set_bg == '8': os.system(colors.dark_green + colors.b_red)
                if set_bg == '9': os.system(colors.dark_green + colors.b_green)
                if set_bg == 'a': os.system(colors.dark_green + colors.b_yellow)
                if set_bg == 'b': os.system(colors.dark_green + colors.b_blue)
                if set_bg == 'c': os.system(colors.dark_green + colors.b_magenta)
                if set_bg == 'd': os.system(colors.dark_green + colors.b_cyan)
                if set_bg == 'e': os.system(colors.dark_green + colors.b_white) 
            if set_text == '3':
                if set_bg == '0': os.system(colors.dark_yellow + colors.b_black)
                if set_bg == '1': os.system(colors.dark_yellow + colors.bd_red)
                if set_bg == '2': os.system(colors.dark_yellow + colors.bd_green)
                if set_bg == '3': os.system(colors.dark_yellow + colors.bd_yellow)
                if set_bg == '4': os.system(colors.dark_yellow + colors.bd_blue)
                if set_bg == '5': os.system(colors.dark_yellow + colors.bd_magenta)
                if set_bg == '6': os.system(colors.dark_yellow + colors.bd_cyan)
                if set_bg == '7': os.system(colors.dark_yellow + colors.b_gray)
                if set_bg == '8': os.system(colors.dark_yellow + colors.b_red)
                if set_bg == '9': os.system(colors.dark_yellow + colors.b_green)
                if set_bg == 'a': os.system(colors.dark_yellow + colors.b_yellow)
                if set_bg == 'b': os.system(colors.dark_yellow + colors.b_blue)
                if set_bg == 'c': os.system(colors.dark_yellow + colors.b_magenta)
                if set_bg == 'd': os.system(colors.dark_yellow + colors.b_cyan)
                if set_bg == 'e': os.system(colors.dark_yellow + colors.b_white) 
            if set_text == '4':
                if set_bg == '0': os.system(colors.dark_blue + colors.b_black)
                if set_bg == '1': os.system(colors.dark_blue + colors.bd_red)
                if set_bg == '2': os.system(colors.dark_blue + colors.bd_green)
                if set_bg == '3': os.system(colors.dark_blue + colors.bd_yellow)
                if set_bg == '4': os.system(colors.dark_blue + colors.bd_blue)
                if set_bg == '5': os.system(colors.dark_blue + colors.bd_magenta)
                if set_bg == '6': os.system(colors.dark_blue + colors.bd_cyan)
                if set_bg == '7': os.system(colors.dark_blue + colors.b_gray)
                if set_bg == '8': os.system(colors.dark_blue + colors.b_red)
                if set_bg == '9': os.system(colors.dark_blue + colors.b_green)
                if set_bg == 'a': os.system(colors.dark_blue + colors.b_yellow)
                if set_bg == 'b': os.system(colors.dark_blue + colors.b_blue)
                if set_bg == 'c': os.system(colors.dark_blue + colors.b_magenta)
                if set_bg == 'd': os.system(colors.dark_blue + colors.b_cyan)
                if set_bg == 'e': os.system(colors.dark_blue + colors.b_white) 
            if set_text == '5':
                if set_bg == '0': os.system(colors.dark_magenta + colors.b_black)
                if set_bg == '1': os.system(colors.dark_magenta + colors.bd_red)
                if set_bg == '2': os.system(colors.dark_magenta + colors.bd_green)
                if set_bg == '3': os.system(colors.dark_magenta + colors.bd_yellow)
                if set_bg == '4': os.system(colors.dark_magenta + colors.bd_blue)
                if set_bg == '5': os.system(colors.dark_magenta + colors.bd_magenta)
                if set_bg == '6': os.system(colors.dark_magenta + colors.bd_cyan)
                if set_bg == '7': os.system(colors.dark_magenta + colors.b_gray)
                if set_bg == '8': os.system(colors.dark_magenta + colors.b_red)
                if set_bg == '9': os.system(colors.dark_magenta + colors.b_green)
                if set_bg == 'a': os.system(colors.dark_magenta + colors.b_yellow)
                if set_bg == 'b': os.system(colors.dark_magenta + colors.b_blue)
                if set_bg == 'c': os.system(colors.dark_magenta + colors.b_magenta)
                if set_bg == 'd': os.system(colors.dark_magenta + colors.b_cyan)
                if set_bg == 'e': os.system(colors.dark_magenta + colors.b_white) 
            if set_text == '6':
                if set_bg == '0': os.system(colors.dark_cyan + colors.b_black)
                if set_bg == '1': os.system(colors.dark_cyan + colors.bd_red)
                if set_bg == '2': os.system(colors.dark_cyan + colors.bd_green)
                if set_bg == '3': os.system(colors.dark_cyan + colors.bd_yellow)
                if set_bg == '4': os.system(colors.dark_cyan + colors.bd_blue)
                if set_bg == '5': os.system(colors.dark_cyan + colors.bd_magenta)
                if set_bg == '6': os.system(colors.dark_cyan + colors.bd_cyan)
                if set_bg == '7': os.system(colors.dark_cyan + colors.b_gray)
                if set_bg == '8': os.system(colors.dark_cyan + colors.b_red)
                if set_bg == '9': os.system(colors.dark_cyan + colors.b_green)
                if set_bg == 'a': os.system(colors.dark_cyan + colors.b_yellow)
                if set_bg == 'b': os.system(colors.dark_cyan + colors.b_blue)
                if set_bg == 'c': os.system(colors.dark_cyan + colors.b_magenta)
                if set_bg == 'd': os.system(colors.dark_cyan + colors.b_cyan)
                if set_bg == 'e': os.system(colors.dark_cyan + colors.b_white) 
            if set_text == '7':
                if set_bg == '0': os.system(colors.gray + colors.b_black)
                if set_bg == '1': os.system(colors.gray + colors.bd_red)
                if set_bg == '2': os.system(colors.gray + colors.bd_green)
                if set_bg == '3': os.system(colors.gray + colors.bd_yellow)
                if set_bg == '4': os.system(colors.gray + colors.bd_blue)
                if set_bg == '5': os.system(colors.gray + colors.bd_magenta)
                if set_bg == '6': os.system(colors.gray + colors.bd_cyan)
                if set_bg == '7': os.system(colors.gray + colors.b_gray)
                if set_bg == '8': os.system(colors.gray + colors.b_red)
                if set_bg == '9': os.system(colors.gray + colors.b_green)
                if set_bg == 'a': os.system(colors.gray + colors.b_yellow)
                if set_bg == 'b': os.system(colors.gray + colors.b_blue)
                if set_bg == 'c': os.system(colors.gray + colors.b_magenta)
                if set_bg == 'd': os.system(colors.gray + colors.b_cyan)
                if set_bg == 'e': os.system(colors.gray + colors.b_white) 
            if set_text == '8':
                if set_bg == '0': os.system(colors.red + colors.b_black)
                if set_bg == '1': os.system(colors.red + colors.bd_red)
                if set_bg == '2': os.system(colors.red + colors.bd_green)
                if set_bg == '3': os.system(colors.red + colors.bd_yellow)
                if set_bg == '4': os.system(colors.red + colors.bd_blue)
                if set_bg == '5': os.system(colors.red + colors.bd_magenta)
                if set_bg == '6': os.system(colors.red + colors.bd_cyan)
                if set_bg == '7': os.system(colors.red + colors.b_gray)
                if set_bg == '8': os.system(colors.red + colors.b_red)
                if set_bg == '9': os.system(colors.red + colors.b_green)
                if set_bg == 'a': os.system(colors.red + colors.b_yellow)
                if set_bg == 'b': os.system(colors.red + colors.b_blue)
                if set_bg == 'c': os.system(colors.red + colors.b_magenta)
                if set_bg == 'd': os.system(colors.red + colors.b_cyan)
                if set_bg == 'e': os.system(colors.red + colors.b_white) 
            if set_text == '9':
                if set_bg == '0': os.system(colors.green + colors.b_black)
                if set_bg == '1': os.system(colors.green + colors.bd_red)
                if set_bg == '2': os.system(colors.green + colors.bd_green)
                if set_bg == '3': os.system(colors.green + colors.bd_yellow)
                if set_bg == '4': os.system(colors.green + colors.bd_blue)
                if set_bg == '5': os.system(colors.green + colors.bd_magenta)
                if set_bg == '6': os.system(colors.green + colors.bd_cyan)
                if set_bg == '7': os.system(colors.green + colors.b_gray)
                if set_bg == '8': os.system(colors.green + colors.b_red)
                if set_bg == '9': os.system(colors.green + colors.b_green)
                if set_bg == 'a': os.system(colors.green + colors.b_yellow)
                if set_bg == 'b': os.system(colors.green + colors.b_blue)
                if set_bg == 'c': os.system(colors.green + colors.b_magenta)
                if set_bg == 'd': os.system(colors.green + colors.b_cyan)
                if set_bg == 'e': os.system(colors.green + colors.b_white) 
            if set_text == 'a':
                if set_bg == '0': os.system(colors.yellow + colors.b_black)
                if set_bg == '1': os.system(colors.yellow + colors.bd_red)
                if set_bg == '2': os.system(colors.yellow + colors.bd_green)
                if set_bg == '3': os.system(colors.yellow + colors.bd_yellow)
                if set_bg == '4': os.system(colors.yellow + colors.bd_blue)
                if set_bg == '5': os.system(colors.yellow + colors.bd_magenta)
                if set_bg == '6': os.system(colors.yellow + colors.bd_cyan)
                if set_bg == '7': os.system(colors.yellow + colors.b_gray)
                if set_bg == '8': os.system(colors.yellow + colors.b_red)
                if set_bg == '9': os.system(colors.yellow + colors.b_green)
                if set_bg == 'a': os.system(colors.yellow + colors.b_yellow)
                if set_bg == 'b': os.system(colors.yellow + colors.b_blue)
                if set_bg == 'c': os.system(colors.yellow + colors.b_magenta)
                if set_bg == 'd': os.system(colors.yellow + colors.b_cyan)
                if set_bg == 'e': os.system(colors.yellow + colors.b_white) 
            if set_text == 'b':
                if set_bg == '0': os.system(colors.blue + colors.b_black)
                if set_bg == '1': os.system(colors.blue + colors.bd_red)
                if set_bg == '2': os.system(colors.blue + colors.bd_green)
                if set_bg == '3': os.system(colors.blue + colors.bd_yellow)
                if set_bg == '4': os.system(colors.blue + colors.bd_blue)
                if set_bg == '5': os.system(colors.blue + colors.bd_magenta)
                if set_bg == '6': os.system(colors.blue + colors.bd_cyan)
                if set_bg == '7': os.system(colors.blue + colors.b_gray)
                if set_bg == '8': os.system(colors.blue + colors.b_red)
                if set_bg == '9': os.system(colors.blue + colors.b_green)
                if set_bg == 'a': os.system(colors.blue + colors.b_yellow)
                if set_bg == 'b': os.system(colors.blue + colors.b_blue)
                if set_bg == 'c': os.system(colors.blue + colors.b_magenta)
                if set_bg == 'd': os.system(colors.blue + colors.b_cyan)
                if set_bg == 'e': os.system(colors.blue + colors.b_white) 
            if set_text == 'c':
                if set_bg == '0': os.system(colors.magenta + colors.b_black)
                if set_bg == '1': os.system(colors.magenta + colors.bd_red)
                if set_bg == '2': os.system(colors.magenta + colors.bd_green)
                if set_bg == '3': os.system(colors.magenta + colors.bd_yellow)
                if set_bg == '4': os.system(colors.magenta + colors.bd_blue)
                if set_bg == '5': os.system(colors.magenta + colors.bd_magenta)
                if set_bg == '6': os.system(colors.magenta + colors.bd_cyan)
                if set_bg == '7': os.system(colors.magenta + colors.b_gray)
                if set_bg == '8': os.system(colors.magenta + colors.b_red)
                if set_bg == '9': os.system(colors.magenta + colors.b_green)
                if set_bg == 'a': os.system(colors.magenta + colors.b_yellow)
                if set_bg == 'b': os.system(colors.magenta + colors.b_blue)
                if set_bg == 'c': os.system(colors.magenta + colors.b_magenta)
                if set_bg == 'd': os.system(colors.magenta + colors.b_cyan)
                if set_bg == 'e': os.system(colors.magenta + colors.b_white) 
            if set_text == 'd':
                if set_bg == '0': os.system(colors.cyan + colors.b_black)
                if set_bg == '1': os.system(colors.cyan + colors.bd_red)
                if set_bg == '2': os.system(colors.cyan + colors.bd_green)
                if set_bg == '3': os.system(colors.cyan + colors.bd_yellow)
                if set_bg == '4': os.system(colors.cyan + colors.bd_blue)
                if set_bg == '5': os.system(colors.cyan + colors.bd_magenta)
                if set_bg == '6': os.system(colors.cyan + colors.bd_cyan)
                if set_bg == '7': os.system(colors.cyan + colors.b_gray)
                if set_bg == '8': os.system(colors.cyan + colors.b_red)
                if set_bg == '9': os.system(colors.cyan + colors.b_green)
                if set_bg == 'a': os.system(colors.cyan + colors.b_yellow)
                if set_bg == 'b': os.system(colors.cyan + colors.b_blue)
                if set_bg == 'c': os.system(colors.cyan + colors.b_magenta)
                if set_bg == 'd': os.system(colors.cyan + colors.b_cyan)
                if set_bg == 'e': os.system(colors.cyan + colors.b_white) 
            if set_text == 'e':
                if set_bg == '0': os.system(colors.white + colors.b_black)
                if set_bg == '1': os.system(colors.white + colors.bd_red)
                if set_bg == '2': os.system(colors.white + colors.bd_green)
                if set_bg == '3': os.system(colors.white + colors.bd_yellow)
                if set_bg == '4': os.system(colors.white + colors.bd_blue)
                if set_bg == '5': os.system(colors.white + colors.bd_magenta)
                if set_bg == '6': os.system(colors.white + colors.bd_cyan)
                if set_bg == '7': os.system(colors.white + colors.b_gray)
                if set_bg == '8': os.system(colors.white + colors.b_red)
                if set_bg == '9': os.system(colors.white + colors.b_green)
                if set_bg == 'a': os.system(colors.white + colors.b_yellow)
                if set_bg == 'b': os.system(colors.white + colors.b_blue)
                if set_bg == 'c': os.system(colors.white + colors.b_magenta)
                if set_bg == 'd': os.system(colors.white + colors.b_cyan)
                if set_bg == 'e': os.system(colors.white + colors.b_white) 
            
        if arg1 == "search":
            if set_stext == '0':
                if set_sbg == '0': os.system(colors.black + colors.b_black)
                if set_sbg == '1': os.system(colors.black + colors.bd_red)
                if set_sbg == '2': os.system(colors.black + colors.bd_green)
                if set_sbg == '3': os.system(colors.black + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.black + colors.bd_blue)
                if set_sbg == '5': os.system(colors.black + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.black + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.black + colors.b_gray)
                if set_sbg == '8': os.system(colors.black + colors.b_red)
                if set_sbg == '9': os.system(colors.black + colors.b_green)
                if set_sbg == 'a': os.system(colors.black + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.black + colors.b_blue)
                if set_sbg == 'c': os.system(colors.black + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.black + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.black + colors.b_white)
            if set_stext == '1':
                if set_sbg == '0': os.system(colors.dark_red + colors.b_black)
                if set_sbg == '1': os.system(colors.dark_red + colors.bd_red)
                if set_sbg == '2': os.system(colors.dark_red + colors.bd_green)
                if set_sbg == '3': os.system(colors.dark_red + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.dark_red + colors.bd_blue)
                if set_sbg == '5': os.system(colors.dark_red + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.dark_red + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.dark_red + colors.b_gray)
                if set_sbg == '8': os.system(colors.dark_red + colors.b_red)
                if set_sbg == '9': os.system(colors.dark_red + colors.b_green)
                if set_sbg == 'a': os.system(colors.dark_red + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.dark_red + colors.b_blue)
                if set_sbg == 'c': os.system(colors.dark_red + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.dark_red + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.dark_red + colors.b_white) 
            if set_stext == '2':
                if set_sbg == '0': os.system(colors.dark_green + colors.b_black)
                if set_sbg == '1': os.system(colors.dark_green + colors.bd_red)
                if set_sbg == '2': os.system(colors.dark_green + colors.bd_green)
                if set_sbg == '3': os.system(colors.dark_green + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.dark_green + colors.bd_blue)
                if set_sbg == '5': os.system(colors.dark_green + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.dark_green + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.dark_green + colors.b_gray)
                if set_sbg == '8': os.system(colors.dark_green + colors.b_red)
                if set_sbg == '9': os.system(colors.dark_green + colors.b_green)
                if set_sbg == 'a': os.system(colors.dark_green + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.dark_green + colors.b_blue)
                if set_sbg == 'c': os.system(colors.dark_green + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.dark_green + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.dark_green + colors.b_white) 
            if set_stext == '3':
                if set_sbg == '0': os.system(colors.dark_yellow + colors.b_black)
                if set_sbg == '1': os.system(colors.dark_yellow + colors.bd_red)
                if set_sbg == '2': os.system(colors.dark_yellow + colors.bd_green)
                if set_sbg == '3': os.system(colors.dark_yellow + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.dark_yellow + colors.bd_blue)
                if set_sbg == '5': os.system(colors.dark_yellow + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.dark_yellow + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.dark_yellow + colors.b_gray)
                if set_sbg == '8': os.system(colors.dark_yellow + colors.b_red)
                if set_sbg == '9': os.system(colors.dark_yellow + colors.b_green)
                if set_sbg == 'a': os.system(colors.dark_yellow + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.dark_yellow + colors.b_blue)
                if set_sbg == 'c': os.system(colors.dark_yellow + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.dark_yellow + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.dark_yellow + colors.b_white) 
            if set_stext == '4':
                if set_sbg == '0': os.system(colors.dark_blue + colors.b_black)
                if set_sbg == '1': os.system(colors.dark_blue + colors.bd_red)
                if set_sbg == '2': os.system(colors.dark_blue + colors.bd_green)
                if set_sbg == '3': os.system(colors.dark_blue + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.dark_blue + colors.bd_blue)
                if set_sbg == '5': os.system(colors.dark_blue + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.dark_blue + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.dark_blue + colors.b_gray)
                if set_sbg == '8': os.system(colors.dark_blue + colors.b_red)
                if set_sbg == '9': os.system(colors.dark_blue + colors.b_green)
                if set_sbg == 'a': os.system(colors.dark_blue + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.dark_blue + colors.b_blue)
                if set_sbg == 'c': os.system(colors.dark_blue + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.dark_blue + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.dark_blue + colors.b_white) 
            if set_stext == '5':
                if set_sbg == '0': os.system(colors.dark_magenta + colors.b_black)
                if set_sbg == '1': os.system(colors.dark_magenta + colors.bd_red)
                if set_sbg == '2': os.system(colors.dark_magenta + colors.bd_green)
                if set_sbg == '3': os.system(colors.dark_magenta + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.dark_magenta + colors.bd_blue)
                if set_sbg == '5': os.system(colors.dark_magenta + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.dark_magenta + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.dark_magenta + colors.b_gray)
                if set_sbg == '8': os.system(colors.dark_magenta + colors.b_red)
                if set_sbg == '9': os.system(colors.dark_magenta + colors.b_green)
                if set_sbg == 'a': os.system(colors.dark_magenta + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.dark_magenta + colors.b_blue)
                if set_sbg == 'c': os.system(colors.dark_magenta + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.dark_magenta + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.dark_magenta + colors.b_white) 
            if set_stext == '6':
                if set_sbg == '0': os.system(colors.dark_cyan + colors.b_black)
                if set_sbg == '1': os.system(colors.dark_cyan + colors.bd_red)
                if set_sbg == '2': os.system(colors.dark_cyan + colors.bd_green)
                if set_sbg == '3': os.system(colors.dark_cyan + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.dark_cyan + colors.bd_blue)
                if set_sbg == '5': os.system(colors.dark_cyan + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.dark_cyan + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.dark_cyan + colors.b_gray)
                if set_sbg == '8': os.system(colors.dark_cyan + colors.b_red)
                if set_sbg == '9': os.system(colors.dark_cyan + colors.b_green)
                if set_sbg == 'a': os.system(colors.dark_cyan + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.dark_cyan + colors.b_blue)
                if set_sbg == 'c': os.system(colors.dark_cyan + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.dark_cyan + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.dark_cyan + colors.b_white) 
            if set_stext == '7':
                if set_sbg == '0': os.system(colors.gray + colors.b_black)
                if set_sbg == '1': os.system(colors.gray + colors.bd_red)
                if set_sbg == '2': os.system(colors.gray + colors.bd_green)
                if set_sbg == '3': os.system(colors.gray + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.gray + colors.bd_blue)
                if set_sbg == '5': os.system(colors.gray + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.gray + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.gray + colors.b_gray)
                if set_sbg == '8': os.system(colors.gray + colors.b_red)
                if set_sbg == '9': os.system(colors.gray + colors.b_green)
                if set_sbg == 'a': os.system(colors.gray + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.gray + colors.b_blue)
                if set_sbg == 'c': os.system(colors.gray + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.gray + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.gray + colors.b_white) 
            if set_stext == '8':
                if set_sbg == '0': os.system(colors.red + colors.b_black)
                if set_sbg == '1': os.system(colors.red + colors.bd_red)
                if set_sbg == '2': os.system(colors.red + colors.bd_green)
                if set_sbg == '3': os.system(colors.red + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.red + colors.bd_blue)
                if set_sbg == '5': os.system(colors.red + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.red + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.red + colors.b_gray)
                if set_sbg == '8': os.system(colors.red + colors.b_red)
                if set_sbg == '9': os.system(colors.red + colors.b_green)
                if set_sbg == 'a': os.system(colors.red + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.red + colors.b_blue)
                if set_sbg == 'c': os.system(colors.red + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.red + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.red + colors.b_white) 
            if set_stext == '9':
                if set_sbg == '0': os.system(colors.green + colors.b_black)
                if set_sbg == '1': os.system(colors.green + colors.bd_red)
                if set_sbg == '2': os.system(colors.green + colors.bd_green)
                if set_sbg == '3': os.system(colors.green + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.green + colors.bd_blue)
                if set_sbg == '5': os.system(colors.green + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.green + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.green + colors.b_gray)
                if set_sbg == '8': os.system(colors.green + colors.b_red)
                if set_sbg == '9': os.system(colors.green + colors.b_green)
                if set_sbg == 'a': os.system(colors.green + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.green + colors.b_blue)
                if set_sbg == 'c': os.system(colors.green + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.green + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.green + colors.b_white) 
            if set_stext == 'a':
                if set_sbg == '0': os.system(colors.yellow + colors.b_black)
                if set_sbg == '1': os.system(colors.yellow + colors.bd_red)
                if set_sbg == '2': os.system(colors.yellow + colors.bd_green)
                if set_sbg == '3': os.system(colors.yellow + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.yellow + colors.bd_blue)
                if set_sbg == '5': os.system(colors.yellow + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.yellow + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.yellow + colors.b_gray)
                if set_sbg == '8': os.system(colors.yellow + colors.b_red)
                if set_sbg == '9': os.system(colors.yellow + colors.b_green)
                if set_sbg == 'a': os.system(colors.yellow + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.yellow + colors.b_blue)
                if set_sbg == 'c': os.system(colors.yellow + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.yellow + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.yellow + colors.b_white) 
            if set_stext == 'b':
                if set_sbg == '0': os.system(colors.blue + colors.b_black)
                if set_sbg == '1': os.system(colors.blue + colors.bd_red)
                if set_sbg == '2': os.system(colors.blue + colors.bd_green)
                if set_sbg == '3': os.system(colors.blue + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.blue + colors.bd_blue)
                if set_sbg == '5': os.system(colors.blue + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.blue + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.blue + colors.b_gray)
                if set_sbg == '8': os.system(colors.blue + colors.b_red)
                if set_sbg == '9': os.system(colors.blue + colors.b_green)
                if set_sbg == 'a': os.system(colors.blue + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.blue + colors.b_blue)
                if set_sbg == 'c': os.system(colors.blue + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.blue + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.blue + colors.b_white) 
            if set_stext == 'c':
                if set_sbg == '0': os.system(colors.magenta + colors.b_black)
                if set_sbg == '1': os.system(colors.magenta + colors.bd_red)
                if set_sbg == '2': os.system(colors.magenta + colors.bd_green)
                if set_sbg == '3': os.system(colors.magenta + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.magenta + colors.bd_blue)
                if set_sbg == '5': os.system(colors.magenta + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.magenta + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.magenta + colors.b_gray)
                if set_sbg == '8': os.system(colors.magenta + colors.b_red)
                if set_sbg == '9': os.system(colors.magenta + colors.b_green)
                if set_sbg == 'a': os.system(colors.magenta + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.magenta + colors.b_blue)
                if set_sbg == 'c': os.system(colors.magenta + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.magenta + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.magenta + colors.b_white) 
            if set_stext == 'd':
                if set_sbg == '0': os.system(colors.cyan + colors.b_black)
                if set_sbg == '1': os.system(colors.cyan + colors.bd_red)
                if set_sbg == '2': os.system(colors.cyan + colors.bd_green)
                if set_sbg == '3': os.system(colors.cyan + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.cyan + colors.bd_blue)
                if set_sbg == '5': os.system(colors.cyan + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.cyan + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.cyan + colors.b_gray)
                if set_sbg == '8': os.system(colors.cyan + colors.b_red)
                if set_sbg == '9': os.system(colors.cyan + colors.b_green)
                if set_sbg == 'a': os.system(colors.cyan + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.cyan + colors.b_blue)
                if set_sbg == 'c': os.system(colors.cyan + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.cyan + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.cyan + colors.b_white) 
            if set_stext == 'e':
                if set_sbg == '0': os.system(colors.white + colors.b_black)
                if set_sbg == '1': os.system(colors.white + colors.bd_red)
                if set_sbg == '2': os.system(colors.white + colors.bd_green)
                if set_sbg == '3': os.system(colors.white + colors.bd_yellow)
                if set_sbg == '4': os.system(colors.white + colors.bd_blue)
                if set_sbg == '5': os.system(colors.white + colors.bd_magenta)
                if set_sbg == '6': os.system(colors.white + colors.bd_cyan)
                if set_sbg == '7': os.system(colors.white + colors.b_gray)
                if set_sbg == '8': os.system(colors.white + colors.b_red)
                if set_sbg == '9': os.system(colors.white + colors.b_green)
                if set_sbg == 'a': os.system(colors.white + colors.b_yellow)
                if set_sbg == 'b': os.system(colors.white + colors.b_blue)
                if set_sbg == 'c': os.system(colors.white + colors.b_magenta)
                if set_sbg == 'd': os.system(colors.white + colors.b_cyan)
                if set_sbg == 'e': os.system(colors.white + colors.b_white) 
#=======================================================================================#



def repeat(arg1,arg2,arg3,arg4):
    while(True):
        useless_1 = input(arg2)
        if useless_1 == "<exit>" : return "<exit>"
        try:
            if arg1 == "i":
                useless = int(useless_1)
            if arg1 == "f":
                useless = float(useless_1) 
            break
        except:
            color('red')
            print('Input ERROR: ' + arg3)
            color('reset')
            pause()            
            cls()
            if arg4 != "":print(arg4)
    return useless
            
# clear screen
def cls():
    if set_ac:
        if ospass: os.system('cls')
        else:
            for x in range(50):print('\n')
    
# Pasue   
def pause():
    if ospass: os.system('pause')
    else:
        input("Press <ENTER> to continue")

# read all data from "inventory.txt"
def listall():
    global g_num, g_name, g_item_num, g_cate, g_c, g_w, g_buyer, g_dst, g_stat, g_max
    with open("inventory.txt","r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    j = 0
    # g_max => the maximum number of the record on the txt file
    g_num = [""]
    g_name = [""]
    g_item_num = [""]
    g_cate = [""]
    g_c = [""]
    g_w = [""]
    g_buyer = [""]
    g_dst = [""]
    g_stat = [""]
    g_max = len(data)//9
    for i in range(g_max):
        g_num.append(str(data[j]))
        g_name.append(data[j+1])
        g_item_num.append(data[j+2])
        g_cate.append(data[j+3])
        g_c.append(str(data[j+4]))
        g_w.append(str(data[j+5]))
        g_buyer.append(data[j+6])
        g_dst.append(data[j+7])
        g_stat.append(data[j+8])
        j+=10
    g_num.remove("")
    g_name.remove("")
    g_item_num.remove("")
    g_cate.remove("")
    g_c.remove("")
    g_w.remove("")
    g_buyer.remove("")
    g_dst.remove("")
    g_stat.remove("")
    f.close()

def saveall():
    f = open("inventory.txt","w")
    for x in range(g_max):
        if g_num[x] != -1:
            f.write(str(g_num[x])+"\n")
            f.write(g_name[x]+"\n")
            f.write(str(g_item_num[x])+"\n")
            f.write(g_cate[x]+"\n")
            f.write(str(g_c[x])+"\n")
            f.write(str(g_w[x])+"\n")
            f.write(g_buyer[x]+"\n")
            f.write(g_dst[x]+"\n")
            f.write(g_stat[x]+"\n\n")
    f.close()
    print("Data has been saved.")

###################### END ##################################

################# MAIN FUNCTION ###################################
def main():
    cls()
    print('--<Basic function>--')
    print('1.Add new item(s)\n')
    print('2.Display Item record(s)\n')
    print('3.Search Item Information\n')
    print('4.Modify Item Record(s)\n')
    print('5.Delete Item Record(s)\n') 
    print('6.Settings\n')
    print('7.Exit program\n')
    while (True):
        try:
            choice=int(input('Please enter the function you want to operate (1-7): '))
            break
        except:
            color ('red');print("Please input integer only!");color('reset')
    if choice<=0 or choice >7:
            color('red'); print("Range ERROR: Please input an integer between 1 to 7.");color('reset')
            pause()
            cls()
            return main()
    if choice == 1:
        adddata()
    if choice == 2:
        displaydata('all')
    if choice == 3:
        searchdata('print')
    if choice == 4:
        modifydata()
    if choice == 5:
        deleteitem()
    if choice == 6:
        setting()
    if choice == 7:
        sys.exit()

def adddata():
    cls()
    appfile=open('inventory.txt','a')
    recnumber=input('Please enter Record number:')
    itemname=input('Please enter Item name:')
    itemnum=input('Please enter Item number:')
    category=input('Please enter Category:')
    quantity=input('Please enter Quantity:')
    weight=input('Please enter Weight:')
    recipent=input('Please enter Recipent:')
    finDes=input('Please enter Final Destination:')
    deli=input('Please enter Delivery status:')

    if not set_as:
        b = input("Type \"Confirm\" to confirm the data. ")
        if b.lower() == "confirm":
            appfile.write(recnumber+'\n')
            appfile.write(itemname+ '\n')
            appfile.write(itemnum+ '\n')
            appfile.write(category+ '\n')
            appfile.write(quantity+ '\n')
            appfile.write(weight+ '\n')
            appfile.write(recipent+ '\n')
            appfile.write(finDes+'\n')
            appfile.write(deli+ '\n\n')
            print("Data has been successfully saved.")
        else: print("Process has been cancelled.")
    appfile.close()
    contin=input('Do you want to add another new item?(y/n)')
    while contin.lower() != 'y'and contin.lower() !='n':
        print('It is a wrong input.Please input again.')
        pause()
        cls()
        contin=input('Do you want to add another new item?(y/n):')
    if contin.lower() == 'y' or contin.lower() == 'yes':
        return adddata()
    if contin.lower() == 'n' or contin.lower() == 'no':
        return main()
        
def displaydata(arg):
    listall()
    cls()
    if arg == 'all' :
        num1 = 0
        num2 = g_max
    else: num1 = arg; num2 = arg + 1
    if g_max == 0 : print("----------------------------------------------------------------------\nThe file \"inventory.txt\" is empty.")
    j = 0
    for i in range(num1,num2):
        print("----------------------------------------------------------------------")
        print("Record Number: ",g_num[i],sep='')
        print("   Item Name . . . . . . . . : ",g_name[i],sep='')
        print("   Item Number . . . . . . . : ",g_item_num[i],sep='')
        print("   Category. . . . . . . . . : ",g_cate[i],sep='')
        print("   Quantity. . . . . . . . . : ",g_c[i],sep='')
        print("   Weight. . . . . . . . . . : ",g_w[i]," kg",sep='')
        print("   Recipient . . . . . . . . : ",g_buyer[i],sep='')
        print("   Final Destination . . . . : ",g_dst[i],sep='')
        print("   Delivery Status . . . . . : ",g_stat[i],sep='')
        j += 1;
        if str(j) == set_length: pause()
    print("----------------------------------------------------------------------\n")
    pause()
      
def searchdata(arg):
    listall()
    cls()
    leave = False
    se_list = ['']
    if g_max == 0: print("----------------------------------------------------------------------\nThe file \"inventory.txt\" is empty.\n----------------------------------------------------------------------\n"); pause();return
    for se_x in range(g_max):
        se_list.append(g_num[se_x])
        se_list.append(g_name[se_x])
        se_list.append(g_item_num[se_x])
        se_list.append(g_cate[se_x])
        se_list.append(g_c[se_x])
        se_list.append(g_w[se_x])
        se_list.append(g_buyer[se_x])
        se_list.append(g_dst[se_x])
        se_list.append(g_stat[se_x])
    se_list.remove('')
    while not leave:
        confirm = False
        cls()
        if arg == "return": search = input("Search(Record number): ")
        else : search = input("Search(Case Sensitive): ")
        for i in range(len(se_list)):
            if search in se_list[i]:
                if arg == "print" : 
                    k = 0
                    j = list(se_list[i])
                    k = list(search)
                    o = round(i%9)
                    pas = True
                    if o == 0: 
                        if se_list[i] == search : displaydata(i//9)
                        pas = False 
                    else: cls();print("Search result of \"",search,"\": ",sep='');print("Record Number: ",g_num[i//9])
                    if o == 1: color("reset") ;os.system('echo|set /p="Item Name: "')
                    if o == 2: color("reset") ;os.system('echo|set /p="Item Number: "')
                    if o == 3: color("reset") ;os.system('echo|set /p="Category: "')
                    if o == 4: color("reset") ;os.system('echo|set /p="Quantity: "')
                    if o == 5: color("reset") ;os.system('echo|set /p="Weight: "')
                    if o == 6: color("reset") ;os.system('echo|set /p="Recipient: "')
                    if o == 7: color("reset") ;os.system('echo|set /p="Final Destination: "')
                    if o == 8: color("reset") ;os.system('echo|set /p="Delivery Status: "')
                    i = 0
                    l = 0                 
                    while i+1 <= len(j) and l+1 <= len(k) and pas:
                        if j[i] == k[l] : 
                            color("search")
                            os.system('echo|set /p="'+ k[l] +'"')
                            color("reset")                            
                            if l+1 >= len(k): l=0
                            else : l+=1
                            i += 1
                        else: 
                            os.system('echo|set /p="'+ j[i] +'"')
                            l = 0
                            i+=1
                    print("")
                    if pas: pause()
                    confirm = True   
                      
                    
                    
        if arg == "return":
            for k in range(g_max): 
                if search == g_num[k]: confirm = True; break
                #break
        if not confirm:
            print("You search -- \"",search,"\" did not match anything in \"inventory.txt\".",sep='')
        if arg == "print":
            while True: 
                b = input("Do you want to search again?(y/n): ")
                cls()
                if b.lower() == "n" or b.lower() == "no": leave = True; break
                if b.lower() == "y" or b.lower() == "yes": leave = False; break
                print("Please input \"Yes\" or \"No\"")
        elif arg == "return":
            if confirm : return k; 
            else: return -1;


def modifydata():
    listall()
    cls()
    leave_1 = True
    if g_max == 0: print("----------------------------------------------------------------------\nThe file \"inventory.txt\" is empty.\n----------------------------------------------------------------------\n");pause();return
    while leave_1:
        m_num = searchdata("return")
        if m_num == -1:
            while True:
                b = input("Do you want to search again?(y/n): ")
                if b.lower() == 'no' or b.lower() == 'n': leave_1 = False; break
                if b.lower() != 'yes' and b.lower() != 'y':cls(); print("Please input \"Yes\" or \"No\"!")
                else: break
        else: break    
    m_list = ("Record Number . . . . . . : ","Item Name . . . . . . . . : ","Item Number . . . . . . . : ","Category. . . . . . . . . : ",
    "Quantity. . . . . . . . . : ","Weight. . . . . . . . . . : ","Recipient . . . . . . . . : ","Final Destination . . . . : ","Delivery Status . . . . . : ")
    cls()
    m_change = 0
    while m_change >= 11 or m_change <= 0 and m_num != -1:
        m_text = "Record:\n" + "1. " + m_list[0] + g_num[m_num] + "\n"
        m_text = m_text + "2. " + m_list[1] + g_name[m_num] + "\n"
        m_text = m_text + "3. " + m_list[2] + g_item_num[m_num] + "\n"
        m_text = m_text + "4. " + m_list[3] + g_cate[m_num] + "\n"
        m_text = m_text + "5. " + m_list[4] + g_c[m_num] + "\n"
        m_text = m_text + "6. " + m_list[5] + g_w[m_num] + " kg\n"
        m_text = m_text + "7. " + m_list[6] + g_buyer[m_num] + "\n"
        m_text = m_text + "8. " + m_list[7] + g_dst[m_num] + "\n"
        m_text = m_text + "9. " + m_list[8] + g_stat[m_num] + "\n10. Exit"
        print(m_text)
        m_change = repeat("i","Input a number (1-10) to modify: ","Please input an integer!",m_text)
        if m_change >= 11 or m_change <= 0 :color('red'); print("Please input an integer within 1 to 10!");color("reset");pause();cls()
    while True:
        if m_change != 10 and m_num != -1: 
            cls()
            if m_change == 1 : g_num[m_num] = repeat("i",m_list[m_change-1],"Please input an integer!","")
            if m_change == 2 : g_name[m_num] = input(m_list[m_change-1])
            if m_change == 3 : g_item_num[m_num] = repeat("i",m_list[m_change-1],"Please input an integer!","")
            if m_change == 4 : g_cate[m_num] = input(m_list[m_change-1])
            if m_change == 5 : g_c[m_num] = repeat("i",m_list[m_change-1],"Please input an integer!","")
            if m_change == 6 : g_w[m_num] = repeat("f",m_list[m_change-1],"Please input an number!","")
            if m_change == 7 : g_buyer[m_num] = input(m_list[m_change-1])
            if m_change == 8 : g_dst[m_num] = input(m_list[m_change-1])
            if m_change == 9 : g_stat[m_num] = input(m_list[m_change-1])
            while True:
                m_text = "Record:\n" + "1. " + m_list[0] + str(g_num[m_num]) + "\n"
                m_text = m_text + "2. " + m_list[1] + g_name[m_num] + "\n"
                m_text = m_text + "3. " + m_list[2] + str(g_item_num[m_num]) + "\n"
                m_text = m_text + "4. " + m_list[3] + g_cate[m_num] + "\n"
                m_text = m_text + "5. " + m_list[4] + str(g_c[m_num]) + "\n"
                m_text = m_text + "6. " + m_list[5] + str(g_w[m_num]) + " kg\n"
                m_text = m_text + "7. " + m_list[6] + g_buyer[m_num] + "\n"
                m_text = m_text + "8. " + m_list[7] + g_dst[m_num] + "\n"
                m_text = m_text + "9. " + m_list[8] + g_stat[m_num] + "\n10. Save and Exit"
                print(m_text)
                pause()
                m_change = repeat("i","Any other to modify?(1-10): ","Please input an integer!",m_text)
                if m_change >= 11 or m_change <= 0 :color('red'); print("Please input an integer within 1 to 10!");color("reset");pause();cls()
                else: break
            if m_change == 10:
                if not set_as:
                    b = input("Type \"Confirm\" to save the data.: ");
                    confirm = b.lower() == "confirm" 
                    if confirm: saveall()
                else: saveall()
                break;
    while True:
        b = input("Do you want to modify another record?(y/n) ")
        if b.lower() == 'n' or b.lower() == 'no' : break
        if b.lower() == 'y' or b.lower() == 'yes': cmd4(); break


def deleteitem():
    listall()
    cls()
    leave_1 = True
    if g_max == 0: print("----------------------------------------------------------------------\nThe file \"inventory.txt\" is empty.\n----------------------------------------------------------------------\n");pause();return
    while leave_1:
        d_num = searchdata("return")
        if d_num == -1:
            while True:
                b = input("Do you want to search again?(y/n): ")
                if b.lower() == 'no' or b.lower() == 'n': leave_1 = False; break
                if b.lower() != 'yes' and b.lower() != 'y':cls(); print("Please input \"Yes\" or \"No\"!")
                else: break
        else: break    
    d_list = ("Record Number . . . . . . : ","Item Name . . . . . . . . : ","Item Number . . . . . . . : ","Category. . . . . . . . . : ",
    "Quantity. . . . . . . . . : ","Weight. . . . . . . . . . : ","Recipient . . . . . . . . : ","Final Destination . . . . : ","Delivery Status . . . . . : ")
    cls()
    d_text ="Record Number . . . . . . : "+g_num[d_num]+"\nItem Name . . . . . . . . : "+g_name[d_num]+"\nItem Number . . . . . . . : "+g_item_num[d_num]
    d_text = d_text + "\nCategory. . . . . . . . . : " +g_cate[d_num]+"\nQuantity. . . . . . . . . : "+g_c[d_num]+"\nWeight. . . . . . . . . . : "
    d_text = d_text + g_w[d_num] + "\nRecipient . . . . . . . . : "+ g_buyer[d_num] + "\nFinal Destination . . . . : " + g_dst[d_num] + "\nDelivery Status . . . . . : "+g_stat[d_num]
    print(d_text)
    if not set_as:
        b = input("Type \"Confirm\" to delete this item record: ")
        if b.lower() == "confirm" : g_num[d_num] = -1; saveall()
        else: print("Process has been cancelled.")
    else: g_num[d_num] = -1; saveall()
    while True:
        b = input("Do you want to search and delete any other item record?(y/n): ")
        if b.lower() == "yes" or b.lower() == 'y' : cmd5(); break;
        if b.lower() == "no" or b.lower() == 'n' : break;
        print("Please input \"Yes\" or \"No\"")
       
       
def setting():
    cls()
    with open("config.cfg","r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    f.close()
    data[0] = data[0].replace("length = ","")
    data[1] = data[1].replace("color_text = ","")
    data[2] = data[2].replace("color_background = ","")
    data[3] = data[3].replace("search_text = ","")
    data[4] = data[4].replace("search_background = ","")
    data[5] = data[5].replace("auto_clean = ","")
    data[6] = data[6].replace("auto_save = ","")
    setting_message = "Setting:\n\n    1. Display item length . . . . . . . . . . . . . ." + data[0] + "\n"
    setting_message = setting_message + "    2. Color of text . . . . . . . . . . . . . . . . ." + trans_color[data[1]] + "\n"
    setting_message = setting_message + "    3. Color of text background . . . . . . . . . . . " + trans_color[data[2]] + "\n"
    setting_message = setting_message + "    4. Color of searched text . . . . . . . . . . . . " + trans_color[data[3]] + "\n"
    setting_message = setting_message + "    5. Color of Searched text background . . . . . . ." + trans_color[data[4]] + "\n"
    setting_message = setting_message + "    6. Auto clean screen . . . . . . . . . . . . . . ." + data[5] + "\n"
    setting_message = setting_message + "    7. Auto save . . . . . . . . . . . .  . . . . . . " + data[6] + "\n"
    setting_message = setting_message + "    8. Restore the setting to default\n    9. Save and Exit"
    print(setting_message)
    setting_input = repeat("i","Input an number to change(1-9): ","Please input an integer!",setting_message)
    if setting_input>9 or setting_input <=0:
        color("error"); print("Range Error: Please input an integer between 1 to 9!"); color("reset")
        pause()
        cls()
        return setting()
    cls()
    if setting_input == 1:
        while True:
            setting_length = repeat("i","Input the length of item record(s) will show in one time (0 = show all in one time): ","Please input an integer only!!","")
            if setting_length < 0 :
                color("error"); print("Range Error: Please input an integer larger than or equal to 0!"); color("reset")
                pause()
                cls()
            else: data[0] = str(setting_length);break;
    if setting_input == 2:
        while True:           
            color_list_fore()
            setting_text = repeat("i","Input the color code (1-15): ","Please input an integer only!!","")
            if setting_text < 0 or setting_text > 15:
                color("error"); print("Range Error: Please input an integer between 1 to 15!");color("reset")
                pause()
                cls()
            else: data[1] = input2py[str(setting_text)]; break;
    if setting_input == 3:
        while True:
            color_list_back()
            setting_back = repeat("i","Input the color code (1-15): ","Please input an integer only!!","")
            if setting_back < 0 or setting_back > 15:
                color("error"); print("Range Error: Please input an integer between 1 to 15!");color("reset")
                pause()
                cls()
            else: data[2] = input2py[str(setting_back)]; break;
    if setting_input == 4:
        while True:           
            color_list_fore()
            setting_text = repeat("i","Input the color code (1-15): ","Please input an integer only!!","")
            if setting_text < 0 or setting_text > 15:
                color("error"); print("Range Error: Please input an integer between 1 to 15!");color("reset")
                pause()
                cls()
            else: data[3] = input2py[str(setting_text)]; break;
    if setting_input == 5:
        while True:
            color_list_back()
            setting_back = repeat("i","Input the color code (1-15): ","Please input an integer only!!","")
            if setting_back < 0 or setting_back > 15:
                color("error"); print("Range Error: Please input an integer between 1 to 15!");color("reset")
                pause()
                cls()
            else: data[4] = input2py[str(setting_back)]; break;
    if setting_input == 6:
        while True:
            setting_bool = input("True or False: ")
            if setting_bool.lower() not in check_bool:
                print("Please input \"True\" or \"False\" only!!")
                pause()
                cls()
            elif setting_bool.lower() == 'true' or setting_bool.lower() == 't': 
                data[5] = "True";break
            else: data[5] = "False";break
    if setting_input == 7:
        while True:
            setting_bool = input("True or False: ")
            if setting_bool.lower() not in check_bool:
                print("Please input \"True\" or \"False\" only!!")
                pause()
                cls()
            elif setting_bool.lower() == 'true' or setting_bool.lower() == 't': 
                data[6] = "True";break
            else: data[6] = "False";break
    if setting_input == 8:
        while True:
            setting_reset = input("Are you sure to restore all the setting? (Yes/No) ")
            if setting_reset.lower() not in check_continue:
                print("Please input \"yes\" or \"no\" only!!")                
                pause()
                cls()
            elif setting_reset.lower() == "yes" or setting_reset.lower() == "y": 
                    data[0] = '0'
                    data[1] = 'e'
                    data[2] = '0'
                    data[3] = '8'
                    data[4] = '4'
                    data[5] = 'True'
                    data[6] = 'False'
                    print("Data has been restored.")
                    pause()
                    break;
            else: print("Process has been cancelled.");pause();break;            
    f = open("config.cfg","w")
    f.write("length = " + data[0] + "\n")
    f.write("color_text = " + data[1] + "\n")
    f.write("color_background = " + data[2] + "\n")
    f.write("search_text = " + data[3] + "\n")
    f.write("search_background = " + data[4] + "\n")
    f.write("auto_clean = " + data[5] + "\n")
    f.write("auto_save = " + data[6] + "\n")
    f.close()
    if setting_input <= 7 : return setting();
    loading()
    
    
def color_list_fore():
    print("\n####################################################\n")
    print("ForeGround: ")
    print("\n####################################################\n")
    os.system('echo|set /p="[30m[107m1. Black"')
    print()
    os.system('echo|set /p="[0m[31m2. Dark Red"')
    print()
    os.system('echo|set /p="[0m[32m3. Dark Green"')
    print()
    os.system('echo|set /p="[0m[33m4. Dark Yellow"')
    print()
    os.system('echo|set /p="[0m[34m5. Dark Blue"')
    print()
    os.system('echo|set /p="[0m[35m6. Dark Magenta"')
    print()
    os.system('echo|set /p="[0m[36m7. Dark Cyan"')
    print()
    os.system('echo|set /p="[0m[37m8. Gray"')
    print()
    os.system('echo|set /p="[0m[91m9. Red"')
    print()
    os.system('echo|set /p="[0m[92m10. Green"')
    print()
    os.system('echo|set /p="[0m[93m11. Yellow"')
    print()
    os.system('echo|set /p="[0m[94m12. Blue"')
    print()
    os.system('echo|set /p="[0m[95m13. Magenta"')
    print()
    os.system('echo|set /p="[0m[96m14. Cyan"')
    print()
    os.system('echo|set /p="[0m[97m15. White"')
    print()
    os.system('echo|set /p="[0m')
def color_list_back():
    print("\n####################################################\n")
    print("BackGround: ")
    print("\n####################################################\n")
    os.system('echo|set /p="[0m[40m1. Black[0m"')
    print()
    os.system('echo|set /p="[0m[41m2. Dark Red[0m"')
    print()
    os.system('echo|set /p="[0m[42m3. Dark Green[0m"')
    print()
    os.system('echo|set /p="[0m[43m4. Dark Yellow[0m"')
    print()
    os.system('echo|set /p="[0m[44m5. Dark Blue[0m"')
    print()
    os.system('echo|set /p="[0m[45m6. Dark Magenta[0m"')
    print()
    os.system('echo|set /p="[0m[46m7. Dark Cyan[0m"')
    print()
    os.system('echo|set /p="[30m[47m8. Gray[0m"')
    print()
    os.system('echo|set /p="[0m[101m9. Red[0m"')
    print()
    os.system('echo|set /p="[0m[102m10. Green[0m"')
    print()
    os.system('echo|set /p="[0m[103m11. Yellow[0m')
    print()
    os.system('echo|set /p="[0m[104m12. Blue[0m"')
    print()
    os.system('echo|set /p="[0m[105m13. Magenta[0m"')
    print()
    os.system('echo|set /p="[30m[106m14. Cyan[0m"')
    print()
    os.system('echo|set /p="[30m[107m15. White[0m"')
    print()
    os.system('echo|set /p="[0m')
   
def loading():
    cls()
    try: 
        with open("config.cfg","r") as f:
            data = f.readlines()
        data = [x.strip() for x in data]
        global set_length, set_text, set_bg, set_stext, set_sbg, set_ac, set_as
        set_length = data[0].replace("length = ","")
        set_text = data[1].replace("color_text = ","")
        set_bg = data[2].replace("color_background = ","")
        set_stext = data[3].replace("search_text = ","")
        set_sbg = data[4].replace("search_background = ","")
        set_ac = data[5].replace("auto_clean = ","")
        set_as = data[6].replace("auto_save = ","")
        set_ac = strtobool(set_ac)
        set_as = strtobool(set_as)
        os.system("color " + py2cmd[set_bg] + py2cmd[set_text])
    except: 
        f = open("config.cfg","w")
        f.write("length = 0\n")
        f.write("color_text = e\n")
        f.write("color_background = 0\n")
        f.write("search_text = 8\n")
        f.write("search_background = 4\n")
        f.write("auto_clean = True\n")
        f.write("auto_save = False\n")
        f.close()
        return loading() 
    
########################## MAIN PAGE ##############################
########################### SETTING ###############################
 
# Check the file is exist or not
if not os.path.isfile('./inventory.txt'):
    f = open("inventory.txt","x")
    f.close()
if not os.path.isfile('./config.cfg'):
    f = open("config.cfg","w")
    f.write("length = 0\n")
    f.write("color_text = e\n")
    f.write("color_background = 0\n")
    f.write("search_text = 8\n")
    f.write("search_background = 4\n")
    f.write("auto_clean = True\n")
    f.write("auto_save = False\n")
    f.close()
a = 0    
global set_length, set_text, set_bg, set_stext, set_sbg, set_ac, set_as
set_length = '0'
set_stext = '8'
set_text = 'e'
set_bg = '0'
set_sbg = '4'
set_ac = 'True'
set_as = 'False'
global ospass, trans_color, py2cmd, input2py, check_continue, check_bool
check_bool = ['t','f','true','false']
check_continue = ['yes','y','no','n']
ospass = True
input2py = {
    "1" : "0",
    "2" : "1",
    "3" : "2",
    "4" : "3",
    "5" : "4",
    "6" : "5",
    "7" : "6",
    "8" : "7",
    "9" : "8",
    "10" : "9",
    "11" : "a",
    "12" : "b",
    "13" : "c",
    "14" : "d",
    "15" : "e"  }
py2cmd = {
    "0" : "0",
    "1" : "4",
    "2" : "2",
    "3" : "6",
    "4" : "1",
    "5" : "5",
    "6" : "3",
    "7" : "8",
    "8" : "c",
    "9" : "a",
    "a" : "e",
    "b" : "9",
    "c" : "d",
    "d" : "b",
    "e" : "f"}
trans_color = {
    "0" : "Black",
    "1" : "Dark Red",
    "2" : "Dark Green",
    "3" : "Dark Yellow",
    "4" : "Dark Blue",
    "5" : "Dark Magenta",
    "6" : "Dark Cyan",
    "7" : "Gray",
    "8" : "Red",
    "9" : "Green",
    "a" : "Yellow",
    "b" : "Blue",
    "c" : "Magenta",
    "d" : "Cyan",
    "e" : "White"}
# Follow is to check the user open the python with start.bat or not
import distutils.spawn
try: 
    os.isatty(sys.stdout.fileno())
except:
    print("WARNING: This python file is recommanded to use \"start.bat\" open for a full function.")
    print("If \"start.bat\" is not exist. Type \"start\". It will restart this python with \"python.exe\" automatically.")
    b = input("Type \"start\" to continue: ")
    if b == "start":
        if not distutils.spawn.find_executable("python.exe") == "None":
            print("System cannot find the path of \"python.exe\".\n You can input the path of \"python.exe\" or double click the python file to open with \"python.exe\"")
            c = input("The path of \"Python.exe\" (e.g. C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37-32): ")
            os.system(c+'\python.exe "%CD%\ICP v6.py"')
        else: os.system('python.exe "%CD%\ICP v6.py"')
        sys.exit()
    else: sys.exit()
    ospass = False

loading()    
###############################  END ################################
    
while True:
    main()

