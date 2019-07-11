#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:23:37 2019

@author: xiangshuyang
"""

from numpy import * 

class  simmeans: 
    def __init__(self,means):
        self.means=means
    
    def meanstype(self,A,B):
        if self.means=='Eclud':
            return 1/(1+linalg.norm(A-B))
        elif self.means=='Pears':
            if len(inA) < 3 :
                return 1.0
            else:
                return 0.5+0.5*corrcoef(A, B, rowvar = 0)[0][1]
        elif self.means=='Cos':
            num = float(A.T*B)
            denom = linalg.norm(A)*linalg.norm(B)
            return 0.5+0.5*(num/denom)
       
class recommendation:
    def __init__(self,data,means,N):
        self.data=data
        self.means=means
        self.N=N
        
    def EstRate(self,user,item): # how can we recommend the given item to the given user?
        m,n=shape(self.data)
        simlarity =0
        simTotal=0
        simRateTotal =0 
        for j in range(n):
            userrating= self.data[user,j] #scann all the rating of the user
            if userrating==0:
                continue # find the ones with zero rating 
            overlap =  nonzero(logical_and(self.data[:,item].A>0, \
                                      self.data[:,j].A>0))[0] 
            if len(overlap)==0:
                similarity=0
            else:
                similarity= means.meanstype(self.data[overlap,item],\
                                             self.data[overlap,j])
            simTotal+= similarity 
            simRateTotal+= similarity* userrating 
            if simTotal==0:
                return simTotal
            else: 
                return simRateTotal/simTotal
            
    def recom(self,user):
        itemscore=[]
        unrateitem= nonzero(data[user:,].A==0)[1] # items that the user did not rate
        if len(unrateitem) ==0:
            print('Every is rate!')
        for item in unrateitem:
            ratevalue= self.EstRate(user,item)
            itemscore.append((item,ratevalue))
        return sorted(itemscore,key=lambda jj: jj[1],reverse=True)[:self.N]
            
    
#####test#####
data= matrix([[1, 1, 1, 0, 0],
       [2, 2, 2, 0, 0],
       [1, 1, 1, 0, 0],
        [5, 5, 5, 0, 0],
        [1, 1, 0, 2, 2],
        [0, 0, 0, 3, 3],
         [0, 0, 0, 1, 1]])
            
               
means=simmeans('Cos')  
recm= recommendation(data,means,2)
user = 5 
recm.recom(user)     
print(recm.recom(user))    
        
        
