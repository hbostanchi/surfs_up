# surfs_up


Challenge Overview
Determine key statistical data about the month of July.
Determine key statistical data about the month of December.
Compare your findings between the month of July and December.
Make 2 or 3 recommendations for further analysis.
Share your findings in the Jupyter Notebook.


Project Overview
In this module, we spent time with new tools such as SQLite, SQLAlchemy, and Flask to build on our knowledge of SQL database structures and querying methods. We, also, wrote and executed Python code in a Jupyter notebook and created graphs using Python.


Resources
Data Source: climate_analysis.ipynb, hawaii.sqlite
Software: SQLite, Flask, Python, Jupyter notebook
Dependencies: SQLAlchemy, NumPy, Pandas, Matplotlib, Datetime

Objectives
Explain the structures, interactions, and types of data of a provided dataset.
Differentiate between SQLite and PostgreSQL databases.
Use SQLAlchemy to connect to and query a SQLite database.
Use statistics like minimum, maximum, and average to analyze data.
Design a Flask application using data.
Summary
Precipitation and station analysis climate_analysis.ipynb
Using Flask, we displayed our results in a webpage app.py
app



Limitations
SQLite Advantages
While there are a few specific use cases for SQLite, we focused on how it can be beneficial to us and where we might get the most value from it. The main advantages are:

It’s local. One of the core advantages of SQLite is that it allows you to create databases locally on your computer to support testing and easy prototyping. This is beneficial, because if you want to test something out and you need a database, it’s not always the most convenient to set up a SQL database server just to try something out.
There’s an app for that. Another advantage of SQLite databases are that they can be used on a mobile phone app. Most mobile phone games will use an SQLite database to store certain information about you or your players statistics. While we won’t be creating a mobile app in this module, it’s still helpful to understand the full context. SQLite Disadvantages
SQLite also has a couple of disadvantages, however. They are:
It’s local. If you’ve used a MYSQL database before, you might have noticed that you can have multiple users access the database. With SQLite, there are no users. SQL is local: stored on one computer or phone. So, only that computer or phone will have access.
There are fewer security features: one other disadvantage to be aware of is that SQLite doesn’t have as many security features as a traditional SQL database.