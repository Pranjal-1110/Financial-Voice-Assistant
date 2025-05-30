
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from datetime import datetime


#Define the output structure for the parsed user query
class parsed_output(BaseModel):
    intent: Literal[
        "market_risk_summary", 
        "earnings_highlight", 
        "macro_update", 
        "news_lookup"
    ] = Field(..., description="The type of user query")
    region: Optional[str] = Field(None, description="Geographical focus of the query (e.g., 'Asia')")
    sector: Optional[str] = Field(None, description="Sector focus like 'Technology', 'Finance', etc.")
    tickers: List[str] = Field(default_factory=list, description="List of relevant stock tickers")
    entities: dict = Field(default_factory=dict, description="Extracted named entities like company names or keywords")
    questions: List[str] = Field(default_factory=list, description="Sub-questions or clauses from the user's prompt")
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Time of the request")
    urgency: Literal["daily_brief", "real_time_alert", "deep_dive",
                     "casual"] = Field("daily_brief", description="Urgency level")
    confidence: Optional[float] = Field(None, description="LLM’s confidence in parsing the query")
    
    
