import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.SynergySvc
# Description: Interacts with Synergy.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSynergyUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetSynergyUrl
   Description: Retrieves the Synergy URL.
   OperationID: GetSynergyUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSynergyUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSynergyApiUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetSynergyApiUrl
   Description: Retrieves the Synergy API URL.
   OperationID: GetSynergyApiUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSynergyApiUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Register(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Register
   Description: Register for Synergy.
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Login(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Login
   Description: Login to Synergy.
   OperationID: Login
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Login_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Login_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadFile
   Description: Download Non ERP file from any DMS
   OperationID: DownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFile
   Description: Delete Non ERP file from any DMS
   OperationID: DeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultCompanyStorage(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultCompanyStorage
   OperationID: GetDefaultCompanyStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultCompanyStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_UploadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadFile
   Description: Upload Non ERP file to any DMS
   OperationID: UploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEnabledStorageTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetEnabledStorageTypes
   Description: Gets the enabled storage types.
   OperationID: GetEnabledStorageTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnabledStorageTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetHealthInfo(epicorHeaders = None):
   """  
   Summary: Invoke method GetHealthInfo
   Description: Gets information for the health check.
   OperationID: GetHealthInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHealthInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_DeployRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeployRules
   Description: Deploy rules.
   OperationID: DeployRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeployRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeployRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Reconnect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Reconnect
   Description: Reconnect to a previous Collaborate environment.
   OperationID: Reconnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Reconnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Reconnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Disconnect(epicorHeaders = None):
   """  
   Summary: Invoke method Disconnect
   Description: Disconnect from the current Collaborate environment.
   OperationID: Disconnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Disconnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Configure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Configure
   Description: Configure Synergy.
   OperationID: Configure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Configure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Configure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetails
   Description: Gets details about a record.
   OperationID: GetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEntityInfoFromTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEntityInfoFromTags
   Description: Get the status of an entity based on the related tags
   OperationID: GetEntityInfoFromTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntityInfoFromTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityInfoFromTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRuleCategories(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRuleCategories
   Description: Get Rule Categories currently in use by a specific company
   OperationID: GetRuleCategories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRuleCategories_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRuleCategories_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActivityFeed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetActivityFeed
   Description: Get the activity feed for the company
   OperationID: GetActivityFeed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActivityFeed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActivityFeed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkActivityRead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkActivityRead
   Description: Mark an activity read in Collobrate
   OperationID: MarkActivityRead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkActivityRead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkActivityRead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkActivityUnread(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkActivityUnread
   Description: Mark an activity unread in Collaborate
   OperationID: MarkActivityUnread
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkActivityUnread_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkActivityUnread_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRules
   Description: Get rules for a specific category
   OperationID: GetRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRulesListWithSecurityCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRulesListWithSecurityCode
   Description: Get rules for a specific category
   OperationID: GetRulesListWithSecurityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRulesListWithSecurityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRulesListWithSecurityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableGroups
   Description: Get list of available Collaborate groups (public and private) for current user
   OperationID: GetAvailableGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostContentToCollaborate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostContentToCollaborate
   Description: Share message content on Collaborate channel or group
   OperationID: PostContentToCollaborate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostContentToCollaborate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostContentToCollaborate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUsersForCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUsersForCompany
   Description: Gets all users for a company
   OperationID: GetUsersForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUsersForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsersForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUsersForGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUsersForGroup
   Description: Gets all members for a group
   OperationID: GetUsersForGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUsersForGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsersForGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Configure_input:
   """ Required : 
   url
   apiUrl
   id
   secret
   subscriber
   """  
   def __init__(self, obj):
      self.url:str = obj["url"]
      """  A new URL, or null/empty to leave it unchanged.  """  
      self.apiUrl:str = obj["apiUrl"]
      """  A new API URL, or null/empty to leave it unchanged.  """  
      self.id:str = obj["id"]
      """  A new ID, or null/empty to leave it unchanged.  """  
      self.secret:str = obj["secret"]
      """  A new secret, or null/empty to leave it unchanged.  """  
      self.subscriber:str = obj["subscriber"]
      """  A new subscriber, or null/empty to leave it unchanged.  """  
      pass

class Configure_output:
   def __init__(self, obj):
      pass

class CreateCollaborateUserDefinedRuleSecurityCode_input:
   """ Required : 
   category
   """  
   def __init__(self, obj):
      self.category:str = obj["category"]
      pass

class CreateCollaborateUserDefinedRuleSecurityCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DeleteFile_input:
   """ Required : 
   fileDetails
   token
   companyId
   storageType
   """  
   def __init__(self, obj):
      self.fileDetails      #schema had no properties on an object.
      self.token:str = obj["token"]
      self.companyId:str = obj["companyId"]
      self.storageType:int = obj["storageType"]
      pass

class DeleteFile_output:
   def __init__(self, obj):
      pass

class DeployRules_input:
   """ Required : 
   company
   rules
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The company to deploy to, or null/empty to deploy to all companies that the current user has access to.  """  
      self.rules:str = obj["rules"]
      """  The rules to deploy.  """  
      pass

class DeployRules_output:
   def __init__(self, obj):
      pass

class Disconnect_output:
   def __init__(self, obj):
      pass

class DownloadFile_input:
   """ Required : 
   xFileRefNum
   companyId
   storageType
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.companyId:str = obj["companyId"]
      self.storageType:int = obj["storageType"]
      pass

class DownloadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetActivityFeed_input:
   """ Required : 
   companyID
   token
   queryParams
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company  """  
      self.token:str = obj["token"]
      self.queryParams:str = obj["queryParams"]
      pass

class GetActivityFeed_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetAvailableGroups_input:
   """ Required : 
   companyID
   queryParams
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.queryParams:str = obj["queryParams"]
      pass

class GetAvailableGroups_output:
   def __init__(self, obj):
      self.returnObj:object
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

class GetDefaultCompanyStorage_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Default Company DMS Value  """  
      pass

class GetDetails_input:
   """ Required : 
   record
   """  
   def __init__(self, obj):
      self.record:str = obj["record"]
      """  Information used to identify the record.  """  
      pass

class GetDetails_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Record details.  """  
      pass

class GetEnabledStorageTypes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A list of enabled storage types.  """  
      pass

class GetEntityInfoFromTags_input:
   """ Required : 
   tags
   """  
   def __init__(self, obj):
      self.tags      #schema had no properties on an object.
      """  Tags to search on, at least one tag must be specified  """  
      pass

class GetEntityInfoFromTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.notSupported:bool = obj["notSupported"]
      self.notFound:bool = obj["notFound"]
      self.type:str = obj["parameters"]
      self.result:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetHealthInfo_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Health info.  """  
      pass

class GetRuleCategories_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company to lookup  """  
      pass

class GetRuleCategories_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Categories (table names)  """  
      pass

class GetRulesListWithSecurityCode_input:
   """ Required : 
   companyID
   category
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company to lookup  """  
      self.category:str = obj["category"]
      """  Company to lookup  """  
      pass

class GetRulesListWithSecurityCode_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Rule description  """  
      pass

class GetRules_input:
   """ Required : 
   companyID
   category
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company to lookup  """  
      self.category:str = obj["category"]
      """  Category (table name), blank for all categories  """  
      pass

class GetRules_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Rule description  """  
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

class GetSynergyApiUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The Synergy API URL.  """  
      pass

class GetSynergyUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The Synergy URL.  """  
      pass

class GetUsersForCompany_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      pass

class GetUsersForCompany_output:
   def __init__(self, obj):
      self.returnObj:object
      pass

class GetUsersForGroup_input:
   """ Required : 
   companyID
   groupID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.groupID:str = obj["groupID"]
      pass

class GetUsersForGroup_output:
   def __init__(self, obj):
      self.returnObj:object
      pass

class Login_input:
   """ Required : 
   erpUrl
   erpToken
   """  
   def __init__(self, obj):
      self.erpUrl:str = obj["erpUrl"]
      """  The ERP URL.  """  
      self.erpToken:str = obj["erpToken"]
      """  The ERP token.  """  
      pass

class Login_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A Synergy token.  """  
      pass

class MarkActivityRead_input:
   """ Required : 
   token
   activityID
   """  
   def __init__(self, obj):
      self.token:str = obj["token"]
      """  Collaborate token  """  
      self.activityID:str = obj["activityID"]
      """  Activity ID  """  
      pass

class MarkActivityRead_output:
   def __init__(self, obj):
      pass

class MarkActivityUnread_input:
   """ Required : 
   token
   activityID
   """  
   def __init__(self, obj):
      self.token:str = obj["token"]
      """  Collaborate token  """  
      self.activityID:str = obj["activityID"]
      """  Activity ID  """  
      pass

class MarkActivityUnread_output:
   def __init__(self, obj):
      pass

class PostContentToCollaborate_input:
   """ Required : 
   content
   groupId
   """  
   def __init__(self, obj):
      self.content:str = obj["content"]
      self.groupId:str = obj["groupId"]
      pass

class PostContentToCollaborate_output:
   def __init__(self, obj):
      pass

class Reconnect_input:
   """ Required : 
   recoveryKey
   """  
   def __init__(self, obj):
      self.recoveryKey:str = obj["recoveryKey"]
      """  The environment's recovery key.  """  
      pass

class Reconnect_output:
   def __init__(self, obj):
      pass

class Register_input:
   """ Required : 
   synergyUrl
   synergyApiUrl
   erpUrl
   erpToken
   """  
   def __init__(self, obj):
      self.synergyUrl:str = obj["synergyUrl"]
      """  The Synergy front-end URL.  """  
      self.synergyApiUrl:str = obj["synergyApiUrl"]
      """  The Synergy API URL.  """  
      self.erpUrl:str = obj["erpUrl"]
      """  The ERP URL.  """  
      self.erpToken:str = obj["erpToken"]
      """  The ERP token.  """  
      pass

class Register_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The environment's recovery key.  """  
      pass

class UploadFile_input:
   """ Required : 
   sourceFile
   fileData
   token
   storageType
   """  
   def __init__(self, obj):
      self.sourceFile:str = obj["sourceFile"]
      self.fileData:str = obj["fileData"]
      self.token:str = obj["token"]
      self.storageType:int = obj["storageType"]
      pass

class UploadFile_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

