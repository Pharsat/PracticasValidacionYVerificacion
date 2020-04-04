Feature: Buscar vuelos en Mercury Tours

  Scenario: Consulta vuelos de Paris a Seatle 2 pasajeros en aerolínea Blue Skies Airlines
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "Paris" hacia "Seattle" para "2" pasajeros en la aerolinea "Blue Skies Airlines"
    Then El sistema muestra los vuelos disponibles

  Scenario: Consulta vuelos de London a Frankfurt 3 pasajeros en aerolínea Unified Airlines
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "London" hacia "Frankfurt" para "3" pasajeros en la aerolinea "Unified Airlines"
    Then El sistema muestra los vuelos disponibles

  Scenario: Consulta vuelos de London a Frankfurt 3 pasajeros en aerolínea Blue Skies Airlines
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "London" hacia "Frankfurt" para "3" pasajeros en la aerolinea "Blue Skies Airlines"
    Then El sistema muestra los vuelos disponibles

  Scenario: Confirmación de reserva Carlos Jaramillo de Londres a Frankfurt Blue Skies Airlines
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "London" hacia "Frankfurt" para "1" pasajeros en la aerolinea "Blue Skies Airlines"
    And Selecciono el vuelo de ida y de regreso
    And Ingreso los datos de los pasajeros Carlos Jaramillo "Visa" 123456789 02 2010 cll10#40-20 Medellin Antioquia 057
    Then El sistema confirma la reserva

  Scenario: Confirmación de reserva Ana Torres de Paris a Londres Pangea Airlines
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "Paris" hacia "London" para "1" pasajeros en la aerolinea "Pangea Airlines"
    And Selecciono el vuelo de ida y de regreso
    And Ingreso los datos de los pasajeros Ana Torres "MasterCard" 987456987 05 2009 cll50#10-32 Sabaneta Antioquia 057
    Then El sistema confirma la reserva