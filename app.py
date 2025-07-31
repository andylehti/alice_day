import streamlit as st
import random
from datetime import datetime, timedelta

def buildPools():
    p1 = ['sol', 'pax', 'lux', 'ver', 'fin', 'vent', 'mar', 'dom', 'nec', 'clar', 'fer']
    p2 = ['aer', 'bell', 'cael', 'dict', 'equi', 'fort', 'glor', 'hon', 'ign', 'juv', 'luc', 'magn', 'nav', 'op', 'prim', 'quant', 'reg', 'sanct', 'ten', 'ult', 'vex', 'xer', 'zen']
    m1 = ['al', 'in', 'or', 'ul', 'ev', 'ax', 'ir', 'um', 'et', 'ob', 'ex']
    m2 = ['ac', 'ad', 'af', 'am', 'ar', 'as', 'at', 'av', 'az', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'ex', 'ez']
    s1 = ['tia', 'ium', 'tor', 'ix', 'ens', 'rus', 'ia', 'ana', 'ora', 'ent']
    s2 = ['atus', 'ensia', 'ilis', 'icus', 'orium', 'axia', 'inus', 'atrix', 'ellus', 'itas', 'andum', 'anus', 'ensis', 'idus', 'orix']
    prefixes = p1 + p2
    middles = m1 + m2
    suffixes = s1 + s2
    return prefixes, middles, suffixes

def buildNames():
    pList, mList, sList = buildPools()
    names = set()
    for p in pList:
        for m in mList:
            for s in sList:
                names.add((p + m + s).capitalize())
    for p in pList:
        for s in sList:
            names.add((p + s).capitalize())
    for m in mList:
        for s in sList:
            names.add((m + s).capitalize())
    nameList = list(names)
    rng = random.Random(42)
    rng.shuffle(nameList)
    return nameList

def getDayIndex(dt):
    base = datetime(1, 1, 1)
    return (dt - base).days

nameList = buildNames()

def getDayName(dt):
    i = getDayIndex(dt)
    return nameList[i % len(nameList)]

# Centering everything using HTML
st.set_page_config(page_title="Latin Day Generator", layout="centered")

st.markdown(
    """
    <style>
    div.block-container {
        text-align: center;
    }
    label, input, select, .stNumberInput, .stDateInput {
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center; font-family:Helvetica; font-weight:900;'>Latin Day Name Generator</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    month = st.selectbox("Month", list(range(1, 13)), index=6, format_func=lambda x: f"{x:02}")
with col2:
    day = st.number_input("Day", min_value=1, max_value=31, value=31)
with col3:
    year = st.number_input("Year", value=2025, step=1)

try:
    dt = datetime(year, month, day)
    name = getDayName(dt)
    st.markdown(
        f"<div style='text-align:center; font-family:Helvetica; font-weight:900; font-size:48px; padding-top:30px;'>{name} Day!</div>",
        unsafe_allow_html=True
    )
except ValueError:
    st.warning("Invalid date. Try a valid combination of month, day, and year.")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "<div style='text-align:center; font-size:14px; color:gray;'>© 2025 Andrew Lehti — Creative Commons Attribution 4.0 International (CC BY 4.0)</div>",
    unsafe_allow_html=True
)
