import argparse
import geopandas as gpd
from shapely.geometry import LineString

def import_trails(geojson_file):
    gdf = gpd.read_file(geojson_file)
    return gdf

def extract_trail_segments(gdf):
    segments = []
    for _, row in gdf.iterrows():
        geometry = row['geometry']
        if isinstance(geometry, LineString):
            segments.append(geometry)
        elif hasattr(geometry, 'geoms'):  # MultiLineString
            segments.extend(list(geometry.geoms))
    return segments

def create_trail_library(geojson_file):
    gdf = import_trails(geojson_file)
    segments = extract_trail_segments(gdf)
    return segments

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process trail data from a GeoJSON file.')
    parser.add_argument('file_path', type=str, help='Path to the GeoJSON file containing trail data')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Use the file path from command line argument
    trail_segments = create_trail_library(args.file_path)
    
    # Print some basic info about the extracted segments
    print(f"Extracted {len(trail_segments)} trail segments.")

if __name__ == "__main__":
    main()