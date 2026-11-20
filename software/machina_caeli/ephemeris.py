"""Heliocentric mean longitudes for the eight planets.

Source: JPL Solar System Dynamics, "Approximate Positions of the Planets",
Table 1 (fit valid 1800 AD to 2050 AD), mean ecliptic and equinox of J2000.
https://ssd.jpl.nasa.gov/planets/approx_pos.html

Machina Caeli moves every planet at a uniform pace, so the mean longitude
L(T) = L0 + L_dot * T is exactly what the face shows. T is Julian centuries
since J2000.0 (JD 2451545.0).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

J2000_JD = 2451545.0
DAYS_PER_CENTURY = 36525.0
VALID_FROM_YEAR = 1800
VALID_TO_YEAR = 2050


@dataclass(frozen=True)
class Planet:
    name: str
    L0_deg: float        # mean longitude at J2000.0
    L_dot_deg_cy: float  # degrees per Julian century


# "EM Bary" (Earth-Moon barycentre) stands in for Earth, as in the JPL table.
PLANETS: tuple[Planet, ...] = (
    Planet("Mercury", 252.25032350, 149472.67411175),
    Planet("Venus", 181.97909950, 58517.81538729),
    Planet("Earth", 100.46457166, 35999.37244981),
    Planet("Mars", -4.55343205, 19140.30268499),
    Planet("Jupiter", 34.39644051, 3034.74612775),
    Planet("Saturn", 49.95424423, 1222.49362201),
    Planet("Uranus", 313.23810451, 428.48202785),
    Planet("Neptune", -55.12002969, 218.45945325),
)

EARTH = next(p for p in PLANETS if p.name == "Earth")


def julian_date(dt: datetime) -> float:
    """Julian Date of a datetime (naive values are treated as UTC)."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    unix = dt.timestamp()
    return unix / 86400.0 + 2440587.5


def centuries_since_j2000(dt: datetime) -> float:
    return (julian_date(dt) - J2000_JD) / DAYS_PER_CENTURY


def in_valid_range(dt: datetime) -> bool:
    return VALID_FROM_YEAR <= dt.year <= VALID_TO_YEAR


def mean_longitude(planet: Planet, dt: datetime) -> float:
    """Heliocentric mean longitude in degrees, wrapped to [0, 360)."""
    T = centuries_since_j2000(dt)
    return (planet.L0_deg + planet.L_dot_deg_cy * T) % 360.0


def sky(dt: datetime) -> dict[str, float]:
    """Angle of every planet on the face for a given date."""
    return {p.name: mean_longitude(p, dt) for p in PLANETS}


def ratio_to_earth(planet: Planet) -> float:
    """Planet revolutions per one Earth revolution (the gear ratio target)."""
    return planet.L_dot_deg_cy / EARTH.L_dot_deg_cy


def period_years(planet: Planet) -> float:
    """Sidereal period in Julian years implied by the JPL rate."""
    return 36000.0 / planet.L_dot_deg_cy
