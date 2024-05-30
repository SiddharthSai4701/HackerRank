import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bn = str(bin(n))[2:]
    print("BN: ", bn)
    maxConsecutiveOnes = 0
    consecutiveOnes = 0

    for i in range(len(bn)):
        # print("BN[I]: ", bn[i])
        if bn[i] != '0':
            consecutiveOnes += 1
            # print("Consecutive Ones: " + str(consecutiveOnes))
        else:
            if consecutiveOnes > maxConsecutiveOnes:
                maxConsecutiveOnes = consecutiveOnes
            consecutiveOnes = 0

    if consecutiveOnes > maxConsecutiveOnes:
        maxConsecutiveOnes = consecutiveOnes
    print("Max consecutive Ones: " + str(maxConsecutiveOnes))




