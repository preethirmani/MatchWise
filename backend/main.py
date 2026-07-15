from fastapi import Depends, FastAPI
from sqlalchemy import text

try:
    from .database import get_db
except ImportError:
    from database import get_db

app = FastAPI(
    title = 'Matchwise API',
    description= 'Backend API for Matchwise Career Coach',
    version='0.1.0'
)

@app.get('/')
def read_root():
    return{
        'message':'Matchwise API running'
    }
    
@app.get('/health')
def health_check():
    return{
        'status':'healthy'
    }
    
@app.get('/health/database')
def database_health_check(db = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {
        "status": "healthy",
        "database": "connected",
        "result": result.scalar()
    }