import streamlit as st
import plotly.graph_objects as go
from src.load_data import yearly_summary

df = yearly_summary()

st.title("Trend Analysis")

country = st.selectbox(
    "Country",
    ["Viet Nam","Thailand","Philippines"]
)

d = df[df.country==country]

# ===== Male vs Female =====
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=d.year,
    y=d.male,
    mode="lines+markers",
    name="Male",
    line=dict(color="#2563EB", width=4)
))

fig.add_trace(go.Scatter(
    x=d.year,
    y=d.female,
    mode="lines+markers",
    name="Female",
    line=dict(color="#EC4899", width=4)
))

fig.update_layout(
    template="plotly_white",
    height=420,
    hovermode="x unified",
    title=f"Average Earnings — {country}"
)

st.plotly_chart(fig, width="stretch")

# ===== Gap =====

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=d.year,
    y=d.gap,
    marker_color="#7C3AED",
    text=d.gap.round(1),
    textposition="outside"
))

fig2.update_layout(
    template="plotly_white",
    title="Average Gender Pay Gap (%)",
    yaxis_title="Gap %",
    height=350
)

st.plotly_chart(fig2, use_container_width=True)