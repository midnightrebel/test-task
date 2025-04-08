from src.core.exception import BaseHTTPException, status


class BetNotFound(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Bet not found"


class BetCannotBePlace(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Bet cannot be placing"


class BetCannotBeUpdated(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Bet cannot be updated"
