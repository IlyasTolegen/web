import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2:
        print("Weird")
    elif not n%2 and 5>=n and n>=2:
        print("Not Weird")
    elif not n%2 and 20>=n and n>= 6:
        print("Weird")
    else:
        print("Not Weird")