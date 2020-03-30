Feature: Administracion de libros

  Scenario: consultar todos los libros
    Given usuario consulta el endpoint
    When  realiza la peticion
    Then  ve el codigo de respuesta 200
    And   el ve 200 libros listados

  Scenario Outline: Agregar nuevo libro
    Given usuario consulta el endpoint
    When  envia la información del libro nuevo: "<id>","<titulo>","<descripcion>","<num_pag>","<extracto>","<fecha_publicacion>"
    Then  Ve el codigo de respuesta 200
    And   el ve la informacion del libro creado en la respuesta
    Examples:
      | id  | titulo             | descripcion | num_pag                                             | extracto           | fecha_publicacion   |
      | 202 | Catalino Bocachica | 100         | Suenos hechos realidad gracias al empeno y el valor | Lorem lorem lorem. | 1998-03-05T00:00:00 |

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
    Given usuario consulta el endpoint
    When  ingresa el id del libro 10
    And   envia la informacion del libro para actualizar
    Then  ve el codigo de respuesta 200
    And   el ve la informacion del libro actualizado
