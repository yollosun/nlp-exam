from fastapi import APIRouter
from typing import List
from domain.models import PegasusTransformer


router = APIRouter(
    prefix="/api/v2", tags=["v2"], responses={404: {"description": "Not found"}}
)


@router.post("/paraphrase")
def get_input_data(data: List[str]):

    model_name = "tuner007/pegasus_paraphrase"
    pegasus = PegasusTransformer(model_name)
    paraphrase = pegasus.paraphrase_english_text(data)

    return {"paraphrased_data": paraphrase}


@router.post("/paraphrase_ru")
def get_input_data(data: List[str]):

    model_name = "tuner007/pegasus_paraphrase"
    pegasus = PegasusTransformer(model_name)
    paraphrase = pegasus.paraphrase_russian_text(data)

    return {"paraphrased_data": paraphrase}
