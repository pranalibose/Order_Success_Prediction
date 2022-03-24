import numpy as np
from flask import Flask, request, render_template
import joblib
import sklearn
import pandas as pd

# start flask
app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # get form data
        # state = request.form.get('state')
        item_total = request.form.get('item_total')
        ship_fee = request.form.get('ship_fee')
        quantity = request.form.get('quantity')
        cod = request.form.get('cod')
        date = request.form.get('date')
        if cod == 'no':
            c = 0
        else:
            c = 1

        year = int(str(date)[:4])
        month = int(str(date)[5:7])
        day = int(str(date)[8:])

        print(year, month, day)

        # call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(item_total, ship_fee, quantity, c, year, month, day)
            # predict = np.round_(prediction, decimals = 4)
            if prediction == 0:
                predict = 'This will be a Return Order'
                image = 'return1.png'
            else:
                predict = 'This order will be successful!'
                image = 'success.jpg'
            return render_template('predict.html', prediction=predict, image=image)          # pass prediction to template
        except ValueError:
            return "Please Enter valid values"
        pass
    pass

def preprocessDataAndPredict(item_total, ship_fee, quantity, c, year, month, day):
    test_data = [item_total, ship_fee, quantity, c, year, month, day]                        # keep all inputs in array
    data = {'quantity': [quantity],
             'item_total': [item_total],
             'shipping_fee': [ship_fee],
             'cod': [c],
             'year': [year],
             'month': [month],
             'day': [day]}

    test_data = pd.DataFrame.from_dict(data)
    print(test_data)
    test_data = np.array(test_data)                                            # convert value data into numpy array
    test_data = test_data.reshape(1, -1)                                       # reshape array
    print(test_data)
    file = open("model.pkl", "rb")                                             # open file
    trained_model = joblib.load("model.pkl")                                              # load trained model
    prediction = trained_model.predict(test_data)                              # predict
    return prediction

if __name__ == '__main__':
    app.run(debug=True)
    print(sklearn.__version__)