# PY Student Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![CI](https://github.com/webkolog/py-student-management-system/actions/workflows/python-tests.yml/badge.svg)](https://github.com/webkolog/py-student-management-system/actions)

**Version:** 1.0

**Created Date:** 2026-09-06

**Last Updated:** 2026-09-06

**Compatibility:** Python 3.x

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

---

**PY Student Management System** is a command-line interface (CLI) application built with Python. It provides a simple, interactive menu interface to perform full CRUD operations on student records stored in a MySQL database, formatted using PrettyTable.

## Features

- **Add Student:** Insert new student records (Name, Class, Roll Number, Marks).
- **View All Students:** Render all records stored in the database in a formatted ASCII table.
- **Search Student:** Instantly query student details using their unique Roll Number.
- **Update Student:** Modify existing records (Name, Class, Marks) based on Roll Number.
- **Delete Student:** Remove student entries safely from the MySQL table.
- **Automatic Initialization:** Automatically creates the `student_db` database and `students` table if they do not exist.

## Prerequisites & Installation

Ensure you have Python 3.x and MySQL Server installed on your environment.

### 1. Clone the Repository
```bash
git clone https://github.com/webkolog/py-student-management-system.git
cd py-student-management-system

```

### 2. Install Required Dependencies

```bash
pip install mysql-connector-python prettytable

```

## Database Schema

The application manages the `students` table inside the `student_db` database:

| Field Name | Data Type | Size | Constraints |
| --- | --- | --- | --- |
| `id` | INT | - | Primary Key, Auto Increment |
| `name` | VARCHAR | 100 | NOT NULL |
| `class` | VARCHAR | 20 | - |
| `roll_no` | VARCHAR | 20 | UNIQUE |
| `marks` | INT | - | - |

## Usage

1. Open `py-student-management-system.py` and configure your MySQL credentials if necessary:
```python
conn = mysql.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD"
)

```


2. Run the application:
```bash
python py-student-management-system.py

```


3. Follow the menu prompts in your terminal:
```text
--- STUDENT MANAGEMENT SYSTEM ---
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

```



## Operations & SQL Examples

### Add Student

Executes parameterized `INSERT` query:

```sql
INSERT INTO students (name, class, roll_no, marks) VALUES ('Ali Candan', '12th', '103', 95);

```

### View Students

Fetches all rows and formats output using `PrettyTable`:

```sql
SELECT * FROM students;

```

### Search Student

Queries record by unique Roll Number:

```sql
SELECT * FROM students WHERE roll_no = '103';

```

### Update Student

Updates name, class, and marks for a target Roll Number:

```sql
UPDATE students SET name='Ali Candan', class='12th', marks=97 WHERE roll_no='103';

```

### Delete Student

Deletes the specific record:

```sql
DELETE FROM students WHERE roll_no = '103';

```

## Dependencies

* **mysql-connector-python:** Official MySQL driver for Python.
* **prettytable:** Library for generating tabular ASCII displays in CLI.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For questions or support regarding the PY Student Management System, visit [webkolog.net](http://webkolog.net) or submit an issue on GitHub.

```
