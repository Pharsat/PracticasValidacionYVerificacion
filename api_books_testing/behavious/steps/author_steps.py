from behave import *
from api_books_testing.request_test.definition_step import ApirequestBooks


@given(u'usuario consulta el enpoint de autores por libro')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given usuario consulta el enpoint de autores por libro')


@when(u'realiza la peticion get a la url https://fakerestapi.azurewebsites.net/authors/books/1')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la peticion get a la url https://fakerestapi.azurewebsites.net/authors/books/1')


@then(u'el ve 3 autores listados')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ve 3 autores listados')


@when(u'realiza la peticion get a la url https://fakerestapi.azurewebsites.net/authors/books/100')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la peticion get a la url https://fakerestapi.azurewebsites.net/authors/books/100')


@then(u'el ve 2 autores listados')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ve 2 autores listados')


@given(u'usuario consulta el enpoint de todos los autores')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given usuario consulta el enpoint de todos los autores')


@when(u'realiza la peticion get a la url https://fakerestapi.azurewebsites.net/api/Authors')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la peticion get a la url https://fakerestapi.azurewebsites.net/api/Authors')


@then(u'el ve 400 autores listados')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ve 400 autores listados')


@given(u'usuario consulta el enpoing de crear un autor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given usuario consulta el enpoing de crear un autor')


@when(u'realiza la petición post al enpoint https://fakerestapi.azurewebsites.net/api/Authors')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la petición post al enpoint https://fakerestapi.azurewebsites.net/api/Authors')


@then(u'el ve el autor que acaba de crear')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ve el autor que acaba de crear')


@given(u'usuario consulta el endpoint de eliminar un autor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given usuario consulta el endpoint de eliminar un autor')


@when(u'realiza la petición delete al enpoint https://fakerestapi.azurewebsites.net/api/Authors/10')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la petición delete al enpoint https://fakerestapi.azurewebsites.net/api/Authors/10')


@then(u'el usuario obtiene una respuesta vacia.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el usuario obtiene una respuesta vacia.')


@given(u'usuario consulta el enpoint de un unico autor por id')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given usuario consulta el enpoint de un unico autor por id')


@when(u'realiza la peticion get a la url https://fakerestapi.azurewebsites.net/api/Authors/10')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la peticion get a la url https://fakerestapi.azurewebsites.net/api/Authors/10')


@then(u'el ve un objeto de autor listado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ve un objeto de autor listado')


@given(u'usuario consulta el enpoint de actualizar un autor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given usuario consulta el enpoint de actualizar un autor')


@when(u'realiza la peticion put a la https://fakerestapi.azurewebsites.net/api/Authors/20')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When realiza la peticion put a la https://fakerestapi.azurewebsites.net/api/Authors/20')


@then(u'el ve un objeto de autor actualizado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ve un objeto de autor actualizado')
