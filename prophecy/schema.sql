CREATE TABLE student(
    id INTEGER,
    student_name TEXT UNIQUE,
    PRIMARY KEY(id)
);
CREATE TABLE houses(
    id INTEGER,
    house TEXT UNIQUE,
    head TEXT UNIQUE,
    PRIMARY KEY(id)
);
CREATE TABLE assignments(
    id INTEGER,
    house_id INTEGER,
    student_id INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(house_id) REFERENCES houses(id),
    FOREIGN KEY(student_id) REFERENCES student(id)
);