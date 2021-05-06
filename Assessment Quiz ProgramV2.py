# Assessment Quiz Program
# Benjamin Shortland

"""
This is my Quiz Program, where you have to answer Random triva question.
"""

# import libraries
from appJar import gui

# variables
question_db = []
score = 0
quiz_progress = 0

# class definitions
class Question:
   
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
   
    # returns True if correct answer is selected
    def check_correct(self, selected_answer):
        global quiz_progress
        print(selected_answer)
        if selected_answer == question_db[quiz_progress].correct_answer:
            print("Correct")
        else:
            print("INCORRECT")
        quiz_progress += 1
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        i = 1
        for option in possible_answers:
            app.setButton(i,option)
            i+=1        
    # returns array of all possible answers
    # returns array of all possible answers
    def get_answer_array(self):
        answer_array = self.answers
        answer_array.append(self.correct_answer)
        return self.answers
    #returns the answer text
    def get_question_text(self):
        return self.question
 
# Random Triva Questions that the user has to answer   
question_db.append(Question('What is the rarest M&M Colour?', ['Blue','Red','Green'],'Brown'))
question_db.append(Question('Which country consumes the most chocolate per capita?', ['Uzbekistan','Australia','Brazil'],'Switzerland'))
question_db.append(Question('How many ribs are in a human body?', ['31','27','22'],'24'))
question_db.append(Question('What is the world’s biggest island??', ['Jamaica','Philppines','New Zealand'],'Greenland'))
question_db.append(Question('Which planet is the hottest in the solar system?', ['Mercury','Mars','Pluto'],'Venus'))
question_db.append(Question('Which chess piece can only move diagonally?', ['Knight','Rook','King'],'A Bishop'))
question_db.append(Question('What US president put a Twinkie in the country’s millennium time capsule?', ['Ronald Reagan','Abraham Lincoln','Frankln D.Roosevelt'],'Bill Clinton'))

# create a GUI variable called app for my program
app = gui("Quiz Window", "400x200")
app.setBg("pink")
app.setFont(18)

def press(button):
    if button == "Start Quiz":
        app.hideFrame("welcome")
        app.showFrame("question")
    
       
       
# My Frames For My Gui
with app.frame("welcome"):
    app.addLabel("title", "Welcome to quiz")
    app.setLabelBg("title", "green")
    app.setLabelFg("title", "lime")
    app.addButton("Start Quiz", press)

with app.frame("question"):
    app.addLabel("question_label", "")
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.addButton(1,press)
    app.addButton(2,press)
    app.addButton(3,press)
    app.addButton(4,press)
    app.addButton(5,press)
    app.addButton(6,press)
    app.addButton(7,press)
    possible_answers = question_db[quiz_progress].get_answer_array()
    i = 1
    for option in possible_answers:
        app.setButton(i,option)
        i+=1
    



# start the GUI
app.go()


