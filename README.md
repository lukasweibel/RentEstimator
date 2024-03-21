Activate environment

```
source .venv/bin/activate
```

python3 scrape/scrape.py

playwright codegen https://flatfox.ch/de/search/?&query=Winterthur&object_category=APARTMENT

export PYTHONPATH="${PYTHONPATH}:/path/to/RentEstimator"

export FLASK_APP=backend/service.py

flask run --host=0.0.0.0 --port=80

az container create --resource-group mdm-weibelu1-project1 --name mdm-rentestimator --image lukasweibel99/rentestimator:latest --dns-name-label mdm-rentestimator --ports 80

az container logs --resource-group mdm-weibelu1-project1 --name mdm-rentestimator

az container restart --resource-group mdm-weibelu1-project1 --name mdm-rentestimator

curl -X POST http://localhost:5000/predict \
 -H "Content-Type: application/json" \
 -d '{"area": 100, "rooms": 3, "zip": 8400}'
