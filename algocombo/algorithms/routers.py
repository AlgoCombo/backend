from typing import List, Union
from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from algorithms.core.movingAverageAlgorithm import MovingAverageAlgorithm
from algorithms.core.relativeStrengthIndexAlgorithm import RelativeStrengthIndexAlgorithm

router = APIRouter()


class get_signal_request(BaseModel):
    inputs: List[List[Union[str, float, int]]]
    timeframe: str = "day",
    args: List = []
    kwargs: dict = {}


@router.post("/get_signal/{algorithm_name}", tags=["algorithms"])
async def get_signal(algorithm_name: str, request_body: get_signal_request = Body(...)):
    """
    Get the signal for the given algorithm
    """
    algorithm_object = None
    if algorithm_name == "MovingAverageAlgorithm":
        algorithm_object = MovingAverageAlgorithm(
            request_body.inputs, request_body.timeframe)
    elif algorithm_name == "RelativeStrengthIndexAlgorithm":
        algorithm_object = RelativeStrengthIndexAlgorithm(
            request_body.inputs, request_body.timeframe)
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Invalid algorithm name"})

    signal = algorithm_object.get_signal(
        *request_body.args, **request_body.kwargs)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Signal retreived successfully", "signal": signal})
