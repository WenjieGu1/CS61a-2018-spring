.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number 
  from students as a, students_pt1 as b
  where a.date=b.date and a.color=b.color and a.pet=b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven from students as a, checkboxes as b
  where a.time=b.time and a.number=7 and b.'7'='true';

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, count(*)as count from students_pt1
  group by number order by count desc limit 1;


CREATE TABLE fa17favpets AS
  SELECT pet, count(*)as count from students_pt1
  group by pet order by count desc limit 10;


CREATE TABLE sp18favpets AS
  SELECT pet, count(*)as count from students
  group by pet order by count desc limit 10;


CREATE TABLE sp18dog AS
  SELECT pet, count(*) from students where pet='dog';


CREATE TABLE sp18alldogs AS
  SELECT 'dog', count(*) from students
   WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, count(*) as count
  from students 
  where seven='7' 
  group by denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*)
  from students
  group by smallest
  order by smallest;
