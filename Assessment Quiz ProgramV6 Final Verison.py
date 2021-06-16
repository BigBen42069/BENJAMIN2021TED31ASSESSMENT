# Assessment Quiz Program (Random Triva Quiz)
# Benjamin Shortland
# 30/3/21 - 
"""
Here is my Quiz Program, where an user has four possible answers to choose from,
to answer a question prompt. There are so far seven questions the user has the
answer, however may add more if they wish too. 
"""

# import libraries
from appJar import gui
import random

# varibles
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
        
        if selected_answer == question_db[quiz_progress].correct_answer:
            app.setLabel("result","Correct") 
            score += 1
            
        else:
            #print("WRONG") 
            app.setLabel("result","Wrong") 
            #print(score)
            app.setLabel("score","Your final score is %s"%score + " out of 7")
             
        value += 14
        
        app.showButton("Next")
        
        
    def next_question(self):
        global quiz_progress
        quiz_progress += 1
        app.setMeter("progress", value , text=None)
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        i = 1
        for option in possible_answers:
            app.setButton(i,option)
            i+=1 
        app.hideButton("Next")
        app.setLabel("result","")
              
                        
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


# Press Function for my Buttons on my gui           
def press(button):
    #print("var button = %s"%button)
    #print("button_text = %s"%app.getButton(button))
    #print(question_db[quiz_progress].get_question_text())
    #print(question_db[quiz_progress].get_answer_array())
    #print(question_db[quiz_progress].correct_answer)

    global score, quiz_progress
    # Starts the Quiz
    if button == "Start Quiz": 
        app.nextFrame("Questions")
        return
    # Quits the Quiz
    elif button == "Quit":
        app.stop()
    # Closes the Quiz
    elif button == "Close":
        app.stop()
    else:
        #print("quiz_progress = %d len(question_db = %d)"%(quiz_progress, len(question_db)))
        if quiz_progress < len(question_db)-1: # remoemeber -1 was here
            #print() # want to put correct answer in here
            #print(button)            
            question_db[quiz_progress].check_correct(app.getButton(button))
            
            
        else:
            app.nextFrame("Questions")
            
            

            

# The Gui Class, where my questions are layed out and my Questions framestacks are                                   s
class Gui:
    def __init__(self):
        
        # My Questions That The User Has to Answer
        question_db.append(Question('What is the rarest M&M Colour?', ['Blue','Red','Green'],'Brown'))
        question_db.append(Question('Which country consumes the most chocolate per capita?', ['Uzbekistan','Australia','Brazil'],'Switzerland'))
        question_db.append(Question('How many ribs are in a human body?', ['31','27','22'],'24',))
        question_db.append(Question('What is the world’s biggest island??', ['Jamaica','Philppines','New Zealand'],'Greenland',))
        question_db.append(Question('Which planet is the hottest in the solar system?', ['Mercury','Mars','Pluto'],'Venus'))
        question_db.append(Question('Which chess piece can only move diagonally?', ['Knight','Rook','King'],'A Bishop'))
        question_db.append(Question('What US president put a Twinkie in the country’s millennium time capsule?', ['Ronald Reagan','George W. Bush','Frankln D.Roosevelt'],'Bill Clinton'))
               
       
        with app.frameStack("Questions"):
            
            with app.frame("welcome"):
                # The "Start Quiz" Frame
                app.addFlashLabel("title", "Answer Some Random Triva Questions!!")
                app.setFlashLabelBg("title", "#343c34")
                app.setFlashLabelFg("title", "#9ba0a9")
                app.addButton("Start Quiz", press)
                app.setButtonBg('Start Quiz',"#959c9a")
                app.addButton("Quit", press)
                app.setButtonBg('Quit',"#959c9a")                
                     
               
            with app.frame("triva"):
                # The "Questions" Frame
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
                app.addLabel("result","")
                app.setLabelBg("result", "#343c34")
                app.addButton("Next", question_db[quiz_progress].next_question)
                app.setButtonBg('Next',"#343c34")
                app.hideButton("Next")
                    
            with app.frame("ending"):
                # The "Ending" frame
                app.addLabel("score","")
                app.setLabel("score","Your final score is %s"%score + "Out of 7")
                app.setLabelFg("score", "#9ba0a9")
                app.setLabelBg("score", "#343c34")   
                app.addFlashLabel("done", "Well Done")                              
                app.addButton("Close", press)
                app.setButtonBg("Close","#959c9a")
                app.setButtonBg("Quit","#959c9a")           
            app.firstFrame("Questions")  
        
                              
        # Starts My Random Triva Questions GUI
        self._app = app               
        
        app.go()                           
              
# Starts My Random Triva Questions GUI Class                    
quiz = Gui()




    





