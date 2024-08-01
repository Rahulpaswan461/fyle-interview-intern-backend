from flask import Flask, request, jsonify
app = Flask(__name__)

# Assuming you have a database setup
from your_database_module import get_all_teachers, get_all_assignments, grade_assignment

@app.route('/principal/teachers', methods=['GET'])
def list_teachers():
    teachers = get_all_teachers()
    return jsonify({"data": teachers})

@app.route('/principal/assignments', methods=['GET'])
def list_assignments():
    assignments = get_all_assignments()
    return jsonify({"data": assignments})

@app.route('/principal/assignments/grade', methods=['POST'])
def regrade_assignment():
    data = request.json
    assignment_id = data['id']
    grade = data['grade']
    result = grade_assignment(assignment_id, grade)
    return jsonify({"data": result})
