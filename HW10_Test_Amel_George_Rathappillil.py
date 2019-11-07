#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  15 12:46:59 2019

@author: amelgr

    This python file contains test implementation for date_arithmetic, file_reading_gen,\
     FileAnalyzer
"""
import unittest
from HW10_Amel_George_Rathappillil import Student, Instructor, Repository, Major


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
            'C:\\Users\\amelg\\Documents\\Course materials\\SSE810\\hw10')

        # print([[ele.cwid, ele.name, ele.major, dict.fromkeys(ele.required, 1) if dict.fromkeys(ele.required, 1) != {} else
        #         None, dict.fromkeys(ele.electives, 1) if dict.fromkeys(ele.electives, 1) != {} else None] for ele in repo.students])

        self.assertEqual([['10103', 'Baldwin, C', 'SFEN', {'SSW 540': 1, 'SSW 564': 1, 'SSW 555': 1}, None],
                          ['10115', 'Wyatt, X', 'SFEN', {'SSW 540': 1, 'SSW 564': 1, 'SSW 555': 1}, None], ['10172', 'Forbes, I', 'SFEN',
                                                                                                            {'SSW 540': 1, 'SSW 564': 1, 'SSW 567': 1}, {'CS 501': 1, 'CS 513': 1, 'CS 545': 1}],
                          ['10175', 'Erickson, D', 'SFEN', {'SSW 540': 1, 'SSW 555': 1}, {
                              'CS 501': 1, 'CS 513': 1, 'CS 545': 1}],
                          ['10183', 'Chapman, O', 'SFEN', {'SSW 540': 1, 'SSW 564': 1, 'SSW 555': 1, 'SSW 567': 1},
                           {'CS 501': 1, 'CS 513': 1, 'CS 545': 1}], ['11399', 'Cordova, I', 'SYEN',
                                                                      {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1}, None], ['11461', 'Wright, U', 'SYEN', {'SYS 671': 1, 'SYS 612': 1},
                                                                                                                          {'SSW 810': 1, 'SSW 565': 1, 'SSW 540': 1}],
                          ['11658', 'Kelly, P', 'SYEN', {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1},
                           {'SSW 810': 1, 'SSW 565': 1, 'SSW 540': 1}], ['11714', 'Morton, A', 'SYEN',
                                                                         {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1}, {'SSW 810': 1, 'SSW 565': 1, 'SSW 540': 1}],
                          ['11788', 'Fuller, E', 'SYEN', {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1}, None]],
                         [[ele.cwid, ele.name, ele.major, dict.fromkeys(ele.required, 1) if dict.fromkeys(ele.required, 1) != {} else
                           None, dict.fromkeys(ele.electives, 1) if dict.fromkeys(ele.electives, 1) != {} else None] for ele in repo.students])

        self.assertNotEqual([['INVALID VALUE', 'Baldwin, C', 'SFEN', {'SSW 540': 1, 'SSW 564': 1, 'SSW 555': 1}, None],
                             ['10115', 'Wyatt, X', 'SFEN', {'SSW 540': 1, 'SSW 564': 1, 'SSW 555': 1}, None], ['10172', 'Forbes, I', 'SFEN',
                                                                                                               {'SSW 540': 1, 'SSW 564': 1, 'SSW 567': 1}, {'CS 501': 1, 'CS 513': 1, 'CS 545': 1}],
                             ['10175', 'Erickson, D', 'SFEN', {'SSW 540': 1, 'SSW 555': 1}, {
                                 'CS 501': 1, 'CS 513': 1, 'CS 545': 1}],
                             ['10183', 'Chapman, O', 'SFEN', {'SSW 540': 1, 'SSW 564': 1, 'SSW 555': 1, 'SSW 567': 1},
                              {'CS 501': 1, 'CS 513': 1, 'CS 545': 1}], ['11399', 'Cordova, I', 'SYEN',
                                                                         {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1}, None], ['11461', 'Wright, U', 'SYEN', {'SYS 671': 1, 'SYS 612': 1},
                                                                                                                             {'SSW 810': 1, 'SSW 565': 1, 'SSW 540': 1}],
                             ['11658', 'Kelly, P', 'SYEN', {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1},
                              {'SSW 810': 1, 'SSW 565': 1, 'SSW 540': 1}], ['11714', 'Morton, A', 'SYEN',
                                                                            {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1}, {'SSW 810': 1, 'SSW 565': 1, 'SSW 540': 1}],
                             ['11788', 'Fuller, E', 'SYEN', {'SYS 671': 1, 'SYS 612': 1, 'SYS 800': 1}, None]],
                            [[ele.cwid, ele.name, ele.major, dict.fromkeys(ele.required, 1) if dict.fromkeys(ele.required, 1) != {} else
                              None, dict.fromkeys(ele.electives, 1) if dict.fromkeys(ele.electives, 1) != {} else None] for ele in repo.students])

        self.assertEqual(['Einstein, A', 'Feynman, R', 'Newton, I',
                          'Hawking, S', 'Edison, A', 'Darwin, C'],
                         [ele.name for ele in repo.instructors])

        self.assertNotEqual(['Einstein,', 'Feynman, R', 'Newton, I',
                             'Hawking, S', 'Edison, A', 'Darwin, C'],
                            [ele.name for ele in repo.instructors])


if (__name__ == '__main__'):
    unittest.main(exit=False, verbosity=2)
