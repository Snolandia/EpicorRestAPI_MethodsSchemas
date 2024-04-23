import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TimeExpenseSharedSvc
# Description: TimeExpensShared Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TimeExpenseSharedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TimeExpenseSharedSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetTimeExpenseSharedOptions(epicorHeaders = None):
   """  
   Summary: Invoke method GetTimeExpenseSharedOptions
   Description: Returns the Time/Expense shared options
   OperationID: GetTimeExpenseSharedOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTimeExpenseSharedOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimeExpenseSharedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetTimeExpenseSharedOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTimeExpenseSharedOptions
   Description: Sets the Time/Expense shared options
   OperationID: SetTimeExpenseSharedOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTimeExpenseSharedOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTimeExpenseSharedOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimeExpenseSharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDateRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDateRange
   OperationID: GetDateRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDateRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimeExpenseSharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_TimeExpenseSharedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TEAprRetrieveApproved:bool = obj["TEAprRetrieveApproved"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  """  
      self.TEAprRetrieveEntered:bool = obj["TEAprRetrieveEntered"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  """  
      self.TEAprRetrievePartiallyApproved:bool = obj["TEAprRetrievePartiallyApproved"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  """  
      self.TEAprRetrieveRejected:bool = obj["TEAprRetrieveRejected"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  """  
      self.TEAprRetrieveSubmitted:bool = obj["TEAprRetrieveSubmitted"]
      """  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  """  
      self.TERetrieveApproved:bool = obj["TERetrieveApproved"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  """  
      self.TERetrieveByDay:bool = obj["TERetrieveByDay"]
      """  Retrieve time and expense records by day  """  
      self.TERetrieveByMonth:bool = obj["TERetrieveByMonth"]
      """  Retrieve time and expense records by month  """  
      self.TERetrieveByWeek:bool = obj["TERetrieveByWeek"]
      """  Retrieve time and expense records by week  """  
      self.TERetrieveEntered:bool = obj["TERetrieveEntered"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  """  
      self.TERetrievePartiallyApproved:bool = obj["TERetrievePartiallyApproved"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  """  
      self.TERetrieveRejected:bool = obj["TERetrieveRejected"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  """  
      self.TERetrieveSubmitted:bool = obj["TERetrieveSubmitted"]
      """  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TimeExpenseSharedTableset:
   def __init__(self, obj):
      self.TimeExpenseShared:list[Erp_Tablesets_TimeExpenseSharedRow] = obj["TimeExpenseShared"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetDateRange_input:
   """ Required : 
   workDate
   """  
   def __init__(self, obj):
      self.workDate:str = obj["workDate"]
      pass

class GetDateRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fromDate:str = obj["parameters"]
      self.toDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTimeExpenseSharedOptions_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TimeExpenseSharedTableset] = obj["returnObj"]
      pass

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

class SetTimeExpenseSharedOptions_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TimeExpenseSharedTableset] = obj["ds"]
      pass

class SetTimeExpenseSharedOptions_output:
   def __init__(self, obj):
      pass

