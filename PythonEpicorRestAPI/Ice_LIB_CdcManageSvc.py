import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.CdcManageSvc
# Description: Cdc Management Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ListCaptureStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ListCaptureStatus
   Description: List the Capture Status
   OperationID: ListCaptureStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListCaptureStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListCaptureStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableCapture(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableCapture
   Description: Enable capture on a list of tables
   OperationID: EnableCapture
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableCapture_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableCapture_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisableCapture(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisableCapture
   Description: Disable capture on a list of tables
   OperationID: DisableCapture
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableCapture_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableCapture_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateAvailableTables(epicorHeaders = None):
   """  
   Summary: Invoke method GenerateAvailableTables
   Description: Generate list of available tables that can have Change Capture enabled on them
This should only be used if a new table was created and the change capture trigger was added, or alternatively a trigger was disabled
   OperationID: GenerateAvailableTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateAvailableTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Register(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Register
   Description: Register a new subscriber for the API
   OperationID: Register
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Register_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Register_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Unregister(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Unregister
   Description: Unregister a subscriber
   OperationID: Unregister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unregister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unregister_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubscriberUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubscriberUpdate
   Description: Update a subscriber's configuration
   OperationID: SubscriberUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubscriberUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscriberUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegenerateSecret(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegenerateSecret
   Description: Generate a new secret for a subscriber
   OperationID: RegenerateSecret
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenerateSecret_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateSecret_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubscribersList(epicorHeaders = None):
   """  
   Summary: Invoke method SubscribersList
   Description: List all CDC subscribers
   OperationID: SubscribersList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscribersList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SubscriberGet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubscriberGet
   Description: Get a specific CDC subscriber
   OperationID: SubscriberGet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubscriberGet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscriberGet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleGet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleGet
   OperationID: RuleGet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleGet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleGet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleAdd
   Description: Add a rule for a specific subscriber
   OperationID: RuleAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleRemove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleRemove
   Description: Remove a rule from a specific subscriber
   OperationID: RuleRemove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleRemove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleRemove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleUpdate
   Description: Update a rule
   OperationID: RuleUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RulesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RulesList
   Description: List out all the rules for a specific subscriber
   OperationID: RulesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RulesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleTableList
   Description: List tables that have been enabled for CDC and can be used for rules
   OperationID: RuleTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSampleData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSampleData
   Description: Generate sample data for a given table
   OperationID: GenerateSampleData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateLookupSampleData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateLookupSampleData
   Description: Generate sample data for the lookups on a given table
   OperationID: GenerateLookupSampleData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLookupSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLookupSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateKeyTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateKeyTags
   Description: Generate Tags based on the primary key columns
   OperationID: GenerateKeyTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateKeyTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateKeyTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupLinks
   Description: Get look up links available for a specific table
   OperationID: GetLookupLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupLinks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupDataFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupDataFields
   Description: Get data fields for a specific look up on a table
   OperationID: GetLookupDataFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupDataFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupDataFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCollaborateUserDefinedRuleSecurityCodes(epicorHeaders = None):
   """  
   Summary: Invoke method GetCollaborateUserDefinedRuleSecurityCodes
   Description: Get User Defined Security Code for Collaborate Notification rules
   OperationID: GetCollaborateUserDefinedRuleSecurityCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateUserDefinedRuleSecurityCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetCollaborateSecurityCodes(epicorHeaders = None):
   """  
   Summary: Invoke method GetCollaborateSecurityCodes
   Description: Get All Security Code for Collaborate Notification rules
   OperationID: GetCollaborateSecurityCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSecurityAccessForUsers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSecurityAccessForUsers
   Description: Return the list of users and their accessible security codes
   OperationID: GetSecurityAccessForUsers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSecurityAccessForUsers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSecurityAccessForUsers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCollaborateSecurityCodeAccessRights(epicorHeaders = None):
   """  
   Summary: Invoke method GetCollaborateSecurityCodeAccessRights
   Description: Get Access status for current user for the collaborate security codes
   OperationID: GetCollaborateSecurityCodeAccessRights
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeAccessRights_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetCollaborateSecurityCodeAccessStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCollaborateSecurityCodeAccessStatus
   Description: Check the access status for the current user for the given security code
   OperationID: GetCollaborateSecurityCodeAccessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCollaborateSecurityCodeAccessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeAccessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCollaborateSecurityCodeUserAccessStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCollaborateSecurityCodeUserAccessStatus
   Description: Check the access status for a user for the given security code
   OperationID: GetCollaborateSecurityCodeUserAccessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCollaborateSecurityCodeUserAccessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeUserAccessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateCollaborateUserDefinedRuleSecurityCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateCollaborateUserDefinedRuleSecurityCode
   Description: Create User Defined Security Code for Collaborate Notification rules
   OperationID: CreateCollaborateUserDefinedRuleSecurityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCollaborateUserDefinedRuleSecurityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCollaborateUserDefinedRuleSecurityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CreateCollaborateUserDefinedRuleSecurityCode_input:
   """ Required : 
   catgory
   """  
   def __init__(self, obj):
      self.catgory:str = obj["catgory"]
      pass

class CreateCollaborateUserDefinedRuleSecurityCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DisableCapture_input:
   """ Required : 
   tables
   """  
   def __init__(self, obj):
      self.tables:str = obj["tables"]
      """  Schema and table name  """  
      pass

class DisableCapture_output:
   def __init__(self, obj):
      pass

class EnableCapture_input:
   """ Required : 
   tables
   """  
   def __init__(self, obj):
      self.tables:str = obj["tables"]
      """  Schema and table name  """  
      pass

class EnableCapture_output:
   def __init__(self, obj):
      pass

class GenerateAvailableTables_output:
   def __init__(self, obj):
      pass

class GenerateKeyTags_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      pass

class GenerateKeyTags_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Tags  """  
      pass

class GenerateLookupSampleData_input:
   """ Required : 
   schemaName
   tableName
   lookupIDs
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      self.lookupIDs:str = obj["lookupIDs"]
      """  Lookup IDs to include  """  
      pass

class GenerateLookupSampleData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Sample data for table  """  
      pass

class GenerateSampleData_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      pass

class GenerateSampleData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Sample data for table  """  
      pass

class GetCollaborateSecurityCodeAccessRights_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetCollaborateSecurityCodeAccessStatus_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      pass

class GetCollaborateSecurityCodeAccessStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetCollaborateSecurityCodeUserAccessStatus_input:
   """ Required : 
   secCode
   userId
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      self.userId:str = obj["userId"]
      pass

class GetCollaborateSecurityCodeUserAccessStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetCollaborateSecurityCodes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCollaborateUserDefinedRuleSecurityCodes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetLookupDataFields_input:
   """ Required : 
   schemaName
   tableName
   lookupID
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      self.lookupID:str = obj["lookupID"]
      """  Lookup ID  """  
      pass

class GetLookupDataFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of lookup links  """  
      pass

class GetLookupLinks_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      pass

class GetLookupLinks_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of lookup links  """  
      pass

class GetSecurityAccessForUsers_input:
   """ Required : 
   userIds
   """  
   def __init__(self, obj):
      self.userIds:str = obj["userIds"]
      pass

class GetSecurityAccessForUsers_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
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

class Ice_Tablesets_CdcCaptureStatusRow:
   def __init__(self, obj):
      self.SchemaName:str = obj["SchemaName"]
      self.TableName:str = obj["TableName"]
      self.CaptureEnabled:bool = obj["CaptureEnabled"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CdcCaptureStatusTableset:
   def __init__(self, obj):
      self.CdcCaptureStatus:list[Ice_Tablesets_CdcCaptureStatusRow] = obj["CdcCaptureStatus"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_CdcSubscriberRow:
   def __init__(self, obj):
      self.SubscriberID:str = obj["SubscriberID"]
      self.Description:str = obj["Description"]
      self.SubscriberMode:str = obj["SubscriberMode"]
      """  Subscribers read mode, options are push, push-pull or pull  """  
      self.Inactive:bool = obj["Inactive"]
      self.MarkDeletion:bool = obj["MarkDeletion"]
      self.Offset:int = obj["Offset"]
      self.PageSize:int = obj["PageSize"]
      self.LastPush:str = obj["LastPush"]
      self.LastPushAttempt:str = obj["LastPushAttempt"]
      self.LastPull:str = obj["LastPull"]
      self.PushAttempts:int = obj["PushAttempts"]
      """  Number of push attempts made without success  """  
      self.TTLRead:int = obj["TTLRead"]
      """  Duration (in seconds) that read messages are kept for the subscriber  """  
      self.TTLUnread:int = obj["TTLUnread"]
      """  Duration (in seconds) that unread messages are kept for the subscriber  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CdcSubscriberRuleRow:
   def __init__(self, obj):
      self.SubscriberID:str = obj["SubscriberID"]
      self.RuleID:str = obj["RuleID"]
      self.SchemaName:str = obj["SchemaName"]
      self.TableName:str = obj["TableName"]
      self.ChangeType:str = obj["ChangeType"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.Inactive:bool = obj["Inactive"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      self.Description:str = obj["Description"]
      self.Company:str = obj["Company"]
      self.SecCode:str = obj["SecCode"]
      """  Security Code  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CdcSubscriberRuleTableset:
   def __init__(self, obj):
      self.CdcSubscriberRule:list[Ice_Tablesets_CdcSubscriberRuleRow] = obj["CdcSubscriberRule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_CdcSubscriberTableset:
   def __init__(self, obj):
      self.CdcSubscriber:list[Ice_Tablesets_CdcSubscriberRow] = obj["CdcSubscriber"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ListCaptureStatus_input:
   """ Required : 
   schemaName
   tableName
   status
   skip
   pageSize
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Table to search for  """  
      self.status:int = obj["status"]
      """  Status 0 = All, 1 = Enabled, 2 = Disabled  """  
      self.skip:int = obj["skip"]
      """  Skip n results  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size, maximum 200  """  
      pass

class ListCaptureStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CdcCaptureStatusTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pageSize:int = obj["parameters"]
      self.morePages:bool = obj["morePages"]
      self.total:int = obj["parameters"]
      pass

      """  output parameters  """  

class RegenerateSecret_input:
   """ Required : 
   subscriberID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      pass

class RegenerateSecret_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newSecret:str = obj["parameters"]
      pass

      """  output parameters  """  

class Register_input:
   """ Required : 
   description
   mode
   webHookURI
   webHookSecret
   """  
   def __init__(self, obj):
      self.description:str = obj["description"]
      """  Description of Subscriber  """  
      self.mode:str = obj["mode"]
      """  Subscriber Mode - "PUSH", "PUSHPULL" or "PULL"  """  
      self.webHookURI:str = obj["webHookURI"]
      """  Web Hook URI for Push or Push-Pull  """  
      self.webHookSecret:str = obj["webHookSecret"]
      """  Web Hook Secret for Push or Push-Pull  """  
      pass

class Register_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.subscriberID:str = obj["parameters"]
      self.secret:str = obj["parameters"]
      pass

      """  output parameters  """  

class RuleAdd_input:
   """ Required : 
   subscriberID
   companyID
   ruleID
   description
   schemaName
   tableName
   changeType
   rule
   metadataRule
   lookupLinks
   inactive
   secCode
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.companyID:str = obj["companyID"]
      """  Company the rule is assigned to  """  
      self.ruleID:str = obj["ruleID"]
      """  Rule ID  """  
      self.description:str = obj["description"]
      """  Description of rule  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema rule applies to  """  
      self.tableName:str = obj["tableName"]
      """  Table rule applies to  """  
      self.changeType:str = obj["changeType"]
      """  Change type rule applies to, valid options are insert, update and delete  """  
      self.rule:str = obj["rule"]
      """  Rule JSON logic  """  
      self.metadataRule:str = obj["metadataRule"]
      """  Metadata JSON logic output  """  
      self.lookupLinks:str = obj["lookupLinks"]
      """  Look up links  """  
      self.inactive:bool = obj["inactive"]
      """  Whether rule is currently active  """  
      self.secCode:str = obj["secCode"]
      """  Security Code  """  
      pass

class RuleAdd_output:
   def __init__(self, obj):
      pass

class RuleGet_input:
   """ Required : 
   subscriberID
   companyID
   ruleID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      self.companyID:str = obj["companyID"]
      self.ruleID:str = obj["ruleID"]
      pass

class RuleGet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.description:str = obj["parameters"]
      self.schemaName:str = obj["parameters"]
      self.tableName:str = obj["parameters"]
      self.changeType:str = obj["parameters"]
      self.rule:str = obj["parameters"]
      self.metadataRule:str = obj["parameters"]
      self.lookupLinks:str = obj["parameters"]
      self.systemFlag:bool = obj["systemFlag"]
      self.inactive:bool = obj["inactive"]
      self.lastUpdated:str = obj["parameters"]
      self.lastUpdatedBy:str = obj["parameters"]
      self.secCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class RuleRemove_input:
   """ Required : 
   subscriberID
   companyID
   ruleID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.companyID:str = obj["companyID"]
      """  Company the rule belongs to  """  
      self.ruleID:str = obj["ruleID"]
      """  Rule ID  """  
      pass

class RuleRemove_output:
   def __init__(self, obj):
      pass

class RuleTableList_input:
   """ Required : 
   subscriberID
   secret
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Secret  """  
      pass

class RuleTableList_output:
   def __init__(self, obj):
      self.returnObj:array
      pass

class RuleUpdate_input:
   """ Required : 
   subscriberID
   companyID
   ruleID
   description
   changeType
   rule
   metadataRule
   lookupLinks
   inactive
   secCode
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.companyID:str = obj["companyID"]
      """  Company the rule is assigned to  """  
      self.ruleID:str = obj["ruleID"]
      """  ID of rule being updated  """  
      self.description:str = obj["description"]
      """  Description of rule  """  
      self.changeType:str = obj["changeType"]
      """  Change type rule applies to, valid options are insert, update and delete  """  
      self.rule:str = obj["rule"]
      """  Rule JSON logic, passing null will ignore column from updating  """  
      self.metadataRule:str = obj["metadataRule"]
      """  Metadata JSON logic output  """  
      self.lookupLinks:str = obj["lookupLinks"]
      """  Look up links  """  
      self.inactive:bool = obj["inactive"]
      """  Set the rule to active/inactive  """  
      self.secCode:str = obj["secCode"]
      """  Security Code  """  
      pass

class RuleUpdate_output:
   def __init__(self, obj):
      pass

class RulesList_input:
   """ Required : 
   subscriberID
   companyID
   description
   schemaName
   tableName
   excludeSystem
   skip
   pageSize
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.companyID:str = obj["companyID"]
      """  Company, blank to list all available companies  """  
      self.description:str = obj["description"]
      """  Contains description  """  
      self.schemaName:str = obj["schemaName"]
      """  Filter to specific schema  """  
      self.tableName:str = obj["tableName"]
      """  Filter to specific table  """  
      self.excludeSystem:bool = obj["excludeSystem"]
      """  Exclude System rules  """  
      self.skip:int = obj["skip"]
      """  Skip n results  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size, maximum 200  """  
      pass

class RulesList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CdcSubscriberRuleTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pageSize:int = obj["parameters"]
      self.morePages:bool = obj["morePages"]
      self.total:int = obj["parameters"]
      pass

      """  output parameters  """  

class SubscriberGet_input:
   """ Required : 
   subscriberID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      pass

class SubscriberGet_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CdcSubscriberTableset] = obj["returnObj"]
      pass

class SubscriberUpdate_input:
   """ Required : 
   subscriberID
   description
   inactive
   webHookURI
   webHookSecret
   pageSize
   TTLRead
   TTLUnread
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.description:str = obj["description"]
      """  New description  """  
      self.inactive:bool = obj["inactive"]
      """  Set subscriber to inactive  """  
      self.webHookURI:str = obj["webHookURI"]
      """  Web Hook URI, only valid for Push or Push-Pull  """  
      self.webHookSecret:str = obj["webHookSecret"]
      """  Web Hook Secret, only valid for Push or Push-Pull  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size for messages are pushed/pulled  """  
      self.TTLRead:int = obj["TTLRead"]
      """  How long to keep read messages, in seconds  """  
      self.TTLUnread:int = obj["TTLUnread"]
      """  How long to keep unread messages, in seconds  """  
      pass

class SubscriberUpdate_output:
   def __init__(self, obj):
      pass

class SubscribersList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CdcSubscriberTableset] = obj["returnObj"]
      pass

class Unregister_input:
   """ Required : 
   subscriberID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      pass

class Unregister_output:
   def __init__(self, obj):
      pass

