#ask how many student
count_student = int(input("How many : "))

#dictionaries for student, format {name:"score"}
dict_students = {}



#ask student and student's score
for i in range(count_student):
    name = input("\nName      :")
    value = int(input("score    : "))
    dict_students[name] = value




#sort the value to list 
list_rankstudents = sorted(dict_students.items(), key=lambda x: x[1],reverse=True)



#get and print highest
name_highestscore = list_rankstudents[0][0]
score_highestscore =  list_rankstudents[0][1]
print(f"highest score {name_highestscore}  {score_highestscore}")

#get and print lowest
lowest_index = count_student -1
name_lowestscore = list_rankstudents[lowest_index][0]
score_lowestscore =  list_rankstudents[lowest_index][1]
print(f"Lowest score {name_lowestscore}  {score_lowestscore}")









