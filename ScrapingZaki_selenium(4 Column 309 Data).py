from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()
driver.set_window_size(3000, 2500) 
driver.implicitly_wait(30)
driver.get('https://www.visionplus.id/movies')

list_kategori = []
list_judul = []
list_link = []
list_genre = []
list_tahun = []
list_durasi = []
list_umur = []
count = 0

kategori_container = driver.find_elements(By.CSS_SELECTOR, value='div.row div.box-category:not(div.box-category:first-of-type)')
time.sleep(2)

for x in kategori_container:
    kategori = x.find_element(By.CSS_SELECTOR, 'div.title-container > h2').text
    time.sleep(2)

    judul_container = x.find_elements(By.CSS_SELECTOR, value='div.swiper-slide')
    for y in judul_container:
        list_kategori.append(kategori)


        action = ActionChains(driver)
        action.move_to_element(y).perform()
        
        link_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#G0')))
        link = link_element.get_attribute('href')
        list_link.append(link)
        

        try:
            tahun = link_element.find_element(By.CSS_SELECTOR, "div.text-caption:nth-of-type(1) > span:nth-of-type(1)").text
            genre = link_element.find_element(By.CSS_SELECTOR, ".q-mb-sm span").text
            durasi = link_element.find_element(By.CSS_SELECTOR, "span:nth-of-type(5)").text
            umur = link_element.find_element(By.CSS_SELECTOR, "span:nth-of-type(3)").text
            
            list_tahun.append(tahun)
            list_genre.append(genre)
            list_durasi.append(durasi)
            list_umur.append(umur)
            print(kategori, genre, tahun, durasi, umur)
            

        except:
            print('Element not found')
            list_tahun.append("")
            list_genre.append("")
            list_durasi.append("")
            list_umur.append("")


        judul_element = y.find_element(By.TAG_NAME, 'img')
        judul = judul_element.get_attribute('alt')
        list_judul.append(judul[7:])
        
        time.sleep(1)
        count += 1
        print("mendapatkan", count, kategori, "data...")        

driver.quit()


data = pd.DataFrame(list(zip(list_kategori, list_judul, list_tahun, list_umur, list_durasi, list_genre, list_link)),columns=
                    ['Kategori', "Judul", "Tahun", "Batas Umur", "Durasi", "Genre", "URL"])
data.to_csv('Assignment2_selenium.csv', index=False)