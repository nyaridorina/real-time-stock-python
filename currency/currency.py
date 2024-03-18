import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_KEY = "feec8b7611be09b0cad59a2b"

def fetch_currency_rates(base_currency, target_currency, days=30):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract exchange rates from the response
    exchange_rates = data['rates']

    # Get current date
    end_date = datetime.now()

    # Calculate start date (30 days ago)
    start_date = end_date - timedelta(days=days)

    dates = []
    rates_base = []
    rates_target = []

    date = start_date
    while date <= end_date:
        date_str = date.strftime("%Y-%m-%d")
        if date_str in exchange_rates:
            dates.append(date_str)
            rates_base.append(exchange_rates[date_str][base_currency])
            rates_target.append(exchange_rates[date_str][target_currency])
        date += timedelta(days=1)

    return dates, rates_base, rates_target

def plot_currency_rates(base_currency, target_currency, days=30):
    dates, rates_base, rates_target = fetch_currency_rates(base_currency, target_currency, days)

    # Plot the data
    plt.plot(dates, rates_base, label=base_currency)
    plt.plot(dates, rates_target, label=target_currency)
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.title(f'Currency Exchange Rates ({base_currency}/{target_currency}) over the last {days} days')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Example usage
plot_currency_rates('EUR', 'CNY', days=30)
