def is_valid_phone_number(phone_number):
    if phone_number.count('-')!=2:
        return False
    phone_number_array=phone_number.split('-')
    if len(phone_number_array)!=3:
        return False
    if len(phone_number_array[0])!=3 or len(phone_number_array[1])!=3 or len(phone_number_array[2])!=4:
        return False
    if phone_number_array[0].isdigit()==False or phone_number_array[1].isdigit()==False or phone_number_array[2].isdigit()==False:
        return False
    else:
        return True