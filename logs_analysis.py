#! /usr/bin/env python
import psycopg2

DBNAME = 'news'
question = []
query = []
type = ['views', 'views', '%']  # Used for printing result statement

# Append questions and queries to respective arrays

# Question 1
question.append('What are the most popular three articles of all time?\n')

query.append('''
SELECT ar.title, COUNT(*) AS views
FROM articles ar, log l
WHERE l.path = CONCAT('/article/',ar.slug)
AND l.status LIKE '%200%'
GROUP BY ar.title
ORDER BY views DESC
LIMIT 3;
''')

# Question 2
question.append('Who are the most popular article authors of all time?\n')

query.append('''
SELECT au.name, COUNT(*) AS views
FROM authors au, articles ar, log l
WHERE au.id = ar.author
AND l.path = CONCAT('/article/',ar.slug)
AND l.status LIKE '%200%'
GROUP BY au.name
ORDER BY views DESC
''')

# Question 3
question.append('On which days did more than 1% of requests lead to errors?\n')

query.append('''
SELECT day, percent_error
FROM (
    SELECT error.day, ROUND((error_count/total_count)*100,1) AS percent_error
    FROM
        (SELECT date(time) AS day,
            CAST(COUNT(status) AS decimal) AS error_count
        FROM log
        WHERE status LIKE '%404%'
        GROUP BY day) AS error,

        (SELECT DATE(time) AS day,
            CAST(COUNT(status) AS decimal) AS total_count
        FROM log
        GROUP BY day) AS total

    WHERE error.day = total.day
    ) AS percent
WHERE percent_error > 1.0
''')


def run_query(query):
    """ Execute the query and return the result set """
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def print_query_result(question, query, type):
    """ Pretty print the results of the executed query """
    print(question)
    res = run_query(query)
    for i in range(len(res)):
        print("\t{0} -- {1} {2}".format(res[i][0], res[i][1], type))
    print('\n')


# Loop through every query and print the results
for i in range(len(query)):
    print_query_result(question[i], query[i], type[i])
