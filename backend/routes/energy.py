from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import random  # For mock data generation

router = APIRouter()

# Mock data models
class EnergyData(BaseModel):
    timestamp: datetime
    consumption: float
    device_id: str
    location: str

class EnergySummary(BaseModel):
    total_consumption: float
    average_consumption: float
    peak_consumption: float
    period: str

# Mock data storage (in production, use database)
mock_data = []

@router.post("/data", response_model=EnergyData)
async def collect_energy_data(data: EnergyData):
    """Collect energy consumption data"""
    mock_data.append(data)
    return data

@router.get("/data", response_model=List[EnergyData])
async def get_energy_data(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    device_id: Optional[str] = None
):
    """Retrieve energy consumption data with optional filters"""
    filtered_data = mock_data

    if start_date:
        filtered_data = [d for d in filtered_data if d.timestamp >= start_date]
    if end_date:
        filtered_data = [d for d in filtered_data if d.timestamp <= end_date]
    if device_id:
        filtered_data = [d for d in filtered_data if d.device_id == device_id]

    return filtered_data

@router.get("/summary/{period}", response_model=EnergySummary)
async def get_energy_summary(period: str):
    """Get energy consumption summary for a period (daily, weekly, monthly)"""
    if not mock_data:
        raise HTTPException(status_code=404, detail="No data available")

    consumptions = [d.consumption for d in mock_data]
    total = sum(consumptions)
    average = total / len(consumptions)
    peak = max(consumptions)

    return EnergySummary(
        total_consumption=total,
        average_consumption=average,
        peak_consumption=peak,
        period=period
    )

@router.post("/data/generate")
async def generate_mock_data(count: int = 10):
    """Generate mock energy data for testing"""
    for _ in range(count):
        data = EnergyData(
            timestamp=datetime.now(),
            consumption=round(random.uniform(10, 100), 2),
            device_id=f"device_{random.randint(1, 5)}",
            location=f"location_{random.randint(1, 3)}"
        )
        mock_data.append(data)
    return {"message": f"Generated {count} mock data points"}
