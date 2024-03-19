Activate environment

```
source .venv/bin/activate
```

python3 scrape/scrape.py

playwright codegen https://flatfox.ch/de/search/?&query=Winterthur&object_category=APARTMENT

export PYTHONPATH="${PYTHONPATH}:/path/to/RentEstimator"

export FLASK_APP=backend/service.py

flask run

curl -X POST http://localhost:5000/predict \
 -H "Content-Type: application/json" \
 -d '{"area": 100, "rooms": 3, "zip": 8400}'
