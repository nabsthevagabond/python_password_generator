#!/usr/bin/env python3

import re
import random


class PyGen:
    currentPassword = ""
    minLength = 8
    maxLength = 16

    list_alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    list_alpha_upper = list_alpha_lower.upper()
    list_numbers = "0123456789"
    list_symbols = "!@#$%&*?"

    # strongPassword requires a password minimum length = 8 and at 3/4 of the following:
    #   uppercase
    #   lowercase
    #   specail characters
    #   numbers

    passwordStrength = 0

    def __init__(self, password, minLength=8, maxLength=16):
        self.currentPassword = password
        self.minLength = minLength
        self.maxLength = maxLength

    def password(self):
        return self.currentPassword

    def check_uppercase(self):
        regex = r"[A-Z]"
        match = bool(re.search(regex, self.currentPassword))
        return 1 if match else 0

    def check_lowercase(self):
        regex = r"[a-z]"
        match = bool(re.search(regex, self.currentPassword))
        return 1 if match else 0

    def check_special_character(self):
        regex = r"[!@#$%&*?]"
        match = bool(re.search(regex, self.currentPassword))
        return 1 if match else 0

    def check_number(self):
        regex = r"\d"
        match = bool(re.search(regex, self.currentPassword))
        return 1 if match else 0

    def check_passwordlength(self):
        # pass length is greater 8
        return 1 if len(self.currentPassword) >= 8 else 0

    def is_password_strong(self):
        password_strength = int(self.check_lowercase() + self.check_uppercase() + self.check_number() + self.check_special_character())
        return True if password_strength >= 3 else False
    
    def shuffled_character_space(self):
        tmp_space = list(self.list_alpha_lower +  self.list_alpha_upper +  self.list_numbers + self.list_symbols)
        random.shuffle(tmp_space)
        return "".join(tmp_space)

    def secure_password(self):
        chr_space = self.shuffled_character_space()
        return chr_space

    def __repr__(self):
        objStr = f"Password: {self.currentPassword}\nMinimum Length: {self.minLength}\nMaximum Length: {self.maxLength}\n"
        return objStr


obj = PyGen("hello")
print(f"Password: {obj.password()}")
print(f"Contains Number: {obj.check_number()}")
print(f"Sufficent Length: {obj.check_passwordlength()}")
print(f"Contains Lowercase: {obj.check_lowercase()}")
print(f"Contains Special characters: {obj.check_special_character()}")
print(f"Strong Password: {obj.is_password_strong()}")
print(f"secure Password: {obj.secure_password()}")
