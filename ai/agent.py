import random
from analysis.extractor import log_data

class PhysicsAI:
    def __init__(self, sandbox):
        self.sandbox = sandbox
        self.memory = []

    def run_episode(self):
        config = self.generate_random_config()
        result = self.sandbox.run(config)
        self.memory.append((config, result))
        log_data(config, result)

    def generate_random_config(self):
        geometry = [random.uniform(-1, 1) for _ in range(5)]
        energy = random.uniform(-1000, 1000)
        return {'geometry': geometry, 'energy': energy}
