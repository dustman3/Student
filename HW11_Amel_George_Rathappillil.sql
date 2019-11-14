
select instructors.Name
from instructors
where CWID = '98763';

select dept, count(*)
from instructors
group by Dept;

select grades.Grade, count(*) as max_Grade
from grades
group by grades.Grade
order by max_Grade desc
limit 1;

select Name, CWID, Major, Course, Grade
from students
join grades
on students.CWID = grades.StudentCWID
where grades.Course = 'SSW 810';

select instructors.CWID, instructors.Name, instructors.Dept
, grades.Course, count(*) as Students
from instructors
join grades
on instructors.CWID = grades.InstructorCWID
group by grades.InstructorCWID,
         grades.Course
order by Students desc;
