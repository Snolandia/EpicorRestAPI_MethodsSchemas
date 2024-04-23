import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustReminderSearchSvc
# Description: Purpose:
Parameters:  none
Notes:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CustomerReminderSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomerReminderSearch
   OperationID: CustomerReminderSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomerReminderSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomerReminderSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhereClause
   Description: Purpose:     Fixing the original WhereClauseCustReminderSearch to be parsed in Dynamic.cs
Parameters:  WhereClauseCustReminderSearch
Notes:
   OperationID: GetNewWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the Customers records that meet the selection criteria.
This method will try to mirror the functionality of the base GetList method but
since we are populating a temp table we need our own public method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListRowLoaded(epicorHeaders = None):
   """  
   Summary: Invoke method GetListRowLoaded
   Description: partial GetListRowLoaded - not working due to no getList method
   OperationID: GetListRowLoaded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListRowLoaded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CustReminderSearchAfterGetNew(epicorHeaders = None):
   """  
   Summary: Invoke method CustReminderSearchAfterGetNew
   Description: Not implemented - exception will thrown
   OperationID: CustReminderSearchAfterGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustReminderSearchAfterGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CustReminderSearchAfterGetRows(epicorHeaders = None):
   """  
   Summary: Invoke method CustReminderSearchAfterGetRows
   Description: Not implemented - no exception
   OperationID: CustReminderSearchAfterGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustReminderSearchAfterGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CustReminderSearchBeforeDelete(epicorHeaders = None):
   """  
   Summary: Invoke method CustReminderSearchBeforeDelete
   Description: Not implemented - exception will thrown
   OperationID: CustReminderSearchBeforeDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustReminderSearchBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CustReminderSearchBeforeUpdate(epicorHeaders = None):
   """  
   Summary: Invoke method CustReminderSearchBeforeUpdate
   Description: Not implemented - exception will thrown
   OperationID: CustReminderSearchBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustReminderSearchBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustReminderSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CustReminderSearchAfterGetNew_output:
   def __init__(self, obj):
      pass

class CustReminderSearchAfterGetRows_output:
   def __init__(self, obj):
      pass

class CustReminderSearchBeforeDelete_output:
   def __init__(self, obj):
      pass

class CustReminderSearchBeforeUpdate_output:
   def __init__(self, obj):
      pass

class CustomerReminderSearch_input:
   """ Required : 
   WhereClauseCustReminderSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClauseCustReminderSearch:str = obj["WhereClauseCustReminderSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class CustomerReminderSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustReminderSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CustReminderSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Country:str = obj["Country"]
      self.CreditHold:bool = obj["CreditHold"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.CustomerType:str = obj["CustomerType"]
      self.GroupCode:str = obj["GroupCode"]
      self.InvoiceBalance:int = obj["InvoiceBalance"]
      self.LastNumDays:int = obj["LastNumDays"]
      self.Name:str = obj["Name"]
      self.PastDueDays:int = obj["PastDueDays"]
      self.ReminderCode:str = obj["ReminderCode"]
      self.State:str = obj["State"]
      self.TerritoryID:str = obj["TerritoryID"]
      self.City:str = obj["City"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustReminderSearchListTableset:
   def __init__(self, obj):
      self.CustReminderSearchList:list[Erp_Tablesets_CustReminderSearchListRow] = obj["CustReminderSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetListFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustReminderSearchListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustReminderSearchListTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListRowLoaded_output:
   def __init__(self, obj):
      pass

class GetNewWhereClause_input:
   """ Required : 
   WhereClauseCustReminderSearch
   """  
   def __init__(self, obj):
      self.WhereClauseCustReminderSearch:str = obj["WhereClauseCustReminderSearch"]
      pass

class GetNewWhereClause_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

