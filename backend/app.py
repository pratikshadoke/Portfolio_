from flask import Flask, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# @app.route('/api/work-experience')
# def work_experience():
#     work_data = [
#         {"role": "DevOps Engineer", "company": "ABC Corp", "duration": "2022 - Present"},
#         {"role": "Intern", "company": "XYZ Ltd", "duration": "2021 - 2022"}
#     ]
#     return jsonify(work_data)
# @app.route('/api/work-experience', methods=['GET'])
# def get_projects():
#     # Read the porjects.json file
#     with open('projects.json') as f:
#         work_data = json.load(f)
#     return jsonify(work_data)
@app.route('/api/work-experience', methods=['GET'])
def get_work_experience():
    try:
        with open('projects1.json') as f:
            work_experience_data = json.load(f)
        return jsonify(work_experience_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/api/personal-projects', methods=['GET'])
def get_p_projects():
    try:
        with open('personal_projects.json') as f:
            personal_projects_data = json.load(f)
        return jsonify(personal_projects_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500        
@app.route('/api/skills', methods=['GET'])
def get_skills():
    # Read the skills.json file
    with open('skills.json') as f:
        skills_data = json.load(f)
    return jsonify(skills_data)
@app.route('/api/data', methods=['GET'])
def get_data():
    resume_data = {
        "resume": "Pratiksha_Doke_Resume.pdf"
    }
    return jsonify(resume_data)
if __name__ == '__main__':
    app.run(debug=True)
