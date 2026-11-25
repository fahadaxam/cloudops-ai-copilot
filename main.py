
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Create the FastAPI application
app = FastAPI(
    title="CloudOps AI Copilot",
    description="Cloud incident analysis and AI automation platform",
    version="0.1.0"
)


# Define the expected incident information
class Incident(BaseModel):
    service: str = Field(
        min_length=2,
        description="Cloud service experiencing the incident"
    )
    symptom: str = Field(
        min_length=5,
        description="Description of the problem"
    )


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CloudOps AI Copilot",
        "version": "0.1.0"
    }


# Incident analysis endpoint
@app.post("/analyze")
def analyze_incident(incident: Incident):
    recommendations = [
        "Review cloud monitoring metrics",
        "Inspect application and infrastructure logs",
        "Check recent configuration or deployment changes"
    ]

    return {
        "service": incident.service,
        "symptom": incident.symptom,
        "analysis": (
            "Initial analysis completed using predefined "
            "troubleshooting recommendations."
        ),
        "recommendations": recommendations,
        "ai_enabled": False
    }
