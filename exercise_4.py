#Name: Irish B De Guzman
#Date: November 4, 2025
#Title: Exercise 4 - Grades Computation

def run_exercise_4():
    #funtion for computing the percentage and weighted score
    def grades_computation(activity_name, percentage_str, percentage_int):
        #initializes the perfect score to 100
        perfect_score = 100
        #inputs the grade
        activity_grade = int(input(f"Enter your {activity_name} grade ({percentage_str}): "))
        #computes the percentage score
        activity_Ps = (activity_grade / perfect_score) * 100
        #computes the weighted score
        activity_Ws = activity_Ps * percentage_int
        return activity_Ps, activity_Ws

    print("Welcome to Grades Computation\n")
    print("\nClass Standing (Lecture) 70%\n")

    lecAssPs, lecAssWs = grades_computation("assignment", "15%", 0.15)
    lecProjPs, lecProjWs = grades_computation("project", "20%", 0.20)
    lecRecitPs, lecRecitWs = grades_computation("recitation", "10%", 0.10)
    lecQuizPs, lecQuizWs = grades_computation("quiz", "25%", 0.25)

    print("\nExamination (Lecture) 30%\n")

    lecExamPs, lecExamWs = grades_computation("examination", "30%", 0.30)

    print("\nClass Standing (Laboratory) 70%\n")
    labAssPs, labAssWs = grades_computation("assignment", "15%", 0.15)
    labProjPs, labProjWs = grades_computation("project", "20%", 0.20)
    labRecitPs, labRecitWs = grades_computation("recitation", "10%", 0.10)
    labQuizPs, labQuizWs = grades_computation("quiz", "25%", 0.25)

    print("\nExamination (Laboratory) 30%\n")
    labExamPs, labExamWs = grades_computation("examination", "30%", 0.30)

    #total of class standing (lecture) grade
    lecTotalCs = (lecAssWs + lecProjWs + lecRecitWs + lecQuizWs) 

    #computes the final (lecture) grade
    finalLecture = lecExamWs + lecTotalCs

    #total of class standing (lab) grade
    labTotalCs = (labAssWs + labProjWs + labRecitWs + labQuizWs) 

    #computes the final (lab) grade
    finalLab = labExamWs + labTotalCs

    #computes the final grade
    finalGrade = (finalLecture * 0.70) + (finalLab * 0.30)

    #rounds off the final grade to the nearest hundreths
    roundedFinalGrade = round(finalGrade, 2)

    #rounds up or rounds down the final grade
    integer_part = int(roundedFinalGrade)
    decimal_part = round(roundedFinalGrade - integer_part, 2)

    if decimal_part >= 0.50:
        roundFinalGrade = integer_part + 1
    else:
        roundFinalGrade = integer_part

    print(f"Final lecture: {finalLecture}")
    print(f"Final lab:  {finalLab}")

    #outputs the final grade and remarks
    if roundFinalGrade >= 97 and roundFinalGrade <= 100:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.00. You Passed!")
    elif roundFinalGrade >= 94 and roundFinalGrade <= 96:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.25. You Passed!")
    elif roundFinalGrade >= 91 and roundFinalGrade <= 93:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.50. You Passed!")
    elif roundFinalGrade >= 88 and roundFinalGrade <= 90:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 1.75. You Passed!")
    elif roundFinalGrade >= 85 and roundFinalGrade <= 87:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.00. You Passed!")
    elif roundFinalGrade >= 82 and roundFinalGrade <= 84:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.25. You Passed!")
    elif roundFinalGrade >= 79 and roundFinalGrade <= 81:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.50. You Passed!")
    elif roundFinalGrade >= 76 and roundFinalGrade <= 78:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 2.75. You Passed!")
    elif roundFinalGrade == 75:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 3.00. You Passed!")
    else:
        print(f"Your final grade is {roundedFinalGrade} which is equivalent to 5.00. You Failed!")