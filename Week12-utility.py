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
def FindWordCount(input_list, input_string):
    counter = 0
    for i in input_list:
        counter += i.count(input_string)
    return(counter)

#ScoreFinder

#Union

#Intersection

#NotIn