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

if st.session_state is not None:
    st.session_state["selectedVenue"] = "42911d00f964a520f5231fe3"
with st.sidebar:
    kota:str = st.selectbox("Pilih Kota",("NYC", "TKY"))
    st.session_state["chosenCity"] = kota
    st.write(st.session_state["selectedVenue"])
    sidebar.WorkHour(st.session_state["selectedVenue"])
    sidebar.MostVisited(kota)


# Main
if st.session_state["chosenCity"]:
    st.header(f"Maps Of {st.session_state["chosenCity"]}")
    data = sidebar.dataset[st.session_state["chosenCity"]].head(100)
    # st.write(data)
    latlong = pd.DataFrame({
        "latitude":data["latitude"],
        "longitude":data["longitude"]
    })

m = folium.Map(location=[data.iloc[0]["latitude"],data.iloc[0]["longitude"]], zoom_start=10)
HeatMap(latlong).add_to(m)
Draw().add_to(m)
for pos in range(0,len(data)):
    folium.Marker(
        location=[data.iloc[pos]["latitude"],data.iloc[pos]["longitude"]],
        popup=data.iloc[pos]["venueId"]
    ).add_to(m)

output = st_folium(m, width=1000, height=1000)
if(output["last_object_clicked_popup"]):
    st.session_state["selectedVenue"] = output["last_object_clicked_popup"]
# st.rerun()
st.button("Ada apa disini?")
