#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys():
    n = int(raw_input())

    s = raw_input()

    if n==len(s):
        res=0
        ses=0
        for i in range(len(s)):
            if(s[i]=='U'):
                res=res+1
            elif(s[i]=='D'):
                ses=ses+1
        return res
        return ses
    print res
    
countingValleys()
        




  


