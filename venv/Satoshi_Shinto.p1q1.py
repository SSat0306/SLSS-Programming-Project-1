# Quiz Creation Activity
# Author:Satoshi

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result.

import time

question = str(input("What is 1+1:")).strip(" ")
question_2 = str(input("What is 5+5:")).strip(" ")
question_3 = input("What is 3*3: A = 10 B = 12 C = 9 \n Answer the alphabet.").lower().strip(" ")
question_4 = str(input("What is the sum of the multiple 6 between 100 to 1000")).strip(" ")
question_5 = input("What is a line segment which the end points both lie on a curve called?").lower().strip(" ")

answer_score = 0

#If the answer is correct, score +1

if question == "2":
    answer_score += 1

    if question_2 == "10":
        answer_score += 1

        if question_3 == "c":
            answer_score += 1

            if question_4 == "82350":
                answer_score += 1

                if question_5 == "a chord" or "chord":
                    answer_score += 1

print("Here is your final score!!")

time.sleep(3)

#Print final score and the percentage.
print(f"You got {answer_score} out of 5!!")
print(f"So, you got {(answer_score * 100) / 5}%!! ")

if answer_score <= 5:
    print("You got all questions right! Awesome!! ")

elif answer_socre <= 3:
    print("You did well on the questions!")

