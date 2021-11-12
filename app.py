from flask import Flask,render_template
from flask import request
import pickle
import numpy as np 
import json

app = Flask(__name__)

@app.route('/')
def index():
    temp = request.args.get("temp")
    humid = request.args.get("humid")
    moist = request.args.get("moist")
    light = request.args.get("light")
    if temp != None and humid != None and moist != None and light != None :
        model = pickle.load(open('model.pkl','rb'))
        inputt = []
        i = 0
        inputt.append(temp)
        inputt.append(humid)
        inputt.append(moist)
        # inputt.append(light)
        print(inputt)
        final=[np.array(inputt)]
        b = model.predict_proba(final)
        no_disease ='{0:.{1}f}'.format(b[0][2], 2)
        blight ='{0:.{1}f}'.format(b[0][0], 2)
        mildew ='{0:.{1}f}'.format(b[0][1], 2)
        stem_gall ='{0:.{1}f}'.format(b[0][3], 2)
        dt  = {}
        dt['blight'] = (float(blight)*100)
        dt['mildew'] = (float(mildew)*100)
        dt['steam'] = (float(stem_gall)*100)
        dt['no disease'] = (float(no_disease)*100)
        to_json = json.dumps(dt)
        print(to_json)
        return str(to_json)
    else :
        return ""

@app.route('/getData')

def getData():
    return render_template('data.html') 


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=False,host='0.0.0.0')