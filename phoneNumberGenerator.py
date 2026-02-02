from faker import Faker
from config import ReadConfig
import random

fake = Faker()

def getRandomNumber(calltype,numberType):
    phonenumber = ""
    config = ReadConfig.getConfig(calltype)
    if calltype == "./config/configIntl.json":
        if numberType == "caller":
            countryCode  = str(random.choice(config[numberType]['country_code']))
            provinceCode = str(random.choice(config[numberType]['province_code']))
            min = config[numberType]['telcom_code']['min']
            max = config[numberType]['telcom_code']['max']
            telcomCode = str(random.randint(min, max))
            phonenumber = f'{countryCode}{provinceCode}{telcomCode}{fake.numerify("####")}'
        else :
            countryCode = str(random.choice(config[numberType]['country_code']))
            number = "".join(random.choices("0123456789", k=10))
            phonenumber = f'{countryCode}{number}'   
    else:
        countryCode  = str(random.choice(config[numberType]['country_code']))
        provinceCode = str(random.choice(config[numberType]['province_code']))
        min = config[numberType]['telcom_code']['min']
        max = config[numberType]['telcom_code']['max']
        telcomCode = str(random.randint(min, max))
        phonenumber = f'{countryCode}{provinceCode}{telcomCode}{fake.numerify("####")}'
    return phonenumber