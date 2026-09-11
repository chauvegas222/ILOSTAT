import streamlit as st
import plotly.express as px
from src.load_data import load_data

df = load_data()

st.title("Data Explorer")

heat = df.pivot_table(
    index="country",
    columns="year",
    values="gap",
    aggfunc="mean"
)

import plotly.express as px

fig = px.imshow(
    heat,
    text_auto=".1f",
    aspect="auto",
    color_continuous_scale="RdPu"
)

fig.update_layout(
    title="Average Gender Pay Gap Heatmap"
)

st.plotly_chart(fig, width="stretch")

st.download_button(
    "Download Clean Dataset",
    df.to_csv(index=False),
    "gender_gap_clean.csv"
)

st.dataframe(df, width="stretch")