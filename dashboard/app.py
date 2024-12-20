import folium
import streamlit as st
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import pandas as pd
from util.sidebar import *
from util.fetching import fetchAPI
import uuid
from util.maps import RenderMap

# Sidebar for city selection
with st.sidebar:
    kota = st.selectbox("Pilih Kota", ("NYC", "TKY"))
    st.session_state["chosenCity"] = kota
    MostVisited(kota)
    MostVisitedPlace(kota)

# Main section
if "chosenCity" in st.session_state:
    chosen_city = st.session_state["chosenCity"]
    st.header(f"Peta Spasial Kota {chosen_city}")

    # Load dataset
    data = dataset[chosen_city]
    latlong = pd.DataFrame({
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    })

    # Render map
    output = st_folium(RenderMap(data, latlong), width=1000, height=500)

    # Display popular venues
    venue_counts = data['venueId'].value_counts().head(5).reset_index()
    venue_counts.columns = ["Venue", "Count"]
    st.header(f"Pilihan Tempat di {chosen_city}")

    for pos in range(0, len(venue_counts), 2):
        cols = st.columns(2)
        for i, col in enumerate(cols):
            if pos + i < len(venue_counts):
                loc = venue_counts.iloc[pos + i]
                with col:
                    data = fetchAPI(loc["Venue"])
                    venue_data = data.get("response", {}).get("venue", {})
                    st.subheader(venue_data.get("name", "Unknown"))
                    st.write(loc["Venue"])
                    address = venue_data.get("location", {}).get("address")
                    if address:
                        st.write(address)
                    st.write(venue_data.get("contact", "No contact info"))
                    st.write(venue_data.get("canonicalUrl", "No URL available"))
                    if st.button(f"Informasi {venue_data.get("name")}"):
                        @st.dialog(f"Informasi {venue_data.get("name")}")
                        def yapper():
                            st.session_state["selectedVenue"]=loc["Venue"]
                            WorkHour(st.session_state["selectedVenue"])
                        yapper()