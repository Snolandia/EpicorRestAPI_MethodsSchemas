import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MassRscGrpReplaceSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassRscGrpReplaceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassRscGrpReplaceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeFromResourceGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromResourceGrpID
   Description: Validates the FromResourceGrpID field and poplutes the From ResourceGrpID description.  Is called when
the From ResourceGrpID changes.  If the code is not valid, an exception will be thrown.
   OperationID: ChangeFromResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassRscGrpReplaceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToResourceGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToResourceGrpID
   Description: Validates the ToResourceGrpID field and poplutes the To ResourceGrpID description.  Is called when
the To ResourceGrpID changes.  If the code is not valid, an exception will be thrown.
   OperationID: ChangeToResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassRscGrpReplaceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMassRscGrpReplace(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMassRscGrpReplace
   Description: Creates a temporary record to store information needed for the mass work center replace process.
   OperationID: GetNewMassRscGrpReplace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMassRscGrpReplace_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassRscGrpReplaceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_MassRscGrpReplace(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method _MassRscGrpReplace
   Description: Peforms the Mass Work Center Replace.
   OperationID: _MassRscGrpReplace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/_MassRscGrpReplace_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_MassRscGrpReplace_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassRscGrpReplaceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeFromResourceGrpID_input:
   """ Required : 
   ipFromResourceGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipFromResourceGrpID:str = obj["ipFromResourceGrpID"]
      """  The proposed from op code  """  
      self.ds:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["ds"]
      pass

class ChangeFromResourceGrpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToResourceGrpID_input:
   """ Required : 
   ipToResourceGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipToResourceGrpID:str = obj["ipToResourceGrpID"]
      """  The proposed from op code  """  
      self.ds:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["ds"]
      pass

class ChangeToResourceGrpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_MassRscGrpReplaceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      self.FromResourceGrpDesc:str = obj["FromResourceGrpDesc"]
      self.ToResourceGrpID:str = obj["ToResourceGrpID"]
      self.ToResourceGrpDesc:str = obj["ToResourceGrpDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassRscGrpReplaceTableset:
   def __init__(self, obj):
      self.MassRscGrpReplace:list[Erp_Tablesets_MassRscGrpReplaceRow] = obj["MassRscGrpReplace"]
      self.MassRscGrpResults:list[Erp_Tablesets_MassRscGrpResultsRow] = obj["MassRscGrpResults"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassRscGrpResultsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.PartDescription:str = obj["PartDescription"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetNewMassRscGrpReplace_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["returnObj"]
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

class _MassRscGrpReplace_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["ds"]
      pass

class _MassRscGrpReplace_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassRscGrpReplaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

