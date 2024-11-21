from pydantic import BaseModel

class HeximalOperationRequest(BaseModel):
    hex_1: str
    hex_2: str
    operation_type: str

class HeximalErrorResponse(BaseModel):
    error: str
    operation_type: str