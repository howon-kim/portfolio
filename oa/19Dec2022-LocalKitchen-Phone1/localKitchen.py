# SELECT ... FROM table
import re
PARSER = re.compile(r'^SELECT (.*) FROM [a-z]+(?: WHERE (.*?))?(?: ORDER BY (.*?))?$')
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


def simpleQuery(table, query):
    # name: name of the object, query: String
    q = PARSER.match(query).groups()[0]
    qs = q.split(',')
    print(qs)
    for entity in table:
        temp = ""
        for c in qs:
            temp += entity[c]
            temp += "       "
        print(temp)


# simpleQuery(LIBRARY, title)
def simple1Query(table, query):
    select = PARSER.match(query).groups()[0]
    where = PARSER.match(query).groups()[1]


temp = ""
flag = true
if (
'Kazuo' in entity[author]:
    TRUE => whole row with select parameters.
    temp +=  entity[author]
)
else:
    flag = false

if (entity[year] > 2015):
    temp += entity[year]
else:
    flag = false

if (flag):
    print(temp)


        
def __main__():
    simpleQuery(LIBRARY, "SELECT title,author FROM library")