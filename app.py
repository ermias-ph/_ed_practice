from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBs = [
  {
    'id': 1,
    'title': 'Web devloper',
    'location': 'Addis Ababa',
    'salary': 'Birr.40,000'
  },
  {
    'id': 2,
    'title': 'UI/UX Developer',
    'location': 'Remote',
    'salary': 'Negotiable'
  },
  {
    'id': 3,
    'title': 'Data Science',
    'location': 'Dire Dawa',
    'salary': 'Birr.100,000'
  },
  {
    'id': 4,
    'title': 'Frontend Developer',
    'location': 'Remote',
    'salary': 'Birr.75,000'
  }
]

@app.route('/')


def hello_world():
  return render_template('home.html',
                        jobs=JOBs)

@app.route('/api/jobs')

def list_jobs():
  return jsonify(JOBs)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  