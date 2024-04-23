import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ExtensionSvc
# Description: Extensions.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Extensions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Extensions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Extensions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions",headers=creds) as resp:
           return await resp.json()

async def post_Extensions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Extensions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Extensions_ExtensionSetID(ExtensionSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Extension item
   Description: Calls GetByID to retrieve the Extension item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Extension
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Extensions_ExtensionSetID(ExtensionSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Extension for the service
   Description: Calls UpdateExt to update Extension. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Extension
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Extensions_ExtensionSetID(ExtensionSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Extension item
   Description: Call UpdateExt to delete Extension item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Extension
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Extensions_ExtensionSetID_ExtensionSetMappings(ExtensionSetID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtensionSetMappings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionSetMappings1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionSetMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionSetMappings",headers=creds) as resp:
           return await resp.json()

async def get_Extensions_ExtensionSetID_ExtensionSetMappings_Company_ExtensionSetID(ExtensionSetID, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionSetMapping item
   Description: Calls GetByID to retrieve the ExtensionSetMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionSetMapping1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Extensions_ExtensionSetID_ExtensionTables(ExtensionSetID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtensionTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionTables1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionTables",headers=creds) as resp:
           return await resp.json()

async def get_Extensions_ExtensionSetID_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID, SystemCode, DataTableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionTable item
   Description: Calls GetByID to retrieve the ExtensionTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTable1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/Extensions(" + ExtensionSetID + ")/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionSetMappings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtensionSetMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionSetMappings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionSetMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings",headers=creds) as resp:
           return await resp.json()

async def post_ExtensionSetMappings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionSetMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtensionSetMappings_Company_ExtensionSetID(Company, ExtensionSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionSetMapping item
   Description: Calls GetByID to retrieve the ExtensionSetMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionSetMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtensionSetMappings_Company_ExtensionSetID(Company, ExtensionSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtensionSetMapping for the service
   Description: Calls UpdateExt to update ExtensionSetMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionSetMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionSetMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtensionSetMappings_Company_ExtensionSetID(Company, ExtensionSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtensionSetMapping item
   Description: Call UpdateExt to delete ExtensionSetMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionSetMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionSetMappings(" + Company + "," + ExtensionSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtensionTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables",headers=creds) as resp:
           return await resp.json()

async def post_ExtensionTables(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID, SystemCode, DataTableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionTable item
   Description: Calls GetByID to retrieve the ExtensionTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTable
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID, SystemCode, DataTableID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtensionTable for the service
   Description: Calls UpdateExt to update ExtensionTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionTable
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtensionTables_ExtensionSetID_SystemCode_DataTableID(ExtensionSetID, SystemCode, DataTableID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtensionTable item
   Description: Call UpdateExt to delete ExtensionTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionTable
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionColumns(ExtensionSetID, SystemCode, DataTableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtensionColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionColumns1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionColumns",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID, SystemCode, DataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionColumn item
   Description: Calls GetByID to retrieve the ExtensionColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionColumn1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionTableKeys(ExtensionSetID, SystemCode, DataTableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtensionTableKeys items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionTableKeys1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionTableKeys",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTables_ExtensionSetID_SystemCode_DataTableID_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID, SystemCode, DataTableID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionTableKey item
   Description: Calls GetByID to retrieve the ExtensionTableKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTableKey1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTables(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + ")/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionColumns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtensionColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionColumns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns",headers=creds) as resp:
           return await resp.json()

async def post_ExtensionColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID, SystemCode, DataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionColumn item
   Description: Calls GetByID to retrieve the ExtensionColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionColumn
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID, SystemCode, DataTableID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtensionColumn for the service
   Description: Calls UpdateExt to update ExtensionColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionColumn
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtensionColumns_ExtensionSetID_SystemCode_DataTableID_FieldName(ExtensionSetID, SystemCode, DataTableID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtensionColumn item
   Description: Call UpdateExt to delete ExtensionColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionColumn
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionColumns(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTableKeys(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtensionTableKeys items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionTableKeys
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionTableKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys",headers=creds) as resp:
           return await resp.json()

async def post_ExtensionTableKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionTableKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID, SystemCode, DataTableID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionTableKey item
   Description: Calls GetByID to retrieve the ExtensionTableKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionTableKey
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID, SystemCode, DataTableID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtensionTableKey for the service
   Description: Calls UpdateExt to update ExtensionTableKey. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionTableKey
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionTableKeyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtensionTableKeys_ExtensionSetID_SystemCode_DataTableID_Seq(ExtensionSetID, SystemCode, DataTableID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtensionTableKey item
   Description: Call UpdateExt to delete ExtensionTableKey item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionTableKey
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionTableKeys(" + ExtensionSetID + "," + SystemCode + "," + DataTableID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionRelations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtensionRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionRelations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations",headers=creds) as resp:
           return await resp.json()

async def post_ExtensionRelations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID(ExtensionSetID, SystemCode, DataSetID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionRelation item
   Description: Calls GetByID to retrieve the ExtensionRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionRelation
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID(ExtensionSetID, SystemCode, DataSetID, RelationID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtensionRelation for the service
   Description: Calls UpdateExt to update ExtensionRelation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionRelation
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID(ExtensionSetID, SystemCode, DataSetID, RelationID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtensionRelation item
   Description: Call UpdateExt to delete ExtensionRelation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionRelation
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID_ExtensionRelationColumns(ExtensionSetID, SystemCode, DataSetID, RelationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtensionRelationColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtensionRelationColumns1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRelationColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")/ExtensionRelationColumns",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionRelations_ExtensionSetID_SystemCode_DataSetID_RelationID_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID, SystemCode, DataSetID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionRelationColumn item
   Description: Calls GetByID to retrieve the ExtensionRelationColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionRelationColumn1
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelations(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + ")/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtensionRelationColumns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtensionRelationColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtensionRelationColumns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionRelationColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns",headers=creds) as resp:
           return await resp.json()

async def post_ExtensionRelationColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtensionRelationColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID, SystemCode, DataSetID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtensionRelationColumn item
   Description: Calls GetByID to retrieve the ExtensionRelationColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtensionRelationColumn
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID, SystemCode, DataSetID, RelationID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtensionRelationColumn for the service
   Description: Calls UpdateExt to update ExtensionRelationColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtensionRelationColumn
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ExtensionRelationColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtensionRelationColumns_ExtensionSetID_SystemCode_DataSetID_RelationID_Seq(ExtensionSetID, SystemCode, DataSetID, RelationID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtensionRelationColumn item
   Description: Call UpdateExt to delete ExtensionRelationColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtensionRelationColumn
      :param ExtensionSetID: Desc: ExtensionSetID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/ExtensionRelationColumns(" + ExtensionSetID + "," + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExtensionListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtension, whereClauseExtensionSetMapping, whereClauseExtensionTable, whereClauseExtensionColumn, whereClauseExtensionRelation, whereClauseExtensionRelationColumn, whereClauseExtensionTableKey, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseExtension=" + whereClauseExtension
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtensionSetMapping=" + whereClauseExtensionSetMapping
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtensionTable=" + whereClauseExtensionTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtensionColumn=" + whereClauseExtensionColumn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtensionRelation=" + whereClauseExtensionRelation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtensionRelationColumn=" + whereClauseExtensionRelationColumn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtensionTableKey=" + whereClauseExtensionTableKey
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extensionSetID, epicorHeaders = None):
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
   params += "extensionSetID=" + extensionSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetExtensionSetAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtensionSetAssembly
   Description: Returns object representing extension set assembly body with optional debug symbols.
   OperationID: GetExtensionSetAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtensionSetAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtensionSetAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtensionTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtensionTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtensionColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtensionColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtensionTableKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtensionTableKey
   Description: Creates a new pk row for the extension table
   OperationID: GetNewExtensionTableKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionTableKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionTableKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetupPeerTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetupPeerTable
   Description: Create structure for peer table - primary key and relationship
   OperationID: SetupPeerTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetupPeerTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetupPeerTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExtensionSetExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExtensionSetExists
   Description: Checks whether extension set with provided ID exists.
   OperationID: ExtensionSetExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExtensionSetExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExtensionSetExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsRestrictedSystemCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsRestrictedSystemCode
   Description: Checks whether SystemCode is Epicor Delivered SystemCode.
   OperationID: IsRestrictedSystemCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsRestrictedSystemCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsRestrictedSystemCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InstallExtensionSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InstallExtensionSet
   Description: Installs provided assembly alongside with optional symbols info.
   OperationID: InstallExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InstallExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InstallExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MapExtensionSetToCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MapExtensionSetToCompany
   Description: Associates extension set related to the specified ID to the specified company.
   OperationID: MapExtensionSetToCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MapExtensionSetToCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MapExtensionSetToCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMapping(epicorHeaders = None):
   """  
   Summary: Invoke method GetMapping
   Description: Returns extensions registered in companies as well as productizations from global level
   OperationID: GetMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RemoveExtensionSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveExtensionSet
   Description: Removes extension set assembly alongside with related metadata
   OperationID: RemoveExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataSetTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataSetTables
   Description: Gets the list of tables (both base and extension) in a dataset.
   OperationID: GetDataSetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportExtensionSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportExtensionSet
   Description: Returns byte[] representing extension set tableset and assembly body with optional debug symbols.
   OperationID: ExportExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportExtensionSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportExtensionSet
   Description: Returns byte[] representing extension set tableset and assembly body with optional debug symbols.
   OperationID: ImportExtensionSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportExtensionSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportExtensionSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckExtensionTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckExtensionTable
   Description: Validates the structure of the extension table definition.
   OperationID: CheckExtensionTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExtensionTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExtensionTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckExtensionTableStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckExtensionTableStatus
   Description: Validates the structure of the extension table definition.
   OperationID: CheckExtensionTableStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExtensionTableStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExtensionTableStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompaniesUsingTheExtension(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCompaniesUsingTheExtension
   Description: Gets the companies using the extensionSetID.
   OperationID: GetCompaniesUsingTheExtension
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompaniesUsingTheExtension_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompaniesUsingTheExtension_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteExtensionSetMappingForCurrentCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteExtensionSetMappingForCurrentCompany
   Description: Deletes the extension set mapping for company in session.
   OperationID: DeleteExtensionSetMappingForCurrentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteExtensionSetMappingForCurrentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteExtensionSetMappingForCurrentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExtensionSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtensionSetID
   Description: Generates the Extension ID for a given provider, level and product
   OperationID: GetExtensionSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtensionSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtensionSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPeerTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPeerTable
   Description: Validates or check the status of a peer table relation.
   OperationID: CheckPeerTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPeerTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPeerTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtension(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtension
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtension
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtension_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtension_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtensionSetMapping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtensionSetMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionSetMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionSetMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionSetMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtensionRelation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtensionRelation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionRelation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionRelation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionRelation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtensionRelationColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtensionRelationColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtensionRelationColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtensionRelationColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtensionRelationColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExtensionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionColumnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionRelationColumnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRelationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionRelationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionSetMappingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionSetMappingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableKeyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionTableKeyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExtensionTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExtensionTableRow] = obj["value"]
      pass

class Ice_Tablesets_ExtensionColumnRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SystemCode:str = obj["SystemCode"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Seq:int = obj["Seq"]
      self.Description:str = obj["Description"]
      self.FieldScale:int = obj["FieldScale"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.InitialValue:str = obj["InitialValue"]
      self.Required:bool = obj["Required"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.IsHidden:bool = obj["IsHidden"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      """  Code and Description value list  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionListRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionRelationColumnRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSetID  """  
      self.RelationID:str = obj["RelationID"]
      """  RelationID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.ParentFieldName:str = obj["ParentFieldName"]
      """  ParentFieldName  """  
      self.ChildFieldName:str = obj["ChildFieldName"]
      """  ChildFieldName  """  
      self.CompOp:str = obj["CompOp"]
      """  CompOp  """  
      self.IsConst:bool = obj["IsConst"]
      """  IsConst  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionRelationRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSetID  """  
      self.RelationID:str = obj["RelationID"]
      """  RelationID  """  
      self.ParentSystemCode:str = obj["ParentSystemCode"]
      """  ParentSystemCode  """  
      self.ParentDataTableID:str = obj["ParentDataTableID"]
      """  ParentDataTableID  """  
      self.ChildSystemCode:str = obj["ChildSystemCode"]
      """  ChildSystemCode  """  
      self.ChildDataTableID:str = obj["ChildDataTableID"]
      """  ChildDataTableID  """  
      self.KeyID:str = obj["KeyID"]
      """  KeyID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.Type:int = obj["Type"]
      """  Type  """  
      self.TreatAsPeer:bool = obj["TreatAsPeer"]
      """  TreatAsPeer  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullParentTableName:str = obj["FullParentTableName"]
      self.FullChildTableName:str = obj["FullChildTableName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.Provider:str = obj["Provider"]
      """  Provider  """  
      self.Product:str = obj["Product"]
      """  Product  """  
      self.Assembly:str = obj["Assembly"]
      """  Assembly  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.Level:int = obj["Level"]
      """  Level  """  
      self.Disabled:bool = obj["Disabled"]
      """  Disabled  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GenIMTable:bool = obj["GenIMTable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionSetMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.Order:int = obj["Order"]
      """  Order  """  
      self.Disabled:bool = obj["Disabled"]
      """  Disabled  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionTableKeyRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SystemCode:str = obj["SystemCode"]
      self.Seq:int = obj["Seq"]
      self.FieldName:str = obj["FieldName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionTableRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.Description:str = obj["Description"]
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SystemCode:str = obj["SystemCode"]
      self.DataSetID:str = obj["DataSetID"]
      self.DataSetSystemCode:str = obj["DataSetSystemCode"]
      self.TableType:str = obj["TableType"]
      self.GenIMTable:bool = obj["GenIMTable"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckExtensionTableStatus_input:
   """ Required : 
   systemCode
   tableName
   createFullReport
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  Table system code  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      self.createFullReport:bool = obj["createFullReport"]
      """  If true, generate full report, otherwise only until first discrepancy in the column definition  """  
      pass

class CheckExtensionTableStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtensionValidationTableset] = obj["returnObj"]
      pass

class CheckExtensionTable_input:
   """ Required : 
   systemCode
   tableName
   createFullReport
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  Table system code  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      self.createFullReport:bool = obj["createFullReport"]
      """  If true, generate full report, otherwise only until first discrepancy in the column definition  """  
      pass

class CheckExtensionTable_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of errors found  """  
      pass

   def parameters(self, obj):
      self.validationFlag:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPeerTable_input:
   """ Required : 
   extensionSetID
   parentDataSetID
   parentSystemCode
   systemCode
   tableName
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  Extension ID  """  
      self.parentDataSetID:str = obj["parentDataSetID"]
      """  Parent table (or base table) dataset ID.  """  
      self.parentSystemCode:str = obj["parentSystemCode"]
      """  Parent table (or base table) system code.  """  
      self.systemCode:str = obj["systemCode"]
      """  Peer (extension) table dataset ID.  """  
      self.tableName:str = obj["tableName"]
      """  Peer (extension) table table ID.  """  
      pass

class CheckPeerTable_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtensionValidationTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteExtensionSetMappingForCurrentCompany_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  The extension set identifier.  """  
      pass

class DeleteExtensionSetMappingForCurrentCompany_output:
   def __init__(self, obj):
      pass

class ExportExtensionSet_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  ID of the extension set  """  
      pass

class ExportExtensionSet_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  null - when no extension set assembly found for the ID, otherwise - instance of the byte[]  """  
      pass

class ExtensionSetExists_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  ID of the extension set  """  
      pass

class ExtensionSetExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true - when extension set is installed, otherwise - false  """  
      pass

class GetByID_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtensionTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtensionTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ExtensionTableset] = obj["returnObj"]
      pass

class GetCompaniesUsingTheExtension_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  The extension set identifier.  """  
      pass

class GetCompaniesUsingTheExtension_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Array of company identifier using the extensionSetID.  """  
      pass

class GetDataSetTables_input:
   """ Required : 
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      pass

class GetDataSetTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtensionDatasetTableListTableset] = obj["returnObj"]
      pass

class GetExtensionSetAssembly_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  ID of the extension set  """  
      pass

class GetExtensionSetAssembly_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Contracts_ExtensionSetAssembly] = obj["returnObj"]
      pass

class GetExtensionSetID_input:
   """ Required : 
   provider
   level
   product
   """  
   def __init__(self, obj):
      self.provider:str = obj["provider"]
      """  provider  """  
      self.level:int = obj["level"]
      """  level  """  
      self.product:str = obj["product"]
      """  product  """  
      pass

class GetExtensionSetID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  the Extension ID  """  
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
      self.returnObj:list[Ice_Tablesets_ExtensionListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMapping_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtensionSetMappingTableset] = obj["returnObj"]
      pass

class GetNewExtensionColumn_input:
   """ Required : 
   ds
   extensionSetID
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      self.extensionSetID:str = obj["extensionSetID"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetNewExtensionColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtensionRelationColumn_input:
   """ Required : 
   ds
   extensionSetID
   systemCode
   dataSetID
   relationID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      self.extensionSetID:str = obj["extensionSetID"]
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      self.relationID:str = obj["relationID"]
      pass

class GetNewExtensionRelationColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtensionRelation_input:
   """ Required : 
   ds
   extensionSetID
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      self.extensionSetID:str = obj["extensionSetID"]
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      pass

class GetNewExtensionRelation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtensionSetMapping_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewExtensionSetMapping_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtensionTableKey_input:
   """ Required : 
   ds
   extensionSetID
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      self.extensionSetID:str = obj["extensionSetID"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetNewExtensionTableKey_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtensionTable_input:
   """ Required : 
   ds
   extensionSetID
   systemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      self.extensionSetID:str = obj["extensionSetID"]
      self.systemCode:str = obj["systemCode"]
      pass

class GetNewExtensionTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtension_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

class GetNewExtension_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtension
   whereClauseExtensionSetMapping
   whereClauseExtensionTable
   whereClauseExtensionColumn
   whereClauseExtensionRelation
   whereClauseExtensionRelationColumn
   whereClauseExtensionTableKey
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtension:str = obj["whereClauseExtension"]
      self.whereClauseExtensionSetMapping:str = obj["whereClauseExtensionSetMapping"]
      self.whereClauseExtensionTable:str = obj["whereClauseExtensionTable"]
      self.whereClauseExtensionColumn:str = obj["whereClauseExtensionColumn"]
      self.whereClauseExtensionRelation:str = obj["whereClauseExtensionRelation"]
      self.whereClauseExtensionRelationColumn:str = obj["whereClauseExtensionRelationColumn"]
      self.whereClauseExtensionTableKey:str = obj["whereClauseExtensionTableKey"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExtensionTableset] = obj["returnObj"]
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

class Ice_Contracts_ExtensionSetAssembly:
   def __init__(self, obj):
      self.Assembly:str = obj["Assembly"]
      self.Symbols:str = obj["Symbols"]
      self.SystemFlag:int = obj["SystemFlag"]
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

class Ice_Tablesets_ExtensionColumnRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SystemCode:str = obj["SystemCode"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Seq:int = obj["Seq"]
      self.Description:str = obj["Description"]
      self.FieldScale:int = obj["FieldScale"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.InitialValue:str = obj["InitialValue"]
      self.Required:bool = obj["Required"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.IsHidden:bool = obj["IsHidden"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      """  Code and Description value list  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionDatasetTableListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionDatasetTableListTableset:
   def __init__(self, obj):
      self.ExtensionDatasetTableList:list[Ice_Tablesets_ExtensionDatasetTableListRow] = obj["ExtensionDatasetTableList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExtensionErrorMessageRow:
   def __init__(self, obj):
      self.Message:str = obj["Message"]
      """  Error message.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionListRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionListTableset:
   def __init__(self, obj):
      self.ExtensionList:list[Ice_Tablesets_ExtensionListRow] = obj["ExtensionList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExtensionRelationColumnRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSetID  """  
      self.RelationID:str = obj["RelationID"]
      """  RelationID  """  
      self.Seq:int = obj["Seq"]
      """  Seq  """  
      self.ParentFieldName:str = obj["ParentFieldName"]
      """  ParentFieldName  """  
      self.ChildFieldName:str = obj["ChildFieldName"]
      """  ChildFieldName  """  
      self.CompOp:str = obj["CompOp"]
      """  CompOp  """  
      self.IsConst:bool = obj["IsConst"]
      """  IsConst  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionRelationRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSetID  """  
      self.RelationID:str = obj["RelationID"]
      """  RelationID  """  
      self.ParentSystemCode:str = obj["ParentSystemCode"]
      """  ParentSystemCode  """  
      self.ParentDataTableID:str = obj["ParentDataTableID"]
      """  ParentDataTableID  """  
      self.ChildSystemCode:str = obj["ChildSystemCode"]
      """  ChildSystemCode  """  
      self.ChildDataTableID:str = obj["ChildDataTableID"]
      """  ChildDataTableID  """  
      self.KeyID:str = obj["KeyID"]
      """  KeyID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.Type:int = obj["Type"]
      """  Type  """  
      self.TreatAsPeer:bool = obj["TreatAsPeer"]
      """  TreatAsPeer  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullParentTableName:str = obj["FullParentTableName"]
      self.FullChildTableName:str = obj["FullChildTableName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.Provider:str = obj["Provider"]
      """  Provider  """  
      self.Product:str = obj["Product"]
      """  Product  """  
      self.Assembly:str = obj["Assembly"]
      """  Assembly  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.Level:int = obj["Level"]
      """  Level  """  
      self.Disabled:bool = obj["Disabled"]
      """  Disabled  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GenIMTable:bool = obj["GenIMTable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionSetMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      """  ExtensionSetID  """  
      self.Order:int = obj["Order"]
      """  Order  """  
      self.Disabled:bool = obj["Disabled"]
      """  Disabled  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionSetMappingTableset:
   def __init__(self, obj):
      self.ExtensionSetMapping:list[Ice_Tablesets_ExtensionSetMappingRow] = obj["ExtensionSetMapping"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExtensionTableKeyRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SystemCode:str = obj["SystemCode"]
      self.Seq:int = obj["Seq"]
      self.FieldName:str = obj["FieldName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionTableRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.Description:str = obj["Description"]
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SystemCode:str = obj["SystemCode"]
      self.DataSetID:str = obj["DataSetID"]
      self.DataSetSystemCode:str = obj["DataSetSystemCode"]
      self.TableType:str = obj["TableType"]
      self.GenIMTable:bool = obj["GenIMTable"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionTableStatusRow:
   def __init__(self, obj):
      self.PrimaryKeyIsNotDefined:bool = obj["PrimaryKeyIsNotDefined"]
      self.TableDoesNotExistInDb:bool = obj["TableDoesNotExistInDb"]
      self.ColumnCountDiffers:bool = obj["ColumnCountDiffers"]
      self.ColumnOrderDiffers:bool = obj["ColumnOrderDiffers"]
      self.DescriptionDiffers:bool = obj["DescriptionDiffers"]
      self.FieldScaleDiffers:bool = obj["FieldScaleDiffers"]
      self.FieldFormatDiffers:bool = obj["FieldFormatDiffers"]
      self.FieldLabelDiffers:bool = obj["FieldLabelDiffers"]
      self.DefaultValueDiffers:bool = obj["DefaultValueDiffers"]
      self.DataTypeDiffers:bool = obj["DataTypeDiffers"]
      self.NullabilityDiffers:bool = obj["NullabilityDiffers"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExtensionTableset:
   def __init__(self, obj):
      self.Extension:list[Ice_Tablesets_ExtensionRow] = obj["Extension"]
      self.ExtensionSetMapping:list[Ice_Tablesets_ExtensionSetMappingRow] = obj["ExtensionSetMapping"]
      self.ExtensionTable:list[Ice_Tablesets_ExtensionTableRow] = obj["ExtensionTable"]
      self.ExtensionColumn:list[Ice_Tablesets_ExtensionColumnRow] = obj["ExtensionColumn"]
      self.ExtensionRelation:list[Ice_Tablesets_ExtensionRelationRow] = obj["ExtensionRelation"]
      self.ExtensionRelationColumn:list[Ice_Tablesets_ExtensionRelationColumnRow] = obj["ExtensionRelationColumn"]
      self.ExtensionTableKey:list[Ice_Tablesets_ExtensionTableKeyRow] = obj["ExtensionTableKey"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExtensionValidationTableset:
   def __init__(self, obj):
      self.ExtensionTableStatus:list[Ice_Tablesets_ExtensionTableStatusRow] = obj["ExtensionTableStatus"]
      self.ExtensionErrorMessage:list[Ice_Tablesets_ExtensionErrorMessageRow] = obj["ExtensionErrorMessage"]
      self.PeerTableStatus:list[Ice_Tablesets_PeerTableStatusRow] = obj["PeerTableStatus"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_PeerTableStatusRow:
   def __init__(self, obj):
      self.Status:int = obj["Status"]
      """  Peer table status - 0 (Unknown), 1 (OK), 2 (Not Found).  """  
      self.StatusMessage:str = obj["StatusMessage"]
      """  The status message.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtExtensionTableset:
   def __init__(self, obj):
      self.Extension:list[Ice_Tablesets_ExtensionRow] = obj["Extension"]
      self.ExtensionSetMapping:list[Ice_Tablesets_ExtensionSetMappingRow] = obj["ExtensionSetMapping"]
      self.ExtensionTable:list[Ice_Tablesets_ExtensionTableRow] = obj["ExtensionTable"]
      self.ExtensionColumn:list[Ice_Tablesets_ExtensionColumnRow] = obj["ExtensionColumn"]
      self.ExtensionRelation:list[Ice_Tablesets_ExtensionRelationRow] = obj["ExtensionRelation"]
      self.ExtensionRelationColumn:list[Ice_Tablesets_ExtensionRelationColumnRow] = obj["ExtensionRelationColumn"]
      self.ExtensionTableKey:list[Ice_Tablesets_ExtensionTableKeyRow] = obj["ExtensionTableKey"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportExtensionSet_input:
   """ Required : 
   extBytes
   """  
   def __init__(self, obj):
      self.extBytes:str = obj["extBytes"]
      """  Byte [] of extension set  """  
      pass

class ImportExtensionSet_output:
   def __init__(self, obj):
      pass

class InstallExtensionSet_input:
   """ Required : 
   assembly
   """  
   def __init__(self, obj):
      self.assembly:list[Ice_Contracts_ExtensionSetAssembly] = obj["assembly"]
      pass

class InstallExtensionSet_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  ID of the installed extension set  """  
      pass

class IsRestrictedSystemCode_input:
   """ Required : 
   systemCode
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System Code  """  
      pass

class IsRestrictedSystemCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true - when SystemCode is Epicor DeliveredSystemCode or dbo, otherwise - false  """  
      pass

class MapExtensionSetToCompany_input:
   """ Required : 
   extensionSetId
   company
   """  
   def __init__(self, obj):
      self.extensionSetId:str = obj["extensionSetId"]
      """  ID of the installed extension set  """  
      self.company:str = obj["company"]
      """  Company ID  """  
      pass

class MapExtensionSetToCompany_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class RemoveExtensionSet_input:
   """ Required : 
   extensionSetID
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  ID of the installed extension set  """  
      pass

class RemoveExtensionSet_output:
   def __init__(self, obj):
      pass

class SetupPeerTable_input:
   """ Required : 
   extensionSetID
   parentDataSetID
   parentSystemCode
   parentTable
   systemCode
   tableName
   """  
   def __init__(self, obj):
      self.extensionSetID:str = obj["extensionSetID"]
      """  ID of the extension set  """  
      self.parentDataSetID:str = obj["parentDataSetID"]
      """  Parent dataset where parent table belong  """  
      self.parentSystemCode:str = obj["parentSystemCode"]
      """  Parent table system code  """  
      self.parentTable:str = obj["parentTable"]
      """  Parent table name  """  
      self.systemCode:str = obj["systemCode"]
      """  Extension table system code  """  
      self.tableName:str = obj["tableName"]
      """  Extension table name  """  
      pass

class SetupPeerTable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true - if changes were made, otherwise - false  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtExtensionTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtExtensionTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExtensionTableset] = obj["ds"]
      pass

      """  output parameters  """  

