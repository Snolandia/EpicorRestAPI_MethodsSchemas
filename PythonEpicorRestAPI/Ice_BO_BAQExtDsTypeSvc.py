import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BAQExtDsTypeSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsTypes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType(Company, DatasourceType, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsType item
   Description: Calls GetByID to retrieve the BAQExtDsType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsTypes_Company_DatasourceType(Company, DatasourceType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsType for the service
   Description: Calls UpdateExt to update BAQExtDsType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsTypes_Company_DatasourceType(Company, DatasourceType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsType item
   Description: Call UpdateExt to delete BAQExtDsType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsColumnFilters(Company, DatasourceType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsColumnFilters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsColumnFilters1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsColumnFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsColumnFilters",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsColumnFilter item
   Description: Calls GetByID to retrieve the BAQExtDsColumnFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsColumnFilter1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsFilterGroups(Company, DatasourceType, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsFilterGroups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsFilterGroups1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsFilterGroups",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company, DatasourceType, FilterGroupName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterGroup item
   Description: Calls GetByID to retrieve the BAQExtDsFilterGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterGroup1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsTableFilters(Company, DatasourceType, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsTableFilters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsTableFilters1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTableFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsTableFilters",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTypes_Company_DatasourceType_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsTableFilter item
   Description: Calls GetByID to retrieve the BAQExtDsTableFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsTableFilter1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTypes(" + Company + "," + DatasourceType + ")/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsColumnFilters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsColumnFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsColumnFilters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsColumnFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsColumnFilters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsColumnFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsColumnFilter item
   Description: Calls GetByID to retrieve the BAQExtDsColumnFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsColumnFilter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsColumnFilter for the service
   Description: Calls UpdateExt to update BAQExtDsColumnFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsColumnFilter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsColumnFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsColumnFilter item
   Description: Call UpdateExt to delete BAQExtDsColumnFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsColumnFilter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsColumnFilters(" + Company + "," + DatasourceType + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsFilterGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsFilterGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsFilterGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsFilterGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsFilterGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company, DatasourceType, FilterGroupName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterGroup item
   Description: Calls GetByID to retrieve the BAQExtDsFilterGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company, DatasourceType, FilterGroupName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsFilterGroup for the service
   Description: Calls UpdateExt to update BAQExtDsFilterGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsFilterGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName(Company, DatasourceType, FilterGroupName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsFilterGroup item
   Description: Call UpdateExt to delete BAQExtDsFilterGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsFilterGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName_BAQExtDsFilterDefs(Company, DatasourceType, FilterGroupName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsFilterDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsFilterDefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")/BAQExtDsFilterDefs",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsFilterGroups_Company_DatasourceType_FilterGroupName_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company, DatasourceType, FilterGroupName, FilterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterDef item
   Description: Calls GetByID to retrieve the BAQExtDsFilterDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterDef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param FilterName: Desc: FilterName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterGroups(" + Company + "," + DatasourceType + "," + FilterGroupName + ")/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsFilterDefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsFilterDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsFilterDefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsFilterDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsFilterDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsFilterDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company, DatasourceType, FilterGroupName, FilterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsFilterDef item
   Description: Calls GetByID to retrieve the BAQExtDsFilterDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsFilterDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param FilterName: Desc: FilterName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company, DatasourceType, FilterGroupName, FilterName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsFilterDef for the service
   Description: Calls UpdateExt to update BAQExtDsFilterDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsFilterDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param FilterName: Desc: FilterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsFilterDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsFilterDefs_Company_DatasourceType_FilterGroupName_FilterName(Company, DatasourceType, FilterGroupName, FilterName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsFilterDef item
   Description: Call UpdateExt to delete BAQExtDsFilterDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsFilterDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterGroupName: Desc: FilterGroupName   Required: True   Allow empty value : True
      :param FilterName: Desc: FilterName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsFilterDefs(" + Company + "," + DatasourceType + "," + FilterGroupName + "," + FilterName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTableFilters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsTableFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsTableFilters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTableFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsTableFilters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsTableFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsTableFilter item
   Description: Calls GetByID to retrieve the BAQExtDsTableFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsTableFilter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsTableFilter for the service
   Description: Calls UpdateExt to update BAQExtDsTableFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsTableFilter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsTableFilters_Company_DatasourceType_FilterID(Company, DatasourceType, FilterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsTableFilter item
   Description: Call UpdateExt to delete BAQExtDsTableFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsTableFilter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/BAQExtDsTableFilters(" + Company + "," + DatasourceType + "," + FilterID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBAQExtDsType, whereClauseBAQExtDsColumnFilter, whereClauseBAQExtDsFilterGroup, whereClauseBAQExtDsFilterDef, whereClauseBAQExtDsTableFilter, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseBAQExtDsType=" + whereClauseBAQExtDsType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDsColumnFilter=" + whereClauseBAQExtDsColumnFilter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDsFilterGroup=" + whereClauseBAQExtDsFilterGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDsFilterDef=" + whereClauseBAQExtDsFilterDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDsTableFilter=" + whereClauseBAQExtDsTableFilter
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(datasourceType, epicorHeaders = None):
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
   params += "datasourceType=" + datasourceType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetGlobalConstantList(epicorHeaders = None):
   """  
   Summary: Invoke method GetGlobalConstantList
   Description: Build a list of global constants
   OperationID: GetGlobalConstantList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlobalConstantList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_MoveTableFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveTableFilter
   Description: Move record up or down
   OperationID: MoveTableFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveTableFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveTableFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveColumnFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveColumnFilter
   Description: Move BAQExtDsColumnFilter record up or down
   OperationID: MoveColumnFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveColumnFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveColumnFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveFilterDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveFilterDef
   Description: Move BAQExtDsFilterDef record up or down
   OperationID: MoveFilterDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveFilterDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFilterDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsColumnFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsColumnFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsColumnFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsColumnFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsColumnFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsFilterGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsFilterGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsFilterGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsFilterGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsFilterGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsFilterDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsFilterDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsFilterDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsFilterDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsFilterDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsTableFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsTableFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsTableFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsTableFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsTableFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnFilterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsColumnFilterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsFilterDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsFilterGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsFilterGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableFilterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsTableFilterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsTypeRow] = obj["value"]
      pass

class Ice_Tablesets_BAQExtDsColumnFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterID:str = obj["FilterID"]
      """  FilterID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsFilterDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterGroupName:str = obj["FilterGroupName"]
      """  FilterGroupName  """  
      self.FilterName:str = obj["FilterName"]
      """  FilterName  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.DefaultConstant:str = obj["DefaultConstant"]
      """  DefaultConstant  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsFilterGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterGroupName:str = obj["FilterGroupName"]
      """  FilterGroupName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTableFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterID:str = obj["FilterID"]
      """  FilterID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ApplicationType:str = obj["ApplicationType"]
      """  ApplicationType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SampleDatasourceName:str = obj["SampleDatasourceName"]
      """  SampleDatasourceName  """  
      self.ApplicationType:str = obj["ApplicationType"]
      """  ApplicationType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   datasourceType
   """  
   def __init__(self, obj):
      self.datasourceType:str = obj["datasourceType"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   datasourceType
   """  
   def __init__(self, obj):
      self.datasourceType:str = obj["datasourceType"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["returnObj"]
      pass

class GetGlobalConstantList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  delimited list of global constants  """  
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsColumnFilter_input:
   """ Required : 
   ds
   datasourceType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.datasourceType:str = obj["datasourceType"]
      pass

class GetNewBAQExtDsColumnFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsFilterDef_input:
   """ Required : 
   ds
   datasourceType
   filterGroupName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.datasourceType:str = obj["datasourceType"]
      self.filterGroupName:str = obj["filterGroupName"]
      pass

class GetNewBAQExtDsFilterDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsFilterGroup_input:
   """ Required : 
   ds
   datasourceType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.datasourceType:str = obj["datasourceType"]
      pass

class GetNewBAQExtDsFilterGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsTableFilter_input:
   """ Required : 
   ds
   datasourceType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.datasourceType:str = obj["datasourceType"]
      pass

class GetNewBAQExtDsTableFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

class GetNewBAQExtDsType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBAQExtDsType
   whereClauseBAQExtDsColumnFilter
   whereClauseBAQExtDsFilterGroup
   whereClauseBAQExtDsFilterDef
   whereClauseBAQExtDsTableFilter
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBAQExtDsType:str = obj["whereClauseBAQExtDsType"]
      self.whereClauseBAQExtDsColumnFilter:str = obj["whereClauseBAQExtDsColumnFilter"]
      self.whereClauseBAQExtDsFilterGroup:str = obj["whereClauseBAQExtDsFilterGroup"]
      self.whereClauseBAQExtDsFilterDef:str = obj["whereClauseBAQExtDsFilterDef"]
      self.whereClauseBAQExtDsTableFilter:str = obj["whereClauseBAQExtDsTableFilter"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["returnObj"]
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

class Ice_Tablesets_BAQExtDsColumnFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterID:str = obj["FilterID"]
      """  FilterID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsFilterDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterGroupName:str = obj["FilterGroupName"]
      """  FilterGroupName  """  
      self.FilterName:str = obj["FilterName"]
      """  FilterName  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.DefaultConstant:str = obj["DefaultConstant"]
      """  DefaultConstant  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsFilterGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterGroupName:str = obj["FilterGroupName"]
      """  FilterGroupName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTableFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.FilterID:str = obj["FilterID"]
      """  FilterID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.AndOr:str = obj["AndOr"]
      """  AndOr  """  
      self.Neg:bool = obj["Neg"]
      """  Neg  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ApplicationType:str = obj["ApplicationType"]
      """  ApplicationType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTypeListTableset:
   def __init__(self, obj):
      self.BAQExtDsTypeList:list[Ice_Tablesets_BAQExtDsTypeListRow] = obj["BAQExtDsTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDsTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SampleDatasourceName:str = obj["SampleDatasourceName"]
      """  SampleDatasourceName  """  
      self.ApplicationType:str = obj["ApplicationType"]
      """  ApplicationType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsTypeTableset:
   def __init__(self, obj):
      self.BAQExtDsType:list[Ice_Tablesets_BAQExtDsTypeRow] = obj["BAQExtDsType"]
      self.BAQExtDsColumnFilter:list[Ice_Tablesets_BAQExtDsColumnFilterRow] = obj["BAQExtDsColumnFilter"]
      self.BAQExtDsFilterGroup:list[Ice_Tablesets_BAQExtDsFilterGroupRow] = obj["BAQExtDsFilterGroup"]
      self.BAQExtDsFilterDef:list[Ice_Tablesets_BAQExtDsFilterDefRow] = obj["BAQExtDsFilterDef"]
      self.BAQExtDsTableFilter:list[Ice_Tablesets_BAQExtDsTableFilterRow] = obj["BAQExtDsTableFilter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtBAQExtDsTypeTableset:
   def __init__(self, obj):
      self.BAQExtDsType:list[Ice_Tablesets_BAQExtDsTypeRow] = obj["BAQExtDsType"]
      self.BAQExtDsColumnFilter:list[Ice_Tablesets_BAQExtDsColumnFilterRow] = obj["BAQExtDsColumnFilter"]
      self.BAQExtDsFilterGroup:list[Ice_Tablesets_BAQExtDsFilterGroupRow] = obj["BAQExtDsFilterGroup"]
      self.BAQExtDsFilterDef:list[Ice_Tablesets_BAQExtDsFilterDefRow] = obj["BAQExtDsFilterDef"]
      self.BAQExtDsTableFilter:list[Ice_Tablesets_BAQExtDsTableFilterRow] = obj["BAQExtDsTableFilter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class MoveColumnFilter_input:
   """ Required : 
   ds
   currentSysRowID
   direction
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.currentSysRowID:str = obj["currentSysRowID"]
      self.direction:str = obj["direction"]
      pass

class MoveColumnFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MoveFilterDef_input:
   """ Required : 
   ds
   currentSysRowID
   filterGroupName
   direction
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.currentSysRowID:str = obj["currentSysRowID"]
      self.filterGroupName:str = obj["filterGroupName"]
      self.direction:str = obj["direction"]
      pass

class MoveFilterDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MoveTableFilter_input:
   """ Required : 
   ds
   currentSysRowID
   direction
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      self.currentSysRowID:str = obj["currentSysRowID"]
      self.direction:str = obj["direction"]
      pass

class MoveTableFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQExtDsTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQExtDsTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

