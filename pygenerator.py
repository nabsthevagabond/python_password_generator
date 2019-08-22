#!/usr/bin/env python3

import re

class PyGen:
    currentPassword = ""
    minLength = 8 
    maxLength = 16
    
    #strongPassword requires a password minimum length = 8 and at 3/4 of the following:
    #   uppercase
    #   lowercase
    #   specail characters
    #   numbers

    passwordStrength = 0


    def __init__(self,password, minLength= 8, maxLength = 16 ):
        self.currentPassword = password
        self.minLength = minLength
        self.maxLength = maxLength

    def __repr__(self):
        objStr = f"Password: {self.currentPassword}\nMinimum Length: {self.minLength}\nMaximum Length: {self.maxLength}\n"
        return objStr



obj = PyGen("Hello World")
print(obj)