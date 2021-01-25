# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:09:50 2020

@author: hp
"""

import pandas as pd  # import pandas module for processing csv file
import wx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotPanel(wx.Panel):
    def __init__(self, parent,xsize,ysize):
        wx.Panel.__init__(self,parent,-1,size=(xsize,ysize))
        self.figure=Figure()
        self.canvas=FigureCanvas(self,-1,self.figure)
        self.axes=self.figure.add_subplot(111)
    
    def plot(self,x,y):
        self.axes.clear()
        self.axes.plot(x,y)
        
    
class DataSet(wx.Frame):    # Wx framework is used so as to specify details of the frame
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title, size=(1000,1000)) #x-axis and y-axis
        self.initialize()   # all gui related implementation methods like buttons are in the initialize method

    def initialize(self):   # to show various elements on the panel that will hold all gui objects
        pannel=wx.Panel(self)  # Assigning the variable to panel
        
        # answer
        rows=wx.BoxSizer(wx.VERTICAL)   # handles visual arrangement and calculates appropriate size for each element automatically
        self.ansText= wx.StaticText(pannel,label='Data set')   # A user cant change the answer so a static text is created
        rows.Add(self.ansText, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)   # Add the panel to the boxsizer by aligning it to the center
        
        # input text
        numsize=wx.BoxSizer(wx.HORIZONTAL)
        self.inp1=wx.StaticText(pannel,label='Start Year',pos=(250,450))
        self.inp1=wx.TextCtrl(pannel)  #User enters value and that vaue can be used for gnrating answers
        self.inp2=wx.StaticText(pannel,label='Ending Year',pos=(375,451)) 
        self.inp2 = wx.TextCtrl (pannel)
        self.inp3=wx.StaticText(pannel,label='KeyWord',pos=(490,452))
        self.inp3= wx.TextCtrl (pannel)
        self.inp4=wx.StaticText(pannel,label='Description',pos=(630,452))
        self.inp4= wx.TextCtrl (pannel)
        self.inp5=wx.StaticText(pannel,label='Legislation',pos=(730,453))
        self.inp5= wx.TextCtrl (pannel)
        numsize.Add(self.inp1, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        numsize.Add (self.inp2, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        numsize.Add (self.inp3, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        numsize.Add (self.inp4, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        numsize.Add (self.inp5, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        rows.Add(numsize, 2, wx.ALIGN_CENTER)
        
        #buttons
        butSize=wx.BoxSizer(wx.HORIZONTAL)  # Place the buttons in a single row
        find1Button=wx.Button(pannel, label="Penalty Report")
        find2Button=wx.Button(pannel, label="Offence Chart")
        find3Button=wx.Button(pannel, label="Camera or Radar Detected")
        find4Button=wx.Button(pannel, label="Mobile Phone Usage Chart")
        find5Button=wx.Button(pannel, label="Legislation Report")
        ClrButton=wx.Button(pannel, label="Clear")
        butSize.Add(find1Button, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)  # In order to use button object properly Add method is used which will add the button object to the Box sizer
        butSize.Add(find2Button, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        butSize.Add(find3Button, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        butSize.Add(find4Button, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        butSize.Add(find5Button, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        butSize.Add(ClrButton, 1, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        rows.Add(butSize, 1, wx.ALIGN_CENTER)
        
        # self.dataplot=PlotPanel(self,400,350)
        # self.dataplot.plot([x_year],[y_cases])
        # numsize.Add(self.dataplot,1,wx.EXPAND)
        
        # self.dataplot=PlotPanel(self,400,350)
        # self.dataplot.plot([0,1,2],[1,2,3])
        # rows.Add(self.dataplot,1,wx.EXPAND)
        
       
        
        self.Bind(wx.EVT_BUTTON, self.onFind1, find1Button)  # For binding the buttons to the frame object Bind method is used. It will also take appropriate action when the button is pressed
        self.Bind(wx.EVT_BUTTON, self.onFind2, find2Button)
        self.Bind(wx.EVT_BUTTON, self.onFind3, find3Button)
        self.Bind(wx.EVT_BUTTON, self.onFind4, find4Button)
        self.Bind(wx.EVT_BUTTON, self.onFind5, find5Button)
        self.Bind(wx.EVT_BUTTON, self.onclear, ClrButton)
        
        pannel.SetSizerAndFit(rows)
        self.Show(True)  # to show the above methods on a popup window
    
    def onclear(self,event):  # Clear button that will clear the user entered values
        self.inp1.Value=""
        self.inp2.Value=""
        self.inp3.Value=""
        self.inp4.Value=""
        self.inp5.Value=""
           
    def onFind1(self,event): # functionaly 1 button that will generate all the information of penalty cases
        try:
            # import csv file in read mode into variable 'data'
            # 'low memory=False' to let pandas acceess more memory and not be restricted while reading different datatypes for csv file columns
            data = pd.read_csv (r'penalty_set.csv', low_memory=False)
            # import 'data' into DataFrame and select columns to access and placed in variable 'df'
            df = pd.DataFrame(data, columns= ['OFFENCE_FINYEAR', 'OFFENCE_MONTH', 
                                  'OFFENCE_CODE', 'OFFENCE_DESC', 'LEGISLATION', 'SECTION_CLAUSE', 'FACE_VALUE', 'CAMERA_IND', 
                                  'CAMERA_TYPE', 'LOCATION_CODE', 'LOCATION_DETAILS', 'SCHOOL_ZONE_IND', 'SPEED_BAND', 'SPEED_IND', 
                                  'POINT_TO_POINT_IND', 'RED_LIGHT_CAMERA_IND', 'SPEED_CAMERA_IND', 'SEATBELT_IND', 'MOBILE_PHONE_IND', 
                                  'PARKING_IND', 'CINS_IND', 'FOOD_IND', 'BICYCLE_TOY_ETC_IND', 'TOTAL_NUMBER', 'TOTAL_VALUE'])
            # user input
            i1=int(self.inp1.Value)
            i2=int(self.inp2.Value)
            
            # variable for looping through 'OFFENCE_FINYEAR' string
            start = i1
            end = i1 + 1
            
            # loop for single year
            if i2 == (i1 + 1):
                # filter column 'OFFENCE_FINYEAR' based on input value
                # string filter method and string is matched exactly
                af = df[df['OFFENCE_FINYEAR'].str.match(str(i1)+'-'+str(i2))]
             
             # loop for multiple years   
            elif i2 > (i1 + 1):
                # loops with 'start' value till 'inp2' value is reached
                while i2 != start:
                    # filter column 'OFFENCE_FINYEAR' based on input value
                    # string filter method and string is matched exactly
                    af = df[df['OFFENCE_FINYEAR'].str.match(str(start)+'-'+str(end))]
                   
                    # values increment for while loop conditions
                    start = start + 1
                    end = end + 1

            
            self.ansText.Label=str(af)   # displays the answer
            self.inp1.Value = ""  # Clears the value entered by the user whn the result is generated
            self.inp2.Value = ""

        except ValueError: # handles exception and prompts error when the value entered is not a 4 digit value
            wx.MessageBox("Please enter 4 digit values")
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.ansText.Label = ""
       
    def onFind2(self,event):  # functionaly 2 button that will generate the graph of umber of cases for a specific offence code 
         try:
            data = pd.read_csv (r'penalty_set.csv',low_memory=False)
            df = pd.DataFrame(data, columns= ['OFFENCE_FINYEAR', 'OFFENCE_CODE'])
            
            i1=int(self.inp1.Value)
            i2=int(self.inp2.Value)
            i3=int(self.inp3.Value)
            start = i1
            end = i1 + 1
            
            count = 0
            x_year = []
            y_cases = []
            
            # loop for single year
            if i2 == (i1 + 1):
                 # filter column 'OFFENCE_FINYEAR' based on input value
                 # string filter method and string is matched exactly
                af = df[df['OFFENCE_FINYEAR'].str.match(str(i1)+'-'+str(i2))]
                
                # filter column 'OFFENCE_CODE' based on input value
                # boolean indexing and int equals value
                bf = af.loc[df['OFFENCE_CODE'] == i3]
                
                # counts length of 'bf' and is given to variable 'count'
                count = len(bf)
                
                # list 'y_cases' is appended with 'count' values
                y_cases.append(count)
                
                # 'join' gets string of current year loop
                join = str(i1)+'-'+str(i2)
                
                # list 'x_year' is appended with 'join' values
                x_year.append(join)
            
            # loop for multiple years
            elif i2 > (i1 + 1):
                while i2 != start:
                    af = df[df['OFFENCE_FINYEAR'].str.match(str(start)+'-'+str(end))]
                    bf = af.loc[df['OFFENCE_CODE'] == i3]
                    join = str(start)+'-'+str(end)
                    x_year.append(join)
                    start = start + 1
                    end = end + 1
                    count = len(bf)
                    
                    # list 'y_cases' is appended with 'count' values
                    y_cases.append(count)
             # plot is given list values and line parameters                 
            plt.plot(x_year, y_cases, "rs-")
            
            # chart title
            plt.title("Offence Chart")
            
            # x-axis label 
            plt.xlabel("Year")
            
            # y-axis label 
            plt.ylabel("No. of Cases")
            
            # legend for plot lines
            plt.legend(["Offence Code"])
            x=plt.savefig("Offence_Chart.png")
            plt.show() 
            
            self.ansText.Label=x
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp3.Value = ""
            
         except ValueError:
            wx.MessageBox("Please enter 4 digit values")
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp2.Value = ""
            self.ansText.Label = ""   
            
    def onFind3(self,event): # functionaly 1 button that will generate report for a specific keyword 'Camera' or 'Radar'
        try:
            data = pd.read_csv (r'penalty_set.csv',low_memory=False)
            df = pd.DataFrame(data, columns= ['OFFENCE_FINYEAR', 'OFFENCE_DESC'])

            i1=int(self.inp1.Value)
            i2=int(self.inp2.Value)
            i3=(self.inp3.Value)
            start = i1
            end = i1 + 1

            if i2 == (i1 + 1):
                # filter column 'OFFENCE_FINYEAR' based on input value
                # string filter method and string is matched exactly
                af = df[df['OFFENCE_FINYEAR'].str.match(str(i1)+'-'+str(i2))]
                
                # filter column 'OFFENCE_DESC' based on input value
                # string filter method and is matched with string containing input values
                bf = af[df['OFFENCE_DESC'].str.contains(str(i3))]
                
             # loop for multiple years   
            elif i2 > (i1 + 1):
                # loops with 'start' value till 'i2' value is reached
                while i2 != start:
                     # filter column 'OFFENCE_FINYEAR' based on input value
                     # string filter method and string is matched exactly
                    af = df[df['OFFENCE_FINYEAR'].str.match(str(start)+'-'+str(end))]
                    bf = af[df['OFFENCE_DESC'].str.contains(str(i3))]
                    start = start + 1
                    end = end + 1
        
            
        
            self.ansText.Label=str(bf) # print filtered results
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp3.Value = ""
            
        except ValueError:
            wx.MessageBox("Please enter 4 digit values")
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp3.Value = ""
            self.ansText.Label = ""
            
            
   
            
            
    def onFind4(self,event): # functionaly 4 button that will generate graph of cases with mobile phone usage
        try:
            
            data = pd.read_csv (r'penalty_set.csv')
            df = pd.DataFrame(data, columns= ['OFFENCE_FINYEAR', 'MOBILE_PHONE_IND', 'OFFENCE_DESC'])
            
            
            i3 = input('Keyword: ')
            i1 = int(input('Starting Year: '))
            i2 = int(input('Ending Year: '))
            i4 = input('Description: ')
            
            # variable for looping through 'OFFENCE_FINYEAR' string
            start = i1
            end = i1 + 1
            
            # int variable for counting values
            count = 0
            
            # list variable for storing values appended to it
            x_year = []
            y_cases = []
            
            # if input values match key then loop is executed
            if i3 == 'Mobile Phone' or 'Mobile phone' or 'mobile Phone' or 'mobile phone':
                # loop for single year
                if i2 == (i1 + 1):
                     # filter column 'OFFENCE_FINYEAR' based on input value
                     # string filter method and string is matched exactly
                    af = df[df['OFFENCE_FINYEAR'].str.match(str(i1)+'-'+str(i2))]
                    
                    # filter column 'MOBILE_PHONE_IND' based on input value
                    # boolean indexing and string equals value
                    bf = af.loc[df['MOBILE_PHONE_IND'] == 'Y']
                    
                    # filter column 'OFFENCE_DESC' based on input value
                    # string filter method and is matched with string containing input values
                    cf = bf[df['OFFENCE_DESC'].str.contains(i4)]
                    
                    # counts length of 'cf' and is given to variable 'count'
                    count = len(cf)
                    
                     # list 'y_cases' is appended with 'count' values
                    y_cases.append(count)
                    
                    # 'join' gets string of current year loop
                    join = str(i1)+'-'+str(i2)
                    
                    # list 'x_year' is appended with 'join' values
                    x_year.append(join)
                    
                # loop for multiple years    
                elif i2 > (i1 + 1):
                    # loops with 'start' value till 'i2' value is reached
                    while i2 != start:
                        af = df[df['OFFENCE_FINYEAR'].str.match(str(start)+'-'+str(end))]
                        bf = af[df['MOBILE_PHONE_IND'] == 'Y']
                        cf = bf[df['OFFENCE_DESC'].str.contains(i4)]
                        join = str(start)+'-'+str(end)
                        x_year.append(join)
                        start = start + 1
                        end = end + 1
                        count = len(cf)
                        
                         # list 'y_cases' is appended with 'count' values
                        y_cases.append(count)
            
            # plot is given list values and line parameters
            plt.plot(x_year, y_cases, "mD-")
            
            # chart title
            plt.title("Mobile Chart")
            
            # x-axis label
            plt.xlabel("Year")
            
            # y-axis label
            plt.ylabel("No. of Cases")
            
            # legend for plot lines
            # value from user input
            plt.legend([i4])
            
            x=plt.savefig("Mobile_Chart.png")
            fig=Figure(figsize=(5, 4), dpi=100)
            # generates charts onto the console
            plt.show()
            
            # self.dataplot=PlotPanel(self,400,350)
            # self.dataplot=plot([x_year],[y_cases])
            # numsize.Add(self.dataplot,1,wx.EXPAND)
            
            self.ansText.Label=fig(x)
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp3.Value = ""
            self.inp4.Value = ""
            
            
        except ValueError:
             wx.MessageBox("Please enter 4 digit values")
             self.inp1.Value = ""
             self.inp2.Value = ""
             self.inp3.Value = ""
             self.inp4.Value = ""
             self.ansText.Label = ""
             
    def onFind5(self,event):  # functionaly 5 button that will generate report for a specific legislation code
        try:
            data = pd.read_csv (r'penalty_set.csv',low_memory=False)
            df = pd.DataFrame(data, columns= ['OFFENCE_FINYEAR', 'LEGISLATION', 'OFFENCE_DESC'])
                
            i1=int(self.inp1.Value)
            i2=int(self.inp2.Value)
            i3=(self.inp3.Value)
            i5=(self.inp5.Value)
            start = i1
            end = i1 + 1
                
            
            if i3 == 'Legislation' or 'legislation':
            # loop for single year
                if i2 == (i1 + 1):
                # filter column 'OFFENCE_FINYEAR' based on input value
                # string filter method and string is matched exactly
                    af = df[df['OFFENCE_FINYEAR'].str.match(str(i1)+'-'+str(i2))]
                    # filter column 'LEGISLATION' based on input value
                    # string filter method and is matched with string containing input values
                    bf = af[df['LEGISLATION'].str.contains(str(i5))]
                    # print filtered results
                    
                # loop for multiple years
                elif i2 > (i1 + 1):
                    # loops with 'start' value till 'inp2' value is reached
                    while i2 != start:
                        # filter column 'OFFENCE_FINYEAR' based on input value
                        # string filter method and string is matched exactly
                        af = df[df['OFFENCE_FINYEAR'].str.match(str(start)+'-'+str(end))]
                        # filter column 'LEGISLATION' based on input value
                        # string filter method and is matched with string containing input values
                        bf = af[df['LEGISLATION'].str.contains(str(i5))]
                        # print filtered results
                        
                        # values increment for while loop conditions
                        start = start + 1
                        end = end + 1
                                  
            self.ansText.Label=str(bf)            
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp3.Value = ""
            self.inp5.Value = ""
            
        except ValueError:
            wx.MessageBox("Please enter 4 digit values")
            self.inp1.Value = ""
            self.inp2.Value = ""
            self.inp3.Value = ""
            self.inp5.Value = ""
            self.ansText.Label = ""

app=wx.App() # Create the instance that makes gui platform fully initialize
frame=DataSet(None, "Data Set")
app.MainLoop() # Executing the Gui every object assigned to wx module