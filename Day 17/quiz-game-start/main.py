from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank =[]
for que in question_data:
    que_text = que["text"]
    que_answer=que["answer"]
    new_que= Question(que_text,que_answer)
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_ques()


print("you completed quiz")
print(f"final score id {quiz.score} / {quiz.question_number}")