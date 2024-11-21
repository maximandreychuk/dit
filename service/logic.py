from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse

from schema import (
    MatrixOperationRequest,
    MatrixErrorResponse,
    HeximalOperationRequest,
    HeximalErrorResponse
)
from .func import apply_matrix_operation

router = APIRouter(tags=["Operations"])


@router.get("/check_health", status_code=status.HTTP_200_OK)
async def check_health():
    try:
        return {"status": "OK"}
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Internal Server Error"}
        )


@router.post("/matrix_operations", responses={400: {"model": MatrixErrorResponse}})
async def matrix_operations(request: MatrixOperationRequest):
    try:
        result = apply_matrix_operation(request.matrix_1, request.matrix_2, request.operation_type)
        return {"matrix": result, "operation_type": request.operation_type}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))


@router.post("/heximal_operations", responses={400: {"model": HeximalErrorResponse}})
async def matrix_operations(request: HeximalOperationRequest):
    ...

