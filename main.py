from api import create_app
from api.routers import hotels, reservations
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
app = create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins= os.getenv('FRONTEND_URL'),
    allow_credentials=True,
    allow_methods= ["GET", "POST", "OPTIONS", "PUT"],
    allow_headers=["*"],
)


app.include_router(hotels.router, prefix="/hotels")
app.include_router(reservations.router, prefix="/reservation")