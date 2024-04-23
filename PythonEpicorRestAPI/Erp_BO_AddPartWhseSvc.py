import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AddPartWhseSvc
# Description: AddPartWhse
           Give the user the ability to create a part/warehouse record on the fly.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AddPartWhseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AddPartWhseSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CreatePartWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePartWhse
   Description: Creates a PartWhse record.
   OperationID: CreatePartWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePartWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePartWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AddPartWhseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWareHseList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWareHseList
   Description: Get a list of warehouses where the part does not exist.
   OperationID: GetWareHseList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWareHseList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWareHseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AddPartWhseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CreatePartWhse_input:
   """ Required : 
   partNum
   plant
   wareHseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number.  """  
      self.plant:str = obj["plant"]
      """  Plant.  """  
      self.wareHseCode:str = obj["wareHseCode"]
      """  Warhouse code.  """  
      pass

class CreatePartWhse_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AddPartWhseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number  """  
      self.PlantID:str = obj["PlantID"]
      """  Plant ID  """  
      self.WareHseCode:str = obj["WareHseCode"]
      """  Warehousecode  """  
      self.WareHseCodeDesc:str = obj["WareHseCodeDesc"]
      """  WareHousecode description  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AddPartWhseTableset:
   def __init__(self, obj):
      self.AddPartWhse:list[Erp_Tablesets_AddPartWhseRow] = obj["AddPartWhse"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetWareHseList_input:
   """ Required : 
   partNum
   plant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number for the search.  """  
      self.plant:str = obj["plant"]
      """  Plant for the search.  """  
      pass

class GetWareHseList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AddPartWhseTableset] = obj["returnObj"]
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

