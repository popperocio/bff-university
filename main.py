from api import create_app
from api.routers import hotels, reservations

app = create_app()

app.include_router(hotels.router, prefix="/hotels")
app.include_router(reservations.router, prefix="/reservation")