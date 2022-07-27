import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://barru.pythonanywhere.com/daftar"

class Test1Register(unittest.TestCase):
    
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # test case 1 (success move from sign in form to sign up form)
    def test_a_success_move_from_sign_in_form_to_sign_up_form(self):
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        
        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/form/h1").text

        self.assertIn('Create', response_data)

    # test case 2 (failed register with empty name, email, and password)
    def test_b_failed_register_with_empty_name_email_and_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    # test case 3 (failed register with invalid email (without @))
    def test_c_failed_register_with_invalid_email_without_at(self):
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("abc") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("abc") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("abc") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        email_error = browser.find_element(By.ID,"email_register").get_attribute("validationMessage")
        # print("PRINT ERROR")
        # print(email_error)

        self.assertIn('Please', email_error)

    # test case 4 (failed register with invalid email TLD)
    def test_d_failed_register_with_invalid_email_tld(self):
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("qwerty") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("qwerty@qwerty.qwerty") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("qwerty") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    # test case 5 (success register)
    def test_e_success_register(self):
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("qwe") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("qwe@qwe.qwe") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("qwe") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    # test case 6 (failed register with registered email)
    def test_f_failed_register_with_registered_email(self):
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("qwe") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("qwe@qwe.qwe") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("qwe") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('sudah terdaftar', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def tearDown(self): 
        self.browser.close()

class Test2Login(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    # test case 7 (success move from sign in form to sign up form and back to sign in form)
    def test_g_success_move_from_sign_in_form_to_sign_up_form_and_back_to_sign_in_form(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"signIn").click() # klik tombol sign in
        time.sleep(1)
        
        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[2]/form/h1").text

        self.assertIn('in', response_data)

    # test case 8 (failed login with empty email and password)
    def test_h_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    # test case 9 (failed login with not registered email)
    def test_i_failed_login_with_not_registered_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("sqa@sqa.sqa") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("sqa") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    # test case 10 (success login)
    def test_j_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get(url) # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("qwe@qwe.qwe") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("qwe") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()