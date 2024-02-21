#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RELCON PV Battery Sizing Simulation
Created on Tue Jan 15 10:31:22 2019

@author: maximus byamukama
"""
import math

class Load:
     def __init__(self, rating, usage,number):
         self.power = rating
         self.usage = usage
         self.number = number
         
class Home:  
    def __init__(self):
        self.loads=[]
        
    def get_energy(self):
        self.energy=0
        self.power=0
        for load in self.loads:
            self.energy += load.power * load.usage * load.number
            self.power += load.power * load.number
        return self.energy

class System:
    def __init__(self):
        self.homes=[]
        self.required_energy=0
        self.peak_power=0
        self.nom_pv_size=0    
    def get_pv_size(self):
        for home in self.homes:
            self.required_energy +=home.get_energy() 
            self.peak_power += home.power
            
        return (self.required_energy*1.2/6.0) # 6 peak sunshine hours per day, assume 20% fudge factor
            
home1 = Home()  #use case 1 - standard home
home1.loads.append(Load(7,24,1)) # 4 5W LED bulbs used 7 hrs a day


system = System()
count = 0;
while count < 1:
    system.homes.append(home1)  # 7 standard homes


req_pv_size = system.get_pv_size();
required_batt_size = system.required_energy/12.0; #Required battery capacity

print("Required PV Size:\t\t", round(req_pv_size),"W (Nominal Insolation)")
print("Total Energy Demand:\t\t" ,round(system.required_energy), "Wh per day")
print("Peak Demand:\t\t\t", system.peak_power, "W")
print("Req. Batt. Capacity:\t\t",required_batt_size,"Ah (12V)")

#calculate installation dimensions

#Jinko Eagle 72, 330Wp panel : 1956×992mm, Yangtze Solar 12V,250Ah battery : 520x269x225mm 
sys_module_batt_ratings = [330, 250]

required_panels = math.ceil(req_pv_size/sys_module_batt_ratings[0])
required_area = round(required_panels * 1.956 * 0.992)
required_batts = math.ceil(required_batt_size/sys_module_batt_ratings[1]) #number of batteries
required_batt_area=round(required_batts * 0.52 * 0.269)

print("Req. No. of Panels:\t\t", required_panels,"(" , required_area, "sq. mtrs)")
print("Req. No. of Batteries:\t\t", required_batts, "(" , required_batt_area, "sq. mtrs - central storage)")
print("Req. Batt. Capacity(per home):\t", round(required_batt_size/len(system.homes)),"Ah - distributed storage")
    
    
    
    
    
    
    
    
    
    
    
    