from fastapi import FastAPI, Request, Header, HTTPException
import json

app = FastAPI()

# Route test simple
@app.get("/")
def read_root():
    return {"message": "Server is running"}

# Webhook GitHub
@app.post("/github-webhook/")
async def github_webhook(request: Request, x_github_event: str = Header(None)):
    try:
        payload = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    print("\n====== WEBHOOK REÇU ======")
    print(f"Event: {x_github_event}")
    print(json.dumps(payload, indent=2))
    print("===========================\n")

    return {"status": "received"}