import SISdatabase

def display_course_table(course_table):
    course_table.delete(*course_table.get_children())
    course_data = SISdatabase.view_course_rec()
    for x in course_data:
        course_table.insert('', 0, values=(x[0], x[1]))

def display_student_table(student_table):
    student_table.delete(*student_table.get_children())
    student_data = SISdatabase.view_student_rec()
    for x in student_data:
        student_table.insert('', 0, values=(x[0], x[1], x[3], x[2], x[4]))
