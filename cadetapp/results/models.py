from django.db import models
from datetime import datetime
import json
import requests
import random

"""Remote Database URL data
Please add/remove/modify table access string data here.
These strings are called in the initialize(entry) functions to determines the URL
""" 
URL_DATA = {
        'db_url':'https://jsonplaceholder.typicode.com/',
        'comment_table':'comments/',
        'comm_dset_table':'comment_dataset/',
        'course_table':'albums/',               #'course/',
        'datasets_table':'datasets/',
        'instructor_table':'users/',            #'instructors/',
        'results_table':'results/',
        'res_details_table':'results_details/',
        'res_top_table':'results_topics/',
        'stop_words_table':'stop_words/',
        'topic_words_table':'todos/',            #'topic_words/',
   }      
        
class Instructor(models.Model):
        """Instructor is an individual.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        first_name - .
        last_name - .

        Functions:
        self.initialize(entry) - initializes an Instructor obj and saves it to the local database.
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        first_name=models.CharField(max_length=30,default='Joel')
        last_name=models.CharField(max_length=30,default='Coffman')

        def initialize(self,entry=-1):
                """Loads the current object with the information from instructor database.
                 Note: saves the object to the local database for later use.

                Param: entry - instructor id (PK in remote database)
                Returns: N/A
                """
                # May be a better way to build this string, but this works
                resp=requests.get(
                        URL_DATA['db_url']
                        + URL_DATA['instructor_table']
                        + str(entry))
                if resp.ok:                    # Ensures get request returned 200
                        jsonObj=resp.json()    # get JSON obj of table entry
                        try:
                                self.id=jsonObj['id']
                                self.first_name=jsonObj['name'].split()[0]
                                self.last_name=jsonObj['name'].split()[1]
                                self.save()    # Save object ot local database
                        # Attempt to fail gracefully
                        except KeyError as err:
                                print('Error: Unknown key: '+str(err))
                else:                          # Bad return from request
                        print("Unable to access table entry")
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

        Functions:
        self.initialize(entry) - initializes a Course obj and saves it to the local database.
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

        def initialize(self,entry=-1):
                """Loads the current object with the information from course database.
                 Note: saves the object to the local database for later use.

                Param: entry - course id (PK in remote database)
                Returns: N/A
                """
                # May be a better way to build this string, but this works
                resp=requests.get(
                        URL_DATA['db_url']
                        + URL_DATA['course_table']
                        + str(entry))
                if resp.ok:                    # Ensures get request returned 200
                        jsonObj=resp.json()    # get JSON obj of table entry
                        try:
                                self.id=jsonObj['id']
                                self.name=jsonObj['title']
                                #self.year=jsonObj['column_name']
                                #self.program=jsonObj['column_name']
                                random.seed()
                                self.modality=random.randint(0,3)
                                self.num_sect=jsonObj['userId']
                                self.save()
                        # Attempt to fail gracefully
                        except KeyError as err:
                                print('Error: Unknown key: '+str(err))
                else:                          # Bad return from request
                        print("Unable to access table entry")
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

        Functions:
        self.initialize(entry) - initializes a Course obj and saves it to the local database.
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

        def initialize(self,entry=-1):
                """Loads the current object with the information from course database.
                 Note: saves the object to the local database for later use.

                Param: entry - course id (PK in remote database)
                Returns: N/A
                """
                # May be a better way to build this string, but this works
                resp=requests.get(
                        URL_DATA['db_url']
                        + URL_DATA['comment_table']
                        + str(entry))
                if resp.ok:                    # Ensures get request returned 200
                        jsonObj=resp.json()    # get JSON obj of table entry
                        try:                        
                                self.id=jsonObj['id']
                                # Get course FK. If DNE, initialize the course 
                                courseID=jsonObj['postId']
                                if not Course.objects.filter(id=courseID):
                                        Course().initialize(courseID)
                                self.course_id=courseID
                                
                                # Get instructor FK. If DNE, initialize the instructor
                                instructorID=jsonObj['postId']
                                if not Instructor.objects.filter(id=instructorID):
                                        Instructor().initialize(instructorID)
                                self.instructor_id=instructorID

                                self.c_comm=jsonObj['name']
                                self.i_comm=jsonObj['email']
                                self.a_comm=jsonObj['body']
                                #self.timestamp=jsonObj['column_name']
                                random.seed()
                                self.anon_id=random.ranint(0,1000)
                                self.tone=random.randint(-1,1)
                                self.topic=random.randint(0,100)
                                self.save()
                        # Attempt to fail gracefully
                        except KeyError as err:
                                print('Error: Unknown key: '+str(err))
                else:                          # Bad return from request
                        print("Unable to access table entry")
#END class Comment


class Topic_Words(models.Model):
        """Topic Words is a set of words that constitue a topic.
        Attributes:
        id - identifier (PK,integer) in both local and remote databases.
        topic_id = .
        word = .

        Functions:
        self.initialize(entry) - initializes a TopicWord obj and saves it to the local database.
        """        
        id=models.IntegerField(primary_key=True,unique=True,default=-1)
        topic_id=models.IntegerField(default=-1)
        words=models.CharField(max_length=30,default='kittens')

        def initialize(self,entry=-1):
                """Loads the current object with the information from course database.
                 Note: saves the object to the local database for later use.

                Param: entry - id (PK in remote database)
                Returns: N/A
                """
                # May be a better way to build this string, but this works
                resp=requests.get(
                        URL_DATA['db_url']
                        + URL_DATA['topic_words_table']
                        + str(entry))
                if resp.ok:                    # Ensures get request returned 200
                        jsonObj=resp.json()    # get JSON obj of table entry
                        try:                                
                                self.id=jsonObj['id']
                                self.topic_id=jsonObj['userId']
                                self.words=jsonObj['title']
                                self.save()
                        # Attempt to fail gracefully
                        except KeyError as err:
                                print('Error: Unknown key: '+str(err))
                else:                          # Bad return from request
                        print("Unable to access table entry")
#END class Topic_Words


