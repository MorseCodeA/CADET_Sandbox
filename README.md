# CADET_Sandbox
Python 3.4, Django 1.11

A text repo to put all of our CADET Django code before we push it to Phabricator. 

## I. Set Up: Project Installation 

1. Installation: Cloning the Project  
- clone the project repo, cd into root directory  
- make sure you use virtualenv    

```bash
git clone https://github.com/AshleyMorse/CADET_Sandbox  
cd CADET_Sandbox 
```

### 2. Virtual Environment (optional, but highly recommended)

A. General virtualenv 
```bash 
# run virtualenv with python3, you can name your environment whatever. This example, we call it *cadetenv*.  
python -m venv cadetenv   
```  
If running virtual env command gives you an error, you might either have anaconda installed, which you need to follow [this setup](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/).  

Mac and Ubuntu users might also run into installation error if pyenv is broken [broken pyenv](https://stackoverflow.com/questions/26215790/venv-doesnt-create-activate-script-python3) so add this modifier to the same command:   
```bash
python -m venv cadetenv --without-pip 
```

### B. With Anaconda
If not using virtualenv and has anaconda installation use this:
```bash   
conda create -n my-dev python=3.4
source activate my-dev
```

The set up will automatically add pip and django packages.  Skip Step II: Django Installation.

## II. Set Up: Django Installation  

```bash
# upgrade pip
pip install --upgrade pip

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

# run server,
python manage.py runserver
```

### IV. Front-End Development Set Up

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
gulp to compile and minify all js and sass files in teh assets directory
gulp

```







