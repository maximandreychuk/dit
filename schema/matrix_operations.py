from typing import List
from pydantic import BaseModel

class MatrixOperationRequest(BaseModel):
    matrix_1: List[List[int]]
    matrix_2: List[List[int]]
    operation_type: str


class MatrixErrorResponse(BaseModel):
    error: str
    operation_type: str