#!/usr/bin/env python

#Function

def hello_my_owner():
	name = raw_input('what is your name?	')
	if not isinstance(name,str):
		raise TypeError('bad')
	if name == 'shaolei':
		print 'hello my owner!', name
	elif name == 'liuxiao':
		print 'How did you find the way to run me?!!'
	else:
		print 'Oh wait, who are you?!!'
	return #Can be omitted

def nothing(x,y=2):
	pass
#for function that has not finished yet
#pass can be used in if as well

def multipleReturn():
	return 1,2,3
#this is actually returning a tuple

def arrayExampe():
	#list
	name = 'shaolei'
	classmate1 = raw_input()
	classmates = [name,classmate1]
	if len(classmates) == 2:
		print 'everything is fine'

	classmates.append('zhenzhen')
	print classmates

	classmates.pop()
	print classmates

	classmates.sort()
	print classmates

	#tuple unchangeable
	classmates2 = (name,classmate1)

	n = len(classmates)
	while n > 0:
		print 'hello'
		n = n - 1

	for x in classmates:
		print x

	return

def dictionaryEx():
	#raw_input
	year = int(raw_input('what is your birth year?'))

	dictionary = {'shaolei': 95,'liuxiao':94}
	dictionary['zhenzhen'] = 94
	if dictionary['shaolei'] == 95:
		print 'right'

	dictionary.pop('zhenzhen')

	if 'zhenzhen' not in dictionary:
		print "right"

	s = set([1,1,2,3,4,4,4])
	s.remove(1)
	print s	
	#s1 & s2 intersection set
	#s1 | s2 union
	return

def calc(*numbers,**numbers2): #use * can avoid make a list then pass as parameter
#now we can write the numbers in bracket directly when we call this
# * : for list ** : for dic
# can pass no parameter for these two
	sum = 0
	for x in numbers:
		sum = sum + x

	for i in range(0,len(numbers)):
		print i, numbers[i]

	return sum

#generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return

def fn(x, y):
    return x * 10 + y

def is_odd(n):
    return n % 2 == 1

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
#name 

#hello_my_owner()
name = 'shaolei'

# None is NULL

# 'Hi, %s, you have $%d.' % ('Michael', 1000000)

#arrayExampe()
#dictionaryEx()

name2 = name.replace('s','S')
print name #will remain smae but name2 is changed one
print name2

x,y,z = multipleReturn()
print x,y,z

print calc(1,2,3,4)
#same as above
numbers = [1,2,3,4]
print calc(*numbers)

#slicing
print 'slicing', numbers[0:2]

#create list
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ']

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print reduce(fn, [1, 3, 5, 7, 9])

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

print sorted([36, 5, 12, 9, 21], reversed_cmp)

map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])