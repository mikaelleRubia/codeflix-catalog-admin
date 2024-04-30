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
            
    def test_name_cannot_be_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")
            
    def test_category_must_be_created_with_id_uuid(self):
        categoria = Category(name="livros")
        assert isinstance(categoria.id, UUID)

        
    def test_created_category_must_be_created_with_default_(self):
        categoria = Category(name="livros")
        
        assert categoria.name ==  "livros"
        assert categoria.description == ""
        assert categoria.is_active is  True

    def test_created_category_must_be_created_with_provided_values(self):
        id_cat = uuid.uuid4()
        categoria = Category(id = id_cat, name="livros", description="descricao do livros", is_active=False)
        assert categoria.id ==  id_cat
        assert categoria.name ==  "livros"
        assert categoria.description == "descricao do livros"
        assert categoria.is_active is  False

    def test_category_str_(self):
        categoria = Category( name="livros", description="descricao do livros", is_active=False)
          
        expected_str = "livros - descricao do livros- (False)"
        actual_str = str(categoria)
        assert actual_str == expected_str
        
    def test_category_repr_(self):
        id_cat = uuid.uuid4()
        categoria = Category(id = id_cat, name="livros", description="descricao do livros", is_active=False)
          
        expected_repr = f"<Category livros ({categoria.id})> "
        actual_repr = repr(categoria)
        assert actual_repr == expected_repr
      

class TesteUpdateCategory:
                                                    
    def teste_update_category_with_name_and_description(self):
        categoria = Category(name="filme", description="descricao do filme")
        
        categoria.update_category(name="serie", description="descricao da serie")
        
        assert categoria.name ==  "serie"
        assert categoria.description == "descricao da serie"
        
        
        
    def teste_update_category_with_invalid_name(self):
        categoria = Category(name="filme", description="descricao do filme")
        
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            categoria.update_category(name="a" * 256, description="descricao da serie")
    
    def teste_update_category_with_empty_name(self):
        categoria = Category(name="filme", description="descricao do filme")
        
        with pytest.raises(ValueError, match="name cannot be empty"):
            categoria.update_category(name="", description="descricao da serie")   
            
class TestActivate:
    
    def test_activate_anactive_category(self):
        categoria = Category(name="filme", description="descricao do filme", is_active= False)
        categoria.activate()
        
        assert categoria.is_active is True
        
        
    def test_activate_active_category(self):
        categoria = Category(name="filme", description="descricao do filme")
        categoria.activate()
        
        assert categoria.is_active is True
        
        
    def test_deactivate_active_category(self):
        categoria = Category(name="filme", description="descricao do filme")
        categoria.deactivate()
        
        assert categoria.is_active is False
        
    def test_deactivate_disabled_category(self):
        categoria = Category(name="filme", description="descricao do filme",is_active= False)
        categoria.deactivate()
        
        assert categoria.is_active is False
        
class TestEquality:
    
    def test_when_categories_have_same_id_the_are_equal(self):
        id_cat1 = uuid.uuid4()
        categoria1 = Category( name="filme", id = id_cat1)
        categoria2 = Category( name="filme",  id = id_cat1)
        
        assert categoria1 == categoria2
         
         
    def test_equality_different_classes(self):
        class Dummy:
            pass
        id_cat1 = uuid.uuid4()
        categoria1 = Category( name="filme", id = id_cat1)
        
        dummy = Dummy()
        dummy.id = id_cat1
        
        assert categoria1 != dummy