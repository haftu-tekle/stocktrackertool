from django.shortcuts import render
import yfinance as yf
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocktrackertool.settings')


def index(request):
    stock_picker = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META']
    return render(request, 'stockpicker/index.html', {'stock_picker': stock_picker})

def stockTracker(request):
    if request.method == 'GET':
        selected_stocks = request.GET.getlist('stock_picker')
        data_list = []

        try:
            for ticker_symbol in selected_stocks:
                ticker = yf.Ticker(ticker_symbol)
                information = ticker.info

                if information:
                    data_list.append({
                        'Symbol': information.get('symbol', 'N/A'),
                        'Short Name': information.get('shortName', 'N/A'),
                        'Price': information.get('currentPrice', 0.0),
                        'Change': information.get('regularMarketChange', 0.0),
                        'Change by Percent': information.get('regularMarketChangePercent', 0.0),
                        'Open': information.get('open', 0.0),
                        'High': information.get('dayHigh', 0.0),
                        'Low': information.get('dayLow', 0.0),
                        'Previous Close': information.get('previousClose', 0.0),
                        'Volume': information.get('volume', 0),
                        'Market Cap': information.get('marketCap', 'N/A'),
                        'P/E Ratio': information.get('trailingPE', 'N/A'),
                        'Forward P/E': information.get('forwardPE', 'N/A'),
                        '52 Week High': information.get('fiftyTwoWeekHigh', 0.0),
                        '52 Week Low': information.get('fiftyTwoWeekLow', 0.0),
                    })
            print(data_list)
            return render(request, 'base/table.html', {'stock_picker': selected_stocks, 'stocks': data_list})

        except Exception as e:
            return render(request, 'base/table.html', {'error': f'An error occurred while fetching stock data: {e}'})
    else:
        return render(request, 'stockpicker/index.html', {'error': 'Invalid request'})