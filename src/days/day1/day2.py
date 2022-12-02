from file_parse import file_rows_to_list, list_of_strs_to_ints
# 1,A,X = Rock
# 2,B,Y = Paper
# 3,C,Z = Scissorsvenv
#Rock > Scissors > Paper > Rock...

input = file_rows_to_list("inputs\input2.txt")
total_score = 0
for row in input:
    temp_score = 0
    if row[0] == 'A':
        if row[2] == 'X':
            temp_score+=3
            temp_score+=1
        elif row[2] == 'Y':
            temp_score+=6
            temp_score+=2
        elif row[2] == 'Z':
            temp_score+=0
            temp_score+=3
    elif row[0] == 'B':
        if row[2] == 'X': #
            temp_score+=0
            temp_score+=1
        elif row[2] == 'Y':
            temp_score+=3
            temp_score+=2
        elif row[2] == 'Z':
            temp_score+=6
            temp_score+=3
    elif row[0] == 'C':
        if row[2] == 'X':
            temp_score+=6
            temp_score+=1
        elif row[2] == 'Y':
            temp_score+=0
            temp_score+=2
        elif row[2] == 'Z':
            temp_score+=3
            temp_score+=3
    total_score+=temp_score

print(total_score)