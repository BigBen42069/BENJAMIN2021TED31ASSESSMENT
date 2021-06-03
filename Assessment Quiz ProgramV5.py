# Assessment Quiz Program
# Benjamin Shortland

"""
This is my Quiz Program, where you have to answer Random triva question.
"""

# import libraries
from appJar import gui
import random
question_db = []
score = 0
quiz_progress = 0
value = 0
# class definitions
class Question:
   
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def check_correct(self, selected_answer):      
        global quiz_progress, score, value
        print(selected_answer)
        if selected_answer == question_db[quiz_progress].correct_answer:
            print("Correct")
            
        else:
            print("WRONG") 
            #print(question_db[quiz_progress].correct_answer)
            score += 1
            print(score)
            app.setLabel("score","Your final score is %s"%score)
        value += 14    
        quiz_progress += 1
        app.setMeter("progress", value , text=None)
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        i = 1
        for option in possible_answers:
            app.setButton(i,option)
            i+=1    
              
                        
    def get_answer_array(self):
        answer_array = self.answers
        answer_array.append(self.correct_answer)
        random.shuffle(answer_array)
        return self.answers
    #returns the answer text
    def get_question_text(self):
        return self.question
    
# Random Triva Questions that the user has to answer  
app = gui("Random Triva Questions", "800x420")
app.setBg("#9ba0a9")
app.setFont(18) 


# Press Function for my buttons on my gui           
def press(button):
    global score, quiz_progress
    if button == "Start Quiz":
        app.nextFrame("Questions")
        return
    elif button == "Quit":
        app.stop()
    elif button == "Close":
        app.stop()
    else:
        #print("quiz_progress = %d len(question_db = %d)"%(quiz_progress, len(question_db)))
        if quiz_progress < len(question_db)-1:
            #print() # want to put correct answer in here
            #print(button)            
            question_db[quiz_progress].check_correct(button)
            
        else:
            app.nextFrame("Questions")
            
            

            

# The Gui Class, where my questions and my Questions framestck are                                   s
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
            global score
            with app.frame("welcome"):
                app.addFlashLabel("title", "Answer Some Random Triva Questions!!")
                app.setFlashLabelBg("title", "#343c34")
                app.setFlashLabelFg("title", "#9ba0a9")
                app.addButton("Start Quiz", press)
                app.setButtonBg('Start Quiz',"#959c9a")
                app.addButton("Quit", press)
                app.setButtonBg('Quit',"#959c9a")                
                     
               
            with app.frame("triva"):
                
                
                app.addMeter("progress")
                app.setMeterFill("progress", "green") 
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
                app.addLabel("done","")
                app.setLabel("done","Well done")
                app.setLabelFg("done", "#9ba0a9")
                app.setLabelBg("done", "#343c34")                
                app.addButton("Close", press)
                app.setButtonBg("Quit","#959c9a")           
            app.firstFrame("Questions")  
        
                              
        # start the GUI
        self._app = app               
        
        app.go()                           
              
# Starts the GUI Class                    
quiz = Gui()




    





