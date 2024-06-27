from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from tensorflow.keras.saving import load_model
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.optimizers import Adam

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        features = request.form
        feature_1 = float(features['feature_1'])
        feature_2 = float(features['feature_2'])
        feature_3 = float(features['feature_3'])
        feature_4 = float(features['feature_4'])
        feature_5 = float(features['feature_5'])
        feature_6 = float(features['feature_6'])
        feature_7 = float(features['feature_7'])
        feature_8 = float(features['feature_8'])
        feature_9 = float(features['feature_9'])
        feature_10 = float(features['feature_10'])
        feature_11 = float(features['feature_11'])
        feature_12 = float(features['feature_12'])

        feature_np = np.array([[feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9, feature_10, feature_11, feature_12]])
        poly = PolynomialFeatures(1, include_bias=False)
        feature_np_mapped = poly.fit_transform(feature_np)
        scaler = StandardScaler()
        feature_np_mapped_scaled = scaler.fit_transform(feature_np_mapped)

        try:
            model = load_model('my_model.keras', compile=False)
            model.compile(
                loss = SparseCategoricalCrossentropy(from_logits=True),
                optimizer = Adam(0.001)
            )
        except Exception as e:
            print(f"Error : {e}")

        def softmax(x):
            z = np.exp(x)
            s = z / z.sum(axis=0)
            return s

        output_np = model.predict(feature_np_mapped_scaled)
        output_np_sm = softmax(output_np)
        output_index = np.argmax(output_np_sm)

        trouble_classes = ['P0133', 'C0300', 'P0079P2004P3000', 'P0078U1004P3000',
        'P0079C1004P3000', 'P007EP2036P18F0', 'P007EP2036P18D0',
        'P007FP2036P18D0', 'P0079P1004P3000', 'P007EP2036P18E0',
        'P007FP2036P18E0', 'P0078B0004P3000', 'P007FP2036P18F0']
        
        return f"Predicted Trouble : {trouble_classes[output_index]}"

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)