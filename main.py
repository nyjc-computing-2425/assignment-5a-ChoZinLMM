def to_hms(seconds):
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    
    if not isinstance(seconds, int):
      print("Unsupported input type.") 
    elif seconds <= 0:
      print("Unsupported input type.")
    else :
      min, sec = divmod(seconds, 60)
      hours, min = divmod(min, 60)
      hms = [hours, min, sec]
      return hms


  
  


      
  
    

