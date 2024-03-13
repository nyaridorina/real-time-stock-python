import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Dropdown(
        id='stock-selector',
        options=[
            {'label': 'Apple Inc. (APPLE)', 'value': 'AAPL'},
            {'label': 'Google LLC (GOOGLE)', 'value': 'GOOGL'},
        ],
        value='AAPL'  # Default value
    ),
    dcc.Graph(id='stock-graph')
])

# Function to fetch stock data from Alpha Vantage API
def get_stock_data(symbol):
    api_key = 'K5O3W5G6S5LISGBJ'  # Replace with your API key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Time Series (5min)' in data:
            time_series = data['Time Series (5min)']
            times = list(time_series.keys())
            prices = [float(time_series[time]['1. open']) for time in times]
            return times, prices
        else:
            print("Error: Time Series (5min) not found in API response.")
            return [], []
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return [], []

# Define callback function to update the graph
@app.callback(
    Output('stock-graph', 'figure'),
    [Input('stock-selector', 'value')]
)
def update_graph(selected_stock):
    print(f"Selected stock: {selected_stock}")
    times, prices = get_stock_data(selected_stock)
    print(f"Times: {times}")
    print(f"Prices: {prices}")

    if not times or not prices:
        return {
            'data': [],
            'layout': go.Layout(
                title=f'Real-Time Stock Price for {selected_stock}',
                xaxis_title='Time',
                yaxis_title='Price'
            )
        }

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=times, y=prices, mode='lines'))

    fig.update_layout(
        title=f'Real-Time Stock Price for {selected_stock}',
        xaxis_title='Time',
        yaxis_title='Price'
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
