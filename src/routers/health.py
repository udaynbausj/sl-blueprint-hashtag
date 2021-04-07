from fastapi import APIRouter
from fastapi import status

router = APIRouter()


@router.get('/health', status_code=status.HTTP_200_OK)
async def health_api():
    return {
        'health': 'everything is alright'
    }
