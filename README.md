## Deployment Setup
* `virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `python app.py` || `gunicorn -b 0.0.0.0:5000 app:app`

## Test Example
* GET: `https://awesome-reading.herokuapp.com/read?url=http://www.bbc.com/news/technology-39920141`