def decorator_function(original_function):
  def wrapper_function(*args, **kwargs):
    print("Wrapper executed before func {}".format(original_function.__name__))
    return original_function(*args, **kwargs)
  return wrapper_function

  
@decorator_function  
def display():
  print("Display function ran")
  
@decorator_function  
def display_info(name,age):
  print("Display {} , {}".format(name,age) )
  
decorated_display = decorator_function(display)
decorated_display()
    
display()


display_info('john',30)
