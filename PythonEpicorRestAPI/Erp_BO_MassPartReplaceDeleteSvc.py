import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MassPartReplaceDeleteSvc
# Description: Use this function to dlete Mass Part Replace
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassPartReplaceDeleteSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MassPartReplaceDeleteSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeFromPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromPartNum
   Description: Validates the FromPartNum field and poplutes the From Part description.  Is called when
the From Part Number changes.  If the part is not valid, an exception will be thrown.
   OperationID: ChangeFromPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassPartReplaceDeleteSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToPartNum
   Description: Validates the ToPartNum field and poplutes the To Part description.  Is called when
the To Part Number changes.  If the part is not valid, an exception will be thrown.
   OperationID: ChangeToPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassPartReplaceDeleteSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassPartReplaceDeleteGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassPartReplaceDeleteGetNew
   Description: Creates a temporary record to store information needed for the mass part
replace/delete process.
   OperationID: MassPartReplaceDeleteGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassPartReplaceDeleteGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassPartReplaceDeleteGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassPartReplaceDeleteSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassReplaceDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassReplaceDelete
   Description: Peforms the Mass Replace/Mass Delete of the Part.  The field ActionRequest
determines which action to perform.
   OperationID: MassReplaceDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassReplaceDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassReplaceDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MassPartReplaceDeleteSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeFromPartNum_input:
   """ Required : 
   cFromPartNum
   ds
   """  
   def __init__(self, obj):
      self.cFromPartNum:str = obj["cFromPartNum"]
      """  The proposed from part number  """  
      self.ds:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["ds"]
      pass

class ChangeFromPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToPartNum_input:
   """ Required : 
   cToPartNum
   ds
   """  
   def __init__(self, obj):
      self.cToPartNum:str = obj["cToPartNum"]
      """  The proposed to part number  """  
      self.ds:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["ds"]
      pass

class ChangeToPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_MassPartReplaceDeleteRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FromPartNum:str = obj["FromPartNum"]
      self.FromPartDescription:str = obj["FromPartDescription"]
      self.ToPartNum:str = obj["ToPartNum"]
      self.ToPartDescription:str = obj["ToPartDescription"]
      self.ActionRequest:str = obj["ActionRequest"]
      self.FromPartUOM:str = obj["FromPartUOM"]
      self.ToPartUOM:str = obj["ToPartUOM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassPartReplaceDeleteTableset:
   def __init__(self, obj):
      self.MassPartReplaceDelete:list[Erp_Tablesets_MassPartReplaceDeleteRow] = obj["MassPartReplaceDelete"]
      self.MassPartResults:list[Erp_Tablesets_MassPartResultsRow] = obj["MassPartResults"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassPartResultsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.StatusText:str = obj["StatusText"]
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

class MassPartReplaceDeleteGetNew_input:
   """ Required : 
   cAction
   """  
   def __init__(self, obj):
      self.cAction:str = obj["cAction"]
      """  The action to take: Options are Replace or Delete  """  
      pass

class MassPartReplaceDeleteGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["returnObj"]
      pass

class MassReplaceDelete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["ds"]
      pass

class MassReplaceDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassPartReplaceDeleteTableset] = obj["ds"]
      pass

      """  output parameters  """  

