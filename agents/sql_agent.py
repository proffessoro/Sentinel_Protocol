from typing import List
from models import InventoryItem

class SQLAgent:
    """
    The Bookkeeper: Accesses and extracts factual inventory metrics.
    """
    def __init__(self):
        # Mock database
        self._mock_db = [
            InventoryItem("P-101", "Microchip A1", "TechSource Inc", "Taiwan", 500, 100),  # 5 weeks supply (Low)
            InventoryItem("P-102", "Steel Casing", "MetalWorks", "Germany", 2000, 100),   # 20 weeks supply (OK)
            InventoryItem("P-103", "Rubber Gasket", "Elastomers Co", "Malaysia", 400, 80), # 5 weeks supply (Low)
            InventoryItem("P-104", "Display Panel", "ScreenCorp", "South Korea", 1200, 150), # 8 weeks supply (OK)
        ]

    def get_vulnerable_items(self, threshold_weeks: int = 6) -> List[InventoryItem]:
        """
        Identifies the initial set of low-coverage, high-risk items.
        """
        print(f"[SQL Agent] Querying ERP for items with < {threshold_weeks} weeks of stock...")
        vulnerable_items = []
        for item in self._mock_db:
            if item.weeks_of_supply < threshold_weeks:
                vulnerable_items.append(item)
                print(f"  -> Found vulnerable item: {item.name} ({item.weeks_of_supply} weeks)")
        
        return vulnerable_items
