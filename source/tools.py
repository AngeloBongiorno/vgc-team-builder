from openai.types.chat import ChatCompletionToolParam
from team import Team
from monster import StatPointsSpread
from team_edit_api import set_species, add_species, remove_species, set_item, set_nick, set_gender, set_tera_type, set_ability, set_nature, add_move, remove_move, replace_move, set_stat_pts, clear_team
import json

tools_guidance_dict: dict[str, str] = {
        "set_species": "When the user wants to replace a PoKémon in their team.",
        "add_species": "When the user wants to add a new Pokémon to the team.",
        "remove_species": "When the user wants to remove a Pokémon from the team.",
        "set_nick": "When the user wants to set or remove a nickname for a Pokémon in the team.",
        "set_gender": "When the user wants to set the gender for a Pokémon in the team or set it to unspecified.",
        "set_item": "When the user wants to set or remove a held item for a Pokémon in the team.",
        "set_tera_type": "When the user wants to set or remove a tera type",
        "set_ability": "When the user wants to set or remove an ability for a Pokémon in the team.",
        "set_nature": "When the user wants to set or remove a nature for a Pokémon in the team.",
        "add_move": "When the user wants to add a move to a Pokémon in the team.",
        "remove_move": "When the user wants to remove a move from a Pokémon in the team.",
        "replace_move": "When the user wants to replace a move from a Pokémon in the team with another move.",
        "set_stat_pts": "When the user wants to set the stat points for a Pokémon in the team.",
        "clear_team": "When the user wants to start building a new team from scratch, deleting the current team. Ask confirmation before performing this action."
}

tools: list[ChatCompletionToolParam] = [
    {
        "type": "function",
        "function": {
            "name": "set_species",
            "description": "Replaces the species of a Pokémon in the team with another one, all the attributes are set to default (empty).",
            "parameters": {
                "type": "object",
                "properties": {
                    "old_species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species to be replaced in the team."
                    },
                    "new_species_name": {
                        "type": "string",
                        "description": "The name of the new Pokémon species that will replace the old one in the team."
                    }
                },
                "required": ["old_species_name", "new_species_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_species",
            "description": "Adds a new Pokémon of the specified species to the team with default values, only usable when there's space available on the team.",
            "parameters": {
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species to add to the team."
                    }
                },
                "required": ["species_name"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remove_species",
            "description": "Removes a Pokémon from the team, identified by its species.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species to remove from the team."
                    }
                },
                "required": ["species_name"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_nick",
            "description": "Sets or removes the nickname of a Pokémon in the team, identified by its species.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose nickname is to be set or removed."
                    },
                    "nick": {
                        "type": ["string", "null"],
                        "description": "The nickname to set for the Pokémon. If None, the existing nickname will be removed."
                    }
                },
                "required": ["species_name", "nick"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_gender",
            "description": "Sets or removes the gender of a Pokémon in the team, identified by its species.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose gender is to be set or removed."
                    },
                    "gender": {
                        "type": ["string", "null"],
                        "enum": ["M", "F", "U", None],
                        "description": "The Pokémon's gender. M for male, F for female, U for unknown."
                    }
                },
                "required": ["species_name", "gender"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_item",
            "description": "Sets or removes the held item of a Pokémon in the team, identified by its species.",
            "parameters": {
                "type": "object",
                "properties": {
                   "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose held item is to be set or removed."
                   },
                   "item_name": {
                        "type": ["string", "null"],
                        "description": "The name of the item to be held by the Pokémon. If None, the existing held item will be removed."

                   }
                },
                "required": ["species_name", "item_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_tera_type",
            "description": "Sets or removes the tera type of a Pokémon in the team, identified by its species.",
            "parameters":{
                "type": "object",
                "properties": {
                   "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose tera type is to be set or removed."
                   },
                   "tera_type": {
                        "type": ["string", "null"],
                        "description": "The name of the tera type to be set for the Pokémon. If None, the existing tera type will be removed."
                   },
                },
                "required": ["species_name", "tera_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_ability",
            "description": "Sets or removes the ability of a Pokémon in the team, identified by its species.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose ability is to be set or removed."
                    },
                    "ability": {
                        "type": ["string", "null"],
                        "description": "The name of the ability to be set for the Pokémon. If None, the existing ability will be removed."
                    },
                },
                "required": ["species_name", "ability"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_nature",
            "description": "Sets or removes the nature of a Pokémon in the team, identified by its species.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose nature is to be set or removed."
                    },
                    "nature": {
                        "type": ["string", "null"],
                        "description": "The name of the nature to be set for the Pokémon. If None, the existing nature will be removed."
                    }
                },
                "required": ["species_name", "nature"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_move",
            "description": "Adds a move to a Pokémon in the team, identified by its species. Fails if the Pokémon already has 4 moves.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species to which the move will be added."
                    },
                    "move_name": {
                        "type": "string",
                        "description": "The name of the move to be added to the Pokémon."
                    }
                },
                "required": ["species_name", "move_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remove_move",
            "description": "Removes a move from a Pokémon in the team, identified by its species. Errors if the Pokémon does not have the move or has no moves.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species from which the move will be removed."
                    },
                    "move_name": {
                        "type": "string",
                        "description": "The name of the move to be removed from the Pokémon."
                    }
                },
                "required": ["species_name", "move_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "replace_move",
            "description": "Replaces a move from a Pokémon in the team, identified by its species, with a new move. Errors if the Pokémon does not have the old move or has no moves.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species for which the move will be replaced."
                    },
                    "old_move_name": {
                        "type": "string",
                        "description": "The name of the move to be replaced on the Pokémon."
                    },
                    "new_move_name": {
                        "type": "string",
                        "description": "The name of the new move to be added to the Pokémon in place of the old move."
                    }
                },
                "required": ["species_name", "old_move_name", "new_move_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_stat_pts",
            "description": "Sets the Stat Points (aka EVs) of a Pokémon in the team, identified by its species. Errors if the Pokémon is not found in the team. Their sum cannot exceed 66, each stat point can range from 0 to 32.",
            "parameters":{
                "type": "object",
                "properties": {
                    "species_name": {
                        "type": "string",
                        "description": "The name of the Pokémon species whose stat points are to be set."
                    },
                    "hp":  {"type": "integer", "description": "HP stat points (0-32)"},
                    "atk": {"type": "integer", "description": "Attack stat points (0-32)"},
                    "dfs": {"type": "integer", "description": "Defense stat points (0-32)"},
                    "spa": {"type": "integer", "description": "Special Attack stat points (0-32)"},
                    "spd": {"type": "integer", "description": "Special Defense stat points (0-32)"},
                    "spe": {"type": "integer", "description": "Speed stat points (0-32)"}
                },
                "required": ["species_name", "hp", "atk", "dfs", "spa", "spd", "spe"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "clear_team",
            "description": "Removes all Pokémon from the team, resulting in an empty team.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

def build_tool_guidance(guidance: dict[str, str]) -> str:
    lines = ["*Tool usage guidance:*"]
    for name, when in guidance.items():
        lines.append(f"- `{name}`: {when}")
    return "\n".join(lines)

available_tools_guidance = build_tool_guidance(tools_guidance_dict)

def dispatch_tool_call(tool_name: str, arguments: str, team: Team) -> tuple[Team, str]:
    args = json.loads(arguments)
    match tool_name:
        case "set_species":
            new_team = set_species(args["old_species_name"], args["new_species_name"], team)
            return new_team, str(new_team)
        case "add_species":
            new_team = add_species(args["species_name"], team)
            return new_team, str(new_team)
        case "remove_species":
            new_team = remove_species(args["species_name"], team)
            return new_team, str(new_team)
        case "set_nick":
            new_team = set_nick(args["species_name"], args["nick"], team)
            return new_team, str(new_team)
        case "set_gender":
            new_team = set_gender(args["species_name"], args["gender"], team)
            return new_team, str(new_team)
        case "set_item":
            new_team = set_item(args["species_name"], args["item_name"], team)
            return new_team, str(new_team)
        case "set_tera_type":
            new_team = set_tera_type(args["species_name"], args["tera_type"], team)
            return new_team, str(new_team)
        case "set_ability":
            new_team = set_ability(args["species_name"], args["ability"], team)
            return new_team, str(new_team)
        case "set_nature":
            new_team = set_nature(args["species_name"], args["nature"], team)
            return new_team, str(new_team)
        case "add_move":
            new_team = add_move(args["species_name"], args["move_name"], team)
            return new_team, str(new_team)
        case "remove_move":
            new_team = remove_move(args["species_name"], args["move_name"], team)
            return new_team, str(new_team)
        case "replace_move":
            new_team = replace_move(args["species_name"], args["old_move_name"], args["new_move_name"], team)
            return new_team, str(new_team)
        case "set_stat_pts":
            sps = StatPointsSpread(
                hp=args["hp"],
                atk=args["atk"],
                dfs=args["dfs"],
                spa=args["spa"],
                spd=args["spd"],
                spe=args["spe"]
            )
            new_team = set_stat_pts(args["species_name"], sps, team)
            return new_team, str(new_team)
        case "clear_team":
            new_team = clear_team(team)
            return new_team, str(new_team)
        case "damage_calc":
            return team, "damage calculation tool is yet to be implemented"
        case "type_effectiveness":
            return team, "type effectiveness tool is yet to be implemented"
        case _:
            return team, f"Unknown tool: {tool_name}"
