# Logs Analysis Project

## About the project
This is my implementation for the Logs Analysis project for the Udacity Full Stack Nanodegree (FSND) course.

We were tasked with writing complex queries to extract data from a news database to solve a series of 3 questions.

The database includes three tables:
* `authors` - includes information about the authors of articles.
* `articles` - includes the articles themselves.
* `log` - includes one entry for each time a user has accessed the site.

## Requirements
This project was developed and tested using the following:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

## Instructions:
   1. These instructions assume you have already setup Vagrant and Virtualbox.  If not, see [instructions here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).
   2. Download or clone this repository into the /vagrant directory.
   3. Download the [newsdata.sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and place it into your repo directory from step 2.
   4. Setup the news database using the following command (run from the repo directory from step 2):
   ```
   $ psql -d news -f newsdata.sql
   ```
   5. Finally, run `logs_analysis.py` using: 
   ```
   $ python3 logs_analysis.py
   ```
   6. Check the output file for the results of the queries: `output.txt`