# Simple SQL engine

SQL (structured query language) is a standard way of querying a database. In
this interview we're going to write a very simple SQL engine.

Our simplified version of SQL allows you to write statements like this:

``` sql
SELECT title, author FROM library
-- This might return:
--
--  title                        |  author
-- ------------------------------+-----------------------
--  The Broken Earth Trilogy     |  N. K. Jemisin
--  Educated                     |  Tara Westover
--  Klara and the Sun            |  Kazuo Ishiguro
--  The Remains of the Day       |  Kazuo Ishiguro

SELECT title, author FROM library WHERE author = 'Kazuo Ishiguro'
--  title                        |  author
-- ------------------------------+-----------------------
--  Klara and the Sun            |  Kazuo Ishiguro
--  The Remains of the Day       |  Kazuo Ishiguro

SELECT title, author FROM library WHERE author = 'Kazuo Ishiguro' AND year > 2015
--  title                        |  author
-- ------------------------------+-----------------------
--  Klara and the Sun            |  Kazuo Ishiguro

SELECT title, author, year FROM library WHERE year > 2015 ORDER BY year, author
--  title                        |  author                |  year
-- ------------------------------+------------------------+-------
--  The Broken Earth Trilogy     |  N. K. Jemisin         |  2018
--  Educated                     |  Tara Westover         |  2018
--  Klara and the Sun            |  Kazuo Ishiguro        |  2021
```

## Goal
Our goal is to write a function that can run simple SQL statements over an
in-memory array. It should support the following sorts of queries:

    SELECT ... FROM table
    SELECT ... FROM table WHERE ... (AND ...)
    SELECT ... FROM table ORDER BY ...
    SELECT ... FROM table WHERE ... (AND ...) ORDER BY ...

In order to get you started, here's a regular expression that separates out the
parts of the query, and the `library` dataset from above. We also have support for [Javascript](https://gist.github.com/b13i/427e9385bdb7bf9c18998dbba4124a9c), [Go](https://gist.github.com/b13i/7624ebacb92007d3d38efc092a8bd854), [Java](https://gist.github.com/b13i/5e5f1e1d14de863f9c96bb6d5bc37f53), and [Ruby](https://gist.github.com/b13i/35b9924ca76fffd235b8d0740bbac862):

``` python
import re

PARSER = re.compile(r'^SELECT (.*) FROM [a-z]+(?: WHERE (.*?))?(?: ORDER BY (.*?))?$')

# Example
print(PARSER.match("SELECT a FROM library WHERE b = 1 ORDER BY c").groups())
# This prints: ('a', 'b = 1', 'c')

LIBRARY = [
    {
        'title': 'The Broken Earth Trilogy',
        'author': 'N. K. Jemisin',
        'year': 2018,
    },
    {
        'title': 'Educated',
        'author': 'Tara Westover',
        'year': 2018,
    },
    {
        'title': 'Klara and the Sun',
        'author': 'Kazuo Ishiguro',
        'year': 2021,
    },
    {
        'title': 'The Remains of the Day',
        'author': 'Kazuo Ishiguro',
        'year': 1989,
    },
]

```

Let's focus on getting something working. You can assume all the queries you're
given are valid, and it's okay to write code that's inefficient.