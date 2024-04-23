import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DataExportSvc
# Description: Data Export Tool
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DataExports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports",headers=creds) as resp:
           return await resp.json()

async def post_DataExports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID(Company, DefinitionID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExport item
   Description: Calls GetByID to retrieve the DataExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExports_Company_DefinitionID(Company, DefinitionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExport for the service
   Description: Calls UpdateExt to update DataExport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExports_Company_DefinitionID(Company, DefinitionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExport item
   Description: Call UpdateExt to delete DataExport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID_DataExportHistories(Company, DefinitionID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportHistories items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportHistories1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportHistories",headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID_DataExportHistories_Company_DefinitionID_iCounter(Company, DefinitionID, iCounter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportHistory item
   Description: Calls GetByID to retrieve the DataExportHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportHistory1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID_DataExportOptions(Company, DefinitionID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportOptions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportOptions",headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company, DefinitionID, OptionName, TableOption, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportOption item
   Description: Calls GetByID to retrieve the DataExportOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportOption1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param OptionName: Desc: OptionName   Required: True   Allow empty value : True
      :param TableOption: Desc: TableOption   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID_DataExportTables(Company, DefinitionID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportTables1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportTables",headers=creds) as resp:
           return await resp.json()

async def get_DataExports_Company_DefinitionID_DataExportTables_Company_DefinitionID_TableName(Company, DefinitionID, TableName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportTable item
   Description: Calls GetByID to retrieve the DataExportTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTable1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExports(" + Company + "," + DefinitionID + ")/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportHistories(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportHistories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportHistories
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories",headers=creds) as resp:
           return await resp.json()

async def post_DataExportHistories(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportHistories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportHistories_Company_DefinitionID_iCounter(Company, DefinitionID, iCounter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportHistory item
   Description: Calls GetByID to retrieve the DataExportHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportHistories_Company_DefinitionID_iCounter(Company, DefinitionID, iCounter, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportHistory for the service
   Description: Calls UpdateExt to update DataExportHistory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportHistoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportHistories_Company_DefinitionID_iCounter(Company, DefinitionID, iCounter, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportHistory item
   Description: Call UpdateExt to delete DataExportHistory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportHistories(" + Company + "," + DefinitionID + "," + iCounter + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportOptions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportOptions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions",headers=creds) as resp:
           return await resp.json()

async def post_DataExportOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company, DefinitionID, OptionName, TableOption, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportOption item
   Description: Calls GetByID to retrieve the DataExportOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportOption
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param OptionName: Desc: OptionName   Required: True   Allow empty value : True
      :param TableOption: Desc: TableOption   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company, DefinitionID, OptionName, TableOption, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportOption for the service
   Description: Calls UpdateExt to update DataExportOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportOption
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param OptionName: Desc: OptionName   Required: True   Allow empty value : True
      :param TableOption: Desc: TableOption   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportOptionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportOptions_Company_DefinitionID_OptionName_TableOption(Company, DefinitionID, OptionName, TableOption, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportOption item
   Description: Call UpdateExt to delete DataExportOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportOption
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param OptionName: Desc: OptionName   Required: True   Allow empty value : True
      :param TableOption: Desc: TableOption   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportOptions(" + Company + "," + DefinitionID + "," + OptionName + "," + TableOption + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables",headers=creds) as resp:
           return await resp.json()

async def post_DataExportTables(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName(Company, DefinitionID, TableName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportTable item
   Description: Calls GetByID to retrieve the DataExportTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportTables_Company_DefinitionID_TableName(Company, DefinitionID, TableName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportTable for the service
   Description: Calls UpdateExt to update DataExportTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportTables_Company_DefinitionID_TableName(Company, DefinitionID, TableName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportTable item
   Description: Call UpdateExt to delete DataExportTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportTable
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName_DataExportColumns(Company, DefinitionID, TableName, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportColumns1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportColumns",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company, DefinitionID, TableName, ColumnName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportColumn item
   Description: Calls GetByID to retrieve the DataExportColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumn1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName_DataExportTableAttributes(Company, DefinitionID, TableName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportTableAttributes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportTableAttributes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableAttributes",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company, DefinitionID, TableName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportTableAttribute item
   Description: Calls GetByID to retrieve the DataExportTableAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableAttribute1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName_DataExportTableParams(Company, DefinitionID, TableName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportTableParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportTableParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableParams",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTables_Company_DefinitionID_TableName_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company, DefinitionID, TableName, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportTableParam item
   Description: Calls GetByID to retrieve the DataExportTableParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTables(" + Company + "," + DefinitionID + "," + TableName + ")/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumns(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportColumns
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns",headers=creds) as resp:
           return await resp.json()

async def post_DataExportColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company, DefinitionID, TableName, ColumnName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportColumn item
   Description: Calls GetByID to retrieve the DataExportColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company, DefinitionID, TableName, ColumnName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportColumn for the service
   Description: Calls UpdateExt to update DataExportColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportColumns_Company_DefinitionID_TableName_ColumnName(Company, DefinitionID, TableName, ColumnName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportColumn item
   Description: Call UpdateExt to delete DataExportColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnAttributes(Company, DefinitionID, TableName, ColumnName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportColumnAttributes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportColumnAttributes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnAttributes",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company, DefinitionID, TableName, ColumnName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportColumnAttribute item
   Description: Calls GetByID to retrieve the DataExportColumnAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnAttribute1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnLinks(Company, DefinitionID, TableName, ColumnName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataExportColumnLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataExportColumnLinks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnLinks",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumns_Company_DefinitionID_TableName_ColumnName_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company, DefinitionID, TableName, ColumnName, iCounter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportColumnLink item
   Description: Calls GetByID to retrieve the DataExportColumnLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnLink1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumns(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + ")/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumnAttributes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportColumnAttributes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportColumnAttributes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes",headers=creds) as resp:
           return await resp.json()

async def post_DataExportColumnAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportColumnAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company, DefinitionID, TableName, ColumnName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportColumnAttribute item
   Description: Calls GetByID to retrieve the DataExportColumnAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company, DefinitionID, TableName, ColumnName, AttributeName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportColumnAttribute for the service
   Description: Calls UpdateExt to update DataExportColumnAttribute. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportColumnAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportColumnAttributeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportColumnAttributes_Company_DefinitionID_TableName_ColumnName_AttributeName(Company, DefinitionID, TableName, ColumnName, AttributeName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportColumnAttribute item
   Description: Call UpdateExt to delete DataExportColumnAttribute item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportColumnAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumnLinks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportColumnLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportColumnLinks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportColumnLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks",headers=creds) as resp:
           return await resp.json()

async def post_DataExportColumnLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportColumnLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company, DefinitionID, TableName, ColumnName, iCounter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportColumnLink item
   Description: Calls GetByID to retrieve the DataExportColumnLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportColumnLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company, DefinitionID, TableName, ColumnName, iCounter, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportColumnLink for the service
   Description: Calls UpdateExt to update DataExportColumnLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportColumnLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportColumnLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportColumnLinks_Company_DefinitionID_TableName_ColumnName_iCounter(Company, DefinitionID, TableName, ColumnName, iCounter, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportColumnLink item
   Description: Call UpdateExt to delete DataExportColumnLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportColumnLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param iCounter: Desc: iCounter   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportColumnLinks(" + Company + "," + DefinitionID + "," + TableName + "," + ColumnName + "," + iCounter + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTableAttributes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportTableAttributes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportTableAttributes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes",headers=creds) as resp:
           return await resp.json()

async def post_DataExportTableAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportTableAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company, DefinitionID, TableName, AttributeName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportTableAttribute item
   Description: Calls GetByID to retrieve the DataExportTableAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company, DefinitionID, TableName, AttributeName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportTableAttribute for the service
   Description: Calls UpdateExt to update DataExportTableAttribute. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportTableAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportTableAttributeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportTableAttributes_Company_DefinitionID_TableName_AttributeName(Company, DefinitionID, TableName, AttributeName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportTableAttribute item
   Description: Call UpdateExt to delete DataExportTableAttribute item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportTableAttribute
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param AttributeName: Desc: AttributeName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableAttributes(" + Company + "," + DefinitionID + "," + TableName + "," + AttributeName + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataExportTableParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataExportTableParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataExportTableParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportTableParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams",headers=creds) as resp:
           return await resp.json()

async def post_DataExportTableParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataExportTableParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company, DefinitionID, TableName, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataExportTableParam item
   Description: Calls GetByID to retrieve the DataExportTableParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataExportTableParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company, DefinitionID, TableName, ParamName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataExportTableParam for the service
   Description: Calls UpdateExt to update DataExportTableParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataExportTableParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataExportTableParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataExportTableParams_Company_DefinitionID_TableName_ParamName(Company, DefinitionID, TableName, ParamName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataExportTableParam item
   Description: Call UpdateExt to delete DataExportTableParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataExportTableParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/DataExportTableParams(" + Company + "," + DefinitionID + "," + TableName + "," + ParamName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataExportDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDataExportDef, whereClauseDataExportHistory, whereClauseDataExportOption, whereClauseDataExportTable, whereClauseDataExportColumn, whereClauseDataExportColumnAttribute, whereClauseDataExportColumnLink, whereClauseDataExportTableAttribute, whereClauseDataExportTableParam, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDataExportDef=" + whereClauseDataExportDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportHistory=" + whereClauseDataExportHistory
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportOption=" + whereClauseDataExportOption
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportTable=" + whereClauseDataExportTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportColumn=" + whereClauseDataExportColumn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportColumnAttribute=" + whereClauseDataExportColumnAttribute
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportColumnLink=" + whereClauseDataExportColumnLink
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportTableAttribute=" + whereClauseDataExportTableAttribute
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataExportTableParam=" + whereClauseDataExportTableParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(definitionID, epicorHeaders = None):
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
   params += "definitionID=" + definitionID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateDefinition
   OperationID: DuplicateDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportDefinition
   OperationID: ExportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportDefinition
   OperationID: ImportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Generate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Generate
   OperationID: Generate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Generate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateToServerFolder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateToServerFolder
   OperationID: GenerateToServerFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateToServerFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateToServerFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDateFormats(epicorHeaders = None):
   """  
   Summary: Invoke method GetDateFormats
   Description: This method returns a list of date formats
   OperationID: GetDateFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateFormats_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldList
   Description: This method returns a list of Fields
   OperationID: GetFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableList
   Description: This method returns a list of Tables
   OperationID: GetTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetForeignTblFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetForeignTblFieldList
   Description: This method returns a list of Foreign Fields excluding already used for links
   OperationID: GetForeignTblFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetForeignTblFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForeignTblFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOwnTblFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOwnTblFieldList
   Description: This method returns a list of Own Fields excluding already used for links
   OperationID: GetOwnTblFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOwnTblFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOwnTblFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetForeignTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetForeignTableList
   Description: This method returns a list of Foreign Key Tables
   OperationID: GetForeignTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetForeignTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForeignTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTablesListWithWrongSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTablesListWithWrongSource
   Description: Get the list of tables, for which data source do not exist.
   OperationID: GetTablesListWithWrongSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTablesListWithWrongSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesListWithWrongSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsPostingsExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsPostingsExist
   Description: Check that postings exist in specified period.
   OperationID: IsPostingsExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsPostingsExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPostingsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGLBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGLBook
   Description: Call method when the over rides the check # in Process Payment.
   OperationID: OnChangeGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnRetrieveColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnRetrieveColumns
   OperationID: OnRetrieveColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnRetrieveColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnRetrieveColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshDataExportDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshDataExportDef
   Description: This method will refresh data in tableset for DataExportDef table.
<param name="ds" type="Erp.Tablesets.DataExportDataSet">Erp.Tablesets.DataExportDataSet</param>
   OperationID: RefreshDataExportDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshDataExportDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshDataExportDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetGDPdUMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetGDPdUMode
   Description: <param name="ds" type="Erp.Tablesets.DataExportDataSet">Erp.Tablesets.DataExportDataSet</param>
   OperationID: SetGDPdUMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGDPdUMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGDPdUMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StoreData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StoreData
   Description: This method will require that all dataset records have a value of 'A' in the corresponding
rowident field/column.
<param name="ipDefinitionID">Definition ID</param><param name="ds" type="Erp.Tablesets.DataExportDataSet">Erp.Tablesets.DataExportDataSet</param>
   OperationID: StoreData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StoreData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StoreData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportHistory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportOption
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportColumnAttribute(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportColumnAttribute
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportColumnAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportColumnAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportColumnAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportColumnLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportColumnLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportColumnLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportColumnLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportColumnLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportTableAttribute(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportTableAttribute
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportTableAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportTableAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportTableAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDataExportTableParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDataExportTableParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDataExportTableParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDataExportTableParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDataExportTableParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnAttributeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportColumnAttributeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnLinkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportColumnLinkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportColumnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportHistoryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportHistoryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportOptionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportOptionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableAttributeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportTableAttributeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportTableParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataExportTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataExportTableRow] = obj["value"]
      pass

class Erp_Tablesets_DataExportColumnAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.AttributeName:str = obj["AttributeName"]
      """  AttributeName  """  
      self.AttributeValue:str = obj["AttributeValue"]
      """  AttributeValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportColumnLinkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.iCounter:int = obj["iCounter"]
      """  iCounter  """  
      self.TblColumnName:str = obj["TblColumnName"]
      """  TblColumnName  """  
      self.ForeignTblColumnName:str = obj["ForeignTblColumnName"]
      """  ForeignTblColumnName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ColumnType:str = obj["ColumnType"]
      """  ColumnType  """  
      self.Accuracy:int = obj["Accuracy"]
      """  Accuracy  """  
      self.IsVarPrimaryKey:bool = obj["IsVarPrimaryKey"]
      """  IsVarPrimaryKey  """  
      self.IsForeignKey:bool = obj["IsForeignKey"]
      """  IsForeignKey  """  
      self.ForeignKeyTableName:str = obj["ForeignKeyTableName"]
      """  ForeignKeyTableName  """  
      self.ForeignKeyColumnName:str = obj["ForeignKeyColumnName"]
      """  ForeignKeyColumnName  """  
      self.ColumnOrder:int = obj["ColumnOrder"]
      """  ColumnOrder  """  
      self.FooterSType:str = obj["FooterSType"]
      """  FooterSType  """  
      self.FooterSOrder:int = obj["FooterSOrder"]
      """  FooterSOrder  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.FooterSNode:str = obj["FooterSNode"]
      """  FooterSNode  """  
      self.IsHidden:bool = obj["IsHidden"]
      """  IsHidden  """  
      self.DisplayName:str = obj["DisplayName"]
      """  DisplayName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SelectionMethod:str = obj["SelectionMethod"]
      """  SelectionMethod  """  
      self.ExportFolder:str = obj["ExportFolder"]
      """  ExportFolder  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.DecimalSeparator:str = obj["DecimalSeparator"]
      """  DecimalSeparator  """  
      self.ThousandSeparator:str = obj["ThousandSeparator"]
      """  ThousandSeparator  """  
      self.IsReleased:bool = obj["IsReleased"]
      """  IsReleased  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.StartDateToken:str = obj["StartDateToken"]
      """  StartDateToken  """  
      self.StartPeriod:int = obj["StartPeriod"]
      """  StartPeriod  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.EndDateToken:str = obj["EndDateToken"]
      """  EndDateToken  """  
      self.EndPeriod:int = obj["EndPeriod"]
      """  EndPeriod  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  LastRunDate  """  
      self.LastRunBy:str = obj["LastRunBy"]
      """  LastRunBy  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  UpdatedDate  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  UpdatedBy  """  
      self.URLforDTD:str = obj["URLforDTD"]
      """  URLforDTD  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  IsUsed  """  
      self.GenerateIndex:bool = obj["GenerateIndex"]
      """  GenerateIndex  """  
      self.CommonFileName:str = obj["CommonFileName"]
      """  CommonFileName  """  
      self.RootNodeName:str = obj["RootNodeName"]
      """  RootNodeName  """  
      self.DSymbol:str = obj["DSymbol"]
      """  DSymbol  """  
      self.LESymbol:str = obj["LESymbol"]
      """  LESymbol  """  
      self.QSymbol:str = obj["QSymbol"]
      """  QSymbol  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.IsCommonFile:bool = obj["IsCommonFile"]
      """  IsCommonFile  """  
      self.AddRecordType:bool = obj["AddRecordType"]
      """  AddRecordType  """  
      self.AddCommonFooter:bool = obj["AddCommonFooter"]
      """  AddCommonFooter  """  
      self.CommonFooter:str = obj["CommonFooter"]
      """  CommonFooter  """  
      self.Encoding:int = obj["Encoding"]
      """  Encoding  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SelectionMethod:str = obj["SelectionMethod"]
      """  SelectionMethod  """  
      self.ExportFolder:str = obj["ExportFolder"]
      """  ExportFolder  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.DecimalSeparator:str = obj["DecimalSeparator"]
      """  DecimalSeparator  """  
      self.ThousandSeparator:str = obj["ThousandSeparator"]
      """  ThousandSeparator  """  
      self.IsReleased:bool = obj["IsReleased"]
      """  IsReleased  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.StartDateToken:str = obj["StartDateToken"]
      """  StartDateToken  """  
      self.StartPeriod:int = obj["StartPeriod"]
      """  StartPeriod  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.EndDateToken:str = obj["EndDateToken"]
      """  EndDateToken  """  
      self.EndPeriod:int = obj["EndPeriod"]
      """  EndPeriod  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  LastRunDate  """  
      self.LastRunBy:str = obj["LastRunBy"]
      """  LastRunBy  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  UpdatedDate  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  UpdatedBy  """  
      self.URLforDTD:str = obj["URLforDTD"]
      """  URLforDTD  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  IsUsed  """  
      self.GenerateIndex:bool = obj["GenerateIndex"]
      """  GenerateIndex  """  
      self.CommonFileName:str = obj["CommonFileName"]
      """  CommonFileName  """  
      self.RootNodeName:str = obj["RootNodeName"]
      """  RootNodeName  """  
      self.DSymbol:str = obj["DSymbol"]
      """  DSymbol  """  
      self.LESymbol:str = obj["LESymbol"]
      """  LESymbol  """  
      self.QSymbol:str = obj["QSymbol"]
      """  QSymbol  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.IsCommonFile:bool = obj["IsCommonFile"]
      """  IsCommonFile  """  
      self.AddRecordType:bool = obj["AddRecordType"]
      """  AddRecordType  """  
      self.AddCommonFooter:bool = obj["AddCommonFooter"]
      """  AddCommonFooter  """  
      self.CommonFooter:str = obj["CommonFooter"]
      """  CommonFooter  """  
      self.Encoding:int = obj["Encoding"]
      """  Encoding  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportHistoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.iCounter:int = obj["iCounter"]
      """  iCounter  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.ActionDate:str = obj["ActionDate"]
      """  ActionDate  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportOptionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.OptionName:str = obj["OptionName"]
      """  OptionName  """  
      self.TableOption:str = obj["TableOption"]
      """  TableOption  """  
      self.OptionType:str = obj["OptionType"]
      """  OptionType  """  
      self.DefaultOption:bool = obj["DefaultOption"]
      """  DefaultOption  """  
      self.IntegerCol:int = obj["IntegerCol"]
      """  IntegerCol  """  
      self.DecimalCol:int = obj["DecimalCol"]
      """  DecimalCol  """  
      self.LogicalCol:bool = obj["LogicalCol"]
      """  LogicalCol  """  
      self.StringCol:str = obj["StringCol"]
      """  StringCol  """  
      self.DateCol:str = obj["DateCol"]
      """  DateCol  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.AttributeName:str = obj["AttributeName"]
      """  AttributeName  """  
      self.AttributeValue:str = obj["AttributeValue"]
      """  AttributeValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ParamName:str = obj["ParamName"]
      """  ParamName  """  
      self.ParamType:str = obj["ParamType"]
      """  ParamType  """  
      self.ReportParameter:str = obj["ReportParameter"]
      """  ReportParameter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.FileName:str = obj["FileName"]
      """  FileName  """  
      self.GenerateMethod:str = obj["GenerateMethod"]
      """  GenerateMethod  """  
      self.DataSource:str = obj["DataSource"]
      """  DataSource  """  
      self.DataSourceID:str = obj["DataSourceID"]
      """  DataSourceID  """  
      self.ExportFileType:str = obj["ExportFileType"]
      """  ExportFileType  """  
      self.IncludeHeader:bool = obj["IncludeHeader"]
      """  IncludeHeader  """  
      self.DSymbol:str = obj["DSymbol"]
      """  DSymbol  """  
      self.ExportMethod:str = obj["ExportMethod"]
      """  ExportMethod  """  
      self.TableOrder:int = obj["TableOrder"]
      """  TableOrder  """  
      self.AddHeader:str = obj["AddHeader"]
      """  AddHeader  """  
      self.AddFooter:str = obj["AddFooter"]
      """  AddFooter  """  
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
   definitionID
   """  
   def __init__(self, obj):
      self.definitionID:str = obj["definitionID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateDefinition_input:
   """ Required : 
   ipGDPdUMode
   ipSourceDefinitionID
   ipTargetDefinitionID
   """  
   def __init__(self, obj):
      self.ipGDPdUMode:bool = obj["ipGDPdUMode"]
      """  GDPdU Mode  """  
      self.ipSourceDefinitionID:str = obj["ipSourceDefinitionID"]
      """  Source Definition ID  """  
      self.ipTargetDefinitionID:str = obj["ipTargetDefinitionID"]
      """  Target (new) Definition ID  """  
      pass

class DuplicateDefinition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DataExportColumnAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.AttributeName:str = obj["AttributeName"]
      """  AttributeName  """  
      self.AttributeValue:str = obj["AttributeValue"]
      """  AttributeValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportColumnLinkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.iCounter:int = obj["iCounter"]
      """  iCounter  """  
      self.TblColumnName:str = obj["TblColumnName"]
      """  TblColumnName  """  
      self.ForeignTblColumnName:str = obj["ForeignTblColumnName"]
      """  ForeignTblColumnName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ColumnType:str = obj["ColumnType"]
      """  ColumnType  """  
      self.Accuracy:int = obj["Accuracy"]
      """  Accuracy  """  
      self.IsVarPrimaryKey:bool = obj["IsVarPrimaryKey"]
      """  IsVarPrimaryKey  """  
      self.IsForeignKey:bool = obj["IsForeignKey"]
      """  IsForeignKey  """  
      self.ForeignKeyTableName:str = obj["ForeignKeyTableName"]
      """  ForeignKeyTableName  """  
      self.ForeignKeyColumnName:str = obj["ForeignKeyColumnName"]
      """  ForeignKeyColumnName  """  
      self.ColumnOrder:int = obj["ColumnOrder"]
      """  ColumnOrder  """  
      self.FooterSType:str = obj["FooterSType"]
      """  FooterSType  """  
      self.FooterSOrder:int = obj["FooterSOrder"]
      """  FooterSOrder  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.FooterSNode:str = obj["FooterSNode"]
      """  FooterSNode  """  
      self.IsHidden:bool = obj["IsHidden"]
      """  IsHidden  """  
      self.DisplayName:str = obj["DisplayName"]
      """  DisplayName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SelectionMethod:str = obj["SelectionMethod"]
      """  SelectionMethod  """  
      self.ExportFolder:str = obj["ExportFolder"]
      """  ExportFolder  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.DecimalSeparator:str = obj["DecimalSeparator"]
      """  DecimalSeparator  """  
      self.ThousandSeparator:str = obj["ThousandSeparator"]
      """  ThousandSeparator  """  
      self.IsReleased:bool = obj["IsReleased"]
      """  IsReleased  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.StartDateToken:str = obj["StartDateToken"]
      """  StartDateToken  """  
      self.StartPeriod:int = obj["StartPeriod"]
      """  StartPeriod  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.EndDateToken:str = obj["EndDateToken"]
      """  EndDateToken  """  
      self.EndPeriod:int = obj["EndPeriod"]
      """  EndPeriod  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  LastRunDate  """  
      self.LastRunBy:str = obj["LastRunBy"]
      """  LastRunBy  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  UpdatedDate  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  UpdatedBy  """  
      self.URLforDTD:str = obj["URLforDTD"]
      """  URLforDTD  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  IsUsed  """  
      self.GenerateIndex:bool = obj["GenerateIndex"]
      """  GenerateIndex  """  
      self.CommonFileName:str = obj["CommonFileName"]
      """  CommonFileName  """  
      self.RootNodeName:str = obj["RootNodeName"]
      """  RootNodeName  """  
      self.DSymbol:str = obj["DSymbol"]
      """  DSymbol  """  
      self.LESymbol:str = obj["LESymbol"]
      """  LESymbol  """  
      self.QSymbol:str = obj["QSymbol"]
      """  QSymbol  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.IsCommonFile:bool = obj["IsCommonFile"]
      """  IsCommonFile  """  
      self.AddRecordType:bool = obj["AddRecordType"]
      """  AddRecordType  """  
      self.AddCommonFooter:bool = obj["AddCommonFooter"]
      """  AddCommonFooter  """  
      self.CommonFooter:str = obj["CommonFooter"]
      """  CommonFooter  """  
      self.Encoding:int = obj["Encoding"]
      """  Encoding  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SelectionMethod:str = obj["SelectionMethod"]
      """  SelectionMethod  """  
      self.ExportFolder:str = obj["ExportFolder"]
      """  ExportFolder  """  
      self.DateFormat:str = obj["DateFormat"]
      """  DateFormat  """  
      self.DecimalSeparator:str = obj["DecimalSeparator"]
      """  DecimalSeparator  """  
      self.ThousandSeparator:str = obj["ThousandSeparator"]
      """  ThousandSeparator  """  
      self.IsReleased:bool = obj["IsReleased"]
      """  IsReleased  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.StartDateToken:str = obj["StartDateToken"]
      """  StartDateToken  """  
      self.StartPeriod:int = obj["StartPeriod"]
      """  StartPeriod  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.EndDateToken:str = obj["EndDateToken"]
      """  EndDateToken  """  
      self.EndPeriod:int = obj["EndPeriod"]
      """  EndPeriod  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  LastRunDate  """  
      self.LastRunBy:str = obj["LastRunBy"]
      """  LastRunBy  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  UpdatedDate  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  UpdatedBy  """  
      self.URLforDTD:str = obj["URLforDTD"]
      """  URLforDTD  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  IsUsed  """  
      self.GenerateIndex:bool = obj["GenerateIndex"]
      """  GenerateIndex  """  
      self.CommonFileName:str = obj["CommonFileName"]
      """  CommonFileName  """  
      self.RootNodeName:str = obj["RootNodeName"]
      """  RootNodeName  """  
      self.DSymbol:str = obj["DSymbol"]
      """  DSymbol  """  
      self.LESymbol:str = obj["LESymbol"]
      """  LESymbol  """  
      self.QSymbol:str = obj["QSymbol"]
      """  QSymbol  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.IsCommonFile:bool = obj["IsCommonFile"]
      """  IsCommonFile  """  
      self.AddRecordType:bool = obj["AddRecordType"]
      """  AddRecordType  """  
      self.AddCommonFooter:bool = obj["AddCommonFooter"]
      """  AddCommonFooter  """  
      self.CommonFooter:str = obj["CommonFooter"]
      """  CommonFooter  """  
      self.Encoding:int = obj["Encoding"]
      """  Encoding  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportHistoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.iCounter:int = obj["iCounter"]
      """  iCounter  """  
      self.Action:str = obj["Action"]
      """  Action  """  
      self.ActionDate:str = obj["ActionDate"]
      """  ActionDate  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportListTableset:
   def __init__(self, obj):
      self.DataExportDefList:list[Erp_Tablesets_DataExportDefListRow] = obj["DataExportDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DataExportOptionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.OptionName:str = obj["OptionName"]
      """  OptionName  """  
      self.TableOption:str = obj["TableOption"]
      """  TableOption  """  
      self.OptionType:str = obj["OptionType"]
      """  OptionType  """  
      self.DefaultOption:bool = obj["DefaultOption"]
      """  DefaultOption  """  
      self.IntegerCol:int = obj["IntegerCol"]
      """  IntegerCol  """  
      self.DecimalCol:int = obj["DecimalCol"]
      """  DecimalCol  """  
      self.LogicalCol:bool = obj["LogicalCol"]
      """  LogicalCol  """  
      self.StringCol:str = obj["StringCol"]
      """  StringCol  """  
      self.DateCol:str = obj["DateCol"]
      """  DateCol  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.AttributeName:str = obj["AttributeName"]
      """  AttributeName  """  
      self.AttributeValue:str = obj["AttributeValue"]
      """  AttributeValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.ParamName:str = obj["ParamName"]
      """  ParamName  """  
      self.ParamType:str = obj["ParamType"]
      """  ParamType  """  
      self.ReportParameter:str = obj["ReportParameter"]
      """  ReportParameter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.FileName:str = obj["FileName"]
      """  FileName  """  
      self.GenerateMethod:str = obj["GenerateMethod"]
      """  GenerateMethod  """  
      self.DataSource:str = obj["DataSource"]
      """  DataSource  """  
      self.DataSourceID:str = obj["DataSourceID"]
      """  DataSourceID  """  
      self.ExportFileType:str = obj["ExportFileType"]
      """  ExportFileType  """  
      self.IncludeHeader:bool = obj["IncludeHeader"]
      """  IncludeHeader  """  
      self.DSymbol:str = obj["DSymbol"]
      """  DSymbol  """  
      self.ExportMethod:str = obj["ExportMethod"]
      """  ExportMethod  """  
      self.TableOrder:int = obj["TableOrder"]
      """  TableOrder  """  
      self.AddHeader:str = obj["AddHeader"]
      """  AddHeader  """  
      self.AddFooter:str = obj["AddFooter"]
      """  AddFooter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataExportTableset:
   def __init__(self, obj):
      self.DataExportDef:list[Erp_Tablesets_DataExportDefRow] = obj["DataExportDef"]
      self.DataExportHistory:list[Erp_Tablesets_DataExportHistoryRow] = obj["DataExportHistory"]
      self.DataExportOption:list[Erp_Tablesets_DataExportOptionRow] = obj["DataExportOption"]
      self.DataExportTable:list[Erp_Tablesets_DataExportTableRow] = obj["DataExportTable"]
      self.DataExportColumn:list[Erp_Tablesets_DataExportColumnRow] = obj["DataExportColumn"]
      self.DataExportColumnAttribute:list[Erp_Tablesets_DataExportColumnAttributeRow] = obj["DataExportColumnAttribute"]
      self.DataExportColumnLink:list[Erp_Tablesets_DataExportColumnLinkRow] = obj["DataExportColumnLink"]
      self.DataExportTableAttribute:list[Erp_Tablesets_DataExportTableAttributeRow] = obj["DataExportTableAttribute"]
      self.DataExportTableParam:list[Erp_Tablesets_DataExportTableParamRow] = obj["DataExportTableParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDataExportTableset:
   def __init__(self, obj):
      self.DataExportDef:list[Erp_Tablesets_DataExportDefRow] = obj["DataExportDef"]
      self.DataExportHistory:list[Erp_Tablesets_DataExportHistoryRow] = obj["DataExportHistory"]
      self.DataExportOption:list[Erp_Tablesets_DataExportOptionRow] = obj["DataExportOption"]
      self.DataExportTable:list[Erp_Tablesets_DataExportTableRow] = obj["DataExportTable"]
      self.DataExportColumn:list[Erp_Tablesets_DataExportColumnRow] = obj["DataExportColumn"]
      self.DataExportColumnAttribute:list[Erp_Tablesets_DataExportColumnAttributeRow] = obj["DataExportColumnAttribute"]
      self.DataExportColumnLink:list[Erp_Tablesets_DataExportColumnLinkRow] = obj["DataExportColumnLink"]
      self.DataExportTableAttribute:list[Erp_Tablesets_DataExportTableAttributeRow] = obj["DataExportTableAttribute"]
      self.DataExportTableParam:list[Erp_Tablesets_DataExportTableParamRow] = obj["DataExportTableParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportDefinition_input:
   """ Required : 
   ipDefinitionID
   ipExportFile
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipExportFile:str = obj["ipExportFile"]
      """  Export Filename, entered by user  """  
      pass

class ExportDefinition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opExportFile:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateToServerFolder_input:
   """ Required : 
   ipGDPdUMode
   ipDefinitionID
   ipTestMode
   ipDTDFile
   ds
   """  
   def __init__(self, obj):
      self.ipGDPdUMode:bool = obj["ipGDPdUMode"]
      """  GDPdU Mode  """  
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipTestMode:bool = obj["ipTestMode"]
      """  Test mode  """  
      self.ipDTDFile:str = obj["ipDTDFile"]
      """  Path to DTD file on server  """  
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class GenerateToServerFolder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opErrMessage:str = obj["parameters"]
      self.opFilesQty:int = obj["parameters"]
      self.opExportSubFolder:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Generate_input:
   """ Required : 
   ipGDPdUMode
   ipDefinitionID
   ipTestMode
   ds
   """  
   def __init__(self, obj):
      self.ipGDPdUMode:bool = obj["ipGDPdUMode"]
      """  GDPdU Mode  """  
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipTestMode:bool = obj["ipTestMode"]
      """  Test mode  """  
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class Generate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opErrMessage:str = obj["parameters"]
      self.opFilesQty:int = obj["parameters"]
      self.opFilesForExport:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   definitionID
   """  
   def __init__(self, obj):
      self.definitionID:str = obj["definitionID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataExportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DataExportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DataExportTableset] = obj["returnObj"]
      pass

class GetDateFormats_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDateFormats:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFieldList_input:
   """ Required : 
   ipDefinitionID
   ipcurrentTable
   ipcurrentColumn
   ipDataType
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipcurrentTable:str = obj["ipcurrentTable"]
      """  current Table  """  
      self.ipcurrentColumn:str = obj["ipcurrentColumn"]
      """  current Column  """  
      self.ipDataType:str = obj["ipDataType"]
      """  column Type  """  
      pass

class GetFieldList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFieldList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetForeignTableList_input:
   """ Required : 
   ipDefinitionID
   ipcurrentTable
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipcurrentTable:str = obj["ipcurrentTable"]
      """  Current Table  """  
      pass

class GetForeignTableList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTableList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetForeignTblFieldList_input:
   """ Required : 
   ipDefinitionID
   ipcurrentTable
   ipcurrentColumn
   ipcurrentForeignTblColumnName
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipcurrentTable:str = obj["ipcurrentTable"]
      """  current Table  """  
      self.ipcurrentColumn:str = obj["ipcurrentColumn"]
      """  current Column  """  
      self.ipcurrentForeignTblColumnName:str = obj["ipcurrentForeignTblColumnName"]
      """  foreign Table column  """  
      pass

class GetForeignTblFieldList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFieldList:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_DataExportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDataExportColumnAttribute_input:
   """ Required : 
   ds
   definitionID
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class GetNewDataExportColumnAttribute_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportColumnLink_input:
   """ Required : 
   ds
   definitionID
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class GetNewDataExportColumnLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportColumn_input:
   """ Required : 
   ds
   definitionID
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewDataExportColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class GetNewDataExportDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportHistory_input:
   """ Required : 
   ds
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewDataExportHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportOption_input:
   """ Required : 
   ds
   definitionID
   optionName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.optionName:str = obj["optionName"]
      pass

class GetNewDataExportOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportTableAttribute_input:
   """ Required : 
   ds
   definitionID
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewDataExportTableAttribute_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportTableParam_input:
   """ Required : 
   ds
   definitionID
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewDataExportTableParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDataExportTable_input:
   """ Required : 
   ds
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewDataExportTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOwnTblFieldList_input:
   """ Required : 
   ipDefinitionID
   ipcurrentTable
   ipcurrentColumn
   ipcurrentOwnColumn
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipcurrentTable:str = obj["ipcurrentTable"]
      """  current Table  """  
      self.ipcurrentColumn:str = obj["ipcurrentColumn"]
      """  current Column  """  
      self.ipcurrentOwnColumn:str = obj["ipcurrentOwnColumn"]
      """  current Own Column  """  
      pass

class GetOwnTblFieldList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFieldList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDataExportDef
   whereClauseDataExportHistory
   whereClauseDataExportOption
   whereClauseDataExportTable
   whereClauseDataExportColumn
   whereClauseDataExportColumnAttribute
   whereClauseDataExportColumnLink
   whereClauseDataExportTableAttribute
   whereClauseDataExportTableParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDataExportDef:str = obj["whereClauseDataExportDef"]
      self.whereClauseDataExportHistory:str = obj["whereClauseDataExportHistory"]
      self.whereClauseDataExportOption:str = obj["whereClauseDataExportOption"]
      self.whereClauseDataExportTable:str = obj["whereClauseDataExportTable"]
      self.whereClauseDataExportColumn:str = obj["whereClauseDataExportColumn"]
      self.whereClauseDataExportColumnAttribute:str = obj["whereClauseDataExportColumnAttribute"]
      self.whereClauseDataExportColumnLink:str = obj["whereClauseDataExportColumnLink"]
      self.whereClauseDataExportTableAttribute:str = obj["whereClauseDataExportTableAttribute"]
      self.whereClauseDataExportTableParam:str = obj["whereClauseDataExportTableParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataExportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTableList_input:
   """ Required : 
   ipDefinitionID
   ipcurrentTable
   ipcurrentColumn
   ipDataType
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipcurrentTable:str = obj["ipcurrentTable"]
      """  Current Table  """  
      self.ipcurrentColumn:str = obj["ipcurrentColumn"]
      """  Current Column  """  
      self.ipDataType:str = obj["ipDataType"]
      """  Column Type  """  
      pass

class GetTableList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTableList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTablesListWithWrongSource_input:
   """ Required : 
   ipDefinitionID
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition  """  
      pass

class GetTablesListWithWrongSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTablesList:str = obj["parameters"]
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

class ImportDefinition_input:
   """ Required : 
   ipGDPdUMode
   ipImportFile
   ipNewDefinitionID
   ipCheckDefinitionExistance
   """  
   def __init__(self, obj):
      self.ipGDPdUMode:bool = obj["ipGDPdUMode"]
      """  GDPdU Mode  """  
      self.ipImportFile:str = obj["ipImportFile"]
      """  Data Definition template file  """  
      self.ipNewDefinitionID:str = obj["ipNewDefinitionID"]
      """  New Definition ID, entered by user  """  
      self.ipCheckDefinitionExistance:bool = obj["ipCheckDefinitionExistance"]
      """  Check whether new definition id alredy exists in db  """  
      pass

class ImportDefinition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opNewDefinitionID:str = obj["parameters"]
      pass

      """  output parameters  """  

class IsPostingsExist_input:
   """ Required : 
   ipGLBook
   ipFiscalYear
   ipStartPeriod
   ipEndPeriod
   """  
   def __init__(self, obj):
      self.ipGLBook:str = obj["ipGLBook"]
      """  Fiscal Year  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Start period  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  End period  """  
      pass

class IsPostingsExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opResult:bool = obj["opResult"]
      pass

      """  output parameters  """  

class OnChangeGLBook_input:
   """ Required : 
   ipGLBook
   ipFiscalYear
   ipStartPeriod
   ipEndPeriod
   ds
   """  
   def __init__(self, obj):
      self.ipGLBook:str = obj["ipGLBook"]
      """  Fiscal Year  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Start period  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  End period  """  
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class OnChangeGLBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnRetrieveColumns_input:
   """ Required : 
   ipDefinitionID
   ipGenMethod
   ipTableName
   ipDataSourceID
   ds
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  Definition ID  """  
      self.ipGenMethod:str = obj["ipGenMethod"]
      """  Generation method  """  
      self.ipTableName:str = obj["ipTableName"]
      """  Table Name  """  
      self.ipDataSourceID:str = obj["ipDataSourceID"]
      """  Data Source ID  """  
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class OnRetrieveColumns_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshDataExportDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class RefreshDataExportDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetGDPdUMode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class SetGDPdUMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StoreData_input:
   """ Required : 
   ipDefinitionID
   ds
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class StoreData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDataExportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDataExportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

