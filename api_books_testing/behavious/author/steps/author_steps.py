import json
from behave import *
from api_books_testing.author_request_test.definition_step import ApiRequestAuthors

test = ApiRequestAuthors()


@given(u'usuario consulta el enpoint de autores por libro')
def step_impl(context):
    context.endpoint = "/authors/books/{}"


@when(u'realiza la peticion get a la url /authors/books/"{id}" del libro 1')
def step_impl(context, id):
    context.response = test.test_get_all_authors_by_book(context.endpoint, id)
    print(context.response)


@then(u'el ve "{authors_required_quantity}" tres autores listados')
def step_impl(context, authors_required_quantity):
    test.test_items_count(context)
    test.assertEqual(context.items_count, authors_required_quantity)


@when(u'realiza la peticion get a la url /authors/books/"{id}" del libro 100')
def step_impl(context, id):
    context.response = test.test_get_all_authors_by_book(context.endpoint, id)


@then(u'el ve "{authors_required_quantity}" dos autores listados')
def step_impl(context, authors_required_quantity):
    test.test_items_count(context)
    test.assertEqual(context.items_count, authors_required_quantity)


@given(u'usuario consulta el enpoint de todos los autores')
def step_impl(context):
    context.endpoint = "/api/Authors"


@when(u'realiza la peticion get a la url /api/Authors')
def step_impl(context):
    context.response = test.test_get_all_authors(context.endpoint)


@then(u'el ve "{authors_required_quantity}" cuatroscientos autores listados')
def step_impl(context, authors_required_quantity):
    test.test_items_count(context)
    test.assertEqual(context.items_count, authors_required_quantity)


@given(u'usuario consulta el enpoing de crear un autor')
def step_impl(context):
    context.endpoint = "/api/Authors"


@when(u'realiza la petición post al enpoint /api/Authors con nombre "{author_name}", apellido "{author_lastname}" autor del libro "{book_id}"')
def step_impl(context, author_name, author_lastname, book_id):
    payload = {
      "IDBook": book_id,
      "FirstName": author_name,
      "LastName": author_lastname
    }
    context.response = test.test_create_author(context.endpoint, payload)


@then(u'el ve el autor que acaba de crear es nombre "{author_name}", apellido "{author_lastname}" autor del libro "{book_id}"')
def step_impl(context, author_name, author_lastname, book_id):
    test.test_item_check(context)
    payload = {
        "IDBook": book_id,
        "FirstName": author_name,
        "LastName": author_lastname
    }
    json_payload = json.loads(payload)
    test.assertEqual(context.item, json_payload)



@given(u'usuario consulta el endpoint de eliminar un autor')
def step_impl(context):
    context.endpoint = "/api/Authors/{}"


@when(u'realiza la petición delete al enpoint /api/Authors/"{id}"')
def step_impl(context, id):
    context.response = test.test_delete_author(context.endpoint, id)


@then(u'el usuario obtiene una respuesta vacia.')
def step_impl(context):
    pass


@given(u'usuario consulta el enpoint de un unico autor por id')
def step_impl(context):
    pass


@when(u'realiza la peticion get a la url /api/Authors/10')
def step_impl(context):
    pass


@then(u'el ve un objeto de autor listado')
def step_impl(context):
    pass


@given(u'usuario consulta el enpoint de actualizar un autor')
def step_impl(context):
    pass


@when(u'realiza la peticion put a la /api/Authors/20')
def step_impl(context):
    pass


@then(u'el ve un objeto de autor actualizado')
def step_impl(context):
    pass
