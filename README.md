# Collection Drenowatz

## Data processing

### Generate overview data and thumbnails

To generate thumbnails, `libvips` is used. Install the package, e.g. for Debian-based systems:

```bash
sudo apt-get install libvips
```

Then install Python dependencies:

```bash
pip install -r requirements
```

To generate the thumbnails (in `ui/public/thumbnails`) and overview data (`ui/public/overview.json`):

```bash
cd process
python generate_overview_data.py
```

## UI

### Development

Install project dependencies:

``` bash
cd ui
npm install
```

Run development server:

``` bash
npm run dev
```

Build production assets:

``` bash
npm run build
```

Build and run production server:

``` bash
docker-compose up -d --build ui
```

## Find stamp positions in images

Finding the stamp positions in the images is executed in a separate step.
It requires the data to be present in the `./data` folder, namely the `MRZ_Kunstwerke.json`, the full images and the stamps.
They can be downloaded with the `bin/download` script.

The stamp positioning process can then be initiated with docker:

``` bash
docker-compose run --build stamps
```

It will produce a `./data/stamp_positions.json` file that can then be further processed.
