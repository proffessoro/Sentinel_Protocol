from orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()
    results = orchestrator.run_sentinel_protocol()

    print("\n" + "="*50)
    print("FINAL RISK REPORT")
    print("="*50)
    
    for res in results:
        print(f"Part ID: {res.part_id}")
        print(f"Risk Level: {res.risk_level}")
        print(f"Action: {res.action_recommendation}")
        print(f"Reasoning: {res.reasoning}")
        print("-" * 30)

if __name__ == "__main__":
    main()
