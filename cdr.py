class CallRecord:
    def __init__(self):
        self.caller = ""
        self.called = ""
        self.duration_seconds = 0
        self.start_time = ""
        self.end_time = ""
        self.balance_change = 0
        self.cdr_type = 0
        self.total_currency_charge = 0
        self.total_non_currency_charge = 0
        self.cos_id = 0
        self.application_subtype = 0
        self.activity_direction = 0
        self.discount_id = 0
        self.cell_id = 0
        self.cdr_call_type = 0
        self.ocn_caller_id = 0
        self.ocn_called_id = 0
    
    # Method to return data as a dictionary
    def to_dict(self):
        return {
        "caller" : self.caller,
        "called" : self.called,
        "duration_seconds" : self.duration_seconds,
        "start_time" : self.start_time,
        "end_time" : self.end_time,
        "balance_change" : self.balance_change,
        "cdr_type" : self.cdr_type,
        "total_currency_charge" : self.total_currency_charge, 
        "total_non_currency_charge" : self.total_non_currency_charge,
        "cos_id" : self.cos_id,
        "application_subtype" : self.application_subtype,
        "activity_direction" : self.activity_direction, 
        "discount_id" : self.discount_id,
        "cell_id" : self.cell_id,
        "cdr_call_type" : self.cdr_call_type,
        "ocn_caller_id" : self.ocn_caller_id,
        "ocn_called_id" : self.ocn_called_id
        }