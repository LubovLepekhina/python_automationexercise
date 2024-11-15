import time

def test_open_url(driver):
    driver.get('https://automationexercise.com/')
    time.sleep(3)
    print(driver.current_url)
    print(driver.title)
    assert driver.current_url == 'https://automationexercise.com/'
    assert driver.title == 'Automation Exercise'

def test_login(driver):
    driver.get('https://www.saucedemo.com/')
    driver.find_element('css selector', "input[placeholder='Username']").send_keys('standard_user')
    time.sleep(2)
    driver.find_element('css selector', "input[placeholder='Password']").send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element('css selector', '#login-button').click()
    time.sleep(2)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    assert driver.title == 'Swag Labs'

# тесты Дениса
def test_strategy(driver):
    print()
    start_time = time.time()
    driver.get("https://letcode.in/test")
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time}")

def test1(driver):
    print()
    locator = "ul>li:first-child>a"
    locator1 = "a[href='/abtest']"
    locator2 = "//a[@href='/abtest']"
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)
    print(f"Начальная страница: {driver.current_url}")
    driver.find_element("xpath", locator2).click()
    time.sleep(2)
    print(f"Страницы А/Б тестов: {driver.current_url}")
    driver.back()
    print(f"Начальная страница: {driver.current_url}")
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    print(f"Страницы А/Б тестов: {driver.current_url}")
    driver.refresh()

def test3(driver):
    """
    Тест кейс №1
    Шаги воспроизведения:
    1. перейти на сайт https://the-internet.herokuapp.com/
    2. получить URL
    3. получить title
    4. проверить URL и title
    :param driver:
    :return:
    """
    print()
    driver.get("https://the-internet.herokuapp.com/")
    url = driver.current_url
    print(url)
    assert url == "https://the-internet.herokuapp.com/"
    title = driver.title
    print(title)
    assert title == "The Internet"

def test4(driver):
    username_loc = "input[data-test='username']"
    password_loc = "input[data-test='password']"
    login_btn_loc = "input[data-test='login-button']"
    username = "standard_user"
    password = "secret_sauce"
    check_url = "https://www.saucedemo.com/inventory.html"
    check_title = "Swag Labs"
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element("css selector", username_loc).send_keys(username)
    time.sleep(1)
    driver.find_element("css selector", password_loc).send_keys(password)
    time.sleep(1)
    driver.find_element("css selector", login_btn_loc).click()
    time.sleep(1)
    assert driver.current_url == check_url
    assert driver.title == check_title

def test5(driver):
    locator = "div[id='selectable']"
    driver.get("https://letcode.in/selectable")
    context = driver.find_elements("css selector", locator)
    for i in context:
        if i.text == "Appium":
            print(i.text)
            i.click()
            time.sleep(2)
            break
    print(context)