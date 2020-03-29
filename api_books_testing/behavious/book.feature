Feature: Administracion de libros

  Scenario: consultar todos los libros
    Given usuario consulta el endpoint
    When  realiza la peticion
    Then  ve el codigo de respuesta 200
    And   el ve 200 libros listados

  Scenario: Agregar nuevo libro
    Given usario ingresa al endpoint
    When  envia la información del libro nuevo
    Then  Ve el codigo de respuesta 200
    And   el ve la informacion del libro creado en la respuesta


    Scenario: Elimina libro por id
      Given usuario consulta el endpoint
      When  elimina el libro con id 1
      Then  ve el codigo de respuesta 200
      And   el ve la informacion del libro eliminado en la respuesta

  Scenario: Consulta libro por id
      Given usuario consulta el endpoint
      When  consulta el libro con id 10
      Then  ve el codigo de respuesta 200
      And   el ve la informacion del libro

    Scenario: Actualizar libro
      Given Usuario consulta el endpoint
      When  ingresa el id del libro 10
      And   envia la informacion del libro para actualizar
      Then  ve el codigo de respuesta 200
      And   el ve la informacion del libro actualizado
