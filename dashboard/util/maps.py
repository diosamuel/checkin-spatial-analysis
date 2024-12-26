from folium.plugins import HeatMap
from folium.plugins import Draw
from streamlit_folium import st_folium
import folium
import geopandas as gpd
from util.sidebar import NYC,TKY
from util.fetching import fetchAPI

def RenderMap(data,latlong,city,heatmap=False,density=False,pinpoin=False):
    m = folium.Map(location=[data.iloc[0]["latitude"],data.iloc[0]["longitude"]], zoom_start=10)
    folium.raster_layers.TileLayer(
        tiles="https://basemaps.arcgis.com/arcgis/rest/services/World_Basemap_v2/VectorTileServer/tile/{z}/{y}/{x}",
        attr="Esri Oceans Basemap",
        name="Esri Oceans",
        control=True
    ).add_to(m)
    if city=="NYC":
        # Get the top 10 most frequent venueId values
        top_venues = NYC["venueId"].value_counts().head(10).reset_index()
        top_venues.columns = ["venueId", "count"]
        # Merge with the original DataFrame to get latitude and longitude
        data = top_venues.merge(NYC, on="venueId")[["venueId", "latitude", "longitude"]].drop_duplicates()
        # Add markers for each venue
        for pos in range(len(data)):
            ambilYap = fetchAPI(data.iloc[pos]["venueId"])
            venue_data = ambilYap.get("response", {}).get("venue", {})
            folium.Marker(
                location=[data.iloc[pos]["latitude"], data.iloc[pos]["longitude"]],
                popup=venue_data.get("name", "Unknown")
            ).add_to(m)
        if density:
            folium.raster_layers.TileLayer(
                tiles="https://tiles.arcgis.com/tiles/4yjifSiIG17X0gW4/arcgis/rest/services/NewYorkCity_PopDensity/MapServer/tile/{z}/{y}/{x}",
                attr="New York Density",
                name="NY Density",
                overlay=True,
                control=True
            ).add_to(m)
    else:
        # Get the top 10 most frequent venueId values
        top_venues = TKY["venueId"].value_counts().head(10).reset_index()
        top_venues.columns = ["venueId", "count"]
        # Merge with the original DataFrame to get latitude and longitude
        data = top_venues.merge(TKY, on="venueId")[["venueId", "latitude", "longitude"]].drop_duplicates()
        # Add markers for each venue
        for pos in range(len(data)):
            ambilYap = fetchAPI(data.iloc[pos]["venueId"])
            venue_data = ambilYap.get("response", {}).get("venue", {})
            folium.Marker(
                location=[data.iloc[pos]["latitude"], data.iloc[pos]["longitude"]],
                popup=venue_data.get("name", "Unknown")
            ).add_to(m)
        if density:
            folium.raster_layers.TileLayer(
                tiles="https://tiles.arcgis.com/tiles/4yjifSiIG17X0gW4/arcgis/rest/services/Tokyo_PopDensity/MapServer/tile/{z}/{y}/{x}",
                attr="Tokyo Density",
                name="Tokyo Density",
                overlay=True,
                control=True
            ).add_to(m)
    if heatmap:
        HeatMap(latlong).add_to(m)

    if pinpoin:
        for pos in range(0,len(data)):
            folium.Marker(
                location=[data.iloc[pos]["latitude"],data.iloc[pos]["longitude"]],
                popup=data.iloc[pos]["venueId"]
            ).add_to(m)
    # Draw().add_to(m)
    # folium.GeoJson(borough).add_to(m)
    return m