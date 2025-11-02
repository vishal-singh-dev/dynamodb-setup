from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
import os
load_dotenv()
from fastapi import FastAPI
aws_access_key_id =os.getenv("aws_access_key_id")
aws_secret_access_key =os.getenv("aws_secret_access_key")
region = os.getenv("region")
table_name = os.getenv("table_name")
__all__ = ["app","BaseModel","APIRouter","HTTPException","aws_access_key_id","aws_secret_access_key","region","table_name"]   