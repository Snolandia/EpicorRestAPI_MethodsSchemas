import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.NamedSearchSvc
# Description: Stores user-defined search parameters, along with two child tables, ControlSettings and WhereClauses.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_NamedSearches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NamedSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NamedSearches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NamedSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches",headers=creds) as resp:
           return await resp.json()

async def post_NamedSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NamedSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.NamedSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.NamedSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom(Company, SearchForm, NSId, UserID, CalledFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NamedSearch item
   Description: Calls GetByID to retrieve the NamedSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NamedSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.NamedSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom(Company, SearchForm, NSId, UserID, CalledFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NamedSearch for the service
   Description: Calls UpdateExt to update NamedSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NamedSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.NamedSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom(Company, SearchForm, NSId, UserID, CalledFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NamedSearch item
   Description: Call UpdateExt to delete NamedSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NamedSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_ControlSettings(Company, SearchForm, NSId, UserID, CalledFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ControlSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ControlSettings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ControlSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/ControlSettings",headers=creds) as resp:
           return await resp.json()

async def get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company, SearchForm, NSId, UserID, CalledFrom, ControlGuid, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlSetting item
   Description: Calls GetByID to retrieve the ControlSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlSetting1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param ControlGuid: Desc: ControlGuid   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")",headers=creds) as resp:
           return await resp.json()

async def get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_WhereClauses(Company, SearchForm, NSId, UserID, CalledFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhereClauses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhereClauses1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/WhereClauses",headers=creds) as resp:
           return await resp.json()

async def get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company, SearchForm, NSId, UserID, CalledFrom, TableName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhereClause item
   Description: Calls GetByID to retrieve the WhereClause item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClause1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ControlSettings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ControlSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlSettings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ControlSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings",headers=creds) as resp:
           return await resp.json()

async def post_ControlSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company, SearchForm, NSId, UserID, CalledFrom, ControlGuid, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlSetting item
   Description: Calls GetByID to retrieve the ControlSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param ControlGuid: Desc: ControlGuid   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company, SearchForm, NSId, UserID, CalledFrom, ControlGuid, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ControlSetting for the service
   Description: Calls UpdateExt to update ControlSetting. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param ControlGuid: Desc: ControlGuid   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company, SearchForm, NSId, UserID, CalledFrom, ControlGuid, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ControlSetting item
   Description: Call UpdateExt to delete ControlSetting item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlSetting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param ControlGuid: Desc: ControlGuid   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhereClauses(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhereClauses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhereClauses
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses",headers=creds) as resp:
           return await resp.json()

async def post_WhereClauses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhereClauses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company, SearchForm, NSId, UserID, CalledFrom, TableName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhereClause item
   Description: Calls GetByID to retrieve the WhereClause item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClause
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company, SearchForm, NSId, UserID, CalledFrom, TableName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhereClause for the service
   Description: Calls UpdateExt to update WhereClause. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhereClause
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company, SearchForm, NSId, UserID, CalledFrom, TableName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhereClause item
   Description: Call UpdateExt to delete WhereClause item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhereClause
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SearchForm: Desc: SearchForm   Required: True   Allow empty value : True
      :param NSId: Desc: NSId   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NamedSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseNamedSearch, whereClauseControlSetting, whereClauseWhereClause, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseNamedSearch=" + whereClauseNamedSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseControlSetting=" + whereClauseControlSetting
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhereClause=" + whereClauseWhereClause
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(searchForm, nsId, userID, calledFrom, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "searchForm=" + searchForm
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "nsId=" + nsId
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "userID=" + userID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "calledFrom=" + calledFrom

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNamedSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNamedSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNamedSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNamedSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNamedSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewControlSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewControlSetting
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewControlSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhereClause
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ControlSettingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ControlSettingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_NamedSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_NamedSearchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_WhereClauseRow] = obj["value"]
      pass

class Ice_Tablesets_ControlSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Search Form  """  
      self.NSId:str = obj["NSId"]
      """  Namespace ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  Called From  """  
      self.ControlGuid:str = obj["ControlGuid"]
      """  Control GUID  """  
      self.ControlValue:str = obj["ControlValue"]
      """  Control Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EpBinding:str = obj["EpBinding"]
      """  EpBinding  """  
      self.ComponentID:str = obj["ComponentID"]
      """  ComponentID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_NamedSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Name of base search form  """  
      self.NSId:str = obj["NSId"]
      """  Named Search ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  UI from which the search is called from  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Default named search flag  """  
      self.AutoExecute:bool = obj["AutoExecute"]
      """  Auto Execute flag  """  
      self.UnpinCrit:bool = obj["UnpinCrit"]
      """  Can unpin Criteria  """  
      self.IsShared:bool = obj["IsShared"]
      """  Can be shared flag  """  
      self.ShareType:str = obj["ShareType"]
      """  Share Type  """  
      self.ReturnAll:bool = obj["ReturnAll"]
      """  Return all rows flag.  """  
      self.MaxRows:int = obj["MaxRows"]
      """  Maximum number search rows.  """  
      self.AutoSelect:bool = obj["AutoSelect"]
      """  Auto select flag  """  
      self.DataSetMode:str = obj["DataSetMode"]
      """  Value will be one of: "RowsDataSet" or "ListDataSet"  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ProductID:str = obj["ProductID"]
      """  "VN" = Vantage; "VS" = Vista  """  
      self.ActiveTab:str = obj["ActiveTab"]
      """  Active panel  """  
      self.GroupOn:bool = obj["GroupOn"]
      """  Can use Group By flag  """  
      self.GroupBy:str = obj["GroupBy"]
      """  Group by column  """  
      self.SearchType:str = obj["SearchType"]
      """  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  """  
      self.SearchUsing:str = obj["SearchUsing"]
      """  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  """  
      self.SortByColumn:str = obj["SortByColumn"]
      """  Column to sort by  """  
      self.SortOrder:str = obj["SortOrder"]
      """  A for Ascending or D for Descending  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_NamedSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Name of base search form  """  
      self.NSId:str = obj["NSId"]
      """  Named Search ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  UI from which the search is called from  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Default named search flag  """  
      self.AutoExecute:bool = obj["AutoExecute"]
      """  Auto Execute flag  """  
      self.UnpinCrit:bool = obj["UnpinCrit"]
      """  Can unpin Criteria  """  
      self.IsShared:bool = obj["IsShared"]
      """  Can be shared flag  """  
      self.ShareType:str = obj["ShareType"]
      """  Share Type  """  
      self.ReturnAll:bool = obj["ReturnAll"]
      """  Return all rows flag.  """  
      self.MaxRows:int = obj["MaxRows"]
      """  Maximum number search rows.  """  
      self.AutoSelect:bool = obj["AutoSelect"]
      """  Auto select flag  """  
      self.DataSetMode:str = obj["DataSetMode"]
      """  Value will be one of: "RowsDataSet" or "ListDataSet"  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ProductID:str = obj["ProductID"]
      """  "VN" = Vantage; "VS" = Vista  """  
      self.ActiveTab:str = obj["ActiveTab"]
      """  Active panel  """  
      self.GroupOn:bool = obj["GroupOn"]
      """  Can use Group By flag  """  
      self.GroupBy:str = obj["GroupBy"]
      """  Group by column  """  
      self.SearchType:str = obj["SearchType"]
      """  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  """  
      self.SearchUsing:str = obj["SearchUsing"]
      """  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  """  
      self.SortByColumn:str = obj["SortByColumn"]
      """  Column to sort by  """  
      self.SortOrder:str = obj["SortOrder"]
      """  A for Ascending or D for Descending  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_WhereClauseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Search Form  """  
      self.NSId:str = obj["NSId"]
      """  Namespace ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  Called From  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.WhereClause1:str = obj["WhereClause1"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   searchForm
   nsId
   userID
   calledFrom
   """  
   def __init__(self, obj):
      self.searchForm:str = obj["searchForm"]
      self.nsId:str = obj["nsId"]
      self.userID:str = obj["userID"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   searchForm
   nsId
   userID
   calledFrom
   """  
   def __init__(self, obj):
      self.searchForm:str = obj["searchForm"]
      self.nsId:str = obj["nsId"]
      self.userID:str = obj["userID"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_NamedSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_NamedSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_NamedSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_NamedSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewControlSetting_input:
   """ Required : 
   ds
   searchForm
   nsId
   userID
   calledFrom
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      self.searchForm:str = obj["searchForm"]
      self.nsId:str = obj["nsId"]
      self.userID:str = obj["userID"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetNewControlSetting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewNamedSearch_input:
   """ Required : 
   ds
   searchForm
   nsId
   userID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      self.searchForm:str = obj["searchForm"]
      self.nsId:str = obj["nsId"]
      self.userID:str = obj["userID"]
      pass

class GetNewNamedSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhereClause_input:
   """ Required : 
   ds
   searchForm
   nsId
   userID
   calledFrom
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      self.searchForm:str = obj["searchForm"]
      self.nsId:str = obj["nsId"]
      self.userID:str = obj["userID"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetNewWhereClause_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseNamedSearch
   whereClauseControlSetting
   whereClauseWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseNamedSearch:str = obj["whereClauseNamedSearch"]
      self.whereClauseControlSetting:str = obj["whereClauseControlSetting"]
      self.whereClauseWhereClause:str = obj["whereClauseWhereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_NamedSearchTableset] = obj["returnObj"]
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

class Ice_Tablesets_ControlSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Search Form  """  
      self.NSId:str = obj["NSId"]
      """  Namespace ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  Called From  """  
      self.ControlGuid:str = obj["ControlGuid"]
      """  Control GUID  """  
      self.ControlValue:str = obj["ControlValue"]
      """  Control Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EpBinding:str = obj["EpBinding"]
      """  EpBinding  """  
      self.ComponentID:str = obj["ComponentID"]
      """  ComponentID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_NamedSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Name of base search form  """  
      self.NSId:str = obj["NSId"]
      """  Named Search ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  UI from which the search is called from  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Default named search flag  """  
      self.AutoExecute:bool = obj["AutoExecute"]
      """  Auto Execute flag  """  
      self.UnpinCrit:bool = obj["UnpinCrit"]
      """  Can unpin Criteria  """  
      self.IsShared:bool = obj["IsShared"]
      """  Can be shared flag  """  
      self.ShareType:str = obj["ShareType"]
      """  Share Type  """  
      self.ReturnAll:bool = obj["ReturnAll"]
      """  Return all rows flag.  """  
      self.MaxRows:int = obj["MaxRows"]
      """  Maximum number search rows.  """  
      self.AutoSelect:bool = obj["AutoSelect"]
      """  Auto select flag  """  
      self.DataSetMode:str = obj["DataSetMode"]
      """  Value will be one of: "RowsDataSet" or "ListDataSet"  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ProductID:str = obj["ProductID"]
      """  "VN" = Vantage; "VS" = Vista  """  
      self.ActiveTab:str = obj["ActiveTab"]
      """  Active panel  """  
      self.GroupOn:bool = obj["GroupOn"]
      """  Can use Group By flag  """  
      self.GroupBy:str = obj["GroupBy"]
      """  Group by column  """  
      self.SearchType:str = obj["SearchType"]
      """  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  """  
      self.SearchUsing:str = obj["SearchUsing"]
      """  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  """  
      self.SortByColumn:str = obj["SortByColumn"]
      """  Column to sort by  """  
      self.SortOrder:str = obj["SortOrder"]
      """  A for Ascending or D for Descending  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_NamedSearchListTableset:
   def __init__(self, obj):
      self.NamedSearchList:list[Ice_Tablesets_NamedSearchListRow] = obj["NamedSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_NamedSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Name of base search form  """  
      self.NSId:str = obj["NSId"]
      """  Named Search ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  UI from which the search is called from  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Default named search flag  """  
      self.AutoExecute:bool = obj["AutoExecute"]
      """  Auto Execute flag  """  
      self.UnpinCrit:bool = obj["UnpinCrit"]
      """  Can unpin Criteria  """  
      self.IsShared:bool = obj["IsShared"]
      """  Can be shared flag  """  
      self.ShareType:str = obj["ShareType"]
      """  Share Type  """  
      self.ReturnAll:bool = obj["ReturnAll"]
      """  Return all rows flag.  """  
      self.MaxRows:int = obj["MaxRows"]
      """  Maximum number search rows.  """  
      self.AutoSelect:bool = obj["AutoSelect"]
      """  Auto select flag  """  
      self.DataSetMode:str = obj["DataSetMode"]
      """  Value will be one of: "RowsDataSet" or "ListDataSet"  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ProductID:str = obj["ProductID"]
      """  "VN" = Vantage; "VS" = Vista  """  
      self.ActiveTab:str = obj["ActiveTab"]
      """  Active panel  """  
      self.GroupOn:bool = obj["GroupOn"]
      """  Can use Group By flag  """  
      self.GroupBy:str = obj["GroupBy"]
      """  Group by column  """  
      self.SearchType:str = obj["SearchType"]
      """  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  """  
      self.SearchUsing:str = obj["SearchUsing"]
      """  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  """  
      self.SortByColumn:str = obj["SortByColumn"]
      """  Column to sort by  """  
      self.SortOrder:str = obj["SortOrder"]
      """  A for Ascending or D for Descending  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_NamedSearchTableset:
   def __init__(self, obj):
      self.NamedSearch:list[Ice_Tablesets_NamedSearchRow] = obj["NamedSearch"]
      self.ControlSetting:list[Ice_Tablesets_ControlSettingRow] = obj["ControlSetting"]
      self.WhereClause:list[Ice_Tablesets_WhereClauseRow] = obj["WhereClause"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtNamedSearchTableset:
   def __init__(self, obj):
      self.NamedSearch:list[Ice_Tablesets_NamedSearchRow] = obj["NamedSearch"]
      self.ControlSetting:list[Ice_Tablesets_ControlSettingRow] = obj["ControlSetting"]
      self.WhereClause:list[Ice_Tablesets_WhereClauseRow] = obj["WhereClause"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_WhereClauseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SearchForm:str = obj["SearchForm"]
      """  Search Form  """  
      self.NSId:str = obj["NSId"]
      """  Namespace ID  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  Called From  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Where Clause  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtNamedSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtNamedSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_NamedSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

