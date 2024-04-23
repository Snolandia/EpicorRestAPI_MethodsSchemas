import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AccessScopeSvc
# Description: AccessScope service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AccessScopes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccessScopes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes",headers=creds) as resp:
           return await resp.json()

async def post_AccessScopes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccessScopes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AccessScopeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AccessScopeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AccessScopes_Company_AccessScopeID(Company, AccessScopeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AccessScope item
   Description: Calls GetByID to retrieve the AccessScope item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScope
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AccessScopeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AccessScopes_Company_AccessScopeID(Company, AccessScopeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AccessScope for the service
   Description: Calls UpdateExt to update AccessScope. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccessScope
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AccessScopeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AccessScopes_Company_AccessScopeID(Company, AccessScopeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AccessScope item
   Description: Call UpdateExt to delete AccessScope item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccessScope
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopes_Company_AccessScopeID_AccessScopeEntities(Company, AccessScopeID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AccessScopeEntities items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AccessScopeEntities1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")/AccessScopeEntities",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopes_Company_AccessScopeID_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company, AccessScopeID, EntityType, EntityID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AccessScopeEntity item
   Description: Calls GetByID to retrieve the AccessScopeEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeEntity1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopes(" + Company + "," + AccessScopeID + ")/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopeEntities(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AccessScopeEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccessScopeEntities
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities",headers=creds) as resp:
           return await resp.json()

async def post_AccessScopeEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccessScopeEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company, AccessScopeID, EntityType, EntityID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AccessScopeEntity item
   Description: Calls GetByID to retrieve the AccessScopeEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company, AccessScopeID, EntityType, EntityID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AccessScopeEntity for the service
   Description: Calls UpdateExt to update AccessScopeEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccessScopeEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AccessScopeEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID(Company, AccessScopeID, EntityType, EntityID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AccessScopeEntity item
   Description: Call UpdateExt to delete AccessScopeEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccessScopeEntity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID_AccessScopeBOMethods(Company, AccessScopeID, EntityType, EntityID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AccessScopeBOMethods items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AccessScopeBOMethods1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeBOMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")/AccessScopeBOMethods",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopeEntities_Company_AccessScopeID_EntityType_EntityID_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company, AccessScopeID, EntityType, EntityID, MethodID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AccessScopeBOMethod item
   Description: Calls GetByID to retrieve the AccessScopeBOMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeBOMethod1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param MethodID: Desc: MethodID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeEntities(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + ")/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AccessScopeBOMethods(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AccessScopeBOMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccessScopeBOMethods
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeBOMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods",headers=creds) as resp:
           return await resp.json()

async def post_AccessScopeBOMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccessScopeBOMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company, AccessScopeID, EntityType, EntityID, MethodID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AccessScopeBOMethod item
   Description: Calls GetByID to retrieve the AccessScopeBOMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccessScopeBOMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param MethodID: Desc: MethodID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company, AccessScopeID, EntityType, EntityID, MethodID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AccessScopeBOMethod for the service
   Description: Calls UpdateExt to update AccessScopeBOMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccessScopeBOMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param MethodID: Desc: MethodID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AccessScopeBOMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AccessScopeBOMethods_Company_AccessScopeID_EntityType_EntityID_MethodID(Company, AccessScopeID, EntityType, EntityID, MethodID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AccessScopeBOMethod item
   Description: Call UpdateExt to delete AccessScopeBOMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccessScopeBOMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AccessScopeID: Desc: AccessScopeID   Required: True   Allow empty value : True
      :param EntityType: Desc: EntityType   Required: True   Allow empty value : True
      :param EntityID: Desc: EntityID   Required: True   Allow empty value : True
      :param MethodID: Desc: MethodID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/AccessScopeBOMethods(" + Company + "," + AccessScopeID + "," + EntityType + "," + EntityID + "," + MethodID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AccessScopeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAccessScope, whereClauseAccessScopeEntity, whereClauseAccessScopeBOMethod, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAccessScope=" + whereClauseAccessScope
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAccessScopeEntity=" + whereClauseAccessScopeEntity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAccessScopeBOMethod=" + whereClauseAccessScopeBOMethod
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, accessScopeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "accessScopeID=" + accessScopeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetServiceMethodList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetServiceMethodList
   Description: This method returns a delimited list of the public methods for the given
object.  This could be used to provide a "picker list" as a starting point
when adding a new Security record related to a method.  These would look the
same as a Security record for an object, but with a SecCode field that has
been appended with "." + MethodName.
For example, a security record for the
   OperationID: GetServiceMethodList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetServiceMethodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServiceMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AccessScopeAllowFunctionExecution(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AccessScopeAllowFunctionExecution
   Description: Returns true if the AccessScope library function is authorized.
   OperationID: AccessScopeAllowFunctionExecution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AccessScopeAllowFunctionExecution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AccessScopeAllowFunctionExecution_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyAccessSope(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyAccessSope
   Description: Copy an existing AccessScope to a new AccessScope row
   OperationID: CopyAccessSope
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyAccessSope_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyAccessSope_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAccessScope(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAccessScope
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAccessScope
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAccessScope_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAccessScope_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAccessScopeEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAccessScopeEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAccessScopeEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAccessScopeEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAccessScopeEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAccessScopeBOMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAccessScopeBOMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAccessScopeBOMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAccessScopeBOMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAccessScopeBOMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AccessScopeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeBOMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AccessScopeBOMethodRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeEntityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AccessScopeEntityRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AccessScopeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AccessScopeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AccessScopeRow] = obj["value"]
      pass

class Ice_Tablesets_AccessScopeBOMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.EntityType:str = obj["EntityType"]
      """  EntityType  """  
      self.EntityID:str = obj["EntityID"]
      """  EntityID  """  
      self.MethodID:str = obj["MethodID"]
      """  MethodID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeEntityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.EntityType:str = obj["EntityType"]
      """  EntityType  """  
      self.EntityID:str = obj["EntityID"]
      """  EntityID  """  
      self.EntityDescription:str = obj["EntityDescription"]
      """  EntityDescription  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AllowExemptBO:bool = obj["AllowExemptBO"]
      """  AllowExemptBO  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AllowExemptBO:bool = obj["AllowExemptBO"]
      """  AllowExemptBO  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      """  All Companies Flag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AccessScopeAllowFunctionExecution_input:
   """ Required : 
   libraryID
   functionID
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      """  The entity id or library name.  """  
      self.functionID:str = obj["functionID"]
      """  The method or function name.  """  
      pass

class AccessScopeAllowFunctionExecution_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true|false  """  
      pass

class CopyAccessSope_input:
   """ Required : 
   sourceCompany
   sourceAccessID
   targetsourceAccessID
   targetDescription
   """  
   def __init__(self, obj):
      self.sourceCompany:str = obj["sourceCompany"]
      """  Existing Menu Company  """  
      self.sourceAccessID:str = obj["sourceAccessID"]
      """  Source Access scope ID  """  
      self.targetsourceAccessID:str = obj["targetsourceAccessID"]
      """  New Access scope ID  """  
      self.targetDescription:str = obj["targetDescription"]
      """  New Access scope description  """  
      pass

class CopyAccessSope_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AccessScopeTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   company
   accessScopeID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.accessScopeID:str = obj["accessScopeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   company
   accessScopeID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.accessScopeID:str = obj["accessScopeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AccessScopeTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AccessScopeTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AccessScopeTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AccessScopeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAccessScopeBOMethod_input:
   """ Required : 
   ds
   company
   accessScopeID
   entityType
   entityID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.accessScopeID:str = obj["accessScopeID"]
      self.entityType:str = obj["entityType"]
      self.entityID:str = obj["entityID"]
      pass

class GetNewAccessScopeBOMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAccessScopeEntity_input:
   """ Required : 
   ds
   company
   accessScopeID
   entityType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.accessScopeID:str = obj["accessScopeID"]
      self.entityType:str = obj["entityType"]
      pass

class GetNewAccessScopeEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAccessScope_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewAccessScope_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAccessScope
   whereClauseAccessScopeEntity
   whereClauseAccessScopeBOMethod
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAccessScope:str = obj["whereClauseAccessScope"]
      self.whereClauseAccessScopeEntity:str = obj["whereClauseAccessScopeEntity"]
      self.whereClauseAccessScopeBOMethod:str = obj["whereClauseAccessScopeBOMethod"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AccessScopeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetServiceMethodList_input:
   """ Required : 
   service
   """  
   def __init__(self, obj):
      self.service:str = obj["service"]
      """  The security code for which you want the list of methods.  """  
      pass

class GetServiceMethodList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AccessScopeMethodsTableset] = obj["returnObj"]
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

class Ice_Tablesets_AccessScopeBOMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.EntityType:str = obj["EntityType"]
      """  EntityType  """  
      self.EntityID:str = obj["EntityID"]
      """  EntityID  """  
      self.MethodID:str = obj["MethodID"]
      """  MethodID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeEntityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.EntityType:str = obj["EntityType"]
      """  EntityType  """  
      self.EntityID:str = obj["EntityID"]
      """  EntityID  """  
      self.EntityDescription:str = obj["EntityDescription"]
      """  EntityDescription  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AllowExemptBO:bool = obj["AllowExemptBO"]
      """  AllowExemptBO  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeListTableset:
   def __init__(self, obj):
      self.AccessScopeList:list[Ice_Tablesets_AccessScopeListRow] = obj["AccessScopeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AccessScopeMethodsRow:
   def __init__(self, obj):
      self.MethodName:str = obj["MethodName"]
      """  Method Name  """  
      self.Service:str = obj["Service"]
      """  Service Name  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeMethodsTableset:
   def __init__(self, obj):
      self.AccessScopeMethods:list[Ice_Tablesets_AccessScopeMethodsRow] = obj["AccessScopeMethods"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AccessScopeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AccessScopeID:str = obj["AccessScopeID"]
      """  AccessScopeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AllowExemptBO:bool = obj["AllowExemptBO"]
      """  AllowExemptBO  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      """  All Companies Flag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AccessScopeTableset:
   def __init__(self, obj):
      self.AccessScope:list[Ice_Tablesets_AccessScopeRow] = obj["AccessScope"]
      self.AccessScopeEntity:list[Ice_Tablesets_AccessScopeEntityRow] = obj["AccessScopeEntity"]
      self.AccessScopeBOMethod:list[Ice_Tablesets_AccessScopeBOMethodRow] = obj["AccessScopeBOMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtAccessScopeTableset:
   def __init__(self, obj):
      self.AccessScope:list[Ice_Tablesets_AccessScopeRow] = obj["AccessScope"]
      self.AccessScopeEntity:list[Ice_Tablesets_AccessScopeEntityRow] = obj["AccessScopeEntity"]
      self.AccessScopeBOMethod:list[Ice_Tablesets_AccessScopeBOMethodRow] = obj["AccessScopeBOMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAccessScopeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAccessScopeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AccessScopeTableset] = obj["ds"]
      pass

      """  output parameters  """  

