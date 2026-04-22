import pytest
from pydantic import ValidationError
from team import Team
from monster import Monster

def test_team_valid():
    team = Team(
        slots=[Monster(species="Garchomp")],
        format="VGC 2025 Reg H"
    )
    assert len(team.slots) == 1

def test_team_too_many_slots():
    with pytest.raises(ValidationError):
        Team(
            slots=[Monster(species=f"Mon{i}") for i in range(7)],
            format="VGC 2025 Reg H"
        )

def test_team_invalid_duplicate_species():
    with pytest.raises(ValidationError):
        Team(
            slots=[Monster(species="Garchomp"), Monster(species="Garchomp")],
            format="VGC 2025 Reg H"
        )

def test_team_invalid_duplicate_items():
    with pytest.raises(ValidationError):
        Team(
            slots=[Monster(species="Garchomp", item="Choice Scarf"), Monster(species="Togekiss", item="Choice Scarf")],
            format="VGC 2025 Reg H"
        )

def test_team_str_contains_format():
    team = Team(slots=[], format="VGC 2025 Reg H")
    assert "VGC 2025 Reg H" in str(team)

def test_empty_team_str():
    team = Team(slots=[], format="VGC 2025 Reg H")
    assert str(team) == "Format: VGC 2025 Reg H\n\n"
