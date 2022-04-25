# CLI Quiz Game in Python

#### Demonstarting Some Simple OOP

Gets data from the Open Trivia Database API and creates a multiple choice quiz. 
The user must then choose between the 1 to 4 possible answers,
if the user answers correctly the score is incremented by 1 out of the total number of questions.

If the user answers incorrectly a message along with the correct answer is displayed.

When the user finishes all the questions the total score out of total number of questions is displayed.

This was just meant to demonstate some object orientated porgramming in action.

> Question_model.py
>
> - This is a basic object that takes to Properties
>   - Question and Answer

> Quiz_brain.py
>
> - Has 3 Properties and 2 Public Methods and 1 Private method
>   - Public Method - still_has_questions -> bool
>   - Public Method - next_question -> void
>   - Private Method - check_answer ->void

> data.py
>
> - Contains 1 list, containing all the questions and answers in Dictionaries

> main.py
>
> - Main Quiz game loop
