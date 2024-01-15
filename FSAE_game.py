# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:56:41 2023

@author: Jubair Ali
"""

import tkinter as tk
from FSAE_QGen import FSAE_QGen


"""
Constants
"""

NEXT_QUEST_STR = "Next Question"
SHOW_ANS_STR = "Show Answer"


"""
Open a new window and start the quiz
"""
def start_Quiz(fName,numQ):

    try:
        new_Quiz = FSAE_QGen(fName)
    except:
        tk.messagebox.showerror("File Error",fName +" could not be opened")
        return(-1)

    #creation of the quiz window
    main = tk.Tk()
    main.title("FSAE Quiz")
    tkimg = None

    #label that holds question number
    global quest_num
    quest_num = 1
    title_string = tk.StringVar(main)
    title_string.set("Question 1")
    top_frame = tk.Frame(main)
    top_label = tk.Label(top_frame,textvariable = title_string)
    top_frame.pack(pady=(10,0))
    top_label.pack()

    #Label that holds the image of question
    que_frame = tk.Frame(main,padx = 7, pady=7)
    quest_label = tk.Label(que_frame)

    que_frame.pack()
    quest_label.pack()


    #Label to show answer
    answer = ""
    answer_text = tk.StringVar(main)
    ans_frame = tk.Frame(main,padx = 7, pady=7)
    ans_label = tk.Label(ans_frame, textvariable = answer_text)
    ans_label.pack()
    ans_frame.pack()

    #button callback function
    def button_action():
        global quest_num
        title_string.set("Question "+ str(quest_num))

        if button_text.get() == NEXT_QUEST_STR:

            quiz_question = new_Quiz.get_question()
            global tkimg
            tkimg = tk.PhotoImage(data = quiz_question[0],master = main)
            quest_label.configure(image = tkimg)

            button_text.set(SHOW_ANS_STR)
            answer_text.set("")
            global answer
            answer = quiz_question[1]


        elif button_text.get() == SHOW_ANS_STR:

            button_text.set(NEXT_QUEST_STR)
            answer_text.set(answer)
            ans_label.config(font=("Helvetica bold",16))

            quest_num = quest_num + 1

            if quest_num > numQ:
                button_text.set("Exit")

        else:
            main.destroy()





    #button to see answers

    button_text = tk.StringVar(main)
    button_text.set(NEXT_QUEST_STR)
    button = tk.Button(main,bd = 3, width= 12, textvariable=button_text, \
                        command = button_action)
    button.pack()

    button.invoke()


    main.mainloop()








#=============================================================
"""
Program starts here
"""
startText = """
            To begin quiz, enter the name of the pdf containing
            the FSAE rules below. Then select the number of questions
            to generate and click start.
            """

#setting up our main window
root = tk.Tk()
root.title("FSAE Quiz Generator")
root.geometry("400x200")
root.resizable(False,False)

fileName = tk.StringVar()
fileName.set("FSAE_Rules.pdf")

#numQ holds the number of questions to make
numQ = tk.IntVar()
numQ.set(10)

tk.Label(root, text = startText).pack()

entry = tk.Entry(root,textvariable= fileName,width = 40).pack()

radioFrame =tk.Frame(root,pady=7)
radioFrame.pack()
tk.Label(radioFrame,text="No. Questions:").pack(anchor=tk.N)
r1 = tk.Radiobutton(radioFrame, text="10", variable=numQ, value=10,padx=5).pack(side="left")
r2 = tk.Radiobutton(radioFrame, text="20", variable=numQ, value=20,padx=5).pack(side="left")
r3 = tk.Radiobutton(radioFrame, text="50", variable=numQ, value=50,padx=5).pack(side="left")

buttonFrame = tk.Frame(root,pady=7)
buttonFrame.pack(side="bottom")
button = tk.Button(buttonFrame,text = "Start",bd=3,width=12,command = lambda: start_Quiz(fileName.get(),numQ.get()))
button.pack()

root.mainloop()

