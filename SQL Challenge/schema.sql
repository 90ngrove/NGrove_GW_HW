DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;


CREATE TABLE departments (
  dept_no character varying(50),
  dept_name character varying(50)
);

CREATE TABLE dept_emp (
  emp_no integer,
  dept_no character varying(50),
  from_date date,
  to_date date
);

CREATE TABLE dept_manager (
  dept_no character varying(50),
  emp_no integer,
  from_date date,
  to_date date
);

CREATE TABLE employees (
    emp_no integer,
    birthdate date,
    first_name character varying(50),
	last_name character varying(50),
	gender character varying(5),
	hire_date date
);

CREATE TABLE salaries (
  emp_no integer,
  salary integer,
  from_date date,
  to_date date
);

CREATE TABLE titles (
  emp_no integer,
  title character varying(50),
  from_date date,
  to_date date
);
