#! /usr/bin/env python
# coding: utf-8

#### This program will search text descriptions for floral terms
#### and write results to a tab-delimited text file. It requires three columns:
#### (1) Some identifier (2) Description to search (3) URL location of species
#### Or placeholder values for any
#### 
#### EDIT SEARCH TERMS IN THE FUNCTION doFileSearch


import re, time, codecs

fileList = ['mesoonline_plain.txt', 'mesopdfs_plain.txt']

print 'Ready to search, do you want to search all files or search individually?'
print 'Please enter A for all or I for individual'
searchCheck = raw_input()
while True:
    if searchCheck == 'A' or searchCheck == 'a':
        doAll = True
        break
    elif searchCheck == 'I' or searchCheck == 'i':
        doAll = False
        break
    else:
        print "That's not a valid choice, please try again"
        searchCheck = raw_input()


def searchForTerm(term, descript):

    varInfo = []
    while True:
    
        varResult = re.search('(?i)([^.\t!?;]*?%s.*?(?<!(mm|ca|cm|\sc))(?<!(&lt|&gt))[.;\t])(?!\d)' % term, descript)
        try:
            varResult = varResult.group(1)
            descript = descript.replace(varResult,'') # Remove result from description before running the search again
            varInfo += [varResult]
        except:
            break
    for i in varInfo:
        i.decode('utf-8')
    return varInfo

def doFileSearch(InFile, OutFile):
    for Line in InFile:
        
        Line = Line.strip('\n')
        Line = Line.strip('\r')
        ElementList = Line.split('\t')
        resList = []

        try:
            SpName = ElementList[0]
        except:
            SpName = 'name_error'
        try:
            URL = ElementList[2]
        except:
            URL = 'url_error'
        try:
            SpDesc = repr(ElementList[1])
        except:
            print 'ERROR ERROR ERROR'
        
        resList.append(SpName)
        
        ### <------- Add/change search terms here! ------->
        StyleResult = searchForTerm('style', SpDesc) ; resList.append(StyleResult)
        StigmaResult = searchForTerm('stigma', SpDesc) ; resList.append(StigmaResult)
        OvuleResult = searchForTerm('ovul', SpDesc) ; resList.append(OvuleResult)
        OvaryResult = searchForTerm('ovar', SpDesc) ; resList.append(OvaryResult)
        CarpelResult = searchForTerm('carpel', SpDesc) ; resList.append(CarpelResult)
        PistilResult = searchForTerm('pistil', SpDesc) ; resList.append(PistilResult)
        GynoeciumResult = searchForTerm('gynoecium', SpDesc) ; resList.append(GynoeciumResult)
        StamenResult = searchForTerm('stamen', SpDesc) ; resList.append(StamenResult)
        FilamentResult = searchForTerm('filament', SpDesc) ; resList.append(FilamentResult)
        AntherResult = searchForTerm('anther', SpDesc) ; resList.append(AntherResult)
        PetalResult = searchForTerm('petals', SpDesc) ; resList.append(PetalResult)
        CorollaResult = searchForTerm('corolla', SpDesc) ; resList.append(CorollaResult)
        FlowerResult = searchForTerm('flower', SpDesc) ; resList.append(FlowerResult)
        SpurResult = searchForTerm('spur', SpDesc) ; resList.append(SpurResult)
        SpatheResult = searchForTerm('spathe', SpDesc) ; resList.append(SpatheResult)
        WingResult = searchForTerm('wings', SpDesc) ; resList.append(WingResult)
        KeelResult = searchForTerm('keel', SpDesc) ; resList.append(KeelResult)
        ### <--------------------------------------------->

        resList.append(URL)
        print 'Done with : ' + SpName
        OutFile.write(('%s\t'*len(resList) % tuple(resList)) + '\n')

    InFile.close()
    OutFile.close()

########## Individual file search
if doAll == False:
    print 'OK! What is the name of file to search?'
    InFileName = raw_input()

    while True:
        try:
            InFile = codecs.open(InFileName, encoding='utf-8', mode='r')
            if not InFileName.endswith('.txt'):
                print 'File name must end with ".txt", please try again'
                InFile.close()
                InFileName = raw_input()
            else:
                break
        except:
            print 'No such file exists by that name, please try again:'
            InFileName = raw_input()
    print 'OK!'
    time.sleep(1)

    newOut = re.search('(.+?)\.txt', InFileName)
    OutFileName = newOut.group(1)+'_RESULTS.txt'
    OutFile = codecs.open(OutFileName, encoding='utf-8', mode='w')
    doFileSearch(InFile, OutFile)
else: ########### Loop over all files
    print 'Searching over all files'
    time.sleep(1)
    for flora in fileList:
        InFileName = flora
        InFile = codecs.open(InFileName, encoding='utf-8', mode='r')
        newOut = re.search('(.+?)\.txt', InFileName)
        OutFileName = newOut.group(1)+'_RESULTS.txt'
        OutFile = codecs.open(OutFileName, encoding='utf-8', mode='w')
        doFileSearch(InFile, OutFile)
