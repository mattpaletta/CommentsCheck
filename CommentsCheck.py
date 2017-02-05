from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import urllib2
import string
import math
import operator
from collections import OrderedDict
import fileinput
import os
import locale
import subprocess

def is_alias(path):
    return subprocess.check_output(["GetFileInfo", "-aa", path]) == "1\n"


locale.setlocale(locale.LC_ALL, 'en_US')

raw = ""

#READ FROM FILES
#f = open("gutenberg/1/GUTINDEX-2003.txt", "r")

rootdir = argv[1]
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        print "Reading: "+file
        if file.endswith('.java') and os.path.islink(os.path.join(root, file)) == False:
            for line in fileinput.input(os.path.join(root, file)):
                raw = line.rstrip()
                print (raw)
