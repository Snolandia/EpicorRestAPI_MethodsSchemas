import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandFromOrdersSvc
# Description: DemandFromOrders Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandFromOrdersSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandFromOrdersSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_UpdateOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateOrders
   Description: A List of orders to Create Demand.
   OperationID: UpdateOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandFromOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDemandContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDemandContract
   Description: Procedure to validate Demand Contract
   OperationID: OnChangeDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandFromOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileType
   OperationID: FileType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandFromOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_DemandFromOrdersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandFromOrdersTableset:
   def __init__(self, obj):
      self.DemandFromOrders:list[Erp_Tablesets_DemandFromOrdersRow] = obj["DemandFromOrders"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FileType_input:
   """ Required : 
   FileInfo
   """  
   def __init__(self, obj):
      self.FileInfo:str = obj["FileInfo"]
      pass

class FileType_output:
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

class OnChangeDemandContract_input:
   """ Required : 
   pOrderNum
   pDcontract
   """  
   def __init__(self, obj):
      self.pOrderNum:int = obj["pOrderNum"]
      """  Complete Message  """  
      self.pDcontract:str = obj["pDcontract"]
      """  Complete Message  """  
      pass

class OnChangeDemandContract_output:
   def __init__(self, obj):
      pass

class UpdateOrders_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandFromOrdersTableset] = obj["ds"]
      pass

class UpdateOrders_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandFromOrdersTableset] = obj["ds"]
      self.opcCompMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

