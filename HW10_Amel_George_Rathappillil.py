#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  16 12:46:59 2019

@author: amelgr
    This python file contains implementation for student, \
        Instructor, Repository
"""
from datetime import timedelta, datetime
import os
from prettytable import PrettyTable
from collections import defaultdict


class Student:
    """Class student holds the info 
    about individual students"""

    def __init__(self, cwid, name, major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course = defaultdict(str)
        self.summary = {}
        self.required = []
        self.electives = []

    def add_course_grade(self, course, grade):
        self.course[course] = grade

    def add_course_required(self, required_course):
        self.required.append(required_course)

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
        self.req = []
        self.elective = []

    def required_c(self, course):
        self.req.append(course)

    def required_e(self, course):
        self.elective.append(course)


class Repository:

    """Class Repository holds the information about the complete
    students and Instructors """

    def __init__(self, dir_path):
        self.directory = dir_path
        self.students = []
        self.instructors = []
        self.majors = [Major('SFEN'), Major('SYEN')]
        self.file_reading_gen("students.txt", 3, ';', header=True)
        self.file_reading_gen("instructors.txt",  3, '|', header=True)
        self.file_reading_gen("grades.txt",  4, '|', header=True)
        self.file_reading_gen("majors.txt",  3, '\t', header=True)
        
        self.add_req_ele()

    def file_reading_gen(self, path, fields, sep='\t', header=False):
        """File reader method"""
        os.chdir(self.directory)
        # for file in files:
        # if(file ==  "students.txt"):
        try:
            fp = open(os.path.join(self.directory, path), "r")
        except FileNotFoundError:
            raise FileNotFoundError("{path} not found")
        else:
            count = 0
            with fp:
                for line in fp:
                    if(count == 0 and header == True):
                        count +=1
                        continue
                    newline = line.strip().split(sep)

                    if(len(newline) > fields):
                        raise ValueError("Number of fields {fields} is invalid for the given {path}")

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
                        for std in self.students:
                            if(std.cwid == newline[0]):
                                if(newline[2].lower() == 'c' or newline[2].lower() == 'b' or newline[2].lower() == 'a'):
                                    std.add_course_grade(newline[1], newline[2])
                        for inst in self.instructors:
                            if(inst.cwid == newline[3]):
                                inst.add_course(newline[1])

                    if(path == "majors.txt"):
                        count += 1
                        for major in self.majors:
                            if major.major == newline[0]:
                                if newline[1] == 'R':
                                    major.required_c(newline[2])
                                if newline[1] == 'E':
                                    major.required_e(newline[2])

    def add_req_ele(self):
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
                std.course.keys()), dict.fromkeys(std.required, 1) if dict.fromkeys(std.required, 1) != {} else
                None , dict.fromkeys(std.electives,1) if dict.fromkeys(std.electives,1) != {} else None])
        return pt

    def pretty_print_instructor(self):
        """Pretty Print for instrutor"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course',
                                      'Students'])
        for inst1 in self.instructors:
            inst1.instructor_summary()
            for inst in inst1.summary:
                pt.add_row([inst['CWID'], inst['Name'], inst['Dept'],
                            inst['Course'], inst['Students']])
        return pt

    def pretty_print_major(self):
        """Pretty Print for instrutor"""
        pt = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for major in self.majors:
            pt.add_row([major.major, major.req, major.elective])
        return pt


def main():
    try:
        stevens = Repository(
            'C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\hw10')
    except FileNotFoundError:
        raise FileNotFoundError("File not Found")
    except ValueError:
        raise ValueError("Number of fields in file is not correct")
    else:
        print(stevens.pretty_print_student())
        print(stevens.pretty_print_instructor())
        print(stevens.pretty_print_major())

        # print([ ele.name for ele in stevens.students])
        # print([ ele.name for ele in stevens.instructors])


main()
