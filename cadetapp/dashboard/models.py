from django.db import models
from django.utils import timezone

##################################################
####              Latest Update               ####
##################################################
# Due to time constraints and complexity, this file's intended use was not 
# actualized. Originally, this file or results/models.py was intended to be 
# the file where data from the back end would be orgalized by classes and 
# functions. Since the front end expects a JSON from the back end, it was 
# easier to take the JSON, feed it into one model in results/models.py, and 
# parse it to retrieve data, rather than parsing it and fitting it in the 
# models below or in results/models.py.

# This file will organize the data retrieved from the data layer after it has 
# been analyzed. 
#class Instructor(models.Model):
#	first_name = models.CharField(max_length=30)
#	last_name = models.CharField(max_length=30)

#class Course(models.Model):
#	name = models.CharField(max_length=50)
#	year = models.PositiveSmallIntegerField()
#	SEMESTERS = (
#		('1', 'Spring'),
#		('2', 'Summer'),
#		('3', 'Fall'),
#	)
#	semester = models.CharField(max_length=1, choices=SEMESTERS)

#class Comment(models.Model):
#	# Topic of Instructor comment?
#	TYPES = (
#		('0', 'instructor'),
#		('1', 'topic')
#	)
#	type_of_comm = models.CharField(max_length=1, choices=TYPES)
#	# many comments belong to one instructor
#	instructor = models.ForeignKey(
#		Instructor,
#		on_delete=models.CASCADE)
#	# many comments belong to one course
#	course = models.ForeignKey(
#		Course,
#		on_delete=models.CASCADE)
#	# what the comment says
#	text = models.TextField()
#	# what is the sentiment?
#	TONES = (
#		('pos', 'positive'),
#		('neu', 'neutral'),
#		('neg', 'negative')
#	)
#	tone = models.CharField(max_length=3, choices=TONES)
#	# Topic ID
#	topic_id = models.IntegerField()

#class Topic(models.Model):
#	topic_id = models.IntegerField()
#	# many topics belong to one comment
#	comment = models.ForeignKey(
#		Comment,
#		on_delete=models.CASCADE)
#	text = models.TextField()
