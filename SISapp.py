from tkinter import *

from DashboardInterface import DashboardInterface
from StudentsInterface import StudentsInterface
from CoursesInterface import CoursesInterface

import SISdatabase


class SISApp:
    def __init__(self, frame):

        SISdatabase.data()

        self.frame = frame
        self.frame.title("Student Information System")
        self.frame.geometry("1350x700+0+0")
        self.frame.resizable(False, False)
        self.frame.iconbitmap(r"images\logo.ico")


        self.bg_frame = Frame(self.frame, bg="#030E3E")
        self.bg_frame.place(x=0, y=0, width=1370, height=706)

        self.nav_frame = Frame(self.bg_frame, bg="#030E3E")
        self.nav_frame.place(x=3, y=3, width=260, height=680)

        self.right_frame = Frame(self.bg_frame, bg="#F3CF04")
        self.right_frame.place(x=266, y=0, width=1200, height=706)

        self.SISlogopic = PhotoImage(file=r"images\sislabellogo.png").subsample(2, 2)
        self.icon_pic_lbl = Label(self.nav_frame, image=self.SISlogopic)
        self.icon_pic_lbl.photo = self.SISlogopic
        self.icon_pic_lbl.place(x=5, y=10, width=250, height=180)

        self.dashboard_img = PhotoImage(file=r"images\dashboard.png")
        self.student_img = PhotoImage(file=r"images\students.png")
        self.course_img = PhotoImage(file=r"images\courses.png")

        self.dashbrd_nav_button = Button(self.nav_frame,
                                         command=self.dashboard_frame_gui,
                                         relief=FLAT,
                                         activebackground="#030E3E",
                                         activeforeground="white",
                                         fg="#F3CF04",
                                         bg="#030E3E",
                                         image=self.dashboard_img,
                                         text="   Dashboard",
                                         font=("Hops And Barley c3 Bold", 17, "bold"),
                                         anchor="w",
                                         compound="left")
        self.dashbrd_nav_button.place(x=0, y=200, width=260, height=50)

        self.stud_nav_button = Button(self.nav_frame,
                                      command=self.student_frame_gui,
                                      relief=FLAT,
                                      activebackground="#030E3E",
                                      activeforeground="white",
                                      fg="#F3CF04",
                                      bg="#030E3E",
                                      image=self.student_img,
                                      text="   Students",
                                      font=("Hops And Barley c3 Bold", 17, "bold"),
                                      anchor="w",
                                      compound="left")
        self.stud_nav_button.place(x=0, y=250, width=260, height=50)

        self.course_nav_button = Button(self.nav_frame,
                                        command=self.courses_frame_gui,
                                        relief=FLAT,
                                        activebackground="#030E3E",
                                        activeforeground="white",
                                        fg="#F3CF04", bg="#030E3E",
                                        image=self.course_img,
                                        text="   Courses",
                                        font=("Hops And Barley c3 Bold", 17, "bold"),
                                        anchor="w",
                                        compound="left")
        self.course_nav_button.place(x=0, y=300, width=260, height=50)

        self.dashboard_cont_frame = Frame(self.right_frame,
                                          bg="white",
                                          highlightbackground="#030E3E",
                                          highlightthickness=5)

        self.student_cont_frame = Frame(self.right_frame,
                                        bg="white",
                                        highlightbackground="#030E3E",
                                        highlightthickness=5)

        self.courses_cont_frame = Frame(self.right_frame,
                                        bg="white",
                                        highlightbackground="#030E3E",
                                        highlightthickness=5)

        self.heading_label = Label(self.right_frame,
                                   text="",
                                   bg="#A51d23",
                                   fg="white",
                                   anchor="w",
                                   font=("Hops And Barley c3 Bold", 20, "bold"))

        self.heading_label.place(x=20, y=50, width=1045, height=50)

        self.dashboard_frame_gui()

    def hide_widgets(self):
        self.dashboard_cont_frame.place_forget()
        self.student_cont_frame.place_forget()
        self.courses_cont_frame.place_forget()


    def dashboard_frame_gui(self):
        self.heading_label.config(text="  DASHBOARD", fg="#F3CF04", bg="#030E3E")
        self.hide_widgets()
        self.dashboard_cont_frame.place(x=20, y=100, width=1045, height=570)
        DashboardInterface(self.dashboard_cont_frame)

    def student_frame_gui(self):
        self.heading_label.config(text="  STUDENTS", fg="#F3CF04", bg="#030E3E")
        self.hide_widgets()
        self.student_cont_frame.place(x=20, y=100, width=1045, height=570)
        StudentsInterface(self.student_cont_frame)

    def courses_frame_gui(self):
        self.heading_label.config(text="  COURSES", fg="#F3CF04", bg="#030E3E")
        self.hide_widgets()
        self.courses_cont_frame.place(x=20, y=100, width=1045, height=570)
        CoursesInterface(self.courses_cont_frame)

root = Tk()
ob = SISApp(root)
root.mainloop()
