#YOUR GITHUB REPO
# Angela Grayson
# CSCI 102 – Section A
# Week 11 - Part B

#PrintOutput
def PrintOutput(string):
    print('OUTPUT', string)

#LoadFile
def LoadFile(file_name):
    file_list = []
    f = open(file_name)
    file_list = f.readlines()
    f.close()
    return(file_list)

#UpdateString
def UpdateString(string_1, string_2, i):
    new_string = ''
    new_string = string_1[:i] + string_2 + string_1[i + 1:]
    return(new_string)

#FindWordCount

#ScoreFinder

#Union

#Intersection

#NotIn