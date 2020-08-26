import os                  
import sys
import shutil               #remove dir
import errno

           
                                                   # 28 hpcs, 1-4 hpcs per txt file -> 12 files
exe = " ./out" 
fileout = "out"
fileout1 = fileout + "1.txt"                        #now have output file name stored ex. a.py -> a1.txt
fileout2 = fileout + "2.txt"                        #now have output file name stored ex. a.py -> a2.txt
fileout3 = fileout + "3.txt"                        #now have output file name stored ex. a.py -> a3.txt
fileout4 = fileout + "4.txt"                        #now have output file name stored ex. a.py -> a4.txt
fileout5 = fileout + "5.txt"                        #now have output file name stored ex. a.py -> a5.txt
fileout6 = fileout + "6.txt"                        #now have output file name stored ex. a.py -> a6.txt
fileout7 = fileout + "7.txt"                        #now have output file name stored ex. a.py -> a7.txt
fileout8 = fileout + "8.txt"                        #.....
fileout9 = fileout + "9.txt" 
fileout10 = fileout + "10.txt" 
fileout11 = fileout + "11.txt" 
fileout12 = fileout + "12.txt"         
     
                                                   # load the strings to be passed as an argument for running perf 
                                                   # string is loaded with terminal command and correct parameters like what instruction to look at
                                                   # and what file should be ran
                                                   # exe can be changed depending on what file you're running
                                                   # collecting every 1ms running on 1 core and appending to file
	                     

temp  = " sudo perf stat -C 0 -A -I 1 -o " + fileout1 + " --append -e branch-instructions,branch-misses,bus-cycles,cache-misses " + exe  
temp1 = " sudo perf stat -C 0 -A -I 1 -o " + fileout2 + " --append -e cache-references,cpu-cycles,instructions,ref-cycles "  + exe
temp2 = " sudo perf stat -C 0 -A -I 1 -o " + fileout3 + " --append -e L1-dcache-load-misses,L1-dcache-loads " +  exe 
temp3 = " sudo perf stat -C 0 -A -I 1 -o " + fileout4 + " --append -e L1-dcache-stores,L1-icache-load-misses " +  exe
temp4 = " sudo perf stat -C 0 -A -I 1 -o " + fileout5 + " --append -e LLC-load-misses,LLC-loads "  + exe
temp5 = " sudo perf stat -C 0 -A -I 1 -o " + fileout6 + " --append -e LLC-store-misses,LLC-stores "  + exe
temp6 = " sudo perf stat -C 0 -A -I 1 -o " + fileout7 + " --append -e branch-load-misses,branch-loads,dTLB-load-misses "  + exe  
temp7 = " sudo perf stat -C 0 -A -I 1 -o " + fileout8 + " --append -e dTLB-loads "  + exe  
temp8 = " sudo perf stat -C 0 -A -I 1 -o " + fileout9 + " --append -e dTLB-store-misses,dTLB-stores "  + exe  
temp9 = " sudo perf stat -C 0 -A -I 1 -o " + fileout10 + " --append -e iTLB-load-misses,iTLB-loads "  + exe
temp10 = " sudo perf stat -C 0 -A -I 1 -o " + fileout11 + " --append -e node-load-misses,node-loads "  + exe  
temp11 = " sudo perf stat -C 0 -A -I 1 -o " + fileout12 + " --append -e node-store-misses,node-stores "  + exe   


    
    
                                                     # If program is quick, you might only get a few HPCs = LOOP it
					             # Loop the perf command (end - start) times depending on how many HPCs you want
									
end = 20
start = 1
while((end - start) != 0):
	os.system(temp)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp1)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp2)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp3)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp4)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp5)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp6)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp7)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp8)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp9)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp10)  
	start = start + 1
start = 1
while((end - start) != 0):
	os.system(temp11)  
	start = start + 1

os.system("mkdir " + fileout + "folder")                                              # Move all files into one folder
os.system("mv " + fileout1 + " " + fileout + "folder")
os.system("mv " + fileout2 + " " + fileout + "folder")
os.system("mv " + fileout3 + " " + fileout + "folder")
os.system("mv " + fileout4 + " " + fileout + "folder")
os.system("mv " + fileout5 + " " + fileout + "folder")
os.system("mv " + fileout6 + " " + fileout + "folder")
os.system("mv " + fileout7 + " " + fileout + "folder")
os.system("mv " + fileout8 + " " + fileout + "folder")
os.system("mv " + fileout9 + " " + fileout + "folder")
os.system("mv " + fileout10 + " " + fileout + "folder")
os.system("mv " + fileout11 + " " + fileout + "folder")
os.system("mv " + fileout12 + " " + fileout + "folder")






