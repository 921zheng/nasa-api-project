import requests
import json

class Nasa:
    def __init__(self):
        self.link='https://api.nasa.gov/DONKI/'

    def cme(self, key):
        endpoint=f'CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key={key}'
        response=requests.get(f'{self.link}{endpoint}')
        data=response.json()
        cme=data[0]['activityID']
        return cme

    def cme_analysis(self,key):
        endpoint=f'CMEAnalysis?startDate=2016-09-01&endDate=2016-09-30&mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL&api_key={key}'
        response=requests.get(f'{self.link}{endpoint}')
        data=response.json()
        analysis=data[0]['time21_5']
        return analysis


    def gst(self, key):
        endpoint=f'GST?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key={key}'
        response=requests.get(f'{self.link}{endpoint}')
        data=response.json()
        gst=data[0]['gstID']
        return gst


objOne=Nasa()
# print(objOne.cme('zDlGyS3aR00pXFk2Yd37u48mJQ8b63MFTbDVaFd9'))
# print(objOne.cme_analysis('zDlGyS3aR00pXFk2Yd37u48mJQ8b63MFTbDVaFd9'))
print(objOne.gst('zDlGyS3aR00pXFk2Yd37u48mJQ8b63MFTbDVaFd9'))