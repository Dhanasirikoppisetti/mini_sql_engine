
# Mini SQL Engine

### Overview

The Mini SQL Engine is a simplified, in-memory SQL query processor implemented in Python. This project demonstrates what happens behind the scenes when you run a SQL query on a database. By building a parser and execution engine from scratch, it provides a hands-on understanding of data processing, filtering, and aggregation logic.

The engine loads data from a CSV file and allows executing basic SQL queries interactively via a command-line interface (CLI).

### Features

Data Loading: Load CSV files into memory as a list of dictionaries.

SQL Parsing: Parse SELECT, FROM, and WHERE clauses.

Filtering: Supports WHERE with operators =, !=, >, <, >=, <=.

Projection: Select all columns (*) or specific columns.

Aggregation: Supports COUNT(*) and COUNT(column) for row counts.

Interactive CLI: Run queries interactively, with user-friendly outputs.

Error Handling: Gracefully handles invalid queries and missing columns.

### Supported SQL Grammar

The engine supports a simplified subset of SQL:

SELECT <columns> FROM <table> [WHERE <column> <operator> <value>];
SELECT COUNT(*) FROM <table> [WHERE <column> <operator> <value>];
SELECT COUNT(<column>) FROM <table> [WHERE <column> <operator> <value>];


<columns>: * for all columns or a comma-separated list of column names.

<table>: The CSV file name (without extension).

<operator>: =, !=, >, <, >=, <=.

<value>: A number or a string in single quotes (e.g., 'Female').

### Usage

Clone the repository and navigate to the folder:

git clone <your-repo-url>
cd mini_sql_engine


Ensure your CSV data file is in the data/ folder. Example: data/users.csv.

### Run the CLI:

python cli.py


### Example Queries:

-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT age, gender FROM users;

-- Filter rows
SELECT * FROM users WHERE age > 30;

-- Count rows
SELECT COUNT(*) FROM users;

-- Count non-null values in a column
SELECT COUNT(purchased) FROM users WHERE gender = 'Female';


### Exit the CLI:

exit

### Project Structure
mini_sql_engine/
│
├── cli.py         
├── engine.py       
├── parser.py       
├── data/
│   └── users.csv   
└── README.md       

### Notes

Only single-condition WHERE clauses are supported.

SQL queries are case-insensitive for column names.

COUNT aggregation only supports COUNT(*) and COUNT(column).

Designed for educational purposes and learning how SQL engines work under the hood.

### Future Improvements

Support multiple WHERE conditions with AND/OR.

Add other aggregate functions like SUM, AVG, MIN, MAX.

Implement ORDER BY and LIMIT.

### License

This project is open-source and free to use for learning and personal projects.