import pytest
from selenium import webdriver


# fetch url based on client role, edit configuration / additional arguments / enter "client_role = {role}"
@pytest.fixture(scope="class")
def setup(request, client_role="administrator"):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    if client_role == "reporter":
        url = "https://redrabbit.rebaseventures.com/catch-of-the-day/maintenance"
    elif client_role == "administrator":
        url = "https://redrabbit.rebaseventures.com/"
    else:
        raise ValueError("Invalid client role provided")

    driver.get(url)
    #driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.close()
