from src.core.exception import BaseHTTPException, status


class EventNotFound(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Event not found"
