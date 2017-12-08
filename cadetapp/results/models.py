from django.db import models
from datetime import datetime
import json
import requests
import random
        
class Instructor(models.Model):
        """Instructor is an individual.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        first_name - .
        last_name - .
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        first_name=models.CharField(max_length=30,default='Joel')
        last_name=models.CharField(max_length=30,default='Coffman')
# END class Instructor
        
class Course(models.Model):
        """Course is an class being offered.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        name - course title.
        year - year of course offering.
        program - discipline to which this cource belongs.
        modality - .
        num_sect - number of individual course sections
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        name=models.CharField(
                max_length=30,
                default='Fundamentals of Software Engineering')
        year=models.IntegerField(default=datetime.now().year)
        program=models.CharField(
                max_length=30,
                default='Comp Sci')
        MODALITY=(
                (0,'Unknown'),
                (1,'Spring'),
                (2,'Summer'),
                (3,'Fall')
        )
        modality=models.IntegerField(
                choices=MODALITY,
                default=0)
        num_sect=models.IntegerField(default=0)
# END class Course
                        
class Comment(models.Model):
        """Comment is a part of a processed, submitted review.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        anon_id - Anonymized user ID of submitter.
        course - course (FK,integer) to which this comment belongs.
        instrcutor - instructor (FW,integer) to which this comment belongs.
        c_comm - course comment text
        i_comm - instrcutor comment text
        a_comm - .
        timestamp - comment post time
        tone - tone of the comment
        topic_id = .
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        anon_id=models.IntegerField(default=-1)
        course=models.ForeignKey(
                Course,
                on_delete=models.CASCADE)
        instructor=models.ForeignKey(
                Instructor,
                on_delete=models.CASCADE)
        c_comm=models.TextField(default='N/A')
        i_comm=models.TextField(default='N/A')
        a_comm=models.TextField(default='N/A')
        timestamp=models.DateTimeField(auto_now=True)
        TONES=(
                (1, 'positive'),
                (0, 'neutral'),
                (-1, 'negative')
        )
        tone = models.IntegerField(choices=TONES,default=0)
        topic = models.IntegerField(default=0)
#END class Comment

class Topic_Words(models.Model):
        """Topic Words is a set of words that constitue a topic.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        topic_id = .
        word = .
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        topic_id=models.IntegerField(default=-1)
        words=models.CharField(max_length=30,default='kittens')

#END class Topic_Words

class Results_Details(models.Model):
        """Results_Details correlates a comment to a topic ID.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        topic_id - topic (FK, integer) related to this result
        comment_id - comment (FK,integer) realted to this result
        course_com_sent - .
        instr_com_sent - .
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        topic=models.ForeignKey(
                Topic_Words,
                on_delete=models.CASCADE)
        comment=models.ForeignKey(
                Comment,
                on_delete=models.CASCADE)
        COMMENT_STAT=(
                (0, 'no comment'),
                (1, 'comment valid'),
        )
        course_comm_sent = models.IntegerField(choices=COMMENT_STAT,default=0)
        instr_comm_sent = models.IntegerField(choices=COMMENT_STAT,default=0)
#END class Results_Details

class Results(models.Model):
        """Results are the output of the NLTK processing
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        num_topics
        words_per_topic
        iterations
        stop_words
        timestamp
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        num_topics=models.IntegerField(default=1)
        words_per_topic=models.IntegerField(default=2)
        iterations=models.IntegerField(default=3)
        stop_words=models.IntegerField(default=4)
        timestamp=models.DateTimeField(auto_now=True)
#END class Results

class Results_Topic(models.Model):
        """Results_Topics does something, but I do not know what
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        results_id - 
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        results=models.ForeignKey(
                Results,
                on_delete=models.CASCADE)        
#END class Results_Details
