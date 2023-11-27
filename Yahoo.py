from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



PREVIOUS_CLOSE_XPATH = '//*[@id="nimbus-app"]/section/section/section/article/div[2]/ul/li[1]/span[2]/fin-streamer'




class Stock:
    def __init__(self, ticker):
        self.ticker_symbol = ticker
        self.regular_market_price = None
        self.previous_close = None
        self.open = None
        self.days_range = None

    def __repr__(self):
        return f"StockInfo(ticker_symbol={self.ticker_symbol}, " \
               f"regular_market_price={self.regular_market_price}, " \
               f"previous_close={self.previous_close}, " \
               f"open={self.open}, " \
               f"days_range={self.days_range})\n\n"
    
    def scrape_data(self,driver):
        url = 'https://finance.yahoo.com/quote/' + self.ticker_symbol
        driver.get(url)

        #Sets Previous Close of Stock
        #self.previous_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,PREVIOUS_CLOSE_XPATH)))
        self.previous_close = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PREV_CLOSE-value"]').text

        self.regular_market_price = driver\
        .find_element(By.CSS_SELECTOR, f'[data-symbol="{self.ticker_symbol}"][data-field="regularMarketPrice"]')\
        .text

        self.open = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="OPEN-value"]').text
        self.days_range = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="DAYS_RANGE-value"]').text
        #driver.close()


ticker_stocks = ["AMZN","AAPL","SHOP","ROKU"]


options = Options()

driver = webdriver.Chrome(options=options)


tesla = Stock("TSLA")
tesla.scrape_data(driver)
print(tesla)

for ticker in ticker_stocks:
    S = Stock(ticker)
    S.scrape_data(driver)
    print(S)

driver.quit()