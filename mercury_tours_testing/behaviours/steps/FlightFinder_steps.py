from behave import *
from tests.login import LoginTest
from tests.FlightFinder import FlightFinderTest
flightFinderTest = FlightFinderTest()
login = LoginTest()

#@given(u'Quiero buscar vuelos Mercury Tours')
#def step_impl(context):
#flightFinderTest.setUpClass()
    #login.test_go_url('http://newtours.demoaut.com/')
    #login.test_login("osolisd", "Moscar13*")

#@when(u'Ingreso un usuario "{user}" y un password "{password}"')
@when(u'Busco vuelos de {desde} hacia {hacia} para {cantidadPasajeros} pasajeros')
def step_impl(context, desde, hacia, cantidadPasajeros):
    context.desde = desde
    context.hacia = hacia
    context.cantidadPasajeros = cantidadPasajeros
    flightFinderTest.test_search_flight(context.desde, context.hacia, context.cantidadPasajeros)

#@then(u'El sistema me autentica como usuario legitimo')
@then(u'El sistema busca los vuelos')
def step_impl(context):
    flightFinderTest.test_reserve_flight()
    flightFinderTest.tearDownClass()
