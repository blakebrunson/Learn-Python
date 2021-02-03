# character_name = "preston"
# character_race = "mouse"


# # basic string commands

# print("I had a mouse named " + character_name + ", ")
# print("He liked being a mouse")
# print("but he didn't like being named " + character_name )

# character_name = "Sam"
# print(character_name + ", ya silly lad!")


# print("giffage\ncabbave")  

# phrase = "Giffrage Acnaemy"
# print(phrase + "is cool")

# print(phrase.lower())
# print(phrase.upper())

# print(phrase.isupper())

# print(phrase[0])
# print(phrase[3])
# print(phrase[5])


# print(phrase.index("n"))


# print(phrase.replace("age", "heuihs"))


# ###########################################


# print(4 * 5.8)

# my_num = -11
# print(pow(3,2))  # 3 to the power or 2

# print(max(4,7))  # prints the highest number
# print(min(3,9))
# print(round(3.21))


# # in python you import stuff

# from math import *

# print(floor(3.7))
# print(ceil(4.3))
# print(sqrt(49.01))

# name = input("enter your name: ")
# print(name)




# ## while loop ##

# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print (n)


# # getting out of a loop - BREAK #

# #while True:
# #    line = input('> ')
# #    if line == 'done' :
# #        break
# #    print(line)
# #print('Done!')

# # FOR loops / definite loops  #

# for i in [5, 4, 3, 2, 1] :
#     print(i)
# print('Blastoff!')


# friends = ['Joe', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy new year ', friend)
# print('Done!')


# # Loop Idioms ##############

# #making smart loops#

# print('Before')
# largest = -1
# for thing in [9,3,18,37,1,60,22,6]:
#     if thing > largest:
#         largest = thing
#     print(largest, thing)
# print('after', largest)




# #############################

# #finding average in a loop#

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [1, 19, 30, 3, 54, 5]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count, sum, sum/count)

# ### filtering / finding with boolean ##
# found = False
# print('Before', found)
# for value in [9,44,53,1,3,6,11] :
#     if value == 3 :
#         found = True
#     print(found, value)
# print('After', found)


# ## how to find the smallest value ##
# #                                 https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/iterations-more-patterns

# smallest = None  ## None is a constant that is often used to flag ' empty'
# print('Before', smallest)
# for the_num in[9,31,45,6,90,21,] :
#     if smallest is None:
#         smallest = value
#     elif the_num < smallest :
#         smallest = the_num
#     print(smallest, the_num)
# print('After', smallest)


# ## is and is not operators ##  'is' is stronger than == becuase it demands Type of variable is the same ##



# ##         ##
# ## STRINGS ##
# ##         ##

# fruit = 'banana'
# letter = fruit[1]
# print(letter)

# x = 3
# w = fruit[x-1]
# print(w)

# ## looping through strings ##
# ## using a while statement and an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually.

# fruit = 'banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1 

# ## REPLACE iteration variable with FOR loop

# fruit = 'banana'
# for letter in fruit :
#     print (letter)


# # looping and counting #  https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/strings-in-python

# word = 'banana'
# count = 0
# for letter in word :
#     if letter == 'a' :
#         count = count + 1
# print(count, letter)


# ## Slicing Strings # 

# s = 'Monty Python'
# print(s[0:4])     ## 's sub 0 through 4'  start at pos 0 and go up through but not including 4'

# print(s[8:])  

# ## string concatenation:

# a = 'hello'
# b = 'there'

# print (a + b)
# print (a + ' ' + b)


# ## using IN as a logical operator

# fruit = 'banana'
# 'n' in fruit  #[True]

# 'm' in fruit  #[False]

# 'nan' in fruit  #[True]

# if 'a' in fruit :
#     print('found it')


# ## STRING LIBRARY

# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)
# # hello bob

# ## visit docs.python.org/3/library/stdtypes.html#string-methods


# # Searching a string:

# fruit = 'banana'
# pos = fruit.find('na')
# print(pos)
# # 2

# aa = fruit.find('z')
# print(aa)
# # -1


# ## search and replace

# greet = 'Hello Bob'
# nstr = greet.replace('Bob', 'Jimmy')
# print(nstr)
# # Hello Jimmy


# #(other examples of string library - refer to link.

# # parsing and extracting

# data = 'FROM stephen.marquard@uct.ac.za Sat Jan   5 09:14:16: 2008'
# atpos = data.find('@')  #find position of @ sign
# sppos = data.find(' ',atpos) #find the next ' ' after the at sign
# # atpos = 21  sppos = 31
# host = data[atpos+1 : sppos] #get the data string between one after @ sign and through the next space position. You don't have to worry about the space since this is up to but not including the space ' ' )
# print(host)
# # uct.ac.za

# # in python 3, all strings are Unicode, but in 1 and 2 there were different kinds of strings <type 'unicode'>


# ##
# ## Chapter 7     ##
# ## READING FILES ##  https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/reading-files
# ##

# # (intro - file types)

# ## using Open

# # handle = open(filename, mode)

# #returns a handle use to manipuate the file (
# # filename is a string
# # mode is optional and should be the 'r' if we are planning to read the file and 'w' if we are going to write to the file

# #fhand = open('mbox.txt')
# #print(fhand)
# #>> <_io.TextIOWrapper name = 'mbox.txt' mode = 'r' encoding = 'utf8'

# #the newline character   \n   causes to go to new line
# stuff = 'Hello\nWorld!'
# print(stuff)

# ##
# # Reading files in python - Files as a Sequence (of lines - and we're going to use loops to do this)
# ##


# xfile = open('mbox-short.txt')
# for beer in xfile:    ## other languages are harder to do this in, this is really nice in python
#     print(beer)

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count +1
# print('Line Count:', count)


# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# # 94626
# print(inp[0:20])

# ## searching through a file

# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:') :
#         print(line)


# #output will have double newlines because the pring statement adds one too
# # so...

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()  #gets rid of whitespace at right of string
#     if line.startswith('From:') :
#         print(line)



# # needle in a haystack -- finding certain lines
# # structure the loop differently
# print('#########################\n#########################')


# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()  
#     if not '@uct.ac.za' in line:
#         continue   #only runs through the good code you want
#     print(line)

# #using quit() to end a pyton cleanly with no tracebakcs

# fname = input('Enter the file name:  ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()

# count = 0 
# for line in fhand:
#     if line.startswith('Subject:') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# ##               ##
# ##               ##
# ## CHAPTER EIGHT ##  lists...
# ##               ##
# ##               ##



# # lists - surprise we already used them #

# # friends = ['Joe', 'Glenn', 'Sally']
# #for friend in friends:
# #    print('Happy new year ', friend)
# #print('Done!')

# #sub 0, sub 1 because it's base 0

# # lists are mutable - we can change an element using the index opeprator
# # unlike strings - which are immutable and cannot change the contents of a string. we make a new string to make a change. 


# # how long is a list - len(listname)

# # using the range function - returns a list of numbers that range from zero to one less than the parameter
# # we can sonstruct an index loop using for and an integer iterator

# print(range(4))
# #[0, 1, 2, 3]
# friends = ['Joe', 'Glenn', 'Sally']
# print(len(friends))
# #3
# print(range(len(friends)))
# #[0, 1, 2]


# #two loops do the same thing:

# friends = ['Joe', 'Glenn', 'Sally']
# #1
# for friend in friends :
#     print('Happy New Year:', friend)

# #2
# for i in range(len(friends)) :
#     friend = friends[i]
#     print('Happy New Year:', friend)



# # Concatenating lists using +

# a = [1, 2, 3]
# b = [4,5,6]
# c = a + b
# print(c)

# # slice lists

# t = [8, 5, 65, 7, 9, 12, 5, 15]
# u = t[1:3]
# #[5,7]

# v = t[:2]
# print(v)       #     ...up to but not including
# #[8, 5]

# ####
# # Building a list from scratch:
# ###

# stuff = list()
# stuff.append('book')    # append
# stuff.append(80)
# print(stuff)
# stuff.append('cookie')
# print(stuff)

# #lists are in order and have other functions

# friends = ['Joe', 'Glenn', 'Sally']
# friends.sort()
# print(friends)

# #built in functions:
# #len
# #max
# #sum



# ###### EXAMPLES USING LISTS FOR PROGRAM ######

# total = 0
# count = 0
# while True :
#     inp = input('Enter a number:  ')
#     if inp == 'done' : break
#     value = float(inp)               # convert string number into float value
#     total = total + value
#     count = count +1

# average = total / count
# print('Average:', average)


# ######

# # numlist = list()
# # while True:
# #     inp = input('Enter a number please: ')
# #     if inp == 'done' : break
# #     value = float(inp)
# #     numlist.append(value)     # this method used a list

# # average = sum(numlist) / len(numlist)  
# # print('Average:', str(average))




# ## Lists and strings ##

# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# #  >> ['With', 'three', 'words']
# print(len(stuff))
# print(stuff[0])


# ## split looks for spaces by default, and doesnt matter how many spaces are in between
# ## so split on something else:

# line = 'first;second;third'
# thing = line.split(';')
# print(thing)
# # >> ['first', 'second', 'third']


# # more parsing using Split
# # lets get the day of the week out on all this

# # example data: From stephen.marque@uct.za Sat Jan 5 09:14:16 2008

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From ') : continue
#     words = line.split()
#     print(words[2])



# ###
# ### the double split pattern

# # From stephen.marque@uct.za Sat Jan 5 09:14:16 2008
# fhand = open('mbox-short.txt')
# for line in fhand:
#     if not line.startswith('From ') : continue
#     words = line.split()
#     email = words[1]    # >> stephen.marque@uct.za
#     # now split the email
#     pieces = email.split('0')
#     print(pieces[0])



# #
# ##
# ###
# ####
# #####
# ##### DICTIONARIES                    chapter 9  ################
# #####
# ####
# ###
# ##
# #  unlike lists - there is no order - everything has a KEY

# # Lists Vs Dictionaries - dictionaries are like lists except that
# # they use keys instead of numbers to look up values. 

# ddd = dict()
# ddd['age'] = 21
# ddd['course'] = 182
# print(ddd)
# # >>{'course': 182, 'age': 21}

# ddd['age'] = 27
# print(ddd)
# # >>{'course': 182, 'age': 27}    # we changes the key's value


# # "in a list, the key is always the position"


# ### Dictionary Literals (Constants)
# # dictionary liters use curly braces and have a list of key: value pairs
# # you can make an impty dictionary using empty curly braces

# jjj = {'chuck' : 1 , 'fred' : 42, 'jan': 100}
# print(jjj)

# ooo = {}   # this is a shortcut method of doing >>  ooo = dict()
# print(ooo)

# #############################################
#                   #counting#
# #############################################



# ccc = {}
# ccc['bob'] = 1
# ccc['randy'] = 1

# ccc['randy'] = ccc['randy'] + 1
# print(ccc)

# # >>{'bob': 1, 'randy': 2)


# #### seeing a new name

# counts = dict()
# names = ['aa', 'bb', 'cc', 'dd', 'ee', 'aa', 'cc', 'ee']
# for name in names :
#     if name not in counts:
#         counts[name] = 1
#     else :
#         counts[name] = counts[name] + 1
# print(counts)


# ##
# ## the GET method: since checking to see if a key is there is so common:
# # instead of:
# if name in counts:
#     x = counts[name]
# else :
#     x = 0
# # use get method:
# x = counts.get(name, 0)   

# # so...

# counts = dict()
# names = ['aa', 'bb', 'cc', 'dd', 'ee', 'aa', 'cc', 'ee']
# for name in names :
#     x = counts.get(name, 0) + 1
# print(counts)


# ###### Counting Pattern
# # 1. split lines into words
# # 2. loop through the words and use...
# # a dictionary to track the count of each word independently

# counts = dict()
# print('Enter a line of text')
# line = input('')

# words = line.split()

# print('Words:', words)

# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) +1
# print('Counts', counts)


# ## dictionaries: Retrieving lists of keys and values...

# jjj = {'chuck' : 1 , 'fred' : 42, 'jan': 100}
# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())

# # > ['chuck', 'fred', 'jan']
# # > dict_keys(['chuck', 'fred', 'jan'])
# # > dict_values([1, 42, 100])
# # > dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])


# ####
# #### finding the most common word in a file

# name = input('Enter file:')
# handle = open(name)

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)




# #############################
# ## Tuples   #################
# ##        ######### ch. 10 ##
# #############################


# #Tuples are a lot like lists except they have () instead of []
# #BUT tuples are IMMUTABLE, meaning you cannot alter their contents - similar to a string. 

# # DO NOT do these things to tuples: sort, append, reverse 

# # you CAN put a tuple on a left side of an argument
# #e.g. :

# (x, y) = (4, 'fred')
# print(y)
# #>> fred
# (a, b) = (99, 98)   # cant have 2 of left and 3 of right
# print(a)
# #>> 99


# ######   items()   ######

# # The items() method in dictionaries...
# # ...returns a list of (key, value) tuples


# d = dict()
# d['bob'] = 2
# d['mary'] = 4
# for (k, v) in d.items():
#     print(k, v)
# #>> bob 2
# #>> mary 4

# tups = d.items()
# print(tups)
# #>> dict_items([('bob', 2), ('mary', 4)])


# ## tuples are comparable  ##

# # the comparison operators work with tuples and other sequences. 
# # if the first item is equal, Python goes on to the next element, 
# # and so on until it finds elements that differ. 

# (0, 1, 2) < (5, 1, 3)
# #>> True     ... 0 is less than 5

# (0, 1, 200) < (0, 3, 4)
# #>> True    ... no decision on 0=0 so moved on to 1<3. 

# ## also for strings (alphabetical order)



# #### sorting lists of Tuples  ##
# ####                            ##

# #sorted function:

# d = {'fred' : 42, 'chuck' : 1 , 'jan': 9}
# d.items()
# #>> dict_items([('fred' : 42), ('chuck' : 1) , ('jan': 9)])\
# print(sorted(d.items()))
# #>> [('chuck', 1), ('fred', 42), ('jan', 9)]   # sorted this by key in ascending, without considering value. 


# ## use the SORTED function to take a sequence as a parameter and returns a sorted sequence

# d = {'fred' : 42, 'chuck' : 1 , 'jan': 9}
# t = sorted(d.items())

# for k, v in sorted(d.items()):
#     print(k, v)

# #>> chuck 1
# #>> fred 42
# #>> jan 9        this is a pretty powerful thing that's easy to do in python


# #look for the most common word - using clervely created data structure
# # append tuples into a list but in value, key orientation
# # then you can use sorted wich will look at the values first. 

# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k, v in c.items() :
#     tmp.append( (v, k) )

# print(tmp)
# #>> [(10, 'a'), (22, 'c'), (1, 'b')]

# tmp = sorted(tmp, reverse=True)
# print(tmp)

# #>> [(22, 'c'), (10, 'a'), (1, 'b')]


# ###
# ### print out the most common words in a file! ###
# # # # # # # # # # # # # # # # # # # # # # # # # ##

# fhand = open('mbox-short.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0 ) + 1    # this is our "idiom" for making a histogram - we use this a lot

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for val, key in lst[:10] :  #lets just print the top 10
#     print(key, val)     # and print in the key, value order. 

# #>> Jan 352
# #>> 2008 324
# #>> by 245
# #>> Received: 243
# #>> -0500 219
# #>> from 218
# #>> 4 203
# #>> with 194
# #>> Fri, 183
# #>> id 136


# ### EVEN SHORTER VERSION ###  ^ above was more procedural. below is using ' lambdas' - create a closed form - do it in one statement there's alot of stuff going on
# ### kind of bonus material 
# # List comprehension creates a dynamic list. 
# #In this case, we make a list of the reversed tuples and then sort it.

# c = {'a':10, 'b':1, 'c':22}
# print( sorted( [ (v,k) for k,v in c.items() ] ) )   #https://youtu.be/dZXzBXUxxCs?t=561



# ###########################################
# ###########################################
# #### Chapter ELEVEN #######################
# #################### Regular Expressions ##
# ###########################################




# import re

# hand = open('mbox-short.txt')
# for line in hand:
#     line.rstrip()
#     if re.search('^From:', line) :
#         print(line)


# # wild-card characters
# # the dot character matches any character
# # if you add the asterisk character, the character is "any number of time"

# hand = open('mbox-short.txt')
# for line in hand:
#     if re.search('^X.*:', line) :    # ^ = match start of line  . = match any char  * = many times  :and X = the characters ':' and 'x'
#         print(line)


# #

# hand = open('mbox-short.txt')
# for line in hand:
#     if re.search('^X-\S+:', line) :   # \S =  non-whitespace character   + = one or more times
#         print(line)


# ###### matching and extracting data #

# # re.search() returns a True/False depending on whether the string matches the regular expression
# # if we actually want the matching strings to be extracted, we use re.findall()

# # [0-9]+  = one or more digits

# import re
# x = 'my 2 fav numbs are 19 and 32'
# y = re.findall('[0-9]+',x)
# print(y)

# y = re.findall('[AEIOU]+', x)
# print(y)   # does not find uppercase vowels and returns [] empty list


# ###

# # WARNING: Greedy Matching 
# # the repeat characters (* and + ) push outward in both directions...
# # ...(greedy) to match the largest possible string

# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)   
# print(y)
# #>> ['From: Using the :']    it chose the longest match to fulfill 


# # Non-Greedy Matching   -- add the ? 

# import re
# x = 'From: using the : character'
# y = re.findall('^F.+?:', x)
# print(y)
# #>> ['From:']

# # parentheses around some regex will return just the part inside

# import re
# x = 'From stephen.marqueard@uct.ac.az Sat Jan 5 '
# y = re.findall('\S+@\S+',x)
# print(y)

# x = 'From stephen.marqueard@uct.ac.az Sat Jan 5 '
# y = re.findall('^From (\S+@\S+)',x)
# print(y)


# ## string parsing examples  https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/regular-expressions-practical-applications

# # first review:

# data = 'From stephen.marqueard@uct.ac.az Sat Jan 5 '
# atpos = data.find('@')
# sppos = data.find(' ',atpos)
# host = data[atpos+1 : sppos]
# print(host)
# #>> uct.ac.az

# # more review - 'doubple split' pattern:

# line = 'From stephen.marqueard@uct.ac.az Sat Jan 5 '
# words = line.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])
# #>> uct.ac.az

# # OK now do in regex:

# import re
# lin = 'From stephen.marqueard@uct.ac.az Sat Jan 5 '
# y = re.findall('@([^ ]*)', lin)          # [^ ] = match non blank character, runs until it finds a non-blank
# print(y)
# #>> ['uct.ac.az']

# # even cooler regex version:

# import re
# lin = 'From stephen.marqueard@uct.ac.az Sat Jan 5 '
# y = re.findall('^From .*@([^ ]*)', lin)
# print(y)


# ###
# # Spam confidence program
# ###

# import re
# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.+)', line)
#     if len(stuff) != 1 : continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:', max(numlist))

# # escape characters  - \ 

# import re
# lin = 'Your total is $121.67 thank  you '
# y = re.findall('\$[0-9.]+', lin)
# print(y)



# ####################################################
# ####################################################

# # NETWORKING WITH PYTHON                           #
# #                                                  #
# #                                                  #

# # TCP = Transport Control Protocol
# # TCP connections - SOCKETS  -  an endpoint of a biderectional inter-process communication flow...
# # ...across and internet protocal-based computer network. such as the Internet. 
# # A Port is an app specific or process=specific software communications endpoint
# # ... It allows multiple networked apps to coexist on the same server. There is a list of well-known port numbers

# # Python has built-in support for TCP sockets

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.py4e.org', 80) )

# #  http://  www.dr-chuck.com  /page1.htm
# # protocol        host         document

# # watch  https://youtu.be/c6vZGescaSc?t=327

# #########################################
# # WRITE A WEB BROWSER ###################
# #########################################
# ###########write a web browser###########
# #########################################
# ###
# ##
# #


# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.py4e.org', 80) )
# cmd = 'GET http.py4e.org/romeo.txt HTTP/1.0\n\n' .encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()


# x = 5

# # we will use .encode() and .decode() when sending data in and out of python - because unicode and stuff. UTF-8


# #### Making urllib to make this even easier! 
# ## here's a 4 line web browser:

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://ignitetalksbtv.com/')
# for line in fhand:
#     print(line.decode().strip())


# ## parsing html easy way - Beautiful Soup
# ## need to install it... lesson: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-web-scraping-with-python


# # but for instance:

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('enter url - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
# # retrive all anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# # More resources:
# # - Exercise: socket1   https://www.youtube.com/watch?v=dWLdI143W-g
# # - Exercise: urllib   https://www.youtube.com/watch?v=8yis2DvbBkI
# # - Exercise: urllinks  https://www.youtube.com/watch?v=g9flPDG9nnY


# # Using Web Services video https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/using-web-services



# ##########  XML BASICS ##########
# ##########  XML BASICS ##########
# ##########  XML BASICS ##########
# ##     eXtensible Markup Language


# # start tag             <person>
# #                          <name>Chuck</name>
# # text content             <phone type = "intl">
# # attribute                  +1 734 378 4789
# # end tag                  </phone>
# # self closing tag         <email hide = "yes" />
# # end tag                </person>

# ## see example, XML as a tree  https://youtu.be/_pZ0srbg7So?t=192
# ## you can have multiple attributes on a node, but only one text


# ###### XML Schema ######
# # description of the legal format of an XML document
# # XML validation takes XML document and compares to the XML schema contract

# # XSD XML Schema #####################

# # XSD Structure:  xs:element, xs:sequence, xs:complexType
# # see here - https://youtu.be/yWU9kTxW-nc?t=119

# # example #  <xs:element name="full_name" type="xs:string"
# #            minOccurs="1" maxOccurs="1" />                  <-- means it's required and can only have 1

# # XSD data types: <xs:element name="startdate" type="xs:dateTime"/>
# #                 <xs:element name = "weeks" type="xs:integer"/>          # these are just examples

# # ISO 8601 Date/Time Format
# # 2002-05-30T09:30:10Z          # T = time of day    Z - timezone, Z = GMT



# # example of xml data self contained in a string: 

# import xml.etree.ElementTree as ET 
# data = '''<person>
#   <name>Chuck</name>
#   <phone type = "intl">
#     +1 734 292 3908
#     </phone>
#     <email hide="yes"/>
#   </person>'''

# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attr:',tree.find('email').get('hide'))    # getting pieces out of XML with call methods


# # multiple items are basically a list. https://youtu.be/yWU9kTxW-nc?t=717


# import xml.etree.ElementTree as ET 
# input = '''<stuff>
#   <users>
#     <user x="2">
#       <id>001</id>
#       <name>Chuck</name>
#     </user>
#     <user x="7">
#       <id>009</id>
#       <name>Sara</name>
#     </user>
#   </users>
# </stuff>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')   #find tags in users ending in /user
# for item in lst:
#     print('Name', item.find('name').text)
#     print('ID', item.find('id').text)
#     print('Attribute', item.get("x"))



# ######  JSON                  ###################################
# ###### you will see more JSON than XML - XML is better for tich documents, JSON is better for pulling data out
# ######

# ## json totally derives 

# import json
# data = '''{
#     "name: : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 873 982 0983"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''
# # remember this ^ will be given from the network

# info = json.loads(data)
# print('Name:',info["name"])
# print('Hide:',info["email"]["hide"])

# # for JSON, once you get a system for going back and forth, it's faster. 


# ######################
# ###### service oriented approach
# #              #########################


# # https://www.youtube.com/watch?v=mj-kCFzF0ME&ab_channel=ChuckSeverance


# # https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/web-services-apis

# ## Example of getting data from google maps API:
# # lat=js["results"][0]["geometry"]["location"]["lat"]
# # lng=js["results"][0]["geometry"]["location"]["lng"]

# ### Example of getting data from twitter api:    # look at dev.twitter.com/docs #

# while True:
#     print('')
#     acct = input('Enter Twitter Account')
#     if (len(acct) < 1): breakurl = twurl.augment(TWITTER_URL,
#                                                   {'screen_name' : acct, 'count': '5'})
#     print('Retrieving', url)
#     connection = urllib.request.urlopen(url)
#     data = connection.read() .decode()
#     headers = dict(connection.getheaders())
#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)
#     print(json.dumps(js, indent=4))

#     for u in js['users']:
#         print(u['screen_name'])
#         s = u['status']['text']
#         print('  ', s[:50])


# ############
# # LOTS of extra practice
# # https://www.youtube.com/watch?v=TJGJN0T8tak&ab_channel=freeCodeCampConcepts
# # https://www.youtube.com/watch?v=vTmw5RtfGMY&ab_channel=freeCodeCampConcepts
# # https://www.youtube.com/watch?v=2c7YwhvpCro&ab_channel=freeCodeCampConcepts



###################################################################################
###################################################################################
#######################

## PYTHON OBJECTS    ##
##                   ##
##                   ##  this is more of a terminology lecture, rather than learning new code

# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/python-objects


# 
# An object is a bit of self contained Code and Data
# Break the problem into smaller parts
# 
# Definitions ##########################################
# Class - a template
# Method or Message - A defined capability of a class
# Field or attribute - -A bit of data in a class
# Object or Instance - A particular instance of a class
# 
#  ##


### EXAMPLES coding with Class, Objects
# class is a reversed obj

class PartyAnimal:              # this is the template for making PartyAnimal objects
    x = 0                       # each PartyAnimal object has a bit of data

    def party(self) :           # each PartyAnimal object has a bit of code
        self.x = self.x + 1    
        print("So far",self.x)

an = PartyAnimal()             # contruct a PartyAnimal object and store in an

an.party                       # tell the an object to run the party() code within it
an.party
an.party                       # basically, PartyAnimal.party(an)


### Playing with dir()and type()

# dir() command lists capabilities

x = list()
print(type(x))
#>> <class 'list'>
print(dir(x))
#>> #['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
# 'remove', 'reverse', 'sort']


# soo... 

class PartyAnimal:              
    x = 0                     

    def party(self) :          
        self.x = self.x + 1    
        print("So far",self.x)

an = PartyAnimal()

print("Type", type(an))
#>> Type <class '__main__.PartyAnimal'>
print("Dir", dir(an))
#>> Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']



####################################
###   Object Lifecycle   ###

#####     #####      ###############


# objects are created, used and discarded
# We have special blocks of code (methods) that get called
#    At the moment of creation (constructor)
#    At the moment of destruction (destructor)
# Constructors are used a lot
# Destructors are seldom used


class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
            self.x = self.x + 1
            print('so far',self.x)

    def __del__(self):
            print('I am destructed', self.x)
    
an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

#>> I am constructed
#>> so far 1
#>> so far 2
#>> I am destructed 2
#>> an contains 42#

#### the constructor and destructor are optional.
#### the constructor is typcially used to set up variables.

 #
#### example with multiple instances   --  https://youtu.be/p1r3h_AMMIM?t=192
  #


###
###  Inheritance  - https://www.youtube.com/watch?v=FBL3alYrxRM&feature=emb_logo&ab_channel=freeCodeCampConcepts
         
        # the ability to extend a class to make a new class.
###


################
################
################

# RELATIONAL DATABASES and SQLite

##################################
##################################


# CREATE TABLE table_name (
#     column1 datatype, 
#     column2 datatype, 
#     column3 datatype)
#);


# EXAMPLE: 
# CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );



# SQL: Insert
# INSERT INTO Users (name, email) VALUES ('Kristen', 'kdonohue@yahoo.com)
# 
# SQL: Delete
# DELETE FROM Users WHERE email = 'kdonohue@yahoo.com'
# 
# SQL: Update
# UPDATE Users SET name = 'Robert' WHERE email='bobtheman@yahoo.com'
# 
# Retrieving Records: Select
# Select * FROM Users
# 
# Select * FROM Users WHERE email='bobtheman@yahoo.com'
# 
# ORDER BY
# SELECT * From Users ORDER BY email
# SELECT * From Users ORDER BY name DESC
# SELECT * From Users ORDER BY name ASC
# 
# 
# RELATIONAL DATABASE DESIGN
# 
# Database design is an art form
# We will learn  how to not make bad mistakes first..
# 
# Drawing a picture of the data objects for our application 
# and then figuring out how to represent the objects and their relationships
# Basic rule - dont put a string in more than once
# 
# https://youtu.be/AqdfbrpkbHk?t=262
# 
# 
# DATABASE Normalization (3NF)
# 
# integer reference pattern
# IDs basically - add keys and relate back to them just with the numbers. 
# 
# Relationship Building
# 
# Add an ID field to every one of these
# Track might have all possible data, but many are taken from foreign tables, which  can each just have their own id and 1 other column for the thing that it is - anytime there will be duplication

##################################################################################vvv
# CREATE TABLE Genre (
# 	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	title TEXT
# );

# CREATE TABLE Track (
# 	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	album_id INTEGER,
# 	genre_id INTEGER, len INTEGER, rating INTEGER, title TEXT, "count" INTEGER
# );

# insert into artist (name) VALUES ('Paul Simon')

# insert into Genre (

# UPDATE Album SET artist_id = "3" WHERE title = "Astral Weeks"

# ALTER TABLE Album
# ADD artist_id INTEGER;

# ALTER TABLE Genre
# RENAME COLUMN title TO "genre"

# insert into Track (title, count, album_id, genre_id)
#   values ('song3', 6, 3, 3)

#################################################################################^^^

#/\-||/|//




# JOIN ###


#
# 
# select Album.title, Artist.name from album join Artist on Album.artist_id = Artist.id
#       (table.field)           (the tables that hold the data)     (how the tables are linked)              
# 
# 
# Big Join across all tables
# 
# select track.title, artist.name, album.title, genre.name from Track join Genre join Album join Artist on Track.genre_id = Genre.id and track.album = album.id and album.artist_id = artist.id #

# rewritten:
# select track.title, artist.name, album.title, genre."genre" 
# from Track 
# join Genre 
# join Album 
# join Artist 
# on Track.genre_id = Genre.id 
# and track.album_id = album.id 
# and album.artist_id = artist.id


#### many to Many Relationships ####    https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/relational-databases-many-to-many-relationships

## make a join table or connector table

# CREATE TABLE "Member" (
# 	user_id INTEGER,
# 	course_id INTEGER,
# 	role INTEGER,
# 	PRIMARY KEY (user_id, course_id)
# );


# exercise: https://www.youtube.com/watch?v=qEkUEAz8j3o&ab_channel=freeCodeCampConcepts


# SELECT user.name, member.role, course.title
# FROM User JOIN Member JOIN Course
# ON member.user_id = user.id AND
# Member.course_id = Course.id
# ORDER BY Course.title, member.role DESC, User.name



#############################################################
#############################################################


#### final chapter - VISUALIZING DATA WITH PYTHON ###########
#                                                           #
#                                                           #
#

# Data Source  --Gather--   Clean/Process   --Visualize   --Analyze


#personal data mining
#GeoData - makes a google map from user entered data


# see the videos:
# https://www.youtube.com/watch?v=KfhslNzopxo&ab_channel=freeCodeCampConcepts
# https://www.youtube.com/watch?v=wSpl1-7afAk&ab_channel=freeCodeCampConcepts
# https://www.youtube.com/watch?v=H3w4lOFBUOI&ab_channel=freeCodeCampConcepts
# https://www.youtube.com/watch?v=LRqVPMEXByw&ab_channel=freeCodeCampConcepts
# https://www.youtube.com/watch?v=yFRAZBkBDBs&ab_channel=freeCodeCampConcepts
# https://www.youtube.com/watch?v=sXedPQ_AnWA&ab_channel=freeCodeCampConcepts
# https://www.youtube.com/watch?v=Fm0hpkxsZoo&ab_channel=freeCodeCampConcepts
