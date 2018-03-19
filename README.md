# Logs Analysis Project

## About the project
This is my implementation for the Logs Analysis project for the Udacity Full Stack Nanodegree (FSND) course.

We were tasked with writing complex queries to extract data from a news database to solve a series of 3 questions:
  1. What are the most popular three articles of all time? 
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

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
   
  1. Download and install Python.
  2. Download and install VirtualBox following the instructions on the site.
  3. Download and install Vagrant following the instructions on the site.
  4. Download or clone this repository into the /vagrant directory.
  5. Download the [newsdata.sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and place it into your repo directory from step 2.
  6. Run `vagrant up` from the repo directory.  This may take a few minutes.
  7. Run `vagrant ssh` from the repo directory.
  8. Setup the news database using the following command (run from the repo directory from step 2):
  ```
  $ psql -d news -f newsdata.sql
  ```
  9. Finally, run `logs_analysis.py` using: 
  ```
  $ python3 logs_analysis.py
  ```
  10. Check the output file for the results of the queries: `output.txt`
