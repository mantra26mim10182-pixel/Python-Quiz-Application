from questions import questions
from result import show_result
from utils import check_answer


def start_quiz():

    score = 0

    for question in questions:

        print(question[0])
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])

        answer = input("Enter your answer: ").upper()

        if check_answer(answer):

            if answer == question[5]:
                print("Correct!")
                score = score + 1
            else:
                print("Wrong!")

        else:
            print("Invalid answer! Please enter A, B, C or D.")

    show_result(score, len(questions))