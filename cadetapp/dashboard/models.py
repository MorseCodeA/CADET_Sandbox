from django.db import models
from django.utils import timezone

# classes below created from back-end-database.rst (D81)
# I believe we need this to store the information sent up through the back-end
class Comment(models.Model):
	primary_key = models.IntegerField()
	anon_user_id = models.IntegerField()
	text = models.TextField()
	course_id = models.IntegerField()
	instructor_id = models.IntegerField()
	timestamp = models.DateTimeField('date published')

class Course(models.Model):
	primary_key = models.IntegerField()
	department = models.CharField(max_length=50)
	program = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	section = models.FloatField('format xxx.xxx')
	year = models.PositiveSmallIntegerField('format xxxx')
	SEMESTERS = (
		('1', 'Spring'),
		('2', 'Summer'),
		('3', 'Fall'),
	)
	semester = models.CharField(max_length=1, choices=SEMESTERS)

class Instructor(models.Model):
	primary_key = models.IntegerField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

# might need for graphing?
class Result(models.Model):
	primary_key = models.IntegerField()
	query = models.TextField()
	result = models.TextField()
	timestamp = models.DateTimeField()

class Stopword(models.Model):
	primary_key = models.IntegerField()
	text = models.TextField()
