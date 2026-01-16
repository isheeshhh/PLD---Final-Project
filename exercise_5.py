#Name: Irish B. De Guzman
#Date: November 13, 2025
#Title: Exercise 5 - Grades Computation

def run_exercise_5():
    #function for computing grades
    def grades_computation(activity_name, percentage):
        activity_list = []
        activity_num = 0

        while True:
            #inputs the number of activities
            activity_getNum = input(f"Enter the number of {activity_name}: ")
            try:
                activity_getNum_int = int(activity_getNum)
                break
            except:
                print("Invalid input.")
                continue

        #loop that gets the scores
        while len(activity_list) < (activity_getNum_int):
            activity_num += 1
            activity_list.append(None)
            activity_getScore = input(f"Enter your grade in {activity_name} {activity_num}: ")
            
            try:
                activity_score = int(activity_getScore)
                activity_list[-1] = activity_score

            except:
                print("Invalid input.")
                activity_list.pop()
                activity_num -= 1
                continue

        #computes the total of scores
        activity_total = sum(activity_list)

        #computes the percentage score
        activity_PS = (activity_total / (activity_getNum_int * 100)) * 100

        #computes the weighted score
        activity_WS = activity_PS * percentage
        return activity_list, activity_PS, activity_WS

    #function for printing grades
    def print_grades(activity_name, catergory_name, list_name):
        print(f"{activity_name} ({catergory_name})")
        for index, items in enumerate(list_name):
            print(f"{activity_name} {index + 1} = {items}")
        print("------------------------------------")

    print("Grades Computation")
    
    print("\nLecture\n")

    print("Assignment\n")
    lecAssList, lecAssPs, lecAssWs = grades_computation("Assignment", 0.15)
    print("\nProject\n")
    lecProjList, lecProjPs, lecProjWs = grades_computation("Project", 0.20) 
    print("\nRecitation\n")
    lecRecitList, lecRecitPs, lecRecitWs = grades_computation("Recitation", 0.10) 
    print("\nQuiz\n")
    lecQuizList, lecQuizPs, lecQuizWs = grades_computation("Quiz", 0.25) 
    print("\nExamination\n")
    lecExamList, lecExamPs, lecExamWs = grades_computation("Examination", 0.30) 

    print("\nLaboratory\n")

    print("Assignment\n")
    labAssList, labAssPs, labAssWs = grades_computation("Assignment", 0.15)
    print("\nProject\n")
    labProjList, labProjPs, labProjWs = grades_computation("Project", 0.20) 
    print("\nRecitation\n")
    labRecitList, labRecitPs, labRecitWs = grades_computation("Recitation", 0.10) 
    print("\nQuiz\n")
    labQuizList, labQuizPs, labQuizWs = grades_computation("Quiz", 0.25) 
    print("\nExamination\n")
    labExamList, labExamPs, labExamWs = grades_computation("Examination", 0.30) 

    #computes the final grade for lecture
    finalLec = lecAssWs + lecProjWs + lecRecitWs + lecQuizWs + lecExamWs

    #computes the final grade for laboratory
    finalLab = labAssWs + labProjWs + labRecitWs + labQuizWs + labExamWs

    #computes the final grade
    finalGrade = (finalLec * 0.70) + (finalLab * 0.30)

    #rounds off the final grade to the nearest hundreths
    roundedFinalGrade = round(finalGrade, 2)

    #rounds up or rounds down the final grade
    integer = int(roundedFinalGrade)

    if roundedFinalGrade > integer:
        roundFinalGrade = integer + 1
    else:
        roundFinalGrade = integer

    print("\n")
    lecAssPrint = print_grades("Assignement","Lecture", lecAssList)
    lecProjPrint = print_grades("Project","Lecture", lecProjList)
    lecRecitPrint = print_grades("Recitation","Lecture", lecRecitList)
    lecQuizPrint = print_grades("Quiz","Lecture", lecQuizList)
    lecExamPrint = print_grades("Examination","Lecture", lecExamList)

    labAssPrint = print_grades("Assignement","Laboratory", labAssList)
    labProjPrint = print_grades("Project","Laboratory", labProjList)
    labRecitPrint = print_grades("Recitation","Laboratory", labRecitList)
    labQuizPrint = print_grades("Quiz","Laboratory", labQuizList)
    labExamPrint = print_grades("Examination","Laboratory", labExamList)

    print(f"\nFinal lecture: {finalLec:.2f}")
    print(f"Final lab: {finalLab:.2f}")
    print(f"Rounded Final Grade (int): {roundFinalGrade} \n")

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