
---1. List the following details of each employee: e.emp_no, e.last_name, e.first_name, e.gender, s.salary from 
select e.emp_no, e.last_name, e.first_name, e.gender, s.salary 
from employees e inner join salaries s on e.emp_no= s.emp_no

---2. List employees who were hired in 1986.
select * from employees where hire_date >= '1986-01-01' and hire_date <= '1986-12-31'

---3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
select mn.emp_no, e.last_name, e.first_name, d.dept_name
from dept_manager mn inner join departments d on mn.dept_no =d.dept_no
inner join employees e on mn.emp_no = e.emp_no

---4. List the department of each employee with the following information: employee number, last name, first name, and department name.
select de.emp_no, e.last_name, e.first_name, d.dept_name 
from dept_emp de
inner join departments d on de.dept_no =d.dept_no
inner join employees e on de.emp_no = e.emp_no

---8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, count(last_name) as lcount from employees 
group by last_name 
order by lcount desc

select count(*) from employees
--5. List all employees whose first name is "Hercules" and last names begin with "B."
select * from employees where first_name ='Hercules' and last_name like 'B%'

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name
select e.emp_no, e.last_name, e.first_name, d.dept_name 
from dept_emp de
inner join departments d on de.dept_no =d.dept_no
inner join employees e on de.emp_no = e.emp_no
where d.dept_name ='Sales'

----7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name 
from dept_emp de
inner join departments d on de.dept_no =d.dept_no
inner join employees e on de.emp_no = e.emp_no
where d.dept_name ='Sales'
or d.dept_name ='Development'
