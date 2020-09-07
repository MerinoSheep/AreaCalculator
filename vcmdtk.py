def test_int(actn_code, entry_input) -> bool:  #'%d', '%S',
    if actn_code == '1':
        if not entry_input.isdigit():
            return False
    return True

def test_float(actn_code, entry_input, entry_string): #'%d', '%S', '%s'
    if test_int(actn_code, entry_input): # if its a number keep it
        return True
    elif actn_code == '1' and entry_input in {'-', '.'} and entry_input in entry_string:
        return False
    return True





if __name__ == "__main__":
    pass