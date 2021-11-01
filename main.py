
import csv
import pandas as pd
import time
import psutil,os

start = time.time()

#converting csv to dictionary
dict_from_csv = pd.read_csv("french_dictionary.csv",header=None, index_col=0, squeeze=True).to_dict()

#opening the text file
text = open("t8.shakespeare.txt")
text = text.read()


#replacing the english words with french words
with open('frequency.csv','w') as f:
  writer=csv.writer(f)
  for key in dict_from_csv:
      text.count(key)
      print(key,dict_from_csv[key],text.count(key))
      writer.writerow((key,dict_from_csv[key],text.count(key)))
      text = text.replace(key,dict_from_csv[key])
  
    

#writing the text file with  replaced french words
with open("t8.shakespeare.translated.txt","w") as file:
    file.write(text)

#finding unique list of words replaced with French words from the dictionary
lists = []
for val in dict_from_csv.values(): 
  if val in lists: 
    continue 
  else:
    lists.append(val)
print ("Unique list of words replaced with French words from the dictionary\n",
"********************************************************************\n",(lists))



f=open('performance.txt','w')

#printing the time taken to process
end = time.time()
#print("Time to process is :\n"
 #"***************************",end - start)
buff=end-start
f.write('Time to processs:'+str(buff)+'seconds')

# Printing memory taken to process
pid = os.getpid()
ps = psutil.Process(pid)
memoryuse = ps.memory_info()
#print("Memory used:\n"
#"*************************",memoryuse.vms/1024)
f.write('\nMemory used:'+str(memoryuse.vms/(1024*1024))+' MB')
f.close()




   




