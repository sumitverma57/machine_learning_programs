T_rain=0.2
F_rain=0.8
rain_prob=[T_rain,F_rain]
T_hose=[0.01,0.4]
F_hose=[0.99,0.6]
rain=['true','false']
hose={rain[0]:[T_hose[0],F_hose[0]],rain[1]:[T_hose[1],F_hose[1]]}
T_yard=[0.0,0.8,0.9,0.99]
F_yard=[1.0,0.2,0.1,0.01]
hose_rain=['false,false','false,true','true,false','true,true']
yard={hose_rain[0]:[T_yard[0],F_yard[0]],hose_rain[1]:[T_yard[1],F_yard[1]],
hose_rain[2]:[T_yard[2],F_yard[2]],hose_rain[3]:[T_yard[3],F_yard[3]]}

#finding if yard is wet,probability that it rained
#      Yard,Hose,Rain
test=['True,True,True',
      'True,False,True',
      'True,True,False',
      'True,False,False']
prob_test={test[0]:(yard[hose_rain[3]][0]*hose[rain[0]][0]*rain_prob[0]),
           test[1]:(yard[hose_rain[1]][0]*hose[rain[0]][1]*rain_prob[0]),
           test[2]:(yard[hose_rain[2]][0]*hose[rain[1]][0]*rain_prob[1]),
           test[3]:(yard[hose_rain[0]][0]*hose[rain[1]][1]*rain_prob[1])}
req_prob=(prob_test[test[0]]+prob_test[test[1]])/(prob_test[test[0]]+prob_test[test[1]]+prob_test[test[2]]+prob_test[test[3]])
print "The required probability is",req_prob
