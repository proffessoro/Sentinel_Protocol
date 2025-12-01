from typing import List
from agents.sql_agent import SQLAgent
from agents.vector_agent import VectorAgent
from agents.synthesizer_agent import SynthesizerAgent
from models import RiskAssessment

class Orchestrator:
    """
    The Router: Manages dependencies, control flow, and data transformation.
    """
    def __init__(self):
        self.sql_agent = SQLAgent()
        self.vector_agent = VectorAgent()
        self.synthesizer_agent = SynthesizerAgent()

    def run_sentinel_protocol(self) -> List[RiskAssessment]:
        """
        Executes the Sentinel Protocol workflow.
        """
        print("\n--- Starting Sentinel Protocol ---\n")
        
        # Step 1: Fact Retrieval (SQL)
        vulnerable_items = self.sql_agent.get_vulnerable_items()
        
        assessments = []

        # Step 2: Contextual Retrieval (Vector) & Step 3: Synthesis
        for item in vulnerable_items:
            print(f"\nProcessing Item: {item.name} ({item.part_id})")
            
            # Get context
            context_data = self.vector_agent.search_risks(item.supplier, item.location)
            
            # Synthesize
            assessment = self.synthesizer_agent.assess_risk(item, context_data)
            assessments.append(assessment)
            
            print(f"  => Result: {assessment.risk_level} - {assessment.action_recommendation}")

        print("\n--- Sentinel Protocol Complete ---\n")
        return assessments
