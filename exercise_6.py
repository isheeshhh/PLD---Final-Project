#Name: Irish B. De Guzman
#Date: November 13, 2025
#Title: Exercise 6 - Asterisk

def run_exercise_6():
    while True:
        print ("Select Pattern")
        print ("A, B, C")
        choice = input("Enter your selected pattern: ").strip().upper()
        
        # pattern A
        if choice == "A":
            print ("\nA")
            a = 5
            for i in range (a):
                for A in range (i + 1):
                    print ("*", end =" ")
                print ()
            a = 4
            for i in range (a):
                for A in range (i, a):
                    print ("*", end = " ")
                print()
        
        #pattern B
        elif choice == "B":
            print ("\nB")
            b = 4
            for i in range (b):
                for B in range (i, b):
                    print (" ", end = " ")
                for B in range (i+1):
                    print ("*", end = " ")
                print ()
            b = 5
            for i in range (b):
                for B in range (i):
                    print(" ", end = " ")
                for B in range (i, b):
                    print ("*", end =" ")
                print ()

        #pattern C
        elif choice == "C":
            print("\nC")
            for x in range(1, 10):
                if x == 5:
                    asterisk = x - 1
                    space = 2 * (5 - x) - 1
                    print("*", end=" ")
                elif x < 5:
                    asterisk = x
                    space = 2 * (5 - asterisk) - 1
                else:
                    asterisk = 10 - x
                    space = 2 * (5 - asterisk) - 1
                for i in range(asterisk):
                    print("*", end=" ")
                for i in range(space):
                    print(" ", end=" ")
                for i in range(asterisk):
                    print("*", end=" ")
                print()
        else:
            print("Invalid input. Please enter A, B, or C.")
            continue

        while True:
            again = input("\nDo you want to select another pattern? (yes or no): ").strip().upper()

            if again == "YES":
                break
            elif again == "NO":
                import final_project
                final_project.con()
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")