def start():
    tmp_str = """
    For contribution enter /contribute whereas for help enter /needhelp
    """
    return tmp_str

def contribute():
    # attach resource list below this.
    tmp_str = """
    Enter details in below given format:
    first-name
    email
    mobile no.
    city 
    state
    resources
    description ('') 

    Note: pls enter resources by the serial no's provided below 
    for mutliple resources enter them in space seprated form.
    e.g. 1 2 for plasma and Remdesvir..
    """
    return tmp_str

def need_help():
    return ''