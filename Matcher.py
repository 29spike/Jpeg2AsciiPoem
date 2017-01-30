#!/usr/bin/python
#NABREU November 2016
import cmath
import math

def doitall(picturefile,poemfile):
	Ap,Piclen=grab(picturefile)	
# Ap = Ascii Picture Piclen = Picture length	
	Po,Polen=grab(poemfile)		
# Po = Poem Polen = Poem Length
#TODO: Finish convert function
#	Con=convert(Ap,Piclen,Po,Polen)
	makefile(Con,picturefile+"Converted.txt")

def grab(filename):
	f=open(filename)
        tstring=f.read()
	#with open(filename) as f:
	#	tstring=f.readlines()
	l=len(tstring)
	f.close()
	return tstring,l

def makefile(convertfile,filename):
	nf=file(filename,"w")
	for y in convertfile:
		for x in y:
			nf.write(str(x))
			nf.write(" ")
		nf.write("\n")
	nf.close()

#TODO: Finish convert function
#def convert(AsciiPic,Piclength,Poem,Poemlength):
#	for line	
