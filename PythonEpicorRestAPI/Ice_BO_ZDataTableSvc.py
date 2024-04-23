import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ZDataTableSvc
# Description: The ZDataTable service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZDataTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZDataTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables",headers=creds) as resp:
           return await resp.json()

async def post_ZDataTables(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZDataTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZDataTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZDataTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID(SystemCode, DataTableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZDataTable item
   Description: Calls GetByID to retrieve the ZDataTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataTable
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZDataTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZDataTables_SystemCode_DataTableID(SystemCode, DataTableID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZDataTable for the service
   Description: Calls UpdateExt to update ZDataTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZDataTable
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZDataTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZDataTables_SystemCode_DataTableID(SystemCode, DataTableID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZDataTable item
   Description: Call UpdateExt to delete ZDataTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZDataTable
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID_ZLookupLinks(SystemCode, DataTableID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZLookupLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZLookupLinks1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZLookupLinks",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode, DataTableID, LookupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZLookupLink item
   Description: Calls GetByID to retrieve the ZLookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupLink1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID_ZDataFields(SystemCode, DataTableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZDataFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZDataFields1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZDataFields",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode, DataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZDataField item
   Description: Calls GetByID to retrieve the ZDataField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataField1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID_ZKeys(SystemCode, DataTableID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZKeys items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZKeys1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZKeys",headers=creds) as resp:
           return await resp.json()

async def get_ZDataTables_SystemCode_DataTableID_ZKeys_SystemCode_DataTableID_KeyID(SystemCode, DataTableID, KeyID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZKey item
   Description: Calls GetByID to retrieve the ZKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKey1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZLookupLinks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZLookupLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZLookupLinks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks",headers=creds) as resp:
           return await resp.json()

async def post_ZLookupLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZLookupLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode, DataTableID, LookupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZLookupLink item
   Description: Calls GetByID to retrieve the ZLookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupLink
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode, DataTableID, LookupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZLookupLink for the service
   Description: Calls UpdateExt to update ZLookupLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZLookupLink
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode, DataTableID, LookupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZLookupLink item
   Description: Call UpdateExt to delete ZLookupLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZLookupLink
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLinkColumns(SystemCode, DataTableID, LookupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZLinkColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZLinkColumns1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLinkColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLinkColumns",headers=creds) as resp:
           return await resp.json()

async def get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode, DataTableID, LookupID, LinkID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZLinkColumn item
   Description: Calls GetByID to retrieve the ZLinkColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLinkColumn1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLookupFields(SystemCode, DataTableID, LookupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZLookupFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZLookupFields1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLookupFields",headers=creds) as resp:
           return await resp.json()

async def get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode, DataTableID, LookupID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZLookupField item
   Description: Calls GetByID to retrieve the ZLookupField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupField1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZLinkColumns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZLinkColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZLinkColumns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLinkColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns",headers=creds) as resp:
           return await resp.json()

async def post_ZLinkColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZLinkColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode, DataTableID, LinkID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZLinkColumn item
   Description: Calls GetByID to retrieve the ZLinkColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLinkColumn
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode, DataTableID, LinkID, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZLinkColumn for the service
   Description: Calls UpdateExt to update ZLinkColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZLinkColumn
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode, DataTableID, LinkID, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZLinkColumn item
   Description: Call UpdateExt to delete ZLinkColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZLinkColumn
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZLookupFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZLookupFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZLookupFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields",headers=creds) as resp:
           return await resp.json()

async def post_ZLookupFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZLookupFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode, DataTableID, LookupID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZLookupField item
   Description: Calls GetByID to retrieve the ZLookupField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode, DataTableID, LookupID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZLookupField for the service
   Description: Calls UpdateExt to update ZLookupField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZLookupField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode, DataTableID, LookupID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZLookupField item
   Description: Call UpdateExt to delete ZLookupField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZLookupField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param LookupID: Desc: LookupID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZDataFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZDataFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZDataFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields",headers=creds) as resp:
           return await resp.json()

async def post_ZDataFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZDataFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode, DataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZDataField item
   Description: Calls GetByID to retrieve the ZDataField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode, DataTableID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZDataField for the service
   Description: Calls UpdateExt to update ZDataField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZDataField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode, DataTableID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZDataField item
   Description: Call UpdateExt to delete ZDataField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZDataField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZKeys(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZKeys items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZKeys
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys",headers=creds) as resp:
           return await resp.json()

async def post_ZKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZKeyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZKeyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZKeys_SystemCode_DataTableID_KeyID(SystemCode, DataTableID, KeyID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZKey item
   Description: Calls GetByID to retrieve the ZKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKey
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZKeys_SystemCode_DataTableID_KeyID(SystemCode, DataTableID, KeyID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZKey for the service
   Description: Calls UpdateExt to update ZKey. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZKey
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZKeyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZKeys_SystemCode_DataTableID_KeyID(SystemCode, DataTableID, KeyID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZKey item
   Description: Call UpdateExt to delete ZKey item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZKey
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZKeys_SystemCode_DataTableID_KeyID_ZKeyFields(SystemCode, DataTableID, KeyID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZKeyFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZKeyFields1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")/ZKeyFields",headers=creds) as resp:
           return await resp.json()

async def get_ZKeys_SystemCode_DataTableID_KeyID_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode, DataTableID, KeyID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZKeyField item
   Description: Calls GetByID to retrieve the ZKeyField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKeyField1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZKeyFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZKeyFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZKeyFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields",headers=creds) as resp:
           return await resp.json()

async def post_ZKeyFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZKeyFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode, DataTableID, KeyID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZKeyField item
   Description: Calls GetByID to retrieve the ZKeyField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKeyField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode, DataTableID, KeyID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZKeyField for the service
   Description: Calls UpdateExt to update ZKeyField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZKeyField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode, DataTableID, KeyID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZKeyField item
   Description: Call UpdateExt to delete ZKeyField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZKeyField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param KeyID: Desc: KeyID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataTableListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseZDataTable, whereClauseZLookupLink, whereClauseZLinkColumn, whereClauseZLookupField, whereClauseZDataField, whereClauseZKey, whereClauseZKeyField, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseZDataTable=" + whereClauseZDataTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZLookupLink=" + whereClauseZLookupLink
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZLinkColumn=" + whereClauseZLinkColumn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZLookupField=" + whereClauseZLookupField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZDataField=" + whereClauseZDataField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZKey=" + whereClauseZKey
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZKeyField=" + whereClauseZKeyField
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(systemCode, dataTableID, epicorHeaders = None):
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
   params += "systemCode=" + systemCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "dataTableID=" + dataTableID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLikeDataFieldName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLikeDataFieldName
   Description: This method should be invoked when the LikeFieldName changes.
   OperationID: ChangeLikeDataFieldName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLikeDataFieldName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLikeDataFieldName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetKeyFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetKeyFields
   Description: Get key fields.
   OperationID: GetKeyFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetKeyFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKeyFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetKeys
   Description: Get key fields for table
   OperationID: GetKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGuid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGuid
   Description: Validate the GUID
   OperationID: ValidateGuid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGuid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGuid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNFormatString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNFormatString
   Description: Get the formated string
   OperationID: ValidateNFormatString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNFormatString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNFormatString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNFormatNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNFormatNumber
   Description: Get the formated number
   OperationID: ValidateNFormatNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNFormatNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNFormatNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Synchronize(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Synchronize
   Description: Synchronize one table
   OperationID: Synchronize
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Synchronize_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Synchronize_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SynchronizeClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SynchronizeClass
   Description: Synchronize all the tables of a class
   OperationID: SynchronizeClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SynchronizeClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SynchronizeClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasDBTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasDBTable
   Description: Checks if DB table exists in database
   OperationID: HasDBTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasDBTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasDBTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasZDataTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasZDataTable
   Description: Checks if DB table exists in database
   OperationID: HasZDataTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasZDataTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasZDataTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExtendedTableSyncInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtendedTableSyncInfo
   Description: Get extended table sync information.
   OperationID: GetExtendedTableSyncInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtendedTableSyncInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtendedTableSyncInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExtendedTableSyncDetailsMessage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtendedTableSyncDetailsMessage
   Description: Get extended table sync information.
   OperationID: GetExtendedTableSyncDetailsMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtendedTableSyncDetailsMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtendedTableSyncDetailsMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CanModifyUDFieldFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CanModifyUDFieldFormat
   Description: Check if UD Field Format can be modified
   OperationID: CanModifyUDFieldFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanModifyUDFieldFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanModifyUDFieldFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClassicFieldName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClassicFieldName
   Description: Check if UD Field Name is the classic fieldName
   OperationID: ClassicFieldName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClassicFieldName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClassicFieldName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZDataTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZDataTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZDataTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZDataTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZDataTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZLookupLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZLookupLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZLookupLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZLookupLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZLookupLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZLinkColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZLinkColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZLinkColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZLinkColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZLinkColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZLookupField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZLookupField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZLookupField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZLookupField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZLookupField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZDataField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZDataField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZDataField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZDataField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZDataField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZKey
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZKeyField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZKeyField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZKeyField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZKeyField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZKeyField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZDataFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZDataTableListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZDataTableRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZKeyFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZKeyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLinkColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZLinkColumnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZLookupFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupLinkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZLookupLinkRow] = obj["value"]
      pass

class Ice_Tablesets_ZDataFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.Required:bool = obj["Required"]
      """  Required  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Read Only  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.External:bool = obj["External"]
      """  External  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Included:bool = obj["Included"]
      """  Included  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldScale:int = obj["FieldScale"]
      """  Field Scale  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.InitialValue:str = obj["InitialValue"]
      """  Initial Value  """  
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      """  Indicates Data Field is a Description Field  """  
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      """  LikeDataFieldSystemCode  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.RequiredModules:str = obj["RequiredModules"]
      """  A delimited list of the modules required by this object.  """  
      self.Delimiters:str = obj["Delimiters"]
      """  Contains the characters that are used as delimiters for when building a list from values of this data field. So during data entry we should validate none of these charater is in the value of this data field.  """  
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      """  Code and Description value list  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Fiel Name reference  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      """  Indicates Data Field is a Currency code column  """  
      self.CurrencyType:str = obj["CurrencyType"]
      """  Currency Type  """  
      self.CurrencySource:str = obj["CurrencySource"]
      """  Currency Source  """  
      self.BizType:str = obj["BizType"]
      """   Further defines the Business use of the Field
Valid values are "Currency,Quantity,UOM"  """  
      self.UDLikeDataFieldSystemCode:str = obj["UDLikeDataFieldSystemCode"]
      """  UDLikeDataFieldSystemCode  """  
      self.UDLikeDataFieldTableID:str = obj["UDLikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.UDLikeDataFieldName:str = obj["UDLikeDataFieldName"]
      """  User Defined Extended Property Like Data Field Name.  """  
      self.UDFieldFormat:str = obj["UDFieldFormat"]
      """  User Defined Extended Property Field Property  """  
      self.UDFieldLabel:str = obj["UDFieldLabel"]
      """  User Defined Extended Property Field Label  """  
      self.UDInitialValue:str = obj["UDInitialValue"]
      """  User Defined Extended Property Initial Value  """  
      self.UDRequired:bool = obj["UDRequired"]
      """  User Defined Extended Property Required flag  """  
      self.UDReadOnly:bool = obj["UDReadOnly"]
      """  User Defined Extended Property Read Only flag  """  
      self.UDCurrencyCodeColumn:str = obj["UDCurrencyCodeColumn"]
      """  User Defined Extended Property Currency code column flag  """  
      self.UDCurrencyType:str = obj["UDCurrencyType"]
      """  User Defined Extended Property Currency Type  """  
      self.UDCurrencySource:str = obj["UDCurrencySource"]
      """  User Defined Extended Property currency Source  """  
      self.UDPredictiveSearchID:str = obj["UDPredictiveSearchID"]
      """  UDPredictiveSearchID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CausesOnChange:bool = obj["CausesOnChange"]
      """  CausesOnChange  """  
      self.DefaultFieldScale:int = obj["DefaultFieldScale"]
      self.DefaultFormat:str = obj["DefaultFormat"]
      self.DefaultInitValue:str = obj["DefaultInitValue"]
      self.DefaultLabel:str = obj["DefaultLabel"]
      self.DelimiterCheck:bool = obj["DelimiterCheck"]
      """  DelimiterCheck  """  
      self.EffectiveCurrencySource:str = obj["EffectiveCurrencySource"]
      self.EffectiveCurrencyType:str = obj["EffectiveCurrencyType"]
      self.LinkedColumn:str = obj["LinkedColumn"]
      self.UDCodeType:str = obj["UDCodeType"]
      """  UD Code Type  """  
      self.UDLinkedColumn:str = obj["UDLinkedColumn"]
      """  UD Linked Column  """  
      self.UDUomColumn:str = obj["UDUomColumn"]
      """  UD UOM Column  """  
      self.UomColumn:str = obj["UomColumn"]
      self.ZoneBAQ:str = obj["ZoneBAQ"]
      """  Zone Baq ID  """  
      self.ZoneSearchOnEmptyControl:bool = obj["ZoneSearchOnEmptyControl"]
      """  Allow Zone Search When control is Empty  """  
      self.Company:str = obj["Company"]
      self.IsHidden:bool = obj["IsHidden"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataTableListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database TableName  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Where Clause  """  
      self.RestrictedByTer:bool = obj["RestrictedByTer"]
      """  If yes then this table is restricted by accessiable sales territories  """  
      self.RestrictedByPlant:bool = obj["RestrictedByPlant"]
      """  If yes then this table is restricted by accessiable Sites  """  
      self.TableType:str = obj["TableType"]
      """   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.TableLabel:str = obj["TableLabel"]
      """  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  """  
      self.ChgLogID:str = obj["ChgLogID"]
      """  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataTableRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database TableName  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Where Clause  """  
      self.RestrictedByTer:bool = obj["RestrictedByTer"]
      """  If yes then this table is restricted by accessiable sales territories  """  
      self.RestrictedByPlant:bool = obj["RestrictedByPlant"]
      """  If yes then this table is restricted by accessiable Sites  """  
      self.FullSync:bool = obj["FullSync"]
      """  controls the behavior of  object designer field synchronization with the db schema. When set True, the synch process will bring in all the DB fields from a DB table into the zDataFields table. When set to False, the synch process will only update the fields that are currently in the zDataFields table.  """  
      self.TableType:str = obj["TableType"]
      """   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.TableLabel:str = obj["TableLabel"]
      """  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  """  
      self.ChgLogID:str = obj["ChgLogID"]
      """  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  """  
      self.BOUpdate:str = obj["BOUpdate"]
      """  BO Used to Update Table  """  
      self.UpdateMethod:str = obj["UpdateMethod"]
      """  BO Method used for Update  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.Interface:str = obj["Interface"]
      """  Interface  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZKeyFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZKeyRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsPrimaryKey:bool = obj["IsPrimaryKey"]
      """  Primary Key  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.External:bool = obj["External"]
      """  External Key  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZLinkColumnRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.LinkID:str = obj["LinkID"]
      """  Link ID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkColName:str = obj["LinkColName"]
      """  LinkColName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ZLookupLinkForeignDataTableID:str = obj["ZLookupLinkForeignDataTableID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZLookupFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.LookupID:str = obj["LookupID"]
      """  LookUp ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.IsConst:bool = obj["IsConst"]
      """  Constant Field indicator  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ForeignFieldName:str = obj["ForeignFieldName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZLookupLinkRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.LookupID:str = obj["LookupID"]
      """  LookUp ID  """  
      self.ForeignSystemCode:str = obj["ForeignSystemCode"]
      """  ForeignSystemCode  """  
      self.ForeignDataTableID:str = obj["ForeignDataTableID"]
      """  Foreign DataTable ID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ValidationRequired:bool = obj["ValidationRequired"]
      """  Validation Required  """  
      self.ValidationPhraseEx:str = obj["ValidationPhraseEx"]
      """  Extra validation  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.ValidationOnly:bool = obj["ValidationOnly"]
      """  Indicating this lookup link is not used for pulling the IsDisplayField  to the master table but for checking referential integraty.  """  
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
class CanModifyUDFieldFormat_input:
   """ Required : 
   ts
   """  
   def __init__(self, obj):
      self.ts:list[Ice_Tablesets_ZDataTableTableset] = obj["ts"]
      pass

class CanModifyUDFieldFormat_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if can be modified  """  
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeLikeDataFieldName_input:
   """ Required : 
   systemCode
   dataTableID
   fieldName
   dbTableName
   external
   likeDataFieldSystemCode
   likeDataFieldTableID
   likeDataFieldName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.fieldName:str = obj["fieldName"]
      self.dbTableName:str = obj["dbTableName"]
      self.external:bool = obj["external"]
      self.likeDataFieldSystemCode:str = obj["likeDataFieldSystemCode"]
      self.likeDataFieldTableID:str = obj["likeDataFieldTableID"]
      self.likeDataFieldName:str = obj["likeDataFieldName"]
      pass

class ChangeLikeDataFieldName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultFormat:str = obj["parameters"]
      self.defaultLabel:str = obj["parameters"]
      self.defaultInitValue:str = obj["parameters"]
      self.defaultFieldScale:int = obj["parameters"]
      pass

      """  output parameters  """  

class ClassicFieldName_input:
   """ Required : 
   fieldName
   """  
   def __init__(self, obj):
      self.fieldName:str = obj["fieldName"]
      """  data (only need the field row)  """  
      pass

class ClassicFieldName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if can be modified  """  
      pass

class DeleteByID_input:
   """ Required : 
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataTableTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZDataTableTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZDataTableTableset] = obj["returnObj"]
      pass

class GetExtendedTableSyncDetailsMessage_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name (Ice, Erp)  """  
      self.tableName:str = obj["tableName"]
      """  table name (e.g. Tip_UD)  """  
      pass

class GetExtendedTableSyncDetailsMessage_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if everything is in sync  """  
      pass

   def parameters(self, obj):
      self.dbExists:bool = obj["dbExists"]
      self.zDataSynced:bool = obj["zDataSynced"]
      self.dataModelSynced:bool = obj["dataModelSynced"]
      self.syncMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetExtendedTableSyncInfo_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name (Ice, Erp)  """  
      self.tableName:str = obj["tableName"]
      """  table name (e.g. Tip_UD)  """  
      pass

class GetExtendedTableSyncInfo_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if everything is in sync  """  
      pass

   def parameters(self, obj):
      self.dbExists:bool = obj["dbExists"]
      self.zDataSynced:bool = obj["zDataSynced"]
      self.dataModelSynced:bool = obj["dataModelSynced"]
      pass

      """  output parameters  """  

class GetKeyFields_input:
   """ Required : 
   systemCode
   dataTableID
   keyID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      """  Table ID  """  
      self.keyID:str = obj["keyID"]
      """  Proposed KeyID  """  
      pass

class GetKeyFields_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataTableTableset] = obj["returnObj"]
      pass

class GetKeys_input:
   """ Required : 
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      """  Table ID  """  
      pass

class GetKeys_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataTableTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZDataTableListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewZDataField_input:
   """ Required : 
   ds
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetNewZDataField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZDataTable_input:
   """ Required : 
   ds
   systemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      pass

class GetNewZDataTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZKeyField_input:
   """ Required : 
   ds
   systemCode
   dataTableID
   keyID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.keyID:str = obj["keyID"]
      pass

class GetNewZKeyField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZKey_input:
   """ Required : 
   ds
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetNewZKey_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZLinkColumn_input:
   """ Required : 
   ds
   systemCode
   dataTableID
   linkID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.linkID:str = obj["linkID"]
      pass

class GetNewZLinkColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZLookupField_input:
   """ Required : 
   ds
   systemCode
   dataTableID
   lookupID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.lookupID:str = obj["lookupID"]
      pass

class GetNewZLookupField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZLookupLink_input:
   """ Required : 
   ds
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetNewZLookupLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseZDataTable
   whereClauseZLookupLink
   whereClauseZLinkColumn
   whereClauseZLookupField
   whereClauseZDataField
   whereClauseZKey
   whereClauseZKeyField
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseZDataTable:str = obj["whereClauseZDataTable"]
      self.whereClauseZLookupLink:str = obj["whereClauseZLookupLink"]
      self.whereClauseZLinkColumn:str = obj["whereClauseZLinkColumn"]
      self.whereClauseZLookupField:str = obj["whereClauseZLookupField"]
      self.whereClauseZDataField:str = obj["whereClauseZDataField"]
      self.whereClauseZKey:str = obj["whereClauseZKey"]
      self.whereClauseZKeyField:str = obj["whereClauseZKeyField"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataTableTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class HasDBTable_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name (Ice, Erp)  """  
      self.tableName:str = obj["tableName"]
      """  table name (e.g. Tip_UD)  """  
      pass

class HasDBTable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if exists  """  
      pass

class HasZDataTable_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name (Ice, Erp)  """  
      self.tableName:str = obj["tableName"]
      """  table name (e.g. Tip_UD)  """  
      pass

class HasZDataTable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if exists  """  
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

class Ice_Tablesets_UpdExtZDataTableTableset:
   def __init__(self, obj):
      self.ZDataTable:list[Ice_Tablesets_ZDataTableRow] = obj["ZDataTable"]
      self.ZLookupLink:list[Ice_Tablesets_ZLookupLinkRow] = obj["ZLookupLink"]
      self.ZLinkColumn:list[Ice_Tablesets_ZLinkColumnRow] = obj["ZLinkColumn"]
      self.ZLookupField:list[Ice_Tablesets_ZLookupFieldRow] = obj["ZLookupField"]
      self.ZDataField:list[Ice_Tablesets_ZDataFieldRow] = obj["ZDataField"]
      self.ZKey:list[Ice_Tablesets_ZKeyRow] = obj["ZKey"]
      self.ZKeyField:list[Ice_Tablesets_ZKeyFieldRow] = obj["ZKeyField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZDataFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.Required:bool = obj["Required"]
      """  Required  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  Read Only  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.External:bool = obj["External"]
      """  External  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Included:bool = obj["Included"]
      """  Included  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldScale:int = obj["FieldScale"]
      """  Field Scale  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.InitialValue:str = obj["InitialValue"]
      """  Initial Value  """  
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      """  Indicates Data Field is a Description Field  """  
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      """  LikeDataFieldSystemCode  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.RequiredModules:str = obj["RequiredModules"]
      """  A delimited list of the modules required by this object.  """  
      self.Delimiters:str = obj["Delimiters"]
      """  Contains the characters that are used as delimiters for when building a list from values of this data field. So during data entry we should validate none of these charater is in the value of this data field.  """  
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      """  Code and Description value list  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Fiel Name reference  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      """  Indicates Data Field is a Currency code column  """  
      self.CurrencyType:str = obj["CurrencyType"]
      """  Currency Type  """  
      self.CurrencySource:str = obj["CurrencySource"]
      """  Currency Source  """  
      self.BizType:str = obj["BizType"]
      """   Further defines the Business use of the Field
Valid values are "Currency,Quantity,UOM"  """  
      self.UDLikeDataFieldSystemCode:str = obj["UDLikeDataFieldSystemCode"]
      """  UDLikeDataFieldSystemCode  """  
      self.UDLikeDataFieldTableID:str = obj["UDLikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.UDLikeDataFieldName:str = obj["UDLikeDataFieldName"]
      """  User Defined Extended Property Like Data Field Name.  """  
      self.UDFieldFormat:str = obj["UDFieldFormat"]
      """  User Defined Extended Property Field Property  """  
      self.UDFieldLabel:str = obj["UDFieldLabel"]
      """  User Defined Extended Property Field Label  """  
      self.UDInitialValue:str = obj["UDInitialValue"]
      """  User Defined Extended Property Initial Value  """  
      self.UDRequired:bool = obj["UDRequired"]
      """  User Defined Extended Property Required flag  """  
      self.UDReadOnly:bool = obj["UDReadOnly"]
      """  User Defined Extended Property Read Only flag  """  
      self.UDCurrencyCodeColumn:str = obj["UDCurrencyCodeColumn"]
      """  User Defined Extended Property Currency code column flag  """  
      self.UDCurrencyType:str = obj["UDCurrencyType"]
      """  User Defined Extended Property Currency Type  """  
      self.UDCurrencySource:str = obj["UDCurrencySource"]
      """  User Defined Extended Property currency Source  """  
      self.UDPredictiveSearchID:str = obj["UDPredictiveSearchID"]
      """  UDPredictiveSearchID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  CGCCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CausesOnChange:bool = obj["CausesOnChange"]
      """  CausesOnChange  """  
      self.DefaultFieldScale:int = obj["DefaultFieldScale"]
      self.DefaultFormat:str = obj["DefaultFormat"]
      self.DefaultInitValue:str = obj["DefaultInitValue"]
      self.DefaultLabel:str = obj["DefaultLabel"]
      self.DelimiterCheck:bool = obj["DelimiterCheck"]
      """  DelimiterCheck  """  
      self.EffectiveCurrencySource:str = obj["EffectiveCurrencySource"]
      self.EffectiveCurrencyType:str = obj["EffectiveCurrencyType"]
      self.LinkedColumn:str = obj["LinkedColumn"]
      self.UDCodeType:str = obj["UDCodeType"]
      """  UD Code Type  """  
      self.UDLinkedColumn:str = obj["UDLinkedColumn"]
      """  UD Linked Column  """  
      self.UDUomColumn:str = obj["UDUomColumn"]
      """  UD UOM Column  """  
      self.UomColumn:str = obj["UomColumn"]
      self.ZoneBAQ:str = obj["ZoneBAQ"]
      """  Zone Baq ID  """  
      self.ZoneSearchOnEmptyControl:bool = obj["ZoneSearchOnEmptyControl"]
      """  Allow Zone Search When control is Empty  """  
      self.Company:str = obj["Company"]
      self.IsHidden:bool = obj["IsHidden"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataTableListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database TableName  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Where Clause  """  
      self.RestrictedByTer:bool = obj["RestrictedByTer"]
      """  If yes then this table is restricted by accessiable sales territories  """  
      self.RestrictedByPlant:bool = obj["RestrictedByPlant"]
      """  If yes then this table is restricted by accessiable Sites  """  
      self.TableType:str = obj["TableType"]
      """   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.TableLabel:str = obj["TableLabel"]
      """  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  """  
      self.ChgLogID:str = obj["ChgLogID"]
      """  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataTableListTableset:
   def __init__(self, obj):
      self.ZDataTableList:list[Ice_Tablesets_ZDataTableListRow] = obj["ZDataTableList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZDataTableRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database TableName  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Where Clause  """  
      self.RestrictedByTer:bool = obj["RestrictedByTer"]
      """  If yes then this table is restricted by accessiable sales territories  """  
      self.RestrictedByPlant:bool = obj["RestrictedByPlant"]
      """  If yes then this table is restricted by accessiable Sites  """  
      self.FullSync:bool = obj["FullSync"]
      """  controls the behavior of  object designer field synchronization with the db schema. When set True, the synch process will bring in all the DB fields from a DB table into the zDataFields table. When set to False, the synch process will only update the fields that are currently in the zDataFields table.  """  
      self.TableType:str = obj["TableType"]
      """   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.TableLabel:str = obj["TableLabel"]
      """  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  """  
      self.ChgLogID:str = obj["ChgLogID"]
      """  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  """  
      self.BOUpdate:str = obj["BOUpdate"]
      """  BO Used to Update Table  """  
      self.UpdateMethod:str = obj["UpdateMethod"]
      """  BO Method used for Update  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.Interface:str = obj["Interface"]
      """  Interface  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataTableTableset:
   def __init__(self, obj):
      self.ZDataTable:list[Ice_Tablesets_ZDataTableRow] = obj["ZDataTable"]
      self.ZLookupLink:list[Ice_Tablesets_ZLookupLinkRow] = obj["ZLookupLink"]
      self.ZLinkColumn:list[Ice_Tablesets_ZLinkColumnRow] = obj["ZLinkColumn"]
      self.ZLookupField:list[Ice_Tablesets_ZLookupFieldRow] = obj["ZLookupField"]
      self.ZDataField:list[Ice_Tablesets_ZDataFieldRow] = obj["ZDataField"]
      self.ZKey:list[Ice_Tablesets_ZKeyRow] = obj["ZKey"]
      self.ZKeyField:list[Ice_Tablesets_ZKeyFieldRow] = obj["ZKeyField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZKeyFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZKeyRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsPrimaryKey:bool = obj["IsPrimaryKey"]
      """  Primary Key  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.External:bool = obj["External"]
      """  External Key  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZLinkColumnRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.LinkID:str = obj["LinkID"]
      """  Link ID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkColName:str = obj["LinkColName"]
      """  LinkColName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ZLookupLinkForeignDataTableID:str = obj["ZLookupLinkForeignDataTableID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZLookupFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.LookupID:str = obj["LookupID"]
      """  LookUp ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.IsConst:bool = obj["IsConst"]
      """  Constant Field indicator  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ForeignFieldName:str = obj["ForeignFieldName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZLookupLinkRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.LookupID:str = obj["LookupID"]
      """  LookUp ID  """  
      self.ForeignSystemCode:str = obj["ForeignSystemCode"]
      """  ForeignSystemCode  """  
      self.ForeignDataTableID:str = obj["ForeignDataTableID"]
      """  Foreign DataTable ID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ValidationRequired:bool = obj["ValidationRequired"]
      """  Validation Required  """  
      self.ValidationPhraseEx:str = obj["ValidationPhraseEx"]
      """  Extra validation  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.ValidationOnly:bool = obj["ValidationOnly"]
      """  Indicating this lookup link is not used for pulling the IsDisplayField  to the master table but for checking referential integraty.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class SynchronizeClass_input:
   """ Required : 
   systemCode
   className
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System code  """  
      self.className:str = obj["className"]
      """  Class name  """  
      pass

class SynchronizeClass_output:
   def __init__(self, obj):
      pass

class Synchronize_input:
   """ Required : 
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      """  Table ID  """  
      pass

class Synchronize_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtZDataTableTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtZDataTableTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataTableTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateGuid_input:
   """ Required : 
   inputValue
   """  
   def __init__(self, obj):
      self.inputValue:str = obj["inputValue"]
      pass

class ValidateGuid_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The formated Guid  """  
      pass

class ValidateNFormatNumber_input:
   """ Required : 
   inputValue
   format
   dataType
   """  
   def __init__(self, obj):
      self.inputValue:str = obj["inputValue"]
      self.format:str = obj["format"]
      self.dataType:str = obj["dataType"]
      pass

class ValidateNFormatNumber_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The formated Number  """  
      pass

   def parameters(self, obj):
      self.inputValue:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateNFormatString_input:
   """ Required : 
   format
   inputValue
   """  
   def __init__(self, obj):
      self.format:str = obj["format"]
      self.inputValue:str = obj["inputValue"]
      pass

class ValidateNFormatString_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The formated String  """  
      pass

