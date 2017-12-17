#https://www.youtube.com/watch?v=NIWwJbo-9_8
try: 
  f = open('file.txt')
  #Custom exception 
  if f.name == 'currput_file.txt':
    raise Exception # will be catched by Exception 
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print('error')
else: # only runs when no exception is thrown
  print(f.read())
  f.close()
finally: # will always execute 
  print('Executing Finally ....') 



