import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MassOperationReplaceSvc
# Description: Use this function to replace Mass Operation
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeFromOpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromOpCode
   Description: Validates the FromOpCode field and poplutes the From OpCode description.  Is called when
the From Op Code changes.  If the code is not valid, an exception will be thrown.
   OperationID: ChangeFromOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToOpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToOpCode
   Description: Validates the ToOpCode field and poplutes the To OpCode description.  Is called when
the To Op Code changes.  If the code is not valid, an exception will be thrown.
   OperationID: ChangeToOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunMassOperationReplace(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunMassOperationReplace
   Description: Peforms the Mass Operation Replace.
   OperationID: RunMassOperationReplace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunMassOperationReplace_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunMassOperationReplace_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassOperationReplaceGetNew(epicorHeaders = None):
   """  
   Summary: Invoke method MassOperationReplaceGetNew
   Description: Creates a temporary record to store information needed for the mass operation replace process.
   OperationID: MassOperationReplaceGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassOperationReplaceGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassOperationReplaceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeFromOpCode_input:
   """ Required : 
   cFromOpCode
   ds
   """  
   def __init__(self, obj):
      self.cFromOpCode:str = obj["cFromOpCode"]
      """  The proposed from operation code  """  
      self.ds:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["ds"]
      pass

class ChangeFromOpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToOpCode_input:
   """ Required : 
   cToOpCode
   ds
   """  
   def __init__(self, obj):
      self.cToOpCode:str = obj["cToOpCode"]
      """  The proposed To operation code  """  
      self.ds:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["ds"]
      pass

class ChangeToOpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_MassOperationReplaceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FromOpCode:str = obj["FromOpCode"]
      self.FromOpCodeDesc:str = obj["FromOpCodeDesc"]
      self.ToOpCode:str = obj["ToOpCode"]
      self.ToOpCodeDesc:str = obj["ToOpCodeDesc"]
      self.RefreshOpDesc:bool = obj["RefreshOpDesc"]
      """  Indicates whether or not to refresh Operation Description with the new Operation Description.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassOperationReplaceTableset:
   def __init__(self, obj):
      self.MassOperationReplace:list[Erp_Tablesets_MassOperationReplaceRow] = obj["MassOperationReplace"]
      self.MassOperationResults:list[Erp_Tablesets_MassOperationResultsRow] = obj["MassOperationResults"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassOperationResultsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.OprSeq:int = obj["OprSeq"]
      self.AltMethod:str = obj["AltMethod"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class MassOperationReplaceGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["returnObj"]
      pass

class RunMassOperationReplace_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["ds"]
      pass

class RunMassOperationReplace_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassOperationReplaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

