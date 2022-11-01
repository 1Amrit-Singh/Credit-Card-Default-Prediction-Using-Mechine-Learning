
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin
import pickle




app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("home.html")


@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == "POST":

      #for rendering results on HTML
        

        features = [int(x) for x in request.form.values()]

        # re-arranging the list as per data set
        feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
        features_arr = [np.array(feature_list)]

        prediction = model.predict(features_arr)

        print(features_arr)
        print("prediction value: ", prediction)

        result = ""
        if prediction == 1:
            return render_template("default.html")
        else:
            return render_template("non_default.html")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
