"""
    Study information: Control groups are people who go to primary care providers (PCPS) for treatment.
                        Intervention groups are people who attend the nine weeks program for treatment.
    
    Goal is to determine which group of patients are better off using their assigned treatment
    
    baseline: data collected before experiment
    9 weeks: data collected immediately after the end of the experiment
    21 weeks: data collected 12 weeks after the end of the experiment
    
    
    63.	painscale: On a scale from 0-10, where 0 is no pain at all and 10 is pain as bad as it could be, how would you rate your average level of pain during the past week?   
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import csv file into data
data = pd.read_csv("C:/Users/Mike Pham/Desktop/Summer Research 2020/alldata.csv");

#slicing the data

#print the first 5 rows of the data
print(data.head())

data.info() #tecnical summary

""""
    Notable columns:
    
    Pain Descrition
    
    psqi5i: Have you had pain for during past month, week? (2, 3, 4: baseline, 9, 21)
    Section: brief Pain inventory
    bpi3: Rate your pain over the last 24 hours (2, 3, 4: baseline, 9 , 21 weeks)
    bpi7: How much pain have been reliefed by the provides treatment or medication
    
    Social fucntional support + Psychological effects:
    (Functional Social Support Questionaire)

"""


def gaussian(x, mu, sig):
    return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)

kwargs = dict(alpha=0.5, bins=20)
x1 = data.loc[data.TreatmentName == 'Intervention', 'fssdiff1']
x2 = data.loc[data.TreatmentName == 'Control', 'fssdiff1']
plt.hist(x1, **kwargs, color = 'g', label = 'Intervention')
plt.hist(x2, **kwargs, color = 'r', label = 'Control')
plt.gca().set(title='Frequency Histogram of Change in Total Funcitonal Social supports of Patients', ylabel='Frequency')
plt.xlim(-5, 5);
plt.legend();
plt.show();

relieved_i09 = []; # list of indexes of patients whose average pain got better after the intervention treatment
worsen_i09 = []; # list of indexes of patients whose pain got worse after the intervention treatment
missing_i09 = []; # list of indexs of patients whose data on this measure is missing
c = 0;
for i in range(155):
    if (data.at[i, 'TreatmentName'] == 'Intervention'):
    # bpi5: Please rate your pain by circling the one number that best describes your pain on the average.
        baseline = data.at[i, 'bpi52'];
        week9 = data.at[i, 'bpi53'];
        print(baseline, " ", week9);
        if (baseline <= week9):
            worsen_i09.append(i);
        elif (baseline > week9):
            relieved_i09.append(i);
        else:
            missing_i09.append(i)

print(relieved_i09);
print(worsen_i09);
print(missing_i09);

x1 = [];
x2 = [];
x3 = [];
for i in relieved_i09:
    x1.append(data.loc[i, 'veg0'])
    x2.append(data.loc[i, 'veg9'])
    x3.append(data.loc[i, 'nutr4new4'] - data.loc[i, 'nutr4new2'])
print(x1)
print(x2)
#plt.hist(x1, color = 'b', bins = 20)
plt.hist(x3, bins = 6)
plt.gca().set(title='Frequency Histogram of Change in Vegetables serving', ylabel='Frequency')
plt.show();
