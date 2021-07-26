import os
import psutil

# print(psutil.virtual_memory())  # physical memory usage
#print('memory % used:', psutil.virtual_memory())
print ("CPU Usage", psutil.cpu_percent(interval=1), "%")

print ("CPU Count", psutil.cpu_count())

#print ("Net addres", psutil.net_if_addrs())

#print ("CPU Count", psutil.getloadavg())
#print  (psutil.disk_usage('/'))  #all
print ("Disk Space Used", psutil.disk_usage(os.sep).percent, "%")



#print ("Disk Less space", diskless, "%")

#memory by PID
#pid = os.getpid()
#python_process = psutil.Process(pid)
#memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think
#print('memory use by python :', memoryUse,'GB')