import pytest
from team_edit_api import set_species, set_nick, set_gender, set_item, set_tera_type, set_ability, set_nature, add_move, remove_move, set_stat_pts, add_species, remove_species, clear_team
from monster import Monster, StatPointsSpread, Move, Gender
from team import Team

@pytest.fixture
def team():
        m1 = Monster(
                species="Garchomp",
                nick="Chompy",
                gender=Gender.MALE,
                item="Choice Scarf",
                tera_type="Steel",
                ability="Rough Skin",
                nature="Jolly",
                moves=[Move(name="Earthquake"), Move(name="Scale Shot")],
                sps=StatPointsSpread(hp=4, spe=32)
        )
        m2 = Monster(
                species="Togekiss",
                nick="Mini",
                gender=Gender.MALE,
                item="Leftovers",
                tera_type="Steel",
                ability="Serene Grace",
                nature="Jolly",
                moves=[Move(name="Dazzling Gleam"), Move(name="Air Slash")],
                sps=StatPointsSpread(hp=4, spe=32)
        )
        return Team(
            slots=[m1, m2],
            format="VGC 2025 Reg H"
        )

@pytest.fixture
def empty_team():
    return Team(
        slots=[],
        format="VGC 2025 Reg H"
    )

def test_set_species(team: Team):
    new_team = set_species("Garchomp", "Dragonite", team)
    assert any(monster.species == "Dragonite" for monster in new_team.slots)
    assert not any(monster.species == "Garchomp" for monster in new_team.slots)

def test_add_species(team: Team):
    new_team = add_species("Pikachu", team)
    assert any(monster.species == "Pikachu" for monster in new_team.slots)

def test_remove_species(team: Team):
    new_team = remove_species("Garchomp", team)
    assert not any(monster.species == "Garchomp" for monster in new_team.slots)

def test_add_species_too_many(empty_team: Team):
    new_team = empty_team
    for i in range(6):
        new_team = add_species(f"Mon{i}", new_team)
    with pytest.raises(ValueError):
        add_species("Mon6", new_team)

def test_add_species_duplicate(team: Team):
    with pytest.raises(ValueError):
        add_species("Garchomp", team)
        
def test_remove_species_not_found(team: Team):
    with pytest.raises(ValueError):
        remove_species("NonExistentMon", team)

def test_remove_species_from_empty_team(empty_team: Team):
    with pytest.raises(ValueError):
         remove_species("AnyMon", empty_team)

def test_set_nick(team: Team):
    new_team = set_nick("Garchomp", "NewNick", team)
    assert any(monster.nick == "NewNick" for monster in new_team.slots if monster.species == "Garchomp")

def test_set_nick_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        set_nick("NonExistentMon", "NewNick", team)

def test_set_gender(team: Team):
    new_team = set_gender("Garchomp", Gender.FEMALE, team)
    assert any(monster.gender == Gender.FEMALE for monster in new_team.slots if monster.species == "Garchomp")

def test_set_gender_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        set_gender("NonExistentMon", Gender.FEMALE, team)

def test_set_item(team: Team):
    new_team = set_item("Garchomp", "Leftovers", team)
    assert any(monster.item == "Leftovers" for monster in new_team.slots if monster.species == "Garchomp")

def test_remove_item(team: Team):
    new_team = set_item("Garchomp", None, team)
    assert any(monster.item is None for monster in new_team.slots if monster.species == "Garchomp")

def test_set_item_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        set_item("NonExistentMon", "Leftovers", team)

def test_set_tera_type(team: Team):
    new_team = set_tera_type("Garchomp", "Fire", team)
    assert any(monster.tera_type == "Fire" for monster in new_team.slots if monster.species == "Garchomp")

def test_set_remove_tera_type(team: Team):
    new_team = set_tera_type("Garchomp", None, team)
    assert any(monster.tera_type is None for monster in new_team.slots if monster.species == "Garchomp")

def test_set_tera_type_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        set_tera_type("NonExistentMon", "Fire", team)

def test_set_ability(team: Team):
    new_team = set_ability("Garchomp", "Sand Veil", team)
    assert any(monster.ability == "Sand Veil" for monster in new_team.slots if monster.species == "Garchomp")

def test_set_remove_ability(team: Team):
    new_team = set_ability("Garchomp", None, team)
    assert any(monster.ability is None for monster in new_team.slots if monster.species == "Garchomp")

def test_set_ability_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        set_ability("NonExistentMon", "Sand Veil", team)

def test_set_nature(team: Team):
    new_team = set_nature("Garchomp", "Adamant", team)
    assert any(monster.nature == "Adamant" for monster in new_team.slots if monster.species == "Garchomp")

def test_set_remove_nature(team: Team):
    new_team = set_nature("Garchomp", None, team)
    assert any(monster.nature is None for monster in new_team.slots if monster.species == "Garchomp")

def test_set_nature_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        set_nature("NonExistentMon", "Adamant", team)

def test_add_move(team: Team):
    new_team = add_move("Garchomp", "Dragon Claw", team)
    moves = [monster.moves for monster in new_team.slots if monster.species == "Garchomp"]
    moves = moves[0]  # get the moves list from the monster
    assert any(move.name == "Dragon Claw" for move in moves)
    assert len(moves) == 3

def test_remove_move(team: Team):
    new_team = remove_move("Garchomp", "Earthquake", team)
    moves = [monster.moves for monster in new_team.slots if monster.species == "Garchomp"]
    moves = moves[0]  # get the moves list from the monster
    assert not any(move.name == "Earthquake" for move in moves)
    assert len(moves) == 1

def test_add_move_too_many(team: Team):
    new_team = add_move("Garchomp", "Dragon Claw", team)
    new_team = add_move("Garchomp", "Swords Dance", new_team)
    with pytest.raises(ValueError):
        add_move("Garchomp", "Stealth Rock", new_team)

def test_remove_move_not_found(team: Team):
    with pytest.raises(ValueError):
        remove_move("Garchomp", "NonExistentMove", team)

def test_remove_move_from_monster_with_no_moves(empty_team: Team):
    new_team = add_species("Garchomp", empty_team)
    with pytest.raises(ValueError):
        remove_move("Garchomp", "AnyMove", new_team)

def test_remove_move_from_nonexistent_mon(team: Team):
    with pytest.raises(ValueError):
        remove_move("NonExistentMon", "AnyMove", team)

def test_set_sps(team: Team):
    new_sps = StatPointsSpread(hp=32, atk=32, dfs=2)
    new_team = set_stat_pts("Garchomp", new_sps, team)
    assert any(monster.sps == new_sps for monster in new_team.slots if monster.species == "Garchomp")

def test_set_sps_nonexistent_mon(team: Team):
    new_sps = StatPointsSpread(hp=32, atk=32, dfs=2)
    with pytest.raises(ValueError):
        set_stat_pts("NonExistentMon", new_sps, team)

def test_clear_team(team: Team):
    cleared_team = clear_team(team)
    assert len(cleared_team.slots) == 0
