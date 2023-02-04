from pydantic import BaseModel
class Settings(BaseModel):
    authjwt_secret_key: str = '4b03c7d2117a9ce3715f2bf3028c87aadc2db39c5ce926a0a35c55e565b26ec1'