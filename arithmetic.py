# write your code here
import random

questions = 0
correct = 5


class WrongTake(Exception):
    def __str__(self):
        self.err = "Wrong format! Try again."
        return self.err


print("Which level do you want? Enter a number:", "1 - simple operations with numbers 2-9",
      "2 - integral squares of 11-29", sep="\n")
option = int(input())



while questions != 5:

    try:
        if option == 1:
            guess_A = random.randint(2, 9)
            guess_B = random.randint(2, 9)
            operator = random.choice(["+", "-", "*"])
            task = F"{guess_A} {operator} {guess_B}"
            answer = eval(task)
            print(task, sep="\n")

            while True:
                choice = input()
                if choice.isdigit() or choice[1:].isdigit():
                    choice = int(choice)
                    break
                else:
                    print(WrongTake())

            if choice == answer:
                print("Right!", sep="\n")

            else:
                correct -= 1
                print("Wrong!", sep="\n")

        elif option == 2:
            sqr_intergral = random.randint(11, 29)
            double_intergral = sqr_intergral ** 2
            print(sqr_intergral)
            try:
                while True:
                    user_answer = input()
                    if user_answer.isdigit() or user_answer[1:].isdigit():
                        user_answer = int(user_answer)
                        break
                    else:
                        print(WrongTake())

                if user_answer == double_intergral:
                    print("Right!")

                else:
                    correct -= 1
                    print("Wrong!")


            except ValueError:
                raise WrongTake



        else:
            print(WrongTake())
    except WrongTake as err:
        print(err)

    finally:
        questions += 1

print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.", sep="\n")
user_selection = input()
if user_selection in ['yes', 'YES', 'y', 'Yes']:
    print("What is your name?")
    level = "level 1 (simple operations with numbers 2-9)." if option == 1 else "level 2 (integral squares of 11-29)."
    name = input()
    file = open("results.txt", "a")
    file.write(f"{name}: {correct}/5 in {level}")
    file.close()
    print("The results are saved in \"results.txt\".")
else:
    exit()
