Feature: Buscar vuelos en Mercury Tours

  Scenario: Consulta vuelos
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "Paris" hacia "Seattle" para "2" pasajeros
    Then El sistema busca los vuelos

  Scenario: Seleccion vuelo
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "Paris" hacia "Seattle" para "2" pasajeros
    And Seleccionar vuelos
    Then Ver formulario de datos de reserva