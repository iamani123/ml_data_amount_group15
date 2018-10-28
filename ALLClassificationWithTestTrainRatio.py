import numpy as np
import datetime
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
X=np.genfromtxt('DataSetLetter.csv', delimiter = ',',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
y=np.genfromtxt('DataSetLetter.csv', delimiter = ',', dtype='str',usecols=(0))
acc =np.zeros((6,9))
n=0
for i in range(1,10):
    acc[0,n]=(i/10)*100
    X_train, X_test, y_train,y_test  = train_test_split(X,y,test_size=(1-i/10), random_state=0)
    classifier=KNeighborsClassifier(n_neighbors=3,metric='minkowski',p=2)
    #classifier=LogisticRegression(random_state=0)
    classifier.fit(X_train,y_train)
    y_pred=classifier.predict(X_test)
    score=0
    
    for j in range(len(y_test)):
        if(y_test[j]==y_pred[j]):
            score=score+1
    #print(score,"/",len(y_test))
    result=(score/len(y_test))*100       
    print("train_size ",(i/10)*100," ",result)
    acc[1,n]=result;
    
    #classifier=KNeighborsClassifier(n_neighbors=3,metric='minkowski',p=2)
    classifier1=LogisticRegression(random_state=0)
    classifier1.fit(X_train,y_train)
    y_pred=classifier1.predict(X_test)
    score=0
    
    for j in range(len(y_test)):
        if(y_test[j]==y_pred[j]):
            score=score+1
    #print(score,"/",len(y_test))
    result=(score/len(y_test))*100       
    print("train_size ",(i/10)*100," ",result)
    acc[2,n]=result;
    
    classifier2 = RandomForestClassifier()
    classifier2.fit(X_train,y_train)
    y_pred=classifier2.predict(X_test)
    score=0
    
    for j in range(len(y_test)):
        if(y_test[j]==y_pred[j]):
            score=score+1
    #print(score,"/",len(y_test))
    result=(score/len(y_test))*100       
    print("train_size ",(i/10)*100," ",result)
    acc[3,n]=result;
  
    classifier3  = tree.DecisionTreeClassifier()
    classifier3.fit(X_train,y_train)
    y_pred=classifier3.predict(X_test)
    score=0
    
    for j in range(len(y_test)):
        if(y_test[j]==y_pred[j]):
            score=score+1
    #print(score,"/",len(y_test))
    result=(score/len(y_test))*100       
    print("train_size ",(i/10)*100," ",result)
    acc[4,n]=result;
    
    clf=SVC(gamma='auto')
    classifier4  =  SVC(kernel='rbf')
    classifier4.fit(X_train,y_train)
    y_pred=classifier4.predict(X_test)
    score=0
    
    for j in range(len(y_test)):
        if(y_test[j]==y_pred[j]):
            score=score+1
    #print(score,"/",len(y_test))
    result=(score/len(y_test))*100       
    print("train_size ",(i/10)*100," ",result)
    acc[5,n]=result;
    
    n=n+1
fig, ax = plt.subplots(figsize=(12, 8))
#ax.bar(index, avgCost)
plt.xlim(0, 100)
ax.plot(acc[0,:], acc[1,:], 'r', label='KNN')
ax.plot(acc[0,:], acc[2,:], 'b', label='LOGISTIC')
ax.plot(acc[0,:], acc[3,:], 'y', label='DecisionTree')
ax.plot(acc[0,:], acc[4,:], 'g', label='RandomForest')
ax.plot(acc[0,:], acc[5,:], 'm', label='SVM')
#plt.xticks(index, cost[0,:], fontsize=5, rotation=30)
ax.set_xlabel('Ratio Of Data Training size')
ax.set_ylabel('Accuracy')
ax.legend(loc=2)
fig.savefig('AccForKNNAlgoForRatioOfData.png')