from wsgiref import simple_server
from flask import Flask, request,render_template
from flask import Response
from flask_cors import CORS
from flask_cors import cross_origin
from logistic_deploy import predObj
import numpy as np

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


class ClientApi:

    def __init__(self):
        self.predObj = predObj()
        print('Here 3')

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():

    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        print('Here 4')

        #if request.json['data'] is not None:
        pregnancies = float(request.form['Pregnancies'])
        glucose = float(request.form['Glucose'])
        bp = float(request.form['BloodPressure'])
        skin_thickness = float(request.form['SkinThickness'])
        insulin = float(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        diabetes_pedigree_function = float(request.form['DiabetesPedigreeFunction'])
        age = float(request.form['Age'])
        print('Here 5')
        # data = request.json['data']
        data = {'pregnancies':pregnancies,'glucose':glucose,'bp':bp,
                'skin_thickness':skin_thickness,'insulin':insulin,
                'bmi':bmi,'diabetes_pedigree_function':diabetes_pedigree_function,'age':age}
        print('data is:     ', data)
        pred=predObj()
        res = pred.predict_log(data)

        #result = clntApp.predObj.predict_log(data)
        print('result is        ',res)
        return render_template('results.html',result=res)
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)


if __name__ == "__main__":
    #print('Here 1')
    clntApp = ClientApi()
    #print('Here 2')
    # host = '0.0.0.0'
    # port = 5000
    app.run(debug=True)
    # httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    # httpd.serve_forever()