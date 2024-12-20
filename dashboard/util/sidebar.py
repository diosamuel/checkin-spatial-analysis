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
NYC = pd.read_csv("dataset/NYC_final.csv")
TKY = pd.read_csv("dataset/TKY_final.csv")
# NYC = pd.read_csv("https://raw.githubusercontent.com/diosamuel/checkin-spatial-analysis/refs/heads/main/dataset/NYC_final.csv")
# TKY = pd.read_csv("https://raw.githubusercontent.com/diosamuel/checkin-spatial-analysis/refs/heads/main/dataset/TKY_final.csv")
dataset = {
    "NYC":NYC.sample(1000,random_state=42),
    "TKY":TKY.sample(1000,random_state=42)
}
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def WorkHour(venueId,city):
    venue = fetchAPI(venueId)
    st.session_state["selectedVenueJSON"] = venue
    if city=="NYC":
        place = NYC[NYC["venueId"] == venueId]
    else:
        place = TKY[TKY["venueId"] == venueId]
    place = place.reset_index()
    place['Day'] = pd.to_datetime(place['utcTimestamp']).dt.day_name()
    daysCount = place["Day"].value_counts().reset_index()
    print(daysCount)
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
        data = NYC["Kategori"].value_counts().head(10).sort_values(ascending=True).reset_index()
    else:
        data = TKY["Kategori"].value_counts().head(10).sort_values(ascending=True).reset_index()
    df = data
    fig = px.bar(
        df,
        x="count",
        y="Kategori",
        orientation="h",
        title=f"Top 10 Kategori Tempat Yang Sering Dikunjungi di {city}",
        labels={"count": "Total Visitor", "Kategori": ""},
        color_discrete_sequence=["orange"]
    )
    fig.update_layout(
        width=800,
        xaxis=dict(showgrid=True, gridcolor="lightgray", gridwidth=0.5),
        yaxis=dict(tickangle=-45),
        title=dict(x=0.25),
    )
    st.plotly_chart(fig, use_container_width=True)

def MostVisitedPlace(city):
    if city == "NYC":
        data = NYC["venueId"].value_counts().head(10).sort_values(ascending=True).reset_index()
    else:
        data = TKY["venueId"].value_counts().head(10).sort_values(ascending=True).reset_index()
    data.columns = ["venueId", "count"]
    def fetchId(venueId):
        ambil=fetchAPI(venueId)
        return ambil["response"]["venue"]["name"]
    data["venueName"] = data["venueId"].apply(fetchId)
    df = data
    fig = px.bar(
        df,
        x="count",
        y="venueName",  # Use venueName for y-axis
        orientation="h",
        title=f"Top 10 Tempat Yang Sering Dikunjungi di {city}",
        labels={"count": "Total Visitor", "venueName": "Venue Name"},
        color_discrete_sequence=["purple"]
    )

    # Update layout
    fig.update_layout(
        width=800,
        xaxis=dict(showgrid=True, gridcolor="lightgray", gridwidth=0.5),
        yaxis=dict(tickangle=-45),
        title=dict(x=0.25),
    )

    # Render chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

