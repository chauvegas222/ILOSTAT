import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/DATA_CLEAN_8.5.1_GENDER_PAY_GAP_2018_2025.csv"
    )

    df = df.rename(columns={
        "ref_area.label":"country",
        "time":"year",
        "Male_clean":"male",
        "Female_clean":"female",
        "GPG_percent_clean":"gap"
    })

    df = df[df.country.isin([
        "Viet Nam",
        "Thailand",
        "Philippines"
    ])]

    df = df[(df.year>=2018) & (df.year<=2025)]

    return df


@st.cache_data
def yearly_summary():

    df = load_data()

    summary = (
        df.groupby(["country","year"], as_index=False)
          .agg({
              "male":"mean",
              "female":"mean",
              "gap":"mean"
          })
    )

    return summary
