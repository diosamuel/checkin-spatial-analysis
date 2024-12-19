import folium
import streamlit as st
from folium.plugins import HeatMap
from folium.plugins import Draw
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
from util import sidebar
from util.tools import haversine
from util.fetching import fetchAPI
import random
import uuid

if st.session_state is not None:
    st.session_state["selectedVenue"] = "42911d00f964a520f5231fe3"

with st.sidebar:
    kota:str = st.selectbox("Pilih Kota",("NYC", "TKY"))
    st.session_state["chosenCity"] = kota
    sidebar.WorkHour(st.session_state["selectedVenue"])
    sidebar.MostVisited(kota)
    sidebar.MostVisitedPlace(kota)


# Main
if st.session_state["chosenCity"]:
    st.header(f"Maps Of {st.session_state["chosenCity"]}")
    data = sidebar.dataset[st.session_state["chosenCity"]]
    latlong = pd.DataFrame({
        "latitude":data["latitude"],
        "longitude":data["longitude"]
    })

#render map
m = folium.Map(location=[data.iloc[0]["latitude"],data.iloc[0]["longitude"]], zoom_start=10)
HeatMap(latlong).add_to(m)
Draw().add_to(m)
fg = folium.FeatureGroup(name="State bounds")
output = st_folium(m, width=1000, height=500,feature_group_to_add=fg)

if(output["last_object_clicked_popup"]):
    st.session_state["selectedVenue"] = output["last_object_clicked_popup"]

#sample
venue_counts = sidebar.dataset[st.session_state["chosenCity"]]['venueId'].value_counts().sort_values(ascending=False)

st.header(f"Tempat Populer di {st.session_state["chosenCity"]}")
df = venue_counts.head(5).reset_index()
for pos in range(len(df)-1):
    col1,col2 = st.columns(2)
    # with col1:
    loc = df.iloc[pos]
    with st.container():
        data=fetchAPI(loc["venueId"])
        data = data["response"]["venue"]
        st.header(data["name"])
        st.write(loc["venueId"])
        if("address" in data["location"]):
            st.write(data["location"]["address"])
        st.write(data["contact"])
        st.write(data["canonicalUrl"])
    # with col2:
    #     loc = df.iloc[pos+1]
    #     with st.container():
    #         data=fetchAPI(loc["venueId"])
    #         data = data["response"]["venue"]
    #         st.header(data["name"])
    #         st.write(loc["venueId"])
    #         if("address" in data["location"]):
    #             st.write(data["location"]["address"])
    #         st.write(data["contact"])
    #         st.write(data["canonicalUrl"])
    #         if st.button("Lihat Jam Sibuk", key=uuid.uuid1()):
    #             with st.sidebar:
    #                 sidebar.WorkHour(loc["venueId"])

# if st.button("Ada apa disini?"):
#     radius = output["all_drawings"][0]["properties"]["radius"]
#     selectedArea = output["all_drawings"][0]["geometry"]["coordinates"]
#     st.write(selectedArea)
#     for i in range(len(sidebar.NYC)):
#         loc = sidebar.NYC.iloc[i]
#         distance = haversine(selectedArea[1], selectedArea[0], loc["latitude"], loc["longitude"])
#         if distance <= radius:
#             fg.add_child(
#                 folium.Marker(
#                 location=[loc["latitude"], loc["longitude"]],
#                 popup="Ini nih"
#             ).add_to(m)
#             )
#             st.write(loc)
#         else:
#             st.write("No found")