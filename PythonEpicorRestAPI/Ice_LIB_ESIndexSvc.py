import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.ESIndexSvc
# Description: ESIndex service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CreateIndex(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateIndex
   Description: Creates an index in Enterprise Search.
   OperationID: CreateIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifyIndex(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifyIndex
   Description: Modifies an existing index in Enterprise Search.
   OperationID: ModifyIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildIndex(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildIndex
   Description: Builds an index in Enterprise Search.
   OperationID: BuildIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteIndex(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteIndex
   Description: Deletes an index from Enterprise Search.
   OperationID: DeleteIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIndex(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIndex
   Description: Gets the index details with the indexed BAQ's from Enterprise Search.
<param name="indexName">index name.</param>
   OperationID: GetIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBuildLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBuildLog
   Description: Gets a build log by its id.
   OperationID: GetBuildLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBuildLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBuildLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteBuildLogToFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteBuildLogToFile
   Description: Gets the build log by its id from Enterprise Search service and saves it in User data shared folder.
The file name is the build log id with .log extension.
   OperationID: WriteBuildLogToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteBuildLogToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteBuildLogToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBuildHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBuildHistory
   Description: Gets a list of the builds per index.
   OperationID: GetBuildHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBuildHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBuildHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllIndexes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAllIndexes
   Description: Gets a list of available indexes in Enterprise Search.
   OperationID: GetAllIndexes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllIndexes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetTemplates(epicorHeaders = None):
   """  
   Summary: Invoke method GetTemplates
   Description: Gets a list of available templates in Enterprise Search.
   OperationID: GetTemplates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTemplates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableCompanies(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableCompanies
   Description: Gets a list of available companies.
   OperationID: GetAvailableCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSearchableBaqs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSearchableBaqs
   Description: Gets a list of shared BAQ's that are NOT cross-company.
   OperationID: GetSearchableBaqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSearchableBaqs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchableBaqs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLikeLinks(epicorHeaders = None):
   """  
   Summary: Invoke method GetLikeLinks
   Description: Gets a list of like links.
   OperationID: GetLikeLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLikeLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_RefreshBaqs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshBaqs
   Description: Refreshes the list of BAQ's.
   OperationID: RefreshBaqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshBaqs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBaqs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshBaqList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshBaqList
   Description: Refreshes the list of BAQ's.
   OperationID: RefreshBaqList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshBaqList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBaqList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBaq
   Description: Validates the list of BAQ's.
   OperationID: ValidateBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAllBaqs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAllBaqs
   Description: Validates all the BAQ's in an index.
   OperationID: ValidateAllBaqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAllBaqs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAllBaqs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteBaq
   Description: Deletes a BAQ from the list of indexed BAQ's in Enterprise Search.
   OperationID: DeleteBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddBaq
   Description: Adds a BAQ to the list of indexed BAQ's in Enterprise Search.
   OperationID: AddBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBaqTuning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBaqTuning
   Description: Gets the BAQ tuning settings.
   OperationID: GetBaqTuning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBaqTuning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaqTuning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBaqTuning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBaqTuning
   Description: Updates the BAQ tuning settings.
   OperationID: UpdateBaqTuning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBaqTuning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqTuning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunBAQValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunBAQValidation
   Description: Validates a BAQ.
   OperationID: RunBAQValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunBAQValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunBAQValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunAllBAQValidations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunAllBAQValidations
   Description: Validates all the BAQ's in an index.
   OperationID: RunAllBAQValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunAllBAQValidations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunAllBAQValidations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Adds and updates any modified rows (ESIndex and ESIndexBAQ tables).
ESIndexBAQField can't have fields added (it comes from the BAQ definition).
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssertUserCanAccess(epicorHeaders = None):
   """  
   Summary: Invoke method AssertUserCanAccess
   Description: Checks if the user can access ESIndex methods.
   OperationID: AssertUserCanAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssertUserCanAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddBaq_input:
   """ Required : 
   indexName
   queryId
   company
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      self.queryId:str = obj["queryId"]
      """  query Id.  """  
      self.company:str = obj["company"]
      """  company.  """  
      pass

class AddBaq_output:
   def __init__(self, obj):
      pass

class AssertUserCanAccess_output:
   def __init__(self, obj):
      pass

class BuildIndex_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      pass

class BuildIndex_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CreateIndex_input:
   """ Required : 
   indexTableset
   """  
   def __init__(self, obj):
      self.indexTableset:list[Ice_Tablesets_ESIndexTableset] = obj["indexTableset"]
      pass

class CreateIndex_output:
   def __init__(self, obj):
      pass

class DeleteBaq_input:
   """ Required : 
   indexName
   queryId
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      self.queryId:str = obj["queryId"]
      """  query Id.  """  
      pass

class DeleteBaq_output:
   def __init__(self, obj):
      pass

class DeleteIndex_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      pass

class DeleteIndex_output:
   def __init__(self, obj):
      pass

class GetAllIndexes_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexTableset] = obj["returnObj"]
      pass

class GetAvailableCompanies_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetBaqTuning_input:
   """ Required : 
   indexTableset
   indexName
   queryId
   """  
   def __init__(self, obj):
      self.indexTableset:list[Ice_Tablesets_ESIndexTableset] = obj["indexTableset"]
      self.indexName:str = obj["indexName"]
      """  the index name.  """  
      self.queryId:str = obj["queryId"]
      """  the query id.  """  
      pass

class GetBaqTuning_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexTableset] = obj["returnObj"]
      pass

class GetBuildHistory_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      pass

class GetBuildHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexTableset] = obj["returnObj"]
      pass

class GetBuildLog_input:
   """ Required : 
   buildLogId
   """  
   def __init__(self, obj):
      self.buildLogId:str = obj["buildLogId"]
      """  the build log identifier.  """  
      pass

class GetBuildLog_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetIndex_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      pass

class GetIndex_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexTableset] = obj["returnObj"]
      pass

class GetLikeLinks_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSearchableBaqs_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      pass

class GetSearchableBaqs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexTableset] = obj["returnObj"]
      pass

class GetTemplates_output:
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

class Ice_Lib_ESIndex_Model_SearchIndexBAQ:
   def __init__(self, obj):
      self.QueryId:str = obj["QueryId"]
      pass

class Ice_Tablesets_ESIndexBAQFieldRow:
   def __init__(self, obj):
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field name.  """  
      self.TitlePosition:int = obj["TitlePosition"]
      """  BAQ Field title position.  """  
      self.KeyPosition:int = obj["KeyPosition"]
      """  BAQ key tag position.  """  
      self.IsIndexed:bool = obj["IsIndexed"]
      """  If BAQ Field is included in the index.  """  
      self.ShowInThumbnail:bool = obj["ShowInThumbnail"]
      """  If BAQ field is shown in search results.  """  
      self.HideIfDefaultValue:bool = obj["HideIfDefaultValue"]
      """  If BAQ field should be hidden if it has its default value.  """  
      self.Alias:str = obj["Alias"]
      """  BAQ Field alias.  """  
      self.SearchIndexName:str = obj["SearchIndexName"]
      """  Search index name.  """  
      self.QueryID:str = obj["QueryID"]
      """  Business Activity Query ID.  """  
      self.IsSurrogateKeyField:bool = obj["IsSurrogateKeyField"]
      """  If the field is part of the surrogate key.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field label.  """  
      self.FieldType:str = obj["FieldType"]
      """  Field type.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  The field format.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  The source database schema name.  """  
      self.DBTableName:str = obj["DBTableName"]
      """  The source database table name.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Row unique identifier.  """  
      self.LikeField:str = obj["LikeField"]
      """  Like Field.  """  
      self.SourceLikeField:str = obj["SourceLikeField"]
      """  BAQ Like Field.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESIndexBAQRow:
   def __init__(self, obj):
      self.SearchIndexName:str = obj["SearchIndexName"]
      """  Search index name.  """  
      self.QueryID:str = obj["QueryID"]
      """  Business Activity Query ID.  """  
      self.Company:str = obj["Company"]
      """  BAQ Company.  """  
      self.TitleTemplate:str = obj["TitleTemplate"]
      """  BAQ table title template.  """  
      self.PluralDescription:str = obj["PluralDescription"]
      """  BAQ Table plural description.  """  
      self.Ranking:int = obj["Ranking"]
      """  BAQ table ranking.  """  
      self.PrimaryTable:str = obj["PrimaryTable"]
      """  BAQ primary table.  """  
      self.LikeField:str = obj["LikeField"]
      """  BAQ like field.  """  
      self.Tags:str = obj["Tags"]
      """  BAQ Tags (search keywords).  """  
      self.DisplayName:str = obj["DisplayName"]
      """  BAQ display name.  """  
      self.QueryDescription:str = obj["QueryDescription"]
      """  BAQ Description.  """  
      self.ExternalQuery:bool = obj["ExternalQuery"]
      """  If it is an external query.  """  
      self.UpdatableQuery:bool = obj["UpdatableQuery"]
      """  If the query is updatable.  """  
      self.QueryPhrase:str = obj["QueryPhrase"]
      """  Query display phrase.  """  
      self.FileChecksum:str = obj["FileChecksum"]
      """  The tuning file checksum used for concurrency.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Row unique identifier.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESIndexBAQTableRow:
   def __init__(self, obj):
      self.DBTableName:str = obj["DBTableName"]
      """  The source database table name.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  The source database schema name.  """  
      self.IsTempTable:bool = obj["IsTempTable"]
      """  If it is a temporary table.  """  
      self.IsSummaryTable:bool = obj["IsSummaryTable"]
      """  If it is a summary table.  """  
      self.TableName:str = obj["TableName"]
      """  The table name.  """  
      self.QueryID:str = obj["QueryID"]
      """  Business Activity Query ID.  """  
      self.SearchIndexName:str = obj["SearchIndexName"]
      """  Search index name.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Row unique identifier.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESIndexLogRow:
   def __init__(self, obj):
      self.BuildID:str = obj["BuildID"]
      """  The build ID.  """  
      self.CrawlRecords:int = obj["CrawlRecords"]
      """  The build number of crawl records.  """  
      self.DistinctWords:int = obj["DistinctWords"]
      """  The build number of distinct words.  """  
      self.TotalDuration:int = obj["TotalDuration"]
      """  The build duration.  """  
      self.Exceptions:int = obj["Exceptions"]
      """  The build number of errors.  """  
      self.RecordCount:int = obj["RecordCount"]
      """  The build number of records.  """  
      self.SearchIndexName:str = obj["SearchIndexName"]
      """  Search Index Name in Enterprise Search  """  
      self.Start:str = obj["Start"]
      """  The build start time.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Row unique identifier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESIndexRow:
   def __init__(self, obj):
      self.SearchIndexName:str = obj["SearchIndexName"]
      """  Search Index Name in Enterprise Search  """  
      self.TemplateName:str = obj["TemplateName"]
      """  Template to use for indexing.  """  
      self.CompanyList:str = obj["CompanyList"]
      """  List of companies to include in the index.  """  
      self.AzureDirectoryID:str = obj["AzureDirectoryID"]
      """  Azure Directory ID.  """  
      self.AzureNativeAppID:str = obj["AzureNativeAppID"]
      """  Azure Native App ID.  """  
      self.AzureWebAppID:str = obj["AzureWebAppID"]
      """  Azure Web App ID.  """  
      self.DNSIdentity:str = obj["DNSIdentity"]
      """  App server DNS identity.  """  
      self.EpicorPassword:str = obj["EpicorPassword"]
      """  Password to connect to app server.  """  
      self.EpicorUser:str = obj["EpicorUser"]
      """  User to connect to app server.  """  
      self.OperationTimeout:int = obj["OperationTimeout"]
      """  The app server operation timeout  """  
      self.UseCertificate:bool = obj["UseCertificate"]
      """  If certiicate should be validated when connecting to the app server.  """  
      self.AppServerURL:str = obj["AppServerURL"]
      """  App server URL.  """  
      self.SearchURL:str = obj["SearchURL"]
      """  Search Index URL.  """  
      self.Status:str = obj["Status"]
      """  Search index build status.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Row unique identifier  """  
      self.AuthenticationMode:str = obj["AuthenticationMode"]
      """  App server authentication mode.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESIndexTableset:
   def __init__(self, obj):
      self.ESIndex:list[Ice_Tablesets_ESIndexRow] = obj["ESIndex"]
      self.ESIndexBAQ:list[Ice_Tablesets_ESIndexBAQRow] = obj["ESIndexBAQ"]
      self.ESIndexBAQField:list[Ice_Tablesets_ESIndexBAQFieldRow] = obj["ESIndexBAQField"]
      self.ESIndexBAQTable:list[Ice_Tablesets_ESIndexBAQTableRow] = obj["ESIndexBAQTable"]
      self.ESIndexLog:list[Ice_Tablesets_ESIndexLogRow] = obj["ESIndexLog"]
      self.SearchableBAQ:list[Ice_Tablesets_SearchableBAQRow] = obj["SearchableBAQ"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ESIndexValidationTableset:
   def __init__(self, obj):
      self.ValidationResult:list[Ice_Tablesets_ValidationResultRow] = obj["ValidationResult"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SearchableBAQRow:
   def __init__(self, obj):
      self.QueryID:str = obj["QueryID"]
      """  Query ID.  """  
      self.Company:str = obj["Company"]
      """  BAQ Company.  """  
      self.Description:str = obj["Description"]
      """  BAQ Description.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ValidationResultRow:
   def __init__(self, obj):
      self.QueryID:str = obj["QueryID"]
      """  Business Activity Query ID.  """  
      self.ValidationRule:str = obj["ValidationRule"]
      """  Validation rule name.  """  
      self.Result:bool = obj["Result"]
      """  The result of the validation rule (if it passed).  """  
      self.Details:str = obj["Details"]
      """  In case of failure, the reason or details.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID. Row unique identifier.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ModifyIndex_input:
   """ Required : 
   indexTableset
   """  
   def __init__(self, obj):
      self.indexTableset:list[Ice_Tablesets_ESIndexTableset] = obj["indexTableset"]
      pass

class ModifyIndex_output:
   def __init__(self, obj):
      pass

class RefreshBaqList_input:
   """ Required : 
   indexName
   queriesToRefresh
   company
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      self.queriesToRefresh:list[Ice_Lib_ESIndex_Model_SearchIndexBAQ] = obj["queriesToRefresh"]
      """  array of BAQ's to refresh  """  
      self.company:str = obj["company"]
      """  company  """  
      pass

class RefreshBaqList_output:
   def __init__(self, obj):
      pass

class RefreshBaqs_input:
   """ Required : 
   indexName
   queriesToRefresh
   company
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      self.queriesToRefresh:str = obj["queriesToRefresh"]
      """  BAQ's to refresh, or null or empty  """  
      self.company:str = obj["company"]
      """  company  """  
      pass

class RefreshBaqs_output:
   def __init__(self, obj):
      pass

class RunAllBAQValidations_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      pass

class RunAllBAQValidations_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexValidationTableset] = obj["returnObj"]
      pass

class RunBAQValidation_input:
   """ Required : 
   indexName
   queryId
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      self.queryId:str = obj["queryId"]
      """  BAQ to validate.  """  
      pass

class RunBAQValidation_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexValidationTableset] = obj["returnObj"]
      pass

class UpdateBaqTuning_input:
   """ Required : 
   indexTableset
   queryId
   """  
   def __init__(self, obj):
      self.indexTableset:list[Ice_Tablesets_ESIndexTableset] = obj["indexTableset"]
      self.queryId:str = obj["queryId"]
      """  query id.  """  
      pass

class UpdateBaqTuning_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESIndexTableset] = obj["returnObj"]
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ESIndexTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ESIndexTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAllBaqs_input:
   """ Required : 
   indexName
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      pass

class ValidateAllBaqs_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  the validation results as XML.  """  
      pass

class ValidateBaq_input:
   """ Required : 
   indexName
   queryId
   """  
   def __init__(self, obj):
      self.indexName:str = obj["indexName"]
      """  index name.  """  
      self.queryId:str = obj["queryId"]
      """  BAQ to validate.  """  
      pass

class ValidateBaq_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  the validation results as XML.  """  
      pass

class WriteBuildLogToFile_input:
   """ Required : 
   buildLogId
   """  
   def __init__(self, obj):
      self.buildLogId:str = obj["buildLogId"]
      """  the build log.  """  
      pass

class WriteBuildLogToFile_output:
   def __init__(self, obj):
      pass

