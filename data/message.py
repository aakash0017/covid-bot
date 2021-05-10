def start():
    tmp_str = """
    if want to contribute please type <b>/contribute</b> and if you are looking for resources please type <b>/needhelp</b>
    """
    return tmp_str

def contribute():
    # attach resource list below this.
    tmp_str = """
    Please enter resources by their serial numbers provided above for mutliple resources enter them in space seprated form.\n\n<i>E.g. <b>1 2 for plasma and Remdesvir.</b></i>
    
Enter details in given format:
your-nameyour-email
mobile no.
city 
state
resources-available
description
    """
    return tmp_str

def need_help():
    tmp_str = """
    Enter details in the following format using the serial number provided above. \nyou can only check for one resource at a time. \n\n<i>E.g. <b>1 in Delhi</b></i>
    """
    
    return tmp_str

def enter_correct_det():
    tmp_str = """
    Enter correct details and don't edit the message.
    """
    return tmp_str