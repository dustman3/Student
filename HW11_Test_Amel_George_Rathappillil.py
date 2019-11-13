#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  15 12:46:59 2019

@author: amelgr

    This python file contains test implementation for date_arithmetic, file_reading_gen,\
     FileAnalyzer
"""
import unittest, sqlite3
from HW11_Amel_George_Rathappillil import Student, Instructor, Repository, Major


class TestRepo(unittest.TestCase):
    """ Class for testing Students, Instructors and Repository"""

    def test_student(self):
        """Test method to test Student class"""
        s = Student(1, 'Amel', 'SSW')
        self.assertEqual(s.cwid, 1)
        self.assertNotEqual(s.cwid, 2)
        self.assertEqual(s.name, 'Amel')
        self.assertNotEqual(s.cwid, 'PROF')
        self.assertEqual(s.major, 'SSW')

    def test_instructors(self):
        i = Instructor(2, 'Prof Rowland', 'SSW')
        self.assertEqual(i.cwid, 2)
        self.assertNotEqual(i.cwid, 1)
        self.assertEqual(i.name, 'Prof Rowland')
        self.assertNotEqual(i.cwid, 'PROF')
        self.assertEqual(i.department, 'SSW')

    def test_major(self):
        major = Major('SSW')
        self.assertEqual(major.major, 'SSW')
        self.assertNotEqual(major.major, 'SSE')

    def test_repository(self):
        repo = Repository(
            'C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\Homeworks')

        # print([[major.major, set(major.req.values()) if len(major.req.values()) != 0 else
        #         None , set(major.elective.values()) if len(major.elective.values()) != 0 else None] for major in repo.majors])

        self.assertEqual([['10103', 'Jobs, S', 'SFEN', ['SSW 810', 'CS 501'], {'SSW 555', 'SSW 540'}, None],
                     ['10115', 'Bezos, J', 'SFEN', [], {'SSW 555', 'SSW 810','SSW 540'}, {'CS 554', 'CS 501', 'CS 546'}],
                     ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 554', 'CS 501', 'CS 546'}], 
                    ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570'], None, {'SSW 565', 'SSW 810'}]],
                        [[std.cwid, std.name, std.major, list(
                std.course.keys()), set(std.required.values()) if len(std.required.values()) != 0 else
                None, set(std.electives.values()) if len(std.electives.values()) != 0 else None] for std in repo.students])

        self.assertNotEqual([['asdfasdf', 'Jobs, S', 'SFEN', ['SSW 810', 'CS 501'], {'SSW 555', 'SSW 540'}, None],
                     ['10115', 'Bezos, J', 'SFEN', [], {'SSW 555', 'SSW 810','SSW 540'}, {'CS 554', 'CS 501', 'CS 546'}],
                     ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 554', 'CS 501', 'CS 546'}], 
                    ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570'], None, {'SSW 565', 'SSW 810'}]],
                         [[std.cwid, std.name, std.major, list(
                std.course.keys()), set(std.required.values()) if len(std.required.values()) != 0 else
                None, set(std.electives.values()) if len(std.electives.values()) != 0 else None] for std in repo.students])

        self.assertEqual([['SFEN', {'SSW 540', 'SSW 810', 'SSW 555'}, {'CS 554', 'CS 546', 'CS 501'}], ['CS', {'CS 546', 'CS 570'}, {'SSW 810', 'SSW 565'}]],
                         [[major.major, set(major.req.values()) if len(major.req.values()) != 0 else
                None , set(major.elective.values()) if len(major.elective.values()) != 0 else None] for major in repo.majors])

        self.assertNotEqual([['INVALID Major', {'SSW 540', 'SSW 810', 'SSW 555'}, {'CS 554', 'CS 546', 'CS 501'}], ['CS', {'CS 546', 'CS 570'}, {'SSW 810', 'SSW 565'}]],
                         [[major.major, set(major.req.values()) if len(major.req.values()) != 0 else
                None , set(major.elective.values()) if len(major.elective.values()) != 0 else None] for major in repo.majors])
        
        self.assertNotEqual([],
                         [[major.major, set(major.req.values()) if len(major.req.values()) != 0 else
                None , set(major.elective.values()) if len(major.elective.values()) != 0 else None] for major in repo.majors])


        self.assertEqual(['Cohen, R', 'Rowland, J', 'Hawking, S'],
                         [ele.name for ele in repo.instructors])

        self.assertNotEqual(['Jobs, S', 'Bezos, J', 'Musk, E', 'Gates, B'],
                            [ele.name for ele in repo.instructors])

    def test_instructors_db(self):
        """This method is used to test the instructors table
        which is fetched from db"""

        repo = Repository(
            'C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\Homeworks')
        
        db_path = "C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\Homeworks\810_startup.db"
        db = sqlite3.connect(db_path)

        Instructor_db_value = [('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
        ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
        ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
        ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
        ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
        ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1)]

        self.assertEqual(Instructor_db_value,
                         [(CWID, Name, Dept, Course,Students) for (CWID, Name, Dept, Course,Students) in db.execute("""
        select instructors.CWID, instructors.Name, instructors.Dept
        , grades.Course, count(*) as Students
        from instructors
        join grades
        on instructors.CWID = grades.InstructorCWID
        group by grades.InstructorCWID,
                grades.Course
        order by Students desc
        """)])
        


if (__name__ == '__main__'):
    unittest.main(exit=False, verbosity=2)
