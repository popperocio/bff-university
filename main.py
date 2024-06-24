from api import create_app
from api.routers import hotels

app = create_app()

app.include_router(hotels.router, prefix="/hotels")