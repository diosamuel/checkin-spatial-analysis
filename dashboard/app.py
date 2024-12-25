import folium
import streamlit as st
from folium.plugins import HeatMap
from streamlit_folium import st_folium,folium_static
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
    kategori = st.selectbox("Kategori",('Transportasi Umum', 'Tempat Makan', 'Belanja & Hiburan',
       'Tempat Kerja', 'Layanan Publik', 'Wisata',
       'Residental (Perumahan/Privat)'))
    if kategori:
        WorkDayCategory(kategori,kota)
    MostVisitedPlace(kota)

# Main section
if "chosenCity" in st.session_state:
    chosen_city = st.session_state["chosenCity"]
    st.header(f"Selamat Datang di Dashboard Kota! {chosen_city}")
    st.markdown(f"### Peta Spasial Kota {chosen_city}")

    # Load dataset
    data = dataset[chosen_city]
    latlong = pd.DataFrame({
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    })

    # Render map
    heat = st.checkbox("heatmap")
    density = st.checkbox("density")
    pinpoin = st.checkbox("pinpoin")
    rendered = RenderMap(data, latlong,chosen_city,heatmap=heat,density=density,pinpoin=pinpoin)
    output = folium_static(rendered, width=1000, height=500)
    # Display popular venues
    venue_counts = data['venueId'].value_counts().head(10).reset_index()
    venue_counts.columns = ["Venue", "Count"]
    st.header(f"Pilihan Tempat di {chosen_city}")

    for pos in range(0, len(venue_counts), 2):
        cols = st.columns(2)
        for i, col in enumerate(cols):
            if pos + i < len(venue_counts):
                loc = venue_counts.iloc[pos + i]
                with col:
                    st.session_state["selectedVenue"] = loc["Venue"]
                    data = fetchAPI(loc["Venue"])
                    venue_data = data.get("response", {}).get("venue", {})
                    st.subheader(venue_data.get("name", "Unknown"))
                    address = venue_data.get("location", {}).get("address")
                    if address:
                        st.write(address)
                    st.write(venue_data.get("contact", "No contact info"))
                    st.write(venue_data.get("canonicalUrl", "No URL available"))
                    if st.button(f"Informasi {venue_data.get('name')}"):
                        @st.dialog(f"Informasi {venue_data.get("name")} ")
                        def yapper():
                            WorkDay(st.session_state["selectedVenue"],chosen_city)
                            WorkHour(st.session_state["selectedVenue"],chosen_city)
                            lat = venue_data.get("location", {}).get("lat")
                            lng = venue_data.get("location", {}).get("lng")
                            map_center = [lat, lng]
                            m = folium.Map(location=map_center, zoom_start=20)
                            folium.Marker(location=map_center, popup=venue_data.get("name", "Unknown")).add_to(m)
                            folium_static(m, width=700, height=500)
                        yapper()