# Author: Preet Dabhi
# Purpose : dabhi.py is used to process graph data
# To run from terminal window:   python3 dabhi.py 

#importing  csv and networkx and time
import csv 
import networkx as nx
import time 

def solution():
    # program start time
    print("Program Start time: " + time.ctime())
    #initalizing networkx 
    start_time = time.time()
    
    g=nx.Graph()
    trust=0
    distrust=0
    no_of_traingles=0
    traids=[]

    no_of_TTT=0
    no_of_TTD=0
    no_of_TDD=0
    no_of_DDD=0

    fileinput = input("Please enter the file name:")
    with open(fileinput, "r") as input_file:
        # reading the CSV file
        csvFile = csv.reader(input_file)
        # iterating through all the lines in the CSV files
        for lines in csvFile:
            #initalizing networkx 
            g.add_edge(lines[0],lines[1],weight=lines[2])
            #checking for trust values
            if(lines[2]=='1'):
                trust+=1
            if(lines[2]=='-1'):
                distrust+=1
            # iterating through all the traids in network 
        for traid in nx.enumerate_all_cliques(g):
            if len(traid) ==3:
                no_of_traingles+=1
                traids.append(traid)
        # iterating thorugh each of the sigle traids in the array for calculating the trust values
        for traid in traids:
            edgeOne = g[traid[0]][traid[1]]['weight']
            edgeTwo = g[traid[0]][traid[2]]['weight']
            edgeThree = g[traid[1]][traid[2]]['weight']
            sum_of_edges = int(edgeOne) + int(edgeTwo) + int(edgeThree)
            # calcalating numbers of actual traids
            if(sum_of_edges==1):
                no_of_TTD+=1
            if(sum_of_edges==-1):
                no_of_TDD+=1
            if(sum_of_edges==3):
                no_of_TTT+=1
            if(sum_of_edges==-3):
                no_of_DDD+=1
    # calculating trust probability
    trust_prob=round((int(trust)/(int(trust)+int(distrust)))*100, 2)
    distrust_prob=round((int(distrust)/(int(trust)+int(distrust)))*100, 2)

    prob = int(trust)/(int(trust)+int(distrust))
    negateprob=1-prob
    # caculating expected percentage of traids
    ex_percent_of_TTT=round(prob*prob*prob*100,2)
    ex_percent_of_TTD=round(3*(prob*prob*negateprob)*100,2)
    ex_percent_of_TDD=round(3*(prob*negateprob*negateprob)*100,2)
    ex_percent_of_DDD=round(negateprob*negateprob*negateprob*100,2)
    # calculating expected total percentage
    ex_total_no_of_percent =round(ex_percent_of_TTT+ex_percent_of_TTD+ex_percent_of_TDD+ex_percent_of_DDD,2)

    # calcualting expected number of traids
    ex_no_of_TTT=round(ex_percent_of_TTT*no_of_traingles*0.01,2)
    ex_no_of_TTD=round(ex_percent_of_TTD*no_of_traingles*0.01,2)
    ex_no_of_TDD=round(ex_percent_of_TDD*no_of_traingles*0.01,2)
    ex_no_of_DDD=round(ex_percent_of_DDD*no_of_traingles*0.01,2)

    # calculating expected total number of traids
    ex_total_numbers=round(ex_no_of_TTT+ex_no_of_TTD+ex_no_of_TDD+ex_no_of_DDD,2)
    # calculating actual percetage of traids
    percent_of_TTT=round((int(no_of_TTT)/(int(no_of_TTT)+int(no_of_TTD)+int(no_of_TDD)+int(no_of_DDD)))*100, 2)
    percent_of_TTD=round((int(no_of_TTD)/(int(no_of_TTT)+int(no_of_TTD)+int(no_of_TDD)+int(no_of_DDD)))*100, 2)
    percent_of_TDD=round((int(no_of_TDD)/(int(no_of_TTT)+int(no_of_TTD)+int(no_of_TDD)+int(no_of_DDD)))*100, 2)
    percent_of_DDD=round((int(no_of_DDD)/(int(no_of_TTT)+int(no_of_TTD)+int(no_of_TDD)+int(no_of_DDD)))*100, 2)

    # printing all the values caculated
    print("***  START ***")
    print("RESULTS FOR FILE: " + fileinput)
    print("Triangles:"+str(no_of_traingles))
    print("TTT:"+str(no_of_TTT) + "         " + "Edges Used:"+str(trust+distrust))
    print("TTD:"+str(no_of_TTD) + "          " + "Trust Edges:"+str(trust) + "          " + "Probability %:"+ str(trust_prob))
    print("TDD:"+str(no_of_TDD) + "          " + "Distrust Edges:"+str(distrust) + "       " + "Probability %:"+ str(distrust_prob))
    print("DDD:"+str(no_of_DDD) + "          " + "Total Edges:"+str(trust+distrust) + "          " + "Total %:" + str(trust_prob+distrust_prob))
    print("\n")

    print("Expected Distribution                  "+ "             Actual Distribution")
    print("      " + "Percent"+ "      " + "Number"+ "                                 " + "Percent"+ "      " + "Number")
    print("TTT:  "+str(ex_percent_of_TTT) +"        "+str(ex_no_of_TTT)+ "                                TTT:  "+str(percent_of_TTT) +"          "+str(no_of_TTT))
    print("TTD:  "+str(ex_percent_of_TTD) +"        "+str(ex_no_of_TTD)+"                               TTD:  "+str(percent_of_TTD) +"          "+str(no_of_TTD))
    print("TDD:  "+str(ex_percent_of_TDD) +"        "+str(ex_no_of_TDD)+"                               TDD:  "+str(percent_of_TDD) +"          "+str(no_of_TDD))
    print("DDD:  "+str(ex_percent_of_DDD) +"        "+str(ex_no_of_DDD)+"                                DDD:  "+str(percent_of_DDD) +"            "+str(no_of_DDD))
    print("       ----" + "       ----"+"                                      ----" + "       ----")
    print("Total:"+str(ex_total_no_of_percent)+"        "+str(ex_total_numbers) + "                              Total:"+str(round(percent_of_TTT+percent_of_TTD+percent_of_TDD+percent_of_DDD))+"         "+str(no_of_TTT+no_of_TTD+no_of_TDD+no_of_DDD))
    print("\n")

    #print("Actual Distribution")
    #print("      " + "Percent"+ "      " + "Number")
    #print("TTT:  "+str(percent_of_TTT) +"          "+str(no_of_TTT))
    #print("TTD:  "+str(percent_of_TTD) +"          "+str(no_of_TTD))
    #print("TDD:  "+str(percent_of_TDD) +"          "+str(no_of_TDD))
    #print("DDD:  "+str(percent_of_DDD) +"            "+str(no_of_DDD))
    #print("       ----" + "        ----")
    #print("Total:"+str(percent_of_TTT+percent_of_TTD+percent_of_TDD+percent_of_DDD)+"         "+str(no_of_TTT+no_of_TTD+no_of_TDD+no_of_DDD))
    
    # program end time
    end_time= time.time()
    print("***  END ***")
    print("Program End time: " + time.ctime())
    program_run_time = end_time-start_time
    print("Total Program Run Time in Seconds : " + str(program_run_time))

solution()
