from selenium import webdriver

browser = webdriver.Remote(
    command_executor='http://127.0.0.1:4446/wd/hub',
    desired_capabilities={
        'browserName': 'chrome',
        'version': '',
        'platform': 'ANY',
        'goog:chromeOptions': {
            'extensions': [],
            'args': ['--no-sandbox', '-headless', '--disable-dev-shm-usage']}
    }
)

browser.get("https://sitoi.cn")
browser.get_screenshot_as_file("sitoi.png")
browser.quit()
