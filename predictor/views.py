
from django.shortcuts import render
from datetime import datetime, timedelta

from .api import (
    get_current_bitcoin_price,
    get_last_60_close_prices,
)

from .model.prediction import (
    predict_next_price,
    predict_next_7_days,
)


def home(request):

    # Current bitcoin price (numeric)
    current_price_value = get_current_bitcoin_price()

    # Price shown on webpage
    current_price = "{:,.2f}".format(current_price_value)

    last_60_prices = get_last_60_close_prices()

    predicted_price = None
    predicted_price_value = None

    prediction_7days = []
    prediction_dates = []

    if len(last_60_prices) == 60:

        # Tomorrow prediction
        predicted_price_value = round(
            predict_next_price(last_60_prices), 2
        )

        predicted_price = "{:,.2f}".format(predicted_price_value)

        # Next 7 days prediction
        prediction_7days = predict_next_7_days(last_60_prices)

        # Round all predictions
        prediction_7days = [round(i, 2) for i in prediction_7days]

        today = datetime.today()

        for i in range(7):

            prediction_dates.append(
                (today + timedelta(days=i + 1)).strftime("%d-%b-%Y")
            )

    context = {

        # Cards
        "current_price": current_price,
        "predicted_price": predicted_price,

        # Numeric values for chart
        "chart_current_price": current_price_value,
        
        # Table
        "prediction_7days": list(zip(prediction_dates, prediction_7days)),

    }

    return render(request, "index.html", context)