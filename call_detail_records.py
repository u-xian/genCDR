from faker import Faker
from decimal import Decimal
import random
from datetime import datetime, timedelta
from config import ReadConfig
import json
from cdr import CallRecord
import phoneNumberGenerator

fake = Faker()

def generate_cdr(calltype):
    config = ReadConfig.getConfig(calltype)
    anumber = phoneNumberGenerator.getRandomNumber(calltype,'caller')
    bnumber = phoneNumberGenerator.getRandomNumber(calltype,'called')
    duration = random.randint(config['duration_seconds']['min'], 
                              config['duration_seconds']['max'])  # duration in seconds 
    caller = phoneNumberGenerator.getRandomNumber(calltype,'caller')
    called = phoneNumberGenerator.getRandomNumber(calltype,'called')
    # Ensure caller and called numbers are different for realism
    while caller == called:
        called = phoneNumberGenerator.getRandomNumber(calltype,'called') 
    start_time = fake.date_time_between_dates(datetime_start=config['start_time']['start'], 
                                              datetime_end=config['start_time']['end'])

    cdr =  CallRecord()                                      
    cdr.caller = caller
    cdr.called = called
    cdr.duration_seconds = duration
    cdr.start_time = start_time
    cdr.end_time = start_time + timedelta(seconds=duration)
    cdr.balance_change = fake.pydecimal(right_digits=config['balance_change']['right_digits'], 
                                    min_value=config['balance_change']['min_value'], 
                                    max_value=config['balance_change']['max_value'], 
                                    positive=config['balance_change']['positive'])
    cdr.cdr_type = config['cdr_type']
    cdr.total_currency_charge = random.randint(config['total_currency_charge']['min'], 
                                            config['total_currency_charge']['max'])
    cdr.total_non_currency_charge =  random.randint(config['total_non_currency_charge']['min'], 
                                                config['total_non_currency_charge']['max'])
    cdr.cos_id =  random.choice(config['cos_id'])
    cdr.application_subtype = random.choice(config['application_subtype'])
    cdr.activity_direction  = random.choice(config['activity_direction'])
    cdr.discount_id = random.choice(config['discount_id'])
    cdr.cell_id =  random.choice(config['cell_id'])
    cdr_call_type = random.choice(config['cdr_call_type'])
    cdr.ocn_caller_id = random.choice(config['ocn_caller_id'])
    cdr.ocn_called_id = random.choice(config['ocn_called_id'])
    return   cdr.to_dict()
