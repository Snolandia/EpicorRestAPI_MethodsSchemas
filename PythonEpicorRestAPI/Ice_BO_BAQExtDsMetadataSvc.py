import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BAQExtDsMetadataSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsMetadatas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsMetadatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsMetadatas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsMetadataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsMetadatas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsMetadatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsMetadataRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsMetadataRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsMetadatas_Company_DatasourceType(Company, DatasourceType, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsMetadata item
   Description: Calls GetByID to retrieve the BAQExtDsMetadata item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsMetadata
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsMetadataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas(" + Company + "," + DatasourceType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsMetadatas_Company_DatasourceType(Company, DatasourceType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsMetadata for the service
   Description: Calls UpdateExt to update BAQExtDsMetadata. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsMetadata
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsMetadataRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas(" + Company + "," + DatasourceType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsMetadatas_Company_DatasourceType(Company, DatasourceType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsMetadata item
   Description: Call UpdateExt to delete BAQExtDsMetadata item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsMetadata
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas(" + Company + "," + DatasourceType + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsMetadatas_Company_DatasourceType_BAQExtDsTables(Company, DatasourceType, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsTables1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas(" + Company + "," + DatasourceType + ")/BAQExtDsTables",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsMetadatas_Company_DatasourceType_BAQExtDsTables_Company_DatasourceType_SchemaName_TableName(Company, DatasourceType, SchemaName, TableName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsTable item
   Description: Calls GetByID to retrieve the BAQExtDsTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsTable1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsMetadatas(" + Company + "," + DatasourceType + ")/BAQExtDsTables(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsTables(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTables_Company_DatasourceType_SchemaName_TableName(Company, DatasourceType, SchemaName, TableName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsTable item
   Description: Calls GetByID to retrieve the BAQExtDsTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsTables_Company_DatasourceType_SchemaName_TableName(Company, DatasourceType, SchemaName, TableName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsTable for the service
   Description: Calls UpdateExt to update BAQExtDsTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsTables_Company_DatasourceType_SchemaName_TableName(Company, DatasourceType, SchemaName, TableName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsTable item
   Description: Call UpdateExt to delete BAQExtDsTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTables_Company_DatasourceType_SchemaName_TableName_BAQExtDsColumns(Company, DatasourceType, SchemaName, TableName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQExtDsColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQExtDsColumns1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + ")/BAQExtDsColumns",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsTables_Company_DatasourceType_SchemaName_TableName_BAQExtDsColumns_Company_DatasourceType_SchemaName_TableName_FieldName(Company, DatasourceType, SchemaName, TableName, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsColumn item
   Description: Calls GetByID to retrieve the BAQExtDsColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsColumn1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsTables(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + ")/BAQExtDsColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsColumns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDsColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDsColumns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsColumns",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDsColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDsColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDsColumns_Company_DatasourceType_SchemaName_TableName_FieldName(Company, DatasourceType, SchemaName, TableName, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDsColumn item
   Description: Calls GetByID to retrieve the BAQExtDsColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDsColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDsColumns_Company_DatasourceType_SchemaName_TableName_FieldName(Company, DatasourceType, SchemaName, TableName, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDsColumn for the service
   Description: Calls UpdateExt to update BAQExtDsColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDsColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDsColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDsColumns_Company_DatasourceType_SchemaName_TableName_FieldName(Company, DatasourceType, SchemaName, TableName, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDsColumn item
   Description: Call UpdateExt to delete BAQExtDsColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDsColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDsColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDataTableSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQExtDataTableSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQExtDataTableSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDataTableSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDataTableSearches",headers=creds) as resp:
           return await resp.json()

async def post_BAQExtDataTableSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQExtDataTableSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQExtDataTableSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQExtDataTableSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDataTableSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDataTableSearches_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDataTableSearch item
   Description: Calls GetByID to retrieve the BAQExtDataTableSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDataTableSearch
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDataTableSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDataTableSearches(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQExtDataTableSearches_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQExtDataTableSearch for the service
   Description: Calls UpdateExt to update BAQExtDataTableSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQExtDataTableSearch
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQExtDataTableSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDataTableSearches(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQExtDataTableSearches_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQExtDataTableSearch item
   Description: Call UpdateExt to delete BAQExtDataTableSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQExtDataTableSearch
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/BAQExtDataTableSearches(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDsMetadataListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBAQExtDsMetadata, whereClauseBAQExtDsTable, whereClauseBAQExtDsColumn, whereClauseBAQExtDataTableSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseBAQExtDsMetadata=" + whereClauseBAQExtDsMetadata
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDsTable=" + whereClauseBAQExtDsTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDsColumn=" + whereClauseBAQExtDsColumn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQExtDataTableSearch=" + whereClauseBAQExtDataTableSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteMetadata(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteMetadata
   Description: Delete all Metadata for type
   OperationID: DeleteMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddNewExtDataTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNewExtDataTables
   OperationID: AddNewExtDataTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewExtDataTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewExtDataTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsMetadata(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsMetadata
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQExtDsColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQExtDsColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQExtDsColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQExtDsColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQExtDsColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDsMetadataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDataTableSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDataTableSearchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsColumnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsMetadataListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsMetadataListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsMetadataRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsMetadataRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDsTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDsTableRow] = obj["value"]
      pass

class Ice_Tablesets_BAQExtDataTableSearchRow:
   def __init__(self, obj):
      self.TableID:str = obj["TableID"]
      self.Description:str = obj["Description"]
      self.TableType:str = obj["TableType"]
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.FullTableName:str = obj["FullTableName"]
      self.Catalog:str = obj["Catalog"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  FieldFormat  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  FieldLabel  """  
      self.Required:bool = obj["Required"]
      """  Required  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsMetadataListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SampleDatasourceName:str = obj["SampleDatasourceName"]
      """  SampleDatasourceName  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsMetadataRow:
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

class Ice_Tablesets_BAQExtDsTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullTableName:str = obj["FullTableName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddNewExtDataTables_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

class AddNewExtDataTables_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class DeleteMetadata_input:
   """ Required : 
   datasourceType
   """  
   def __init__(self, obj):
      self.datasourceType:str = obj["datasourceType"]
      pass

class DeleteMetadata_output:
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDsMetadataListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsColumn_input:
   """ Required : 
   ds
   datasourceType
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      self.datasourceType:str = obj["datasourceType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewBAQExtDsColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsMetadata_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

class GetNewBAQExtDsMetadata_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQExtDsTable_input:
   """ Required : 
   ds
   datasourceType
   schemaName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      self.datasourceType:str = obj["datasourceType"]
      self.schemaName:str = obj["schemaName"]
      pass

class GetNewBAQExtDsTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBAQExtDsMetadata
   whereClauseBAQExtDsTable
   whereClauseBAQExtDsColumn
   whereClauseBAQExtDataTableSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBAQExtDsMetadata:str = obj["whereClauseBAQExtDsMetadata"]
      self.whereClauseBAQExtDsTable:str = obj["whereClauseBAQExtDsTable"]
      self.whereClauseBAQExtDsColumn:str = obj["whereClauseBAQExtDsColumn"]
      self.whereClauseBAQExtDataTableSearch:str = obj["whereClauseBAQExtDataTableSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["returnObj"]
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

class Ice_Tablesets_BAQExtDataTableSearchRow:
   def __init__(self, obj):
      self.TableID:str = obj["TableID"]
      self.Description:str = obj["Description"]
      self.TableType:str = obj["TableType"]
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.FullTableName:str = obj["FullTableName"]
      self.Catalog:str = obj["Catalog"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  FieldFormat  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  FieldLabel  """  
      self.Required:bool = obj["Required"]
      """  Required  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsMetadataListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SampleDatasourceName:str = obj["SampleDatasourceName"]
      """  SampleDatasourceName  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDsMetadataListTableset:
   def __init__(self, obj):
      self.BAQExtDsMetadataList:list[Ice_Tablesets_BAQExtDsMetadataListRow] = obj["BAQExtDsMetadataList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDsMetadataRow:
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

class Ice_Tablesets_BAQExtDsMetadataTableset:
   def __init__(self, obj):
      self.BAQExtDsMetadata:list[Ice_Tablesets_BAQExtDsMetadataRow] = obj["BAQExtDsMetadata"]
      self.BAQExtDsTable:list[Ice_Tablesets_BAQExtDsTableRow] = obj["BAQExtDsTable"]
      self.BAQExtDsColumn:list[Ice_Tablesets_BAQExtDsColumnRow] = obj["BAQExtDsColumn"]
      self.BAQExtDataTableSearch:list[Ice_Tablesets_BAQExtDataTableSearchRow] = obj["BAQExtDataTableSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDsTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullTableName:str = obj["FullTableName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtBAQExtDsMetadataTableset:
   def __init__(self, obj):
      self.BAQExtDsMetadata:list[Ice_Tablesets_BAQExtDsMetadataRow] = obj["BAQExtDsMetadata"]
      self.BAQExtDsTable:list[Ice_Tablesets_BAQExtDsTableRow] = obj["BAQExtDsTable"]
      self.BAQExtDsColumn:list[Ice_Tablesets_BAQExtDsColumnRow] = obj["BAQExtDsColumn"]
      self.BAQExtDataTableSearch:list[Ice_Tablesets_BAQExtDataTableSearchRow] = obj["BAQExtDataTableSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQExtDsMetadataTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBAQExtDsMetadataTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BAQExtDsMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

