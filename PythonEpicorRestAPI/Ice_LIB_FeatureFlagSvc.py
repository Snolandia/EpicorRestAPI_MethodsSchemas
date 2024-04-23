import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.FeatureFlagSvc
# Description: Service for managing feature flags.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_EnableFeature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableFeature
   Description: Enable a feature.
   OperationID: EnableFeature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableFeature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableFeature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisableFeature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisableFeature
   Description: Disable a feature.
   OperationID: DisableFeature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableFeature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableFeature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEnabledFeatures(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEnabledFeatures
   Description: Get the list of enabled features.
   OperationID: GetEnabledFeatures
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEnabledFeatures_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnabledFeatures_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DisableFeature_input:
   """ Required : 
   featureID
   level
   target
   """  
   def __init__(self, obj):
      self.featureID:str = obj["featureID"]
      """  Feature flag identifier.  """  
      self.level:int = obj["level"]
      """  Level at which the feature flag is to be disabled.  """  
      self.target:str = obj["target"]
      """  The identifier for the level at which the flag applies. One of TenantID, Company, SecGroupCode, UserID. Ignored for level System.  """  
      pass

class DisableFeature_output:
   def __init__(self, obj):
      pass

class EnableFeature_input:
   """ Required : 
   featureID
   level
   target
   """  
   def __init__(self, obj):
      self.featureID:str = obj["featureID"]
      """  Feature flag identifier.  """  
      self.level:int = obj["level"]
      """  Level at which the feature flag is to be enabled.  """  
      self.target:str = obj["target"]
      """  The identifier for the level at which the flag applies. One of TenantID, Company, SecGroupCode, UserID. Ignored for level System.  """  
      pass

class EnableFeature_output:
   def __init__(self, obj):
      pass

class GetEnabledFeatures_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier for which to retrieve the enabled feature flags or null for all users.  """  
      pass

class GetEnabledFeatures_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FeatureFlagTableset] = obj["returnObj"]
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

class Ice_Tablesets_EnabledFeatureRow:
   def __init__(self, obj):
      self.FeatureID:str = obj["FeatureID"]
      """  FeatureID  """  
      self.Level:int = obj["Level"]
      """  Level  """  
      self.Target:str = obj["Target"]
      """  Target  """  
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_FeatureFlagTableset:
   def __init__(self, obj):
      self.EnabledFeature:list[Ice_Tablesets_EnabledFeatureRow] = obj["EnabledFeature"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

