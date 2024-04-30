import uuid
from dataclasses import dataclass, field

@dataclass 
class Category:
    # construtor
    name: str
    description: str = ""
    is_active: bool = True
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    
    def __post_init__(self):
        self.validate_name()
    # def __init__(
    #     self,
    #     name,
    #     id = "",
    #     description= "",
    #     is_active= True,
    # ):
    #     self.id = id or uuid.uuid4()
    #     self.name = name
    #     self.description = description
    #     self.is_active = is_active
       
    #     self.validate_name()
        
    def validate_name(self):
        if len(self.name) > 255:
            raise ValueError("name must have less than 256 characters")
        if not self.name:
            raise ValueError("name cannot be empty")
            
    def __str__(self):
        return f"{self.name} - {self.description}- ({self.is_active})"
    
    def __repr__(self):
        return f"<Category {self.name} ({self.id})> "
    
    def __eq__(self, other):
        if not isinstance(other, Category):
            return False    
        return self.id == other.id
    
    def update_category(self, name, description): 
        self.name = name
        self.description = description
        
        self.validate_name()
        
    def activate(self): 
        self.is_active = True
        
        self.validate_name()
        
    def deactivate(self): 
        self.is_active = False
        
        self.validate_name()