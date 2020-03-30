from behave import *

from api_books_testing.request_test.definition_step import ApirequestBooks

test_api = ApirequestBooks()


@given(u'Usuario consulta el endpoint')
def step_impl(context):
    context.endpoint = "/api/Books"


@when(u'realiza la peticion')
def step_impl(context):
    context.response = test_api.test_get_all_books(context.endpoint)


@then(u've el codigo de respuesta {code}')
def step_impl(context, code):
    context.code = code
    test_api.validate_code(int(context.code))


@then(u'el ve {number_books} libros listados')
def step_impl(context, number_books):
    context.number_books = number_books
    test_api.validate_number_book(int(context.number_books))



@when(u'envia la información del libro nuevo: "{id}","{title}","{Description}","{PageCount}","{Excerpt}","{PublishDate}"')
def step_impl(context,id,title,Description,PageCount,Excerpt,PublishDate):
    context.response=test_api.test_post_new_book(context.endpoint,id,title,Description,PageCount,Excerpt,PublishDate)


@then(u'el ve la informacion del libro creado en la respuesta')
def step_impl(context):
    test_api.valide_new_book()


@when(u'elimina el libro con id 1')
def step_impl(context):
    pass


@then(u'el ve la informacion del libro eliminado en la respuesta')
def step_impl(context):
    pass


@when(u'consulta el libro con id 10')
def step_impl(context):
    pass


@then(u'el ve la informacion del libro')
def step_impl(context):
    pass


@when(u'ingresa el id del libro 10')
def step_impl(context):
    pass


@when(u'envia la informacion del libro para actualizar')
def step_impl(context):
    pass


@then(u'el ve la informacion del libro actualizado')
def step_impl(context):
    pass
