import pandas as pd
from fredapi import Fred
from datetime import datetime
import yfinance as yf

start_date = "2010-01-01"
end_date = datetime.today().strftime("%Y-%m-%d")



efts = ["XLK", "XLE", "XLF", "XLI"]
data = yf.download(efts, start_date, end_date)
weekly_data = data.resample("W-MON").ffill()
weekly_data.to_csv("data/eft_prices.csv")


fred = Fred(api_key="f0150da1b6ca4257533df31008977c3f")
series = {
    "Fed Funds Rate": "FEDFUNDS",
    "CPI": "CPIAUCNS",
    "10Y Treasury": "GS10",
    "Unemployment": "UNRATE",
    "WTI Crude": "DCOILWTICO",
    "DXY": "DTWEXBGS",
    "VIX": "VIXCLS",
    "US Durable Goods": "DGORDER",
    "Manufacturers New Orders": "AMTMNO"
    }


df_dict = {}

for name, code in series.items():
    data = fred.get_series(code)
    data.index = pd.to_datetime(data.index)
    weekly = data.resample("W-MON").ffill()
    df_dict[name] = weekly

# Combine all into single DataFrame on weekly index
df_macro = pd.concat(df_dict.values(), axis=1)
df_macro.columns = df_dict.keys()
df_macro = df_macro.ffill(limit=10)
df_macro.to_csv("data/macro_data.csv")