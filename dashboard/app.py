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

if st.session_state is not None:
    st.session_state["selectedVenue"] = "42911d00f964a520f5231fe3"
    
with st.sidebar:
    kota:str = st.selectbox("Pilih Kota",("NYC", "TKY"))
    st.session_state["chosenCity"] = kota
    st.write(st.session_state["selectedVenue"])
    # sidebar.WorkHour(st.session_state["selectedVenue"])
    sidebar.MostVisited(kota)


# Main
if st.session_state["chosenCity"]:
    st.header(f"Maps Of {st.session_state["chosenCity"]}")
    data = sidebar.dataset[st.session_state["chosenCity"]].head(100)
    latlong = pd.DataFrame({
        "latitude":data["latitude"],
        "longitude":data["longitude"]
    })

#render map
m = folium.Map(location=[data.iloc[0]["latitude"],data.iloc[0]["longitude"]], zoom_start=10)
HeatMap(latlong).add_to(m)
Draw().add_to(m)
fg = folium.FeatureGroup(name="State bounds")
output = st_folium(m, width=1000, height=400,feature_group_to_add=fg)

if(output["last_object_clicked_popup"]):
    st.session_state["selectedVenue"] = output["last_object_clicked_popup"]

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