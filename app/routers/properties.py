from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.property import Property, PropertyCreate, PropertyUpdate
from app.code.database import db

router = APIRouter(prefix="/properties", tags=["properties"])

@router.get("/", response_model=List[Property])
async def get_all_properties():
    """Get all properties"""
    return db.get_all_properties()

@router.get("/{property_id}", response_model=Property)
async def get_property_by_id(property_id: int):
    """Get property by ID"""
    property = db.get_property_by_id(property_id)
    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Property with ID {property_id} not found"
        )
    return property

@router.post("/", response_model=Property, status_code=status.HTTP_201_CREATED)
async def create_property(property_data: PropertyCreate):
    """Create a new property"""
    new_property = db.create_property(property_data)
    return new_property

@router.put("/{property_id}", response_model=Property)
async def update_property(property_id: int, property_data: PropertyUpdate):
    """Update an existing property"""
    updated_property = db.update_property(property_id, property_data)
    if not updated_property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Property with ID {property_id} not found"
        )
    return updated_property

@router.delete("/{property_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_property(property_id: int):
    """Delete a property"""
    success = db.delete_property(property_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Property with ID {property_id} not found"
        )
    return None 