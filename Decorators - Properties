class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self._b = b
    
    @property
    def b(self):
      return self._b
      
    @b.setter
    def b(self,value):
      if value > 255:
        raise ValueError('Invalid Value')
      self._b = value
        
    
    
    @property
    def hex(self):
        rgb = [self.r, self.g, self.b]
        return '#{:02X}{:02X}{:02X}'.format(*rgb)
    
    @property    
    def rgb(self):  
      rgb = [self.r, self.g, self.b]
      return 'rgb({}, {}, {})'.format(*rgb)
        


c = Color(255, 255, 255)
print(c.hex)
print(c.rgb)

print('-------')

c.b = 40
print(c.hex)
print(c.rgb)


