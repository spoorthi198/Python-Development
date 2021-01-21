class QuizBrain:
    def __init__(self, que_list):
        self.question_number = 0
        self.question_list = que_list
        self.score = 0
    def still_has_ques(self):
        return self.question_number < len(self.question_list)

    def next_ques(self):
        current_question=self.question_list[self.question_number]
        self.question_number +=1
        user_answer=input(f" Q . {self.question_number} {current_question.text}:(True/False?)")
        self.check_answer(user_answer,current_question.answer)


    def check_answer(self,u_ans,c_ans):
        if u_ans.lower() == c_ans.lower():
            self.score +=1
            print(f"you got it right!😊 ")
        else:
            self.score
            print(f"you are wrong ")
        print(f"correct answer was {c_ans}")
        print(f"your score is {self.score}/{self.question_number}")
        return self.score,self.question_number

