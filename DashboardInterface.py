from tkinter import *
from tkinter import ttk

import displaytable as disp
import SISdatabase


class DashboardInterface:
    def __init__(self, frame):
        self.dashboard_cont_frame = frame

        self.bg_frame = Frame(self.dashboard_cont_frame, bg="white")

        self.student_dshbrd_img = PhotoImage(file=r"images\dashboardstud.png")
        self.course_dshbrd_img = PhotoImage(file=r"images\dashboardcourse.png")

        self.student_count_dash = Label(self.dashboard_cont_frame, image=self.student_dshbrd_img)
        self.student_count_dash.photo = self.student_dshbrd_img
        self.student_count_dash.place(x=250, y=19, width=250, height=152)

        self.student_count = Label(self.dashboard_cont_frame,
                                   text="1000",
                                   font=("Hops And Barley c3 Bold", 40, "bold"),
                                   fg="#030E3E",
                                   bg="#F3CF04")
        self.student_count.place(x=307, y=20, width=140, height=77)

        self.course_count_dash = Label(self.dashboard_cont_frame, image=self.course_dshbrd_img)
        self.course_count_dash.photo = self.course_dshbrd_img
        self.course_count_dash.place(x=540, y=19, width=250, height=152)

        self.course_count = Label(self.dashboard_cont_frame,
                                  text="0",
                                  font=("Hops And Barley c3 Bold", 40, "bold"),
                                  bg="#030E3E",
                                  fg="#F3CF04")
        self.course_count.place(x=597, y=20, width=140, height=77)

        self.stud_list_label = Label(self.dashboard_cont_frame,
                                     fg="#F3CF04",
                                     bg="#030E3E",
                                     text=" LIST OF STUDENTS",
                                     font=("Hops And Barley c3 Bold", 15, "bold"),
                                     anchor="w")

        self.stud_list_frame = Frame(self.dashboard_cont_frame,
                                     bg="white",
                                     highlightbackground="#030E3E",
                                     highlightthickness=3)

        self.course_label = Label(self.dashboard_cont_frame,
                                  fg="#F3CF04",
                                  bg="#030E3E",
                                  text=" LIST OF COURSES",
                                  font=("Hops And Barley c3 Bold", 15, "bold"),
                                  anchor="w")
        self.course_list_frame = Frame(self.dashboard_cont_frame,
                                       bg="white",
                                       highlightbackground="#030E3E",
                                       highlightthickness=3)

        scroll_x_stud_list = Scrollbar(self.stud_list_frame, orient=HORIZONTAL)
        scroll_y_stud_list = Scrollbar(self.stud_list_frame, orient=VERTICAL)

        scroll_x_course_list = Scrollbar(self.course_list_frame, orient=HORIZONTAL)
        scroll_y_course_list = Scrollbar(self.course_list_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(self.stud_list_frame,
                                          xscrollcommand=scroll_x_stud_list.set,
                                          yscrollcommand=scroll_y_stud_list.set,
                                          columns=("id_no", "name", "course_code", "year", "gender"))

        scroll_x_stud_list.pack(side=BOTTOM, fill=X)
        scroll_y_stud_list.pack(side=RIGHT, fill=Y)

        scroll_x_stud_list.config(command=self.student_table.xview)
        scroll_y_stud_list.config(command=self.student_table.yview)

        self.student_table.heading("id_no", text="ID Number")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course_code", text="Course Code")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table['show'] = 'headings'
        self.student_table.column("id_no", width=70)
        self.student_table.column("name", width=190)
        self.student_table.column("course_code", width=100)
        self.student_table.column("year", width=70)
        self.student_table.column("gender", width=70)

        self.student_table.pack(fill=BOTH, expand=1)

        self.course_table = ttk.Treeview(self.course_list_frame,
                                         xscrollcommand=scroll_x_course_list.set,
                                         yscrollcommand=scroll_y_course_list.set,
                                         columns=("course_code", "course"))

        scroll_x_course_list.pack(side=BOTTOM, fill=X)
        scroll_y_course_list.pack(side=RIGHT, fill=Y)

        scroll_x_course_list.config(command=self.course_table.xview)
        scroll_y_course_list.config(command=self.course_table.yview)

        self.course_table.heading("course_code", text="Course Code")
        self.course_table.heading("course", text="Course")
        self.course_table['show'] = 'headings'
        self.course_table.column("course_code", width=50)
        self.course_table.column("course", width=200)

        self.course_table.pack(fill=BOTH, expand=1)

        self.max_student_img = PhotoImage(file=r"images\max.png").subsample(5, 5)
        self.max_course_img = PhotoImage(file=r"images\max.png").subsample(5, 5)

        self.max_student_button = Button(self.dashboard_cont_frame,
                                         command=self.max_student_table,
                                         relief=FLAT,
                                         bg="#030E3E",
                                         activebackground="#030E3E",
                                         image=self.max_student_img)
        self.max_course_button = Button(self.dashboard_cont_frame,
                                        command=self.max_course_table,
                                        relief=FLAT,
                                        bg="#030E3E",
                                        activebackground="#030E3E",
                                        image=self.max_course_img)

        self.min_image = PhotoImage(file=r"images\min.png").subsample(5, 5)

        self.min_button = Button(self.dashboard_cont_frame,
                                 command=self.default_layout,
                                 relief=FLAT,
                                 fg="white",
                                 bg="#030E3E",
                                 activeforeground="white",
                                 activebackground="#030E3E",
                                 image=self.min_image)
        self.min_button.photo = self.min_image

        self.default_layout()
        self.count_data()
        disp.display_student_table(self.student_table)
        disp.display_course_table(self.course_table)

    def default_layout(self):
        self.min_button.place_forget()
        self.max_student_button.place(x=470, y=190, height=30, width=30)
        self.max_course_button.place(x=985, y=190, height=30, width=30)
        self.bg_frame.place(x=10, y=190, height=350, width=880)
        self.stud_list_label.place_configure(x=20, y=190, width=480, height=30)
        self.stud_list_frame.place_configure(x=20, y=220, width=480, height=320)
        self.course_label.place_configure(x=540, y=190, width=475, height=30)
        self.course_list_frame.place_configure(x=540, y=220, width=475, height=320)

    def count_data(self):
        self.student_count.config(text=len(SISdatabase.view_student_rec()))
        self.course_count.config(text=len(SISdatabase.view_course_rec()))

    def max_student_table(self):
        self.hide_widgets()
        self.stud_list_label.place_configure(x=20, y=190, width=995, height=30)
        self.stud_list_frame.place_configure(x=20, y=220, width=995, height=320)
        self.min_button.place(x=985, y=190, height=30, width=30)

    def max_course_table(self):
        self.hide_widgets()
        self.course_label.place_configure(x=20, y=190, width=995, height=30)
        self.course_list_frame.place_configure(x=20, y=220, width=995, height=320)
        self.min_button.place(x=985, y=190, height=30, width=30)

    def hide_widgets(self):
        self.stud_list_label.place_forget()
        self.stud_list_frame.place_forget()
        self.max_student_button.place_forget()
        self.max_course_button.place_forget()
        self.course_list_frame.place_forget()
        self.course_label.place_forget()
