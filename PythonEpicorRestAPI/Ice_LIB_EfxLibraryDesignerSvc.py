import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.EfxLibraryDesignerSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ApplyChanges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApplyChanges
   OperationID: ApplyChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApplyChangesWithDiagnostics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApplyChangesWithDiagnostics
   OperationID: ApplyChangesWithDiagnostics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyChangesWithDiagnostics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyChangesWithDiagnostics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOwner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOwner
   Description: Changes ownership of specified library to specified user
   OperationID: ChangeOwner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOwner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOwner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaults(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaults
   OperationID: GetDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionInfo
   OperationID: GetFunctionInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionList
   OperationID: GetFunctionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionList2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionList2
   Description: Kinetic REST params do not support FunctionSearchOptions.
   OperationID: GetFunctionList2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLibraryInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLibraryInfo
   OperationID: GetLibraryInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLibraryInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraryInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLibraryList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLibraryList
   Description: Gets a list of libraries.
   OperationID: GetLibraryList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLibraryList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraryList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLibraryList2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLibraryList2
   Description: Gets a list of libraries.
   OperationID: GetLibraryList2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLibraryList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraryList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLibrary
   Description: Finds a library by its ID.
   OperationID: GetLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLibraries(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLibraries
   Description: Gets a list of libraries.
   OperationID: GetLibraries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLibraries_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraries_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DetectCircularReferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DetectCircularReferences
   Description: Method returns true first found circular reference path for the specified library configuration if any.
Otherwise, it returns an empty array.
   OperationID: DetectCircularReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DetectCircularReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetectCircularReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockLibrary
   Description: Locks a library.
   OperationID: LockLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReleaseLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReleaseLibrary
   Description: Releases a library.
   OperationID: ReleaseLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReleaseLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReleaseLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PromoteToProduction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PromoteToProduction
   Description: Promote specified library to production
   OperationID: PromoteToProduction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromoteToProduction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromoteToProduction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DemoteFromProduction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DemoteFromProduction
   Description: Demote the specified library from production to staging
   OperationID: DemoteFromProduction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DemoteFromProduction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DemoteFromProduction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegenerateLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegenerateLibrary
   OperationID: RegenerateLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenerateLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegenerateAllLibraries(epicorHeaders = None):
   """  
   Summary: Invoke method RegenerateAllLibraries
   OperationID: RegenerateAllLibraries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateAllLibraries_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ExportLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportLibrary
   Description: Exports the specified library.
   OperationID: ExportLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportLibrary
   Description: Imports the provided library.
   OperationID: ImportLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InstallLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InstallLibrary
   OperationID: InstallLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InstallLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InstallLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UninstallLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UninstallLibrary
   Description: Removes previously installed library.
   OperationID: UninstallLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UninstallLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UninstallLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DetermineInstallationOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DetermineInstallationOrder
   Description: Tries to order specified library Id from most independent to most dependent.
   OperationID: DetermineInstallationOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DetermineInstallationOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetermineInstallationOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ApplyChangesWithDiagnostics_input:
   """ Required : 
   libraryTableset
   """  
   def __init__(self, obj):
      self.libraryTableset:list[Ice_Tablesets_EfxLibraryTableset] = obj["libraryTableset"]
      pass

class ApplyChangesWithDiagnostics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.libraryTableset:list[Ice_Tablesets_EfxLibraryTableset] = obj["libraryTableset"]
      self.diagnostics:list = obj[any]
      pass

      """  output parameters  """  

class ApplyChanges_input:
   """ Required : 
   input
   """  
   def __init__(self, obj):
      self.input:list[Ice_Tablesets_EfxLibraryTableset] = obj["input"]
      pass

class ApplyChanges_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.input:list[Ice_Tablesets_EfxLibraryTableset] = obj["input"]
      pass

      """  output parameters  """  

class ChangeOwner_input:
   """ Required : 
   libraryId
   userId
   """  
   def __init__(self, obj):
      self.libraryId:str = obj["libraryId"]
      self.userId:str = obj["userId"]
      pass

class ChangeOwner_output:
   def __init__(self, obj):
      pass

class DemoteFromProduction_input:
   """ Required : 
   libraryID
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      pass

class DemoteFromProduction_output:
   def __init__(self, obj):
      pass

class DetectCircularReferences_input:
   """ Required : 
   libraryId
   referencedLibraries
   """  
   def __init__(self, obj):
      self.libraryId:str = obj["libraryId"]
      self.referencedLibraries:str = obj["referencedLibraries"]
      pass

class DetectCircularReferences_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DetermineInstallationOrder_input:
   """ Required : 
   libraryIds
   """  
   def __init__(self, obj):
      self.libraryIds:str = obj["libraryIds"]
      pass

class DetermineInstallationOrder_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of library Ids in the order of installation  """  
      pass

class ExportLibrary_input:
   """ Required : 
   libraryID
   options
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      """  The identifier of the library to export.  """  
      self.options:list[Ice_Lib_EfxLibraryDesigner_ExportOptions] = obj["options"]
      pass

class ExportLibrary_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The binary representation of the library.  """  
      pass

class GetDefaults_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxLibraryTableset] = obj["returnObj"]
      pass

class GetFunctionInfo_input:
   """ Required : 
   options
   """  
   def __init__(self, obj):
      self.options:list[Ice_Lib_EfxLibraryDesigner_FunctionInfoSearchOptions] = obj["options"]
      pass

class GetFunctionInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_EfxLibraryDesigner_FunctionInfoDto] = obj["returnObj"]
      pass

class GetFunctionList2_input:
   """ Required : 
   libraryID
   kind
   functionIDStartsWith
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      self.kind:int = obj["kind"]
      self.functionIDStartsWith:str = obj["functionIDStartsWith"]
      pass

class GetFunctionList2_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxFunctionSearchTableset] = obj["returnObj"]
      pass

class GetFunctionList_input:
   """ Required : 
   options
   """  
   def __init__(self, obj):
      self.options:list[Ice_Lib_EfxLibraryDesigner_FunctionSearchOptions] = obj["options"]
      pass

class GetFunctionList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxFunctionSearchTableset] = obj["returnObj"]
      pass

class GetLibraries_input:
   """ Required : 
   libraryIds
   """  
   def __init__(self, obj):
      self.libraryIds:str = obj["libraryIds"]
      """  the array of library ID's.  """  
      pass

class GetLibraries_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxLibraryTableset] = obj["returnObj"]
      pass

class GetLibraryInfo_input:
   """ Required : 
   options
   """  
   def __init__(self, obj):
      self.options:list[Ice_Lib_EfxLibraryDesigner_LibraryInfoSearchOptions] = obj["options"]
      pass

class GetLibraryInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_EfxLibraryDesigner_LibraryInfoDto] = obj["returnObj"]
      pass

class GetLibraryList2_input:
   """ Required : 
   startsWith
   kind
   rollOutMode
   status
   """  
   def __init__(self, obj):
      self.startsWith:str = obj["startsWith"]
      """  library ID starts with  """  
      self.kind:int = obj["kind"]
      """  library kind.  """  
      self.rollOutMode:int = obj["rollOutMode"]
      """  the rollout mode.  """  
      self.status:int = obj["status"]
      """  library status.  """  
      pass

class GetLibraryList2_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxLibrarySearchTableset] = obj["returnObj"]
      pass

class GetLibraryList_input:
   """ Required : 
   options
   """  
   def __init__(self, obj):
      self.options:list[Ice_Lib_EfxLibraryDesigner_LibrarySearchOptions] = obj["options"]
      pass

class GetLibraryList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxLibrarySearchTableset] = obj["returnObj"]
      pass

class GetLibrary_input:
   """ Required : 
   libraryId
   """  
   def __init__(self, obj):
      self.libraryId:str = obj["libraryId"]
      """  the library ID.  """  
      pass

class GetLibrary_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EfxLibraryTableset] = obj["returnObj"]
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Ice_Lib_EfxLibraryDesigner_ExportOptions:
   def __init__(self, obj):
      self.Mode:int = obj["Mode"]
      self.Format:int = obj["Format"]
      self.Package:str = obj["Package"]
      self.PackageVersion:str = obj["PackageVersion"]
      self.Publisher:str = obj["Publisher"]
      self.InstallAsHidden:bool = obj["InstallAsHidden"]
      pass

class Ice_Lib_EfxLibraryDesigner_FunctionInfoDto:
   def __init__(self, obj):
      self.LibraryId:str = obj["LibraryId"]
      self.FunctionId:str = obj["FunctionId"]
      self.Disabled:bool = obj["Disabled"]
      self.SignatureData:list[Ice_Lib_EfxLibraryDesigner_FunctionSignatureItem] = obj["SignatureData"]
      self.Description:str = obj["Description"]
      self.Kind:int = obj["Kind"]
      pass

class Ice_Lib_EfxLibraryDesigner_FunctionInfoSearchOptions:
   def __init__(self, obj):
      self.kind:int = obj["kind"]
      self.libraryId:str = obj["libraryId"]
      self.functionId:str = obj["functionId"]
      pass

class Ice_Lib_EfxLibraryDesigner_FunctionSearchOptions:
   def __init__(self, obj):
      self.kind:int = obj["kind"]
      self.libraryID:str = obj["libraryID"]
      self.functionIDStartsWith:str = obj["functionIDStartsWith"]
      pass

class Ice_Lib_EfxLibraryDesigner_FunctionSignatureItem:
   def __init__(self, obj):
      self.Response:bool = obj["Response"]
      self.ParameterID:int = obj["ParameterID"]
      self.ArgumentName:str = obj["ArgumentName"]
      self.Order:int = obj["Order"]
      self.DataType:str = obj["DataType"]
      self.DataTypeInfo:str = obj["DataTypeInfo"]
      pass

class Ice_Lib_EfxLibraryDesigner_ImportOptions:
   def __init__(self, obj):
      self.NewLibraryId:str = obj["NewLibraryId"]
      self.OverwriteMode:int = obj["OverwriteMode"]
      pass

class Ice_Lib_EfxLibraryDesigner_InstallOptions:
   def __init__(self, obj):
      self.AllowUpgrade:bool = obj["AllowUpgrade"]
      self.EnableIn:int = obj["EnableIn"]
      pass

class Ice_Lib_EfxLibraryDesigner_LibraryInfoDto:
   def __init__(self, obj):
      self.LibraryId:str = obj["LibraryId"]
      self.Disabled:bool = obj["Disabled"]
      self.Functions:list[Ice_Lib_EfxLibraryDesigner_FunctionInfoDto] = obj["Functions"]
      pass

class Ice_Lib_EfxLibraryDesigner_LibraryInfoSearchOptions:
   def __init__(self, obj):
      self.libraryId:str = obj["libraryId"]
      pass

class Ice_Lib_EfxLibraryDesigner_LibrarySearchOptions:
   def __init__(self, obj):
      self.kind:int = obj["kind"]
      self.startsWith:str = obj["startsWith"]
      self.rollOutMode:int = obj["rollOutMode"]
      self.status:int = obj["status"]
      pass

class Ice_Tablesets_EfxFunctionListRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      self.FunctionID:str = obj["FunctionID"]
      self.Description:str = obj["Description"]
      """  Short function description  """  
      self.Kind:int = obj["Kind"]
      """  Type of function: widget-based, widget-based with custom code, code-based  """  
      self.Private:bool = obj["Private"]
      """  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  """  
      self.Disabled:bool = obj["Disabled"]
      """  Function activity status  """  
      self.Invalid:bool = obj["Invalid"]
      """  Flags determines whether stored function valid or not  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxFunctionRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      self.FunctionID:str = obj["FunctionID"]
      """  Function ID  """  
      self.Description:str = obj["Description"]
      """  Short function description  """  
      self.Kind:int = obj["Kind"]
      """  Type of function: widget-based, widget-based with custom code, code-based  """  
      self.RequireTransaction:bool = obj["RequireTransaction"]
      """  Flag determines whether the function requires transaction or not  """  
      self.SingleRowMode:bool = obj["SingleRowMode"]
      """  Flag allows enabling the legacy single dirty row mode  """  
      self.Private:bool = obj["Private"]
      """  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  """  
      self.Disabled:bool = obj["Disabled"]
      """  Function activity status  """  
      self.Invalid:bool = obj["Invalid"]
      """  Flags determines whether stored function valid or not  """  
      self.Thumbnail:str = obj["Thumbnail"]
      """  Preview of widget-based function  """  
      self.Body:str = obj["Body"]
      """  Serialized function's body  """  
      self.Notes:str = obj["Notes"]
      """  Function-level notes  """  
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxFunctionSearchTableset:
   def __init__(self, obj):
      self.EfxFunctionList:list[Ice_Tablesets_EfxFunctionListRow] = obj["EfxFunctionList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_EfxFunctionSignatureRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      self.FunctionID:str = obj["FunctionID"]
      self.Response:bool = obj["Response"]
      """  Flag determines kind of parameter: request or response  """  
      self.ParameterID:int = obj["ParameterID"]
      """  Internal parameter id (part of PK)  """  
      self.ArgumentName:str = obj["ArgumentName"]
      self.Order:int = obj["Order"]
      self.DataType:str = obj["DataType"]
      """  Full qualified .NET type name  """  
      self.DataTypeInfo:str = obj["DataTypeInfo"]
      """  Additional data type information  """  
      self.Optional:bool = obj["Optional"]
      """  Flag determines whether a parameter is mandatory or can be omitte  """  
      self.DefaultValue:str = obj["DefaultValue"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxLibraryListRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      self.Description:str = obj["Description"]
      """  Short library description  """  
      self.Published:bool = obj["Published"]
      """  Flag determines is library published for the production or is in staging mode  """  
      self.Private:bool = obj["Private"]
      """  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  """  
      self.OwnedByCompany:str = obj["OwnedByCompany"]
      """  Company where the library was created or imported  """  
      self.Disabled:bool = obj["Disabled"]
      """  Library activity status  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Library cannot be edit by the current user  """  
      self.LockedBy:str = obj["LockedBy"]
      """  Library exlusively locked by the user  """  
      self.SysRowID:str = obj["SysRowID"]
      self.Mode:int = obj["Mode"]
      """  Installation mode  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxLibraryMappingRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      self.Company:str = obj["Company"]
      self.Allowed:bool = obj["Allowed"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxLibraryRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      """  Unique user-friendly Library Identifier  """  
      self.OriginalID:str = obj["OriginalID"]
      """  Original library ID specified during development  """  
      self.Description:str = obj["Description"]
      """  Short description of library  """  
      self.GlobalID:str = obj["GlobalID"]
      """  Internal unique library reference ID  """  
      self.EpicorVersion:str = obj["EpicorVersion"]
      """  Version of a product used to build library  """  
      self.Revision:int = obj["Revision"]
      """  Library version  """  
      self.Published:bool = obj["Published"]
      """  Flag determines is library published for the production or is in staging mode  """  
      self.Private:bool = obj["Private"]
      """  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  """  
      self.Disabled:bool = obj["Disabled"]
      """  Library activity status  """  
      self.Mode:int = obj["Mode"]
      """  Installation mode  """  
      self.Frozen:bool = obj["Frozen"]
      """  Flag determining the ability to change the library  """  
      self.AllowCustomCodeWidgets:bool = obj["AllowCustomCodeWidgets"]
      """  Flag determining the ability to add widget-based functions with custom code elements  """  
      self.AllowCustomCodeFunctions:bool = obj["AllowCustomCodeFunctions"]
      """  Flag determining the ability to add custom code-base functions  """  
      self.DirectDBAccess:int = obj["DirectDBAccess"]
      """  Allowed direct DB access mode in C# code: node, read-only, and read-write  """  
      self.OwnedByCompany:str = obj["OwnedByCompany"]
      """  Company where the library was created or imported  """  
      self.Owner:str = obj["Owner"]
      """  Library maintainer's ID  """  
      self.SharedWithGroup:str = obj["SharedWithGroup"]
      """  Library maintainers group  """  
      self.Notes:str = obj["Notes"]
      """  Library-levele notes  """  
      self.Package:str = obj["Package"]
      """  Library is part of this project  """  
      self.PackageVersion:str = obj["PackageVersion"]
      """  Version of packge containing the library  """  
      self.Publisher:str = obj["Publisher"]
      """  Library provided by the publisher  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Row version column  """  
      self.SysRowID:str = obj["SysRowID"]
      self.DebugMode:bool = obj["DebugMode"]
      """  Enables (true) or disables (false) the debug mode of EFx library build  """  
      self.DumpSources:bool = obj["DumpSources"]
      """  Enables (true) or disables (false) the storing of the generated sources of an EFx library on the server  """  
      self.AdvTracing:bool = obj["AdvTracing"]
      """  Enables (true) or disables (false) advanced tracing for an EFx library  """  
      self.LockedBy:str = obj["LockedBy"]
      """  Library exlusively locked by the user  """  
      self.LockedOn:str = obj["LockedOn"]
      self.LockedFrom:str = obj["LockedFrom"]
      """  Library locked for edit from the specific workstation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxLibrarySearchTableset:
   def __init__(self, obj):
      self.EfxLibraryList:list[Ice_Tablesets_EfxLibraryListRow] = obj["EfxLibraryList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_EfxLibraryTableset:
   def __init__(self, obj):
      self.EfxLibrary:list[Ice_Tablesets_EfxLibraryRow] = obj["EfxLibrary"]
      self.EfxFunction:list[Ice_Tablesets_EfxFunctionRow] = obj["EfxFunction"]
      self.EfxFunctionSignature:list[Ice_Tablesets_EfxFunctionSignatureRow] = obj["EfxFunctionSignature"]
      self.EfxLibraryMapping:list[Ice_Tablesets_EfxLibraryMappingRow] = obj["EfxLibraryMapping"]
      self.EfxRefAssembly:list[Ice_Tablesets_EfxRefAssemblyRow] = obj["EfxRefAssembly"]
      self.EfxRefLibrary:list[Ice_Tablesets_EfxRefLibraryRow] = obj["EfxRefLibrary"]
      self.EfxRefService:list[Ice_Tablesets_EfxRefServiceRow] = obj["EfxRefService"]
      self.EfxRefTable:list[Ice_Tablesets_EfxRefTableRow] = obj["EfxRefTable"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_EfxRefAssemblyRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      """  Library ID  """  
      self.Assembly:str = obj["Assembly"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxRefLibraryRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      """  Id of the current library  """  
      self.LibraryRef:str = obj["LibraryRef"]
      """  Id of a referenced library  """  
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Mode:int = obj["Mode"]
      """  Refernced library mode (0  -Normal, 1 - ReadOnly (Installed), 2 - Hidden (Installed as Hidden))  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxRefServiceRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      """  Library ID  """  
      self.ServiceID:str = obj["ServiceID"]
      """  Epicor Service ID  """  
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfxRefTableRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      """  Library ID  """  
      self.TableID:str = obj["TableID"]
      """  DB Table ID  """  
      self.Updatable:bool = obj["Updatable"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ImportLibrary_input:
   """ Required : 
   libraryPackage
   options
   """  
   def __init__(self, obj):
      self.libraryPackage:str = obj["libraryPackage"]
      """  The binary representation of the library.  """  
      self.options:list[Ice_Lib_EfxLibraryDesigner_ImportOptions] = obj["options"]
      pass

class ImportLibrary_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

class InstallLibrary_input:
   """ Required : 
   libraryPackage
   options
   """  
   def __init__(self, obj):
      self.libraryPackage:str = obj["libraryPackage"]
      self.options:list[Ice_Lib_EfxLibraryDesigner_InstallOptions] = obj["options"]
      pass

class InstallLibrary_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

class LockLibrary_input:
   """ Required : 
   libraryID
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      pass

class LockLibrary_output:
   def __init__(self, obj):
      pass

class PromoteToProduction_input:
   """ Required : 
   libraryID
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      pass

class PromoteToProduction_output:
   def __init__(self, obj):
      pass

class RegenerateAllLibraries_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

class RegenerateLibrary_input:
   """ Required : 
   libraryID
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      pass

class RegenerateLibrary_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

class ReleaseLibrary_input:
   """ Required : 
   libraryID
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      pass

class ReleaseLibrary_output:
   def __init__(self, obj):
      pass

class UninstallLibrary_input:
   """ Required : 
   libraryId
   """  
   def __init__(self, obj):
      self.libraryId:str = obj["libraryId"]
      pass

class UninstallLibrary_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

