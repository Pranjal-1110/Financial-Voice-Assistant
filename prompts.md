# Documenting the Prompts
## Prompt ID: 001
#### Intent: 
Generate synthetic data about stocks under management of the manager
#### Model Used: 
Claude Sonnet 4
#### Prompt:
regions = {
    "Asia": 
    "Europe": 
    "America": 
    "Australia": 
    "Middle-East": 
}

Assume I have a portfolio of stocks from 25 different companies, the division of these stocks amongst the different regions is given above.

The sectors across which these stocks span is:
sectors = ["Tech", "Finance", "Healthcare", "Entertainment", "Oil & Gas"]

The division of stocks can be random amongst the regions and the sectors.

The schema in which these stocks are to be stored is:
{
    "company_name": "",
    "ticker_symbol": "",
    "current_price": ,
    "region": "",
    "sector": "",
    "aum_percentage": ,
    "market_cap": ,
    "volatility_index": ,
    "dividend_yield": ,
    "pe_ratio": 
}

Based on the above requirements, provide me a JSON database of real companies, with their actual:
- company_name
- ticker_symbol  
- current_price
- region
- sector
- market_cap

Calculate AUM% based on the data provided above, regarding the diversity of the portfolio.

You can either calculate/fetch the remaining fields, or generate them. But follow strict guidelines for the fields that have been explicitly mentioned.

REMEMBER TO CREATE A DATABASE OF REAL COMPANIES.

#### Output:
 Generated the synthetic database, regarding the portfolio.
