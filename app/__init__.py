from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import os
load_dotenv()

table_name = os.getenv("table_name")
__all__ = ["app","BaseModel","APIRouter","HTTPException","table_name"]   