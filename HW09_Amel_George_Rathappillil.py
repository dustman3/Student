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

    def add_course_grade(self, course, grade):
        self.course[course] = grade

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


class Repository:

    """Class Repository holds the information about the complete
    students and Instructors """

    def __init__(self, dir_path):
        self.directory = dir_path
        self.students = []
        self.instructors = []
        self.file_reading_gen()

    def file_reading_gen(self):
        """File reader method"""
        os.chdir(self.directory)
        # for file in files:
        # if(file ==  "students.txt"):
        try:
            fp = open(os.path.join(self.directory, "students.txt"), "r")
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            with fp:
                for line in fp:
                    newline = line.strip().split('\t')
                    if(len(newline) > 3):
                        raise ValueError("Number of fields is invalid")
                    s_temp = Student(newline[0], newline[1], newline[2])
                    self.students.append(s_temp)

        # elif(file == "instructors.txt"):
        try:
            fp = open(os.path.join(self.directory, "instructors.txt"), "r")
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            with fp:
                for line in fp:
                    newline = line.strip().split('\t')
                    if(len(newline) > 3):
                        raise ValueError("Number of fields is invalid")
                    i_temp = Instructor(newline[0], newline[1], newline[2])
                    self.instructors.append(i_temp)

        # elif(file == "grades.txt"):
        try:
            fp = open(os.path.join(self.directory, "grades.txt"), "r")
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            with fp:
                for line in fp:
                    newline = line.strip().split('\t')
                    if(len(newline) > 4):
                        raise ValueError("Number of fields is invalid")
                    for std in self.students:
                        if(std.cwid == newline[0]):
                            std.add_course_grade(newline[1], newline[2])
                    for inst in self.instructors:
                        if(inst.cwid == newline[3]):
                            inst.add_course(newline[1])

    def pretty_print_student(self):
        """Pretty table for student"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        for std in self.students:
            std.student_summary()
            pt.add_row([std.summary['CWID'], std.summary['Name'],
                        std.summary['Completed Courses']])
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


def main():
    try:
        stevens = Repository(
            'C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\hw9')
    except FileNotFoundError:
        raise FileNotFoundError("File not Found")
    except ValueError:
        raise ValueError("Number of fields in file is not correct")
    else:
        print(stevens.pretty_print_student())
        print(stevens.pretty_print_instructor())
        # print([ ele.name for ele in stevens.students])
        # print([ ele.name for ele in stevens.instructors])



main()
