from flask import Flask, jsonify, abort, make_response, request
from datetime import date

app = Flask(__name__)

today = date.today()

tasks = [
    {
        'id': 1,
        'value': 22.51,
        'timestamp': today.strftime("%d/%m/%Y"),
    },
    {
        'id': 2,
        'value': 22.54,
        'timestamp': today.strftime("%d/%m/%Y"),
    }
]


@app.route('/')
def home():
    readingCount = (len(tasks))

    sum = 0
    list = [d['value'] for d in tasks]
    for num in list:
        sum = sum + num
    average = sum / readingCount

    varianceList = [i * i for i in list]
    for num in varianceList:
        sum = sum + num
    variance = sum / readingCount

    return jsonify({'reading count': readingCount,
                    'mean': average,
                    'variance': variance})


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'value' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'value': request.json['value'],
        'timestamp': today.strftime("%d/%m/%Y"),
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'value' in request.json and type(request.json['value']) != float:
        abort(400)
    task[0]['value'] = request.json.get('value', task[0]['value'])
    return jsonify({'task': task[0]})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
