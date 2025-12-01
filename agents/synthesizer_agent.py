from typing import List
from models import InventoryItem, ContextData, RiskAssessment

class SynthesizerAgent:
    """
    The Analyst: Combines disparate data streams to form a decision.
    """
    def assess_risk(self, item: InventoryItem, context: List[ContextData]) -> RiskAssessment:
        """
        Assigns a final, actionable risk rating (CRITICAL/HIGH/LOW).
        """
        print(f"[Synthesizer Agent] Analyzing risk for {item.name}...")
        
        # Logic to simulate LLM reasoning
        # In a real scenario, this would construct a prompt and call an LLM.
        
        risk_score = 0
        reasons = []

        # Factor 1: Inventory Level
        if item.weeks_of_supply < 4:
            risk_score += 3
            reasons.append(f"Critical low stock ({item.weeks_of_supply} weeks).")
        elif item.weeks_of_supply < 6:
            risk_score += 2
            reasons.append(f"Low stock ({item.weeks_of_supply} weeks).")

        # Factor 2: External Context
        high_relevance_context = [c for c in context if c.relevance_score > 0.7]
        if high_relevance_context:
            risk_score += 3
            reasons.append(f"External risks detected: {[c.content for c in high_relevance_context]}")
        
        # Determine Rating
        if risk_score >= 5:
            rating = "CRITICAL"
            action = f"IMMEDIATE ACTION: Contact {item.supplier} and identify alternative sources."
        elif risk_score >= 2:
            rating = "HIGH"
            action = f"WARNING: Monitor {item.supplier} closely and draft backup orders."
        else:
            rating = "LOW"
            action = "Monitor situation normally."

        return RiskAssessment(
            part_id=item.part_id,
            risk_level=rating,
            action_recommendation=action,
            reasoning="; ".join(reasons)
        )
