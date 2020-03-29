Feature: escenarios relacionados al login de mercury tools

  Scenario:
    Given Estoy en la pagina de login Mercury Tours
    When Ingreso un usuario "cfgallegor" y un password "ICE_Master"
    Then El sistema me autentica como usuario legitimo

   Scenario:
    Given Estoy en la pagina de login Mercury Tours
    When Ingreso un usuario "cfgallegor" y un password "EstePasswordEstaMal"
    Then El sistema no me autentica como usuario legitimo