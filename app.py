import streamlit as st
import plotly.express as px
from src.load_data import load_data

st.set_page_config(
    page_title="Gender Wage Gap ASEAN",
    page_icon="📊",
    layout="wide"
)

from src.load_data import yearly_summary

df = yearly_summary()

st.title("Gender Wage Gap in Southeast Asia")
st.subheader("Vietnam • Thailand • Philippines (2018–2025)")

# =====================
# Sidebar
# =====================

country = st.sidebar.selectbox(
    "Country",
    ["All"] + sorted(df.country.unique())
)

year = st.sidebar.slider(
    "Year",
    2018, 2025, 2025
)

filtered = df[df.year <= year]

if country != "All":
    filtered = filtered[filtered.country == country]

# =====================
# KPI
# =====================

latest = filtered[filtered.year == year]

avg_gap = latest.gap.mean()

female = latest.female.mean()

male = latest.male.mean()

c1, c2, c3 = st.columns(3)

c1.metric("Average Gender Pay Gap", f"{avg_gap:.1f}%")
c2.metric("Average Female Wage", f"{female:.0f}")
c3.metric("Average Male Wage", f"{male:.0f}")

st.divider()

fig = px.line(
    filtered,
    x="year",
    y="gap",
    color="country",
    markers=True,
    color_discrete_map={
        "Viet Nam":"#5B5FEF",
        "Thailand":"#EC4899",
        "Philippines":"#14B8A6"
    }
)

fig.update_layout(
    template="plotly_white",
    height=500,
    title="Gender Pay Gap Trend",
    yaxis_title="Gap (%)"
)

st.plotly_chart(fig, width="stretch")