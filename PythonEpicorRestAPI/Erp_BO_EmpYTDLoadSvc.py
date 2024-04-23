import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EmpYTDLoadSvc
# Description: 
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_DeleteEmpYTDLoad(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteEmpYTDLoad
   Description: Deletes the PRCheck record.  The delete trigger for PRCheck deletes the
PRChkDtl, PRChkTax and PRChkDed records.
   OperationID: DeleteEmpYTDLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteEmpYTDLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteEmpYTDLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmpYTDLoadForEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmpYTDLoadForEmpID
   Description: Gets the data for Deductions, Earnings, and Tax for a specific employee id.
   OperationID: GetEmpYTDLoadForEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpYTDLoadForEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpYTDLoadForEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEmpYTDLoad(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmpYTDLoad
   Description: Gets the data for the Deductions, Earnings and Tax temp tables based on the
employee ID's from the Employee ID temp table.
   OperationID: GetEmpYTDLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpYTDLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpYTDLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmployeeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmployeeList
   Description: This method is only to be used in the BL Tester to get a EmployeeList
record for employee 100.
   OperationID: GetNewEmployeeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmployeeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetEmpYTDLoad(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetEmpYTDLoad
   Description: Updates the appropriate tables with the data for the Deductions, Earnings and
Tax temp tables.
   OperationID: SetEmpYTDLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEmpYTDLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEmpYTDLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPRPeriodEndDate(epicorHeaders = None):
   """  
   Summary: Invoke method GetPRPeriodEndDate
   OperationID: GetPRPeriodEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPRPeriodEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetEmpYTDLoadTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmpYTDLoadTotals
   Description: Calculates Employee YTD Load totals and returns the values in a dataset
   OperationID: GetEmpYTDLoadTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpYTDLoadTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpYTDLoadTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteEmpYTDLoad_input:
   """ Required : 
   EmployeeID
   """  
   def __init__(self, obj):
      self.EmployeeID:str = obj["EmployeeID"]
      """  Employee number  """  
      pass

class DeleteEmpYTDLoad_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EmpYTDLoadDeductRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeID:str = obj["EmployeeID"]
      """  Employee ID  """  
      self.DeductionID:str = obj["DeductionID"]
      """  Payroll deduction ID  """  
      self.DeductionDesc:str = obj["DeductionDesc"]
      """  Deductions description  """  
      self.DeductionAmt:int = obj["DeductionAmt"]
      """  Deduction Amount  """  
      self.DeductionNum:int = obj["DeductionNum"]
      """  Deduction number  """  
      self.OrigDeductionAmt:int = obj["OrigDeductionAmt"]
      """  Original deduction amount  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpYTDLoadEarnRow:
   def __init__(self, obj):
      self.EarningType:str = obj["EarningType"]
      """  Earnings type.  """  
      self.EarningsHours:int = obj["EarningsHours"]
      """  Earning hours  """  
      self.EarningsAmt:int = obj["EarningsAmt"]
      """  Earnings amount  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeID:str = obj["EmployeeID"]
      """  Employee ID  """  
      self.EarningTypeDesc:str = obj["EarningTypeDesc"]
      """  Earning type description  """  
      self.OrigPremiumPay:int = obj["OrigPremiumPay"]
      """  Original Premium pay amount  """  
      self.OrigPremiumBasePay:int = obj["OrigPremiumBasePay"]
      """  Original Premium base pay amount  """  
      self.OrigBasePay:int = obj["OrigBasePay"]
      """  Original base pay amount  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpYTDLoadTableset:
   def __init__(self, obj):
      self.EmpYTDLoadDeduct:list[Erp_Tablesets_EmpYTDLoadDeductRow] = obj["EmpYTDLoadDeduct"]
      self.EmpYTDLoadEarn:list[Erp_Tablesets_EmpYTDLoadEarnRow] = obj["EmpYTDLoadEarn"]
      self.EmpYTDLoadTax:list[Erp_Tablesets_EmpYTDLoadTaxRow] = obj["EmpYTDLoadTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpYTDLoadTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeID:str = obj["EmployeeID"]
      """  Employee ID  """  
      self.TaxTableID:str = obj["TaxTableID"]
      """  Tax table ID  """  
      self.TaxTableDesc:str = obj["TaxTableDesc"]
      """  Tax table description  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax amount  """  
      self.OrigTaxAmt:int = obj["OrigTaxAmt"]
      """  Original tax amount  """  
      self.TaxType:str = obj["TaxType"]
      """  Tax type from PRTaxMas  """  
      self.InActive:bool = obj["InActive"]
      """  In active status from PREmpTax  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpYTDLoadTotalsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DeductionTotal:int = obj["DeductionTotal"]
      """  Deduction Total  """  
      self.EarningsTotal:int = obj["EarningsTotal"]
      """  Earnings total  """  
      self.HoursTotal:int = obj["HoursTotal"]
      """  Hours Total  """  
      self.TaxTotal:int = obj["TaxTotal"]
      """  Tax Total  """  
      self.EmployeeID:str = obj["EmployeeID"]
      """  Employee ID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpYTDLoadTotalsTableset:
   def __init__(self, obj):
      self.EmpYTDLoadTotals:list[Erp_Tablesets_EmpYTDLoadTotalsRow] = obj["EmpYTDLoadTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmployeeIDListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeID:str = obj["EmployeeID"]
      """  Employee IDs  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmployeeIDListTableset:
   def __init__(self, obj):
      self.EmployeeIDList:list[Erp_Tablesets_EmployeeIDListRow] = obj["EmployeeIDList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetEmpYTDLoadForEmpID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      pass

class GetEmpYTDLoadForEmpID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpYTDLoadTableset] = obj["returnObj"]
      pass

class GetEmpYTDLoadTotals_input:
   """ Required : 
   empID
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  The employee id to calculate totals for  """  
      self.ds:list[Erp_Tablesets_EmpYTDLoadTableset] = obj["ds"]
      pass

class GetEmpYTDLoadTotals_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpYTDLoadTotalsTableset] = obj["returnObj"]
      pass

class GetEmpYTDLoad_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmployeeIDListTableset] = obj["ds"]
      pass

class GetEmpYTDLoad_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpYTDLoadTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmployeeIDListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmployeeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmployeeIDListTableset] = obj["returnObj"]
      pass

class GetPRPeriodEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.prPeriodEndDate:str = obj["parameters"]
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class SetEmpYTDLoad_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpYTDLoadTableset] = obj["ds"]
      pass

class SetEmpYTDLoad_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpYTDLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

