import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BAQExtDatasourceSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDatasources(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDatasources items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDatasources
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDatasourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/BAQExtDatasources",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDatasources(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDatasources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDatasourceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDatasourceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/BAQExtDatasources", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDatasources_Company_DatasourceName(Company, DatasourceName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDatasource item
   Description: Calls GetByID to retrieve the BAQExtDatasource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDatasource
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceName: Desc: DatasourceName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDatasourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/BAQExtDatasources(" + Company + "," + DatasourceName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDatasources_Company_DatasourceName(Company, DatasourceName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDatasource for the service
   Description: Calls UpdateExt to update BAQExtDatasource. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDatasource
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceName: Desc: DatasourceName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDatasourceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/BAQExtDatasources(" + Company + "," + DatasourceName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDatasources_Company_DatasourceName(Company, DatasourceName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDatasource item
   Description: Call UpdateExt to delete BAQExtDatasource item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDatasource
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceName: Desc: DatasourceName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/BAQExtDatasources(" + Company + "," + DatasourceName + ")",headers=creds) as resp:
           return await resp.json()

async def get_EfAdvancedProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EfAdvancedProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EfAdvancedProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.EfAdvancedPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/EfAdvancedProperties",headers=creds) as resp:
           return await resp.json()

async def post_EfAdvancedProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EfAdvancedProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.EfAdvancedPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.EfAdvancedPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/EfAdvancedProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EfAdvancedProperties_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EfAdvancedProperty item
   Description: Calls GetByID to retrieve the EfAdvancedProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EfAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EfAdvancedPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/EfAdvancedProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EfAdvancedProperties_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EfAdvancedProperty for the service
   Description: Calls UpdateExt to update EfAdvancedProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EfAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.EfAdvancedPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/EfAdvancedProperties(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EfAdvancedProperties_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EfAdvancedProperty item
   Description: Call UpdateExt to delete EfAdvancedProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EfAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/EfAdvancedProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_MsSqlAdvancedProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MsSqlAdvancedProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MsSqlAdvancedProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MsSqlAdvancedPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlAdvancedProperties",headers=creds) as resp:
           return await resp.json()

async def post_MsSqlAdvancedProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MsSqlAdvancedProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MsSqlAdvancedPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MsSqlAdvancedPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlAdvancedProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MsSqlAdvancedProperties_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MsSqlAdvancedProperty item
   Description: Calls GetByID to retrieve the MsSqlAdvancedProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MsSqlAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MsSqlAdvancedPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlAdvancedProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MsSqlAdvancedProperties_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MsSqlAdvancedProperty for the service
   Description: Calls UpdateExt to update MsSqlAdvancedProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MsSqlAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MsSqlAdvancedPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlAdvancedProperties(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MsSqlAdvancedProperties_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MsSqlAdvancedProperty item
   Description: Call UpdateExt to delete MsSqlAdvancedProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MsSqlAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlAdvancedProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_MsSqlKeyProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MsSqlKeyProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MsSqlKeyProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MsSqlKeyPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlKeyProperties",headers=creds) as resp:
           return await resp.json()

async def post_MsSqlKeyProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MsSqlKeyProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MsSqlKeyPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MsSqlKeyPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlKeyProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MsSqlKeyProperties_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MsSqlKeyProperty item
   Description: Calls GetByID to retrieve the MsSqlKeyProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MsSqlKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MsSqlKeyPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlKeyProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MsSqlKeyProperties_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MsSqlKeyProperty for the service
   Description: Calls UpdateExt to update MsSqlKeyProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MsSqlKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MsSqlKeyPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlKeyProperties(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MsSqlKeyProperties_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MsSqlKeyProperty item
   Description: Call UpdateExt to delete MsSqlKeyProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MsSqlKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/MsSqlKeyProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OdbcKeyProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OdbcKeyProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OdbcKeyProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.OdbcKeyPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OdbcKeyProperties",headers=creds) as resp:
           return await resp.json()

async def post_OdbcKeyProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OdbcKeyProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.OdbcKeyPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.OdbcKeyPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OdbcKeyProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OdbcKeyProperties_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OdbcKeyProperty item
   Description: Calls GetByID to retrieve the OdbcKeyProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OdbcKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.OdbcKeyPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OdbcKeyProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OdbcKeyProperties_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OdbcKeyProperty for the service
   Description: Calls UpdateExt to update OdbcKeyProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OdbcKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.OdbcKeyPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OdbcKeyProperties(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OdbcKeyProperties_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OdbcKeyProperty item
   Description: Call UpdateExt to delete OdbcKeyProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OdbcKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OdbcKeyProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OleDbAdvancedProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OleDbAdvancedProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OleDbAdvancedProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.OleDbAdvancedPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbAdvancedProperties",headers=creds) as resp:
           return await resp.json()

async def post_OleDbAdvancedProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OleDbAdvancedProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.OleDbAdvancedPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.OleDbAdvancedPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbAdvancedProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OleDbAdvancedProperties_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OleDbAdvancedProperty item
   Description: Calls GetByID to retrieve the OleDbAdvancedProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OleDbAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.OleDbAdvancedPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbAdvancedProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OleDbAdvancedProperties_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OleDbAdvancedProperty for the service
   Description: Calls UpdateExt to update OleDbAdvancedProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OleDbAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.OleDbAdvancedPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbAdvancedProperties(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OleDbAdvancedProperties_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OleDbAdvancedProperty item
   Description: Call UpdateExt to delete OleDbAdvancedProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OleDbAdvancedProperty
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbAdvancedProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OleDbKeyProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OleDbKeyProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OleDbKeyProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.OleDbKeyPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbKeyProperties",headers=creds) as resp:
           return await resp.json()

async def post_OleDbKeyProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OleDbKeyProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.OleDbKeyPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.OleDbKeyPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbKeyProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OleDbKeyProperties_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OleDbKeyProperty item
   Description: Calls GetByID to retrieve the OleDbKeyProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OleDbKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.OleDbKeyPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbKeyProperties(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OleDbKeyProperties_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OleDbKeyProperty for the service
   Description: Calls UpdateExt to update OleDbKeyProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OleDbKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.OleDbKeyPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbKeyProperties(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OleDbKeyProperties_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OleDbKeyProperty item
   Description: Call UpdateExt to delete OleDbKeyProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OleDbKeyProperty
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/OleDbKeyProperties(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDatasourceListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBAQExtDatasource, whereClauseEfAdvancedProperties, whereClauseMsSqlAdvancedProperties, whereClauseMsSqlKeyProperties, whereClauseOdbcKeyProperties, whereClauseOleDbAdvancedProperties, whereClauseOleDbKeyProperties, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseBAQExtDatasource=" + whereClauseBAQExtDatasource
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEfAdvancedProperties=" + whereClauseEfAdvancedProperties
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMsSqlAdvancedProperties=" + whereClauseMsSqlAdvancedProperties
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMsSqlKeyProperties=" + whereClauseMsSqlKeyProperties
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOdbcKeyProperties=" + whereClauseOdbcKeyProperties
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOleDbAdvancedProperties=" + whereClauseOleDbAdvancedProperties
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOleDbKeyProperties=" + whereClauseOleDbKeyProperties
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(datasourceName, epicorHeaders = None):
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
   params += "datasourceName=" + datasourceName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_LoadBAQExtAvailableDs(epicorHeaders = None):
   """  
   Summary: Invoke method LoadBAQExtAvailableDs
   Description: List of external data sources, available for company
   OperationID: LoadBAQExtAvailableDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBAQExtAvailableDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LoadCompanyExtDsList(epicorHeaders = None):
   """  
   Summary: Invoke method LoadCompanyExtDsList
   Description: Load data sources for current company
   OperationID: LoadCompanyExtDsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadCompanyExtDsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LoadCompanyExtDsListForCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadCompanyExtDsListForCompany
   Description: Loads the company ext ds list for company.
   OperationID: LoadCompanyExtDsListForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadCompanyExtDsListForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadCompanyExtDsListForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateRootEntryForExtDsInCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateRootEntryForExtDsInCompany
   Description: Create record in [SysCompanyBAQExtDs] for particulair company, extrenal DS and empty filter group
   OperationID: CreateRootEntryForExtDsInCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateRootEntryForExtDsInCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRootEntryForExtDsInCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveCompanyExtDsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveCompanyExtDsList
   Description: Save data source list for current company
   OperationID: SaveCompanyExtDsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveCompanyExtDsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveCompanyExtDsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportDataSources(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportDataSources
   Description: Export the data source information.
   OperationID: ExportDataSources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportDataSources_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportDataSources_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnlistDatasourceBackupInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnlistDatasourceBackupInfo
   Description: Returns information about datasources available for backup
   OperationID: EnlistDatasourceBackupInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnlistDatasourceBackupInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnlistDatasourceBackupInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DatasourceApplicationType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DatasourceApplicationType
   Description: retrieves application type for specified datasource
   OperationID: DatasourceApplicationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DatasourceApplicationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DatasourceApplicationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EncryptConnectionString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EncryptConnectionString
   Description: Encrypts the connection string.
   OperationID: EncryptConnectionString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EncryptConnectionString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EncryptConnectionString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildConnectionString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildConnectionString
   Description: Builds the connection string.
   OperationID: BuildConnectionString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildConnectionString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildConnectionString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateExportDatasourcesFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateExportDatasourcesFile
   Description: Generate Export Data sources File.
   OperationID: GenerateExportDatasourcesFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateExportDatasourcesFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateExportDatasourcesFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReadBackupSettingsFromFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReadBackupSettingsFromFile
   Description: Read the data from the provided fileRelativePath and transform it to Ice.BO.BAQExtBackupSettingsDataSet.
   OperationID: ReadBackupSettingsFromFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReadBackupSettingsFromFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadBackupSettingsFromFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportExternalDatasources(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportExternalDatasources
   Description: Imports the external data sources from a ds.
<param name="fileRelativePath">The path to the server file.</param>
   OperationID: ImportExternalDatasources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportExternalDatasources_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportExternalDatasources_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableCatalogs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableCatalogs
   Description: Get the available catalogs.
   OperationID: GetAvailableCatalogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableCatalogs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCatalogs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDatasource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDatasource
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDatasource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDatasource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDatasource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDatasourceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDatasourceListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDatasourceListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDatasourceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDatasourceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_EfAdvancedPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_EfAdvancedPropertiesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MsSqlAdvancedPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MsSqlAdvancedPropertiesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MsSqlKeyPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MsSqlKeyPropertiesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_OdbcKeyPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_OdbcKeyPropertiesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_OleDbAdvancedPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_OleDbAdvancedPropertiesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_OleDbKeyPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_OleDbKeyPropertiesRow] = obj["value"]
      pass

class Ice_Tablesets_BAQExtDatasourceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceName:str = obj["DatasourceName"]
      """  DatasourceName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.ProviderType:str = obj["ProviderType"]
      """  ProviderType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDatasourceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceName:str = obj["DatasourceName"]
      """  DatasourceName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.ProviderType:str = obj["ProviderType"]
      """  ProviderType  """  
      self.ConnectionString:str = obj["ConnectionString"]
      """  ConnectionString  """  
      self.TokenServer_URL:str = obj["TokenServer_URL"]
      """  TokenServer_URL  """  
      self.TokenServer_ClientID:str = obj["TokenServer_ClientID"]
      """  TokenServer_ClientID  """  
      self.TokenServer_ClientSecret:str = obj["TokenServer_ClientSecret"]
      """  TokenServer_ClientSecret  """  
      self.QueryMaxResultSet:int = obj["QueryMaxResultSet"]
      """  QueryMaxResultSet  """  
      self.QueryTimeOut:int = obj["QueryTimeOut"]
      """  QueryTimeOut  """  
      self.Settings:str = obj["Settings"]
      """  Settings  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.ClearText_ClientID:str = obj["ClearText_ClientID"]
      self.ClearText_ClientSecret:str = obj["ClearText_ClientSecret"]
      self.ClearText_URL:str = obj["ClearText_URL"]
      self.Login:str = obj["Login"]
      self.Password:str = obj["Password"]
      self.UseTrusted:bool = obj["UseTrusted"]
      self.DecryptedConnectionString:str = obj["DecryptedConnectionString"]
      """  Decrypted Connection String  """  
      self.DecryptedConnectionStringPresentation:str = obj["DecryptedConnectionStringPresentation"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EfAdvancedPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MsSqlAdvancedPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.ApplicationName:str = obj["ApplicationName"]
      self.ApplicationIntent:str = obj["ApplicationIntent"]
      self.AttachDbFilename:str = obj["AttachDbFilename"]
      self.ConnectTimeout:int = obj["ConnectTimeout"]
      self.ConnectRetryCount:int = obj["ConnectRetryCount"]
      self.ConnectRetryInterval:int = obj["ConnectRetryInterval"]
      self.CurrentLanguage:str = obj["CurrentLanguage"]
      self.Encrypt:bool = obj["Encrypt"]
      self.Enlist:bool = obj["Enlist"]
      self.FailoverPartner:str = obj["FailoverPartner"]
      self.LoadBalanceTimeout:int = obj["LoadBalanceTimeout"]
      self.MaxPoolSize:int = obj["MaxPoolSize"]
      self.MinPoolSize:int = obj["MinPoolSize"]
      self.MultipleActiveResultSets:bool = obj["MultipleActiveResultSets"]
      self.MultiSubnetFailover:bool = obj["MultiSubnetFailover"]
      self.PacketSize:int = obj["PacketSize"]
      self.PersistSecurityInfo:bool = obj["PersistSecurityInfo"]
      self.PoolBlockingPeriod:str = obj["PoolBlockingPeriod"]
      self.Pooling:bool = obj["Pooling"]
      self.Replication:bool = obj["Replication"]
      self.TransactionBinding:str = obj["TransactionBinding"]
      self.TrustServerCertificate:bool = obj["TrustServerCertificate"]
      self.TypeSystemVersion:str = obj["TypeSystemVersion"]
      self.UserInstance:bool = obj["UserInstance"]
      self.WorkstationID:str = obj["WorkstationID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MsSqlKeyPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.DataSource:str = obj["DataSource"]
      self.IntegratedSecurity:bool = obj["IntegratedSecurity"]
      self.UserID:str = obj["UserID"]
      self.Password:str = obj["Password"]
      self.InitialCatalog:str = obj["InitialCatalog"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_OdbcKeyPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.DSN:str = obj["DSN"]
      self.Server:str = obj["Server"]
      self.Driver:str = obj["Driver"]
      self.Database:str = obj["Database"]
      self.Trusted_connection:bool = obj["Trusted_connection"]
      self.Uid:str = obj["Uid"]
      self.Password:str = obj["Password"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_OleDbAdvancedPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.DataSource:str = obj["DataSource"]
      self.FileName:str = obj["FileName"]
      self.OleDbServices:int = obj["OleDbServices"]
      self.PersistSecurityInfo:bool = obj["PersistSecurityInfo"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_OleDbKeyPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.Provider:str = obj["Provider"]
      self.DataSource:str = obj["DataSource"]
      self.InitialCatalog:str = obj["InitialCatalog"]
      self.IntegratedSecurity:bool = obj["IntegratedSecurity"]
      self.UserID:str = obj["UserID"]
      self.Password:str = obj["Password"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildConnectionString_input:
   """ Required : 
   datasourceName
   ds
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      """  Name of the data source.  """  
      self.ds:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["ds"]
      pass

class BuildConnectionString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.connectionString:str = obj["parameters"]
      self.connectionStringPresentation:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateRootEntryForExtDsInCompany_input:
   """ Required : 
   companyId
   """  
   def __init__(self, obj):
      self.companyId:str = obj["companyId"]
      pass

class CreateRootEntryForExtDsInCompany_output:
   def __init__(self, obj):
      pass

class DatasourceApplicationType_input:
   """ Required : 
   datasourceName
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      pass

class DatasourceApplicationType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   datasourceName
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EncryptConnectionString_input:
   """ Required : 
   connectionString
   """  
   def __init__(self, obj):
      self.connectionString:str = obj["connectionString"]
      """  The connection string.  """  
      pass

class EncryptConnectionString_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Encrypted connection string.  """  
      pass

class EnlistDatasourceBackupInfo_input:
   """ Required : 
   dsList
   """  
   def __init__(self, obj):
      self.dsList:list[Ice_Tablesets_BAQExtBackupSettingsTableset] = obj["dsList"]
      pass

class EnlistDatasourceBackupInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsList:list[Ice_Tablesets_BAQExtBackupSettingsTableset] = obj["dsList"]
      pass

      """  output parameters  """  

class ExportDataSources_input:
   """ Required : 
   dataSourceName
   dataSourcetype
   """  
   def __init__(self, obj):
      self.dataSourceName:str = obj["dataSourceName"]
      """  Name of the data source.  """  
      self.dataSourcetype:str = obj["dataSourcetype"]
      """  The data source type.  """  
      pass

class ExportDataSources_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtBackupSettingsTableset] = obj["returnObj"]
      pass

class GenerateExportDatasourcesFile_input:
   """ Required : 
   backupSettingsTableset
   """  
   def __init__(self, obj):
      self.backupSettingsTableset:list[Ice_Tablesets_BAQExtBackupSettingsTableset] = obj["backupSettingsTableset"]
      pass

class GenerateExportDatasourcesFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The file server relative path in next format: temp\{RandomFolderName}\ExportDatasourcesFile.baqds  """  
      pass

class GetAvailableCatalogs_input:
   """ Required : 
   dataSource
   integratedSecurity
   userId
   password
   """  
   def __init__(self, obj):
      self.dataSource:str = obj["dataSource"]
      """  The data source.  """  
      self.integratedSecurity:bool = obj["integratedSecurity"]
      """  True if use integrated security for log in, false otherwise.  """  
      self.userId:str = obj["userId"]
      """  The user identifier.  """  
      self.password:str = obj["password"]
      """  The user password.  """  
      pass

class GetAvailableCatalogs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.catalogs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   datasourceName
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDatasourceListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBAQExtDatasource_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["ds"]
      pass

class GetNewBAQExtDatasource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBAQExtDatasource
   whereClauseEfAdvancedProperties
   whereClauseMsSqlAdvancedProperties
   whereClauseMsSqlKeyProperties
   whereClauseOdbcKeyProperties
   whereClauseOleDbAdvancedProperties
   whereClauseOleDbKeyProperties
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBAQExtDatasource:str = obj["whereClauseBAQExtDatasource"]
      self.whereClauseEfAdvancedProperties:str = obj["whereClauseEfAdvancedProperties"]
      self.whereClauseMsSqlAdvancedProperties:str = obj["whereClauseMsSqlAdvancedProperties"]
      self.whereClauseMsSqlKeyProperties:str = obj["whereClauseMsSqlKeyProperties"]
      self.whereClauseOdbcKeyProperties:str = obj["whereClauseOdbcKeyProperties"]
      self.whereClauseOleDbAdvancedProperties:str = obj["whereClauseOleDbAdvancedProperties"]
      self.whereClauseOleDbKeyProperties:str = obj["whereClauseOleDbKeyProperties"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["returnObj"]
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

class Ice_Tablesets_BAQExtAvailableDsRow:
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.DatasourceType:str = obj["DatasourceType"]
      self.Description:str = obj["Description"]
      self.Company:str = obj["Company"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtAvailableDsTableset:
   def __init__(self, obj):
      self.BAQExtAvailableDs:list[Ice_Tablesets_BAQExtAvailableDsRow] = obj["BAQExtAvailableDs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtBackupCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.ExportCompany:bool = obj["ExportCompany"]
      self.ReplaceSettings:bool = obj["ReplaceSettings"]
      self.DatasourceType:str = obj["DatasourceType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtBackupSettingsRow:
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.DatasourceType:str = obj["DatasourceType"]
      self.DsDescription:str = obj["DsDescription"]
      self.ExportDatasource:bool = obj["ExportDatasource"]
      self.ExportType:bool = obj["ExportType"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.ReplaceType:bool = obj["ReplaceType"]
      self.RenameDatasourceTo:str = obj["RenameDatasourceTo"]
      self.RenameTypeTo:str = obj["RenameTypeTo"]
      self.ReplaceDatasource:bool = obj["ReplaceDatasource"]
      self.ReplaceMetadata:bool = obj["ReplaceMetadata"]
      self.ExportMetadata:bool = obj["ExportMetadata"]
      self.DsCompany:str = obj["DsCompany"]
      self.TypeCompany:str = obj["TypeCompany"]
      self.CompanyDatasource:str = obj["CompanyDatasource"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtBackupSettingsTableset:
   def __init__(self, obj):
      self.BAQExtBackupSettings:list[Ice_Tablesets_BAQExtBackupSettingsRow] = obj["BAQExtBackupSettings"]
      self.BAQExtBackupCompany:list[Ice_Tablesets_BAQExtBackupCompanyRow] = obj["BAQExtBackupCompany"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDatasourceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceName:str = obj["DatasourceName"]
      """  DatasourceName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.ProviderType:str = obj["ProviderType"]
      """  ProviderType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDatasourceListTableset:
   def __init__(self, obj):
      self.BAQExtDatasourceList:list[Ice_Tablesets_BAQExtDatasourceListRow] = obj["BAQExtDatasourceList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDatasourceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceName:str = obj["DatasourceName"]
      """  DatasourceName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.ProviderType:str = obj["ProviderType"]
      """  ProviderType  """  
      self.ConnectionString:str = obj["ConnectionString"]
      """  ConnectionString  """  
      self.TokenServer_URL:str = obj["TokenServer_URL"]
      """  TokenServer_URL  """  
      self.TokenServer_ClientID:str = obj["TokenServer_ClientID"]
      """  TokenServer_ClientID  """  
      self.TokenServer_ClientSecret:str = obj["TokenServer_ClientSecret"]
      """  TokenServer_ClientSecret  """  
      self.QueryMaxResultSet:int = obj["QueryMaxResultSet"]
      """  QueryMaxResultSet  """  
      self.QueryTimeOut:int = obj["QueryTimeOut"]
      """  QueryTimeOut  """  
      self.Settings:str = obj["Settings"]
      """  Settings  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.ClearText_ClientID:str = obj["ClearText_ClientID"]
      self.ClearText_ClientSecret:str = obj["ClearText_ClientSecret"]
      self.ClearText_URL:str = obj["ClearText_URL"]
      self.Login:str = obj["Login"]
      self.Password:str = obj["Password"]
      self.UseTrusted:bool = obj["UseTrusted"]
      self.DecryptedConnectionString:str = obj["DecryptedConnectionString"]
      """  Decrypted Connection String  """  
      self.DecryptedConnectionStringPresentation:str = obj["DecryptedConnectionStringPresentation"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDatasourceTableset:
   def __init__(self, obj):
      self.BAQExtDatasource:list[Ice_Tablesets_BAQExtDatasourceRow] = obj["BAQExtDatasource"]
      self.EfAdvancedProperties:list[Ice_Tablesets_EfAdvancedPropertiesRow] = obj["EfAdvancedProperties"]
      self.MsSqlAdvancedProperties:list[Ice_Tablesets_MsSqlAdvancedPropertiesRow] = obj["MsSqlAdvancedProperties"]
      self.MsSqlKeyProperties:list[Ice_Tablesets_MsSqlKeyPropertiesRow] = obj["MsSqlKeyProperties"]
      self.OdbcKeyProperties:list[Ice_Tablesets_OdbcKeyPropertiesRow] = obj["OdbcKeyProperties"]
      self.OleDbAdvancedProperties:list[Ice_Tablesets_OleDbAdvancedPropertiesRow] = obj["OleDbAdvancedProperties"]
      self.OleDbKeyProperties:list[Ice_Tablesets_OleDbKeyPropertiesRow] = obj["OleDbKeyProperties"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_EfAdvancedPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MsSqlAdvancedPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.ApplicationName:str = obj["ApplicationName"]
      self.ApplicationIntent:str = obj["ApplicationIntent"]
      self.AttachDbFilename:str = obj["AttachDbFilename"]
      self.ConnectTimeout:int = obj["ConnectTimeout"]
      self.ConnectRetryCount:int = obj["ConnectRetryCount"]
      self.ConnectRetryInterval:int = obj["ConnectRetryInterval"]
      self.CurrentLanguage:str = obj["CurrentLanguage"]
      self.Encrypt:bool = obj["Encrypt"]
      self.Enlist:bool = obj["Enlist"]
      self.FailoverPartner:str = obj["FailoverPartner"]
      self.LoadBalanceTimeout:int = obj["LoadBalanceTimeout"]
      self.MaxPoolSize:int = obj["MaxPoolSize"]
      self.MinPoolSize:int = obj["MinPoolSize"]
      self.MultipleActiveResultSets:bool = obj["MultipleActiveResultSets"]
      self.MultiSubnetFailover:bool = obj["MultiSubnetFailover"]
      self.PacketSize:int = obj["PacketSize"]
      self.PersistSecurityInfo:bool = obj["PersistSecurityInfo"]
      self.PoolBlockingPeriod:str = obj["PoolBlockingPeriod"]
      self.Pooling:bool = obj["Pooling"]
      self.Replication:bool = obj["Replication"]
      self.TransactionBinding:str = obj["TransactionBinding"]
      self.TrustServerCertificate:bool = obj["TrustServerCertificate"]
      self.TypeSystemVersion:str = obj["TypeSystemVersion"]
      self.UserInstance:bool = obj["UserInstance"]
      self.WorkstationID:str = obj["WorkstationID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MsSqlKeyPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.DataSource:str = obj["DataSource"]
      self.IntegratedSecurity:bool = obj["IntegratedSecurity"]
      self.UserID:str = obj["UserID"]
      self.Password:str = obj["Password"]
      self.InitialCatalog:str = obj["InitialCatalog"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_OdbcKeyPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.DSN:str = obj["DSN"]
      self.Server:str = obj["Server"]
      self.Driver:str = obj["Driver"]
      self.Database:str = obj["Database"]
      self.Trusted_connection:bool = obj["Trusted_connection"]
      self.Uid:str = obj["Uid"]
      self.Password:str = obj["Password"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_OleDbAdvancedPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.DataSource:str = obj["DataSource"]
      self.FileName:str = obj["FileName"]
      self.OleDbServices:int = obj["OleDbServices"]
      self.PersistSecurityInfo:bool = obj["PersistSecurityInfo"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_OleDbKeyPropertiesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.Provider:str = obj["Provider"]
      self.DataSource:str = obj["DataSource"]
      self.InitialCatalog:str = obj["InitialCatalog"]
      self.IntegratedSecurity:bool = obj["IntegratedSecurity"]
      self.UserID:str = obj["UserID"]
      self.Password:str = obj["Password"]
      self.SimpleSQL:bool = obj["SimpleSQL"]
      self.SkipLoadErrors:bool = obj["SkipLoadErrors"]
      self.UseFieldAlias:bool = obj["UseFieldAlias"]
      self.AliasMaxLength:int = obj["AliasMaxLength"]
      self.SQLDialect:str = obj["SQLDialect"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCompanyBAQExtDsDefRow:
   def __init__(self, obj):
      self.Constant:str = obj["Constant"]
      self.ConstantValue:str = obj["ConstantValue"]
      self.DatasourceName:str = obj["DatasourceName"]
      self.FilterGroupName:str = obj["FilterGroupName"]
      self.FilterName:str = obj["FilterName"]
      self.FilterValue:str = obj["FilterValue"]
      self.UseDefault:bool = obj["UseDefault"]
      self.Company:str = obj["Company"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCompanyBAQExtDsGroupRow:
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.FilterGroupName:str = obj["FilterGroupName"]
      self.GroupDescr:str = obj["GroupDescr"]
      self.SkipFilter:bool = obj["SkipFilter"]
      self.Company:str = obj["Company"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCompanyBAQExtDsRow:
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.Description:str = obj["Description"]
      self.Enabled:bool = obj["Enabled"]
      self.SkipFilter:bool = obj["SkipFilter"]
      self.Company:str = obj["Company"]
      self.DatasourceCompany:str = obj["DatasourceCompany"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCompanyBAQExtDsTableset:
   def __init__(self, obj):
      self.SysCompanyBAQExtDs:list[Ice_Tablesets_SysCompanyBAQExtDsRow] = obj["SysCompanyBAQExtDs"]
      self.SysCompanyBAQExtDsGroup:list[Ice_Tablesets_SysCompanyBAQExtDsGroupRow] = obj["SysCompanyBAQExtDsGroup"]
      self.SysCompanyBAQExtDsDef:list[Ice_Tablesets_SysCompanyBAQExtDsDefRow] = obj["SysCompanyBAQExtDsDef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtBAQExtDatasourceTableset:
   def __init__(self, obj):
      self.BAQExtDatasource:list[Ice_Tablesets_BAQExtDatasourceRow] = obj["BAQExtDatasource"]
      self.EfAdvancedProperties:list[Ice_Tablesets_EfAdvancedPropertiesRow] = obj["EfAdvancedProperties"]
      self.MsSqlAdvancedProperties:list[Ice_Tablesets_MsSqlAdvancedPropertiesRow] = obj["MsSqlAdvancedProperties"]
      self.MsSqlKeyProperties:list[Ice_Tablesets_MsSqlKeyPropertiesRow] = obj["MsSqlKeyProperties"]
      self.OdbcKeyProperties:list[Ice_Tablesets_OdbcKeyPropertiesRow] = obj["OdbcKeyProperties"]
      self.OleDbAdvancedProperties:list[Ice_Tablesets_OleDbAdvancedPropertiesRow] = obj["OleDbAdvancedProperties"]
      self.OleDbKeyProperties:list[Ice_Tablesets_OleDbKeyPropertiesRow] = obj["OleDbKeyProperties"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportExternalDatasources_input:
   """ Required : 
   fileRelativePath
   ds
   """  
   def __init__(self, obj):
      self.fileRelativePath:str = obj["fileRelativePath"]
      self.ds      #schema had no properties on an object.
      pass

class ImportExternalDatasources_output:
   def __init__(self, obj):
      pass

class LoadBAQExtAvailableDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtAvailableDsTableset] = obj["returnObj"]
      pass

class LoadCompanyExtDsListForCompany_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  The company identifier.  """  
      pass

class LoadCompanyExtDsListForCompany_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysCompanyBAQExtDsTableset] = obj["returnObj"]
      pass

class LoadCompanyExtDsList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysCompanyBAQExtDsTableset] = obj["returnObj"]
      pass

class ReadBackupSettingsFromFile_input:
   """ Required : 
   fileRelativePath
   ds
   """  
   def __init__(self, obj):
      self.fileRelativePath:str = obj["fileRelativePath"]
      """  The path to the server file.  """  
      self.ds      #schema had no properties on an object.
      """  The BAQ External Backup Settings Data Set.  """  
      pass

class ReadBackupSettingsFromFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds: UNKNOW TYPE(error 2338) = obj["ds"]
      pass

      """  output parameters  """  

class SaveCompanyExtDsList_input:
   """ Required : 
   companyDs
   """  
   def __init__(self, obj):
      self.companyDs:list[Ice_Tablesets_SysCompanyBAQExtDsTableset] = obj["companyDs"]
      pass

class SaveCompanyExtDsList_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQExtDatasourceTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQExtDatasourceTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDatasourceTableset] = obj["ds"]
      pass

      """  output parameters  """  

