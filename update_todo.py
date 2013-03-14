#!/usr/bin/python

# Copyright (c) <2013>, <Benjamin Ross>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met: 
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution. 
#
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#       ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#       WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#       DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#       ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#       (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#       LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#       ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#       SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import sys, getopt
import re, os
from itertools import islice
import linecache

def main(argv):
    infile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:", ["file="])
    except getopt.GetoptError:
        print "update_todo -i <infile>"
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print "update_todo -i <infile>"
            sys.exit()
        elif opt in ("-i", "--file"):
            infile = arg 

    print "Updating: ", infile

    # Regex to match date
    re_date = re.compile(r'([0-9]{1,2}/[0-9]{1,2})')
    f = open(infile, 'r+')
    num_lines = sum(1 for line in f)
    last_date = ''
    date_line = 0
    f.seek(0)
    for i, line in enumerate(f.readlines()):
        searchedstr = re_date.findall(line)
        for word in searchedstr:
            last_date = word
            date_line = i
            break
    f.close()
    copy_lines = []
    for i in range (date_line, num_lines):
        line = linecache.getline(infile,i)
        copy_lines.append(line)
    re_complete = re.compile(r'\s*X.*')
    for line in copy_lines:
        searchedstr = re_complete.findall(line)
        for word in searchedstr:
            print "Word :" + str(word)
            print "Line: " + line
if __name__ == "__main__":
    main(sys.argv[1:])
