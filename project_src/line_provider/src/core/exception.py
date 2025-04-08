from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server error"
    headers = None

    def __init__(self) -> None:
        super().__init__(
            status_code=self.status_code,
            detail=self.detail,
            headers=self.headers,
        )
