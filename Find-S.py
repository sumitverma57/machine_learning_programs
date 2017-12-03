from pandas import DataFrame
import pandas as pd
import numpy as np

class FindS:
    def __init__(self):
        self.ar=[]
        self.h0=['$','$','$','$','$','$']
        self.df=pd.read_csv('training_examples.csv')
        self.flag=[]
    def testcases(self,m):    #for grnerating random test cases
        attributes=np.array([self.df.Sky.unique(),self.df.AirTemp.unique(),self.df.Humidity.unique(),
        self.df.Wind.unique(),self.df.Water.unique(),self.df.Forecast.unique()])
        lst=[]
        for i in range(m):
            for item in attributes:
                lst.append(np.random.choice(item))
        self.ar=[lst[i:i+6] for i  in range(0, len(lst), 6)]
        self.testing_enjoy(m)
        for i in range(m):
            print(self.ar[i],self.flag[i])

    def testing_enjoy(self,m):      #for classifying the test cases
        for i in range(m):
            if(self.ar[i][0]=='Rainy' or self.ar[i][1]=='Cold'):
                self.flag.append('No')
            else:
                self.flag.append('Yes')

    def logic_S(self):
        positive_examples=self.df[self.df['EnjoySport']=='Yes']#taking only the positive example
        print(positive_examples)
        for j in range(positive_examples.shape[0]):
            xj=positive_examples.iloc[j,1:]#taking each row at a time
            if(self.h0[0]==self.h0[1]==self.h0[2]==self.h0[3]==self.h0[4]==self.h0[5]=='$'):
                self.h0[0]=xj['Sky']
                self.h0[1]=xj['AirTemp']
                self.h0[2]=xj['Humidity']
                self.h0[3]=xj['Wind']
                self.h0[4]=xj['Water']
                self.h0[5]=xj['Forecast']
            for j in range(len(self.h0)):
                if(self.h0[j]!=xj.iloc[j]):
                    self.h0[j]='?'     #the final hypo after findS algo is stored in h0
if __name__ == '__main__':
    s=FindS()
    s.logic_S()
    print(s.h0)
    s.testcases(10)
