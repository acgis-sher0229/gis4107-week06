def has_x_code (in_text):
    if in_text.find("Tx6op3")>=0:
        return True
    else:
        return False
    
def get_x_code_position (in_text):
    return in_text.find("Tx6op3")  
