import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class TestLoginMultiRol(unittest.TestCase):

    def setUp(self):
        print("\n[CONFIG] Inicializando entorno WebDriver...")
        opciones = webdriver.ChromeOptions()
        opciones.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=opciones)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        # Ruta exacta del archivo base
        self.url_login = "file:///C:/final/login_dentista.html"

    def test_cp_001_login_doctora_exitoso(self):
        print("\n" + "="*60)
        print("EJECUTANDO: CP-001 - Autenticación y Ruteo de la Doctora")
        print("="*60)
        
        self.driver.get(self.url_login)
        
        # Datos de Entrada
        self.wait.until(EC.presence_of_element_located((By.ID, "correo"))).send_keys("doctora@dentalsys.com")
        self.driver.find_element(By.ID, "password").send_keys("DocDental2026*")
        time.sleep(1) # Pausa para el video demo
        
        self.driver.find_element(By.ID, "btn-login").click()
        
        # Verificación del Dashboard de la Doctora
        elemento_header = self.wait.until(EC.visibility_of_element_located((By.ID, "rol-header")))
        valor_actual = elemento_header.text
        valor_esperado = "Panel de la Doctora Rojas"
        
        print(f"  > Validando redirección... Texto en UI obtenido: '{valor_actual}'")
        self.assertEqual(valor_esperado, valor_actual, "Error: No se redirigió al portal médico de la Doctora.")
        print("✅ VEREDICTO CP-001: PASS")
        time.sleep(2)

    def test_cp_002_login_asistente_exitoso(self):
        print("\n" + "="*60)
        print("EJECUTANDO: CP-002 - Autenticación y Ruteo del Asistente")
        print("="*60)
        
        self.driver.get(self.url_login)
        
        # Datos de Entrada
        self.wait.until(EC.presence_of_element_located((By.ID, "correo"))).send_keys("asistente@dentalsys.com")
        self.driver.find_element(By.ID, "password").send_keys("AsisDental2026*")
        time.sleep(1)
        
        self.driver.find_element(By.ID, "btn-login").click()
        
        # Verificación del Dashboard del Asistente
        elemento_header = self.wait.until(EC.visibility_of_element_located((By.ID, "rol-header")))
        valor_actual = elemento_header.text
        valor_esperado = "Panel de Control de Asistencia"
        
        print(f"  > Validando redirección... Texto en UI obtenido: '{valor_actual}'")
        self.assertEqual(valor_esperado, valor_actual, "Error: No se redirigió al portal administrativo del Asistente.")
        print("✅ VEREDICTO CP-002: PASS")
        time.sleep(2)

    def tearDown(self):
        print("[CLEANUP] Cerrando instancia de prueba...")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
    # ... (al final de tus pruebas)
    def tearDown(self):
        # Este comando hará que el navegador NO se cierre 
        # hasta que tú presiones ENTER en la terminal de VS Code
        input("\n🔥 Pruebas terminadas. Presiona ENTER en la terminal para cerrar el navegador...")
        self.driver.quit()