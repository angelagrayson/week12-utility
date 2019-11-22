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
    PrintOutput(new_string)

#FindWordCount
def FindWordCount(input_list, input_string):
    counter = 0
    for i in input_list:
        counter += i.count(input_string)
    return(counter)

#ScoreFinder
def ScoreFinder(player_names, player_scores, player_to_find):
    counter = 0
    found = False
    for i in player_names:
        if i.lower() == player_to_find.lower():
            found = True
            break
        else:
            counter +=1
    if found == False:
        PrintOutput('Player not found')
    else:
        output_string = player_to_find + ' got a score of ' + str(player_scores[counter])
        PrintOutput(output_string)

#Union
def Union(list_1, list_2):
    list_1 = list(dict.fromkeys(list_1))
    list_2 = list(dict.fromkeys(list_2))
    return(list_1 + list_2)

#Intersection

#NotIn