import customtkinter
from tkinter import ttk
import numpy as np
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1000x500")


#root.config(bg='#242424')
root.title("Gigachads")

#Function to change the theme of the window
def change_appearance_mode(new_appearance:str):
    customtkinter.set_appearance_mode(new_appearance)
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, values=["Light", "Dark", "System"],command= change_appearance_mode)
appearance_mode_optionemenu.grid(row=9, column=12, padx=20, pady=(10, 10))

#Function to change the size of the window
def change_Scalling(new_Scalling:str):
    new_Scalling_float=int(new_Scalling.replace("%",""))/100
    customtkinter.set_widget_scaling(new_Scalling_float)

scaling_optionemenu = customtkinter.CTkOptionMenu(root, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=change_Scalling)
scaling_optionemenu.grid(row=11, column=12, padx=20, pady=(10, 20))



#Global Frame for first page
frame = None
frame1 = None
frame3 = None
frame4 = None
frame5 = None
second_frame = None
frame = None
menu_frame = None
about_frame = None
help_frame = None
def menu():
    global menu_frame
    if about_frame!=None:
        about_frame.grid_forget()
    if help_frame!=None:
        help_frame.grid_forget()
    if frame != None:
        frame.grid_forget()
        frame1.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()

    if menu_frame!=None:
        menu_frame.grid_forget()
    menu_frame = customtkinter.CTkFrame(master=root)

    menu_frame.grid(row=0, column=0, columnspan=1, rowspan=4, pady=20, padx=10)
    button1 = customtkinter.CTkButton(master=menu_frame, text="Free Test", command=secondPage)
    button1.grid(row=0, column=0, pady=12, padx=10)
    button2 = customtkinter.CTkButton(master=menu_frame, text="Premium Test", command=secondPage)
    button2.grid(row=1, column=0, pady=12, padx=10)
    button3 = customtkinter.CTkButton(master=menu_frame, text="About Us", command=about)
    button3.grid(row=2, column=0, pady=12, padx=10)
    button4 = customtkinter.CTkButton(master=menu_frame, text="Help", command=help)
    button4.grid(row=3, column=0, pady=12, padx=10)
    button5 = customtkinter.CTkButton(master=menu_frame, text="Go Back", command=firsPage)
    button5.grid(row=4, column=0, pady=12, padx=10)

def firsPage():
    global frame
    global frame1
    global frame3
    global frame4
    global frame5

    if frame1 !=None:
        frame.grid_forget()
        frame1.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()



    if menu_frame != None:
        menu_frame.grid_forget()
    if second_frame != None:
        second_frame.grid_forget()
    if help_frame!=None:
        help_frame.grid_forget()


    #3rd Frame
    frame = customtkinter.CTkFrame(master=root)
    frame.grid(row = 0, column = 0, rowspan=1, columnspan=1, pady=10, padx=10)
    #pics

    #Label 1
    label1 = customtkinter.CTkLabel(master=frame)
    label1.grid(row=0, column=0,columnspan=1,rowspan=1, pady=2, padx=1)

    first_text1 = customtkinter.CTkLabel(master=frame, text="What Is Atherosclerosis?", wraplength=350)
    first_text1.grid(row=0, column=0, rowspan=1, columnspan=5, pady=10, padx=10)
    first_text2 = customtkinter.CTkLabel(master=frame,
                                                     text="Atherosclerosis is a common condition that develops when a sticky substance called plaque builds up inside your\n"
                                                          "arteries. Disease linked to atherosclerosis is the leading cause of death in the United States. About half of Americans\n"
                                                          "between ages 45 and 84 have atherosclerosis and don’t know it.",
                                                     wraplength=350)
    first_text2.grid(row=1, column=0, rowspan=2, columnspan=3, pady=10, padx=10)
    #2nd Frame
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.grid(row = 0, column = 5, rowspan=4, columnspan=4, pady=10, padx=10)

    first_text4 = customtkinter.CTkLabel(master=frame1, text="What causes atherosclerosis?", wraplength=350)
    first_text4.grid(row = 0, column = 1,rowspan = 1,columnspan = 5,pady=10,padx=10)
    first_text3 = customtkinter.CTkLabel(master=frame1,
                                         text="It's not clear exactly how atherosclerosis starts or what causes it. However, a "
                                              "gradual buildup of plaque or thickening due to inflammation occurs on the inside"
                                              " of the walls of the artery. This reduces blood flow and oxygen supply to the vital"
                                              " body organs and extremities.",
                                         wraplength=350)
    first_text3.grid(row = 1, column = 1,rowspan = 1,columnspan = 5,pady=10,padx=10)

#3rd Frame
    frame3 = customtkinter.CTkFrame(master=root)
    frame3.grid(row=5, column=0, rowspan=5, columnspan=4, pady=10, padx=10)

    first_text6 = customtkinter.CTkLabel(master=frame3, text="What are the symptoms?", wraplength=350)
    first_text6.grid(row=0, column=4, rowspan=1, columnspan=5, pady=10, padx=10)
    first_text7 = customtkinter.CTkLabel(master=frame3,
                                         text="It's not clear exactly how atherosclerosis starts or what causes it. However, a "
                                              "gradual buildup of plaque or thickening due to inflammation occurs on the inside"
                                              " of the walls of the artery. This reduces blood flow and oxygen supply to the vital"
                                              " body organs and extremities.",
                                         wraplength=350)

    first_text7.grid(row=1, column=4, rowspan=1, columnspan=5, pady=10, padx=10)

    #4th Frame
    frame4 = customtkinter.CTkFrame(master=root)
    frame4.grid(row=5, column=5, rowspan=5, columnspan=4, pady=10, padx=10)

    first_text8 = customtkinter.CTkLabel(master=frame4, text="What are the risk factors for atherosclerosis?", wraplength=350)
    first_text8.grid(row=0, column=2, rowspan=1, columnspan=5, pady=10, padx=10)
    first_text9 = customtkinter.CTkLabel(master=frame4,
                                         text="Risk factors for atherosclerosis, include:\n"
                                              "body organs and extremities.\n"
                                              "High blood pressure.\n"
                                              "Smoking\n"
                                              "Type 1 diabetes\n"
                                              "Obesity\n"
                                              "Physical inactivity\n"
                                              "High saturated fat diet",
                                         wraplength=350)

    first_text9.grid(row = 5, column=4, rowspan=1, columnspan=5, pady=10, padx=10)

    # 5th Frame
    frame5 = customtkinter.CTkFrame(master=root)
    frame5.grid(row=12, column=3, rowspan=2, columnspan=4, pady=10, padx=10)

    button = customtkinter.CTkButton(master=frame5, text="Find Out the risk", command=menu)
    button.grid(row=6, column=1, pady=12, padx=10)

def secondPage():
    global frame
    if about_frame!=None:
        about_frame.grid_forget()
    if frame != None:
        frame.grid_forget()
        frame1.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()
    if second_frame!=None:
        second_frame.grid_forget()

    frame = customtkinter.CTkFrame(master=root)
    frame.grid(row = 0, column = 2, columnspan=1, rowspan=4, pady=20, padx=10)
    # body mass index label
    label1 = customtkinter.CTkLabel(master=frame, text="Body mass index")
    label1.grid(row=0, column=0, pady=20, padx=10)
    # body mass index entry
    float_bmiarray = [round(x / 10, 1) for x in range(0, 1500)]
    comboboxbmi = ttk.Combobox(master=frame, values=list(float_bmiarray))
    comboboxbmi.grid(row=0, column=1, padx=12, pady=10)

    # Age label
    label2 = customtkinter.CTkLabel(master=frame, text="Age")
    label2.grid(row=1, column=0, pady=12, padx=10)
    # Age entry
    int_array = np.arange(0, 150, 1)
    comboboxage = ttk.Combobox(master=frame, values=list(int_array))
    comboboxage.grid(row=1, column=1, padx=12, pady=10)

    # Gender label
    label3 = customtkinter.CTkLabel(master=frame, text="Gender")
    label3.grid(row=2, column=0, pady=12, padx=10)
    # gender Combobox
    genderValue = ["Male", "Female", "Other"]
    combobox1 = ttk.Combobox(master=frame, values=genderValue)
    combobox1.grid(row=2, column=1, padx=12, pady=10)

    label4 = customtkinter.CTkLabel(master=frame, text="Smoking Status")
    label4.grid(row=3, column=0, pady=12, padx=10)

    smokerValue = ["Current Smoker", "Former Smoker", "Never Smoked"]
    combobox2 = ttk.Combobox(master=frame, values=smokerValue)
    combobox2.grid(row=3, column=1, padx=12, pady=10)

    # blood Pressure label
    label5 = customtkinter.CTkLabel(master=frame, text="Blood Pressure(low,high)")
    label5.grid(row=4, column=0, pady=12, padx=10)

    # combobox
    int_bP1 = np.arange(0, 150, 1)
    comboboxbp1 = ttk.Combobox(master=frame, values=list(int_bP1))
    comboboxbp1.grid(row=4, column=1, padx=12, pady=10)
    int_bP2 = np.arange(0, 150, 1)
    comboboxbp2 = ttk.Combobox(master=frame, values=list(int_bP2))
    comboboxbp2.grid(row=4, column=2, padx=12, pady=10)

    button1 = customtkinter.CTkButton(master=frame, text="Analyze", command=analyze)
    button1.grid(row=5, column=1, pady=12, padx=10)
    button2 = customtkinter.CTkButton(master=frame, text="Go Back", command= menu)
    button2.grid(row=5, column=2, pady=12, padx=10)

def analyze():
    # hide the old widgets
    if about_frame!=None:
        about_frame.grid_forget()
    if help_frame != None:
        help_frame.grid_forget()
    if frame1 != None:
        frame.grid_forget()
        frame1.grid_forget()
        frame3.grid_forget()
        frame4.grid_forget()
        frame5.grid_forget()
    # create new widgets
    global second_frame
    second_frame = customtkinter.CTkFrame(master=root)
    second_frame.grid(row = 0, column = 0,pady=20,padx=10)
    new_label1 = customtkinter.CTkLabel(master=second_frame,text="The percentage of You getting the diesease is\n\n\n\n\n   ")
    new_label1.grid(row = 0, column = 1,pady=20,padx=10)
    new_label2 = customtkinter.CTkLabel(master=second_frame,text="This analysis is based on limited information click on the button given below to find out\nmore accurate risk of genetic factor")
    new_label2.grid(row = 1, column = 1,pady=20,padx=10)

    button1 = customtkinter.CTkButton(master=second_frame, text="Risk Factor based on Genome Analysis")
    button1.grid(row=2, column=1, pady=20, padx=10)
    button2 = customtkinter.CTkButton(master=second_frame, text="Go Back",command=secondPage)
    button2.grid(row=3, column=1, pady=20, padx=10)

def about():
    global about_frame
    if frame!=None:
        frame.grid_forget()

    if about_frame!=None:
        about_frame.grid_forget()
    if help_frame!=None:
        help_frame.grid_forget()

    about_frame = customtkinter.CTkFrame(master=root)
    about_frame.grid(row=0, column=2, columnspan=5, rowspan=5, pady=20, padx=10)
    aboutfirst_text1 = customtkinter.CTkLabel(master=about_frame, text="Our Team ", wraplength=350)
    aboutfirst_text1.grid(row = 0, column = 4 ,pady=5,padx=5)
    aboutfirst_text2 = customtkinter.CTkLabel(master=about_frame, text="Benefits:\n"
"Team has experience in various fields (ML, AI, bioinformatics, molecular biology, medicine etc.)\n"

"Extensive background in medicine and health-related sciences\n\n\n\n\n\n" , wraplength=350)
    aboutfirst_text2.grid(row =5 , column =4  ,pady=5,padx=5)
    aboutfirst_text3 = customtkinter.CTkLabel(master=about_frame, text="Team Lead:Ilya \n"
                                                                       "Bioinformatician: Daria\n"
                                                                       "Software engineer: Asif\n"
                                                                       "Programmer: Zain\n"
                                                                       "Data Scientist: Hamna\n" , wraplength=350)
    aboutfirst_text3.grid(row = 1, column = 4 ,pady=5,padx=5)
    button2 = customtkinter.CTkButton(master=about_frame, text="Go Back", command= menu)
    button2.grid(row=6, column=4, pady=10, padx=5)

def help():
    global help_frame
    if frame!=None:
        frame.grid_forget()

    if help_frame!=None:
        help_frame.grid_forget()
    if about_frame!=None:
        about_frame.grid_forget()

    help_frame = customtkinter.CTkFrame(master=root)
    help_frame.grid(row=0, column=2, columnspan=5, rowspan=5, pady=20, padx=10)
    helpfirst_text1 = customtkinter.CTkLabel(master=help_frame, text="Contact us for help at  ", wraplength=350)
    helpfirst_text1.grid(row = 0, column = 4 ,pady=5,padx=5)

    button2 = customtkinter.CTkButton(master=help_frame, text="Go Back", command= menu)
    button2.grid(row=6, column=4, pady=10, padx=5)


if __name__ == "__main__":

    firsPage()
    root.mainloop()

