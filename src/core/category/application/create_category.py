from uuid import UUID
from dataclasses import dataclass
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

@dataclass
class InvalidCategoryData(Exception):
    pass

@dataclass
class CreateCategoryRequest:
    name:str
    description:str=""
    is_active:bool= True


@dataclass
class CreateCategoryResponse:
    id: UUID


class CreateCategory:
    def __init__(self, repository: InMemoryCategoryRepository):
        self.repository = repository
        
    def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse:
        try:
            category = Category(
                name=request.name, 
                description=request.description, 
                is_active=request.is_active, 
            )
        
        except ValueError as e:
            raise InvalidCategoryData(e)
        
        self.repository.save(category)    
        return category.id