# trail-buddy
Find interesting trails to hike, run, or bike

## Setup

1. Create a Python virtual environment (`python3 -m venv env && source env/bin/activate`)
1. Install dependencies (`pip install -r requirements.txt`)
1. Download a GeoJSON dataset (e.g. `Trails.geojson`) for testing. You may put it in the data/ folder for convenience.
1. Run `python generate data/Trails.geojson` to generate trail segments and preview the first few.