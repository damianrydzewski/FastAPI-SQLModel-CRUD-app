from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

#=========================================================#
### Hero MODEL ###
#=========================================================#

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    team: Optional["Team"] = Relationship(back_populates="heroes")


class HeroRequest(HeroBase):
    pass


class HeroResponse(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None




#=========================================================#
### Team MODEL ###
#=========================================================#

class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    heroes: List["Hero"] = Relationship(back_populates="team")

class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None

#=========================================================#

class HeroReadWithTeam(HeroResponse):
    team: Optional[TeamRead] = None


class TeamReadWithHeroes(TeamRead):
    heroes: List[HeroResponse] = []