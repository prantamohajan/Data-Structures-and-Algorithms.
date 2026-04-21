#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    current_vowels = 0
    best_start_idx = -1
    
    # প্রথম উইন্ডো (0 থেকে k-1 পর্যন্ত) গণনা করা
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
            
    max_vowels = current_vowels
    if max_vowels > 0:
        best_start_idx = 0
        
    # স্লাইডিং উইন্ডো শুরু (বাকি স্ট্রিংয়ের জন্য)
    for i in range(k, len(s)):
        # নতুন ক্যারেক্টারটি ভাওয়েল হলে যোগ হবে
        if s[i] in vowels:
            current_vowels += 1
        # আগের উইন্ডোর প্রথম ক্যারেক্টারটি ভাওয়েল হলে বিয়োগ হবে
        if s[i - k] in vowels:
            current_vowels -= 1
            
        # যদি বর্তমান উইন্ডোতে আগের থেকে বেশি ভাওয়েল পাওয়া যায়
        if current_vowels > max_vowels:
            max_vowels = current_vowels
            best_start_idx = i - k + 1
            
    # যদি কোন ভাওয়েল না পাওয়া যায়
    if best_start_idx == -1:
        return "Not found!"
    else:
        return s[best_start_idx : best_start_idx + k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()