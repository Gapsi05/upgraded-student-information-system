from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import SISdatabase

from AddCourse import AddCourse
from EditCourse import EditCourse
import displaytable as disp


class CoursesInterface:
    def __init__(self, frame):
        self.courses_cont_frame = frame

        self.search_course_id = StringVar()

        self.add_button_img = PhotoImage(file=r"images\addcourse.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"images\editcourse.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"images\deletecourse.png").subsample(1, 1)
        self.srch_img = PhotoImage(file=r"images\searchbuttonimg.png").subsample(1, 1)

        self.add_course_btn = Button(self.courses_cont_frame,
                                image=self.add_button_img,
                                bg="white",
                                command=self.add_course)
        self.add_course_btn.photo = self.add_button_img
        self.add_course_btn.place(x=10, y=50, width=70, height=70)

        self.edit_course_btn = Button(self.courses_cont_frame,
                                 image=self.edit_button_img,
                                 bg="white",
                                 command=self.edit_course)
        self.edit_course_btn.photo = self.edit_button_img
        self.edit_course_btn.place(x=85, y=50, width=70, height=70)

        self.delete_course_btn = Button(self.courses_cont_frame,
                                   image=self.delete_button_img,
                                   bg="white",
                                   command=self.delete_course)
        self.delete_course_btn.photo = self.delete_button_img
        self.delete_course_btn.place(x=160, y=50, width=70, height=70)

        self.search_code_label = Label(self.courses_cont_frame,
                                  font=("Hops And Barley c3 Bold", 10),
                                  fg="#F3CF04",
                                  bg="#030E3E",
                                  text="Course ID:")
        self.search_code_label.place(x=661, y=85, width=80, height=35)

        self.search_course_bar_entry = Entry(self.courses_cont_frame,
                                             textvariable=self.search_course_id,
                                             font=("Hops And Barley c3 Bold", 15, "bold"),
                                             highlightthickness=3,
                                             highlightbackground="#030E3E")
        self.search_course_bar_entry.place(x=740, y=85, width=250, height=35)

        self.search_course_id.trace("w", lambda name, index, mode, sv=self.search_course_id: self.search_course())

        self.search_course_lbl = Label(self.courses_cont_frame, image=self.srch_img)
        self.search_course_lbl.photo = self.srch_img
        self.search_course_lbl.place(x=990, y=85, width=35, height=35)

        self.course_list_label = Label(self.courses_cont_frame,
                                       fg="#F3CF04",
                                       bg="#030E3E",
                                       anchor='w',
                                       text=" LIST OF COURSES",
                                       font=("Hops And Barley c3 Bold", 15))
        self.course_list_label.place(x=360, y=140, width=665, height=30)

        self.course_list_frame = Frame(self.courses_cont_frame,
                                       bg="white",
                                       highlightbackground="#030E3E",
                                       highlightthickness=3)
        self.course_list_frame.place(x=360, y=170, width=665, height=370)

        scroll_x_course_list = Scrollbar(self.course_list_frame,
                                         orient=HORIZONTAL)
        scroll_y_course_list = Scrollbar(self.course_list_frame,
                                         orient=VERTICAL)
        self.course_table = ttk.Treeview(self.course_list_frame,
                                         xscrollcommand=scroll_x_course_list.set,
                                         yscrollcommand=scroll_y_course_list.set,
                                         columns=("course_code","course"))

        scroll_x_course_list.pack(side=BOTTOM, fill=X)
        scroll_y_course_list.pack(side=RIGHT, fill=Y)

        scroll_x_course_list.config(command=self.course_table.xview)
        scroll_y_course_list.config(command=self.course_table.yview)

        self.course_table.heading("course_code", text="Course Code")
        self.course_table.heading("course", text="Course")
        self.course_table['show'] = 'headings'
        self.course_table.column("course_code", width=100)
        self.course_table.column("course", width=390)

        self.course_table.pack(fill=BOTH, expand=1)

        self.heading_label = Label(self.courses_cont_frame,
                                   bg="#A51d23",
                                   fg="white",
                                   anchor='w',
                                   font=("Hops And Barley c3 Bold", 15))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.features_frame = Frame(self.courses_cont_frame,
                                    bg="white",
                                    highlightbackground="#030E3E",
                                    highlightthickness=3)

        self.add_course_frame = Frame(self.courses_cont_frame,
                                      bg="white",
                                      highlightbackground="#030E3E",
                                      highlightthickness=3)
        self.edit_course_frame = Frame(self.courses_cont_frame,
                                       bg="white",
                                       highlightbackground="#030E3E",
                                       highlightthickness=3)

        self.default_layout()
        disp.display_course_table(self.course_table)

    def default_layout(self):
        self.heading_label.config(text=" MENU", fg="#F3CF04", bg="#030E3E")
        self.hide_widgets()
        self.features_frame.place(x=10, y=170, width=340, height=370)

        add_button_nav = Button(self.features_frame,
                                command=self.add_course,
                                activebackground="#F3CF04",
                                fg="#F3CF04",
                                activeforeground="#030E3E",
                                bg="#030E3E",
                                text=" ADD COURSE",
                                image=self.add_button_img,
                                compound="left",
                                anchor="w",
                                font=("Hops And Barley c3 Bold", 22)
                                )
        add_button_nav.place(x=20, y=40, width=290, height=70)

        edit_button_nav = Button(self.features_frame,
                                 font=("Hops And Barley c3 Bold", 22),
                                 command=self.edit_course,
                                 activebackground="#F3CF04",
                                 fg="#F3CF04",
                                 activeforeground="#030E3E",
                                 bg="#030E3E",
                                 text=" EDIT COURSE",
                                 image=self.edit_button_img,
                                 compound="left",
                                 anchor="w",
                                 )
        edit_button_nav.place(x=20, y=120, width=290, height=70)

        delete_button_nav = Button(self.features_frame,
                                   command=self.delete_course,
                                   activebackground="#F3CF04",
                                   fg="#F3CF04",
                                   activeforeground="#030E3E",
                                   bg="#030E3E",
                                   text=" DELETE COURSE",
                                   image=self.delete_button_img,
                                   compound="left",
                                   anchor="w",
                                   font=("Hops And Barley c3 Bold", 18)
                                   )
        delete_button_nav.place(x=20, y=200, width=290, height=70)

    def hide_widgets(self):
        self.features_frame.place_forget()
        self.add_course_frame.place_forget()
        self.edit_course_frame.place_forget()

    def add_course(self):
        self.heading_label.config(text="  ADD COURSE")
        self.hide_widgets()
        self.add_course_frame.place(x=10, y=170, width=340, height=370)
        AddCourse(self.add_course_frame, self.course_table)

    def edit_course(self):
        self.heading_label.config(text="  EDIT COURSE")
        self.hide_widgets()
        self.edit_course_frame.place(x=10, y=170, width=340, height=370)
        EditCourse(self.edit_course_frame, self.course_table)

    def delete_course(self):
        cursor_row = self.course_table.focus()
        contents = self.course_table.item(cursor_row)
        rows = contents['values']
        if rows == "":
            messagebox.showerror("Error", "Select course first")
            return
        else:
            if messagebox.askyesno("Delete Course", "Do you wish to delete this course? Some students might be enrolled"
                                                    " in this course."):
                if SISdatabase.delete_course_rec(rows[0]):
                    messagebox.showinfo("Success", "Course deleted in database")
                    disp.display_course_table(self.course_table)
                    self.default_layout()
                return
            else:
                return

    def search_course(self):
        result = SISdatabase.search_course_rec(self.search_course_id.get().upper())
        self.course_table.delete(*self.course_table.get_children())
        if not result:
            return
        else:
            for x in result:
                self.course_table.insert('', 0, values=(x[0], x[1]))
