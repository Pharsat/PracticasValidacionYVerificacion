Feature: Administracion de autores

  Scenario: consultar los autores del libro 1
    Given usuario consulta el enpoint de autores por libro
    When  realiza la peticion get a la url /authors/books/"1" del libro 1
    Then  ve el codigo de respuesta 200
    And   el ve "3" tres autores listados

