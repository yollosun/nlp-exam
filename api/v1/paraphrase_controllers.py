from fastapi import APIRouter
from typing import List
from domain.pegasus import get_response


router = APIRouter(
    prefix="/api/v1", tags=["v1"], responses={404: {"description": "Not found"}}
)


@router.post("/paraphrase")
def get_input_data(data: List[str]):
    paraphrase = []
    for i in data:
        a = get_response(i, 1)
        paraphrase.append(a)

    return {"paraphrased_data": paraphrase}
