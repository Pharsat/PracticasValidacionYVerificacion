import time
import unittest
from tests.login import LoginTest

login = LoginTest()

class FlightFinderTest(unittest.TestCase):

    # Este método realiza la búsqueda de los vuelos para la rutaespecificada
    def test_search_flight(self, desde, hacia, cantidadPasajeros):
        self.driver = login.driver
        self.driver.find_element_by_xpath("//select[@name='passCount']/option[@value=" + cantidadPasajeros + "]").click()
        self.driver.find_element_by_xpath("//select[@name='fromPort']/option[@value=" + desde + "]").click()
        self.driver.find_element_by_xpath("//select[@name='fromMonth']/option[@value='12']").click()
        self.driver.find_element_by_xpath("//select[@name='fromDay']/option[@value='1']").click()
        self.driver.find_element_by_xpath("//select[@name='toPort']/option[@value=" + hacia + "]").click()
        self.driver.find_element_by_xpath("//select[@name='toMonth']/option[@value='12']").click()
        self.driver.find_element_by_xpath("//select[@name='toDay']/option[@value='23']").click()
        self.driver.find_element_by_xpath("//input[@name='servClass']").click()
        self.driver.find_element_by_xpath("//select[@name='airline']/option[text()='Blue Skies Airlines']").click()
        self.driver.find_element_by_xpath("//input[@name='findFlights']").click()
        time.sleep(3)

    def test_reserve_flight(self):
        reserveFlights = self.driver.find_element_by_xpath("//input[@name='reserveFlights']")
        self.assertTrue(reserveFlights)

    def test_select_flight(self):
        self.driver.find_element_by_css_selector("input[type='radio'][value='Blue Skies Airlines$361$271$7:10']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][value='Pangea Airlines$632$282$16:37']").click()
        self.driver.find_element_by_xpath("//input[@name='reserveFlights']").click()
        # time.sleep(5)

    def test(self):
        self.driver.find_element_by_name("passFirst0").send_keys("Carlos")
        self.driver.find_element_by_name("passLast0").send_keys("Jaramillo")
        self.driver.find_element_by_name("creditnumber").send_keys("321654987")
        self.driver.find_element_by_name("buyFlights").click()
        # time.sleep(5)

    def test1(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Your itinerary has been bookt')]")
        # time.sleep(5)

    # Este método se ejecuta al final y cierra el navegador
    @ classmethod
    def tearDownClass(self):
        login.tearDownClass()

if __name__ == '__main__':
    unittest.main()
