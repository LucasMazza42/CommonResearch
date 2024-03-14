from flask import Flask, render_template, request, jsonify
import alphaVantage
import os
app = Flask(__name__)

# Route for serving the HTML file from the 'templates' folder
@app.route('/')
def home():
    return render_template('main.html')

# Route for the research page
@app.route('/research')
def research():
    return render_template('research.html')


@app.route('/search', methods=['POST'])
def search():
    # Get the ticker value from the request
    ticker = request.form['ticker']

    # Call the function to get daily time series data with the provided ticker value
    alphaVantage.get_daily_time_series(ticker, alphaVantage.API_key)

    return jsonify({'message': 'Data fetched successfully'})
if __name__ == '__main__':
    app.run(debug=True)



