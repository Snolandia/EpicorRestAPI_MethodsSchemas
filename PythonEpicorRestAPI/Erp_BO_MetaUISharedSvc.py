import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MetaUISharedSvc
# Description: MetaUIShared BO for shared logic needed by metaUI clients
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetCurrentDateAndTime(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentDateAndTime
   Description: GetCurrentDateAndTime
Returns current date and time information from server
   OperationID: GetCurrentDateAndTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentDateAndTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetFeatureAvailable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFeatureAvailable
   Description: Returns true if the feature flag is enabled.
   OperationID: GetFeatureAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFeatureAvailable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFeatureAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRandom(epicorHeaders = None):
   """  
   Summary: Invoke method GetRandom
   Description: GetRandom
Returns random guid string and random integer
   OperationID: GetRandom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRandom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetUISettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUISettings
   Description: Gets UI/User specific setting string
   OperationID: GetUISettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUISettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUISettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUISettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUISettings
   Description: Sets UI/User specific setting string
   OperationID: SetUISettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUISettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUISettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddDay
   Description: Returns a date + 1 day. Created for use in Process Review Kinetic Conversion.
   OperationID: AddDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateDate
   Description: Returns date.
   OperationID: GenerateDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUISharedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddDay_input:
   """ Required : 
   day
   numDays
   """  
   def __init__(self, obj):
      self.day:str = obj["day"]
      self.numDays:int = obj["numDays"]
      pass

class AddDay_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Erp_Tablesets_MetaUISharedRow:
   def __init__(self, obj):
      self.CurrentDate:str = obj["CurrentDate"]
      self.SecondsSinceMidnight:int = obj["SecondsSinceMidnight"]
      self.LongTimeString:str = obj["LongTimeString"]
      self.ShortTimeString:str = obj["ShortTimeString"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MetaUISharedTableset:
   def __init__(self, obj):
      self.MetaUIShared:list[Erp_Tablesets_MetaUISharedRow] = obj["MetaUIShared"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateDate_input:
   """ Required : 
   year
   month
   day
   """  
   def __init__(self, obj):
      self.year:int = obj["year"]
      self.month:int = obj["month"]
      self.day:int = obj["day"]
      pass

class GenerateDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrentDateAndTime_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MetaUISharedTableset] = obj["returnObj"]
      pass

class GetFeatureAvailable_input:
   """ Required : 
   featureFlag
   """  
   def __init__(self, obj):
      self.featureFlag:str = obj["featureFlag"]
      """  The name if the feature flag  """  
      pass

class GetFeatureAvailable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetRandom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.randomString:str = obj["parameters"]
      self.randomInt:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetUISettings_input:
   """ Required : 
   assemblyName
   """  
   def __init__(self, obj):
      self.assemblyName:str = obj["assemblyName"]
      pass

class GetUISettings_output:
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

class SetUISettings_input:
   """ Required : 
   assemblyName
   value
   """  
   def __init__(self, obj):
      self.assemblyName:str = obj["assemblyName"]
      self.value:str = obj["value"]
      pass

class SetUISettings_output:
   def __init__(self, obj):
      pass

