#NABREU November 2016

def fileopen(filename):
        f=open(filename)
        tstring=f.read()
        f.close()
        return tstring

def makearray(warray):

        warray=[]
        for line in wstring:
            Warray.extend(line)
        return Warray

def main():
    #Edit these with the correct file locations
    #Cfile is your converted picture in a txt file
    #pname is your poem in a txt file
    Convertfile='mario.txt'
    poemfile='mariopoem.txt'

    #opens the file
    CLpoem=(poemfile)
    Curlinepoem=CLpoem.read()

    Wordarray = []
    for line in Curlinepoem:
            Wordarray.extend(line)

    # Length of current line Word array
    wordcount=len(Wordarray)

    # Opened File
    CLpic = open(Convertfile)
    Curlinepic=CLpic.read()

    # Make CurentLine into a string of single characters
    Asciiarray = []
    for line in Curlinepic:
            Asciiarray.extend(line)

    # Length of current line Asciiarray
    asciicount=len(Asciiarray)
    current=0

    Continue='true'

    # Compare to string of single characters
    while(Continue=='true'):
            if Asciiarray[line]!= ' ' | line != wordcount | line != asciicount:
                Asciiarray[line]=Wordarray[current]
                current+=1
                line+=1
            if line == wordcount:
                # What if end of poem?
                for line in Curlinepoem:
                    Wordarray.extend(line)
                wordcount = len(Wordarray)
            if line == asciicount:
                # What if end of picture?
                # Write to txt first line
                for line in Curlinepic:
                    Asciiarray.extend(line)
                asciicount = len(Asciiarray)
            else:
                line+=1
