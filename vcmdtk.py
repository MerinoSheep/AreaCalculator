def test_int(actn_code, entry_input) -> bool:  #'%d', '%S'
    if actn_code == '1':
        if entry_input.isdigit():
            return True
    return False

def test_float(actn_code, entry_input, entry_string): #'%d', '%S', '%s'
    if test_int(actn_code, entry_input): # if its a number keep it
        return True
    elif entry_input == '.' and entry_input not in entry_string:
        return True
    return False





if __name__ == "__main__":
    pass