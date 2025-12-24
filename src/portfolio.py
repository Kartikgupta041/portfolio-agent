import json
from typing import List, Literal, Dict, Any
from pydantic import BaseModel


class Position(BaseModel):
    ticker: str
    weight: float


class Constraints(BaseModel):
    max_position_weight: float = 0.35
    risk_tolerance: Literal["conservative", "moderate", "aggressive"] = "moderate"


class Portfolio(BaseModel):
    as_of: str
    positions: List[Position]
    constraints: Constraints


def load_portfolio(path: str) -> Portfolio:
    with open(path, "r") as f:
        data: Dict[str, Any] = json.load(f)
    return Portfolio(**data)
