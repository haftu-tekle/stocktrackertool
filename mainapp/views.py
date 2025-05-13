from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import yfinance as yf 
import pandas as pd


def index(request):
    stock_picker=['AAPL','MSFT','GOOGL','AMZN','TSLA','META']
    tickers=yf.Ticker(stock_picker)
    print(tickers)
    return render(request, 'stockpicker/index.html',{'stock_picker':tickers})

def table(request):
    # stockpicker=request.GET.getlist('stockpicker')
    # print(stockpicker)
    stock_picker=['AAPL','MSFT','GOOGL','AMZN','TSLA','META']


    try:
        if isinstance(stock_picker, str):
            ticker=yf.Ticker(stock_picker)
            information=ticker.info
            if information:
                table={
                    'Symbol':information.get('symbol'),
                    'Short Name':information.get('shortName'),
                    'Price':information.get('currentPrice'),
                    'Change':information.get('regularMarketChange'),
                    'Change by Percent':information.get('regularMarketChangePercent'),
                    'Open':information.get('open'),
                    'High':information.get('dayHigh'),
                    'Low':information.get('dayLow'),
                    'Previous Close':information.get('previousClose'),
                    'Volume':information.get('volume'),
                    'Market Cap':information.get('marketCap'),
                    'P/E Ratio':information.get('trailingPE'),
                    'Forward P/E':information.get('forwardPE'),
                    '52 Week High':information.get('fiftyTwoWeekHigh'),
                    '53 Week Low':information.get('fiftyTwoWeekLow'),

                }
                return pd.DataFrame([table])

            else:
                print(f'Could not retrive inforamation {ticker}')
                return None
        elif isinstance(stock_picker, list):
            data_list=[]
            for ticker_symbol in stock_picker:
                ticker=yf.Ticker(ticker_symbol)
                information=ticker.info
                if information:
                    table={
                    'Symbol':information.get('symbol'),
                    'Short Name':information.get('shortName'),
                    'Price':information.get('currentPrice'),
                    'Change':information.get('regularMarketChange'),
                    'Change by Percent':information.get('regularMarketChangePercent'),
                    'Open':information.get('open'),
                    'High':information.get('dayHigh'),
                    'Low':information.get('dayLow'),
                    'Previous Close':information.get('previousClose'),
                    'Volume':information.get('volume'),
                    'Market Cap':information.get('marketCap'),
                    'P/E Ratio':information.get('trailingPE'),
                    'Forward P/E':information.get('forwardPE'),
                    '52 Week High':information.get('fiftyTwoWeekHigh'),
                    '53 Week Low':information.get('fiftyTwoWeekLow'),

                    }
                    data_list.append(table)
                else:
                    print(f'could not retrive info for {ticker_symbol}')
            if data_list:
                return pd.DataFrame(data_list)
            else:
                print('Error!!')
                return None
        
        else:
            print('Invalid input for tickers. Please provide a string or a list of strings')

            return None
    except Exception as e:
        print(f'An error occured: {e}')
        return None
table(request=all)