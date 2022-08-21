import streamlit as st
import pandas as pd
import openpyxl
# import plotly.express as px

# https://www.webfx.com/tools/emoji-cheat-sheet/
xlfile = r'D:\EXCEL\Dartbot matches.xlsx'

# st.set_page_config(page_title="Dartbot Matches 2022", page_icon=":bar_chart:", layout="wide")
st.set_page_config(page_title="Dartbot Matches 2022", page_icon=":bar_chart:")

df = pd.read_excel(io=xlfile,engine='openpyxl',sheet_name='Dartbot_matches')
df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')
df.columns = df.columns.str.lower()
dates = df.date.unique()

"""
-- MEAN OF 3-DART AVERAGE FOR EACH DARTBOT LEVEL
"""
db_level_3da = df.groupby('dartbot_level')['3-dart average'].mean().round(2)

"""
-- COUNT OF MATCHES AT EACH LEVEL
"""
db_level_count = df.groupby('dartbot_level')['result'].count() # counts number of records at each dartbot level

db_level_result = df['result'].groupby(df['dartbot_level']).value_counts()

""" 
-- TABLE OF WIN % 
"""
db_level_crosstab = pd.crosstab(df.dartbot_level,df.result,normalize='index')
db_level_crosstab.drop('Lost', axis=1,inplace=True)
db_level_crosstab['Won'] *= 100
db_level_crosstab['Won'] = db_level_crosstab['Won'].round(decimals=0)
print(db_level_crosstab)

# ---- HEADER SECTION ----
with st.container():
    st.title("Dartbot Matches 2022")
    st.subheader("First to 5 legs")
    date = st.selectbox("Select date", df.date.unique())
    match_result = st.selectbox("Select result", df.result.unique())
    df_selection = df.query("date == @date & result == @match_result")
    df_page = df_selection.transpose().astype(str)
    st.table(df_page)



print(df.head())


