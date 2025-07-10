from typing import List, Optional
from datetime import datetime
from app.models.property import Property, PropertyCreate, PropertyUpdate

class InMemoryDatabase:
    def __init__(self):
         # This list simulates the database table for properties
        self.properties: List[Property] = []
        # Counter to generate unique IDs for each property
        self._counter = 1
    
    def get_all_properties(self) -> List[Property]:
        """Get all properties"""
        return self.properties
    
    def get_property_by_id(self, property_id: int) -> Optional[Property]:
        """Get property by ID"""
        for property in self.properties:
            if property.id == property_id:
                return property
        return None # Return None if not found
    
    def create_property(self, property_data: PropertyCreate) -> Property:
        """Create a new property"""
        # Use the counter to assign a unique ID
        new_property = Property(
            id=self._counter,
            **property_data.dict(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        # Add the property to the list (simulate insert)
        self.properties.append(new_property)
        # Increment ID counter
        self._counter += 1
        return new_property
    
    def update_property(self, property_id: int, property_data: PropertyUpdate) -> Optional[Property]:
        """Update an existing property"""
        for i, property in enumerate(self.properties):
            # Iterate with both index and item
            if property.id == property_id:
                 # Only include fields that were actually sent (skip None)
                update_data = property_data.dict(exclude_unset=True)
                update_data['updated_at'] = datetime.now()
                
                # Update the corresponding attributes on the object
                for key, value in update_data.items():
                    # Set each updated field dynamically
                    setattr(self.properties[i], key, value)
                
                return self.properties[i]
        return None # If no property was found
    
    def delete_property(self, property_id: int) -> bool:
        """Delete a property"""
        for i, property in enumerate(self.properties):
             # Loop over each property and get both the index (i) and the object (property)
            if property.id == property_id:
                # Remove the item from the list by index
                del self.properties[i]
                return True # Successfully deleted
        return False  # Not found

# Global instance to be used in routes or services
db = InMemoryDatabase() 