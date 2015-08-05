#! /usr/bin/env python

# Will output a file with min, mid, and max values given
# a data set formatted such as "(10)14-17(23) mm"
# with or without a range or extreme values

inFile = open('num-list.txt', 'r')
outFile = open('num-sep.tsv', 'w')

import re

def isRange(valueRange):
    if '-' in valueRange:
        return True
    else:
        return False

def average(valueMin, valueMax, unit):
    valueMin = float(valueMin)
    valueMax = float(valueMax)
    if unit == 'cm':
        valueMin = valueMin*10
        valueMax = valueMax*10
    avg = (valueMin+valueMax)/2
    return avg

def convertCm(val, unit):
    val = float(val)
    if unit == 'cm':
        val = val*10
    return val

for line in inFile:
    line = line.strip('\n')

    try:
        unitSplit = line.split(' ')
        valRange = unitSplit[0]
        unit = unitSplit[1]
        
        try:
            exMin = re.search('^\(([\d\.]+?)\)', valRange)
            if exMin.group(1) != None:
                exMin = exMin.group(1)
                valRange = re.sub('^(\([\d\.]+?\))', '', valRange)
        except:
            exMin = ''
        try:
            exMax = re.search('\(([\d\.]+?)\)$', valRange)
            if exMax.group(1):
                exMax = exMax.group(1)
                valRange = re.sub('(\([\d\.]+?\))$', '', valRange)
        except:
            exMax = ''
        
        if isRange(valRange):
            valRange = valRange.split('-')
            if exMin != '' and exMax != '':
                avg = average(valRange[0], valRange[1], unit)
            elif exMin == '' and exMax != '':
                avg = average(valRange[0], valRange[1], unit)
                exMin = valRange[0]
            elif exMin != '' and exMax == '':
                avg = average(valRange[0], valRange[1], unit)
                exMax = valRange[1]
            elif exMin == '' and exMax == '':
                avg = average(valRange[0], valRange[1], unit)
                exMin = valRange[0]
                exMax = valRange[1]
            exMax = convertCm(exMax, unit)
            exMin = convertCm(exMin, unit)
        else:
            avg = float(valRange)
            if unit == 'cm':
                avg = avg*10

        exMin = str(exMin)
        avg = str(avg)
        exMax = str(exMax)

        print exMin+'\t'+avg+'\t'+exMax
        outFile.write(exMin+'\t'+avg+'\t'+exMax+'\n')

    except:
        print line
        outFile.write(line+'\n')

inFile.close()
outFile.close()
