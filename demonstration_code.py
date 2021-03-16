# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:06:00 2021

@author: Minghim
"""


alphabet="bcdfghjklmnpqrstvwxyz"
code = "cdfghjklmnpqrstvwxyzb"
special="aeiou"
code_special="iouae"

full_alphabet=alphabet+special
full_code=code+code_special



numbers="1234567890 "

code="zwyxtvkmnl_"


message_coded= "mty_www"

str1=''
for c in message_coded:
    i=code.index(c)
    passw=numbers[i]
    str1=str1+passw
    print(str1)
    
print(str1)