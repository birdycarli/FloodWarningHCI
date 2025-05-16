import waterLevelScraping
import rainfallandTempScraping
import dataArrange

dataArrange.ClearData("rainfallAndTemp.csv", 'waterLevel.csv')

rainfallandTempScraping.GetRainfallAndTemp("rainfallAndTemp.csv")
waterLevelScraping.GetWaterLevel("waterLevel.csv")

dataArrange.InputDate('finalData.csv')
dataArrange.AddColumns('finalData.csv', 'waterLevel.csv', 'rainfallAndTemp.csv')
dataArrange.ReplaceErrorValue('finalData.csv')

