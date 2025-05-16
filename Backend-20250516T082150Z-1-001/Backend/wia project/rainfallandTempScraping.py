from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def GetRainfallAndTemp(fileName):
    driver = webdriver.Chrome()

    stateMalaysia = {
        'johor' : ['johor-bahru', '228029'],
        'kedah': ['alor-setar', '228319'], 
        'kelantan': ['kota-bharu', '228390'], 
        'malacca': ['malacca', '229199'],
        'negeri-sembilan': ['seremban', '229315'], 
        'pahang': ['kuantan', '229423'], 
        'penang': ['george-town', '234975'], 
        'perak': ['ipoh', '234818'], 
        'perlis': ['kangar', '229830'], 
        'selangor': ['shah-alam', '230464'], 
        'terengganu': ['kuala-terengganu', '230666'], 
    }

    with open (fileName, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['state', 'city', 'rainfall', 'highestTemperature', 'lowestTemperature'])


    for state, data in stateMalaysia.items():        #data[0] is the city, data[1] is the code for the website
        for i in range(1,6):

            driver.get("https://www.accuweather.com/en/my/" + data[0] + "/" + data[1] + 
                    "/daily-weather-forecast/" + data[1] + "?day="+ str(i))

            try:
                rainfall = driver.find_element("xpath", "/html/body/div/div[7]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/p[2]/span").text
                rainfall = float(''.join(filter(str.isdigit, rainfall)))/10
            except: 
                rainfall = 0
                
            temps = driver.find_elements(By.CLASS_NAME, 'temperature')
            highestTemp = int(''.join(filter(str.isdigit, temps[0].text)))
            lowestTemp = int(''.join(filter(str.isdigit, temps[1].text)))

            with open (fileName, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([state, data[0], rainfall, highestTemp, lowestTemp])
    driver.quit()