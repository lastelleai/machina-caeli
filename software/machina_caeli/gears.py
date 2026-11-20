"""Search for printable gear trains that match each planet's pace.

The single input shaft is Earth (one turn per Earth year). Each planet needs
the ratio  planet_turns / earth_turns = L_dot_planet / L_dot_earth.

A compound train of k stages has ratio (a1*a2*...*ak) / (b1*b2*...*bk), with
every tooth count inside [min_teeth, max_teeth]. We take the fewest stages
whose drift stays under the target, and report the drift so the error is
published per planet.

Drift is how far the printed planet strays from the true one, in degrees of
its own orbit per Earth century.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

from .ephemeris import EARTH, PLANETS, Planet, ratio_to_earth

EARTH_DEG_PER_CENTURY = EARTH.L_dot_deg_cy


@dataclass(frozen=True)
class Train:
    planet: str
    target: float
    drivers: tuple[int, ...]
    driven: tuple[int, ...]

    @property
    def ratio(self) -> float:
        n = d = 1
        for a in self.drivers:
            n *= a
        for b in self.driven:
            d *= b
        return n / d

    @property
    def stages(self) -> int:
        return len(self.drivers)

    @property
    def drift_deg_per_century(self) -> float:
        return abs(self.ratio - self.target) * EARTH_DEG_PER_CENTURY

    @property
    def rel_error_ppm(self) -> float:
        return abs(self.ratio / self.target - 1.0) * 1e6


def _products(k: int, lo: int, hi: int) -> dict[int, tuple[int, ...]]:
    """Every product of k tooth counts in [lo, hi], with one factorisation."""
    out: dict[int, tuple[int, ...]] = {}
    for combo in itertools.combinations_with_replacement(range(lo, hi + 1), k):
        p = 1
        for c in combo:
            p *= c
        out.setdefault(p, combo)
    return out


def best_train(planet: Planet, stages: int, lo: int, hi: int) -> Train | None:
    target = ratio_to_earth(planet)
    prods = _products(stages, lo, hi)
    best: Train | None = None
    for den, den_f in prods.items():
        num = round(target * den)
        for n in (num - 1, num, num + 1):
            num_f = prods.get(n)
            if num_f is None:
                continue
            t = Train(planet.name, target, num_f, den_f)
            if best is None or t.drift_deg_per_century < best.drift_deg_per_century:
                best = t
    return best


def design(
    lo: int = 12,
    hi: int = 100,
    max_drift_deg_per_century: float = 0.5,
    max_stages: int = 3,
) -> list[Train]:
    trains: list[Train] = []
    for p in PLANETS:
        if p.name == "Earth":
            continue
        chosen: Train | None = None
        for k in range(1, max_stages + 1):
            t = best_train(p, k, lo, hi)
            if t is None:
                continue
            if chosen is None or t.drift_deg_per_century < chosen.drift_deg_per_century:
                chosen = t
            if t.drift_deg_per_century <= max_drift_deg_per_century:
                chosen = t
                break
        if chosen is not None:
            trains.append(chosen)
    return trains


def table(trains: list[Train]) -> str:
    rows = [
        "| Planet | Target ratio | Stages | Driver teeth | Driven teeth | Gear ratio | Error (ppm) | Drift (deg/century) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for t in trains:
        rows.append(
            f"| {t.planet} | {t.target:.8f} | {t.stages} | "
            f"{'·'.join(map(str, t.drivers))} | {'·'.join(map(str, t.driven))} | "
            f"{t.ratio:.8f} | {t.rel_error_ppm:.1f} | {t.drift_deg_per_century:.3f} |"
        )
    return "\n".join(rows)


if __name__ == "__main__":
    print(table(design()))
