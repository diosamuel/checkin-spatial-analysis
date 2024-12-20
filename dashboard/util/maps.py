from folium.plugins import HeatMap
from folium.plugins import Draw
from streamlit_folium import st_folium
import folium
import geopandas as gpd
def RenderMap(data,latlong,city,heatmap=False,density=False,pinpoin=False):
    m = folium.Map(location=[data.iloc[0]["latitude"],data.iloc[0]["longitude"]], zoom_start=10)
    folium.raster_layers.TileLayer(
        tiles="https://basemaps.arcgis.com/arcgis/rest/services/World_Basemap_v2/VectorTileServer/tile/{z}/{y}/{x}",
        attr="Esri Oceans Basemap",
        name="Esri Oceans",
        control=True
    ).add_to(m)
    if city=="NYC":
        if density:
            folium.raster_layers.TileLayer(
                tiles="https://tiles.arcgis.com/tiles/4yjifSiIG17X0gW4/arcgis/rest/services/NewYorkCity_PopDensity/MapServer/tile/{z}/{y}/{x}",
                attr="New York Density",
                name="NY Density",
                overlay=True,
                control=True
            ).add_to(m)
    else:
        if density:
            folium.raster_layers.TileLayer(
                tiles="https://tiles.arcgis.com/tiles/4yjifSiIG17X0gW4/arcgis/rest/services/Tokyo_PopDensity/MapServer/tile/{z}/{y}/{x}",
                attr="Tokyo Density",
                name="Tokyo Density",
                overlay=True,
                control=True
            ).add_to(m)
    # borough = gpd.read_file('dataset/Borough Boundaries.geojson')
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