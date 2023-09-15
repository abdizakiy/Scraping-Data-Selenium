from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.visionplus.id/movies')


list_kategori = []
list_judul = []
count = 0


kategori_container = driver.find_elements(By.CSS_SELECTOR, value='div.row div.box-category:not(div.box-category:first-of-type)')
for x in kategori_container:
    kategori = x.find_element(By.CSS_SELECTOR, 'div.title-container > h2').text
    
    judul_container = x.find_elements(By.CSS_SELECTOR, value='div.swiper-slide')
    for y in judul_container:
        judul = y.find_element(By.TAG_NAME, 'img').get_attribute('alt')
        
        list_kategori.append(kategori)
        list_judul.append(judul[7:])
        count += 1
        print('mendapatkan', count, 'film...')
    
driver.quit()


data = pd.DataFrame(list(zip(list_kategori, list_judul)),columns=['Kategori', "Judul"])
data.to_csv('Assignment2_selenium(2 Column 309 Data).csv', index=False)