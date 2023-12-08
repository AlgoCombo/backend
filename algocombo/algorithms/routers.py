from typing import List, Union
from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from algorithms.core.movingAverageAlgorithm import MovingAverageAlgorithm

router = APIRouter()


class get_signal_request(BaseModel):
    inputs: List[List[Union[str, float, int]]]
    timeframe: str = "day"


@router.post("/get_signal/{algorithm_name}", tags=["algorithms"])
async def get_signal(algorithm_name: str, request_body: get_signal_request = Body(...)):
    """
    Get the signal for the given algorithm
    """
    algorithm_object = None
    if algorithm_name == "Moving Average Algorithm":
        algorithm_object = MovingAverageAlgorithm(
            request_body.inputs, request_body.timeframe)
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Invalid algorithm name"})

    signal = algorithm_object.get_signal()

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Signal retreived successfully", "signal": signal})
