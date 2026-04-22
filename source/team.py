from pydantic import BaseModel, Field, model_validator
from typing import Annotated
from monster import Monster

class Team(BaseModel):
    slots: Annotated[list[Monster], Field(min_length=0, max_length=6)] = []
    format: str

    def __str__(self):
        output = f"Format: {self.format}\n\n"
        for monster in self.slots:
            output += str(monster) + '\n'
        return output

    @model_validator(mode="after")
    def check_duplicate_species(self) -> "Team":
        species = [monster.species for monster in self.slots]
        if len(species) != len(set(species)):
            raise ValueError("Duplicate species found in team")
        return self
    
    @model_validator(mode="after")
    def check_duplicate_items(self) -> "Team":
        items = [monster.item for monster in self.slots if monster.item is not None]
        if len(items) != len(set(items)):
            raise ValueError("Duplicate items found in team")
        return self

    """
    def is_team_valid(self) -> bool:
        if len(self.slots) != 6:
            return False
        for monster in self.slots:
            if monster.ability is None or monster.nature is None or len(monster.moves) == 0:
                return False
        return True
    """
