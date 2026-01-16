import exercise_1, exercise_2, exercise_3, exercise_4, exercise_5, exercise_6

while True:
    choice = input("\nEnter the number of exercise you want to run (1-6): ")
    try:
        choice_int = int(choice)
        if choice_int == 1:
            exercise_1.run_exercise_1()
        elif choice_int == 2:
            exercise_2.run_exercise_2()
        elif choice_int == 3:
            exercise_3.run_exercise_3()
        elif choice_int == 4:
           exercise_4.run_exercise_4()
        elif choice_int == 5:
            exercise_5.run_exercise_5()
        elif choice_int == 6:
            exercise_6.run_exercise_6()
        else:
            print("\nInput out of range. Please enter a number from 1-6.")
            continue
    except:
        print("\nInvalid input. Please enter a valid number.")
        continue
    
    while True:
        choice_2 = input("\nDo you want to run another exercise? (yes or no): ").strip().upper()
        if choice_2 == "YES":
            break
        elif choice_2 == "NO":
            print("\nThank you!\n")
            exit()
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
            continue




        