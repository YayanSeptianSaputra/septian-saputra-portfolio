"""Selenium (Python) + pytest pada situs demo publik saucedemo.com. Tanpa data privat."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "https://www.saucedemo.com"


@pytest.fixture()
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    d = webdriver.Chrome(options=opts)
    yield d
    d.quit()


def wait_for(driver, locator):
    # explicit wait, tanpa sleep tetap
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))


def login(driver, user, password):
    driver.get(BASE)
    wait_for(driver, (By.ID, "user-name")).send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_login_gagal_menampilkan_pesan_error(driver):
    login(driver, "standard_user", "salah")
    err = wait_for(driver, (By.CSS_SELECTOR, "[data-test='error']"))
    assert "do not match" in err.text


def test_login_berhasil_membuka_daftar_produk(driver):
    login(driver, "standard_user", "secret_sauce")
    wait_for(driver, (By.CLASS_NAME, "inventory_list"))
    assert driver.current_url.endswith("/inventory.html")
    assert len(driver.find_elements(By.CLASS_NAME, "inventory_item")) == 6


def test_urut_harga_rendah_ke_tinggi(driver):
    login(driver, "standard_user", "secret_sauce")
    wait_for(driver, (By.CLASS_NAME, "inventory_list"))
    from selenium.webdriver.support.ui import Select
    Select(driver.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")).select_by_value("lohi")
    prices = [float(e.text.replace("$", "")) for e in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices)


def test_tambah_ke_keranjang_mengubah_badge(driver):
    login(driver, "standard_user", "secret_sauce")
    wait_for(driver, (By.CLASS_NAME, "inventory_list"))
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = wait_for(driver, (By.CLASS_NAME, "shopping_cart_badge"))
    assert badge.text == "1"
