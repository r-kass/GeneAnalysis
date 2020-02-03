import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

#-----------------------------------------------------------
#   Filename: Project2
#   Author: Ruby Kassala
#   Course: CSS 383 - Bioinformatics
#   Date: 2017.05.28
#   Decription: Script that takes .txt input from a BLAST
#               query to compare the average similatity
#               between two sequences.
#
#               Will print averages to the console, and
#               display graphs
#
#   Usage:      python project2_script.py filename.txt
#
#   Notes:      Ensure .txt files are in the same directory
#
#               Can only view one graph and output at a
#               time; exit the first graph to view
#               additional comparison output
#
#               Uncomment to store the rest of the data in
#               varibles, or to add additional comparisons
#-----------------------------------------------------------


def geneStats (data, filename):
    count = 0 #vertical count
    #qseqid = 0
    #sseqid = 0
    pindent = 0 #percentage of identical matches
    alignlength = 0 #alignment length
    mismatch = 0 #number of mismatches
    #gapopen = 0 #number of gap opening
    #qstart = 0 #start of alignment in query
    #qend = 0 #end of alignment in query
    #sstart = 0 #start of alignment in subject
    #send = 0 #end of alignment in subject
    evalue = 0  #expect value
    bitscore = 0 #bit score

    maxPindent = 0
    maxAlignlength = 0
    maxMismatch = 0
    maxEvalue = 0
    maxBitscore = 0

    for line in data:

        dataArray = line.split()
        #qseqid = dataArray[0]
        #sseqid = dataArray[1]
        thisPindent = float(dataArray[2])
        pindent += float(dataArray[2])
        thisAlignlength = float(dataArray[3])
        alignlength += float(dataArray[3])
        thisMismatch = float(dataArray[4])
        mismatch += float(dataArray[4])
        #gapopen = dataArray[5]
        #qstart = dataArray[6]
        #qend = dataArray[7]
        #sstart = dataArray[8]
        #send = dataArray[9]
        thisEvalue = float(dataArray[10])
        evalue += float(dataArray[10])
        thisBitscore = float(dataArray[11])
        bitscore += float(dataArray[11])

        if (thisPindent > maxPindent):
            maxPindent = thisPindent
        if (thisAlignlength > maxAlignlength):
            maxAlignlength = thisAlignlength
        if (thisMismatch > maxMismatch):
            maxMismatch = thisMismatch
        if (thisEvalue > maxEvalue):
            maxEvalue = thisEvalue
        if (thisBitscore > maxBitscore):
            maxBitscore = thisBitscore
        count+=1


    #find averages
    pindentAve = pindent/count
    alignlengthAve = alignlength/count
    mismatchAve = mismatch/count
    evalueAve = evalue/count
    bitscoreAve = bitscore/count

    print('Maximum percentage of identical matches = ' + str(maxPindent) + '\n')
    print('Maximum alignment length = ' + str(maxAlignlength) + '\n')
    print('Maximum number of mismatches = ' + str(maxMismatch) + '\n')
    print('Maximum expect value = ' + str(maxEvalue) + '\n')
    print('Maximum bitscore = ' + str(maxBitscore) + '\n')



    print('Average percentage of identical matches = ' + str(pindentAve) + '\n')
    print('Average alignment length = ' + str(alignlengthAve) + '\n')
    print('Average number of mismatches = ' + str(mismatchAve) + '\n')
    print('Average expect value = ' + str(evalueAve) + '\n')
    print('Average bitscore = ' + str(bitscoreAve) + '\n')

    # graphing code
    objects = ('aveP', 'aveL', 'aveM', 'aveB', 'maxP', 'maxL', 'maxM', 'maxB')
    y_pos = np.arange(len(objects))
    performance = [pindentAve, alignlengthAve, mismatchAve, bitscoreAve, maxPindent, maxAlignlength, maxMismatch, maxBitscore]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('')

    # add numbers for additional comparison graphs
    plt.title(filename)
    plt.show()
    plt.close()

filename = sys.argv[1]
print('\n' +'---------' + filename + '---------\n')
file1 = open(filename, "r")
data1 = file1.readlines()
geneStats(data1, filename)


# ADD MORE FILES FOR COMPARISON HERE
# print('\n' +'--------- HUMAN - XX COMPARISON ---------' + '\n')
# file3 = open("HUMAN_XX_output.txt", "r")
# data3 = file3.readlines()
# geneStats(data3, 3)
