import sqlite3

from flask import Flask, render_template
from flask import request
from flask import redirect

from models.student import Student
from models.subject import Subject
from models.teacher import Teacher
from tables import studenttable, teachertable, subjecttable, studentsubjecttable

app = Flask(__name__)


# the base level of the interface. each line prints out a link to a table.
@app.route("/")
def index():
    return '<h1>Database Assignment</h1>' \
           '<a href="/students">Students</a>' \
           '<br><br>' \
           '<a href="/teachers">Teachers</a>' \
           '<br><br>' \
           '<a href="/subjects">Subjects</a>'


# this displays the student table, including links to edit the students.
@app.route("/students", methods=["GET", "POST"])
def students():
    # connects to the database
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    if request.method != "POST":  # if you aren't searching the database
        # this creates a new instance of 'StudentTable', a class that stores the table functions.
        table = studenttable.StudentTable()
        students = table.get_all(c)  # gets all the data in the table and puts it into a list
        connect.close()  # closes the connection to the database
        return render_template('students.html', items=students)  # renders the template 'students.html', passing in
        # the students from the get_all function
    else:
        try:
            # searches everything under the query
            search = request.form["search"]
            query = "SELECT id, firstName, lastName, yearLevel FROM Student as s "
            if len(search) > 0:
                query += "WHERE LOWER(s.id) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(s.firstName) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(s.lastName) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(s.yearLevel) LIKE '%" + str(search) + "%'"
            query += " ORDER BY s.lastName"
            c.execute(query)
        except Exception as e:  # exception catch!! wow!!!
            return '<h1>you have a problem. oh dear. - ' + str(e) + '</h1>'
        # gets the results of the query and creates a list to use to render the template.
        students = []
        for row in c.fetchall():
            student = Student()
            student.id = row[0]
            student.first_name = row[1]
            student.last_name = row[2]
            student.year_level = row[3]
            students.append(student)
        connect.close()  # closes the connection
        return render_template('students.html', items=students)  # renders the template 'students.html', passing in
        # the list of students.


# this displays the teacher table, including links to edit the teachers. this is essentially the exact same as the
# student table, hence why this comment is the same.
@app.route("/teachers", methods=["GET", "POST"])
def teachers():
    # connects to the database
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    if request.method != "POST":  # again, if not searching
        # creates the teacher table object.
        table = teachertable.teacherTable()
        teachers = table.get_all(c)  # gets everything in the table
        connect.close()  # closes the connection
        return render_template('teachers.html', items=teachers)  # renders the template 'teachers.html', passing in
        # the results of the get_all function.
    else:
        try:
            # searches everything under the query
            search = request.form["search"]
            query = "SELECT id, firstName, lastName FROM Teacher as t "
            if len(search) > 0:
                query += "WHERE LOWER(t.id) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(t.firstName) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(t.lastName) LIKE '%" + str(search) + "%'"
            query += " ORDER BY t.lastName"
            c.execute(query)
        except Exception as e:  # exception catch!! wow!!!
            return '<h1>you have a problem. oh dear. - ' + str(e) + '</h1>'
        # gets the results of the query and creates a list to use to render the template.
        teachers = []
        for row in c.fetchall():
            teacher = Teacher()
            teacher.id = row[0]
            teacher.first_name = row[1]
            teacher.last_name = row[2]
            teachers.append(teacher)
        connect.close()  # closes the connection.
        return render_template('teachers.html', items=teachers)  # renders the template 'teachers.html', passing in
        # the list of teachers.


# this displays the subject table, including links to edit the subjects. bored yet?
@app.route("/subjects", methods=["GET", "POST"])
def subjects():
    # connects to the database
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    if request.method != "POST":  # if not searching
        # creates the subject table object.
        table = subjecttable.SubjectTable()
        subjects = table.get_all(c)
        connect.close()
        return render_template('subjects.html', items=subjects)  # renders the template 'subjects.html', passing in
        # the results of the get_all function.
    else:
        try:
            # searches everything under the query
            search = request.form["search"]
            query = "SELECT id, name, yearLevel, teacherId FROM Subject as s "
            if len(search) > 0:
                query += "WHERE LOWER(s.id) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(s.name) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(s.yearLevel) LIKE '%" + str(search) + "%'"
                query += "OR LOWER(s.teacherId) LIKE '%" + str(search) + "%'"
            query += " ORDER BY s.name"
            c.execute(query)
        except Exception as e:  # exception catch!! wow!!!
            return '<h1>you have a problem. oh dear. - ' + str(e) + '</h1>'
        # gets the results of the query and creates a list to use to render the template.
        subjects = []
        for row in c.fetchall():
            subject = Subject()
            subject.id = row[0]
            subject.name = row[1]
            subject.year_level = row[2]
            subject.teacher_id = row[3]
            subjects.append(subject)
        connect.close()
        return render_template('subjects.html', items=subjects)  # renders the template 'subjects.html', passing in
        # the list of subjects.


# finally something different. this is the page you get when editing or adding a student.
@app.route("/students/edit", methods=["GET", "POST"])
def edit_student():
    # the connection, ladies and gentlemen. or, well, Mr Jones.
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    table = studenttable.StudentTable()
    if request.method == 'POST':  # if you're submitting your form
        try:
            #  this gets all the data you've submitted and stores it in variables :)
            id = request.form['id']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            year_level = request.form['year_level']
            # data validity checks!! you can call yourself '@($U%Y$*(#)' but heaven forbid you call yourself
            # '2834756748329'. i didn't check for special characters cause some names have them (for example,
            # hyphens) and i thought it would be a bit bad to exclude them.
            if first_name == "":
                return '<h4>Error: First Name field cannot be blank.</h4>'
            elif last_name == "":
                return '<h4>Error: Last Name field cannot be blank.</h4>'
            elif year_level == "":
                return '<h4>Error: Year level field cannot be blank.</h4>'
            else:
                if any(i.isdigit() for i in first_name):
                    return '<h4>Error: Your first name cannot contain numbers.</h4>'
                elif any(i.isdigit() for i in last_name):
                    return '<h4>Error: Your last name cannot contain numbers.</h4>'
                if not any(i.isdigit() for i in year_level):
                    return '<h4>Error: Year level must be a number.</h4>'
                if year_level == '0':
                    return '<h4>Error: Why would your year level be 0?</h4>'
                if 9 < int(year_level) > 13:
                    return '<h4>Error: Year level must be a high school year, 9-13.</h4>'  # this was originally just
                    # 9 or 10, but it didn't take anything to fix it so i did
                else:
                    if id == '-1':  # '-1' is an id that we give to students that don't exist yet.
                        table.add(c, first_name, last_name, year_level)  # adds the new student to the table.
                    else:
                        student = table.get_by_id(c, id)  # this gets the student you want by using the id parameter.
                        student.first_name = first_name  # this and the two lines below it are updating the values
                        # based on the information in the form
                        student.last_name = last_name
                        student.year_level = year_level
                        table.update(c, student)  # this updates it in the actual database
                    connect.commit()  # commits changes
                    connect.close()  # closes connection
                    return redirect('/students')  # redirects you back to the student table.
        except Exception as e:  # this is to prevent it breaking when you enter floats. it won't break, but if you
            # don't understand exception messages you're out of luck.
            return '<h3>You have an issue: ' + str(e) + ' Please fix this issue.</h3>'
    # if you haven't already submitted your edited student, it gives you the form to edit the student
    else:
        if 'id' in request.args.keys():  # because a student that doesn't exist yet doesn't have an id, this checks
            # whether you're editing or adding a student.
            id = request.args["id"]
            student = table.get_by_id(c, id)  # gets the student using the id
            subjects = table.get_subjects(c, id)  # this is where you can see the list of subjects your student
            # takes! i didn't forget, i promise!
            connect.close()
            return render_template('editstudent.html', item=student, subjects=subjects)  # renders the template
        else:
            connect.close()
            return render_template('editstudent.html', item=Student(-1, '', '', 9), subjects="No subjects yet!")  #
            # uses a blank student template with default values to create an edit page for a new student


# this does the same as the student edit page above. i do not want to type every single comment out again so i will
# just comment on the differences
@app.route("/teachers/edit", methods=["GET", "POST"])
def edit_teacher():
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    table = teachertable.teacherTable()
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        if first_name == "":
            return '<h4>Error: First Name field cannot be blank.</h4>'
        elif last_name == "":
            return '<h4>Error: Last Name field cannot be blank.</h4>'
        else:
            if any(i.isdigit() for i in first_name):
                return '<h4>Error: Your first name cannot contain numbers.</h4>'
            elif any(i.isdigit() for i in last_name):
                return '<h4>Error: Your last name cannot contain numbers.</h4>'
            else:
                if id == '-1':
                    table.add(c, request.form['first_name'], request.form['last_name'])
                else:
                    teacher = table.get_by_id(c, id)
                    teacher.first_name = request.form['first_name']
                    teacher.last_name = request.form['last_name']
                    table.update(c, teacher)
                connect.commit()
                connect.close()
                return redirect('/teachers')
    else:
        if 'id' in request.args.keys():
            id = request.args["id"]
            teacher = table.get_by_id(c, id)
            subjects = table.get_subjects(c, id)  # rather than getting the subjects a student takes, it's the
            # subjects a teacher teaches.
            connect.close()
            return render_template('editteacher.html', item=teacher, subjects=subjects)
        else:
            connect.close()
            return render_template('editteacher.html', item=Teacher(-1, '', ''), subjects="No subjects taught.")


# this one also basically does the same thing except there are a few differences
@app.route("/subjects/edit", methods=["GET", "POST"])
def edit_subject():
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    table = subjecttable.SubjectTable()
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        year_level = request.form['year_level']  # there is no teacher id in this because you select your teacher
        # with a dropdown menu instead
        if name == "":
            return '<h4>Error: Name field cannot be blank.</h4>'
        elif year_level == "":
            return '<h4>Error: Year level field cannot be blank.</h4>'
        else:
            if not any(i.isdigit() for i in year_level):
                return '<h4>Error: Year level must be a number.</h4>'
            if year_level == '0':
                return '<h4>Error: Why would your year level be 0?</h4>'
            if 9 < int(year_level) > 13:
                return '<h4>Error: Year level must be a valid high school year level (9-13).</h4>'
            else:
                if id == '-1':
                    table.add(c, request.form['name'], request.form['year_level'], request.form['teacher_id'])
                else:
                    subject = table.get_by_id(c, id)
                    subject.name = request.form['name']
                    subject.year_level = request.form['year_level']
                    subject.teacher_id = request.form['teacher_id']
                    table.update(c, subject)
                connect.commit()
                connect.close()
                return redirect('/subjects')
    else:
        # this creates a table of the available teachers so it can be used for the dropdown menu
        teacher_table = teachertable.teacherTable()
        teachers = teacher_table.get_all(c)
        if 'id' in request.args.keys():
            id = request.args["id"]
            subject = table.get_by_id(c, id)
            students = table.get_students(c, id)
            connect.close()
            return render_template('editsubject.html', item=subject, teachers=teachers, students=students)
        else:
            connect.close()
            return render_template('editsubject.html', item=Subject(-1, '', 9, 0), teachers=teachers,
                                   students="No Students available for a new subject")


# this is the code that deletes things!!!
@app.route("/delete")
def delete():
    connect = sqlite3.connect('Database.db')
    c = connect.cursor()
    if request.args["type"] == 'student':  # if you want to delete a student
        table = studenttable.StudentTable()
        table.delete_by_id(c, request.args['id'])  # finds the student you want to delete in the table and deletes it
        connect.commit()
        connect.close()
        return redirect('/students')
    elif request.args["type"] == 'teacher':  # if you want to delete a teacher
        table = teachertable.teacherTable()
        subject_table = subjecttable.SubjectTable()
        # this one is a bit different since it has to make sure that the subjects that this teacher was teaching have
        # their teacher values set to none cause if you don't do that it breaks.
        for subject in subject_table.get_by_teacher(c, request.args['id']):
            subject.teacher_id = None
            subject_table.update(c, subject)
        table.delete_by_id(c, request.args['id'])  # finds the teacher you want to delete in the table and deletes it
        connect.commit()
        connect.close()
        return redirect('/teachers')
    elif request.args["type"] == 'subject':  # if you want to delete a subject
        table = subjecttable.SubjectTable()
        table.delete_by_id(c, request.args['id'])  # finds the subject you want to delete in the table and deletes it
        connect.commit()
        connect.close()
        return redirect('/subjects')
    elif request.args["type"] == 'studentsubject':  # if you want to delete a subject from a student
        table = studentsubjecttable.StudentSubjectTable()
        student_id = request.args["studentid"]
        subject_id = request.args["subjectid"]
        table.delete_by_id(c, subject_id, student_id)  # finds the 'studentsubject' you want to delete in the table
        # and deletes it
        connect.commit()
        connect.close()
        return redirect('/students/edit?id=' + str(request.args['studentid']))  # unlike the ones above, it sends you
        # to the edit page of the student you deleted the subject from.
    else:
        connect.close()
        return render_template('error.html')  # if, for some inexplicable reason, none of those conditions are
        # filled, it gives you an error screen. this shouldn't happen.


# this allows you to add a subject to a student.
@app.route("/students/edit/addsubject", methods=['GET', 'POST'])
def add_subject_to_student():
    connect = sqlite3.connect("Database.db")
    c = connect.cursor()
    id = request.args["id"]  # gets you the id of the student you're editing
    subject = subjecttable.SubjectTable()
    subjects = subject.get_all(c)  # gets you the list of subjects available
    table = studenttable.StudentTable()
    student = table.get_by_id(c, id)
    if request.method != 'POST':  # if you haven't submitted the form yet
        connect.close()
        return render_template('addsubject.html', subjects=subjects, student=student)
    else:
        sstable = studentsubjecttable.StudentSubjectTable()
        subject_id = request.form['subject']  # which subject have you chosen??? we shall see
        sstable.add(c, id, subject_id)
        connect.commit()
        connect.close()
        return redirect('/students/edit?id=' + id)  # takes you back to your student :)


app.run()  # runs the app. the END. it's over. no more comments.
