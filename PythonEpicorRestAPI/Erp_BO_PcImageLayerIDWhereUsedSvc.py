import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PcImageLayerIDWhereUsedSvc
# Description: Determines which ConfigID's are using a specific Image Layer ID
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetImageLayerIDWhereUsed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetImageLayerIDWhereUsed
   Description: Retrieve Configurations using the Image Layer ID passed into this method.
   OperationID: GetImageLayerIDWhereUsed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetImageLayerIDWhereUsed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetImageLayerIDWhereUsed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RebuildLayerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RebuildLayerDetails
   Description: Call this method when you want to push image layer definition changes to a configurator
   OperationID: RebuildLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RebuildLayerDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RebuildLayerDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcImageLayerIDWhereUsedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PcImageLayerIDWhereUsedRow:
   def __init__(self, obj):
      self.Approved:bool = obj["Approved"]
      """  Indicates the approval status of the configuration.  """  
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Indicates the configuration ID this Image LayerID is associated with.  """  
      self.ConfigType:str = obj["ConfigType"]
      """  Indicates the type of configuration defined in Configuration Entry.  """  
      self.Description:str = obj["Description"]
      """  Configuration description.  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Identifies a unique Image Layer.  """  
      self.Selected:bool = obj["Selected"]
      """  Indicates selected status.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcImageLayerIDWhereUsedTableset:
   def __init__(self, obj):
      self.PcImageLayerIDWhereUsed:list[Erp_Tablesets_PcImageLayerIDWhereUsedRow] = obj["PcImageLayerIDWhereUsed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetImageLayerIDWhereUsed_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      """  Image Layer ID used to query configurations for their use.  """  
      pass

class GetImageLayerIDWhereUsed_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcImageLayerIDWhereUsedTableset] = obj["returnObj"]
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

class RebuildLayerDetails_input:
   """ Required : 
   pcImageLayerIDWhereUsedTS
   """  
   def __init__(self, obj):
      self.pcImageLayerIDWhereUsedTS:list[Erp_Tablesets_PcImageLayerIDWhereUsedTableset] = obj["pcImageLayerIDWhereUsedTS"]
      pass

class RebuildLayerDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcImageLayerIDWhereUsedTS:list[Erp_Tablesets_PcImageLayerIDWhereUsedTableset] = obj["pcImageLayerIDWhereUsedTS"]
      pass

      """  output parameters  """  

