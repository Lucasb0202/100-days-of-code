def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
      if year % 100 == 0 and year % 400 == 0:
        return True
      elif year % 100 == 0:
        return False
      else: return True
    else: return False

is_leap_year(2100)