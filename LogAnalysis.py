#!/usr/bin/env python3
# Log Analysis for News Database
# Johnny Mendoza - JohnnyMendoza@gmail.com


import psycopg2


# Database Query: What are the most popular three articles of all time?


sql_articles_popular = (
    "SELECT articles.title, "
    "count(*) as views "
    "FROM log, articles "
    "WHERE log.status LIKE '%200%' "
    "and articles.slug = substr(log.path, 10) "
    "GROUP by articles.title "
    "ORDER by views desc "
    "limit 3")


# Database Query: Who are the most popular article authors of all time?


sql_authors_popular = (
    "SELECT authors.name, "
    "count(*) as views "
    "FROM articles, authors, log "
    "WHERE log.status LIKE '%200%' "
    "and authors.id = articles.author "
    "and articles.slug = substr(log.path, 10) "
    "GROUP by authors.name "
    "ORDER by views desc")


# Database Query: On which day did more than 1% of requests lead to errors?


sql_error_requests = (
    "SELECT day, perc FROM "
    "(SELECT day, round((sum(requests)/(SELECT count(*) "
    "FROM log WHERE substring(cast(log.time AS text), "
    "0, 11) = day) * 100), 2) "
    "AS perc FROM (SELECT substring(cast(log.time AS text), 0, 11) "
    "AS day, count(*) "
    "AS requests FROM log "
    "WHERE status LIKE '%404%' "
    "GROUP BY day)"
    "AS log_percentage "
    "GROUP BY day ORDER BY perc DESC) "
    "AS final_query "
    "WHERE perc >= 1")


# Connect to the database and create cursor


def connect(sql_request):
    try:
        conn = psycopg2.connect(database="news")
        cursor = conn.cursor()
        cursor.execute(sql_request)
        results = cursor.fetchall()
        conn.close()
        return results
    except:
        print ("Cannot connect to the database")


# Format the title of each section


def print_title(title):
    print ("\n\t" + title + "\n")


# Print popular articles query results


def print_articles():
    print_articles = connect(sql_articles_popular)
    print_title("Most Popular Three Articles of All Time")
    for title, num in print_articles:
        print ("\t {} - {} views".format(title, num))


# Print popular author query results


def print_authors():
    print_authors = connect(sql_authors_popular)
    print_title("Most Popular Authors of All Time")
    for name, num in print_authors:
        print("\t {} - {} views".format(name, num))


# Print more than 1% errors query results


def print_errors():
    print_errors = connect(sql_error_requests)
    print_title("Days with more than one percentage of bad requests")
    for results in print_errors:
        print ("\t", results[0], "-", str(results[1]) + "% errors")


# Print final output


if __name__ == '__main__':
    print_articles()
    print_authors()
    print_errors()
