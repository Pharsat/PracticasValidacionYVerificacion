from behave import *
from api_books_testing.request_test.definition_step import ApirequestBooks

test_api=ApirequestBooks()

@given(u'Usuario consulta el endpoint')
def step_impl(context):
    context.endpoint="/api/Books"


@when(u'realiza la peticion')
def step_impl(context):
    context.response = test_api.test_get_all_books(context.endpoint)


@then(u've el codigo de respuesta {code}')
def step_impl(context, code):
    context.code=code
    test_api.validate_code(int(context.code))



@then(u'el ve {number_books} libros listados')
def step_impl(context,number_books):
    context.number_books=number_books
    test_api.validate_number_book(int(context.number_books))
