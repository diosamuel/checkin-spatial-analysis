import folium
import streamlit as st
from folium.plugins import Draw
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
with st.sidebar:

    kota:str = st.selectbox(
    "Pilih Kota",
    ("New York City", "Tokyo")
    )

    st.header(f"Top 5 Most Visited in {kota}")

    col1, col2= st.columns(2)
    with col1:
        st.write("Restoran Minang")
        st.write("Restoran Minang")
    with col2:
        st.button("Kunjungi")
        st.button("Kunjungid")
    st.write("Kepadatan Tempat")
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig, use_container_width=True)

col1,col2 = st.columns(2)
with col1:
    container = st.container(border=True)
    container.markdown("### 10:30")
with col2:
    container = st.container(border=True)
    # container.markdown('<iframe scrolling="no" frameborder="no" clocktype="html5" style="overflow:hidden;border:0;margin:0;padding:0;width:480px;height:250px;" src="https://www.clocklink.com/clocks/HTML5/html5-world.html?&Tokyo&New_York&480&gray"></iframe>',unsafe_allow_html=True)

st.header(f"Maps Of Tokyo")
m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
Draw(export=True).add_to(m)

output = st_folium(m, width=1000, height=1000)
st.header("Ada apa disini?")
