import json
import requests
import streamlit as st, pandas as pf, yfinance as yf
import plotly.express as px 
from streamlit_lottie import st_lottie 


# Page title
st.title('📊 Stock Dashboard')
#Sidebar
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

dashboard, about, contact = st.tabs(["Dashboard","About","Contact"])  #Adding tabs 
with dashboard:
    try: 
        data = yf.download(ticker, start=start_date, end=end_date)
        fig = px.line(data, x = data.index, y = data['Adj Close'], title=ticker)
        st.plotly_chart(fig)

    except ValueError:
        st.text("""Author : K.$.Nath""")

    result = st.button("Show data")
    if result:
        st.write(data)

with about:
    #Adding animation 
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_coding = load_lottieurl("https://lottie.host/12726fe4-4d4c-4d0d-a04c-20592832a4d0/ZrkBdSphZh.json")
    st_lottie(lottie_coding, height=300, key = "coding")

with contact:
    #Adding animation 
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_coding = load_lottieurl("https://lottie.host/5159656e-c6f2-4e7b-854b-8acf2b6cd2bc/Pg1KzvfFYA.json")
    st_lottie(lottie_coding, height=300, key = "coding2")
    st.write("Check out my website [:globe_with_meridians:](https://ksnath.com)")
    st.write("Connect On Instagram [:camera:](https://www.instagram.com/k.s.srinath_1?igsh=MWJ4NWV5NGtnYTE5dg==)")
