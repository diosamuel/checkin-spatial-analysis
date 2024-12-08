import folium
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
from util.fetching import fetchAPI

NYC = pd.read_csv("dataset/dataset_TSMC2014_NYC.csv")
TKY = pd.read_csv("dataset/dataset_TSMC2014_TKY.csv")
dataset = {
    "NYC":NYC,
    "TKY":TKY
}

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 1000px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def WorkHour(venueId="42911d00f964a520f5231fe3"):
    venue = fetchAPI(venueId)
    st.session_state["selectedVenueJSON"] = venue
    place = NYC[NYC["venueId"] == venueId]
    place = place.reset_index()
    place['Day'] = pd.to_datetime(place['utcTimestamp']).dt.day_name()
    daysCount = place["Day"].value_counts().reset_index()
    fixed_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    fig = px.bar(
        daysCount,
        x="Day",
        y="count",
        orientation="v",
        title=f"Pengunjung {venue["response"]["venue"]["name"]}",
        labels={"count": "Total Pengunjung", "day": "Hari"},
        color_discrete_sequence=["skyblue"],
        category_orders={"Day":fixed_order}
    )
    fig.update_layout(
        width=800,
        xaxis=dict(showgrid=True, gridcolor="lightgray", gridwidth=0.5),
        yaxis=dict(tickangle=-45),
        title=dict(x=0.25),
    )
    st.plotly_chart(fig, use_container_width=True)


def MostVisited(city):
    if city == "NYC":
        data = NYC["venueCategory"].value_counts().head(10).sort_values(ascending=True).reset_index()
    else:
        data = TKY["venueCategory"].value_counts().head(10).sort_values(ascending=True).reset_index()
    df = data
    fig = px.bar(
        df,
        x="count",
        y="venueCategory",
        orientation="h",
        title=f"Top 10 Tempat Populer di {city}",
        labels={"count": "Total Visitor", "venueCategory": ""},
        color_discrete_sequence=["orange"]
    )
    fig.update_layout(
        width=800,
        xaxis=dict(showgrid=True, gridcolor="lightgray", gridwidth=0.5),
        yaxis=dict(tickangle=-45),
        title=dict(x=0.25),
    )
    st.plotly_chart(fig, use_container_width=True)
