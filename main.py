from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response


@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/stats')
def get_stats():
    statDict = {
        "Chicken": 0,
        "Fish": 0,
        "Vegetable": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
    }
    for student in data:
        if student['pref'] == "Chicken":
            statDict["Chicken"] += 1
        elif student['pref'] == "Fish":
            statDict["Fish"] += 1
        elif student['pref'] == "Vegetable":
            statDict['Vegetable'] += 1

        if student['programme'] == "Computer Science (Major)":
            statDict["Computer Science (Major)"] += 1
        elif student['programme'] == "Computer Science (Special)":
            statDict["Computer Science (Special)"] += 1
        elif student['programme'] == "Information Technology (Major)":
            statDict["Information Technology (Major)"] += 1
        elif student['programme'] == "Information Technology (Special)":
            statDict["Information Technology (Special)"] += 1
    return jsonify(statDict)

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)
@app.route('/subtract/<int:a>/<int:b>')
def sub(a, b):
    return str(a - b)
@app.route('/multiply/<int:a>/<int:b>')
def mult(a, b):
    return str(a * b)
@app.route('/divide/<int:a>/<int:b>')
def div(a, b):
    return str(a / b)

app.run(host='0.0.0.0', port=8080)