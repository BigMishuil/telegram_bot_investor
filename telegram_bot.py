import requests
from config import API_TOKEN, BOT_API_TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


HELP_COMMAND = """
Write the ticker of the company you need information about.
"""

bot = Bot(BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hi! I am the Telegram Bot Investor! I can display information about the company and"
    " basic financial indicators of the company.")
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND)
    await message.delete()


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def info_func(message: types.Message):
    try:
        r = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={message.text}&apikey={API_TOKEN}')
        data = r.json()

        name = data['Name']
        description = data['Description']
        country = data['Country']
        industry = data['Industry']

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

        await message.answer(f" <b>Company name</b>: {name}\n <b>Company description</b>: {description}\n <b>Country</b>: {country}\n <b>Industry</b>: {industry}", parse_mode='HTML')
        await message.answer(
            f" <b>Market capitalization</b>: {capitalization}\n <b>Book value</b>: {book_value}\n <b>Beta</b>: {beta}\n <b>Revenue TTM</b>: {revenue_last_12_months}\n <b>P/E TTM</b>: {pe_last_12_months}\n"
            f" <b>Forward P/E</b>: {forward_pe}\n <b>P/B Ratio</b>: {pb_ratio}\n <b>P/S Ratio</b>: {ps_ratio}\n <b>EPS</b>: {eps}\n <b>EBITDA</b>: {ebitda}\n <b>EV/EBITDA</b>: {ev_to_ebitda}\n <b>EV/Revenue</b>: {ev_to_revenue}\n"
            f" <b>ROE</b>: {roe}\n <b>ROA</b>: {roa}\n <b>Dividend yield</b>: {dividend_yield} ", parse_mode='HTML')

    except Exception as ex:
        await message.answer('Something went wrong..')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

