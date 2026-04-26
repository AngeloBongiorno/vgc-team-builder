from typing import TypedDict, TypeAlias, NotRequired

class ToolParameter(TypedDict):
    name: str
    type: str
    enum: NotRequired[list[str]]
    description: str

#class ToolParameters(TypedDict):
#    type: str
#    properties: dict[str, ToolParameter]
#    required: list[str]

class ToolFunction(TypedDict):
    name: str
    description: str
    parameters: list[ToolParameter]

class ToolDefinition(TypedDict):
    type: str
    function: ToolFunction
    when_to_use: str

ToolList: TypeAlias = list[ToolDefinition]




tools: ToolList = [
    {
        "type": "function",
        "function": {
            "name": "set_species",
            "description": "Replaces the species of a Pokémon in the team with another one, all the attributes are set to default (empty).",
            "parameters": [
                {
                    "name": "old_species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species to be replaced in the team."
                },
                {
                    "name": "new_species_name",
                    "type": "string",
                    "description": "The name of the new Pokémon species that will replace the old one in the team."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the species replacement will occur."
                }
            ]
        },
        "when_to_use": "When the user wants to replace a PoKémon in their team."
    },
    {
        "type": "function",
        "function": {
            "name": "add_species",
            "description": "Adds a new Pokémon of the specified species to the team with default values, only usable when there's space available on the team.",
            "parameters": [
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species to add to the team."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team to which the new Pokémon will be added."
                }
            ],
        },
        "when_to_use": "When the user wants to add a new Pokémon to the team."
    },
    {
        "type": "function",
        "function": {
            "name": "remove_species",
            "description": "Removes a Pokémon from the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species to remove from the team."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team from which the Pokémon will be removed."
                }
            ],
        },
        "when_to_use": "When the user wants to remove a Pokémon from the team."
    },
    {
        "type": "function",
        "function": {
            "name": "set_nick",
            "description": "Sets or removes the nickname of a Pokémon in the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose nickname is to be set or removed."
                },
                {
                    "name": "nick",
                    "type": "string | None",
                    "description": "The nickname to set for the Pokémon. If None, the existing nickname will be removed."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's nickname will be set or removed."
                }
            ],
        },
        "when_to_use": "When the user wants to set or remove a nickname for a Pokémon in the team."
    },
    {
        "type": "function",
        "function": {
            "name": "set_gender",
            "description": "Sets or removes the gender of a Pokémon in the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose gender is to be set or removed."
                },
                {
                    "name": "gender",
                    "type": "string",
                    "enum": ["M", "F", "U"],
                    "description": "The Pokémon's gender. M for male, F for female, U for unknown."
                }
            ]
        },
        "when_to_use": "When the user wants to set the gender for a Pokémon in the team or set it to unspecified."
    },
    {
        "type": "function",
        "function": {
            "name": "set_item",
            "description": "Sets or removes the held item of a Pokémon in the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose held item is to be set or removed."
                },
                {
                    "name": "item_name",
                    "type": "string | None",
                    "description": "The name of the item to be held by the Pokémon. If None, the existing held item will be removed."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's held item will be set or removed."
                }
            ]
        },
        "when_to_use": "When the user wants to edit an held item."
    },
    {
        "type": "function",
        "function": {
            "name": "set_tera_type",
            "description": "Sets or removes the tera type of a Pokémon in the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose tera type is to be set or removed."
                },
                {
                    "name": "tera_type",
                    "type": "string | None",
                    "description": "The name of the tera type to be set for the Pokémon. If None, the existing tera type will be removed."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's tera type will be set or removed."
                }
            ]
        },
        "when_to_use": "When the user wants to edit a tera type, should be set only if the active regulation allows terastalization."
    },
    {
        "type": "function",
        "function": {
            "name": "set_ability",
            "description": "Sets or removes the ability of a Pokémon in the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose ability is to be set or removed."
                },
                {
                    "name": "ability",
                    "type": "string | None",
                    "description": "The name of the ability to be set for the Pokémon. If None, the existing ability will be removed."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's ability will be set or removed."
                }
            ]
        },
        "when_to_use": "When the user wants to edit an ability."
    },
    {
        "type": "function",
        "function": {
            "name": "set_nature",
            "description": "Sets or removes the nature of a Pokémon in the team, identified by its species.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose nature is to be set or removed."
                },
                {
                    "name": "nature",
                    "type": "string | None",
                    "description": "The name of the nature to be set for the Pokémon. If None, the existing nature will be removed."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's nature will be set or removed."
                }
            ]
        },
        "when_to_use": "When the user wants to edit a nature."
    },
    {
        "type": "function",
        "function": {
            "name": "add_move",
            "description": "Adds a move to a Pokémon in the team, identified by its species. Fails if the Pokémon already has 4 moves.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species to which the move will be added."
                },
                {
                    "name": "move_name",
                    "type": "string",
                    "description": "The name of the move to be added to the Pokémon."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's move will be added."
                }
            ]
        },
        "when_to_use": "When the user wants to add a move to a Pokémon in the team and that Pokémon has less than 4 moves."
    },
    {
        "type": "function",
        "function": {
            "name": "remove_move",
            "description": "Removes a move from a Pokémon in the team, identified by its species. Errors if the Pokémon does not have the move or has no moves.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species from which the move will be removed."
                },
                {
                    "name": "move_name",
                    "type": "string",
                    "description": "The name of the move to be removed from the Pokémon."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's move will be removed."
                }
            ]
        },
        "when_to_use": "When the user wants to remove a move from a Pokémon in the team."
    },
    {
        "type": "function",
        "function": {
            "name": "replace_move",
            "description": "Replaces a move from a Pokémon in the team, identified by its species, with a new move. Errors if the Pokémon does not have the old move or has no moves.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species for which the move will be replaced."
                },
                {
                    "name": "old_move_name",
                    "type": "string",
                    "description": "The name of the move to be replaced on the Pokémon."
                },
                {
                    "name": "new_move_name",
                    "type": "string",
                    "description": "The name of the new move to be added to the Pokémon in place of the old move."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's move will be replaced."
                }
            ]
        },
        "when_to_use": "When the user wants to replace a move from a Pokémon in the team with another move."
    },
    {
        "type": "function",
        "function": {
            "name": "set_stat_pts",
            "description": "Sets the Stat Points (aka EVs) of a Pokémon in the team, identified by its species. Errors if the Pokémon is not found in the team. Their sum cannot exceed 66, each stat point can range from 0 to 32.",
            "parameters":[
                {
                    "name": "species_name",
                    "type": "string",
                    "description": "The name of the Pokémon species whose stat points are to be set."
                },
                {
                    "name": "sps",
                    "type": "StatPointsSpread",
                    "description": "The stat points spread to be set for the Pokémon."
                },
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team in which the Pokémon's stat points will be set."
                }
            ]
        },
        "when_to_use": "When the user wants to set the stat points for a Pokémon in the team."
    },
    {
        "type": "function",
        "function": {
            "name": "clear_team",
            "description": "Removes all Pokémon from the team, resulting in an empty team.",
            "parameters":[
                {
                    "name": "team",
                    "type": "Team",
                    "description": "The current team to be cleared."
                }
            ]
        },
        "when_to_use": "When the user wants to start building a new team from scratch, deleting the current team. Ask confirmation before performing this action!"
    }
]

def build_tool_guidance(tools: ToolList) -> str:
    lines = ["*Tool usage guidance:*"]
    for tool in tools:
        name = tool["function"]["name"]
        when = tool.get("when_to_use", "")
        if when:
            lines.append(f"- `{name}`: {when}")
    return "\n".join(lines)

available_tools_guidance = build_tool_guidance(tools)
