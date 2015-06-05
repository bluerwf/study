import os, pickle
import time


class Model:
    def __init__(self, title, date, qua):
        self.title = title
        self.date = date
        self.qua = qua
    
    def display(self):
        print self.title
        print self.date
        print self.qua

class Base(object):
    def __init__(self, id, ts):
        self.id = id
        self.ts = ts

    def read(self, fname, *arg, **karg):
        raise NotImplemented
    
    def write(self, fname, content, *arg, **karg):
        raise NotImplemented

    def detele(self, fname, *arg, **karg):
        os.remove(fname) 

class Spice(Base):
    
    def __init__(self, id, ts, author):
        super(Spice, self).__init__(id, ts)
        self.author = author

    def read(self, fname, *arg, **karg):
        data = None
        try:
            with open(fname, 'rb') as f:
                data = f.read()
            if data:
                model  = pickle.loads(data)
                return model
        except Exception as e:
            print e


    def write(self, fname, content, *arg, **karg):
        content = pickle.dumps(content, 1)
        try:
            with open(fname, 'wb') as f:
                f.write(content)
        except Exception as e:
            print e
    
    def read1(self, fname, *arg, **karg):
        data = None
        try:
            with open(fname, 'rb') as f:
                f.seek(len('I am writing\n'))
                data = f.read()
            data = pickle.loads(data)
            return data
        except Exception as e:
            print e

    def write1(self, fname, content, *arg, **karg):
        s = 'I am writing\n'
        content = pickle.dumps(content, 1)
        try:
            with open(fname, 'ab') as f:
                f.write(s)
                f.write(content)
        except Exception as e:
            print e

if __name__ == '__main__':
    m = Model('test', time.asctime(), 1)
    s = Spice(1, time.time(), 'ann')

    s.write1('test.db', m)
    m2 = s.read1('test.db')
    m2.display()
