# fastapi 서버 실행 명령어: uvicorn main:app --reload --port 8009 (port 번호 변경 시, gene.py에 있는 port 번호도 함께 수정)
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.augmentation_router import router as augmentation_router
from api.recommendation_router import router as recomendation_router
from api.preprocessing_router import router as preprocessing_router
import os

app = FastAPI()

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

app.include_router(augmentation_router, prefix="/augmentation", tags=['augmentation'])
app.include_router(recomendation_router, prefix="/recommendation", tags=['recommendation'])
app.include_router(preprocessing_router, prefix="/preprocessing", tags=['preprocessing'])

app.get('/')
def main():
    return "connection success!"

app.get('/test')
def main():
    return "connection success!"