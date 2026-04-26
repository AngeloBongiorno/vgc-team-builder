from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing import Annotated

class Move(BaseModel):
    name: str

class Gender(str, Enum):
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

BPValue = Annotated[int, Field(ge=0, le=32)]

class StatPointsSpread(BaseModel):
    hp: BPValue = 0
    atk: BPValue = 0
    dfs: BPValue = 0
    spa: BPValue = 0
    spd: BPValue = 0
    spe: BPValue = 0

    @model_validator(mode="after")
    def check_total(self) -> "StatPointsSpread":
        total = self.hp + self.atk + self.dfs + self.spa + self.spd + self.spe
        if total > 66:
            raise ValueError(f"Total stat points cannot exceed 66, got {total}")
        return self
    
    def __str__(self):
        return f"EVs: {self.hp} HP / {self.atk} Atk / {self.dfs} Def / {self.spa} SpA / {self.spd} SpD / {self.spe} Spe"

class Monster(BaseModel):
    species: str
    nick: str | None = None
    gender: Gender | None = None
    item: str | None = None
    tera_type: str | None = None
    ability: str | None = None
    nature: str | None = None
    moves: Annotated[list[Move], Field(min_length=0, max_length=4)] = []
    sps: StatPointsSpread = Field(default_factory=StatPointsSpread)

    def __str__(self):
        """
        Returns the moster in a pasteable format.
        """
        output = ''
        if self.nick:
            output += f"{self.nick} ({self.species})"
        else:
            output += self.species
        if self.gender:
            output += f" ({self.gender.value})"
        if self.item:
            output += f" @ {self.item}"
        output += '\n'
        if self.ability:
            output += f"Ability: {self.ability}\n"
        output += f"{self.sps}\n"
        if self.tera_type:
            output += f"Tera Type: {self.tera_type}\n"
        if self.nature:
            output += f"{self.nature} Nature\n"
        for move in self.moves:
            output += f"- {move.name}\n"
        return output



if __name__ == "__main__":

    m = Monster(
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
    print(m)
