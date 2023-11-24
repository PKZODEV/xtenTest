querySalary = [
{'name': 'James', 'salary': 25000},
{'name': 'John', 'salary': 15000},
{'name': 'Mark', 'salary': 40000},
{'name': 'Emma', 'salary': 38000},
{'name': 'Max', 'salary': 27000},
{'name': 'Scott', 'salary': 32000}
]

queryExp = [
{'name': 'emma', 'exp': 55}, 
{'name': 'max', 'exp': 32},
{'name': 'james', 'exp': 63},
{'name': 'john', 'exp': 9},
{'name': 'mark', 'exp': 49},
{'name': 'scott', 'exp': 74}
]

queryGrade = [
{'name': 'James Wilson', 'grade': 'D'}, 
{'name': 'John Gatlin', 'grade': 'B'},
{'name': 'Scott Madison', 'grade': 'A'},
{'name': 'Mark Gray', 'grade': 'C'}, 
{'name': 'Max Raven', 'grade': 'B'},
{'name': 'Emma Ford', 'grade': 'B'}, 
]

salary = {
    i['name'].lower(): i['salary'] 
    for i in querySalary
}
exp = {
    i['name'].lower(): i['exp'] 
    for i in queryExp
}
grade_values = {'A': 3, 'B': 2.5, 'C': 2, 'D': 1.5}
grade = {
    i['name'].lower().split()[0]: 
    grade_values.get(i['grade']) 
    for i in queryGrade
}

Result = []
for name in salary.keys():
    Salary = salary.get(name)
    Exp = exp.get(name)
    Grade = grade.get(name)

    if Exp < 1:
        multiply = 1.5
    elif 1 <= Exp < 3:
        multiply = 2
    elif 3 <= Exp < 5:
        multiply = 2.5
    else:
        multiply = 3

    bonus = Salary * multiply * Grade
    Result.append({'name': name, 'bonus': int(bonus)})

for i in Result:
    print(str(i))