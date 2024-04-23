import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.MailSettingSvc
# Description: Company settings for emails.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MailSettings(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MailSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MailSettings
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MailSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings",headers=creds) as resp:
           return await resp.json()

async def post_MailSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MailSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MailSettingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MailSettingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MailSettings_Company(Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MailSetting item
   Description: Calls GetByID to retrieve the MailSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MailSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MailSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MailSettings_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MailSetting for the service
   Description: Calls UpdateExt to update MailSetting. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MailSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MailSettingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MailSettings_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MailSetting item
   Description: Call UpdateExt to delete MailSetting item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MailSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_MailSettings_Company_MailAppSettings(Company, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MailAppSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MailAppSettings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MailAppSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")/MailAppSettings",headers=creds) as resp:
           return await resp.json()

async def get_MailSettings_Company_MailAppSettings_Company_AppType(Company, AppType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MailAppSetting item
   Description: Calls GetByID to retrieve the MailAppSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MailAppSetting1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MailAppSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")/MailAppSettings(" + Company + "," + AppType + ")",headers=creds) as resp:
           return await resp.json()

async def get_MailSettings_Company_MailThrottlingSettings(Company, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MailThrottlingSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MailThrottlingSettings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MailThrottlingSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")/MailThrottlingSettings",headers=creds) as resp:
           return await resp.json()

async def get_MailSettings_Company_MailThrottlingSettings_Company_AppType_Origin(Company, AppType, Origin, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MailThrottlingSetting item
   Description: Calls GetByID to retrieve the MailThrottlingSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MailThrottlingSetting1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param Origin: Desc: Origin   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MailThrottlingSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailSettings(" + Company + ")/MailThrottlingSettings(" + Company + "," + AppType + "," + Origin + ")",headers=creds) as resp:
           return await resp.json()

async def get_MailAppSettings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MailAppSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MailAppSettings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MailAppSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailAppSettings",headers=creds) as resp:
           return await resp.json()

async def post_MailAppSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MailAppSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MailAppSettingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MailAppSettingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailAppSettings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MailAppSettings_Company_AppType(Company, AppType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MailAppSetting item
   Description: Calls GetByID to retrieve the MailAppSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MailAppSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MailAppSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailAppSettings(" + Company + "," + AppType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MailAppSettings_Company_AppType(Company, AppType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MailAppSetting for the service
   Description: Calls UpdateExt to update MailAppSetting. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MailAppSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MailAppSettingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailAppSettings(" + Company + "," + AppType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MailAppSettings_Company_AppType(Company, AppType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MailAppSetting item
   Description: Call UpdateExt to delete MailAppSetting item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MailAppSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailAppSettings(" + Company + "," + AppType + ")",headers=creds) as resp:
           return await resp.json()

async def get_MailThrottlingSettings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MailThrottlingSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MailThrottlingSettings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MailThrottlingSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailThrottlingSettings",headers=creds) as resp:
           return await resp.json()

async def post_MailThrottlingSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MailThrottlingSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MailThrottlingSettingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MailThrottlingSettingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailThrottlingSettings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MailThrottlingSettings_Company_AppType_Origin(Company, AppType, Origin, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MailThrottlingSetting item
   Description: Calls GetByID to retrieve the MailThrottlingSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MailThrottlingSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param Origin: Desc: Origin   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MailThrottlingSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailThrottlingSettings(" + Company + "," + AppType + "," + Origin + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MailThrottlingSettings_Company_AppType_Origin(Company, AppType, Origin, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MailThrottlingSetting for the service
   Description: Calls UpdateExt to update MailThrottlingSetting. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MailThrottlingSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param Origin: Desc: Origin   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MailThrottlingSettingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailThrottlingSettings(" + Company + "," + AppType + "," + Origin + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MailThrottlingSettings_Company_AppType_Origin(Company, AppType, Origin, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MailThrottlingSetting item
   Description: Call UpdateExt to delete MailThrottlingSetting item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MailThrottlingSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AppType: Desc: AppType   Required: True   Allow empty value : True
      :param Origin: Desc: Origin   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/MailThrottlingSettings(" + Company + "," + AppType + "," + Origin + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MailSettingListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMailSetting, whereClauseMailAppSetting, whereClauseMailThrottlingSetting, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMailSetting=" + whereClauseMailSetting
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMailAppSetting=" + whereClauseMailAppSetting
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMailThrottlingSetting=" + whereClauseMailThrottlingSetting
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "company=" + company

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ResetThrottleCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetThrottleCount
   Description: Resets the current count to zero.
   OperationID: ResetThrottleCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetThrottleCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetThrottleCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestMailSend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestMailSend
   Description: Send test email.
   OperationID: TestMailSend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestMailSend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestMailSend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMailSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMailSetting
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMailSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMailSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMailSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMailAppSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMailAppSetting
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMailAppSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMailAppSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMailAppSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMailThrottlingSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMailThrottlingSetting
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMailThrottlingSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMailThrottlingSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMailThrottlingSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MailSettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MailAppSettingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MailAppSettingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MailSettingListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MailSettingListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MailSettingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MailSettingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MailThrottlingSettingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MailThrottlingSettingRow] = obj["value"]
      pass

class Ice_Tablesets_MailAppSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AppType:str = obj["AppType"]
      """  AppType  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.ApplicationSecret:str = obj["ApplicationSecret"]
      """  ApplicationSecret  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.EndPoint:str = obj["EndPoint"]
      """  EndPoint  """  
      self.SendUser:str = obj["SendUser"]
      """  SendUser  """  
      self.UseSendAs:bool = obj["UseSendAs"]
      """  UseSendAs  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UseDefaultEndpoint:bool = obj["UseDefaultEndpoint"]
      """  Use default authority endpoint.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MailSettingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  EmailFromAddr  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  EmailFromLabel  """  
      self.SMTPServer:str = obj["SMTPServer"]
      """  SMTPServer  """  
      self.DefaultMailer:str = obj["DefaultMailer"]
      """  DefaultMailer  """  
      self.ReportMailer:str = obj["ReportMailer"]
      """  ReportMailer  """  
      self.TrackMailSend:bool = obj["TrackMailSend"]
      """  TrackMailSend  """  
      self.LogPurgeIntervalDays:int = obj["LogPurgeIntervalDays"]
      """  LogPurgeIntervalDays  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MailSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  EmailFromAddr  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  EmailFromLabel  """  
      self.SMTPServer:str = obj["SMTPServer"]
      """  SMTPServer  """  
      self.SMTPPort:int = obj["SMTPPort"]
      """  SMTPPort  """  
      self.SMTPAcct:str = obj["SMTPAcct"]
      """  SMTPAcct  """  
      self.SMTPAcctPW:str = obj["SMTPAcctPW"]
      """  SMTPAcctPW  """  
      self.IsSMTPCredential:bool = obj["IsSMTPCredential"]
      """  IsSMTPCredential  """  
      self.SMTPEnableSSL:bool = obj["SMTPEnableSSL"]
      """  SMTPEnableSSL  """  
      self.DefaultMailer:str = obj["DefaultMailer"]
      """  DefaultMailer  """  
      self.ReportMailer:str = obj["ReportMailer"]
      """  ReportMailer  """  
      self.TrackMailSend:bool = obj["TrackMailSend"]
      """  TrackMailSend  """  
      self.LogPurgeIntervalDays:int = obj["LogPurgeIntervalDays"]
      """  LogPurgeIntervalDays  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MailThrottlingSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AppType:str = obj["AppType"]
      """  AppType  """  
      self.Origin:str = obj["Origin"]
      """  Origin  """  
      self.Threshold:int = obj["Threshold"]
      """  Threshold  """  
      self.CurrentCount:int = obj["CurrentCount"]
      """  CurrentCount  """  
      self.TimeframeType:str = obj["TimeframeType"]
      """  TimeframeType  """  
      self.Timeframe:int = obj["Timeframe"]
      """  Timeframe  """  
      self.LastResetOn:str = obj["LastResetOn"]
      """  LastResetOn  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.SendNotification:bool = obj["SendNotification"]
      """  SendNotification  """  
      self.NotificationEmailTo:str = obj["NotificationEmailTo"]
      """  NotificationEmailTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MailSettingTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MailSettingTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MailSettingTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MailSettingListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMailAppSetting_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewMailAppSetting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMailSetting_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      pass

class GetNewMailSetting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMailThrottlingSetting_input:
   """ Required : 
   ds
   company
   appType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.appType:str = obj["appType"]
      pass

class GetNewMailThrottlingSetting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMailSetting
   whereClauseMailAppSetting
   whereClauseMailThrottlingSetting
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMailSetting:str = obj["whereClauseMailSetting"]
      self.whereClauseMailAppSetting:str = obj["whereClauseMailAppSetting"]
      self.whereClauseMailThrottlingSetting:str = obj["whereClauseMailThrottlingSetting"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MailSettingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

class Ice_Tablesets_MailAppSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AppType:str = obj["AppType"]
      """  AppType  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.ApplicationSecret:str = obj["ApplicationSecret"]
      """  ApplicationSecret  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.EndPoint:str = obj["EndPoint"]
      """  EndPoint  """  
      self.SendUser:str = obj["SendUser"]
      """  SendUser  """  
      self.UseSendAs:bool = obj["UseSendAs"]
      """  UseSendAs  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UseDefaultEndpoint:bool = obj["UseDefaultEndpoint"]
      """  Use default authority endpoint.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MailSettingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  EmailFromAddr  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  EmailFromLabel  """  
      self.SMTPServer:str = obj["SMTPServer"]
      """  SMTPServer  """  
      self.DefaultMailer:str = obj["DefaultMailer"]
      """  DefaultMailer  """  
      self.ReportMailer:str = obj["ReportMailer"]
      """  ReportMailer  """  
      self.TrackMailSend:bool = obj["TrackMailSend"]
      """  TrackMailSend  """  
      self.LogPurgeIntervalDays:int = obj["LogPurgeIntervalDays"]
      """  LogPurgeIntervalDays  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MailSettingListTableset:
   def __init__(self, obj):
      self.MailSettingList:list[Ice_Tablesets_MailSettingListRow] = obj["MailSettingList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_MailSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  EmailFromAddr  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  EmailFromLabel  """  
      self.SMTPServer:str = obj["SMTPServer"]
      """  SMTPServer  """  
      self.SMTPPort:int = obj["SMTPPort"]
      """  SMTPPort  """  
      self.SMTPAcct:str = obj["SMTPAcct"]
      """  SMTPAcct  """  
      self.SMTPAcctPW:str = obj["SMTPAcctPW"]
      """  SMTPAcctPW  """  
      self.IsSMTPCredential:bool = obj["IsSMTPCredential"]
      """  IsSMTPCredential  """  
      self.SMTPEnableSSL:bool = obj["SMTPEnableSSL"]
      """  SMTPEnableSSL  """  
      self.DefaultMailer:str = obj["DefaultMailer"]
      """  DefaultMailer  """  
      self.ReportMailer:str = obj["ReportMailer"]
      """  ReportMailer  """  
      self.TrackMailSend:bool = obj["TrackMailSend"]
      """  TrackMailSend  """  
      self.LogPurgeIntervalDays:int = obj["LogPurgeIntervalDays"]
      """  LogPurgeIntervalDays  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MailSettingTableset:
   def __init__(self, obj):
      self.MailSetting:list[Ice_Tablesets_MailSettingRow] = obj["MailSetting"]
      self.MailAppSetting:list[Ice_Tablesets_MailAppSettingRow] = obj["MailAppSetting"]
      self.MailThrottlingSetting:list[Ice_Tablesets_MailThrottlingSettingRow] = obj["MailThrottlingSetting"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_MailThrottlingSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AppType:str = obj["AppType"]
      """  AppType  """  
      self.Origin:str = obj["Origin"]
      """  Origin  """  
      self.Threshold:int = obj["Threshold"]
      """  Threshold  """  
      self.CurrentCount:int = obj["CurrentCount"]
      """  CurrentCount  """  
      self.TimeframeType:str = obj["TimeframeType"]
      """  TimeframeType  """  
      self.Timeframe:int = obj["Timeframe"]
      """  Timeframe  """  
      self.LastResetOn:str = obj["LastResetOn"]
      """  LastResetOn  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.SendNotification:bool = obj["SendNotification"]
      """  SendNotification  """  
      self.NotificationEmailTo:str = obj["NotificationEmailTo"]
      """  NotificationEmailTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtMailSettingTableset:
   def __init__(self, obj):
      self.MailSetting:list[Ice_Tablesets_MailSettingRow] = obj["MailSetting"]
      self.MailAppSetting:list[Ice_Tablesets_MailAppSettingRow] = obj["MailAppSetting"]
      self.MailThrottlingSetting:list[Ice_Tablesets_MailThrottlingSettingRow] = obj["MailThrottlingSetting"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ResetThrottleCount_input:
   """ Required : 
   appType
   origin
   """  
   def __init__(self, obj):
      self.appType:str = obj["appType"]
      """  The AppType  """  
      self.origin:str = obj["origin"]
      """  The Origin type.  """  
      pass

class ResetThrottleCount_output:
   def __init__(self, obj):
      pass

class TestMailSend_input:
   """ Required : 
   mailerType
   from
   to
   subject
   testSettings
   """  
   def __init__(self, obj):
      self.mailerType:str = obj["mailerType"]
      """  Email application type to use.  """  
      self.from:str = obj["from"]
      """  Mail address From (optional).  """  
      self.to:str = obj["to"]
      """  Mail address To (required).  """  
      self.subject:str = obj["subject"]
      """  Test email subject.  """  
      self.testSettings:list[Ice_Tablesets_MailSettingTableset] = obj["testSettings"]
      pass

class TestMailSend_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtMailSettingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtMailSettingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MailSettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

