## Deployment Setup
* `virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `python app.py` || `gunicorn -b 0.0.0.0:5000 app:app`