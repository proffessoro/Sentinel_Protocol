from dataclasses import dataclass
from typing import List, Optional

@dataclass
class InventoryItem:
    part_id: str
    name: str
    supplier: str
    location: str
    current_stock: int
    burn_rate_weekly: int
    
    @property
    def weeks_of_supply(self) -> float:
        if self.burn_rate_weekly == 0:
            return float('inf')
        return self.current_stock / self.burn_rate_weekly

@dataclass
class ContextData:
    source: str  # e.g., "News", "Email"
    content: str
    relevance_score: float

@dataclass
class RiskAssessment:
    part_id: str
    risk_level: str  # CRITICAL, HIGH, LOW
    action_recommendation: str
    reasoning: str
