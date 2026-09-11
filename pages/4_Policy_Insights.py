import streamlit as st
from src.load_data import load_data

df = load_data()

st.title("Policy Insights")

latest = df[df.year == 2025]

highest = latest.sort_values("gap", ascending=False).iloc[0]
lowest = latest.sort_values("gap").iloc[0]

st.metric(
    "Highest Gap (2025)",
    highest.country,
    f"{highest.gap:.1f}%"
)

st.metric(
    "Lowest Gap (2025)",
    lowest.country,
    f"{lowest.gap:.1f}%"
)

st.header("Key Findings")

st.markdown("""
- Vietnam has shown a gradual decline in gender pay inequality.
- Thailand maintains a moderate wage gap throughout the period.
- The Philippines consistently records the lowest gap among the three countries.
""")

st.header("Recommendations")

st.success("Increase wage transparency in both public and private sectors.")
st.success("Expand women's participation in high-income occupations.")
st.success("Strengthen labour market monitoring using ILO SDG Indicator 8.5.1.")