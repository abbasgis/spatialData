from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base, SessionLocal
from app.routers import sentinel, landsat
# For django imports
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
from importlib.util import find_spec
from fastapi.staticfiles import StaticFiles
from django.conf import settings
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

# Export Django settings env variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spatialData.settings')

# Get Django WSGI app
django_app = get_wsgi_application()

# Import a model
# And always import your models after you export settings
# and you get Django WSGI app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve Django static files
app.mount('/static',
          StaticFiles(
              directory=os.path.normpath(
                  os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
              )
          ),
          name='static',
          )
app.mount('/django', WSGIMiddleware(django_app))


@app.get("/")
def read_root():
    response = RedirectResponse(url='/docs')
    return response


@app.get("/admin")
def django_admin():
    response = RedirectResponse(url='/django/admin')
    return response

app.include_router(sentinel.router)
app.include_router(landsat.router)