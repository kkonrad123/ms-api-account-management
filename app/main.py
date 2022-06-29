import asyncio
from typing import Dict, Optional, Union
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

class Account(BaseModel):
    name: str
    description: Optional[str] = None
    balance: float
    active: bool = True

accounts = dict()

accounts = {
    1: {"name": "joe", "balance": 500, "active": True, "description": None},
    2: {"name": "smith", "balance": 400, "active": True, "description": None},
    3: {"name": "example", "balance": 300, "active": True, "description": None}
}

###################
# Metadata and Docs
###################

description = """
Features:

* Check health status of the application 🚀
* Create account
* Delete account
* Read account

"""

tags_metadata = [
    {
        "name": "accounts",
        "description": "Operations with accounts. Basic error handling has been implemented."
    },
    {
        "name": "health",
        "description": "Health checks that can be used to verify application status."
    }
]

app = FastAPI(title="Account Management",
    description=description,
    version="1",
    terms_of_service="https://www.example.org",
    contact={
        "name": "<Contact Name>",
        "url": "https://www.example.org",
        "email": "<Contact Email>",
    },
    license_info={
        "name": "<License Link>",
        "url": "https://www.example.org",
    },
    openapi_tags=tags_metadata
)

###########
# Functions
###########

async def get_account(account_id: int) -> Optional[Account]:
    if account_id in accounts:
        return accounts[account_id]
    else:
        return None

async def add_account(account_id: int, account: Account) -> Optional[Account]:
    if account_id in accounts:
        return None
    else:
        accounts[account_id] = account.dict()
        return accounts[account_id]

async def delete_account(account_id: int) -> Optional[bool]:
    if account_id in accounts:
        del accounts[account_id]
        return True
    else:
        return None

@app.get("/health", status_code=200, tags=["health"])
async def get_health(request: Request) -> Union[Optional[Dict], HTTPException]:
    return {"status": True}

@app.get("/accounts/{account_id}", status_code=200, tags=["accounts"])
async def read_account(account_id: int):
    res = await get_account(account_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Account not found")
    else:
        return res

@app.post("/accounts/{account_id}", status_code=201, tags=["accounts"])
async def create_account(account_id: int, account: Account):
    res = await add_account(account_id, account)
    if res is None:
        raise HTTPException(status_code=409, detail="Account exists")
    else:
        return res

@app.delete("/accounts/{account_id}", status_code=200, tags=["accounts"])
async def remove_account(account_id: int):
    res = await delete_account(account_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Account not found")
    else:
        return res
