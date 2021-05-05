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

    Note: pls enter resources by their serial no's provided below 
    for mutliple resources enter them in space seprated form.
    e.g. 1 2 for plasma and Remdesvir..
    """
    return tmp_str

def need_help():
    tmp_str = """
    Enter details in below given format:\nResource in City or state\nNote: pls enter resource by their serial no's provided below.
    """
    return tmp_str