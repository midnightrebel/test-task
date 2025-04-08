from src.core.exception import BaseHTTPException, status


class EventNotFound(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Event not found"


class EventCannotBeAdded(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Event cannot be added"


class EventCannotBeUpdated(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Event cannot be updated"
