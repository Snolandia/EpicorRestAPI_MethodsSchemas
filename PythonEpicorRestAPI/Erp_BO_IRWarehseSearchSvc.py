import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IRWarehseSearchSvc
# Description: Used in bo/IssueReturn/IssueReturn.p to display From and To Warehouse combo-box.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IRWarehseSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IRWarehseSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetWarehseList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWarehseList
   Description: This method returns a list of warehouses. In a STK type of transaction
this search looks into PlantWhse table and returns the warehouses where the
pcPartNum is defined. For other transaction types it looks into PlantShare table
and returns the shared warehouses.
   OperationID: GetWarehseList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarehseList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IRWarehseSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_IRWarehseSearchTableset:
   def __init__(self, obj):
      self.WarehseSearch:list[Erp_Tablesets_WarehseSearchRow] = obj["WarehseSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WarehseSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.Description:str = obj["Description"]
      self.Name:str = obj["Name"]
      self.Plant:str = obj["Plant"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetWarehseList_input:
   """ Required : 
   pcTranType
   pcPartNum
   pcWarehseType
   pcPkgControlWarehouseType
   """  
   def __init__(self, obj):
      self.pcTranType:str = obj["pcTranType"]
      """  IssueReturn Transaction type  """  
      self.pcPartNum:str = obj["pcPartNum"]
      """  PartNum involved in Issue / Return  """  
      self.pcWarehseType:str = obj["pcWarehseType"]
      """  Valid values are From or To.  """  
      self.pcPkgControlWarehouseType:str = obj["pcPkgControlWarehouseType"]
      """  Warehouse type. Valid values are WIP, STOCK and QUALITY  """  
      pass

class GetWarehseList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IRWarehseSearchTableset] = obj["returnObj"]
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

