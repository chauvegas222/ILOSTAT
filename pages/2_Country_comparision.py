import streamlit as st
import plotly.graph_objects as go
from src.load_data import yearly_summary

# Load dữ liệu đã group theo country + year
df = yearly_summary()

st.title("🌏 Country Comparison")

# Chọn năm
year = st.selectbox(
    "Select Year",
    sorted(df.year.unique()),
    index=len(df.year.unique()) - 1
)

d = df[df.year == year].sort_values("gap", ascending=False)

# ==========================
# KPI
# ==========================
c1, c2, c3 = st.columns(3)

c1.metric(
    "Highest Gap",
    d.iloc[0]["country"],
    f"{d.iloc[0]['gap']:.1f}%"
)

c2.metric(
    "Lowest Gap",
    d.iloc[-1]["country"],
    f"{d.iloc[-1]['gap']:.1f}%"
)

c3.metric(
    "Average Gap",
    f"{d.gap.mean():.1f}%"
)

st.divider()

# ==========================
# Dumbbell Chart
# ==========================

fig = go.Figure()

for _, r in d.iterrows():

    # Đường nối Male - Female
    fig.add_trace(go.Scatter(
        x=[r["female"], r["male"]],
        y=[r["country"], r["country"]],
        mode="lines",
        line=dict(color="#D1D5DB", width=4),
        showlegend=False,
        hoverinfo="skip"
    ))

    # Female
    fig.add_trace(go.Scatter(
        x=[r["female"]],
        y=[r["country"]],
        mode="markers",
        marker=dict(size=16, color="#EC4899"),
        name="Female",
        legendgroup="female",
        showlegend=(_ == 0),
        hovertemplate=
        "<b>%{y}</b><br>Female: %{x:.1f}<extra></extra>"
    ))

    # Male
    fig.add_trace(go.Scatter(
        x=[r["male"]],
        y=[r["country"]],
        mode="markers",
        marker=dict(size=16, color="#2563EB"),
        name="Male",
        legendgroup="male",
        showlegend=(_ == 0),
        hovertemplate=
        "<b>%{y}</b><br>Male: %{x:.1f}<extra></extra>"
    ))

fig.update_layout(
    title=f"Average Earnings by Gender ({year})",
    template="plotly_white",
    height=420,
    xaxis_title="Average Earnings",
    yaxis_title="",
    hovermode="closest",
    legend=dict(
        orientation="h",
        y=1.08,
        x=0.75
    ),
    margin=dict(l=20, r=20, t=70, b=20)
)

st.plotly_chart(fig, width="stretch")

# ==========================
# Gender Gap Ranking
# ==========================

st.subheader("Gender Pay Gap Ranking")

bar = go.Figure()

bar.add_trace(go.Bar(
    x=d["gap"],
    y=d["country"],
    orientation="h",
    marker=dict(
        color=d["gap"],
        colorscale="RdPu"
    ),
    text=d["gap"].round(1),
    textposition="outside"
))

bar.update_layout(
    template="plotly_white",
    height=320,
    xaxis_title="Gender Pay Gap (%)",
    yaxis_title="",
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(bar, use_container_width=True)

# ==========================
# Data Table
# ==========================

st.subheader("Summary Table")

table = d[["country", "male", "female", "gap"]].copy()

table.columns = [
    "Country",
    "Male Wage",
    "Female Wage",
    "Pay Gap (%)"
]

st.dataframe(table, use_container_width=True)