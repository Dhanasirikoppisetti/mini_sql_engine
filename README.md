# Mini SQL Engine

### Overview

The Mini SQL Engine is a simplified, in-memory SQL query processor implemented in Python. This project demonstrates what happens behind the scenes when you run a SQL query on a database. By building a parser and execution engine from scratch, it provides a hands-on understanding of data processing, filtering, and aggregation logic.

The engine loads data from a CSV file and allows executing basic SQL queries interactively via a command-line interface (CLI).



### Features

- **Data Loading:** Load CSV files into memory as a list of dictionaries.  
- **SQL Parsing:** Parse `SELECT`, `FROM`, and `WHERE` clauses.  
- **Filtering:** Supports `WHERE` with operators `=`, `!=`, `>`, `<`, `>=`, `<=`.  
- **Projection:** Select all columns (`*`) or specific columns.  
- **Aggregation:** Supports `COUNT(*)` and `COUNT(column)` for row counts.  
- **Interactive CLI:** Run queries interactively, with user-friendly outputs.  
- **Error Handling:** Gracefully handles invalid queries and missing columns.  



### Setup Instructions

1. **Clone the repository:**

git clone https://github.com/Dhanasirikoppisetti/mini_sql_engine.git
cd mini_sql_engine
Ensure Python 3 is installed (Python 3.10+ recommended).

Ensure your CSV data files are in the data/ folder (e.g., data/users.csv, data/customers.csv).

### Run the CLI:

python cli.py
### Exit the CLI:

exit

### Supported SQL Grammar
The engine supports a simplified subset of SQL with the following formats:

-- Select all columns
SELECT * FROM <table>;

-- Select specific columns
SELECT <column1>, <column2> FROM <table>;

-- Filter rows with a single condition
SELECT * FROM <table> WHERE <column> <operator> <value>;

-- Count total rows
SELECT COUNT(*) FROM <table>;

-- Count non-null values in a column
SELECT COUNT(<column>) FROM <table> [WHERE <column> <operator> <value>];
Details:

<columns>: * for all columns or a comma-separated list.

<table>: CSV file name (without .csv).

<operator>: =, !=, >, <, >=, <=.

<value>: Number or string in single quotes (e.g., 'Female').

### Example Queries

-- Select all users
SELECT * FROM users;

-- Select specific columns
SELECT age, gender FROM users;

-- Filter rows
SELECT * FROM users WHERE age > 30;
SELECT user_id, email FROM customers WHERE region = 'North';

-- Count rows
SELECT COUNT(*) FROM users;

-- Count non-null values in a column
SELECT COUNT(purchased) FROM users WHERE gender = 'Female';
SELECT COUNT(loyalty_tier) FROM customers WHERE region = 'South';


### Project Structure

``` bash
mini_sql_engine/
│
├── cli.py         # CLI interface
├── engine.py      # Query execution engine
├── parser.py      # SQL parser
├── data/          # CSV files
│   ├── users.csv
│   └── customers.csv
└── README.md

```
### Notes
Only single-condition WHERE clauses are supported.

SQL keywords are case-insensitive; column names are case-insensitive in queries.

COUNT aggregation only supports COUNT(*) and COUNT(column).

Designed for educational purposes to understand SQL engine internals.

### Future Improvements
Support multiple WHERE conditions with AND/OR.

Add other aggregate functions like SUM, AVG, MIN, MAX.

Implement ORDER BY and LIMIT.

### License
This project is open-source and free to use for learning and personal projects.







