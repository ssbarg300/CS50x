from cs50 import SQL
import csv

db = SQL("sqlite:///roster.db")

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            db.execute("INSERT INTO student (student_name) VALUES(?)", row["student_name"])
            db.execute("INSERT INTO houses (house, head) VALUES(?, ?)", row["house"], row["head"])
        except ValueError:
            continue
    # store houses names and id's
    houses = db.execute("SELECT id, house FROM houses;")
    # store student id's and house
    students = db.execute("SELECT id, house FROM students;")
    # empty dictionary formatted:{house name: {id}}
    houses_key = {}

    # Loop over all houses and store id.
    for house in houses:
        houses_key[house['house']] = house['id']

    for student in students:
        fhk = houses_key[student['house']]
        fstdk = student['id']
        db.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?)", fstdk, fhk)


"""
SELECT student.student_name, houses.house FROM assignments JOIN student ON student.id = assignments.student_id JOIN houses ON houses.id = assignments.house_id;
"""

# REMEMBER THIS ^ SQL QUERY



