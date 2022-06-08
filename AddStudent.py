from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import SISdatabase
import displaytable


class AddStudent:
    def __init__(self, frame, table, searchentry):
        self.add_student_frame = frame
        self.student_table = table
        self.searchEntry = searchentry

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.add_name_entry = Entry(self.add_student_frame,
                                    textvariable=self.name,
                                    highlightthickness=3,
                                    highlightbackground="#030E3E",
                                    font=("Hops And Barley c3 Bold", 14))
        self.add_name_entry.place(x=90, y=20, width=235, height=35)

        self.add_id_entry = Entry(self.add_student_frame,
                                  textvariable=self.id_no,
                                  highlightthickness=3,
                                  highlightbackground="#030E3E",
                                  font=("Hops And Barley c3 Bold", 14))
        self.add_id_entry.place(x=90, y=80, width=235, height=35)

        self.add_year_combo = ttk.Combobox(self.add_student_frame,
                                           textvariable=self.year,
                                           state="readonly",
                                           font=("Hops And Barley c3 Bold", 14),
                                           values=["1ST YEAR", "2ND YEAR", "3RD YEAR", "4TH YEAR", "5TH YEAR"])
        self.add_year_combo.place(x=90, y=125, width=235, height=35)

        self.add_course_id_entry = Entry(self.add_student_frame,
                                         textvariable=self.course,
                                         highlightthickness=3,
                                         highlightbackground="#030E3E",
                                         font=("Hops And Barley c3 Bold", 14))
        self.add_course_id_entry.place(x=90, y=170, width=235, height=35)

        self.add_gender_combo = ttk.Combobox(self.add_student_frame,
                                             textvariable=self.gender,
                                             state="readonly",
                                             font=("Hops And Barley c3 Bold", 14),
                                             values=["MALE", "FEMALE"])
        self.add_gender_combo.place(x=90, y=215, width=235, height=35)

        self.name_label = Label(self.add_student_frame,
                           text="NAME",
                           font=("Hops And Barley c3 Bold", 17),
                           fg="#F3CF04",
                           bg="#030E3E")
        self.name_label.place(x=10, y=20, width=80, height=35)

        self.name_format = Label(self.add_student_frame,
                                 text="Last Name, First Name, M.I",
                                 font=("Hops And Barley c3 Bold", 8),
                                 fg="#030E3E",
                                 bg="white")
        self.name_format.place(x=95, y=56, height=20)

        self.id_no_label = Label(self.add_student_frame,
                                 text="ID NO.",
                                 font=("Hops And Barley c3 Bold", 17),
                                 fg="#F3CF04",
                                 bg="#030E3E")
        self.id_no_label.place(x=10, y=80, width=80, height=35)

        self.year_label = Label(self.add_student_frame,
                                text="YEAR",
                                font=("Hops And Barley c3 Bold", 17),
                                fg="#F3CF04",
                                bg="#030E3E")
        self.year_label.place(x=10, y=125, width=80, height=35)

        self.course_id_label = Label(self.add_student_frame,
                                     text="COURSE ID",
                                     font=("Hops And Barley c3 Bold", 11),
                                     fg="#F3CF04",
                                     bg="#030E3E")
        self.course_id_label.place(x=10, y=170, width=80, height=35)

        self.gender_label = Label(self.add_student_frame,
                                  text="GENDER",
                                  font=("Hops And Barley c3 Bold", 14),
                                  fg="#F3CF04",
                                  bg="#030E3E")
        self.gender_label.place(x=10, y=215, width=80, height=35)

        self.add_info_button = Button(self.add_student_frame,
                                      command=self.add_student,
                                      text="ADD",
                                      fg="#F3CF04",
                                      bg="#030E3E",
                                      activebackground="#030E3E",
                                      activeforeground="white",
                                      font=("Hops And Barley c3 Bold", 15))
        self.add_info_button.place(x=175, y=300, width=70, height=30)

        self.clear_info_button = Button(self.add_student_frame,
                                        command=self.clear_data,
                                        text="CLEAR",
                                        fg="#F3CF04",
                                        bg="#030E3E",
                                        activebackground="#030E3E",
                                        activeforeground="white",
                                        font=("Hops And Barley c3 Bold", 15))
        self.clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.add_id_entry.delete(0, END)
        self.add_name_entry.delete(0, END)
        self.add_course_id_entry.delete(0, END)
        self.add_year_combo.set("")
        self.add_gender_combo.set("")

    def add_student(self):
        if messagebox.askyesno("Add Student", "Do you want to add the student in the database"):
            if not SISdatabase.info_checker(self.id_no.get(), self.name.get().upper(), self.year.get(),
                                            self.course.get().upper(), self.gender.get().upper()):
                return
            else:
                if SISdatabase.add_student_rec(self.id_no.get(), self.name.get().upper(), self.year.get(),
                                               self.course.get().upper(), self.gender.get()):
                    messagebox.showinfo("Success", "Student added to database")
                    self.clear_data()
                    displaytable.display_student_table(self.student_table)
                else:
                    return
