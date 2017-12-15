#### CADET Front End Developer Guide ####
Python 3.4, Django 1.11

A guide to help developers install and run the front end of CADET.

## I. Set Up: Project Installation 

1. Installation: Cloning the Project  
- clone the project repo, cd into root directory  
- make sure you use virtualenv    

```bash
git clone ssh://git@web4.jhuep.com:2222/diffusion/CADET/cadet.git  
cd cadet/src/front-end
```

### A. Virtual Environment (optional, but highly recommended)

A. General virtualenv

```bash 
# run virtualenv with python3, you can name your environment whatever. This
# example, we call it *cadetenv*.
python -m venv cadetenv   
```  
If running virtual env command gives you an error, you might either have 
anaconda installed, which you need to follow[this setup:]
(https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/).

Mac and Ubuntu users might also run into installation error if pyenv is
broken, then add this modifier to the same command:

```bash
python -m venv cadetenv --without-pip 
```

### B. With Anaconda
If not using virtualenv and has anaconda installation use this:
```bash   
conda create -n my-dev python=3.4
source activate my-dev
```

The set up will automatically add pip and django packages.  
Skip Step II: Django Installation.

## II. Set Up: Django Installation  

```bash
# upgrade pip
pip install --upgrade pip
- Make sure you are running pip +3.0, it might be necessary to enter 'pip3'

# install django 
pip install django~=1.10.0 

# activate virtualenv  
source cadetenv/bin/activate  

# upgrade django
sudo pip install django --upgrade 
```

### III. Activate Django App

```bash
#install dependencies
pip install -r requirements.txt

# migrate database, default is sqlite
python manage.py migrate 

# Run this when you first begin
python manage.py migrate --run-syncdb

# run server
python manage.py runserver

# run to ensure that results URL is working
127.0.0.1:8000/results/test

# website homepage
127.0.0.1:8000/dashboard
```

#### Common Issues in the Installation Steps  

Make sure you're using python +3.0! You may need to run 'python3' instead 
of 'python' for commands.

#### You need these libraries installed in order to run our Django Cadet:

```bash
# notice we install with pip3 not pip
pip3 install djangorestframework

# node for setting up node modules
sudo apt-get install npm

# d3 library
pip3 install django-nvd3

# JSONField libary
pip3 install jsonfield

# Polling library
pip3 install polling
```

## Removing/Repopulating the Database if Needed
1. 'cd cadet/src/front-end/cadetapp'
2. remove '/migrations' folder in app you want to clear
- for example 'rm -r /results/migrations'
3. 'rm db.sqlite3'
4. 'python manage.py makemigrations "app_name"' 
5. 'pythom manage.py migrate'

### IV. Running Test Suites
Install dependencies

```bash
pip install coverage==3.6
pip install selenium==2.33.0
```

#### To run test suite, use this command:

```bash
coverage run manage.py test [name of subapp]

# example, running dashboard/tests.py would be
coverage run manage.py test dashboard
```

### V. Front-End Development Set Up

This section is for future front-end developers who wishes to modify the HTML,
CSS, and JS of the project.

We are using Gulp as a taskrunner to autocompile JS and CSS assets.  Two files
Gulpfile.js and package.json lists all dependencies and configuration.  In
order to set up gulp to your local environment, you must have node.js set up.
Run these commands:

```bash
# node will search for package.json file and install dependencies
npm init
# this command finds the Gulpfile.js and run all tasks there, mostly it tells 
# gulp to compile and minify all js and sass files in teh assets directory
gulp
```

### Errors and Commented Out Code
There are some errors including that we did not use the full functionality of 
stop words, URL redirecting errors, and file uploads errors where the upload 
options are not fully visible.

There is also commented out code in results/models.py and dashboard/models.py 
where models caould be used to store the data layer results instead of just 
passing it on through to the charts. This was would be more organized and 
allow the user to manipulate the data in better.

### Test Plan
Run Back end code: 
First run data layer's code, which is './install.sh' then ./start.sh' 
in the /cadet/Datalayer folder. 

Run Front end code:
In the /cadet/src/front-end/cadet, run 'python manage.py migrate' then 
'python manage.py runserver'. Go to 127.0.0.1:8000 to view our home page. 
To upload a file and view it, go to 'Upload' tab and select the csv file 
under /media/downloads to submit. This will redirect you to an Upload 
Options page. If you do not see the file name in the first tab, please 
restart the server and submit the same file again (bug). If you are 
redirected to a very long URL, just remove the '/dashboard' part that 
repeats at the end (bug). On the Upload Options page, enter your 
parameters and upload the file to the database (there should be a 
confirmation on the page and on the data layer terminal).

This will redirect you to the topics distribution charts. The charts 
represent the number of positive, neutral, and negative comments per 
topic and instructors for the topic and instructors page respectively.
The topics page the list of sentiment words per topic taken from the 
data layer. It was meant for the instructor names to appear, but the 
JSON we recieved did not have those name fields. We compensated by 
nameing each instructor 'instructor 1', 'instructor 2', etc. 

If you would like to adjust the upload options, please go to the upload 
page first, then the upload option page, otherwise you may not see 
anything there (bug).

Going to the Documents tab will show all of the documentation.

There is currently no page for Export or Team.

Going to the GitHub page will redirect you to our GitHub.

# Resources:

[Ready to use Structure for Django Tests](https://dezoito.github.io/2015/09/21/how-to-test-django-applications_pt1.html)
[Testing in Django Part 1 - Best Practices](https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/)
[Django Docs - Testing Tools](https://docs.djangoproject.com/en/2.0/topics/testing/tools/)



