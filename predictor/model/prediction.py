# import os
# import joblib
# import numpy as np
# import tensorflow as tf

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# MODEL_PATH = os.path.join(BASE_DIR, "bitcoin_price_prediction_lstm.keras")
# SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# model = tf.keras.models.load_model(MODEL_PATH)
# scaler = joblib.load(SCALER_PATH)

# def predict_next_price(last_60_prices):

#     data = np.array(last_60_prices).reshape(-1,1)

#     scaled_data = scaler.transform(data)

#     X = scaled_data.reshape(1,60,1)

#     prediction = model.predict(X, verbose=0)

#     prediction = scaler.inverse_transform(prediction)

#     return float(prediction[0][0])


import os
import joblib
import numpy as np
import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "bitcoin_price_prediction_lstm.keras")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

model = tf.keras.models.load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def predict_next_price(last_60_prices):
    data = np.array(last_60_prices).reshape(-1, 1)

    scaled_data = scaler.transform(data)

    X = scaled_data.reshape(1, 60, 1)

    prediction = model.predict(X, verbose=0)

    prediction = scaler.inverse_transform(prediction)

    return float(prediction[0][0])


def predict_next_7_days(last_60_prices):

    prices = last_60_prices.copy()

    predictions = []

    for _ in range(7):

        next_price = predict_next_price(prices[-60:])

        predictions.append(round(next_price, 2))

        prices.append(next_price)

    return predictions