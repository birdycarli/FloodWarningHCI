from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def GetWaterLevel(fileName):
    driver = webdriver.Chrome()

    states = ['PLS','KDH', 'PNG', 'PRK', 'SEL', 'NSN', 'MLK', 'JHR', 'PHG', 'TRG', 'KEL']
    data = {
        'state': [],
        'district': [],
        'waterLevel': [],
        'normal': [],
        'alert': [],
        'warning': [],
        'danger': []
    }

    for state in states: 
        driver.get("https://publicinfobanjir.water.gov.my/aras-air/data-paras-air/?state=" + state + "&lang=en")
        table = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'normaltable1'))
        )

        districts = []
        
        districtsWeb = table.find_elements(By.XPATH, '//td[@data-th="District"]')

        for districtWeb in districtsWeb:
            districts.append(districtWeb.text)

        indexes = [districts.index(x) for x in sorted(set(districts), reverse = True)]
        indexes = indexes[0:3]
        lines = (table.text).strip().split('\n')
        waterLevelDatas = []
        simplifiedDistrict = []

        for index in indexes:
            datas = lines[index+3].split()
            waterLevelDatas.append(datas[-5:])
            simplifiedDistrict.append(districts[index])

        labels = ['waterLevel', 'normal', 'alert', 'warning', 'danger']
        for district in simplifiedDistrict:
            data['district'].append(district)
            data['state'].append(state)  

        for row in waterLevelDatas:
            for i in range(len(row)):
                data[labels[i]].append(row[i])

    df = pd.DataFrame(data)
    df.to_csv(fileName, index=False)

    driver.quit()