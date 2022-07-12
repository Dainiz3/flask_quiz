from flask import Flask, render_template, request

app = Flask(__name__)

class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correct_option = -1

    def __init__(self, q_id, question, option1, option2, option3, correct_option):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correct_option = correct_option

    def get_correct_option(self):
        if self.correct_option == 1:
            return self.option1
        elif self.correct_option == 2:
            return self.option2
        elif self.correct_option == 3:
            return self.option3
        
q1 = Question(1, "Why are you doing this test?", "Because we were forced to", "Because we have so much fun", "Because we have nothing to do", 1)
q2 = Question(2, "Who do you think created this test?", "Alliens", "Teachers (Mindaugas and Vytautas)", "Dainius mldc", 3)
q3 = Question(3, "Which teacher is the best?", "Mindaugas", "Vytautas", "Both options mentioned above", 3)
q4 = Question(4, "Will the teachers grade this work more than 8?", "Yes", "No", "We will see", 3)

questions_list = [q1, q2, q3, q4]

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions_list = questions_list)

@app.route("/submitquiz", methods=["POST", "GET"])
def submit():
    correct_count=0
    for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count = correct_count +1
    correct_count = str(correct_count)
    return render_template("quizend.html", correct_count = correct_count, correct_option = correct_option)


if __name__ == "__main__":
    app.run(debug=True)
