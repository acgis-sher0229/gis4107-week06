def get_db_link(building_code):
    link_code=""
    link_code+=building_code[4]
    link_code+=building_code[5]
    link_code+="-"
    link_code+=building_code[10]
    link_code+=building_code[11]
    link_code+=building_code[12]    
    return link_code    