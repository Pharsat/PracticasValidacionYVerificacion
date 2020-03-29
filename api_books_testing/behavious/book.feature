Feature: Administracion de libros

  Scenario: consultar todos los libros
    Given Usuario consulta el endpoint
    When  realiza la peticion
    Then  ve el codigo de respuesta 200
    And   el ve 200 libros listados