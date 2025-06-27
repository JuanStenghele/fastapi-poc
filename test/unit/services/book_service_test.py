import pytest


from unittest.mock import MagicMock
from services.book_service import BookService
from dal.book_dal import BookDAL
from objects.book import Book
from sqlmodel import Session


class TestBookService():
  def test_create_book_success(self):
    book_name = 'test_book'
    book_dal_mock = MagicMock(spec = BookDAL)
    book_dal_mock.create_book.return_value = Book(id = '1', name = book_name)
    session_mock = MagicMock(spec = Session)
    instance = BookService(book_dal_mock)
    book_result = instance.create_book(session_mock, book_name)
    assert book_result.id is not None
    assert book_result.name == book_name

  def test_create_book_fail(self):
    book_name = 'test_book'
    book_dal_mock = MagicMock(spec = BookDAL)
    book_dal_mock.create_book.side_effect = Exception('error')
    session_mock = MagicMock(spec = Session)
    instance = BookService(book_dal_mock)
    with pytest.raises(Exception) as e:
      instance.create_book(session_mock, book_name)
    assert str(e.value) == 'error'

  def test_get_book_success(self):
    book_id = '1'
    book_name = 'test_book'
    book_dal_mock = MagicMock(spec = BookDAL)
    book_dal_mock.get_book.return_value = Book(id = book_id, name = book_name)
    session_mock = MagicMock(spec = Session)
    instance = BookService(book_dal_mock)
    book_result = instance.get_book(session_mock, book_id)
    assert book_result is not None
    assert book_result.id == book_id
    assert book_result.name == book_name

  def test_get_book_fail(self):
    book_id = '1'
    book_dal_mock = MagicMock(spec = BookDAL)
    book_dal_mock.get_book.side_effect = Exception('error')
    session_mock = MagicMock(spec = Session)
    instance = BookService(book_dal_mock)
    with pytest.raises(Exception) as e:
      instance.get_book(session_mock, book_id)
    assert str(e.value) == 'error'
