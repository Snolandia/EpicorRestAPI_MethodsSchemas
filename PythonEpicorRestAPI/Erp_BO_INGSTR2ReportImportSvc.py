import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.INGSTR2ReportImportSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2ReportImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2ReportImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR2ReportImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2ReportImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportImports_Company_ReportID(Company, ReportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2ReportImport item
   Description: Calls GetByID to retrieve the INGSTR2ReportImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR2ReportImports_Company_ReportID(Company, ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR2ReportImport for the service
   Description: Calls UpdateExt to update INGSTR2ReportImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2ReportImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR2ReportImports_Company_ReportID(Company, ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR2ReportImport item
   Description: Call UpdateExt to delete INGSTR2ReportImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2ReportImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportImports_Company_ReportID_INGSTR2MatchedLines(Company, ReportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get INGSTR2MatchedLines items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_INGSTR2MatchedLines1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2MatchedLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2MatchedLines",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportImports_Company_ReportID_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company, ReportID, Section, TransactionType, ExternalSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2MatchedLine item
   Description: Calls GetByID to retrieve the INGSTR2MatchedLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2MatchedLine1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Section: Desc: Section   Required: True   Allow empty value : True
      :param TransactionType: Desc: TransactionType   Required: True
      :param ExternalSysRowID: Desc: ExternalSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportImports_Company_ReportID_INGSTR2ReportAttchs(Company, ReportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get INGSTR2ReportAttchs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_INGSTR2ReportAttchs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2ReportAttchs",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportImports_Company_ReportID_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company, ReportID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2ReportAttch item
   Description: Calls GetByID to retrieve the INGSTR2ReportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2MatchedLines(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2MatchedLines items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2MatchedLines
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2MatchedLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR2MatchedLines(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2MatchedLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company, ReportID, Section, TransactionType, ExternalSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2MatchedLine item
   Description: Calls GetByID to retrieve the INGSTR2MatchedLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2MatchedLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Section: Desc: Section   Required: True   Allow empty value : True
      :param TransactionType: Desc: TransactionType   Required: True
      :param ExternalSysRowID: Desc: ExternalSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company, ReportID, Section, TransactionType, ExternalSysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR2MatchedLine for the service
   Description: Calls UpdateExt to update INGSTR2MatchedLine. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2MatchedLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Section: Desc: Section   Required: True   Allow empty value : True
      :param TransactionType: Desc: TransactionType   Required: True
      :param ExternalSysRowID: Desc: ExternalSysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company, ReportID, Section, TransactionType, ExternalSysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR2MatchedLine item
   Description: Call UpdateExt to delete INGSTR2MatchedLine item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2MatchedLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Section: Desc: Section   Required: True   Allow empty value : True
      :param TransactionType: Desc: TransactionType   Required: True
      :param ExternalSysRowID: Desc: ExternalSysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportAttchs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2ReportAttchs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2ReportAttchs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR2ReportAttchs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2ReportAttchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company, ReportID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2ReportAttch item
   Description: Calls GetByID to retrieve the INGSTR2ReportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company, ReportID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR2ReportAttch for the service
   Description: Calls UpdateExt to update INGSTR2ReportAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2ReportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company, ReportID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR2ReportAttch item
   Description: Call UpdateExt to delete INGSTR2ReportAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2ReportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR23s(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR23s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR23s
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR23Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR23s(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR23s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR23Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR23Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR23s_Company_LocalName_Key1_Key2_Key3_Key4(Company, LocalName, Key1, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR23 item
   Description: Calls GetByID to retrieve the INGSTR23 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR23
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR23Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR23s_Company_LocalName_Key1_Key2_Key3_Key4(Company, LocalName, Key1, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR23 for the service
   Description: Calls UpdateExt to update INGSTR23. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR23
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR23Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR23s_Company_LocalName_Key1_Key2_Key3_Key4(Company, LocalName, Key1, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR23 item
   Description: Call UpdateExt to delete INGSTR23 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR23
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR26Cs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR26Cs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR26Cs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR26CRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR26Cs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR26Cs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR26CRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR26CRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR26Cs_Company_LocalName_Key1_Key2_Key3_Key4(Company, LocalName, Key1, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR26C item
   Description: Calls GetByID to retrieve the INGSTR26C item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR26C
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR26CRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR26Cs_Company_LocalName_Key1_Key2_Key3_Key4(Company, LocalName, Key1, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR26C for the service
   Description: Calls UpdateExt to update INGSTR26C. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR26C
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR26CRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR26Cs_Company_LocalName_Key1_Key2_Key3_Key4(Company, LocalName, Key1, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR26C item
   Description: Call UpdateExt to delete INGSTR26C item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR26C
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2Transactions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2Transactions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2Transactions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2TransactionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR2Transactions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2Transactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2Transactions_Company_LocalName_Key1_IntKey1_IntKey2_Key2_IntKey3(Company, LocalName, Key1, IntKey1, IntKey2, Key2, IntKey3, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2Transaction item
   Description: Calls GetByID to retrieve the INGSTR2Transaction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2Transaction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param IntKey2: Desc: IntKey2   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param IntKey3: Desc: IntKey3   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions(" + Company + "," + LocalName + "," + Key1 + "," + IntKey1 + "," + IntKey2 + "," + Key2 + "," + IntKey3 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR2Transactions_Company_LocalName_Key1_IntKey1_IntKey2_Key2_IntKey3(Company, LocalName, Key1, IntKey1, IntKey2, Key2, IntKey3, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR2Transaction for the service
   Description: Calls UpdateExt to update INGSTR2Transaction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2Transaction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param IntKey2: Desc: IntKey2   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param IntKey3: Desc: IntKey3   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions(" + Company + "," + LocalName + "," + Key1 + "," + IntKey1 + "," + IntKey2 + "," + Key2 + "," + IntKey3 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR2Transactions_Company_LocalName_Key1_IntKey1_IntKey2_Key2_IntKey3(Company, LocalName, Key1, IntKey1, IntKey2, Key2, IntKey3, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR2Transaction item
   Description: Call UpdateExt to delete INGSTR2Transaction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2Transaction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param IntKey2: Desc: IntKey2   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param IntKey3: Desc: IntKey3   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions(" + Company + "," + LocalName + "," + Key1 + "," + IntKey1 + "," + IntKey2 + "," + Key2 + "," + IntKey3 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseINGSTR2Report, whereClauseINGSTR2ReportAttch, whereClauseINGSTR23, whereClauseINGSTR26C, whereClauseINGSTR2MatchedLine, whereClauseINGSTR2Transaction, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseINGSTR2Report=" + whereClauseINGSTR2Report
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseINGSTR2ReportAttch=" + whereClauseINGSTR2ReportAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseINGSTR23=" + whereClauseINGSTR23
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseINGSTR26C=" + whereClauseINGSTR26C
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseINGSTR2MatchedLine=" + whereClauseINGSTR2MatchedLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseINGSTR2Transaction=" + whereClauseINGSTR2Transaction
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ImportStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportStatement
   Description: Import Statement file
   OperationID: ImportStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteImportData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteImportData
   Description: Deletes lines imported for the current section of the current report and removes links from the previous reports
   OperationID: DeleteImportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsImportData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsImportData
   Description: Checks existence of imported data
   OperationID: ExistsImportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsImportDataSection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsImportDataSection
   Description: Checks for existence of imported data in specific section of the report.
   OperationID: ExistsImportDataSection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsImportDataSection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsImportDataSection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsApproveAllowed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsApproveAllowed
   Description: Check if report can be approved
   OperationID: IsApproveAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsApproveAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsApproveAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveTransactions
   Description: Retrieve Transactions
   OperationID: RetrieveTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchTransaction2Line(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchTransaction2Line
   OperationID: MatchTransaction2Line
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchTransaction2Line_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchTransaction2Line_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchFromLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchFromLine
   OperationID: UnmatchFromLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchFromLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchFromLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchSection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchSection
   OperationID: MatchSection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchSection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchSection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR2Report(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR2Report
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2Report
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2Report_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2Report_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR2ReportAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR2ReportAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2ReportAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2ReportAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2ReportAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR23(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR23
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR23
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR23_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR23_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR26C(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR26C
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR26C
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR26C_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR26C_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR2MatchedLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR2MatchedLine
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2MatchedLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2MatchedLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2MatchedLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR2Transaction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR2Transaction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2Transaction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2Transaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2Transaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR23Row:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR23Row] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR26CRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR26CRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2MatchedLineRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2MatchedLineRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2ReportAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2ReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2ReportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2TransactionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2TransactionRow] = obj["value"]
      pass

class Erp_Tablesets_INGSTR23Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APInvoiceAmt:int = obj["APInvoiceAmt"]
      self.APInvoiceDate:str = obj["APInvoiceDate"]
      self.APInvoiceLegalNumber:str = obj["APInvoiceLegalNumber"]
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      self.CESSAmt:int = obj["CESSAmt"]
      """  CESS Amount  """  
      self.CGSTAmt:int = obj["CGSTAmt"]
      """  CGST Amount  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.Eligibility:str = obj["Eligibility"]
      """  Eligibility  """  
      self.GSTID:str = obj["GSTID"]
      """  GST ID  """  
      self.IGSTAmt:int = obj["IGSTAmt"]
      """  IGST Amount  """  
      self.ImportCounter:int = obj["ImportCounter"]
      self.INGSTR2TransactionCESSAmt:int = obj["INGSTR2TransactionCESSAmt"]
      """  Matched AP Invoice CESS Amount  """  
      self.INGSTR2TransactionCGSTAmt:int = obj["INGSTR2TransactionCGSTAmt"]
      """  Matched AP Invoice CGST Amount  """  
      self.INGSTR2TransactionIGSTAmt:int = obj["INGSTR2TransactionIGSTAmt"]
      """  Matched AP Invoice IGST Amoun  """  
      self.INGSTR2TransactionITCCESSAmt:int = obj["INGSTR2TransactionITCCESSAmt"]
      """  Matched AP Invoice ITC CESS Amoun  """  
      self.INGSTR2TransactionITCCGSTAmt:int = obj["INGSTR2TransactionITCCGSTAmt"]
      """  Matched AP Invoice ITC CGST Amoun  """  
      self.INGSTR2TransactionITCIGSTAmt:int = obj["INGSTR2TransactionITCIGSTAmt"]
      """  Matched AP Invoice ITC IGST Amoun  """  
      self.INGSTR2TransactionITCSGSTAmt:int = obj["INGSTR2TransactionITCSGSTAmt"]
      """  Matched AP Invoice ITC SGST Amoun  """  
      self.INGSTR2TransactionRate:int = obj["INGSTR2TransactionRate"]
      """  Matched AP Invoice Rate  """  
      self.INGSTR2TransactionSGSTAmt:int = obj["INGSTR2TransactionSGSTAmt"]
      """  Matched AP Invoice SGST Amoun  """  
      self.INGSTR2TransactionTaxableAmt:int = obj["INGSTR2TransactionTaxableAmt"]
      """  Matched AP Invoice Taxable Amoun  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.ITCCESSAmt:int = obj["ITCCESSAmt"]
      """  ITC CESS Amount  """  
      self.ITCCGSTAmt:int = obj["ITCCGSTAmt"]
      """  ITC CGST Amount  """  
      self.ITCIGSTAmt:int = obj["ITCIGSTAmt"]
      """  ITC IGST Amount  """  
      self.ITCSGSTAmt:int = obj["ITCSGSTAmt"]
      """  ITC SGST Amount  """  
      self.LatestImport:int = obj["LatestImport"]
      """  Latest Import  """  
      self.LineStatus:int = obj["LineStatus"]
      """  Line Status  """  
      self.Matched:bool = obj["Matched"]
      """  Matched  """  
      self.Message:str = obj["Message"]
      """  Message  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.PlaceSupply:str = obj["PlaceSupply"]
      """  Place of Supply  """  
      self.Rate:int = obj["Rate"]
      """  Rate  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RowNum:int = obj["RowNum"]
      """  Row Number  """  
      self.SGSTAmt:int = obj["SGSTAmt"]
      """  SGST Amount  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount  """  
      self.APVendorNum:int = obj["APVendorNum"]
      self.Manual:bool = obj["Manual"]
      self.VendorName:str = obj["VendorName"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR26CRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APInvoiceAmt:int = obj["APInvoiceAmt"]
      self.APInvoiceDate:str = obj["APInvoiceDate"]
      self.APInvoiceLegalNumber:str = obj["APInvoiceLegalNumber"]
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      self.CESSAmt:int = obj["CESSAmt"]
      """  CESS Amount  """  
      self.CGSTAmt:int = obj["CGSTAmt"]
      """  CGST Amount  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.Eligibility:str = obj["Eligibility"]
      """  Eligibility  """  
      self.GSTID:str = obj["GSTID"]
      """  GST ID  """  
      self.IGSTAmt:int = obj["IGSTAmt"]
      """  IGST Amount  """  
      self.ImportCounter:int = obj["ImportCounter"]
      self.INGSTR2TransactionCESSAmt:int = obj["INGSTR2TransactionCESSAmt"]
      """  Matched AP Invoice CESS Amount  """  
      self.INGSTR2TransactionCGSTAmt:int = obj["INGSTR2TransactionCGSTAmt"]
      """  Matched AP Invoice CGST Amount  """  
      self.INGSTR2TransactionIGSTAmt:int = obj["INGSTR2TransactionIGSTAmt"]
      """  Matched AP Invoice IGST Amoun  """  
      self.INGSTR2TransactionITCCESSAmt:int = obj["INGSTR2TransactionITCCESSAmt"]
      """  Matched AP Invoice ITC CESS Amoun  """  
      self.INGSTR2TransactionITCCGSTAmt:int = obj["INGSTR2TransactionITCCGSTAmt"]
      """  Matched AP Invoice ITC CGST Amoun  """  
      self.INGSTR2TransactionITCIGSTAmt:int = obj["INGSTR2TransactionITCIGSTAmt"]
      """  Matched AP Invoice ITC IGST Amoun  """  
      self.INGSTR2TransactionITCSGSTAmt:int = obj["INGSTR2TransactionITCSGSTAmt"]
      """  Matched AP Invoice ITC SGST Amoun  """  
      self.INGSTR2TransactionRate:int = obj["INGSTR2TransactionRate"]
      """  Matched AP Invoice Rate  """  
      self.INGSTR2TransactionSGSTAmt:int = obj["INGSTR2TransactionSGSTAmt"]
      """  Matched AP Invoice SGST Amoun  """  
      self.INGSTR2TransactionTaxableAmt:int = obj["INGSTR2TransactionTaxableAmt"]
      """  Matched AP Invoice Taxable Amoun  """  
      self.NoteAmt:int = obj["NoteAmt"]
      """  Note Amount  """  
      self.NoteDate:str = obj["NoteDate"]
      """  Note Date  """  
      self.NoteNum:str = obj["NoteNum"]
      """  Note Number  """  
      self.NoteType:str = obj["NoteType"]
      """  Note Type  """  
      self.ITCCESSAmt:int = obj["ITCCESSAmt"]
      """  ITC CESS Amount  """  
      self.ITCCGSTAmt:int = obj["ITCCGSTAmt"]
      """  ITC CGST Amount  """  
      self.ITCIGSTAmt:int = obj["ITCIGSTAmt"]
      """  ITC IGST Amount  """  
      self.ITCSGSTAmt:int = obj["ITCSGSTAmt"]
      """  ITC SGST Amount  """  
      self.LatestImport:int = obj["LatestImport"]
      """  Latest Import  """  
      self.LineStatus:int = obj["LineStatus"]
      """  Line Status  """  
      self.Matched:bool = obj["Matched"]
      """  Matched  """  
      self.Message:str = obj["Message"]
      """  Message  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.Rate:int = obj["Rate"]
      """  Rate  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RowNum:int = obj["RowNum"]
      """  Row Number  """  
      self.SGSTAmt:int = obj["SGSTAmt"]
      """  SGST Amount  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.APVendorNum:int = obj["APVendorNum"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Manual:bool = obj["Manual"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2MatchedLineRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Section:str = obj["Section"]
      """  Section  """  
      self.TransactionType:int = obj["TransactionType"]
      """  TransactionType  """  
      self.ExternalSysRowID:str = obj["ExternalSysRowID"]
      """  ExternalSysRowID  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.IntKey1:int = obj["IntKey1"]
      """  IntKey1  """  
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

class Erp_Tablesets_INGSTR2ReportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportListRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.FinancialPeriod:str = obj["FinancialPeriod"]
      """  FinancialPeriod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Status:int = obj["Status"]
      """  Status  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ConfirmedBy:str = obj["ConfirmedBy"]
      """  ConfirmedBy  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.FinancialPeriod:str = obj["FinancialPeriod"]
      """  FinancialPeriod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FromDate:str = obj["FromDate"]
      """  FromDate  """  
      self.ToDate:str = obj["ToDate"]
      """  ToDate  """  
      self.Status:int = obj["Status"]
      """  Status  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ConfirmedBy:str = obj["ConfirmedBy"]
      """  ConfirmedBy  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  ConfirmDate  """  
      self.SkipInvoices:bool = obj["SkipInvoices"]
      """  SkipInvoices  """  
      self.ReportNotes:str = obj["ReportNotes"]
      """  ReportNotes  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Imported:bool = obj["Imported"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2TransactionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.IntKey1:int = obj["IntKey1"]
      """  Integer Key field 1  """  
      self.IntKey2:int = obj["IntKey2"]
      """  Integer Key field 2  """  
      self.IntKey3:int = obj["IntKey3"]
      """  Integer Key field 3  """  
      self.Key1:str = obj["Key1"]
      """  Character Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Character Key field 2  """  
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportID:str = obj["ReportID"]
      self.TransactionType:int = obj["TransactionType"]
      self.RowNum:int = obj["RowNum"]
      self.Rate:int = obj["Rate"]
      self.TaxableAmt:int = obj["TaxableAmt"]
      self.IGSTAmt:int = obj["IGSTAmt"]
      self.CGSTAmt:int = obj["CGSTAmt"]
      self.SGSTAmt:int = obj["SGSTAmt"]
      self.CESSAmt:int = obj["CESSAmt"]
      self.ITCIGSTAmt:int = obj["ITCIGSTAmt"]
      self.ITCCGSTAmt:int = obj["ITCCGSTAmt"]
      self.ITCSGSTAmt:int = obj["ITCSGSTAmt"]
      self.ITCCESSAmt:int = obj["ITCCESSAmt"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.VendorNum:int = obj["VendorNum"]
      self.Matched:bool = obj["Matched"]
      self.Selected:bool = obj["Selected"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.APInvHedInvoiceAmt:int = obj["APInvHedInvoiceAmt"]
      self.APInvHedInvoiceDate:str = obj["APInvHedInvoiceDate"]
      self.APInvHedLegalNumber:str = obj["APInvHedLegalNumber"]
      self.VendorName:str = obj["VendorName"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteImportData_input:
   """ Required : 
   reportID
   section
   ds
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      self.section:str = obj["section"]
      """  Section  """  
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class DeleteImportData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_INGSTR23Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APInvoiceAmt:int = obj["APInvoiceAmt"]
      self.APInvoiceDate:str = obj["APInvoiceDate"]
      self.APInvoiceLegalNumber:str = obj["APInvoiceLegalNumber"]
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      self.CESSAmt:int = obj["CESSAmt"]
      """  CESS Amount  """  
      self.CGSTAmt:int = obj["CGSTAmt"]
      """  CGST Amount  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.Eligibility:str = obj["Eligibility"]
      """  Eligibility  """  
      self.GSTID:str = obj["GSTID"]
      """  GST ID  """  
      self.IGSTAmt:int = obj["IGSTAmt"]
      """  IGST Amount  """  
      self.ImportCounter:int = obj["ImportCounter"]
      self.INGSTR2TransactionCESSAmt:int = obj["INGSTR2TransactionCESSAmt"]
      """  Matched AP Invoice CESS Amount  """  
      self.INGSTR2TransactionCGSTAmt:int = obj["INGSTR2TransactionCGSTAmt"]
      """  Matched AP Invoice CGST Amount  """  
      self.INGSTR2TransactionIGSTAmt:int = obj["INGSTR2TransactionIGSTAmt"]
      """  Matched AP Invoice IGST Amoun  """  
      self.INGSTR2TransactionITCCESSAmt:int = obj["INGSTR2TransactionITCCESSAmt"]
      """  Matched AP Invoice ITC CESS Amoun  """  
      self.INGSTR2TransactionITCCGSTAmt:int = obj["INGSTR2TransactionITCCGSTAmt"]
      """  Matched AP Invoice ITC CGST Amoun  """  
      self.INGSTR2TransactionITCIGSTAmt:int = obj["INGSTR2TransactionITCIGSTAmt"]
      """  Matched AP Invoice ITC IGST Amoun  """  
      self.INGSTR2TransactionITCSGSTAmt:int = obj["INGSTR2TransactionITCSGSTAmt"]
      """  Matched AP Invoice ITC SGST Amoun  """  
      self.INGSTR2TransactionRate:int = obj["INGSTR2TransactionRate"]
      """  Matched AP Invoice Rate  """  
      self.INGSTR2TransactionSGSTAmt:int = obj["INGSTR2TransactionSGSTAmt"]
      """  Matched AP Invoice SGST Amoun  """  
      self.INGSTR2TransactionTaxableAmt:int = obj["INGSTR2TransactionTaxableAmt"]
      """  Matched AP Invoice Taxable Amoun  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.ITCCESSAmt:int = obj["ITCCESSAmt"]
      """  ITC CESS Amount  """  
      self.ITCCGSTAmt:int = obj["ITCCGSTAmt"]
      """  ITC CGST Amount  """  
      self.ITCIGSTAmt:int = obj["ITCIGSTAmt"]
      """  ITC IGST Amount  """  
      self.ITCSGSTAmt:int = obj["ITCSGSTAmt"]
      """  ITC SGST Amount  """  
      self.LatestImport:int = obj["LatestImport"]
      """  Latest Import  """  
      self.LineStatus:int = obj["LineStatus"]
      """  Line Status  """  
      self.Matched:bool = obj["Matched"]
      """  Matched  """  
      self.Message:str = obj["Message"]
      """  Message  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.PlaceSupply:str = obj["PlaceSupply"]
      """  Place of Supply  """  
      self.Rate:int = obj["Rate"]
      """  Rate  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RowNum:int = obj["RowNum"]
      """  Row Number  """  
      self.SGSTAmt:int = obj["SGSTAmt"]
      """  SGST Amount  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount  """  
      self.APVendorNum:int = obj["APVendorNum"]
      self.Manual:bool = obj["Manual"]
      self.VendorName:str = obj["VendorName"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR26CRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APInvoiceAmt:int = obj["APInvoiceAmt"]
      self.APInvoiceDate:str = obj["APInvoiceDate"]
      self.APInvoiceLegalNumber:str = obj["APInvoiceLegalNumber"]
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      self.CESSAmt:int = obj["CESSAmt"]
      """  CESS Amount  """  
      self.CGSTAmt:int = obj["CGSTAmt"]
      """  CGST Amount  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.Eligibility:str = obj["Eligibility"]
      """  Eligibility  """  
      self.GSTID:str = obj["GSTID"]
      """  GST ID  """  
      self.IGSTAmt:int = obj["IGSTAmt"]
      """  IGST Amount  """  
      self.ImportCounter:int = obj["ImportCounter"]
      self.INGSTR2TransactionCESSAmt:int = obj["INGSTR2TransactionCESSAmt"]
      """  Matched AP Invoice CESS Amount  """  
      self.INGSTR2TransactionCGSTAmt:int = obj["INGSTR2TransactionCGSTAmt"]
      """  Matched AP Invoice CGST Amount  """  
      self.INGSTR2TransactionIGSTAmt:int = obj["INGSTR2TransactionIGSTAmt"]
      """  Matched AP Invoice IGST Amoun  """  
      self.INGSTR2TransactionITCCESSAmt:int = obj["INGSTR2TransactionITCCESSAmt"]
      """  Matched AP Invoice ITC CESS Amoun  """  
      self.INGSTR2TransactionITCCGSTAmt:int = obj["INGSTR2TransactionITCCGSTAmt"]
      """  Matched AP Invoice ITC CGST Amoun  """  
      self.INGSTR2TransactionITCIGSTAmt:int = obj["INGSTR2TransactionITCIGSTAmt"]
      """  Matched AP Invoice ITC IGST Amoun  """  
      self.INGSTR2TransactionITCSGSTAmt:int = obj["INGSTR2TransactionITCSGSTAmt"]
      """  Matched AP Invoice ITC SGST Amoun  """  
      self.INGSTR2TransactionRate:int = obj["INGSTR2TransactionRate"]
      """  Matched AP Invoice Rate  """  
      self.INGSTR2TransactionSGSTAmt:int = obj["INGSTR2TransactionSGSTAmt"]
      """  Matched AP Invoice SGST Amoun  """  
      self.INGSTR2TransactionTaxableAmt:int = obj["INGSTR2TransactionTaxableAmt"]
      """  Matched AP Invoice Taxable Amoun  """  
      self.NoteAmt:int = obj["NoteAmt"]
      """  Note Amount  """  
      self.NoteDate:str = obj["NoteDate"]
      """  Note Date  """  
      self.NoteNum:str = obj["NoteNum"]
      """  Note Number  """  
      self.NoteType:str = obj["NoteType"]
      """  Note Type  """  
      self.ITCCESSAmt:int = obj["ITCCESSAmt"]
      """  ITC CESS Amount  """  
      self.ITCCGSTAmt:int = obj["ITCCGSTAmt"]
      """  ITC CGST Amount  """  
      self.ITCIGSTAmt:int = obj["ITCIGSTAmt"]
      """  ITC IGST Amount  """  
      self.ITCSGSTAmt:int = obj["ITCSGSTAmt"]
      """  ITC SGST Amount  """  
      self.LatestImport:int = obj["LatestImport"]
      """  Latest Import  """  
      self.LineStatus:int = obj["LineStatus"]
      """  Line Status  """  
      self.Matched:bool = obj["Matched"]
      """  Matched  """  
      self.Message:str = obj["Message"]
      """  Message  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.Rate:int = obj["Rate"]
      """  Rate  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RowNum:int = obj["RowNum"]
      """  Row Number  """  
      self.SGSTAmt:int = obj["SGSTAmt"]
      """  SGST Amount  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.APVendorNum:int = obj["APVendorNum"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Manual:bool = obj["Manual"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2MatchedLineRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Section:str = obj["Section"]
      """  Section  """  
      self.TransactionType:int = obj["TransactionType"]
      """  TransactionType  """  
      self.ExternalSysRowID:str = obj["ExternalSysRowID"]
      """  ExternalSysRowID  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.IntKey1:int = obj["IntKey1"]
      """  IntKey1  """  
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

class Erp_Tablesets_INGSTR2ReportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportImportTableset:
   def __init__(self, obj):
      self.INGSTR2Report:list[Erp_Tablesets_INGSTR2ReportRow] = obj["INGSTR2Report"]
      self.INGSTR2ReportAttch:list[Erp_Tablesets_INGSTR2ReportAttchRow] = obj["INGSTR2ReportAttch"]
      self.INGSTR23:list[Erp_Tablesets_INGSTR23Row] = obj["INGSTR23"]
      self.INGSTR26C:list[Erp_Tablesets_INGSTR26CRow] = obj["INGSTR26C"]
      self.INGSTR2MatchedLine:list[Erp_Tablesets_INGSTR2MatchedLineRow] = obj["INGSTR2MatchedLine"]
      self.INGSTR2Transaction:list[Erp_Tablesets_INGSTR2TransactionRow] = obj["INGSTR2Transaction"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_INGSTR2ReportListRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.FinancialPeriod:str = obj["FinancialPeriod"]
      """  FinancialPeriod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Status:int = obj["Status"]
      """  Status  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ConfirmedBy:str = obj["ConfirmedBy"]
      """  ConfirmedBy  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportListTableset:
   def __init__(self, obj):
      self.INGSTR2ReportList:list[Erp_Tablesets_INGSTR2ReportListRow] = obj["INGSTR2ReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_INGSTR2ReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.FinancialPeriod:str = obj["FinancialPeriod"]
      """  FinancialPeriod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.FromDate:str = obj["FromDate"]
      """  FromDate  """  
      self.ToDate:str = obj["ToDate"]
      """  ToDate  """  
      self.Status:int = obj["Status"]
      """  Status  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ConfirmedBy:str = obj["ConfirmedBy"]
      """  ConfirmedBy  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  ConfirmDate  """  
      self.SkipInvoices:bool = obj["SkipInvoices"]
      """  SkipInvoices  """  
      self.ReportNotes:str = obj["ReportNotes"]
      """  ReportNotes  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Imported:bool = obj["Imported"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2TransactionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.IntKey1:int = obj["IntKey1"]
      """  Integer Key field 1  """  
      self.IntKey2:int = obj["IntKey2"]
      """  Integer Key field 2  """  
      self.IntKey3:int = obj["IntKey3"]
      """  Integer Key field 3  """  
      self.Key1:str = obj["Key1"]
      """  Character Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Character Key field 2  """  
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportID:str = obj["ReportID"]
      self.TransactionType:int = obj["TransactionType"]
      self.RowNum:int = obj["RowNum"]
      self.Rate:int = obj["Rate"]
      self.TaxableAmt:int = obj["TaxableAmt"]
      self.IGSTAmt:int = obj["IGSTAmt"]
      self.CGSTAmt:int = obj["CGSTAmt"]
      self.SGSTAmt:int = obj["SGSTAmt"]
      self.CESSAmt:int = obj["CESSAmt"]
      self.ITCIGSTAmt:int = obj["ITCIGSTAmt"]
      self.ITCCGSTAmt:int = obj["ITCCGSTAmt"]
      self.ITCSGSTAmt:int = obj["ITCSGSTAmt"]
      self.ITCCESSAmt:int = obj["ITCCESSAmt"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.VendorNum:int = obj["VendorNum"]
      self.Matched:bool = obj["Matched"]
      self.Selected:bool = obj["Selected"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.APInvHedInvoiceAmt:int = obj["APInvHedInvoiceAmt"]
      self.APInvHedInvoiceDate:str = obj["APInvHedInvoiceDate"]
      self.APInvHedLegalNumber:str = obj["APInvHedLegalNumber"]
      self.VendorName:str = obj["VendorName"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtINGSTR2ReportImportTableset:
   def __init__(self, obj):
      self.INGSTR2Report:list[Erp_Tablesets_INGSTR2ReportRow] = obj["INGSTR2Report"]
      self.INGSTR2ReportAttch:list[Erp_Tablesets_INGSTR2ReportAttchRow] = obj["INGSTR2ReportAttch"]
      self.INGSTR23:list[Erp_Tablesets_INGSTR23Row] = obj["INGSTR23"]
      self.INGSTR26C:list[Erp_Tablesets_INGSTR26CRow] = obj["INGSTR26C"]
      self.INGSTR2MatchedLine:list[Erp_Tablesets_INGSTR2MatchedLineRow] = obj["INGSTR2MatchedLine"]
      self.INGSTR2Transaction:list[Erp_Tablesets_INGSTR2TransactionRow] = obj["INGSTR2Transaction"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsImportDataSection_input:
   """ Required : 
   reportID
   section
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      self.section:str = obj["section"]
      """  Section key  """  
      pass

class ExistsImportDataSection_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsImportData_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      pass

class ExistsImportData_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewINGSTR23_input:
   """ Required : 
   ds
   localName
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewINGSTR23_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewINGSTR26C_input:
   """ Required : 
   ds
   localName
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewINGSTR26C_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewINGSTR2MatchedLine_input:
   """ Required : 
   ds
   reportID
   section
   transactionType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.section:str = obj["section"]
      self.transactionType:int = obj["transactionType"]
      pass

class GetNewINGSTR2MatchedLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewINGSTR2ReportAttch_input:
   """ Required : 
   ds
   reportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      pass

class GetNewINGSTR2ReportAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewINGSTR2Report_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class GetNewINGSTR2Report_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewINGSTR2Transaction_input:
   """ Required : 
   ds
   localName
   key1
   intKey1
   intKey2
   key2
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.intKey1:int = obj["intKey1"]
      self.intKey2:int = obj["intKey2"]
      self.key2:str = obj["key2"]
      pass

class GetNewINGSTR2Transaction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseINGSTR2Report
   whereClauseINGSTR2ReportAttch
   whereClauseINGSTR23
   whereClauseINGSTR26C
   whereClauseINGSTR2MatchedLine
   whereClauseINGSTR2Transaction
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseINGSTR2Report:str = obj["whereClauseINGSTR2Report"]
      self.whereClauseINGSTR2ReportAttch:str = obj["whereClauseINGSTR2ReportAttch"]
      self.whereClauseINGSTR23:str = obj["whereClauseINGSTR23"]
      self.whereClauseINGSTR26C:str = obj["whereClauseINGSTR26C"]
      self.whereClauseINGSTR2MatchedLine:str = obj["whereClauseINGSTR2MatchedLine"]
      self.whereClauseINGSTR2Transaction:str = obj["whereClauseINGSTR2Transaction"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["returnObj"]
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

class ImportStatement_input:
   """ Required : 
   eftHeadUID
   section
   importFile
   reportID
   """  
   def __init__(self, obj):
      self.eftHeadUID:int = obj["eftHeadUID"]
      """  EFTHeadUID  """  
      self.section:str = obj["section"]
      """  Section  """  
      self.importFile:str = obj["importFile"]
      """  Import file name  """  
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      pass

class ImportStatement_output:
   def __init__(self, obj):
      pass

class IsApproveAllowed_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      pass

class IsApproveAllowed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.result:int = obj["parameters"]
      pass

      """  output parameters  """  

class MatchSection_input:
   """ Required : 
   ipReportID
   ipSectionName
   ipRematch
   ds
   """  
   def __init__(self, obj):
      self.ipReportID:str = obj["ipReportID"]
      self.ipSectionName:str = obj["ipSectionName"]
      self.ipRematch:bool = obj["ipRematch"]
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class MatchSection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MatchTransaction2Line_input:
   """ Required : 
   ipReportID
   ipSectionName
   ipGSTR2XSysRowID
   ds
   """  
   def __init__(self, obj):
      self.ipReportID:str = obj["ipReportID"]
      self.ipSectionName:str = obj["ipSectionName"]
      self.ipGSTR2XSysRowID:str = obj["ipGSTR2XSysRowID"]
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class MatchTransaction2Line_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RetrieveTransactions_input:
   """ Required : 
   ipReportID
   ipSection
   ds
   """  
   def __init__(self, obj):
      self.ipReportID:str = obj["ipReportID"]
      """  From date  """  
      self.ipSection:str = obj["ipSection"]
      """  To date  """  
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class RetrieveTransactions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnmatchFromLine_input:
   """ Required : 
   ipReportID
   ipSectionName
   ipINGSTR2XSysRowID
   ds
   """  
   def __init__(self, obj):
      self.ipReportID:str = obj["ipReportID"]
      self.ipSectionName:str = obj["ipSectionName"]
      self.ipINGSTR2XSysRowID:str = obj["ipINGSTR2XSysRowID"]
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class UnmatchFromLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtINGSTR2ReportImportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtINGSTR2ReportImportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

