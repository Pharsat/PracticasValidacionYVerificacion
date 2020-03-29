Feature: Administracion de autores

  Scenario: consultar los autores del libro 1
    Given usuario consulta el enpoint de autores por libro
    When  realiza la peticion get a la url https://fakerestapi.azurewebsites.net/authors/books/1
    Then  ve el codigo de respuesta 200
    And   el ve 3 autores listados

  Scenario: consultar los autores del libro 100
    Given usuario consulta el enpoint de autores por libro
    When  realiza la peticion get a la url https://fakerestapi.azurewebsites.net/authors/books/100
    Then  ve el codigo de respuesta 200
    And   el ve 2 autores listados

  Scenario: consultar todos los autores
    Given usuario consulta el enpoint de todos los autores
    When  realiza la peticion get a la url https://fakerestapi.azurewebsites.net/api/Authors
    Then  ve el codigo de respuesta 200
    And   el ve 400 autores listados

  Scenario: crear un autor
    Given usuario consulta el enpoing de crear un autor
    When  realiza la petición post al enpoint https://fakerestapi.azurewebsites.net/api/Authors
    Then  ve el codigo de respuesta 200
    And   el ve el autor que acaba de crear

  Scenario: eliminar el autor numero 10
    Given usuario consulta el endpoint de eliminar un autor
    When  realiza la petición delete al enpoint https://fakerestapi.azurewebsites.net/api/Authors/10
    Then  ve el codigo de respuesta 200
    And   el usuario obtiene una respuesta vacia.

  Scenario: consulta el autor numero 10
    Given usuario consulta el enpoint de un unico autor por id
    When  realiza la peticion get a la url https://fakerestapi.azurewebsites.net/api/Authors/10
    Then  ve el codigo de respuesta 200
    And   el ve un objeto de autor listado

  Scenario: actualizar el autor numero 20
    Given usuario consulta el enpoint de actualizar un autor
    When  realiza la peticion put a la https://fakerestapi.azurewebsites.net/api/Authors/20
    Then  ve el codigo de respuesta 200
    And   el ve un objeto de autor actualizado