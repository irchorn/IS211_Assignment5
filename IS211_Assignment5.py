#!/usr/bin/env python
# coding: utf-8

# In[77]:


class Server: 
    def __init__(self, ppm): 
        self.page_rate = ppm 
        self.current_task = None 
        self.time_remaining = 0
    def tick(self): 
        if self.current_task != None: 
            self.time_remaining = self.time_remaining - 1 
            if self.time_remaining <= 0: 
                self.current_task = None
    def busy(self): 
        if self.current_task != None: 
            return True 
        else: 
            return False
    def start_next(self,new_task): 
        self.current_task = new_task 
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


# In[78]:


class Request: 
    def __init__(self, time): 
        self.timestamp = time 
        self.pages = range(1, 21)
    def get_stamp(self): 
        return self.timestamp
    def get_pages(self): 
        return self.pages
    def wait_time(self, current_time): 
        return current_time - self.timestamp


# In[79]:


def downloadData(url):
    """Downloads the data"""
    
    return url


# In[80]:


def main(url):
    print(f"Running main with URL = {'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'}...")


# In[81]:


import urllib.request

with urllib.request.urlopen('http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv') as response:
    html = response.read()


# In[82]:


print(html.decode('utf-8'))


# In[83]:


def simulation(num_seconds, pages_per_minute):
    simulation_server = Server(pages_per_minute) 
    server_queue= Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if (not simulation_server.busy()) and (not server_queue.is_empty()): 
            next_task = server_queue.dequeue() 
            waiting_times.append(next_task.wait_time(current_second)) 
            simulation_server.start_next(next_task)
            simulation_server.tick()
            average_wait = sum(waiting_times) / len(waiting_times) 
            print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, server_queue.size()))
           
    
    
   


# In[93]:


average_wait =0
server_queue = []
total_wait = 0
def simulateOneServer(file_name):
    with open(file_name, 'r') as f:
        lines = f.readLines()
    for line in lines:
        values = line.split()
        request = Request(int(values[2]))
        server_queue.append(request)
        total_wait += values[2]
    average_wait = total_wait / len(server_queue)    
    return average_wait
print('Average wait time', average_wait)


# In[94]:


def simulateManyServers(file_name, num_Server):
       return average_wait
print('Average wait time',average_wait)    
   
      
       
   


# In[87]:


import sys
    
    
if __name__ == "__main__":
    import argparse
    import queue
    
  
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    opts = [opt for opt in sys.argv[1:] if opt.startswith('--')]
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
    if '--servers' in opts:
        simulateManyServers(args[0], args[1])
    else:
        simulateOneServer(args[0])


# In[ ]:





# In[ ]:




