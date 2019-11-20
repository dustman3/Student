#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 4 12:46:59 2019

@author: amelgr

    This file Implements a program for the game Rock,Paper and Scissors
"""

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/instructors')
def student_courses():
    dbpath = "C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\Homeworks\810_startup.db"

    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError:
        return f"Error: unable to open the {dbpath}"
    else:
        query = """select instructors.CWID, instructors.Name, instructors.Dept
                    , grades.Course, count(*) as Students
                    from instructors
                    join grades
                    on instructors.CWID = grades.InstructorCWID
                    group by grades.InstructorCWID,
                            grades.Course
                    order by CWID asc """
    
        data = [{'cwid' : cwid , 'name' : name, 'dept' :  dept, 'course' : course, 'students': students}
                for cwid, name, dept, course, students in db.execute(query)]
        
        db.close()

        return render_template(
            'instructors.html',
            title = 'Stevens Repository',
            table_title = 'Courses and student counts',
            students = data
        )

app.run(debug=True)