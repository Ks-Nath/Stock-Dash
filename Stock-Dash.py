import json
import requests
import streamlit as st, pandas as pf, yfinance as yf
import plotly.express as px 
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/db79e7cb-5d16-4835-98c3-f4d7c97656f3/mplX6B6uxK.json")


# Page title
st.title('📊 Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')
try: 
    data = yf.download(ticker, start=start_date, end=end_date)
    fig = px.line(data, x = data.index, y = data['Adj Close'], title=ticker)
    st.plotly_chart(fig)

except ValueError:
    st.text("""Author : K.$.Nath""")

result = st.button("Show data")
if result:
    st.write(data)

st_lottie(lottie_coding, height=300, key = "coding")
