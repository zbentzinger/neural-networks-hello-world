from constructs import SimulationV1, BoardV1


def sim_v1():
    # Create a new simulation
    tick_rate = (1 / 60)
    randomness = 0.00
    sim = SimulationV1(
        BoardV1(200, 200, entropy=randomness), ticks=10000, tick_rate=tick_rate
    )
    # Run the simulation
    sim.run()



if __name__ == '__main__':
    sim_v1()
