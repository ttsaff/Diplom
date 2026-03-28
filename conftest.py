import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> WebDriver:
    """Драйвер с настройками против CAPTCHA"""
    options: Options = Options()

    # Скрыть признаки автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    #  Реалистичный User-Agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    #  Для macOS/Linux
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Отключить images (быстрее)
    prefs: dict = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    #  Сказать браузеру что это реальный Chrome
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    driver: WebDriver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Inject JS чтобы скрыть что это Selenium
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => false})"
    )

    yield driver
    driver.quit()
