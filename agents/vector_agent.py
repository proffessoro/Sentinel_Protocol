from typing import List
from models import ContextData

class VectorAgent:
    """
    The Researcher: Searches and retrieves external context snippets.
    """
    def __init__(self):
        # Mock vector store responses keyed by (supplier, location) or similar keywords
        self._mock_knowledge_base = {
            "Taiwan": [
                ContextData("News", "Typhoon warning issued for coastal industrial zones in Taiwan.", 0.85),
                ContextData("Report", "Port congestion in Kaohsiung increasing delays by 3 days.", 0.7)
            ],
            "Malaysia": [
                ContextData("News", "Labor strikes reported in rubber manufacturing sector.", 0.9),
                ContextData("Weather", "Heavy monsoon rains expected to impact logistics.", 0.6)
            ]
        }

    def search_risks(self, supplier: str, location: str) -> List[ContextData]:
        """
        Provides real-time context on geopolitical or weather risks.
        """
        print(f"[Vector Agent] Searching for risks related to {supplier} in {location}...")
        results = []
        
        # Simple keyword matching for mock purposes
        if location in self._mock_knowledge_base:
            results.extend(self._mock_knowledge_base[location])
        
        # Add a generic result if nothing specific found
        if not results:
             results.append(ContextData("General", f"No specific high-risk news found for {location}.", 0.1))

        for res in results:
             if res.relevance_score > 0.5:
                 print(f"  -> Found relevant context: {res.content[:50]}...")
        
        return results
