import random
from datetime import datetime, timedelta

def buildPools():
    """Builds lists of word fragments."""
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
    """Builds a deterministic, shuffled list of names."""
    pList, mList, sList = buildPools()
    names = set()

    # Generate 3-part names
    for p in pList:
        for m in mList:
            for s in sList:
                names.add((p + m + s).capitalize())

    # Generate 2-part names
    for p in pList:
        for s in sList:
            names.add((p + s).capitalize())
    for m in mList:
        for s in sList:
            names.add((m + s).capitalize())

    # Convert set to a list and SORT it to ensure consistent order
    nameList = sorted(list(names))

    # Shuffle the consistently ordered list with a fixed seed
    rng = random.Random(42)
    rng.shuffle(nameList)
    
    return nameList

def getDayIndex(y, d):
    """Calculates the number of days since a fixed epoch."""
    base = datetime(1, 1, 1)
    t = datetime(y, 1, 1) + timedelta(days=d)
    delta = (t - base).days
    return delta

# This line now gets the cached list, which is built deterministically
nameList = buildNames()

def getDayName(ds):
    """Gets the persistent name for a given date string."""
    dt = datetime.strptime(ds, "%m/%d/%Y")
    y = dt.year
    d = (dt - datetime(y, 1, 1)).days
    i = getDayIndex(y, d)
    return nameList[i % len(nameList)]

# Streamlit UI
st.set_page_config(page_title="Latin Day Generator", layout="centered")

st.markdown(
    """
    <style>
    div.block-container {
        text-align: center;
    }
    label, input, select, .stNumberInput, .stDateInput {
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 style='font-family:Helvetica; font-weight:900;'>Latin Day Name Generator</h1>", unsafe_allow_html=True)

cols = st.columns(3)

with cols[0]:
    month = st.selectbox("Month", list(range(1, 13)), index=6, format_func=lambda x: f"{x:02}")

with cols[1]:
    day = st.number_input("Day", min_value=1, max_value=31, value=31)

with cols[2]:
    year = st.number_input("Year", value=2025, step=1)

try:
    dt = f"{month}/{day}/{year}"
    name = getDayName(dt)
    st.markdown(f"<div style='font-family:Helvetica; font-weight:900; font-size:48px; padding-top:30px;'>{name} Day!</div>", unsafe_allow_html=True)
except Exception:
    st.warning("Invalid date. Please enter a valid date.")

st.markdown(
    "<br><br><div style='font-size:14px; color:gray;'>© 2025 Andrew Lehti — Creative Commons Attribution 4.0 International (CC BY 4.0)</div>",
    unsafe_allow_html=True
)
