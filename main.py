from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from html import unescape
import random

# TODO: Get this to work with the online trivia DB
# Loop trought the question data and create a Question Object
# and append the Question Object to a new array called
# question_bank
question_bank = []
for i in question_data:
  incorect_answers = i['incorrect_answers']
  incorect_answers.append(i['correct_answer'])
  random.shuffle(incorect_answers)
  question_bank.append(Question(i['question'], incorect_answers , i['correct_answer']))

# Init a QuizBrain Object and pass in the question_bank array
quiz = QuizBrain(question_bank)

# Main game loop
while quiz.still_has_questions():
  quiz.next_question()

print("You have completed the quiz")
print(f"Your Final score was {quiz.score}/{len(quiz.questions_list)}")

# ------------------------------------------
# print(len(question_bank))
# random_question_object = random.choice(question_bank)
# question_bank.remove(random_question_object)
# print(random_question_object.question, 'answer', random_question_object.answer)
# print(len(question_bank))
# ("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")