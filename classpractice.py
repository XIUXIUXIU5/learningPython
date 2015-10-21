#!/usr/bin/env python

import pdb

class someone(object):
    pass


class Student(object):

	#all the functions in class needs to have self as first para, but don't need to pass this in
    def __init__(self, name, score):
        self.name = name
        self.__score = score #__make the member private, _ means intend to be private but not 'real' private

    def print_score(self):
        print '%s: %s' % (self.name, self.__score)
        
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


class collegeStudent(Student): #inheritence
    def __init__(self, name, score):
    	Student.__init__(self, name, score)

	def print_score(self):
		print 'college score is' 
		print '%s: %s' % (self.name, self.__score)

shaolei = collegeStudent('shaolei',99)
shaolei.print_score()

type(shaolei)
isinstance(shaolei,collegeStudent)
dir(shaolei)


#handle error
#python -O filename.py will turn off assert
try:
    print 'try...'
    n = int('0')
    pdb.set_trace() #this is setting breakpoint
    #p variablename can print variable
    #n run this line of code
    #q quit
    #c continue
    assert n != 0, 'n is zero!'
    r = 10 / n
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'
