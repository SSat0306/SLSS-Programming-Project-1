# Quiz Creation Activity
# Author:Satoshi

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result.


import time

questions = {
    "What is 1+1": "2",
    "What is 5+5:": "10",
    "What is 3*3: A = 10 B = 12 C = 9 \n Answer the alphabet.": "c",
    "What is the sum of the multiple 6 between 100 to 1000": "83250",
    "What is a line segment which the end points both lie on a curve called?": "chord"
}

score = 0
for question in questions:
    response = input(question).lower().strip(" ,.?")

    if response == questions[question]:
        print("You got right.")
        score += 1

    else:
        print("You got wrong")



print("So, you got....")
time.sleep(3)
print(f"{score} out of {len(questions)}!!")
print(f"You got {(score/len(questions)) * 100}%!!")
