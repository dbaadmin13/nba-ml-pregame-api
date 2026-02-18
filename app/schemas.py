from pydantic import BaseModel

class GameFeatures(BaseModel):
    elo_diff: float
    netrtg_diff: float
    matchup_home: float
    matchup_away: float
    pace_projection: float
    rolling_3_diff: float
    rest_diff: float
    home_b2b: int
    away_b2b: int
