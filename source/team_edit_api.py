from monster import Monster, StatPointsSpread, Gender, Move
from team import Team

def set_species(old_species_name: str, new_species_name: str, team: Team) -> Team:
    "Replaces the species of a monster in the team with a new one. The new monster will have default values for all other attributes."

    team = team.model_copy(deep=True)
    species_list = [slot.species for slot in team.slots]
    if old_species_name not in species_list:
        raise ValueError(f"Species '{old_species_name}' not found in team")
    
    new_monster = Monster(species=new_species_name)
    team.slots = [new_monster if slot.species == old_species_name else slot for slot in team.slots]
    return team

def add_species(species_name: str, team: Team) -> Team:
    "Adds a new default monster with the specified species to the team."

    team = team.model_copy(deep=True)
    if len(team.slots) >= 6:
        raise ValueError("Team is already at maximum capacity")
    if any(slot.species == species_name for slot in team.slots):
        raise ValueError(f"{species_name} is already in the team.")
    team.slots.append(Monster(species=species_name))
    return team

def remove_species(species_name: str, team: Team) -> Team:
    "Removes a monster with the specified species from the team. If the species is not found, raises an error."

    team = team.model_copy(deep=True)
    if len(team.slots) <= 0:
        raise ValueError("Attempting to remove species from an empty team")
    if not any(slot.species == species_name for slot in team.slots):
        raise ValueError(f"Species '{species_name}' not found in team")
    team.slots = [slot for slot in team.slots if slot.species != species_name]
    return team

def set_nick(species_name: str, nick: str | None, team: Team) -> Team:
    "Sets the nickname of a monster in the team. If nick is None, removes the nickname."

    team = team.model_copy(deep=True) 
    for slot in team.slots:
        if slot.species == species_name:
            slot.nick = nick
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team


def set_gender(species_name: str, gender: Gender | None, team: Team) -> Team:
    "Sets the gender of a monster in the team. If gender is None, removes the gender."

    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            slot.gender = gender
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def set_item(species_name: str, item_name: str | None, team: Team) -> Team:
    "Sets the item of a monster in the team. If item_name is None, removes the item."

    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            slot.item = item_name
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def set_tera_type(species_name: str, tera_type: str | None, team: Team) -> Team:
    "Sets the tera type of a monster in the team. If tera_type is None, removes the tera type."

    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            slot.tera_type = tera_type
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def set_ability(species_name: str, ability: str | None, team: Team) -> Team:
    "Sets the ability of a monster in the team. If ability is None, removes the ability."

    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            slot.ability = ability
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def set_nature(species_name: str, nature: str | None, team: Team) -> Team:
    "Sets the nature of a monster in the team. If nature is None, removes the nature."
    for slot in team.slots:
        if slot.species == species_name:
            slot.nature = nature
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    team = team.model_copy(deep=True)
    return team

def add_move(species_name: str, move_name: str, team: Team) -> Team:
    "Adds a move to a monster in the team. If the monster already has 4 moves, raises an error."
    for slot in team.slots:
        if slot.species == species_name:
            if len(slot.moves) >= 4:
                raise ValueError(f"Monster '{species_name}' already has 4 moves")
            slot.moves.append(Move(name=move_name))
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    team = team.model_copy(deep=True)
    return team

def remove_move(species_name: str, move_name: str, team: Team) -> Team:
    "Removes a move from a monster in the team. If the monster does not have the move, or has no moves, raises an error."

    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            if all(move.name != move_name for move in slot.moves):
                raise ValueError(f"Move '{move_name}' not found for monster '{species_name}'")
            slot.moves = [move for move in slot.moves if move.name != move_name]
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def replace_move(species_name: str, old_move_name: str, new_move_name: str, team: Team) -> Team:
    "Replaces a move of a monster in the team with a new move. If the monster does not have the old move, raises an error."

    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            for i, move in enumerate(slot.moves):
                if move.name == old_move_name:
                    slot.moves[i] = Move(name=new_move_name)
                    break
            else:
                raise ValueError(f"Move '{old_move_name}' not found for monster '{species_name}'")
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def set_stat_pts(species_name: str, sps: StatPointsSpread, team: Team) -> Team:
    "Sets the stat points spread of a monster in the team. If the monster is not found, raises an error."
    
    team = team.model_copy(deep=True)
    for slot in team.slots:
        if slot.species == species_name:
            slot.sps = sps
            break
    else:
        raise ValueError(f"Species '{species_name}' not found in team")
    return team

def clear_team(team: Team) -> Team:
    "Removes all monsters from the team, resulting in an empty team."

    team = team.model_copy(deep=True)
    team.slots = []
    return team
