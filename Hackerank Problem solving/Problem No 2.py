#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    s = list(s)
    res = []
    numbers = []
    i = 0
    
    # প্রথমে স্ট্রিংয়ের শুরুতে থাকা সংখ্যাগুলো সংগ্রহ করি
    while i < len(s) and s[i].isdigit() and s[i] != '0':
        numbers.append(s[i])
        i += 1
        
    # বাকি স্ট্রিং প্রসেস করা শুরু করি
    while i < len(s):
        # যদি '0' পাই, তবে জমানো সংখ্যা দিয়ে রিপ্লেস করি (পিছন থেকে)
        if s[i] == '0':
            res.append(numbers.pop())
            i += 1
        # যদি দেখি দুটি অক্ষরের পরে '*' আছে (যেমন: aB*)
        elif i + 2 < len(s) and s[i+2] == '*':
            # আবার সোয়াপ করি (B + a)
            res.append(s[i+1])
            res.append(s[i])
            i += 3 # অক্ষর দুটি এবং '*' পার হয়ে যাই
        else:
            # সাধারণ অক্ষর হলে সরাসরি যোগ করি
            res.append(s[i])
            i += 1
            
    return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()