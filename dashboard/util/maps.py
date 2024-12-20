from folium.plugins import HeatMap
from folium.plugins import Draw
from streamlit_folium import st_folium
import folium
import geopandas as gpd
def RenderMap(data,latlong):
    m = folium.Map(location=[data.iloc[0]["latitude"],data.iloc[0]["longitude"]], zoom_start=10)
    borough = gpd.read_file('dataset/Borough Boundaries.geojson')
    HeatMap(latlong).add_to(m)
    # Draw().add_to(m)
    folium.GeoJson(borough).add_to(m)
    return m