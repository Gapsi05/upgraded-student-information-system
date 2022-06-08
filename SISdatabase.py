from tkinter import messagebox
import sqlite3


def data():
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coursedata (course_id VARCHAR(10) NOT NULL PRIMARY KEY, course_name " 
                "VARCHAR(100) NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS studentdata (stud_id VARCHAR(9) NOT NULL PRIMARY KEY,"
                "stud_name VARCHAR(100) NOT NULL, stud_year VARCHAR(8), stud_course_id VARCHAR(10),"
                "stud_gender VARCHAR(6) NOT NULL,"
                "FOREIGN KEY(stud_course_id)"
                "REFERENCES coursedata(course_id)"
                "   ON DELETE RESTRICT"
                "   ON UPDATE CASCADE) ")
    con.commit()
    con.close()

def add_student_rec(studid, studname, studyear, studcourseid, studgender):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO studentdata VALUES(?, ?, ?, ?, ?)",
                    (studid, studname, studyear, studcourseid, studgender))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        if studcourseid not in list_of_courses():
            messagebox.showerror("Error", "Course ID not in database")
        else:
            messagebox.showerror("Error", "Student ID already in database.")
        return False

def add_course_rec(course_id, course_name):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO coursedata VALUES (?, ?)", (course_id, course_name))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Course ID already in database.")
        return False

def view_student_rec():
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentdata")
    students = cur.fetchall()
    con.close()
    return students

def view_course_rec():
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    cur.execute("SELECT * FROM coursedata")
    courses = cur.fetchall()
    con.close()
    return courses

def delete_student_rec(studid):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    cur.execute("DELETE FROM studentdata WHERE stud_id=?", (studid,))
    con.commit()
    con.close()

def delete_course_rec(course_id):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM coursedata WHERE course_id=?", (course_id,))
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "You cannot delete this course. Students are enrolled in this course.")
        return False
    con.commit()
    con.close()
    return True

def update_student_rec(key, studid, studname, studyear, studcourseid, studgender):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    try:
        if key != studid:
            cur.execute("UPDATE studentdata SET stud_id=?, stud_name=?, stud_year=?, stud_course_id=?, stud_gender=? "
                        "WHERE stud_id=?", (studid, studname, studyear, studcourseid, studgender, key))
        else:
            cur.execute("UPDATE studentdata SET stud_name=?, stud_year=?, stud_course_id=?, stud_gender=? "
                        "WHERE stud_id=?", (studname, studyear, studcourseid, studgender, studid))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        if studcourseid not in list_of_courses():
            messagebox.showerror("Error", "Course ID not in database")
        else:
            messagebox.showerror("Error", "Student ID already in database.")
        return False

def update_course_rec(key, course_id, course_name):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    try:
        if key != course_id:
            cur.execute("UPDATE coursedata SET course_id=?, course_name=?  WHERE course_id=?",
                        (course_id, course_name, key))
        else:
            cur.execute("UPDATE coursedata SET course_name=?  WHERE course_id=?", (course_name, course_id))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Course ID already in database.")
        return False

def search_student_rec(student_id):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentdata WHERE stud_id LIKE ?", ('%'+student_id+'%',))
    result = cur.fetchall()
    con.close()
    return result

def search_course_rec(course_id):
    con = sqlite3.connect("students.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    cur.execute("SELECT * FROM coursedata WHERE course_id LIKE ?", ('%'+course_id+'%',))
    result = cur.fetchall()
    con.close()
    return result

def info_checker(studid, name, year, courseid, gender):
    if studid == "" or name == "" or year == "" or courseid == "" or gender == "":
        messagebox.showerror("Error", "Please fill out all fields")
        return False
    elif len(studid) != 9 or studid[4] != '-' or not studid.replace("-", "").isdigit():
        messagebox.showerror("Error", "Invalid ID Number")
        return False
    else:
        return True

def list_of_courses():
    course_list = []
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("SELECT course_id FROM coursedata")
    result = cur.fetchall()
    for x in result:
        course_list.append(x[0])
    con.close()
    return course_list
