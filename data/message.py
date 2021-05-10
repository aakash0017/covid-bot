def start():
    tmp_str = """
    if want to contribute please type /contribute and if you are 
    looking for resources please type /needhelp
    """
    return tmp_str

def contribute():
    # attach resource list below this.
    tmp_str = """
    please enter resources by their serial numbers provided above 
    for mutliple resources enter them in space seprated form.
    E.g. 1 2 for plasma and Remdesvir..
    
    Enter details in given format:
    <b>your-name
    your-email
    mobile no.
    city 
    state
    resources-available
    description</b>
    """
    return tmp_str

def need_help():
    tmp_str = """
    Enter details in the following format using the serial number provided above.
    you can only check for one resource at a time. \nE.g. *1 in Delhi*
    """
    tmp_str = """
    Enter details in below given format:\nResource in City or state\nNote: pls enter resource by their serial no's provided below.
    """
    return tmp_str

def enter_correct_det():
    tmp_str = """
    Enter correct details and don't edit the message.
    """
    return tmp_str