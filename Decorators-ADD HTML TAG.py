#Version 1
def get_name(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)
  
def p_decorate(func):
  def func_wrapper(name):
    return "<p>{}</p>".format(func(name))
  return func_wrapper

get_name_tagged = p_decorate(get_name)  

#calling func applies parameter to inner func wrapper final output comes from func wrapper
print(get_name_tagged('john'))


#Version 2
def p_decorate(func):
  def func_wrapper(name):
    return "<p>{}</p>".format(func(name))
  return func_wrapper

@p_decorate
def get_name(name):
  return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_name('john'))


  
  
