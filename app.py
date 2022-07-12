from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_dt.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age, systolicbp, diastolicbp, bs, bodytemp, heartrate = [x for x in request.form.values()]

    data = []

    data.append(int(age))
    data.append(int(systolicbp))
    data.append(int(diastolicbp))
    data.append(int(bs))
    data.append(int(bodytemp))
    data.append(int(heartrate))


    prediction = model.predict([data])
    if prediction==0 :
        output = "High Risk"
    elif prediction==1 :
        output = "Low Risk"
    else :
        output = "Mid Risk"

    return render_template('index.html', prediction=output, age=age, systolicbp=systolicbp, diastolicbp=diastolicbp, bs=bs, bodytemp=bodytemp, heartrate=heartrate)


if __name__ == '__main__':
    app.run(debug=True)
