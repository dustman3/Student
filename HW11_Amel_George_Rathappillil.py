#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  13 12:46:59 2019

@author: amelgr
    This python file contains implementation for student, \
        Instructor, Repository, Majors
"""
from datetime import timedelta, datetime
import os
from prettytable import PrettyTable
from collections import defaultdict
import sqlite3


class Student:
    """Class student holds the info 
    about individual students"""

    def __init__(self, cwid, name, major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course = defaultdict(str)
        self.summary = {}
        self.required = {}
        self.electives = {}

    def add_course_grade(self, course, grade):
        self.course[course] = grade

    def add_course_required(self, required_course):
        self.required[required_course] = required_course

    def add_course_elective(self, elective_course):
        self.electives = elective_course

    def student_summary(self):
        """ pretty_print method."""
        self.summary = {
            'CWID': self.cwid,
            'Name': self.name,
            'Completed Courses': sorted([key for key in self.course.keys()])
        }


class Instructor:
    """class Instructor holds the 
    individual info about instructor"""

    def __init__(self, cwid, name, department):
        self.cwid = cwid
        self.name = name
        self.department = department
        self.courses = defaultdict(int)
        self.summary = []

    def add_course(self, course):
        self.courses[course] += 1

    def instructor_summary(self):
        for element in self.courses:
            count = self.courses[element]
            self.summary.append({
                'CWID': self.cwid,
                'Name': self.name,
                'Dept': self.department,
                'Course': element,
                'Students': count
            })


class Major:
    """Class Major holds the informations of
    each department"""

    def __init__(self, major):
        self.major = major
        self.req = {}
        self.elective = {}

    def required_c(self, course):
        self.req[course] = course

    def required_e(self, course):
        self.elective[course] = course


class Repository:

    """Class Repository holds the information about the complete
    students and Instructors """

    def __init__(self, dir_path):
        self.directory = dir_path
        self.students = []
        self.instructors = []
        self.majors = []
        self.file_reading_gen("students.txt", 3, '\t', header=True)
        self.file_reading_gen("instructors.txt",  3, '\t', header=True)
        self.file_reading_gen("grades.txt",  4, '\t', header=True)
        self.file_reading_gen("majors.txt",  3, '\t', header=True)
        self.add_req_ele()

    def file_reading_gen(self, path, fields, sep='\t', header=False):
        """File reader method"""
        os.chdir(self.directory)
        try:
            fp = open(os.path.join(self.directory, path), "r")
        except FileNotFoundError:
            raise FileNotFoundError(f"{path} not found in the given directory {self.directory}")
        else:
            count = 0
            with fp:
                for line in fp:
                    if(count == 0 and header == True):
                        count +=1
                        continue
                    newline = line.strip().split(sep)

                    if(len(newline) != fields):
                        raise ValueError(f"Number of fields is {fields} which is invalid for the given {path}")

                    if(path == "students.txt"):
                        count += 1
                        s_temp = Student(newline[0], newline[1], newline[2])
                        self.students.append(s_temp)

                    if(path == "instructors.txt"):
                        count += 1
                        i_temp = Instructor(newline[0], newline[1], newline[2])
                        self.instructors.append(i_temp)

                    if(path == "grades.txt"):
                        count += 1
                        grades = ['A','A-','A+','B+','B-','B', 'C+','C']
                        for std in self.students:
                            if(std.cwid == newline[0]):
                                if newline[2] in grades:
                                    std.add_course_grade(newline[1], newline[2])
                        for inst in self.instructors:
                            if(inst.cwid == newline[3]):
                                inst.add_course(newline[1])

                    if(path == "majors.txt"):
                        count += 1
                        flag = 0
                        for m in self.majors:
                            if m.major == newline[0]:
                                flag = 1
                                m_temp = m
                                if newline[1] == 'R':
                                    m_temp.required_c(newline[2])
                                if newline[1] == 'E':
                                   m_temp.required_e(newline[2])
                                break;
                        if flag == 0:
                            m_temp = Major(newline[0])
                            if newline[1] == 'R':
                                m_temp.required_c(newline[2])
                            if newline[1] == 'E':
                                m_temp.required_e(newline[2])
                            self.majors.append(m_temp)

    def add_req_ele(self):
        """This method add the required courses and Electives"""
        for student in self.students:
            student.student_summary()
            flag = 0
            for major in self.majors:
                if student.major == major.major:
                    for required in major.req:
                        if required in student.course.keys():
                            continue
                        else:
                            student.add_course_required(required)
                    for elective in major.elective:
                        if elective in student.course.keys():
                            flag = 1
                    if(flag == 0):
                        student.add_course_elective(major.elective)

    def pretty_print_student(self):
        """Pretty table for student"""
        pt = PrettyTable(field_names=[
                         'CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'])
        for std in self.students:
            pt.add_row([std.cwid, std.name, std.major, list(
                std.course.keys()), set(std.required.values()) if len(std.required.values()) != 0 else
                None , set(std.electives.values()) if len(std.electives.values()) != 0 else None])
        return pt

    def pretty_print_major(self):
        """Pretty Print for major"""
        pt = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for major in self.majors:
            pt.add_row([major.major, set(major.req.values()) if len(major.req.values()) != 0 else
                None , set(major.elective.values()) if len(major.elective.values()) != 0 else None])
        return pt
    
    def instructor_table_db(self, db_path):
        """ Printing the instructor table from database"""
        db = sqlite3.connect(db_path)
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course',
                                      'Students'])
        for (CWID, Name, Dept, Course,Students) in db.execute("""
        select instructors.CWID, instructors.Name, instructors.Dept
        , grades.Course, count(*) as Students
        from instructors
        join grades
        on instructors.CWID = grades.InstructorCWID
        group by grades.InstructorCWID,
                grades.Course
        order by Students desc
        """):
            pt.add_row([CWID, Name, Dept, Course, Students])
        return pt



def main():
    try:
        stevens = Repository(
            'C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\Homeworks')
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(stevens.pretty_print_student())
        # print(stevens.pretty_print_instructor())
        print(stevens.pretty_print_major())
        print(stevens.instructor_table_db( "C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\Homeworks\810_startup.db"))
        # print([ ele.name for ele in stevens.students])
        # print([ ele.name for ele in stevens.instructors])

main()
