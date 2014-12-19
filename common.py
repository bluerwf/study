
class TokenError(Exception):
    def __init__(self, nm):
        self.nm = nm
    def __str__(self):
        return "Error: nm: {0} is illegale".format(self.nm)

def save_dir(path,dic):
   with open(path,'w') as fh:
       for k in dic:
           fh.write(k+':'+dic[k]+'\n')


        


