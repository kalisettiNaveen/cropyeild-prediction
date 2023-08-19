from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model1 = pickle.load(open('model1.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))
model3 = pickle.load(open('model3.pkl', 'rb'))
model4 = pickle.load(open('model4.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['time']
    arr = np.array([val1])
    arr = arr.astype(np.float64)
    pred1 = model1.predict([arr])
    pred2 = model2.predict([arr])
    pred3 = model3.predict([arr])
    pred4 = model4.predict([arr])
    return render_template('index.html', data1=float(pred1),data2=float(pred2),data3=float(pred3),data4=float(pred4))

if __name__ == '__main__':
    app.run(debug=True)