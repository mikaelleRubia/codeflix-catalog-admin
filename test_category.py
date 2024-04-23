import pytest
import unittest
from category import Category
from uuid import UUID
import uuid

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
           Category()
           
    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            Category(name="a" * 256)
            
    def test_category_must_be_created_with_id_uuid(self):
        categoria = Category(name="livros")
        self.assertEquals(type(categoria.id), UUID)
        
    def test_created_category_must_be_created_with_default_(self):
        categoria = Category(name="livros")
        self.assertEquals(categoria.name, "livros")
        self.assertEquals(categoria.description,"")
        self.assertEquals(categoria.is_active, True)

    def test_created_category_must_be_created_with_provided_values(self):
        id_cat = uuid.uuid4()
        categoria = Category(id = id_cat, name="livros", description="descricao do livros", is_active=False)
        self.assertEquals(categoria.id, id_cat)
        self.assertEquals(categoria.name, "livros")
        self.assertEquals(categoria.description,"descricao do livros")
        self.assertEquals(categoria.is_active, False)

    def test_category_str_(self):
        categoria = Category( name="livros", description="descricao do livros", is_active=False)
          
        expected_str = "livros - descricao do livros- (False)"
        actual_str = str(categoria)
        self.assertEquals(actual_str, expected_str)
        
    def test_category_repr_(self):
        id_cat = uuid.uuid4()
        categoria = Category(id = id_cat, name="livros", description="descricao do livros", is_active=False)
          
        expected_repr = f"<Category livros ({categoria.id})> "
        actual_repr = repr(categoria)
        self.assertEquals(actual_repr, expected_repr)
                                        
if __name__ == "__main__":
    unittest.main()           