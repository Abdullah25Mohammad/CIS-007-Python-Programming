#10.1
#Assign grades
#Abdullah Mohammad
#1/20/23

scores = input("Enter a list of scores: ")

scoresListString = scores.split()
scoresList = [eval(scoreStrings) for scoreStrings in scoresListString]

best = max(scoresList)
count = 0

for score in scoresList:
    if score >= best - 10:
        grade = 'A'
    
    elif score >= best - 20:
        grade = 'B'
            
    elif score >= best - 30:
        grade = 'C'
            
    elif score >= best - 40:
        grade = 'D'
    
    else:
        grade = 'F'
    
    count += 1

    print("Student", count, "score is", grade)

