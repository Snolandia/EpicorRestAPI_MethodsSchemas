import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.SessionModSvc
# Description: Modifies session state
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetLicense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLicense
   OperationID: GetLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetModuleAccess(epicorHeaders = None):
   """  
   Summary: Invoke method GetModuleAccess
   OperationID: GetModuleAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetModuleAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetLicensedModuleAccess(epicorHeaders = None):
   """  
   Summary: Invoke method GetLicensedModuleAccess
   Description: Returns all the modules for the current company with flag for licensed.
   OperationID: GetLicensedModuleAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicensedModuleAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCompany
   Description: Set the session's current company.
   OperationID: SetCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDateFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDateFormat
   Description: Set the date format for the session
   OperationID: SetDateFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDateFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDateFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetEmployee(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetEmployee
   Description: Set the current employee ID for the session
   OperationID: SetEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetLanguage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetLanguage
   OperationID: SetLanguage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetLanguage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetLanguage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetPlant
   Description: Set the session's current site.
   OperationID: SetPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUser
   Description: Sets the user.
   OperationID: SetUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetWorkstation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetWorkstation
   Description: Set the current workstation ID for the session
   OperationID: SetWorkstation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetWorkstation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetWorkstation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetTaskClientID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTaskClientID
   Description: Set the TaskClientID for the current session
   OperationID: SetTaskClientID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTaskClientID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTaskClientID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Handshake(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Handshake
   Description: Validate the client version against server version.
   OperationID: Handshake
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Handshake_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Handshake_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssertConversionsPending(epicorHeaders = None):
   """  
   Summary: Invoke method AssertConversionsPending
   Description: Checks if the current logged in user has any pending conversions.
   OperationID: AssertConversionsPending
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssertConversionsPending_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_UpdateSeedData(epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSeedData
   Description: call to update seed data for patches
   OperationID: UpdateSeedData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSeedData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_HandshakeBaseVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HandshakeBaseVersion
   Description: Validate the base FW client version against base FW server version
   OperationID: HandshakeBaseVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HandshakeBaseVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HandshakeBaseVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Sync(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Sync
   Description: Synchronize the client and server copies of the session state
   OperationID: Sync
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Sync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Sync_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Login(epicorHeaders = None):
   """  
   Summary: Invoke method Login
   Description: Creates a Session on the server for the validated user that is maintained until Logout is called.
   OperationID: Login
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Login_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Logout(epicorHeaders = None):
   """  
   Summary: Invoke method Logout
   Description: Stops caching this Session.
   OperationID: Logout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Logout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetLanguage(epicorHeaders = None):
   """  
   Summary: Invoke method GetLanguage
   OperationID: GetLanguage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLanguage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_InMobileConnect(epicorHeaders = None):
   """  
   Summary: Invoke method InMobileConnect
   OperationID: InMobileConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InMobileConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_IsValidSession(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidSession
   Description: Checks whether a given session ID/user ID combination is valid
   OperationID: IsValidSession
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidSession_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidSession_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSessionInfoForEdgeAgentUser(epicorHeaders = None):
   """  
   Summary: Invoke method GetSessionInfoForEdgeAgentUser
   OperationID: GetSessionInfoForEdgeAgentUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSessionInfoForEdgeAgentUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetCustomVersion(epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomVersion
   Description: Returns the custom version string defined by a third-party
   OperationID: GetCustomVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPatchLevel(epicorHeaders = None):
   """  
   Summary: Invoke method GetPatchLevel
   Description: Returns the Server FW patch level
   OperationID: GetPatchLevel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPatchLevel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPatchLevelApp(epicorHeaders = None):
   """  
   Summary: Invoke method GetPatchLevelApp
   Description: Returns the Sever App patch level
   OperationID: GetPatchLevelApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPatchLevelApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetRequiredDBVersionApp(epicorHeaders = None):
   """  
   Summary: Invoke method GetRequiredDBVersionApp
   Description: Returns the Sever App Required DB level
   OperationID: GetRequiredDBVersionApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRequiredDBVersionApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSystemCodeApp(epicorHeaders = None):
   """  
   Summary: Invoke method GetSystemCodeApp
   Description: Returns the Sever Application system code
   OperationID: GetSystemCodeApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemCodeApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetBaseLevel(epicorHeaders = None):
   """  
   Summary: Invoke method GetBaseLevel
   Description: Returns the FW Base Level
   OperationID: GetBaseLevel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseLevel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetBaseLevelApp(epicorHeaders = None):
   """  
   Summary: Invoke method GetBaseLevelApp
   Description: Returns the FW Base Level
   OperationID: GetBaseLevelApp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseLevelApp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_DedicatedTenancy(epicorHeaders = None):
   """  
   Summary: Invoke method DedicatedTenancy
   Description: Returns the DedicatedTenancy value
   OperationID: DedicatedTenancy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DedicatedTenancy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentValues(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentValues
   OperationID: GetCurrentValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentValuesFromServer(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentValuesFromServer
   OperationID: GetCurrentValuesFromServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentValuesFromServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSynergyUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetSynergyUrl
   Description: Get the Synergy URL if one is setup within the system.
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetTelemetrySettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetTelemetrySettings
   Description: Get the telemetry settings to filter events in the client.
   OperationID: GetTelemetrySettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTelemetrySettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SessionModSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AssertConversionsPending_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  False if there are no pending conversions to be run.  """  
      pass

class DedicatedTenancy_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetBaseLevelApp_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetBaseLevel_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrentValuesFromServer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.companyID:str = obj["parameters"]
      self.companyName:str = obj["parameters"]
      self.siteID:str = obj["parameters"]
      self.siteName:str = obj["parameters"]
      self.employeeID:str = obj["parameters"]
      self.workstationID:str = obj["parameters"]
      self.workstationDescription:str = obj["parameters"]
      self.systemCode:str = obj["parameters"]
      self.countryGroupCode:str = obj["parameters"]
      self.countryCode:str = obj["parameters"]
      self.tenantID:str = obj["parameters"]
      self.solutionID:str = obj["parameters"]
      self.accessScopeID:str = obj["parameters"]
      self.isProductionInstance:bool = obj["isProductionInstance"]
      self.enabledFeatureFlags:list = obj[any]
      pass

      """  output parameters  """  

class GetCurrentValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.companyID:str = obj["parameters"]
      self.companyName:str = obj["parameters"]
      self.siteID:str = obj["parameters"]
      self.siteName:str = obj["parameters"]
      self.employeeID:str = obj["parameters"]
      self.workstationID:str = obj["parameters"]
      self.workstationDescription:str = obj["parameters"]
      self.systemCode:str = obj["parameters"]
      self.countryGroupCode:str = obj["parameters"]
      self.countryCode:str = obj["parameters"]
      self.tenantID:str = obj["parameters"]
      self.solutionID:str = obj["parameters"]
      self.enabledFeatureFlags:list = obj[any]
      pass

      """  output parameters  """  

class GetCustomVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetLanguage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetLicense_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      pass

class GetLicense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.maxUsers:int = obj["parameters"]
      self.maxDCUsers:int = obj["parameters"]
      self.installationID:str = obj["parameters"]
      self.evalExpires:str = obj["parameters"]
      self.editionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLicensedModuleAccess_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ModuleAccessTableset] = obj["returnObj"]
      pass

class GetModuleAccess_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.moduleAccessList: UNKNOW TYPE(error 2338) = obj["moduleAccessList"]
      pass

      """  output parameters  """  

class GetPatchLevelApp_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetPatchLevel_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRequiredDBVersionApp_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSessionInfoForEdgeAgentUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.userName:str = obj["parameters"]
      self.authMode:str = obj["parameters"]
      self.expiresOn:int = obj["parameters"]
      self.oid:str = obj["parameters"]
      self.tid:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSynergyUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSystemCodeApp_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTelemetrySettings_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class HandshakeBaseVersion_input:
   """ Required : 
   clientVersion
   """  
   def __init__(self, obj):
      self.clientVersion:str = obj["clientVersion"]
      """  The Client version.  """  
      pass

class HandshakeBaseVersion_output:
   def __init__(self, obj):
      pass

class Handshake_input:
   """ Required : 
   clientVersion
   """  
   def __init__(self, obj):
      self.clientVersion:str = obj["clientVersion"]
      """  The client version.  """  
      pass

class Handshake_output:
   def __init__(self, obj):
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

class Ice_Tablesets_ModuleAccessRow:
   def __init__(self, obj):
      self.Identifier:str = obj["Identifier"]
      """  Guid identifier for module.  """  
      self.Name:str = obj["Name"]
      """  String description for module  """  
      self.isLicensed:bool = obj["isLicensed"]
      """  Indicates if the module is licensed  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ModuleAccessTableset:
   def __init__(self, obj):
      self.ModuleAccess:list[Ice_Tablesets_ModuleAccessRow] = obj["ModuleAccess"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class InMobileConnect_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsValidSession_input:
   """ Required : 
   sessionID
   userID
   """  
   def __init__(self, obj):
      self.sessionID:str = obj["sessionID"]
      self.userID:str = obj["userID"]
      pass

class IsValidSession_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Login_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A new SessionID  """  
      pass

class Logout_output:
   def __init__(self, obj):
      pass

class SetCompany_input:
   """ Required : 
   newCompany
   """  
   def __init__(self, obj):
      self.newCompany:str = obj["newCompany"]
      pass

class SetCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.companyName:str = obj["parameters"]
      self.siteID:str = obj["parameters"]
      self.siteName:str = obj["parameters"]
      self.workstationID:str = obj["parameters"]
      self.workstationDescription:str = obj["parameters"]
      self.employeeID:str = obj["parameters"]
      self.countryGroupCode:str = obj["parameters"]
      self.countryCode:str = obj["parameters"]
      self.tenantID:str = obj["parameters"]
      self.isProductionInstance:bool = obj["isProductionInstance"]
      pass

      """  output parameters  """  

class SetDateFormat_input:
   """ Required : 
   dateFormat
   """  
   def __init__(self, obj):
      self.dateFormat:str = obj["dateFormat"]
      """  Date format  """  
      pass

class SetDateFormat_output:
   def __init__(self, obj):
      pass

class SetEmployee_input:
   """ Required : 
   employeeID
   """  
   def __init__(self, obj):
      self.employeeID:str = obj["employeeID"]
      pass

class SetEmployee_output:
   def __init__(self, obj):
      pass

class SetLanguage_input:
   """ Required : 
   languageID
   """  
   def __init__(self, obj):
      self.languageID:str = obj["languageID"]
      pass

class SetLanguage_output:
   def __init__(self, obj):
      pass

class SetPlant_input:
   """ Required : 
   newSite
   """  
   def __init__(self, obj):
      self.newSite:str = obj["newSite"]
      pass

class SetPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.siteName:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetTaskClientID_input:
   """ Required : 
   environmentUserName
   """  
   def __init__(self, obj):
      self.environmentUserName:str = obj["environmentUserName"]
      """  Environment.UserName  """  
      pass

class SetTaskClientID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.taskClientID:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetUser_input:
   """ Required : 
   userID
   password
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      """  The user identifier.  """  
      self.password:str = obj["password"]
      """  The password.  """  
      pass

class SetUser_output:
   def __init__(self, obj):
      pass

class SetWorkstation_input:
   """ Required : 
   newWorkstationID
   """  
   def __init__(self, obj):
      self.newWorkstationID:str = obj["newWorkstationID"]
      """  New workstation ID  """  
      pass

class SetWorkstation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.workstationDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class Sync_input:
   """ Required : 
   clientDateFormat
   clientComputerName
   clientTerminalID
   clientUserName
   appserver
   """  
   def __init__(self, obj):
      self.clientDateFormat:str = obj["clientDateFormat"]
      """  The client date format.  """  
      self.clientComputerName:str = obj["clientComputerName"]
      """  Name of the client computer.  """  
      self.clientTerminalID:int = obj["clientTerminalID"]
      """  The client terminal ID.  """  
      self.clientUserName:str = obj["clientUserName"]
      """  Current client machine user name.  """  
      self.appserver:str = obj["appserver"]
      """  URL of the application server the client is connected to.  """  
      pass

class Sync_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.userID:str = obj["parameters"]
      self.replicatedDatabase:bool = obj["replicatedDatabase"]
      self.taskClientID:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateSeedData_output:
   def __init__(self, obj):
      pass

