from selenium import webdriver
import pytest

Accounts = [('testingkaryasa21@gmail.com','carrot2348'),
            ('testingsaja@gmail.com','carrot2348.'),
            ('testingkaryasa21','rambutan123@'),
            ('','carrot2348.'),
            ('testingkaryasa21@gmail.com','')
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    driver.implicitly_wait(10)
    driver.minimize_window()
    yield driver
    driver.close()


def test_login_success(setup):
    setup.find_element_by_id('login_field').send_keys('testingkaryasa21@gmail.com')
    setup.find_element_by_id('password').send_keys('carrot2348.')
    setup.find_element_by_name('commit').click()

    setup.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary').click()
    name = setup.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a/strong').text
    assert name == 'ranitestkarya'

@pytest.mark.parametrize('uemail,upassword', Accounts)
def test_login_unsuccess(setup, uemail, upassword):
    setup.find_element_by_id('login_field').send_keys(uemail)
    setup.find_element_by_id('password').send_keys(upassword)
    setup.find_element_by_name('commit').click()

    alert = setup.find_element_by_xpath('//*[@id="js-flash-container"]/div/div').is_displayed()
    assert alert == True


