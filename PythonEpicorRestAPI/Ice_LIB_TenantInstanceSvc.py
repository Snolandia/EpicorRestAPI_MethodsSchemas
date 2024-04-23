import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.TenantInstanceSvc
# Description: Provides information about a tenant instance.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.TenantInstanceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.TenantInstanceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CanRestartAppServers(epicorHeaders = None):
   """  
   Summary: Invoke method CanRestartAppServers
   Description: Returns a value that indicates whether the AppServers can safely be restarted at this moment.
   OperationID: CanRestartAppServers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanRestartAppServers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TenantInstanceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetInstanceDefinition(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstanceDefinition
   Description: Gets the tenant instance definition.
   OperationID: GetInstanceDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstanceDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TenantInstanceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetDatabaseValues(epicorHeaders = None):
   """  
   Summary: Invoke method GetDatabaseValues
   Description: Get values from the database.
   OperationID: GetDatabaseValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatabaseValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TenantInstanceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CanRestartAppServers_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.reason:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDatabaseValues_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_TenantInstance_DatabaseValues] = obj["returnObj"]
      pass

class GetInstanceDefinition_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_TenantInstance_InstanceDefinition] = obj["returnObj"]
      pass

class Ice_Lib_TenantInstance_DatabaseValues:
   def __init__(self, obj):
      self.FileRootDir:str = obj["FileRootDir"]
      self.SysAgentPassword:str = obj["SysAgentPassword"]
      self.EddUrl:str = obj["EddUrl"]
      self.WinWebUrl:str = obj["WinWebUrl"]
      self.MetadataPath:str = obj["MetadataPath"]
      self.EpicAdminPassword:str = obj["EpicAdminPassword"]
      self.ProviderID:str = obj["ProviderID"]
      self.ScimClientSecret:str = obj["ScimClientSecret"]
      self.NativeClientID:str = obj["NativeClientID"]
      self.WebClientID:str = obj["WebClientID"]
      self.ServerOnlyClientID:str = obj["ServerOnlyClientID"]
      self.ServerOnlyClientSecret:str = obj["ServerOnlyClientSecret"]
      self.ScimClientID:str = obj["ScimClientID"]
      self.DirectoryID:str = obj["DirectoryID"]
      self.WebAppID:str = obj["WebAppID"]
      self.TenantID:str = obj["TenantID"]
      self.Description:str = obj["Description"]
      self.NativeClientAppID:str = obj["NativeClientAppID"]
      self.ClaimName:str = obj["ClaimName"]
      self.UseAsDefaultApp:bool = obj["UseAsDefaultApp"]
      self.SysRowID:str = obj["SysRowID"]
      self.PersistentLogin:bool = obj["PersistentLogin"]
      pass

class Ice_Lib_TenantInstance_InstanceDefinition:
   def __init__(self, obj):
      self.MachineName:str = obj["MachineName"]
      self.AppPoolName:str = obj["AppPoolName"]
      self.PID:str = obj["PID"]
      self.Details      #schema had no properties on an object.
      pass

