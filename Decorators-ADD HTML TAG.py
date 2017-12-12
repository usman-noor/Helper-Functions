def get_name(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)
  
def p_decorate(func):
  def func_wrapper(name):
    return "<p>{}</p>".format(func(name))
  return func_wrapper

get_name_tagged = p_decorate(get_name)  

print(get_name_tagged('john'))




  
  
