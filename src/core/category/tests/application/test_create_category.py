
import unittest
import pytest
import unittest
from unittest.mock import MagicMock
from src.core.category.domain.category import Category
from src.core.category.application.create_category import CreateCategory,InvalidCategoryData,  CreateCategoryRequest, CreateCategoryResponse
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

from uuid import UUID
import uuid

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mockRepository = MagicMock(InMemoryCategoryRepository)
        use_case = CreateCategory(repository= mockRepository)
        request = CreateCategoryRequest(
            name="livros", 
            description="descrição dos livros",
            is_active=True
        )
        category_id = use_case.execute(request)
        
        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mockRepository.save.called is True

    def test_create_category_with_invalid_data(self):
        use_case = CreateCategory(repository=MagicMock(InMemoryCategoryRepository))
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            request = CreateCategoryRequest(name="")
            category_id = use_case.execute(request)
        
        # Você também pode usar exc_info para verificar algo mais específico
        assert exc_info.type is InvalidCategoryData  
        assert str(exc_info.value) == "name cannot be empty"

if __name__ == "__main__":
    unittest.main()
