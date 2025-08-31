from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_product():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    # Log in
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Add a product to the cart
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()

    # Verify the product is added to the cart
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    sleep(5)
    assert cart_badge.text == "1"

    driver.quit()