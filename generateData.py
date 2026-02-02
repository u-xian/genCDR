import call_detail_records

def generate_cdrs_data(calltype,num_records):
    data_list = []
    for _ in range(num_records):
        data_list.append(call_detail_records.generate_cdr(calltype))
    return data_list