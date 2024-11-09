from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
ChromeDriverManager().install()
driver = webdriver.Chrome()

# Open a URL
driver.get("https://www.google.com")

# Interact with the page (optional)
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium")
search_box.submit()

# Wait for a moment to see results
driver.implicitly_wait(5)

# Close the browser
driver.quit()
