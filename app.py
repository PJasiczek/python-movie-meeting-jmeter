import csv
import datetime
import group
import os
import showing
from flask import Flask, request, jsonify

# Init app
app = Flask(__name__)

sh = [{

        'id': '1',
        'title': 'Kraina cudów',
        'duration': '85',
        'type': 'Dla dzieci',
        'direction': 'Dylan Brown',
        'year': 2019,
        'month': 4,
        'day': 25,
        'hour': 12,
        'minute': 35
    },
    {
        'id': '2',
        'title': 'Kraina cudów',
        'duration': '85',
        'type': 'Dla dzieci',
        'direction': 'Dylan Brown',
        'year': 2019,
        'month': 4,
        'day': 25,
        'hour': 14,
        'minute': 45
    },
    {
        'id': '3',
        'title': 'Niedobrani',
        'duration': '125',
        'type': 'Komedia',
        'direction': 'Jonathan Levine',
        'year': 2019,
        'month': 4,
        'day': 16,
        'hour': 12,
        'minute': 33
    }
]

gr = [
    {
        'name': 'Klasowe',
        'year': 2019,
        'month': 4,
        'day': 16,
        'hour': 11,
        'minute': 10,
        'show': [{
            'id': '1',
            'title': 'Kraina cudów',
            'duration': '85',
            'type': 'Dla dzieci',
            'direction': 'Dylan Brown',
            'year': 2019,
            'month': 4,
            'day': 25,
            'hour': 12,
            'minute': 35
        }
        ],
        'members': [

        ]
    }
]


@app.route('/sh/show_all', methods=['GET'])
def get_all_show():
    return jsonify({'shows': sh})


@app.route('/sh/show/<show_id>', methods=['GET'])
def get_show(show_id):
    s = [shw for shw in sh if (shw['id'] == show_id)]
    return jsonify({'show': s})


@app.route('/sh/create_show', methods=['POST'])
def create_show():
    shb = {
        'id': request.json['id'],
        'title': request.json['title'],
        'duration': request.json['duration'],
        'type': request.json['type'],
        'direction': request.json['direction'],
        'year': request.json['year'],
        'month': request.json['month'],
        'day': request.json['day'],
        'hour': request.json['hour'],
        'minute': request.json['minute']
    }

    sh.append(shb)
    return jsonify(shb)

@app.route('/sh/show/<show_id>', methods=['PUT'])
def update_show(show_id):
    s = [shw for shw in sh if (shw['id'] == show_id)]
    if 'title' in request.json:
        s[0]['title'] = request.json['title']
    if 'duration' in request.json:
        s[0]['duration'] = request.json['duration']
    if 'type' in request.json:
        s[0]['type'] = request.json['type']
    if 'direction' in request.json:
        s[0]['direction'] = request.json['direction']
    if 'year' in request.json:
        s[0]['year'] = request.json['year']
    if 'month' in request.json:
        s[0]['month'] = request.json['month']
    if 'day' in request.json:
        s[0]['day'] = request.json['day']
    if 'hour' in request.json:
        s[0]['hour'] = request.json['hour']
    if 'minute' in request.json:
        s[0]['minute'] = request.json['minute']
    return jsonify({'show': s[0]})


@app.route('/sh/show/<show_id>', methods=['DELETE'])
def delete_show(show_id):
    s = [shw for shw in sh if (shw['id'] == show_id)]
    if len(s) == 0:
        abort(404)
    sh.remove(s[0])
    return jsonify({'response': 'Success'})

@app.route('/gr/groups_all', methods=['GET'])
def get_all_groups():
    return jsonify({'groups': gr})

@app.route('/gr/groups/<group_name>', methods=['GET'])
def get_group(group_name):
    g = [grp for grp in gr if (grp['name'] == group_name)]
    return jsonify({'group': g})

@app.route('/gr/create_group', methods=['POST'])
def create_group():
    grp = {

        'name': request.json['name'],
        'year': request.json['year'],
        'month': request.json['month'],
        'day': request.json['day'],
        'hour': request.json['hour'],
        'minute': request.json['minute'],
        'show': request.json['show'],
        'members': request.json['members']
    }

    gr.append(grp)
    return jsonify(gr)

@app.route('/gr/group/<group_name>', methods=['PUT'])
def update_group(group_name):
    g = [grp for grp in gr if (grp['name'] == group_name)]
    if 'year' in request.json:
        g[0]['year'] = request.json['year']
    if 'month' in request.json:
        g[0]['month'] = request.json['month']
    if 'day' in request.json:
        g[0]['day'] = request.json['day']
    if 'hour' in request.json:
        g[0]['hour'] = request.json['hour']
    if 'minute' in request.json:
        g[0]['minute'] = request.json['minute']
    if 'show' in request.json:
        g[0]['show'] = request.json['show']
    return jsonify({'group': g[0]})


@app.route('/gr/group/<group_name>', methods=['DELETE'])
def delete_group(group_name):
    g = [grp for grp in gr if (grp['name'] == group_name)]
    if len(g) == 0:
        abort(404)
    gr.remove(g[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)