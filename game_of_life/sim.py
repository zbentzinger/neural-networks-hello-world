from constructs import Simulation, Board


if __name__ == '__main__':
    # Create a new simulation
    tick_rate = (1 / 60)
    randomness = 0.00
    sim = Simulation(
        Board(200, 200, entropy=randomness), ticks=10000, tick_rate=tick_rate
    )
    # Run the simulation
    sim.run()
