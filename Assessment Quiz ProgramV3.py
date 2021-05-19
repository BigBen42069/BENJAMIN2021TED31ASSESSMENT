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

    def check_correct(self, selected_answer):      
        global quiz_progress
        global score
        print(selected_answer)
        if selected_answer == question_db[quiz_progress].correct_answer:
            print("Correct")
            score += 1
        else:
            print("WRONG")
            
        quiz_progress += 1
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        i = 1
        for option in possible_answers:
            app.setButton(i,option)
            i+=1    
              
                        
    def get_answer_array(self):
        answer_array = self.answers
        answer_array.append(self.correct_answer)
        return self.answers
    #returns the answer text
    def get_question_text(self):
        return self.question
    
# Random Triva Questions that the user has to answer  
app = gui("Random Triva Questions", "800x420")
app.setBg("#9ba0a9")
app.setFont(18)           

           
def press(button):
    global score, quiz_progress
    if button == "Start Quiz":
        app.nextFrame("Questions")
        return
                   
    else:
        print("quiz_progress = %d len(question_db = %d)"%(quiz_progress, len(question_db)))
        if quiz_progress < len(question_db)-1:
            question_db[quiz_progress].check_correct(button) 
        else:
            app.nextFrame("Questions")
    
                                   
class Gui:
    def __init__(self):
        
        
        question_db.append(Question('What is the rarest M&M Colour?', ['Blue','Red','Green'],'Brown'))
        question_db.append(Question('Which country consumes the most chocolate per capita?', ['Uzbekistan','Australia','Brazil'],'Switzerland'))
        question_db.append(Question('How many ribs are in a human body?', ['31','27','22'],'24',))
        question_db.append(Question('What is the world’s biggest island??', ['Jamaica','Philppines','New Zealand'],'Greenland',))
        question_db.append(Question('Which planet is the hottest in the solar system?', ['Mercury','Mars','Pluto'],'Venus'))
        question_db.append(Question('Which chess piece can only move diagonally?', ['Knight','Rook','King'],'A Bishop'))
        question_db.append(Question('What US president put a Twinkie in the country’s millennium time capsule?', ['Ronald Reagan','Abraham Lincoln','Frankln D.Roosevelt'],'Bill Clinton'))
                 
        
       
        with app.frameStack("Questions"):
            
            with app.frame("welcome"):
                app.addLabel("title", "Welcome to quiz")
                app.setLabelBg("title", "#343c34")
                app.setLabelFg("title", "#9ba0a9")
                app.addButton("Start Quiz", press)
                app.setButtonBg('Start Quiz',"#d9d9d9")
               
            with app.frame("triva"):
                app.addLabel("question_label", "")
                app.setLabel("question_label",question_db[quiz_progress].get_question_text())
                app.setLabelFg("question_label", "#9ba0a9")
                app.setLabelBg("question_label", "#343c34")
                app.addButton(1,press)
                app.setButtonBg(1,"#959c9a")
                app.addButton(2,press)
                app.setButtonBg(2,"#959c9a")
                app.addButton(3,press)
                app.setButtonBg(3,"#959c9a")
                app.addButton(4,press)
                app.setButtonBg(4,"#959c9a")           
                possible_answers = question_db[quiz_progress].get_answer_array()
                i = 1
                for option in possible_answers:
                    app.setButton(i,option)
                    i+=1 
               
            with app.frame("ending"):
                
                app.addLabel("score","")
                app.setLabel("score","Your final score is %s"%score)
                app.setLabelFg("score", "#9ba0a9")
                app.setLabelBg("score", "#343c34")                
            
            app.firstFrame("Questions")  
        
                              
        # start the GUI
        self._app = app               
        
        app.go()                           
              
                    
quiz = Gui()




    





