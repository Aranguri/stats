# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:24:54 2018

@author: Perni
"""

from pg import PG
pg = PG()

import random as r


def writeText():

    words = []

    words.append('hello')

    for i in range(1000):
        previousWord = words[-1]

        ranNum = r.random()

        cumFreq = 0.0

        nextWord = ''

        wordDict = pg.distFn(previousWord)


        for word in wordDict.keys():
            cumFreq += wordDict[word]

            if (cumFreq > ranNum):
                nextWord = word
                break

        words.append(nextWord)

    return words

a = writeText()
print (' '.join(a))
