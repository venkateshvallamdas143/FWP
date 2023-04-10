import pandas as pd
import openpyxl
import os
import json 
import os
import numpy as np
import datetime as dt

#//*----when the input path is Xlsx File....*//

def xlsx_to_dict1(new_excel):

    #//*----Name---*//
    # df = pd.read_excel(r"C:\Users\HP\Downloads\Master FWR to PDF File.xlsx",usecols='A:C',nrows=1,index_col=False)
    # df.columns = df.columns.str.strip()
    # df.fillna('', inplace=True)
    # json_format = df.to_dict(orient='records')
    # json_data['Name']=json_format
    
    # df1 = pd.read_excel(r"C:\Users\HP\Downloads\Master FWR to PDF File.xlsx",usecols='A',skiprows=4,nrows=1,index_col=False)
    # df1.columns = df1.columns.str.strip()
    # df1.fillna('', inplace=True)
    # json_format = df1.to_dict(orient='records')
    # json_data['Score']=json_format
    #//*---Namee----*//
    json_data = {}
    df = pd.read_excel(new_excel)
    df1 = df.iloc[[0],0:3]
    df.fillna('', inplace=True)
    json_format = df1.to_dict(orient='records')
    json_data['Name']=json_format
    
    #//*----Score----*//
    df2 = df.iloc[[4],[0]]
    df2.rename(columns = {'Name':'C_Score'}, inplace = True)
    df2.fillna('', inplace=True)
    json_format = df2.to_dict(orient='records')
    json_data['Score']=json_format
    json_data

    #//*----Genration-------*//
    
    df3 = df.iloc[[7],[0]]
    df3.rename(columns = {'Name':'Gen Profile'}, inplace = True)
    df3.fillna('', inplace=True)
    json_format = df3.to_dict(orient='records')
    json_data['Genration']=json_format
    
    #//*----Life Stage--*//
    df4 = df.iloc[[10],[0]]
    df4.rename(columns = {'Name':'Life Stage'}, inplace = True)
    df4.fillna('', inplace=True)
    json_format = df4.to_dict(orient='records')
    json_data['Life Stage']=json_format
    
    #//*----Asset---*//
    df5 = df.iloc[15:22,0:3]
    df5.rename(columns = {'Name':'Asset','Date':'Amount','Mobile no':'Units'}, inplace = True)
    asset = df5.replace(r'^\s*$', np.nan, regex=True)
    asset = asset.dropna()
    json_format = asset.to_dict(orient='records')
    json_data['Asset']=json_format
    
    #//*----Income----*//
    df6 = df.iloc[25:28,0:3]
    df6.rename(columns = {'Name':'Income','Date':'Amount','Mobile no':'Units'}, inplace = True)
    income = df6.replace(r'^\s*$','-', regex=True)
    json_format = income.to_dict(orient='records')
    json_data['Income']=json_format
    
    #//*----Expense---*//
    df6 = df.iloc[31:34,0:3]
    df6.rename(columns = {'Name':'Expense','Date':'Amount','Mobile no':'Units'}, inplace = True)
    expense = df6.replace(r'^\s*$','-', regex=True)
    json_format = expense.to_dict(orient='records')
    json_data['Expense']=json_format
    
    #//*----Insurance---*//
    df6 = df.iloc[38:40,0:3]
    df6.rename(columns = {'Name':'Insurance','Date':'Amount','Mobile no':'Units'}, inplace = True)
    expense = df6.replace(r'^\s*$','-', regex=True)
    json_format = expense.to_dict(orient='records')
    json_data['Insurance']=json_format
    
    #//*----Liabilities---*//
    df6 = df.iloc[44:46,0:3]
    df6.rename(columns = {'Name':'Liabilities','Date':'Amount','Mobile no':'Units'}, inplace = True)
    Liabilities = df6.replace(r'^\s*$','-', regex=True)
    json_format = Liabilities.to_dict(orient='records')
    json_data['Liabilities']=json_format
    
    #//*---Asset Snap Shot----*//
    df7 = df.iloc[48:60,0:7]
    df7.columns = df7.iloc[0]
    df7=df7.drop(df7.index[0])
    asset_snap = df7.replace(r'^\s*$',np.nan, regex=True)
    asset_snap = asset_snap.replace({np.nan: None})
    asset_snap = asset_snap.dropna(subset=['%'])
    json_format = asset_snap.to_dict(orient='records')
    json_data['Asset Snapshot']=json_format
    
    #//*----Asset Allocation----*//
    df8 = df.iloc[62:67,0:2]
    df8.rename(columns = {'Name':'Asset Allocation','Date':'%'}, inplace = True)
    asset_alloc = df8.replace(r'^\s*$',np.nan, regex=True)
    asset_alloc = asset_alloc.dropna(subset=['Asset Allocation'])
    asset_alloc = asset_alloc.replace({np.nan: 0})
    json_format = asset_alloc.to_dict(orient='records')
    json_data['Asset Allocation']=json_format
    
    #//*---Liability Snapshot----*//
    df9 = df.iloc[70:79,0:6]
    df9.columns = df9.iloc[0]
    df9=df9.drop(df9.index[0])
    lib_snap = df9.replace(r'^\s*$',np.nan, regex=True)
    lib_snap = lib_snap.dropna(subset=['Liability'])
    lib_snap = lib_snap.replace(np.nan,'-', regex=True)
    json_format = lib_snap.to_dict(orient='records')
    json_data['Liability Snapshot']=json_format
    
    #//**---Liability Allocation----*//
    df10 = df.iloc[82:84,0:2]
    df10.rename(columns = {'Name':'Liability Allocation','Date':'%'}, inplace = True)
    lib_alloc = df10.replace(r'^\s*$',0, regex=True)
    lib_alloc = lib_alloc.replace('-',0)
    json_format = lib_alloc.to_dict(orient='records')
    json_data['Liability Allocation']=json_format
    
    
    #//*----Expense and Liability Management----*//
    df11 = df.iloc[87:94,0:5]
    df11.columns = df11.iloc[0]
    df11=df11.drop(df11.index[0])
    exp_lib_manag = df11.replace(r'^\s*$',np.nan, regex=True)
    exp_lib_manag = exp_lib_manag.dropna(subset=['Ratios'])
    exp_lib_manag = exp_lib_manag.replace({np.nan:0})
    json_format = exp_lib_manag.to_dict(orient='records')
    json_data['Exp_lib_management']=json_format
    
    #//*----Asset Allocation 2------*//
    df12 = df.iloc[97:103,0:5]
    df12.columns = df12.iloc[0]
    df12=df12.drop(df12.index[0])
    asset_alloc2 = df12.replace(r'^\s*$','-', regex=True)
    asset_alloc2 = asset_alloc2.dropna(subset=['Ratios'])
    asset_alloc2 = asset_alloc2.replace({np.nan:0})
    json_format = asset_alloc2.to_dict(orient='records')
    json_data['Asset Allocation_2']=json_format
    
    #//*----Emergency Planning------*//
    df13 = df.iloc[106:110,0:7]
    df13.columns = df13.iloc[0]
    df13=df13.drop(df13.index[0])
    
    new_reg = []
    for i in range(len(df13)):
        try:
            x =(df13['Ideal'].iloc[i]).strftime('%#m-%d')
            new_reg.append(x)
        except:
            new_reg.append(df13['Ideal'].iloc[i])
    df13['Ideal'] = new_reg
            
    emeg_plan = df13.replace(r'^\s*$',np.nan, regex=True)
    emeg_plan = emeg_plan.dropna(subset=['Ratios'])
    emeg_plan = emeg_plan.replace({np.nan:0})
    json_format = emeg_plan.to_dict(orient='records')

    json_data['Emergence Planning']=json_format
    
    #//*------Net Worth-------*//
    df14 = df.iloc[113:115,0:6]
    df14.columns = df14.iloc[0]
    df14=df14.drop(df14.index[0])
    net_worth = df14.replace(r'^\s*$','0', regex=True)
    json_format = net_worth.to_dict(orient='records')
    json_data['Net Worth']=json_format
    json_format
    
    #//*------Value Under Advisoary-------*//
    df25 = df.iloc[115:117,0:2]
    df25.columns = df25.iloc[0]
    df25=df25.drop(df25.index[0])
    val_un_adv = df25.replace(r'^\s*$','0', regex=True)
    json_format = val_un_adv.to_dict(orient='records')
    json_data['val_un_adv']=json_format
    json_format
     
    #//*----Networth Projection-----*//
    df15 = df.iloc[120:160,0:5]
    df15.columns = df15.iloc[0]
    df15=df15.drop(df15.index[0])
    net_worth_proj = df15.replace(r'^\s*$',np.nan, regex=True)
    net_worth_proj = net_worth_proj.replace({np.nan: None})
    net_worth_proj = net_worth_proj.dropna(subset=['year'])
    json_format = net_worth_proj.to_dict(orient='records')
    json_data['Networth Projection']=json_format
    
    #//*-------Our Asuumption -----*//
    df16 = df.iloc[167:173,0:6]
    df16.columns = df16.iloc[0]
    df16=df16.drop(df16.index[0])
    our_asumpt = df16.replace(r'^\s*$',np.nan, regex=True)
    our_asumpt = our_asumpt.dropna(subset=['Asset Classes'])
    json_format = our_asumpt.to_dict(orient='records')
    json_data['Our Assumption']=json_format
    
    #//*---------Our Asuumption (Expected Income Growth)----*//
    df17 = df.iloc[176:183,0:3]
    df17.columns = df17.iloc[0]
    df17=df17.drop(df17.index[0])
    oa_expect_income = df17.replace(r'^\s*$',np.nan, regex=True)
    oa_expect_income = oa_expect_income.replace({np.nan: None})
    oa_expect_income = oa_expect_income.dropna(subset=['Expected Income Growth'])
    new_reg = []
    for i in range(len(df17)):
        try:
            x =(df17['Age Range'].iloc[i]).strftime('%#m-%d')
            new_reg.append(x)
        except:
            new_reg.append(df17['Age Range'].iloc[i])
    df17['Age Range'] = new_reg
    json_format = oa_expect_income.to_dict(orient='records')
    json_data['OA Expected Income']=json_format
    
    #//*---------Our Asuumption (Expected Interest Rate)----*// 
    df18 = df.iloc[176:182,4:6]
    df18.columns = df18.iloc[0]
    df18=df18.drop(df18.index[0])
    oa_expect_interest = df18.replace(r'^\s*$',np.nan, regex=True)
    oa_expect_interest = oa_expect_interest.replace({np.nan: None})
    oa_expect_interest = oa_expect_interest.dropna(subset=['Expected Interest Rate'])
    json_format = oa_expect_interest.to_dict(orient='records')
    json_data['OA Expected Interest']=json_format
    
    #//**------------Key Takeaways---------------------*//
    df19 = df.iloc[186:189,0:1]
    df19.columns = df19.iloc[0]
    df19=df19.drop(df19.index[0])
    kt_expense = df19.replace(r'^\s*$',np.nan, regex=True)
    kt_expense = kt_expense.dropna(subset=['Expense and Liabiility Management'])
    json_format = kt_expense.to_dict(orient='records')
    json_data['Kt Expense_lib_manage']=json_format

    df20 = df.iloc[190:193,0:1]
    df20.columns = df20.iloc[0]
    df20=df20.drop(df20.index[0])
    kt_asset = df20.replace(r'^\s*$',np.nan, regex=True)
    kt_asset = kt_asset.dropna(subset=['Asset Allocation'])
    json_format = kt_asset.to_dict(orient='records')
    json_data['Kt Asset']=json_format

    df21 = df.iloc[194:197,0:1]
    df21.columns = df21.iloc[0]
    df21=df21.drop(df21.index[0])
    kt_emergency = df21.replace(r'^\s*$',np.nan, regex=True)
    kt_emergency = kt_emergency.dropna(subset=['Emergency Planning'])
    json_format = kt_emergency.to_dict(orient='records')
    json_data['Kt Expense']=json_format
    
    
    #//*---Next 3 months Cash Flow Plan----*//
    #//*----Table
    df22 = df.iloc[201:208,0:3]
    df22.columns = df22.iloc[0]
    df22=df22.drop(df22.index[0])
    cash_flow = df22.replace(r'^\s*$',np.nan, regex=True)
    cash_flow = cash_flow.dropna(subset=['Next 3M Cashflows'])
    json_format = cash_flow.to_dict(orient='records')
    json_data['Cash Flow Plan']=json_format
    
    #//*---Comments (Cf Emergency Planning)---*/
    df23 = df.iloc[210:214,0:1]
    
    try:
        df23.columns = df23.iloc[0]
        df23=df23.drop(df23.index[0])
        
    except:
        pass
    cf_emergency = df23.replace(r'^\s*$',np.nan, regex=True)
    cf_emergency = cf_emergency.dropna()
    json_format = cf_emergency.to_dict(orient='records')
    json_data['Cf Emergency Planning']=json_format
    
     #//*---Comments (Cf Asset Allocation)---*/
    df24 = df.iloc[215:219,0:1]
    try:
        df24.columns = df24.iloc[0]
        df24=df24.drop(df24.index[0])
        
    except:
        pass
    cf_asset = df24.replace(r'^\s*$',np.nan, regex=True)
    cf_asset = cf_asset.dropna()
    json_format = cf_asset.to_dict(orient='records')
    json_data['Cf Asset Allocation']=json_format
    
    #//*---Cooments (Cf Asset Allocation)---*/
    df24 = df.iloc[220:224,0:1]
    try:
        df24.columns = df24.iloc[0]
        df24=df24.drop(df24.index[0])
        
    except:
        pass
    cf_ass_lib = df24.replace(r'^\s*$',np.nan, regex=True)
    cf_ass_lib = cf_ass_lib.dropna()
    json_format = cf_ass_lib.to_dict(orient='records')
    json_data['Cf Asset Lib Allooc']=json_format
    
    #//*-----Bureau Report Summary---*//
    #//*---Credit Score Analysis---*//
    df26 = df.iloc[227:229,0:3]
    df26.columns = df26.iloc[0]
    df26=df26.drop(df26.index[0])
    json_format = df26.to_dict(orient='records')
    json_data['Credit_score_analysis']=json_format
    
    #//*---Credit Facilities Taken---*//
    df27 = df.iloc[231:239,0:5]
    try:
        df27.columns = df27.iloc[0]
        df27=df27.drop(df27.index[0])
        df27 = df27.replace(r'^\s*$',np.nan, regex=True)
        df27 = df27.dropna(subset=['Type of Facility'])
        
    except:
        pass
    
    json_format = df27.to_dict(orient='records')
    json_data['Credit_facility_taken']=json_format
    
    
    
    #//***----B. Liability Analysis-----*//
    #//*--B.a. Affordability Check
    df28 = df.iloc[243:247,0:7]
    df28.columns = df28.iloc[0]
    df28=df28.drop(df28.index[0])
    json_format = df28.to_dict(orient='records')
    json_data['affordibility_check']=json_format
    
    #//***----B.a. Affordability Check (Comments)-----*//
    df29 = df.iloc[248:251,0:1]
    df29.columns = df29.iloc[0]
    df29=df29.drop(df29.index[0])
    df29 = df29.replace(r'^\s*$',np.nan, regex=True)
    df29 = df29.dropna()
    json_format = df29.to_dict(orient='records')
    json_data['affordibility_check_comment']=json_format
    
    #//***----Rate Reduction Opportunities-----*//
    
    df30 = df.iloc[253:264,0:8]
    try:
        df30.columns = df30.iloc[0]
        df30=df30.drop(df30.index[0])
        df30 = df30.replace(r'^\s*$',np.nan, regex=True)
        df30 = df30.dropna(subset=['Liability'])
        df30 = df30.replace({np.nan: '-'})
        
    except:
        pass
    
    json_format = df30.to_dict(orient='records')
    json_data['rate_reduction_oppurtunities']=json_format
    
    
    
    
    
    json_data = json.dumps(json_data,default = str)
    with open('json_data_new.json', 'w') as outfile:
        outfile.write(json_data)
    return json_data

    
    
    


      
# new_excel = r"C:\Users\HP\OneDrive\Desktop\New Master FWP.xlsx"
# xlsx_to_dict1(new_excel)

#//*----When the input file is Json File----*//
def json_to_dict(json_file):
    with open(json_file) as f:
        js_data = json.load(f)
    json_data = {}
    
    for key,value in js_data.items():
        df = pd.DataFrame.from_dict(js_data[key])
        df.columns = df.columns.str.strip()
        json_format = df.to_dict(orient='records')
        json_data[key.strip()]=json_format
        
    json_data = json.dumps(json_data,default = str)
    with open('json_data.json', 'w') as outfile:
        outfile.write(json_data)
        
    return json_data   
      
# json_to_dict(r'D:\Atrina\1F Wellness Report1\json_data.json')  
    
