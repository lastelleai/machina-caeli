from datetime import datetime, timezone

from machina_caeli.ephemeris import (
    EARTH,
    PLANETS,
    julian_date,
    mean_longitude,
    period_years,
)
from machina_caeli.gears import design


def test_j2000_epoch():
    assert julian_date(datetime(2000, 1, 1, 12, tzinfo=timezone.utc)) == 2451545.0


def test_epoch_longitudes_match_jpl_table():
    t = datetime(2000, 1, 1, 12, tzinfo=timezone.utc)
    assert abs(mean_longitude(EARTH, t) - 100.46457166) < 1e-9


def test_periods_match_known_values():
    # NASA planetary fact sheet sidereal periods, in Earth days -> years
    expected = {"Mercury": 0.2408, "Venus": 0.6152, "Mars": 1.8808,
                "Jupiter": 11.862, "Saturn": 29.457, "Uranus": 84.01,
                "Neptune": 164.8}
    for p in PLANETS:
        if p.name in expected:
            assert abs(period_years(p) / expected[p.name] - 1) < 0.005, p.name


def test_every_planet_gets_a_train():
    trains = design()
    assert {t.planet for t in trains} == {p.name for p in PLANETS} - {"Earth"}
    for t in trains:
        assert all(12 <= x <= 100 for x in t.drivers + t.driven)
