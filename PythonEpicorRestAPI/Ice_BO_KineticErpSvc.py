import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.KineticErpSvc
# Description: Represents the Kinetic Erp Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetTokenList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given data type.
   OperationID: GetTokenList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTokenList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTokenValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of vaules based on a type that is passed in.
   OperationID: GetTokenValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTokenValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SerializePrinterAndPageSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SerializePrinterAndPageSettings
   Description: Serialized the printer and page settings using the ERP library.
   OperationID: SerializePrinterAndPageSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SerializePrinterAndPageSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SerializePrinterAndPageSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeserializePrinterAndPageSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeserializePrinterAndPageSettings
   Description: Deserialize the printer and page settings using the ERP library.
   OperationID: DeserializePrinterAndPageSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeserializePrinterAndPageSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeserializePrinterAndPageSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserSessionAndVersion(epicorHeaders = None):
   """  
   Summary: Invoke method GetUserSessionAndVersion
   Description: Get the current user, session and version info.
   OperationID: GetUserSessionAndVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserSessionAndVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetHomepageCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHomepageCompany
   Description: Get the company info for KHP.
   OperationID: GetHomepageCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHomepageCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHomepageCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFeaturesAndLicenses(epicorHeaders = None):
   """  
   Summary: Invoke method GetFeaturesAndLicenses
   Description: Gets the object that provides the collection of Licensed Modules and Feature Flags.
   OperationID: GetFeaturesAndLicenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFeaturesAndLicenses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetTables
   Description: Gets the collection of <cref>ErpDataset</cref> when given a collection of system codes and dataset ids.
   OperationID: GetDatasetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConfirmDialogUserOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConfirmDialogUserOptions
   Description: Retrieves the personalization layer for the current user from Ice.XXXDef and extracts the ConfirmOptions
form options.
   OperationID: GetConfirmDialogUserOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConfirmDialogUserOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfirmDialogUserOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateConfirmDialogOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateConfirmDialogOptions
   Description: Updates the confirm dialog options into the XXXDef Personalization row.
   OperationID: UpdateConfirmDialogOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateConfirmDialogOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateConfirmDialogOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSearchOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSearchOptions
   Description: Gets the <cref>ErpSearchOptions</cref> object that describes the various search options.
   OperationID: GetSearchOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSearchOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteBaq
   Description: This method run an existing query with differing params and returns a collection of untyped datasets.
   OperationID: ExecuteBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBaq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBaq
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
Call Update method of an updatable query and return result dataset
   OperationID: UpdateBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBaqCustomAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBaqCustomAction
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
This method does nothing per se, but is useful if there are BPM directives
attached to the query. Directives can examine actionId value and perform some actions.
   OperationID: UpdateBaqCustomAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBaqCustomAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqCustomAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBaqFieldValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBaqFieldValidate
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
Calls FieldUpdate method of an updatable query and return result set.
   OperationID: UpdateBaqFieldValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBaqFieldValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqFieldValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBaqFieldUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBaqFieldUpdate
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
Calls FieldUpdate method of an updatable query and return result set.
   OperationID: UpdateBaqFieldUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBaqFieldUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqFieldUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserSettingsForView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUserSettingsForView
   Description: Gets the <cref>ErpUserSettingsForView</cref> object that has user settings for a view.
   OperationID: GetUserSettingsForView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUserSettingsForView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserSettingsForView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveGridLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveGridLayout
   Description: Save a grid layout.
   OperationID: SaveGridLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveGridLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveGridLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteGridLayout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteGridLayout
   Description: Deletes a grid layout for a user.
   OperationID: DeleteGridLayout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteGridLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteGridLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInstallationSettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstallationSettings
   Description: Gets the installation level Kinetic settings.
   OperationID: GetInstallationSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstallationSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_UpdateInstallationSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateInstallationSettings
   Description: Updates the installation level Kinetic settings.
   OperationID: UpdateInstallationSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateInstallationSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateInstallationSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLaunchModes(epicorHeaders = None):
   """  
   Summary: Invoke method GetLaunchModes
   Description: Returns launch modes json
   OperationID: GetLaunchModes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaunchModes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SendEmail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendEmail
   Description: Use the from email address and mail services from the current company company mail settings to send email.
   OperationID: SendEmail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SendEmailWithClientAttachments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendEmailWithClientAttachments
   Description: Use the from email address and mail services from the current company mail settings to send email from smart client.
   OperationID: SendEmailWithClientAttachments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendEmailWithClientAttachments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendEmailWithClientAttachments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLikeFieldForAdapter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLikeFieldForAdapter
   Description: Gets the related likeField given an adapter name.
   OperationID: GetLikeFieldForAdapter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLikeFieldForAdapter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLikeFieldForAdapter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAdapterList(epicorHeaders = None):
   """  
   Summary: Invoke method GetAdapterList
   Description: Gets the adapter name list.
   OperationID: GetAdapterList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdapterList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetGrowMetrics(epicorHeaders = None):
   """  
   Summary: Invoke method GetGrowMetrics
   Description: Gets grow's metrics.
   OperationID: GetGrowMetrics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrowMetrics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetEmbedGrowMetricUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEmbedGrowMetricUrl
   Description: Gets grow's metric url.
   OperationID: GetEmbedGrowMetricUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmbedGrowMetricUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmbedGrowMetricUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarTestConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarTestConnection
   Description: Test connection to DocStar system.
   OperationID: DocStarTestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarTestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarTestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarCreateBrowserUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarCreateBrowserUrl
   Description: Builds a URL in DocStar which will be used to open the attachment within DocStar.
   OperationID: DocStarCreateBrowserUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateBrowserUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateBrowserUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteGridLayout_input:
   """ Required : 
   formKey
   gridId
   """  
   def __init__(self, obj):
      self.formKey:str = obj["formKey"]
      """  The unique view key. Example: App.AbcCodeEntry.AbcCodeForm  """  
      self.gridId:str = obj["gridId"]
      """  The unique grid id from the view.  """  
      pass

class DeleteGridLayout_output:
   def __init__(self, obj):
      pass

class DeserializePrinterAndPageSettings_input:
   """ Required : 
   serializedPrinterSettings
   serializedPageSettings
   """  
   def __init__(self, obj):
      self.serializedPrinterSettings:str = obj["serializedPrinterSettings"]
      """  Serialized printer settings  """  
      self.serializedPageSettings:str = obj["serializedPageSettings"]
      """  Serialized page settings  """  
      pass

class DeserializePrinterAndPageSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_ErpPrinterProperties] = obj["returnObj"]
      pass

class DocStarCreateBrowserUrl_input:
   """ Required : 
   docTypeID
   documentId
   userName
   userPwd
   domain
   authType
   saveLogin
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type for the attachment  """  
      self.documentId:str = obj["documentId"]
      """  Document identifier  """  
      self.userName:str = obj["userName"]
      """  User Identifier  """  
      self.userPwd:str = obj["userPwd"]
      """  Encrypted user password  """  
      self.domain:str = obj["domain"]
      """  Domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type  """  
      self.saveLogin:bool = obj["saveLogin"]
      """  If true saves the user account information  """  
      pass

class DocStarCreateBrowserUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  URL for the attachment document within DocStar  """  
      pass

class DocStarTestConnection_input:
   """ Required : 
   docTypeID
   userName
   userPwd
   domain
   authType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to test company access  """  
      self.userName:str = obj["userName"]
      """  suggested user name  """  
      self.userPwd:str = obj["userPwd"]
      """  suggested password  """  
      self.domain:str = obj["domain"]
      """  domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - NTLM or USERNAME  """  
      pass

class DocStarTestConnection_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message that connection succeeded. In case of failure exception will be thrown  """  
      pass

class ExecuteBaq_input:
   """ Required : 
   queryID
   executionParams
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  The current Query ID  """  
      self.executionParams:list[Ice_Tablesets_QueryExecutionTableset] = obj["executionParams"]
      """  The collection of Query execution parameters (named parameter values, filtering and etc.)  """  
      pass

class ExecuteBaq_output:
   def __init__(self, obj):
      self.returnObj:object
      """  Returns the collection of results from each of the query executions.  """  
      pass

class GetAdapterList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetConfirmDialogUserOptions_input:
   """ Required : 
   formKey
   """  
   def __init__(self, obj):
      self.formKey:str = obj["formKey"]
      """  Key for the UI form.  """  
      pass

class GetConfirmDialogUserOptions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_ErpDialogConfirmOption] = obj["returnObj"]
      pass

class GetDatasetTables_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:list[Ice_BO_KineticErp_ErpDatasetId] = obj["ids"]
      """  The collection of system code and dataset ids.  """  
      pass

class GetDatasetTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_ErpDataset] = obj["returnObj"]
      """  The collection of <cref>ErpDataset</cref>.  """  
      pass

class GetEmbedGrowMetricUrl_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      """  Metric id  """  
      pass

class GetEmbedGrowMetricUrl_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetFeaturesAndLicenses_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_ErpFeaturesAndLicenses] = obj["returnObj"]
      pass

class GetGrowMetrics_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetHomepageCompany_input:
   """ Required : 
   companyId
   """  
   def __init__(self, obj):
      self.companyId:str = obj["companyId"]
      pass

class GetHomepageCompany_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetInstallationSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_InstallationSettings] = obj["returnObj"]
      pass

class GetLaunchModes_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetLikeFieldForAdapter_input:
   """ Required : 
   adapterName
   """  
   def __init__(self, obj):
      self.adapterName:str = obj["adapterName"]
      """  The adapter name  """  
      pass

class GetLikeFieldForAdapter_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSearchOptions_input:
   """ Required : 
   context
   """  
   def __init__(self, obj):
      self.context:list[Ice_BO_KineticErp_ErpSearchContext] = obj["context"]
      pass

class GetSearchOptions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_ErpSearchOptions] = obj["returnObj"]
      pass

class GetTokenList_input:
   """ Required : 
   tokenDataType
   """  
   def __init__(self, obj):
      self.tokenDataType:str = obj["tokenDataType"]
      """  Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear  """  
      pass

class GetTokenList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTokenValue_input:
   """ Required : 
   token
   """  
   def __init__(self, obj):
      self.token:str = obj["token"]
      """  Type of token  """  
      pass

class GetTokenValue_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.tokenValue:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetUserSessionAndVersion_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetUserSettingsForView_input:
   """ Required : 
   formKey
   """  
   def __init__(self, obj):
      self.formKey:str = obj["formKey"]
      """  The unique view key. Example: App.AbcCodeEntry.AbcCodeForm  """  
      pass

class GetUserSettingsForView_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_KineticErp_ErpUserSettingsForView] = obj["returnObj"]
      pass

class Ice_BO_KineticErp_ErpDataset:
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.datasetId:str = obj["datasetId"]
      self.tables:list[Ice_BO_KineticErp_ErpDatasetTable] = obj["tables"]
      pass

class Ice_BO_KineticErp_ErpDatasetId:
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.datasetId:str = obj["datasetId"]
      pass

class Ice_BO_KineticErp_ErpDatasetTable:
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.tableId:str = obj["tableId"]
      self.keys:str = obj["keys"]
      self.isPrimaryTable:bool = obj["isPrimaryTable"]
      self.childAttachmentTableName:str = obj["childAttachmentTableName"]
      self.parentAttachmentTableName:str = obj["parentAttachmentTableName"]
      self.changeLogTableName:str = obj["changeLogTableName"]
      self.memoTableName:str = obj["memoTableName"]
      pass

class Ice_BO_KineticErp_ErpDialogConfirmOption:
   def __init__(self, obj):
      self.optionName:str = obj["optionName"]
      self.optionEnabled:bool = obj["optionEnabled"]
      self.key:str = obj["key"]
      pass

class Ice_BO_KineticErp_ErpFeatureFlag:
   def __init__(self, obj):
      self.Identifier:str = obj["Identifier"]
      self.Name:str = obj["Name"]
      self.isEnabled:bool = obj["isEnabled"]
      pass

class Ice_BO_KineticErp_ErpFeaturesAndLicenses:
   def __init__(self, obj):
      self.FeatureFlags:list[Ice_BO_KineticErp_ErpFeatureFlag] = obj["FeatureFlags"]
      self.LicensedModules:list[Ice_BO_KineticErp_ErpLicensedModule] = obj["LicensedModules"]
      self.LicensedCsfModules:list[Ice_BO_KineticErp_ErpLicensedModule] = obj["LicensedCsfModules"]
      pass

class Ice_BO_KineticErp_ErpLicensedModule:
   def __init__(self, obj):
      self.Identifier:str = obj["Identifier"]
      self.Name:str = obj["Name"]
      self.isLicensed:bool = obj["isLicensed"]
      self.isEnabled:bool = obj["isEnabled"]
      pass

class Ice_BO_KineticErp_ErpPrinterProperties:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PrinterID:str = obj["PrinterID"]
      self.Description:str = obj["Description"]
      self.NetworkPath:str = obj["NetworkPath"]
      self.PageColor:bool = obj["PageColor"]
      self.PageLandscape:bool = obj["PageLandscape"]
      self.PageLeftMargin:int = obj["PageLeftMargin"]
      self.PageRightMargin:int = obj["PageRightMargin"]
      self.PageTopMargin:int = obj["PageTopMargin"]
      self.PageBottomMargin:int = obj["PageBottomMargin"]
      self.PagePaperSizeKind:str = obj["PagePaperSizeKind"]
      self.PagePaperHeight:int = obj["PagePaperHeight"]
      self.PagePaperWidth:int = obj["PagePaperWidth"]
      self.PagePaperSourceKind:str = obj["PagePaperSourceKind"]
      self.PagePrinterResolutionX:int = obj["PagePrinterResolutionX"]
      self.PagePrinterResolutionY:int = obj["PagePrinterResolutionY"]
      self.PageDuplex:str = obj["PageDuplex"]
      self.FromPage:int = obj["FromPage"]
      self.ToPage:int = obj["ToPage"]
      self.Copies:int = obj["Copies"]
      self.CanDuplex:bool = obj["CanDuplex"]
      self.Collate:bool = obj["Collate"]
      self.IsDefaultPrinter:bool = obj["IsDefaultPrinter"]
      self.PagePaperSourceRawKind:int = obj["PagePaperSourceRawKind"]
      self.PagePaperSourceName:str = obj["PagePaperSourceName"]
      self.PagePaperSizeName:str = obj["PagePaperSizeName"]
      pass

class Ice_BO_KineticErp_ErpSearchContext:
   def __init__(self, obj):
      self.product:str = obj["product"]
      self.searchName:str = obj["searchName"]
      self.calledFrom:str = obj["calledFrom"]
      self.likeTableName:str = obj["likeTableName"]
      self.likeFieldName:str = obj["likeFieldName"]
      self.includeQuickSearchWithNoCriteria:bool = obj["includeQuickSearchWithNoCriteria"]
      pass

class Ice_BO_KineticErp_ErpSearchOptions:
   def __init__(self, obj):
      self.namedSearches:list[Ice_IceTableset] = obj["namedSearches"]
      self.quickSearches:list[Ice_IceTableset] = obj["quickSearches"]
      self.baqSearches:list[Ice_IceTableset] = obj["baqSearches"]
      self.advancedSearches:list[Ice_IceTableset] = obj["advancedSearches"]
      self.baseDefaultQuickSearch:str = obj["baseDefaultQuickSearch"]
      self.contextDefaultQuickSearch:str = obj["contextDefaultQuickSearch"]
      pass

class Ice_BO_KineticErp_ErpUserSettingsForView:
   def __init__(self, obj):
      self.gridLayouts      #schema had no properties on an object.
      pass

class Ice_BO_KineticErp_IceEmailMessageRequest:
   def __init__(self, obj):
      self.from:str = obj["from"]
      self.attachments:str = obj["attachments"]
      self.removeAttachmentFromSpecialFolder:bool = obj["removeAttachmentFromSpecialFolder"]
      self.attachmentSpecialFolder:int = obj["attachmentSpecialFolder"]
      self.body:str = obj["body"]
      self.subject:str = obj["subject"]
      self.to:str = obj["to"]
      self.cc:str = obj["cc"]
      self.bcc:str = obj["bcc"]
      self.priority:int = obj["priority"]
      self.isBodyHtml:bool = obj["isBodyHtml"]
      pass

class Ice_BO_KineticErp_IceEmailMessageRequestWithIncludedAttachments:
   def __init__(self, obj):
      self.from:str = obj["from"]
      self.includedAttachments:list[System_Collections_Generic_KeyValuePair_System_String_System_ByteArray] = obj["includedAttachments"]
      self.body:str = obj["body"]
      self.subject:str = obj["subject"]
      self.to:str = obj["to"]
      self.cc:str = obj["cc"]
      self.bcc:str = obj["bcc"]
      self.priority:int = obj["priority"]
      self.isBodyHtml:bool = obj["isBodyHtml"]
      pass

class Ice_BO_KineticErp_InstallationSettings:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.Color:str = obj["Color"]
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

class Ice_IceTableset:
   def __init__(self, obj):
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExecutionFilterRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Neg:bool = obj["Neg"]
      self.CompOp:str = obj["CompOp"]
      self.RValue:str = obj["RValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_ExecutionParameterRow:
   def __init__(self, obj):
      self.ParameterID:str = obj["ParameterID"]
      self.ParameterValue:str = obj["ParameterValue"]
      self.ValueType:str = obj["ValueType"]
      self.IsEmpty:bool = obj["IsEmpty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_ExecutionSettingRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.Value:str = obj["Value"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_ExecutionValueSetItemsRow:
   def __init__(self, obj):
      self.ValueSetID:str = obj["ValueSetID"]
      self.ItemValue:str = obj["ItemValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryExecutionTableset:
   def __init__(self, obj):
      self.ExecutionFilter:list[Ice_Tablesets_ExecutionFilterRow] = obj["ExecutionFilter"]
      self.ExecutionParameter:list[Ice_Tablesets_ExecutionParameterRow] = obj["ExecutionParameter"]
      self.ExecutionSetting:list[Ice_Tablesets_ExecutionSettingRow] = obj["ExecutionSetting"]
      self.ExecutionValueSetItems:list[Ice_Tablesets_ExecutionValueSetItemsRow] = obj["ExecutionValueSetItems"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class SaveGridLayout_input:
   """ Required : 
   formKey
   gridId
   layout
   """  
   def __init__(self, obj):
      self.formKey:str = obj["formKey"]
      """  The unique view key. Example: App.AbcCodeEntry.AbcCodeForm  """  
      self.gridId:str = obj["gridId"]
      """  The unique grid id from the view.  """  
      self.layout:str = obj["layout"]
      """  The serialized layout for the grid  """  
      pass

class SaveGridLayout_output:
   def __init__(self, obj):
      pass

class SendEmailWithClientAttachments_input:
   """ Required : 
   message
   """  
   def __init__(self, obj):
      self.message:list[Ice_BO_KineticErp_IceEmailMessageRequestWithIncludedAttachments] = obj["message"]
      pass

class SendEmailWithClientAttachments_output:
   def __init__(self, obj):
      pass

class SendEmail_input:
   """ Required : 
   message
   """  
   def __init__(self, obj):
      self.message:list[Ice_BO_KineticErp_IceEmailMessageRequest] = obj["message"]
      pass

class SendEmail_output:
   def __init__(self, obj):
      pass

class SerializePrinterAndPageSettings_input:
   """ Required : 
   printerPageProperties
   """  
   def __init__(self, obj):
      self.printerPageProperties:list[Ice_BO_KineticErp_ErpPrinterProperties] = obj["printerPageProperties"]
      pass

class SerializePrinterAndPageSettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.serializedPrinterSettings:str = obj["parameters"]
      self.serializedPageSettings:str = obj["parameters"]
      pass

      """  output parameters  """  

class System_Collections_Generic_KeyValuePair_System_String_System_ByteArray:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      pass

class UpdateBaqCustomAction_input:
   """ Required : 
   queryID
   actionID
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.actionID:str = obj["actionID"]
      """  An action id  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class UpdateBaqCustomAction_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class UpdateBaqFieldUpdate_input:
   """ Required : 
   queryID
   fieldName
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.fieldName:str = obj["fieldName"]
      """  Name of an updatable field  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

class UpdateBaqFieldUpdate_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

class UpdateBaqFieldValidate_input:
   """ Required : 
   queryID
   fieldName
   fieldValue
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.fieldName:str = obj["fieldName"]
      """  Name of an updatable field  """  
      self.fieldValue      #schema had no properties on an object.
      """  The proposed value for the field  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset with a changed row  """  
      pass

class UpdateBaqFieldValidate_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Query result dataset with a row where the field is going to be updated  """  
      pass

   def parameters(self, obj):
      self.isValid:bool = obj["isValid"]
      pass

      """  output parameters  """  

class UpdateBaq_input:
   """ Required : 
   queryID
   queryResultDataset
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Updatable query id  """  
      self.queryResultDataset      #schema had no properties on an object.
      """  Query result dataset  """  
      pass

class UpdateBaq_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Result of Update method call. Usually this is incoming query result dataset with some changes  """  
      pass

class UpdateConfirmDialogOptions_input:
   """ Required : 
   formKey
   confirmOptions
   """  
   def __init__(self, obj):
      self.formKey:str = obj["formKey"]
      """  The form key.  """  
      self.confirmOptions:list[Ice_BO_KineticErp_ErpDialogConfirmOption] = obj["confirmOptions"]
      """  The confirmOptions (all items are expected).  """  
      pass

class UpdateConfirmDialogOptions_output:
   def __init__(self, obj):
      pass

class UpdateInstallationSettings_input:
   """ Required : 
   installationSettings
   """  
   def __init__(self, obj):
      self.installationSettings:list[Ice_BO_KineticErp_InstallationSettings] = obj["installationSettings"]
      pass

class UpdateInstallationSettings_output:
   def __init__(self, obj):
      pass

