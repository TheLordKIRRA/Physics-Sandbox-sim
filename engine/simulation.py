import numpy as np

class SimulationSandbox:
    def __init__(self):
        self.constants = {
            'c': 299792458,
            'hbar': 1.0545718e-34,
            'G': 6.67430e-11,
            'epsilon_0': 8.854e-12,
            'kB': 1.380649e-23  # Boltzmann constant
        }

    def run(self, config):
        # --- Physical Inputs ---
        geometry = np.array(config['geometry'])
        energy_input = config['energy']

        # --- Core Energy Dynamics ---
        field_interaction = np.sin(np.sum(geometry))  # placeholder field interaction
        usable_work = max(0.0, field_interaction + energy_input)

        # --- Thermodynamic Modeling ---
        heat_loss = 0.1 * abs(usable_work)  # 10% lost as heat (irreversible)
        internal_energy = usable_work - heat_loss

        # Estimate entropy change from heat loss
        temperature = 300  # Assume 300K system
        delta_S = heat_loss / (temperature * self.constants['kB'])  # ΔS = Q/TkB

        # Thermal efficiency
        efficiency = internal_energy / (energy_input + 1e-9)  # avoid div by zero

        # Metric result is derived from field
        metric_result = usable_work

        return {
            'metric_result': metric_result,
            'energy_condition_violated': metric_result < 0,
            'internal_energy': internal_energy,
            'heat_loss': heat_loss,
            'entropy_generated': delta_S,
            'thermal_efficiency': efficiency
        }
