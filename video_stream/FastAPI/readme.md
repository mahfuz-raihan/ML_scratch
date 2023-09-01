# FastAPI note

```python
from fastapi import FastAPI

# common format
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello world"}
```
