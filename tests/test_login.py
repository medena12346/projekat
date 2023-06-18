from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_page_title() == "Products"
    home_page.Products()
    assert home_page.get_page_title() =="Your Cart"
    
    assert home_page.product1_text() == "Sauce Labs Bolt T-Shirt"
    assert home_page.product2_text() == "Test.allTheThings() T-Shirt (Red)"
    home_page.checkout()
    assert home_page.get_page_title() == "Checkout: Your Information"
    home_page.checkout_information("medina", "smajlovic","71210")
    assert home_page.get_page_title() == "Checkout: Overview"
    home_page.finish_action()

    home_page.get_page_title() == "Checkout: Complete!"
    home_page.click_burger_menu()
    home_page.log_out()

    home_page.login_page()
    
    
    
    
    
