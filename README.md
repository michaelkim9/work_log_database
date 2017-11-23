# Work Log With a Database
## Terminal Application for Logging Work Into a Database

### Running the program

Use Python 3 ONLY. Python 2 will not work for this.\
To run the code, please run the following in Bash.

```bash
$ python3 work_log.py
```

To run the coverage test, please run the following in Bash. This needs to be run AFTER work_log.py is run and a SQLite database is created with some entries. It's testing functions that require a database with entries. After running work_log.py, a SQLite database will get created with the entries you give it.
```bash
$ python3 -m coverge run work_log_tests.py
$ python3 -m coverage report
```

### The Task

The CSV timesheets were a huge success but some more features are needed, including the ability for other developers to use the data without worrying about file locking or availability. The managers have also asked for a way to view time entries for each employee. Seems like a database would be a better solution than a CSV file!

Create a command line application that will allow employees to enter their name, time worked, task worked on, and general notes about the task into a database. There should be a way to add a new entry, list all entries for a particular employee, and list all entries that match a date or search term. Print a report of this information to the screen, including the date, title of task, time spent, employee, and general notes.