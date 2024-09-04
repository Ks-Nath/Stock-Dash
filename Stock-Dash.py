import streamlit as st, pandas as pf, yfinance as yf, numpy as np
import plotly.express as px 

# Page title
st.title('📊 Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data['Adj Close'], title=ticker)
st.plotly_chart(fig)

result = st.button("Show data")
if result:
    st.write(data)