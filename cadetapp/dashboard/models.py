from django.db import models
from django.utils import timezone

# make default values for everything here
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
	# An instructor can tach many courses, and a course can be
	# taught by many instructors
	courses = models.ManyToManyField(Course)

# might need for graphing?
class Result(models.Model):
	primary_key = models.IntegerField()
	query = models.TextField()
	result = models.TextField()
	timestamp = models.DateTimeField()

class Stopword(models.Model):
	primary_key = models.IntegerField()
	text = models.TextField()

# topics can have many comments
class Topic(models.Model):
	topic_id = models.PositiveSmallIntegerField('a number between 1-5')

# classes below created from back-end-database.rst (D81)
# I believe we need this to store the information sent up through the back-end
class Comment(models.Model):
	primary_key = models.IntegerField()
	anon_user_id = models.IntegerField()
	TONES = (
		('pos', 'positive'),
		('neu', 'neutral'),
		('neg', 'negative')
	)
	tone = models.CharField(max_length=3, choices=TONES)
	text = models.TextField()
	# many comments belong to one course
	course = models.ForeignKey(
		Course,
		on_delete=models.CASCADE)
	# many comments belong to one topic
	topic = models.ForeignKey(
		Topic,
		on_delete=models.CASCADE)
	instructor_id = models.IntegerField()
	timestamp = models.DateTimeField('date published')
