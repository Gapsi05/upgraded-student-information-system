from tkinter import *
from tkinter import messagebox
import SISdatabase

import displaytable


class AddCourse:
    def __init__(self, frame, table):

        self.add_course_frame = frame
        self.course_table = table

        self.course_id = StringVar()

        self.add_course_id_entry = Entry(self.add_course_frame,
                                         textvariable=self.course_id,
                                         highlightthickness=3,
                                         highlightbackground="#030E3E",
                                         font=("Hops And Barley c3 Bold", 14))
        self.add_course_id_entry.place(x=90, y=50, width=235, height=35)

        self.add_course_text = Text(self.add_course_frame,
                                    highlightthickness=3,
                                    highlightbackground="#030E3E",
                                    font=("Hops And Barley c3 Bold", 14))
        self.add_course_text.place(x=10, y=135, width=315, height=125)

        self.course_id_label = Label(self.add_course_frame,
                                     text="COURSE ID",
                                     font=("Hops And Barley c3 Bold", 11),
                                     fg="#F3CF04", bg="#030E3E")
        self.course_id_label.place(x=10, y=50, width=80, height=35)

        self.course_label = Label(self.add_course_frame,
                                  text="COURSE NAME",
                                  font=("Hops And Barley c3 Bold", 15),
                                  fg="#F3CF04", bg="#030E3E")
        self.course_label.place(x=10, y=100, width=150, height=35)

        self.add_info_button = Button(self.add_course_frame,
                                      command=self.add_course,
                                      text="ADD",
                                      fg="#F3CF04",
                                      bg="#030E3E",
                                      activebackground="#030E3E",
                                      activeforeground="white",
                                      font=("Hops And Barley c3 Bold", 15))
        self.add_info_button.place(x=175, y=300, width=70, height=30)

        self.clear_info_button = Button(self.add_course_frame,
                                        command=self.clear_data,
                                        text="CLEAR",
                                        fg="#F3CF04",
                                        bg="#030E3E",
                                        activebackground="#030E3E",
                                        activeforeground="white",
                                        font=("Hops And Barley c3 Bold", 15))
        self.clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.add_course_id_entry.delete(0, END)
        self.add_course_text.delete(1.0, END)

    def add_course(self):
        if self.add_course_id_entry.get() == "" or self.add_course_text.get(1.0, END) == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        else:
            if messagebox.askyesno("Add Course", "Do you wish to add the course to database?"):
                if SISdatabase.add_course_rec(self.course_id.get().upper(),
                                              self.add_course_text.get(1.0, END).upper().replace("\n", "")):
                    messagebox.showinfo("Success", "Course added to database.")
                    self.clear_data()
                    displaytable.display_course_table(self.course_table)
                else:
                    return
            else:
                return
