import numpy as np
from ortools.linear_solver import pywraplp

from fleets.fleet import Fleet
from simulation.scheduler import Scheduler
from services.planning.cyclic_scheduler import create_valid_offsets

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


def create_searcher_schedule(scheduler: Scheduler, search_fleet: Fleet) -> None:
    agents = search_fleet.agents
    # TODO: unpack agents into cyclic scheduler here


def optimise_agent_schedule(
    time_horizon: int,
    agent_ids: np.ndarray,
    quantities: np.ndarray,
    uptimes: np.ndarray,
    downtimes: np.ndarray,
    service_level: np.ndarray,
    threads: int = 16,
    time_limit_sec: int = 1200,
):
    if not (len(agent_ids) == len(quantities) == len(uptimes)
            == len(downtimes) == len(service_level)):
        raise ValueError("Provided arrays are not of the same length.")

    agent_data = {
        idx: dict(
            q=int(q),
            sl=float(sl),
            u=int(u),
            d=int(d),
            cycle=int(u + d),
        )
        for idx, q, u, d, sl in zip(
            agent_ids, quantities, uptimes, downtimes, service_level
        )
    }

    solver = pywraplp.Solver.CreateSolver("SAT")
    if solver is None:
        raise RuntimeError("Solver backend unavailable.")

    solver.EnableOutput()
    solver.SetNumThreads(threads)
    solver.SetTimeLimit(int(time_limit_sec * 1000))

    x = {}
    for idx, meta in agent_data.items():
        for offset in range(meta["cycle"]):
            x[(idx, offset)] = solver.IntVar(
                0, meta["q"], f"x_{idx}_{offset}"
            )

    gamma = solver.IntVar(0.0, solver.infinity(), "gamma")

    # All agents should be assigned to a searching cycle
    for idx, meta in agent_data.items():
        solver.Add(
            solver.Sum(
                x[(idx, o)] for o in range(meta["cycle"])
            ) == meta["q"]
        )

    phase_cache = {}
    active_cache = {}

    # Create insight into which searching cycles contribute to what timestep
    for meta in agent_data.values():
        key = (meta["u"], meta["d"])
        if key not in phase_cache:
            phases = create_valid_offsets(
                meta["u"],
                meta["d"],
                time_horizon,
            )
            phase_cache[key] = phases
            active_cache[key] = [
                np.flatnonzero(phase)
                for phase in phases
            ]

    # Ensure the objective is bounded by the lowest searching capacity
    constraints = [
        solver.RowConstraint(
            0.0,
            solver.infinity(),
            f"service_{t}",
        )
        for t in range(time_horizon)
    ]

    for c in constraints:
        c.SetCoefficient(gamma, -1.0)

    for idx in agent_ids:
        meta = agent_data[idx]
        key = (meta["u"], meta["d"])
        coeff = meta["sl"]

        for offset, active_times in enumerate(active_cache[key]):
            var = x[(idx, offset)]
            for t in active_times:
                constraints[t].SetCoefficient(var, coeff)

    solver.Maximize(gamma)

    print("Variables:", solver.NumVariables())
    print("Constraints:", solver.NumConstraints())
    status = solver.Solve()

    return solver, status, x, gamma


if __name__ == "__main__":
    n = 3
    horizon = 180

    rng = np.random.default_rng(0)

    agent_ids = np.arange(n)
    quantities = rng.integers(3, 45, n)
    uptimes = rng.integers(2, 20, n)
    downtimes = rng.integers(2, 24, n)
    service_level = rng.integers(1, 4, n)

    solver, status, x, gamma = optimise_agent_schedule(
        horizon,
        agent_ids,
        quantities,
        uptimes,
        downtimes,
        service_level,
    )

    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal:", gamma.solution_value())
    elif status == pywraplp.Solver.FEASIBLE:
        print("Feasible:", gamma.solution_value())
    else:
        print("No solution")
