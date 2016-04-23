import random
from os import path


class PriorityList:
    def __init__(self):
        self._olist = []
        self._priority = {}
        self._plist = []
        self._rlist = []
        self._length = []

    def getoriginal(self):
        return self._olist

    def getpriority(self):
        return self._priority

    def getprioritylist(self):
        return self._plist

    def add2original(self, line, index):
        self._olist += [line[index]]

    def keeplength(self, line, index):
        self._length += [line[index]]

    def getlengthlist(self, index):
        return self._length[index]

    @property
    def getlength(self):
        return len(self._length)

    def createpriority(self):
        for i in range(len(self._olist) - 1):
            self._priority[self._olist[i]] = len(self._olist) - i

    def createprioritylist(self):
        for eachThing in self._priority:
            for i in range(self._priority[eachThing]):
                self._plist += [eachThing]

    def randomlist(self):
        for i in range(10):
            a = random.randint(0, len(self._olist) - 1)
            if self._plist[a] not in self._rlist:
                if self._plist[a] != '.':
                    self._rlist += self._plist[a]
            else:
                a = random.randint(0, len(self._olist) - 1)

    def getrandomlist(self):
        return self._rlist

    def getrandomindex(self, index):

        return self._rlist, index

    def __str__(self):
        return str(self._olist)

    def __repr__(self):
        return self._olist


def canes3():
    wwd = PriorityList()
    haw = PriorityList()
    clean = PriorityList()
    mystery = PriorityList()
    train = PriorityList()

    mainlist = ['What we do', 'How and Why', 'Cleanliness', 'Mystery Shops',
                'Training']
    trycount = 0
    while True and trycount < 3:
        try:
            fname = '/Users/Aaron/Documents/list.csv'
            efile = open(fname, 'r')  # opens file and reads it
            trycount = 10  # If it works then it won't go through the loop again

        except FileNotFoundError:
            print('File not found. Try count =', trycount, '/3')
            trycount += 1  # If it is not found it will add to the try count
            if trycount == 3:  # Stops program if file is not found after 3 tries
                print('File not found. Out of tries.')
                return False

    ofname = '/Users/Aaron/Documents/PyOutput.csv'
    if path.isfile(ofname):  # Checks to see if the file you want to create exists
        q = str(input('File exists... overwrite? (y for yes, n for no): '))
        q = q.lower()  # Makes sure that the y or n is lowercase no matter what is entered
        if q == 'y':
            ofile = open(ofname, 'w')
        else:
            return False  # Ends the program if you do not want to overwrite the file
    else:
        ofile = open(ofname, 'w')  # If it does not exist, it just opens like normal

    line = efile.readline()  # Skips the first line because it is the title
    line = efile.readline()
    while line != '':  # All lists are assumed to be the same size

        line = line.strip()
        line = line.split(',')

        wwd.add2original(line, 0)  # Adds the first thing to the first list
        haw.add2original(line, 1)  # Adds the second thing to the second list
        clean.add2original(line, 2)  # 3rd
        mystery.add2original(line, 3)  # 4th
        train.add2original(line, 4)  # 5th

        wwd.keeplength(line, 0)
        haw.keeplength(line, 1)
        clean.keeplength(line, 2)
        mystery.keeplength(line, 3)
        train.keeplength(line, 4)

        line = efile.readline()

    for i in range(4):
        ofile.write(mainlist[i])
        if i != 4:
            ofile.write(',')
        else:
            ofile.write('\n')
    for i in range(wwd.getlength - 1):
        ofile.write(wwd.getlengthlist(i))
        ofile.write(',')
        print(ofile)
        ofile.write(haw.getlengthlist(i))
        ofile.write(',')
        ofile.write(clean.getlengthlist(i))
        ofile.write(',')
        ofile.write(mystery.getlengthlist(i))
        ofile.write(',')
        ofile.write(train.getlengthlist(i))
        ofile.write('\n')

    wwd.createpriority()
    haw.createpriority()
    clean.createpriority()
    mystery.createpriority()
    train.createpriority()

    wwd.createprioritylist()
    haw.createprioritylist()
    clean.createprioritylist()
    mystery.createprioritylist()
    train.createprioritylist()

    wwd.randomlist()
    haw.randomlist()
    clean.randomlist()
    clean.randomlist()
    mystery.randomlist()
    train.randomlist()

    ofile.write('Priority Lists')
    ofile.write('\n')

    for i in range(4):
        ofile.write(mainlist[i])
        if i != 4:
            ofile.write(',')
        else:
            ofile.write('\n')
    for i in range(9):
        ofile.write(wwd.getrandomindex(i))
        ofile.write(',')
        ofile.write(haw.getrandomindex(i))
        ofile.write(',')
        ofile.write(clean.getrandomindex(i))
        ofile.write(',')
        ofile.write(mystery.getrandomindex(i))
        ofile.write(',')
        ofile.write(train.getrandomindex(i))
        ofile.write('\n')

    final = {}
    final[mainlist[0]] += [wwd.getrandomlist]
    final[mainlist[1]] += [haw.getrandomlist]
    final[mainlist[2]] += [clean.getrandomlist]
    final[mainlist[3]] += [mystery.getrandomlist]
    final[mainlist[4]] += [train.getrandomlist]

    print(final)

    ofile.close()
    efile.close()
