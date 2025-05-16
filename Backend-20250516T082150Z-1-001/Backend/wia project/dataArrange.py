import pandas as pd 
from datetime import date

def InputDate(fileName):
    df = pd.read_csv(fileName)

    dateToday = date.today()
    try:
        df.insert(0, 'date', dateToday)
    except: 
        df['date'] = dateToday

    df.to_csv(fileName, index=False)


def AddColumns(mainFile, firstFile, secondFile):
    df1 = pd.read_csv(firstFile)
    df1Sorted = df1.sort_values(by='state').reset_index(drop=True)
    df2 = pd.read_csv(secondFile)


    data = {
        'rainfallDay1': [],
        'rainfallDay2': [],
        'rainfallDay3': [],
        'rainfallDay4': [],
        'rainfallDay5': [],
    }

    for i in range(0, len(df2), 5):
        #highTemps = df2.iloc[i:i+5]['highestTemperature']
        #lowTemps = df2.iloc[i:i+5]['lowestTemperature']
        rainfalls = df2.iloc[i:i+5]['rainfall']

        #data['state'].append(df2.iloc[i]['state'])

        j=1
        for rainfall in rainfalls:
            for i in range (3):
                data['rainfallDay' + str(j)].append(rainfall)
            j +=1

        '''
        for highTemp, lowTemp in zip(highTemps, lowTemps):
            data['highTemp'].append(highTemp)
            data['lowTemp'].append(lowTemp)
        '''

    df = pd.DataFrame(data)
    combined = pd.concat([df1Sorted,df], axis=1)
    combined.to_csv(mainFile, mode ='a', index=False, header=False)
 

def ReplaceStateName(fileName):
    stateNames = ['perlis', 'kedah', 'penang', 'perak', 'selangor', 'negeri-sembilan', 'malacca', 'johor', 'pahang', 'terengganu', 'kelantan']
    df = pd.read_csv(fileName)
    i=0

    for stateName in stateNames:
        df.loc[i:i+2, ['state']] = stateName
        i+=3

    df.to_csv(fileName, index=False)


def ReplaceErrorValue(fileName):
    df = pd.read_csv(fileName)

    df['waterLevel'] = df['waterLevel'].where(df['waterLevel'] != -9999.00, df['normal'])

    df.to_csv(fileName, index=False)


def ClearData(fileName1, fileName2):
    f = open(fileName1, "w")
    f.truncate()
    f.close()

    f = open(fileName2, "w")
    f.truncate()
    f.close()


#InputDate('waterLevel.csv')
#ReplaceStateName('waterLevel.csv')
#InputDate("waterLevel.csv")
#AddColumns('finalData.csv', 'waterLevel.csv', 'rainfallandTemp.csv')
#ReplaceErrorValue('waterLevel.csv')
#ClearData("rainfallAndTemp.csv", "waterLevel.csv")