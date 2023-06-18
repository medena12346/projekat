from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.project_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.project_driver.get("https://www.saucedemo.com")
        self.project_driver.maximize_window()
    
    def login(self, username, password):
        username_field_locator = (By.ID, "user-name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        

        password_field = self.project_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.project_driver.find_element(By.ID, "login-button")
        login_button.click()
        
    def is_login_and_signup_invisible(self):
        shopping_icon_locator = (By.ID, "shopping_cart_container")
        self.wait.until(EC.visibility_of_element_located(shopping_icon_locator))
       
    def get_page_title(self):
        page_title = (By.CLASS_NAME, "title")
        wait_page_title = self.wait.until(EC.element_to_be_clickable(page_title))
        title_text = wait_page_title.text
        return title_text       
    
        
        
    
    def Products(self):
        
        product1_button = self.project_driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        product1_button.click()
        
        product2_button = self.project_driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        product2_button.click()
        
        basket_button = self.project_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        basket_button.click()
        
    
        
        
    def product1_text(self):
        product1_text_tuple = (By.XPATH, "//*[text()=\"Sauce Labs Bolt T-Shirt\"]")
        Wait_product1_text = self.wait.until(EC.visibility_of_element_located(product1_text_tuple))
        product1_text = Wait_product1_text.text
        return product1_text
    
    
    def product2_text(self):
        product2_text_tuple = (By.XPATH, "//*[text()=\"Test.allTheThings() T-Shirt (Red)\"]")
        Wait_product2_text = self.wait.until(EC.visibility_of_element_located(product2_text_tuple))
        product2_text = Wait_product2_text.text
        return product2_text   
        
    def checkout(self):
        
        checkout_button = self.project_driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
    
    
    def checkout_information(self, name, surname, zipkod):
        name_field_locator = (By.ID, "first-name")
        wait_name_field = self.wait.until(EC.element_to_be_clickable(name_field_locator))
        wait_name_field.click()
        wait_name_field.clear()
        wait_name_field.send_keys(name)

        

        surname_field = self.project_driver.find_element(By.ID, "last-name")
        surname_field.click()
        surname_field.clear()
        surname_field.send_keys(surname)
        
        zipkod_field = self.project_driver.find_element(By.ID, "postal-code")
        zipkod_field.click()
        zipkod_field.clear()
        zipkod_field.send_keys(zipkod)
        
        continue_button = self.project_driver.find_element(By.ID, "continue")
        continue_button.click()  

    def finish_action(self):
        finish_button = self.project_driver.find_element(By.ID, "finish")
        finish_button.click()     
 
    def click_burger_menu(self):
        burger_menu_locator = self.project_driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu_locator.click()

    def log_out(self):
        log_out_locator = (By.ID, "logout_sidebar_link")
        log_out = self.wait.until(EC.element_to_be_clickable(log_out_locator))
        log_out.click()  
    
    def verify_order_completion(self):
        verification_message = (By.XPATH, "//a[@id='checkout_complete_container']/h2")
        self.wait.until(EC.visibility_of_element_located(verification_message))
        message = verification_message.text
        return message

    def login_page(self):
        login_button_locator = (By.ID, "login-button")
        self.wait.until(EC.element_to_be_clickable(login_button_locator))
        
   
        
    
    
        
    
    
    

    

    

        
    
    
    