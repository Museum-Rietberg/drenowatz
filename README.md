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
