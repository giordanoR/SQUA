import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLoginMultiRol(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[CONFIG] Inicializando entorno WebDriver UNA SOLA VEZ...")
        opciones = webdriver.ChromeOptions()
        opciones.add_experimental_option("detach", True)
        
        cls.driver = webdriver.Chrome(options=opciones)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_cp_001_login_doctora_exitoso(self):
        print("\n" + "="*60)
        print("EJECUTANDO: CP-001 - Autenticación y Ruteo de la Doctora")
        print("="*60)
        
        self.driver.get("file:///C:/final/login_dentista.html")
        
        # Datos de Entrada
        self.wait.until(EC.presence_of_element_located((By.ID, "correo"))).send_keys("doctora@dentalsys.com")
        self.driver.find_element(By.ID, "password").send_keys("DocDental2026*")
        time.sleep(2) # Pausa para que el ingeniero lo vea
        
        self.driver.find_element(By.ID, "btn-login").click()
        
        # Verificación
        elemento_header = self.wait.until(EC.visibility_of_element_located((By.ID, "rol-header")))
        valor_actual = elemento_header.text
        valor_esperado = "Panel de la Doctora Rojas"
        
        self.assertEqual(valor_esperado, valor_actual, "Error: No se redirigió.")
        print("✅ VEREDICTO CP-001: PASS")
        time.sleep(3) # Pausa para ver el panel antes de la siguiente prueba

    def test_cp_002_login_asistente_exitoso(self):
        print("\n" + "="*60)
        print("EJECUTANDO: CP-002 - Autenticación y Ruteo del Asistente")
        print("="*60)
        
        self.driver.get("file:///C:/final/login_dentista.html")
        
        # Datos de Entrada
        self.wait.until(EC.presence_of_element_located((By.ID, "correo"))).send_keys("asistente@dentalsys.com")
        self.driver.find_element(By.ID, "password").send_keys("AsisDental2026*")
        time.sleep(2)
        
        self.driver.find_element(By.ID, "btn-login").click()
        
        # Verificación
        elemento_header = self.wait.until(EC.visibility_of_element_located((By.ID, "rol-header")))
        valor_actual = elemento_header.text
        valor_esperado = "Panel de Control de Asistencia"
        
        self.assertEqual(valor_esperado, valor_actual, "Error: No se redirigió.")
        print("✅ VEREDICTO CP-002: PASS")

    @classmethod
    def tearDownClass(cls):
        print("\n[CLEANUP] Pruebas finalizadas. El navegador se quedará abierto por la opción detach.")
        # AQUÍ NO HAY DRIVER.QUIT(), el navegador se queda abierto para tu defensa.

if __name__ == "__main__":
    unittest.main()