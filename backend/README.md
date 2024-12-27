
# Execution

To execute the server, run the following from `backend/vassal/`:

``` bash
poetry run gunicorn -b 0.0.0.0:8000 'app:run_app()'
```