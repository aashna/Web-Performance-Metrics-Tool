import mechanize
import time
import urllib 


class Transaction3(object):
    def __init__(self,url):
        self.custom_timers = {}
        self.s = 0
        self.base_url = url
    
    def run(self):
        for num in range(0,20):
            br = mechanize.Browser()
            br.set_handle_robots(False)
            
            start_timer = time.time()
            resp = br.open(self.base_url)
            #resp.read()
            response_time = time.time() - start_timer
            self.custom_timers['All_Items'] = response_time
            print response_time
            print ("\n")
            self.s += response_time 
            assert (resp.code == 200), 'Bad HTTP Response'
            
           

if __name__ == '__main__':
    trans = Transaction3(' ')
    trans.run
    print 600/trans.s
    #print trans.custom_timers 
