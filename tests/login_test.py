import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    assert "Swag Labs" in driver.page_source

    driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("invalid_user")
    password_input.send_keys("invalid_password")
    login_button.click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.text

    driver.quit()