from flask import Flask, jsonify,request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos',methods=['GET'])
def hello_world():
    return  jsonify(todos),200

@app.route('/todos',methods=['POST'])
def add_new_todo():

  data = json.loads(request.data)
  print(data)
  todos.append(data)
  return  jsonify(todos),201

@app.route('/todos/<int:id>',methods=['DElETE'])
def delete_todo(id):
  todos.pop(id)
  
  return  jsonify(todos),200



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
