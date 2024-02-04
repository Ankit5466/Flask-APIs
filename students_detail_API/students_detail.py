from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {'id':1, 'name':'Ankit', 'marks':90, 'address':'DLW'},
    {'id':2, 'name':'Anuj', 'marks':92, 'address':'88-b Noida'},
    {'id':3, 'name':'shubham', 'marks': 95, 'address':'77-A DLW'},
    {'id':4, 'name':'Rohan', 'marks':80, 'address':'Varanasi'},
    {'id':5, 'name':'Monu', 'marks':34, 'address':'121-D delhi'}
]

@app.route("/students", methods=['GET'])
def get_students():
    return jsonify(students)

@app.route("/students/<int:id>", methods=['GET'])
def get_student_by_id(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student)
    return jsonify({'error':'students not found'}), 404

@app.route("/students/add-student", methods=['POST'])
def add_student():
    data = request.json
    if 'id' not in data or 'name' not in data or 'marks' not in data or 'address' not in data:
        return jsonify({'error':'Invalid data, enter correct fields'}), 400

    new_id = int(data['id'])
    for student in students:
        if student['id'] == new_id:
            return jsonify({'error':'id already exist, add new student'}), 400

    new_student = {'id': new_id, 'name':data['name'], 'marks':data['marks'], 'address':data['address']}
    students.append(new_student)
    return jsonify({'message':'Student added succesfully'}), 201

@app.route("/students/update/<int:id>", methods=['PUT'])
def update_student(id):
    data = request.json
    if 'name' not in data or 'marks' not in data or 'address' not in data:
        return jsonify({'error':'invalid data, enter all field'}), 400

    for student in students:
        if student['id'] == id:
            student['name'] = data['name']
            student['marks'] = data['marks']
            student['address'] = data['address']
            return jsonify({'message':'student updated successfully'}), 201

    return jsonify({'error':'student not found'}), 404

@app.route("/students/delete/<int:id>", methods=['DELETE'])
def delete_students(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify({'message':'Student deleted successfuly'}), 200

    return jsonify({'error':'Student not found'}), 404


app.run(debug=True)