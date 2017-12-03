import pandas as pd
import numpy as np

class FindS:
    def __init__(self):
        self.ar=[]
        self.h0=['$','$','$','$','$','$']
        self.h1=['?','?','?','?','?','?']
        self.h2=['?','?','?','?','?','?']
        self.h3=['?','?','?','?','?','?']
        self.h4=['?','?','?','?','?','?']
        self.h5=['?','?','?','?','?','?']
        self.h6=['?','?','?','?','?','?']
        self.final=[]
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
        print("Positive examples")
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
                if(self.h0[j]!=xj[j]):
                    self.h0[j]='?'     #the final hypo after findS algo is stored in h0
        negative_examples=self.df[self.df['EnjoySport']=='No']
        print("Negative examples")
        print(negative_examples)
        for j in range(negative_examples.shape[0]):
            xj=negative_examples.iloc[j,1:]#taking each row at a time
            if(self.h1[0]==self.h1[1]==self.h1[2]==self.h1[3]==self.h1[4]==self.h1[5]=='?'):
                a=self.df.Sky.unique()
                g1=a[a!=xj['Sky']]
                if(g1):
                    self.h1[0]=g1[0]
                b=self.df.AirTemp.unique()
                g2=b[b!=xj['AirTemp']]
                if(g2):
                    self.h2[1]=g2[0]
                c=self.df.Humidity.unique()
                g3=c[c!=xj['Humidity']]
                if(g3):
                    self.h3[2]=g3[0]
                d=self.df.Wind.unique()
                g4=d[d!=xj['Wind']]
                if(g4):
                    self.h4[3]=g4[0]
                e=self.df.Water.unique()
                g5=e[e!=xj['Water']]
                if(g5):
                    self.h5[4]=g5[0]
                f=self.df.Forecast.unique()
                g6=f[f!=xj['Forecast']]
                if(g6):
                    self.h6[5]=g6[0]
        remove=[0]*6
        if(self.h0[0]!=self.h1[0]):
            remove[0]=1
        if(self.h0[1]!=self.h2[1]):
            remove[1]=2
        if(self.h0[2]!=self.h3[2]):
            remove[2]=3
        if(self.h0[3]!=self.h4[3]):
            remove[3]=4
        if(self.h0[4]!=self.h5[4]):
            remove[4]=5
        if(self.h0[5]!=self.h6[5]):
            remove[5]=6
        h=[self.h1,self.h2,self.h3,self.h4,self.h5,self.h6]
        for i in range(6):
            if remove[i]==0:
                self.final.append(h[i])


if __name__ == '__main__':
    s=FindS()
    s.logic_S()
    print("All general hypothesis are:")
    print(s.h1)
    print(s.h2)
    print(s.h3)
    print(s.h4)
    print(s.h5)
    print(s.h6)
    print("valid general hypothesis are:")
    print(s.final)
    print("specific hypothesis is:")
    print(s.h0)
    print("The test cases are as follows:")
    s.testcases(10)
