from fastapi import FastAPI

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
    