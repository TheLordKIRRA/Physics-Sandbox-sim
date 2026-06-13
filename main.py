from engine.simulation import SimulationSandbox
from ai.agent import PhysicsAI
from analysis.extractor import TheoryExtractor

if __name__ == "__main__":
    sim = SimulationSandbox()
    ai = PhysicsAI(sim)

    try:
        while True:
            ai.run_episode()
    except KeyboardInterrupt:
        print("🛑 Interrupted by user. Saving theory report...")
        TheoryExtractor.generate_report(ai.memory)
        print("✅ Report saved as 'theory_report.txt'")
