"""
IX-CerealKiller REST API Server

Provides HTTP endpoints to analyze forensic incident reports and respond to queries
related to cybercrime pattern recognition and profiling.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXCerealKillerQueryProcessor

app = FastAPI()
query_processor = IXCerealKillerQueryProcessor()

class IncidentRequest(BaseModel):
    incident_report: str

@app.post("/analyze")
async def analyze_incident(request: IncidentRequest):
    if not request.incident_report or request.incident_report.strip() == "":
        raise HTTPException(status_code=400, detail="Incident report must not be empty.")
    try:
        result = query_processor.process_query(f"analyze incident {request.incident_report}")
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8043)
