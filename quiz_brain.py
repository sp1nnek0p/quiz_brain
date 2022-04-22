from html import unescape

class QuizBrain:
  def __init__(self, questions_list: list) -> None:
    self.question_number = 0
    self.score = 0
    self.questions_list = questions_list


  def still_has_questions(self) -> bool:
    return self.question_number != len(self.questions_list)


  def next_question(self):
    """
    Takes no Parameters
    Function to ask the current question and go to the next one when done
    Function Outputs to User Directly
    """
    keys = {'1': 0, '2': 1, '3': 2, '4': 3}
    current_question = self.questions_list[self.question_number]
    self.question_number += 1
    print(f"Q-{self.question_number}: {unescape(current_question.question)} ?: ")
    print(f"| 1. {unescape(current_question.posible_answers[0])}")
    print(f"| 2. {unescape(current_question.posible_answers[1])}")
    print(f"| 3. {unescape(current_question.posible_answers[2])}")
    print(f"| 4. {unescape(current_question.posible_answers[3])}")
    user_answer = input("Choose your answer 1, 2, 3 or 4 : ")    

    self.__check_answer(current_question.posible_answers[keys[user_answer.lower()]], current_question.answer)


  def __check_answer(self, user_answer, current_question_answer):
    if (user_answer.lower() == current_question_answer.lower()):
      print(f"You answered {unescape(user_answer)}, that was right!")
      self.score += 1
    else:
      print(f"You answered {unescape(user_answer)}, that was incorect")
    print(f"The correct answer is {unescape(current_question_answer)}")
    print(f"Your score is : {self.score}/{len(self.questions_list)}\n")