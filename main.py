import os
from pprint import pprint
import requests
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")


def get_info_about_the_company(ticker, API_TOKEN):
    try:
        r = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={API_TOKEN}')
        data = r.json()
        #pprint(data)

        name = data['Name']
        description = data['Description']
        country = data['Country']
        industry = data['Industry']

        print(f" Company name: {name}\n Company description: {description}\n Country: {country}\n Industry: {industry}")

    except Exception as ex:
        print(ex)


def get_basic_financials(ticker, API_TOKEN):
    try:
        r = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={API_TOKEN}')
        data = r.json()
        #pprint(data)

        capitalization = round(float(data['MarketCapitalization']), 2)
        book_value = data['BookValue']
        beta = data['Beta']
        revenue_last_12_months = round(float(data['RevenueTTM']), 2)
        pe_last_12_months = data['TrailingPE']
        forward_pe = data['ForwardPE']
        pb_ratio = data['PriceToBookRatio']
        ps_ratio = data['PriceToSalesRatioTTM']
        eps = data['EPS']
        ebitda = round(float(data['EBITDA']), 2)
        ev_to_ebitda = data['EVToEBITDA']
        ev_to_revenue = data['EVToRevenue']
        roe = data['ReturnOnEquityTTM']
        roa = data['ReturnOnAssetsTTM']
        dividend_yield = data['DividendYield']

        print(f" Market capitalization: {capitalization}\n Book value: {book_value}\n Beta: {beta}\n Revenue TTM: {revenue_last_12_months}\n P/E TTM: {pe_last_12_months}\n"
              f" Forward P/E: {forward_pe}\n P/B Ratio: {pb_ratio}\n P/S Ratio: {ps_ratio}\n EPS: {eps}\n EBITDA: {ebitda}\n EV/EBITDA: {ev_to_ebitda}\n EV/Revenue: {ev_to_revenue}\n"
              f" ROE: {roe}\n ROA: {roa}\n Dividend yield: {dividend_yield} ")

    except Exception as ex:
        print(ex)


def currency_exchange_rate(from_cur, to_cur, API_TOKEN):
    #This function also returns cryptocurrency exchange rates

    try:
        r = requests.get(f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_cur}&to_currency={to_cur}&apikey={API_TOKEN}')
        data = r.json()
        #pprint(data)

        first_currency = data['Realtime Currency Exchange Rate']['1. From_Currency Code']
        second_currency = data['Realtime Currency Exchange Rate']['3. To_Currency Code']
        ex_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

        print(f"{first_currency}/{second_currency} - {ex_rate} ")

    except Exception as ex:
        print(ex)


#get_info_about_the_company('TSLA', API_TOKEN)
#get_basic_financials('TSLA', API_TOKEN)
#currency_exchange_rate('USD', 'RUB', API_TOKEN)
#currency_exchange_rate('BTC', 'USD', API_TOKEN)







