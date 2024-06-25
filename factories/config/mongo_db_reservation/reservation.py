from ..utils import parse_env_variable


class ReservationMongoDB:
    MONGO_DB_URL: str = parse_env_variable("MONGO_DB_URL")
    MONGO_DB_DATABASE: str = parse_env_variable("MONGO_DB_DATABASE")
    MONGO_DB_COLLECTION = parse_env_variable("MONGO_DB_COLLECTION")
