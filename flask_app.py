from flask import Flask,jsonify,request

app = Flask(__name__)

data =  [
    {
        "id":1,
        "Contact":u'9987644456',
        "Name":u'Raju',
        "Done":False
    },
    {
        "id":2,
        "Contact":u'9876543222',
        "Name":u'Rahul',
        "Done":False
    }
]

@app.route("/")

def hello_world():
    return "Hello World"
@app.route("/add-data",methods = ["POST"])

def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Pls provide the data"
        },400)
    data1 = {
        "id":data[-1]['id'],
        "Name":request.json['Name'],
        "Contact":request.json.get('Contact',""),
        "Done":False
    }
    data.append(data1)
    return jsonify({
        "status":'Success',
        "message":"task added successfully"
    })
         
@app.route("/get-data")

def get_task():
    return jsonify({
        "data":data
    })


if(__name__=="__main__"):
    app.run(debug = True)
