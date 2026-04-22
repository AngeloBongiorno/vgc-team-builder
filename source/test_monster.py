import pytest
from pydantic import ValidationError
from monster import Move, Gender, BasePointsSpread, Monster


# --- BasePointsSpread ---

def test_bps_valid():
    bps = BasePointsSpread(hp=32, atk=32, spe=2)
    assert bps.hp == 32

def test_bps_stat_exceeds_max():
    with pytest.raises(ValidationError):
        BasePointsSpread(hp=33)

def test_bps_stat_negative():
    with pytest.raises(ValidationError):
        BasePointsSpread(atk=-1)

def test_bps_total_exceeds_cap():
    with pytest.raises(ValidationError):
        BasePointsSpread(hp=32, atk=32, spe=3)  # total = 67

def test_bps_defaults_to_zero():
    bps = BasePointsSpread()
    assert sum([bps.hp, bps.atk, bps.dfs, bps.spa, bps.spd, bps.spe]) == 0


# --- Monster ---

def test_monster_minimal():
    m = Monster(species="Garchomp")
    assert m.species == "Garchomp"
    assert m.nature is None
    assert m.moves == []

def test_monster_str_minimal():
    m = Monster(species="Garchomp")
    output = str(m)
    assert "Garchomp" in output
    assert "None" not in output  # no field should print as None

def test_monster_str_full():
    m = Monster(
        species="Garchomp",
        nick="Chompy",
        gender=Gender.MALE,
        item="Choice Scarf",
        tera_type="Steel",
        ability="Rough Skin",
        nature="Jolly",
        moves=[Move(name="Earthquake"), Move(name="Scale Shot")],
        bps=BasePointsSpread(hp=4, spe=32)
    )
    output = str(m)
    assert "Chompy (Garchomp)" in output
    assert "(M)" in output
    assert "@ Choice Scarf" in output
    assert "Tera Type: Steel" in output
    assert "Jolly Nature" in output
    assert "- Earthquake" in output

def test_monster_too_many_moves():
    with pytest.raises(ValidationError):
        Monster(species="Garchomp", moves=[
            Move(name="Earthquake"),
            Move(name="Scale Shot"),
            Move(name="Stealth Rock"),
            Move(name="Swords Dance"),
            Move(name="Dragon Claw"),  # 5th move
        ])
