#!/usr/bin/env python3

import re
import random


class PyGen:
    """
    # strongPassword requires a password minimum length = 8 and at 3/4 of the following:
    #  uppercase
    #  lowercase
    #  specail characters
    #  numbers
    """
    # password params
    currentPassword = ""
    minLength = 8
    maxLength = 16

    list_alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    list_alpha_upper = list_alpha_lower.upper()
    list_numbers = "0123456789"
    list_symbols = "!@#$%&*?"

    passwordStrength = 0

    def __init__(self, password="", minLength=8, maxLength=16):
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

    @property
    def is_password_strong(self):
        password_strength = int(self.check_lowercase(
        ) + self.check_uppercase() + self.check_number() + self.check_special_character())
        return True if password_strength >= 3 else False

    def shuffled_character_space(self):
        tmp_space = list(self.list_alpha_lower + self.list_alpha_upper +
                         self.list_numbers + self.list_symbols)
        random.shuffle(tmp_space)
        return "".join(tmp_space)

    @property
    def secure_password(self):
        chr_space = self.shuffled_character_space()
        self.currentPassword = ""

        while not self.is_password_strong:
            tmp_password = ""
            for _ in range(self.maxLength):
                index = random.randrange(len(chr_space))
                tmp_password += chr_space[index]
            self.currentPassword = tmp_password

        return self.currentPassword

    def __repr__(self):
        objStr = f"Password: {self.currentPassword}\nSecure Password: {self.is_password_strong}"
        return objStr


if __name__ == "__main__":
    obj = PyGen("Hello World!")
    print(obj)
