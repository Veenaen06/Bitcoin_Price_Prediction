# Bitcoin Price Prediction Using Django and LSTM

A Django web application that displays the current Bitcoin price, predicts the next day's price, and generates an iterative seven-day forecast using a pre-trained Long Short-Term Memory (LSTM) neural network.

> **Disclaimer:** This project is for academic and educational purposes. Predictions are estimates, not guarantees of future prices or financial advice.

## Features

- Retrieves the current BTC/USDT price from Binance's public REST API.
- Retrieves the latest 60 daily Bitcoin closing prices from Binance.
- Uses a saved TensorFlow/Keras LSTM model to predict the next day's price.
- Generates a seven-day forecast by feeding each prediction into the next prediction step.
- Displays current and predicted prices,line chart, and a seven-day prediction table.
- Uses Django templates, Bootstrap, Gunicorn, and WhiteNoise.

## Technology Stack

- **Backend:** Python, Django 5.2
- **Machine learning:** TensorFlow/Keras, LSTM
- **Data processing/model support:** NumPy, scikit-learn, Joblib
- **Market data:** Binance public REST API
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Deployment support:** Gunicorn, WhiteNoise
- **Database configuration:** SQLite (Django default; the current prediction workflow does not use application database models)

## Project Structure

```text
Bitcoin_Price_Prediction-main/
├── bitcoin_prediction/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Root URL routes
│   └── wsgi.py
├── predictor/
│   ├── migrations/
│   │   └── __init__.py
│   ├── model/
│   │   ├── bitcoin_price_prediction_lstm.keras  # Saved LSTM model
│   │   ├── prediction.py                       # Model loading and forecasts
│   │   └── scaler.pkl                          # Saved data scaler
│   ├── templates/
│   │   └── index.html        # Dashboard interface
│   ├── api.py                # Binance price requests
│   ├── apps.py
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py               # Predictor URL routes
│   └── views.py              # Dashboard view and prediction flow
├── staticfiles/              # Collected Django admin static files, if included
├── manage.py
├── requirements.txt
├── runtime.txt               # Specifies Python 3.11.9
├── Procfile                  # Gunicorn startup command
└── .gitignore
```

## How It Works

1. The home page invokes `home()` in `predictor/views.py`.
2. `predictor/api.py` requests the current BTC/USDT price and the latest 60 daily candles from Binance.
3. The closing prices are extracted from the candle response.
4. `predictor/model/prediction.py` loads the saved `.keras` model and `scaler.pkl` file.
5. The 60 prices are scaled and reshaped into the model's expected input shape `(1, 60, 1)`.
6. The model predicts the next price, which is converted back to the original price scale using the scaler.
7. For the seven-day forecast, each predicted value is appended to the input sequence to predict the following day.
8. Django passes the values to `predictor/templates/index.html`, which renders the price cards, chart, and forecast table.

The seven-day forecast is recursive: later predictions depend on earlier predictions, so uncertainty can accumulate over the forecast period.

## Prerequisites

- Python 3.11 (the included `runtime.txt` specifies Python 3.11.9)
- `pip`
- Internet access for Binance requests and Bootstrap/Chart.js CDN assets
- The model and scaler files included under `predictor/model/`

TensorFlow, NumPy, and scikit-learn are platform-sensitive. Use compatible package versions and an environment supported by the pinned dependencies in `requirements.txt`.

## Installation and Local Setup

### 1. Extract the ZIP

Extract the project archive and open a terminal in the folder containing `manage.py`.

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply Django migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Running the Application

The dashboard is available at `/`. It requests fresh market data when the page loads. Use the **Refresh** button to reload the page and request updated data. The current Binance endpoints are public and do not require an API key in this code.

## Limitations

- Forecasts are estimates and are not financial advice.
- The model uses the latest 60 daily closing prices returned by Binance.
- Recursive multi-day predictions may become less reliable farther into the forecast.
- API availability, network access, package compatibility, and model compatibility affect runtime behavior.
- The dashboard does not currently show model evaluation metrics or confidence intervals.

## Future Enhancements

- Add robust API/model error handling and user-friendly messages.
- Display historical prices alongside forecast values.
- Evaluate performance with appropriate metrics such as MAE, RMSE, and MAPE on a held-out dataset.
- Add prediction uncertainty only if it is supported by a suitable method.
- Cache market data to reduce repeated API requests.
- Use environment variables for secret settings and improve production configuration.
- Add tests for API handling and prediction outputs.
- Show data-source timestamps and clarify date/time zones.

## Author

Veena E N
