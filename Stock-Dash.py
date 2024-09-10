import json 
import requests
import streamlit as st, pandas as pf, yfinance as yf
import plotly.express as px 
from streamlit_lottie import st_lottie 
from alpha_vantage.fundamentaldata import FundamentalData
   
# Page title
st.title('📊 Stock Dashboard')
 
#Hide footer and the hamburger
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#Sidebar
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

dashboard,fund_data,about, contact = st.tabs(["Dashboard","Fundamental data","About","Contact"])  #Adding tabs 
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
   
with fund_data:
        key = 'U8931XI2ODS6XEB5'
        fd = FundamentalData(key,output_format = 'pandas') 
 
        st.subheader('Balance Sheet')
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)

        st.subheader('Cash Flow Statement')
        cash_flow = fd.get_cash_flow_annual(ticker)[0]
        cf = cashflow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)
        
        st.subheader('Income Statement')
        income_statement = fd.get_income_statement_annual(ticker)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1) 

with about:
    #Some text
    st.subheader("Just a clean and minimalistic stock tracking website.")
    st.markdown("***Simplicity*** is the ultimate *sophistication*.")
    st.subheader(" ")

    #some more text
    st.subheader(":heavy_exclamation_mark: How to use :heavy_exclamation_mark:")
    st.write("On the sidebar, select the date interval and enter the ticker for the stock that you want to monitor. ")
    st.write("To find tickers, visit yahoo finance. Eg: INFY, SBIN.NS ")
    
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

