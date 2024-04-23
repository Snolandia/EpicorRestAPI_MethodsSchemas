import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLJournalEntrySvc
# Description: Business Object for Journal Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLJournalEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJournalEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJournalEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries",headers=creds) as resp:
           return await resp.json()

async def post_GLJournalEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJournalEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJournalEntry item
   Description: Calls GetByID to retrieve the GLJournalEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJournalEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJournalEntry for the service
   Description: Calls UpdateExt to update GLJournalEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJournalEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJournalEntry item
   Description: Call UpdateExt to delete GLJournalEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJournalEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls",headers=creds) as resp:
           return await resp.json()

async def get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, JournalLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnl item
   Description: Calls GetByID to retrieve the GLJrnDtlMnl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param JournalLine: Desc: JournalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnHedAttches(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnHedAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnHedAttches",headers=creds) as resp:
           return await resp.json()

async def get_GLJournalEntries_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnHedAttch item
   Description: Calls GetByID to retrieve the GLJrnHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnHedAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJournalEntries(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlMnls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnl item
   Description: Calls GetByID to retrieve the GLJrnDtlMnl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlMnl for the service
   Description: Calls UpdateExt to update GLJrnDtlMnl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlMnl item
   Description: Call UpdateExt to delete GLJrnDtlMnl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlDEASches(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlDEASches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlDEASches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlDEASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlDEASches",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, GLBookID, GLJournalNum, AmortSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlDEASch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlTranGLCs(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlTranGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlTranGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlTranGLCs",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlTranGLCs_SysRowID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlTranGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlTranGLCs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlAttches(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlAttches",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlDEASches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnlDEASches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlDEASches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlDEASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlMnlDEASches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlDEASches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, GLBookID, JournalCode, GLJournalNum, JournalLine, AmortSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlDEASch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, GLBookID, JournalCode, GLJournalNum, JournalLine, AmortSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlMnlDEASch for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlDEASch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlDEASch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, GLBookID, JournalCode, GLJournalNum, JournalLine, AmortSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlMnlDEASch item
   Description: Call UpdateExt to delete GLJrnDtlMnlDEASch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlDEASch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlTranGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnlTranGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlTranGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlMnlTranGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlTranGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlTranGLCs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlTranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlTranGLC
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlMnlTranGLCs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlMnlTranGLC for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlTranGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlTranGLC
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlTranGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlMnlTranGLCs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlMnlTranGLC item
   Description: Call UpdateExt to delete GLJrnDtlMnlTranGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlTranGLC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlTranGLCs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlMnlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlMnlAttch for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlMnlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlMnlAttch item
   Description: Call UpdateExt to delete GLJrnDtlMnlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnDtlMnlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnHedAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnHedAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnHedAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnHedAttch item
   Description: Calls GetByID to retrieve the GLJrnHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnHedAttch for the service
   Description: Calls UpdateExt to update GLJrnHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnHedAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnHedAttch item
   Description: Call UpdateExt to delete GLJrnHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GLJrnHedAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlAllocations(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlAllocations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlAllocations
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlAllocationsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations",headers=creds) as resp:
           return await resp.json()

async def post_GlAllocations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlAllocations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlAllocationsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlAllocationsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlAllocations_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlAllocation item
   Description: Calls GetByID to retrieve the GlAllocation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlAllocation
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlAllocationsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlAllocations_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlAllocation for the service
   Description: Calls UpdateExt to update GlAllocation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlAllocation
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlAllocationsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlAllocations_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlAllocation item
   Description: Call UpdateExt to delete GlAllocation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlAllocation
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/GlAllocations(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLJrnHed, whereClauseGLJrnHedAttch, whereClauseGLJrnDtlMnl, whereClauseGLJrnDtlMnlAttch, whereClauseGLJrnDtlMnlDEASch, whereClauseGLJrnDtlMnlTranGLC, whereClauseGlAllocations, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLJrnHed=" + whereClauseGLJrnHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnHedAttch=" + whereClauseGLJrnHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnDtlMnl=" + whereClauseGLJrnDtlMnl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnDtlMnlAttch=" + whereClauseGLJrnDtlMnlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnDtlMnlDEASch=" + whereClauseGLJrnDtlMnlDEASch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnDtlMnlTranGLC=" + whereClauseGLJrnDtlMnlTranGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlAllocations=" + whereClauseGlAllocations
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bookID, fiscalYear, fiscalYearSuffix, journalCode, journalNum, fiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "bookID=" + bookID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYear=" + fiscalYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYearSuffix=" + fiscalYearSuffix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "journalCode=" + journalCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "journalNum=" + journalNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalCalendarID=" + fiscalCalendarID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AutoBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoBalance
   Description: This method will create a new line with the balancing figure defaulted
into the appropriate debit or credit column if the current line has a
non-zero balance.  If the current line has zero debit/credit values then
the debit/credit values of that line are updated with the balancing entry.
   OperationID: AutoBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoComplete
   Description: This method is called only for 'Tax Line' and will update current line in the following way:
- calculate tax amount using tax type, tax rate and taxable amount from 'Tax Options' and update correspondent amount (credit or debit);
- update account
   OperationID: AutoComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateAmountForTaxLineEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateAmountForTaxLineEx
   Description: This method calculates debit/credit amount if selected tax rate is applied to the taxable amount
   OperationID: CalculateAmountForTaxLineEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateAmountForTaxLineEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateAmountForTaxLineEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExtCompanyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExtCompanyID
   Description: This method resets the regular and Multi-Company G/L Accounts and the Reference Codes
when the External Company ID changes.
   OperationID: ChangeExtCompanyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExtCompanyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExtCompanyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGlAcct1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGlAcct1
   Description: This method calls Check StatUOMCoe and CheckCurrencyAccount instead 2 calls from UIs
   OperationID: ChangeGlAcct1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlAcct1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlAcct1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExtGlAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExtGlAcct
   Description: This method calls Check if external G/L Account is valid
   OperationID: ChangeExtGlAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExtGlAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExtGlAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGlRefCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGlRefCode
   Description: This method updates the G/L Reference Type and Code Description when the
GL Reference Code changes.
   OperationID: ChangeGlRefCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlRefCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlRefCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLinkedLineAmnts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLinkedLineAmnts
   Description: This method updates amounts in the linked journal details.
   OperationID: ChangeLinkedLineAmnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLinkedLineAmnts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLinkedLineAmnts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMultiCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMultiCompany
   Description: This method resets the External Company ID, regular and Multi-Company G/L Accounts
and the Reference Codes when the Multi-Company flag changes.
   OperationID: ChangeMultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMultiCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeReverse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeReverse
   Description: This method defaults the Reverse Date when the Reverse flag is checked.
   OperationID: ChangeReverse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxCode
   Description: This method gets the default Tax Rate for a Tax Code
   OperationID: ChangeTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAllocations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAllocations
   Description: This procudura validata if there is Allocations for the Journal Book
   OperationID: CheckAllocations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAllocations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAllocations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyAccount
   Description: This procedure validates if the Account is a currency Account
   OperationID: CheckCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyAccountExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyAccountExt
   Description: This procedure validates if the Account is a currency Account, define list of available currencies.
   OperationID: CheckCurrencyAccountExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccountExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccountExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckStatUOMAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckStatUOMAccount
   Description: This
   OperationID: CheckStatUOMAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckStatUOMAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckStatUOMAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyAccount2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyAccount2
   Description: This procudura validate if the Account is a currency Account
   OperationID: CheckCurrencyAccount2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccount2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccount2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyAccountForTaxLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyAccountForTaxLine
   Description: This procudure validate if the Account is a currency Account for tax line with linked taxable line
   OperationID: CheckCurrencyAccountForTaxLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyAccountForTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyAccountForTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDocumentIsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlBeforeUpdate
   Description: Check that Journal Line is not linked from another External Company
   OperationID: CheckDtlBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartOfDual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartOfDual
   Description: This procudura checks In/Out value.
   OperationID: CheckPartOfDual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartOfDual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartOfDual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckReportingModule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReportingModule
   Description: This procudura checks Reporting Module value.
   OperationID: CheckReportingModule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReportingModule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReportingModule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxableLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxableLine
   Description: This procudura checks taxable line: it should exist and not a tax line.
   OperationID: CheckTaxableLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxableLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxableLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxAmountSign(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxAmountSign
   Description: This procudura checks whether sign of tax amount correspond to sign of taxable amount
   OperationID: CheckTaxAmountSign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxAmountSign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxAmountSign_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxLiability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxLiability
   Description: This procudura checks Tax liability exists and not flagged as used in Tax Connect.
   OperationID: CheckTaxLiability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxPointDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxPointDate
   Description: This procudure checks whether Tax Point date is not later then tax rate Effective from date
   OperationID: CheckTaxPointDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxPointDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxPointDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxRate
   Description: This procudura checks Tax Rate
   OperationID: CheckTaxRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaxType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaxType
   Description: This procudure checks Tax Type
   OperationID: CheckTaxType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaxType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaxType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertCreditAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertCreditAmount
   Description: This method convert the document currency to the journal currency.
   OperationID: ConvertCreditAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertCreditAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertCreditAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertDebitAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertDebitAmount
   Description: This method convert the document currency to the journal currency.
   OperationID: ConvertDebitAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertDebitAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertDebitAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateDetailLineFromAllocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDetailLineFromAllocation
   Description: /// Call this method when the user clicks OK on the allocation sheet.  It
/// will create journal entries using the allocation information entered.
///
   OperationID: CreateDetailLineFromAllocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDetailLineFromAllocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDetailLineFromAllocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenLegalNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenLegalNum
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method is called when the journal was created from recurring journal
and legal number is set as 'manual'.
   OperationID: GenLegalNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByGroupID
   Description: This method is called in place of the GetByID method, requiring only the
the GL Group ID.
   OperationID: GetByGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlJrnHedTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlJrnHedTran
   Description: This method is called in place of the GetNewGlJrnHed method.  It allows
the input of the Current Group so that certian fields on the header
record can be defaulted from the group record.
   OperationID: GetNewGlJrnHedTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlJrnHedTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlJrnHedTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewStatisticalGLJrnHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewStatisticalGLJrnHed
   Description: Create Statistical Journal
   OperationID: GetNewStatisticalGLJrnHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewStatisticalGLJrnHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewStatisticalGLJrnHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxEntryMode(epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxEntryMode
   Description: Get company value 'Tax Entry Mode in GL Journal'
   OperationID: GetTaxEntryMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTaxRatesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxRatesList
   Description: Get the list of tax rates, related to specified Tax Type
   OperationID: GetTaxRatesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxRatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxRatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableCurrencies(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableCurrencies
   Description: Return available currencies for account. It is for multicurrency accounts for public usage.
   OperationID: GetAvailableCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxTypesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxTypesList
   Description: Get where clause to select tax types, related to specified Tax Liability
   OperationID: GetTaxTypesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRefSourceJrnLineList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRefSourceJrnLineList
   Description: Gets SourceJrnLineList from current GL Journal
   OperationID: GetRefSourceJrnLineList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRefSourceJrnLineList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRefSourceJrnLineList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxableLinesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxableLinesList
   Description: Gets TaxableLinesList from current GL Journal
   OperationID: GetTaxableLinesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxableLinesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxableLinesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGenLegalNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGenLegalNum
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method is called when the journal was created from recurring journal
and legal number is set as 'manual'.
   OperationID: PreGenLegalNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGenLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGenLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCurrencyAccount
   Description: This procedure validate it the currency is allowed.
   OperationID: ValidateCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAccountForStatJournal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAccountForStatJournal
   Description: Validate Account For Statistical Journal
   OperationID: ValidateAccountForStatJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAccountForStatJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccountForStatJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAccountForAllocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAccountForAllocation
   Description: Validate Account For Allocation
   OperationID: ValidateAccountForAllocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAccountForAllocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccountForAllocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCurrencyAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCurrencyAcct
   Description: This method should be called when book currency is changed
   OperationID: OnChangeCurrencyAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxableAmntInTranCurr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxableAmntInTranCurr
   Description: This method should be called when Taxable amount in transactional currency is changed
   OperationID: OnChangeTaxableAmntInTranCurr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableAmntInTranCurr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableAmntInTranCurr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxableLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxableLine
   Description: This method should be called when Taxable Line is changed
   OperationID: OnChangeTaxableLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxLiability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxLiability
   Description: This method should be called when Tax Liability is changed
   OperationID: OnChangeTaxLiability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxRate
   Description: This method should be called when Tax Rate is changed
   OperationID: OnChangeTaxRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxType
   Description: This method should be called when Tax Type is changed
   OperationID: OnChangeTaxType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLineReferenceHolder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLineReferenceHolder
   Description: This method should be called when Line Reference Holder is changed
   OperationID: OnChangeLineReferenceHolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLineReferenceHolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineReferenceHolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLineReference(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLineReference
   Description: This method should be called when Line Reference is changed
   OperationID: OnChangeLineReference
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLineReference_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineReference_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDefaultsForTaxLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDefaultsForTaxLine
   Description: Set default values if user check/uncheck 'Tax Line' option
   OperationID: SetDefaultsForTaxLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDefaultsForTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultsForTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAmountForTaxLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAmountForTaxLine
   Description: This method updates debit/credit amount
   OperationID: UpdateAmountForTaxLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAmountForTaxLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAmountForTaxLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllocations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllocations
   OperationID: GetAllocations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllocations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllocations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLineDefferedExp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLineDefferedExp
   Description: Occurs when Invoice Line Deferred Expense switch changed
   OperationID: OnChangeLineDefferedExp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLineDefferedExp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDefferedExp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLineDEACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLineDEACode
   Description: Occurs when Invoice Line DEA Code changed
   OperationID: OnChangeLineDEACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLineDEACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDEACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLineDEAAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLineDEAAccount
   Description: Occurs when GL Journal Line DEA Account changed
   OperationID: OnChangeLineDEAAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLineDEAAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDEAAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLineDEAStartDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLineDEAStartDate
   Description: Occurs when Invoice Line DEA Start Date changed
   OperationID: OnChangeLineDEAStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLineDEAStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLineDEAStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateAmortizationSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateAmortizationSchedule
   Description: Generates Amortization Schedule
   OperationID: GenerateAmortizationSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateAmortizationSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateAmortizationSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAmortizationSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAmortizationSchedule
   Description: Deletes Amortization Schedule
   OperationID: DeleteAmortizationSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAmortizationSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAmortizationSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDEAScheduleLineAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDEAScheduleLineAmount
   Description: Occurs when DEA Schedule Line Amortization Amount changed
   OperationID: OnChangeDEAScheduleLineAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDEAScheduleLineAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDEAScheduleLineAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDEAScheduleLineFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDEAScheduleLineFiscalPeriod
   Description: Occurs when DEA Schedule Line Fiscal Period changed
   OperationID: OnChangeDEAScheduleLineFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDEAScheduleLineFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDEAScheduleLineFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutocompleteAmortizationSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutocompleteAmortizationSchedule
   Description: Applies Remaining Amount to the last Schedule Line
   OperationID: AutocompleteAmortizationSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutocompleteAmortizationSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutocompleteAmortizationSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateAmortizationTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateAmortizationTotals
   Description: Calculates Deferred Expense Amortization Total Amounts
   OperationID: CalculateAmortizationTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateAmortizationTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateAmortizationTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnlDEASchPopulated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnlDEASchPopulated
   Description: Inserts a new row into the DataSet with fields populated depending on parent Invoice Line
   OperationID: GetNewGLJrnDtlMnlDEASchPopulated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlDEASchPopulated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlDEASchPopulated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultAccount
   Description: Gets default Deferred Expense GL account for a line.
   OperationID: GetDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetMYIndustryCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetMYIndustryCode
   Description: Resets MY Industry Code when Tax Line or Reporting Module is adjusted
   OperationID: ResetMYIndustryCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetMYIndustryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetMYIndustryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxableLinesListWithParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxableLinesListWithParams
   Description: Gets TaxableLinesList from current GL Journal
   OperationID: GetTaxableLinesListWithParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxableLinesListWithParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxableLinesListWithParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxaHandlingList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxaHandlingList
   Description: Get list of available Tax Handling values.
   OperationID: GetTaxaHandlingList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxaHandlingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxaHandlingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnHedAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnlDEASch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnlDEASch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlDEASch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnlTranGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnlTranGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlTranGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlTranGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlTranGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJournalEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlTranGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlTranGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnHedAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlAllocationsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlAllocationsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_GLJrnDtlMnlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
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

class Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  AmortSeq  """  
      self.SchFiscalCalendarID:str = obj["SchFiscalCalendarID"]
      """  SchFiscalCalendarID  """  
      self.SchFiscalYear:int = obj["SchFiscalYear"]
      """  SchFiscalYear  """  
      self.SchFiscalYearSuffix:str = obj["SchFiscalYearSuffix"]
      """  SchFiscalYearSuffix  """  
      self.SchFiscalPeriod:int = obj["SchFiscalPeriod"]
      """  SchFiscalPeriod  """  
      self.AmortDate:str = obj["AmortDate"]
      """  AmortDate  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  AmortPercent  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  AmortAmt  """  
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      """  DocAmortAmt  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  PostedDate  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  Rpt1AmortAmt  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Document currency  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  Rpt2AmortAmt  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  Rpt3AmortAmt  """  
      self.GLBookID:str = obj["GLBookID"]
      """  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  """  
      self.GLJournalNum:int = obj["GLJournalNum"]
      """  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  """  
      self.DispAmortAmt:int = obj["DispAmortAmt"]
      """  DispAmortAmt  """  
      self.DispDocAmortAmt:int = obj["DispDocAmortAmt"]
      """  DispDocAmortAmt  """  
      self.HasReverseLines:bool = obj["HasReverseLines"]
      """  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  Account Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMnlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Flag that indicate if the account is a curency account  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  identifies the currency for the Currency Account.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.DocTransAmt:int = obj["DocTransAmt"]
      """  Transaction amount in document currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.SkipBalances:bool = obj["SkipBalances"]
      """  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  Chart of Account ID  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full External GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the External GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartOfDual:str = obj["PartOfDual"]
      """  Possible values: 0`In~1`Out  """  
      self.ReportingModule:str = obj["ReportingModule"]
      """  Tax Journal Line reporting module.  Possible values: 0`AP~1`AR  """  
      self.TaxableAmtBookCurr:str = obj["TaxableAmtBookCurr"]
      """  Book Currency for Taxable Amount  """  
      self.TaxableAmtCurr:str = obj["TaxableAmtCurr"]
      """  Transactional Currency for Taxable Amount  """  
      self.TaxableAmtInBookCurr:int = obj["TaxableAmtInBookCurr"]
      """  Taxable Amount In Book Currency  """  
      self.TaxableAmtInTranCurr:int = obj["TaxableAmtInTranCurr"]
      """  Taxable Amount InTransactional Currency  """  
      self.TaxableLine:str = obj["TaxableLine"]
      """  Taxable Line. It is used for tax Jornal Line.  """  
      self.TaxLiability:str = obj["TaxLiability"]
      """  Tax Liability. It is used for tax Jornal Line.  """  
      self.TaxLine:bool = obj["TaxLine"]
      """  Inducate that it is Tax Journal Line  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  Tax Percent. It is used for tax Jornal Line.  """  
      self.TaxPointDate:str = obj["TaxPointDate"]
      """  Tax Point Date. It is used for tax Jornal Line.  """  
      self.TaxRate:str = obj["TaxRate"]
      """  Tax Rate. It is used for tax Jornal Line.  """  
      self.TaxType:str = obj["TaxType"]
      """  Tax Type. It is used for tax Jornal Line.  """  
      self.OverrideGLAcct:bool = obj["OverrideGLAcct"]
      """  OverrideGLAcct  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  OneTimeID  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  DeferredExp  """  
      self.DEACode:str = obj["DEACode"]
      """  DEACode  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEAStartDate  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEAEndDate  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  Malaysia Industry Code  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.LineReferenceType:str = obj["LineReferenceType"]
      """  GL Journal Line Reference Type  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.COLTaxTranType:str = obj["COLTaxTranType"]
      """  Colombia Loc Field.  """  
      self.CurrencyCodeAcctList:str = obj["CurrencyCodeAcctList"]
      self.DEAScheduled:bool = obj["DEAScheduled"]
      """  Is Deferred Expense Amortization Scheduled  """  
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.ExtRefAcctChart:str = obj["ExtRefAcctChart"]
      self.ExtRefAcctDept:str = obj["ExtRefAcctDept"]
      self.ExtRefAcctDiv:str = obj["ExtRefAcctDiv"]
      self.ExtRefCodeStatus:str = obj["ExtRefCodeStatus"]
      self.GlbGLAccountDesc:str = obj["GlbGLAccountDesc"]
      self.PartOfDualEnabled:bool = obj["PartOfDualEnabled"]
      """  Flag: true - control In/Out is enabled, else disabled  """  
      self.RateCode:str = obj["RateCode"]
      """  Colombia Loc Field.  """  
      self.RateDescription:str = obj["RateDescription"]
      """  Colombia Loc Field.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.StatAmount:int = obj["StatAmount"]
      """  Statistical Amount. UI display value.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Colombia Loc Field.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Used for Colombia CSF  """  
      self.TaxLiabilityDescr:str = obj["TaxLiabilityDescr"]
      self.TaxLiabilityTaxCodes:str = obj["TaxLiabilityTaxCodes"]
      """  The list of tax codes for Tax Liability  """  
      self.TaxRateDescr:str = obj["TaxRateDescr"]
      self.TaxTypeDescr:str = obj["TaxTypeDescr"]
      self.TaxTypeTaxRates:str = obj["TaxTypeTaxRates"]
      """  The list of tax rates for Tax code  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotCurrCredit:int = obj["TotCurrCredit"]
      self.TotCurrDebit:int = obj["TotCurrDebit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.COIsTaxLn:bool = obj["COIsTaxLn"]
      """  Colombia Loc Field.  """  
      self.LineReferenceHolder:str = obj["LineReferenceHolder"]
      """  GL Journal Line Reference Holder.  """  
      self.LineReferenceHolderName:str = obj["LineReferenceHolderName"]
      """  GL Journal Line Reference Holder Name.  """  
      self.LineReference:str = obj["LineReference"]
      """  GL Journal Line Reference.  """  
      self.RefSourceJrnLine:str = obj["RefSourceJrnLine"]
      """  Source GL Journal Line to copy reference data.  """  
      self.InvalidGLAccount:bool = obj["InvalidGLAccount"]
      """  Result of account validation. False if account is valid.  """  
      self.InvalidGLAccountMessage:str = obj["InvalidGLAccountMessage"]
      """  Result of account validation. Empty if account is valid.  """  
      self.InvalidExtGLAccount:bool = obj["InvalidExtGLAccount"]
      """  Result of external account validation. False if account is valid.  """  
      self.InvalidExtGLAccountMessage:str = obj["InvalidExtGLAccountMessage"]
      """  Result of external account validation. Empty if account is valid.  """  
      self.CorrAcctOddLine:bool = obj["CorrAcctOddLine"]
      """  Calculated field for correspondence accounting journals. Determines if the current line an odd one.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AcctCurrCurrencyID:str = obj["AcctCurrCurrencyID"]
      self.AcctCurrCurrSymbol:str = obj["AcctCurrCurrSymbol"]
      self.AcctCurrCurrDesc:str = obj["AcctCurrCurrDesc"]
      self.AcctCurrCurrName:str = obj["AcctCurrCurrName"]
      self.AcctCurrDocumentDesc:str = obj["AcctCurrDocumentDesc"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DEACodeDescRADesc:str = obj["DEACodeDescRADesc"]
      self.ExtRefCodeRefCodeDesc:str = obj["ExtRefCodeRefCodeDesc"]
      self.GLGLAcctDisp:str = obj["GLGLAcctDisp"]
      self.GLGLShortAcct:str = obj["GLGLShortAcct"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.GlRefCodeDescRefCodeDesc:str = obj["GlRefCodeDescRefCodeDesc"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMnlTranGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.GroupID:str = obj["GroupID"]
      self.BookMode:str = obj["BookMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
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

class Erp_Tablesets_GLJrnHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  """  
      self.JEDate:str = obj["JEDate"]
      """  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.Override:bool = obj["Override"]
      """  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.EnteredBy:str = obj["EnteredBy"]
      """  User ID that created the record.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  """  
      self.GlbPostedDate:str = obj["GlbPostedDate"]
      """  Date that this transaction was posted from the external company to the G/L files.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  Global Vendor ID.  Used by Multi-Company Journal.  """  
      self.GlbVendorName:str = obj["GlbVendorName"]
      """  Global Vendor Name.  Used by the Multi-Company Journal.  """  
      self.GlbAPLegalNumber:str = obj["GlbAPLegalNumber"]
      """  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  """  
      self.GlbAPInvDesc:str = obj["GlbAPInvDesc"]
      """  Global AP Invoice description.  Used by Multi-Company Journal.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.GlbJournalCodeDesc:str = obj["GlbJournalCodeDesc"]
      """  Global Journal Code Description.  """  
      self.GlbEnteredBy:str = obj["GlbEnteredBy"]
      """  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if the record was posted.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date when record was posted.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.ProcessType:int = obj["ProcessType"]
      """  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Display total debit.  """  
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Display total credit.  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowUnbalancedEntries:bool = obj["AllowUnbalancedEntries"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  """  
      self.JEDate:str = obj["JEDate"]
      """  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.Override:bool = obj["Override"]
      """  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.EnteredBy:str = obj["EnteredBy"]
      """  User ID that created the record.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  """  
      self.GlbPostedDate:str = obj["GlbPostedDate"]
      """  Date that this transaction was posted from the external company to the G/L files.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  Global Vendor ID.  Used by Multi-Company Journal.  """  
      self.GlbVendorName:str = obj["GlbVendorName"]
      """  Global Vendor Name.  Used by the Multi-Company Journal.  """  
      self.GlbAPLegalNumber:str = obj["GlbAPLegalNumber"]
      """  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  """  
      self.GlbAPInvDesc:str = obj["GlbAPInvDesc"]
      """  Global AP Invoice description.  Used by Multi-Company Journal.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.GlbJournalCodeDesc:str = obj["GlbJournalCodeDesc"]
      """  Global Journal Code Description.  """  
      self.GlbEnteredBy:str = obj["GlbEnteredBy"]
      """  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if the record was posted.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date when record was posted.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.ProcessType:int = obj["ProcessType"]
      """  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxHandling:str = obj["TaxHandling"]
      """  Tax Handling: 0 - No Tax; 1 - Journal Includes Taxes; 2 - Tax adlustment Journal  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.Statistical:bool = obj["Statistical"]
      """  Indicate, that this Journal can have only lines with Statistical Accounts. Legal Number creation for Statistical Journals should be skipped.  """  
      self.TransferredToParent:bool = obj["TransferredToParent"]
      """  TransferredToParent  """  
      self.TransferredDate:str = obj["TransferredDate"]
      """  TransferredDate  """  
      self.TransferredPerson:str = obj["TransferredPerson"]
      """  TransferredPerson  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.JournalHeld:bool = obj["JournalHeld"]
      """  If box is checked, this journal has been marked as on hold.  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Display total credit.  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Display total debit.  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableCorrAccounting:bool = obj["EnableCorrAccounting"]
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      """  Used by UI to determine if the Red Storno checkbox is to be enabled.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  """  
      self.AllowUnbalancedEntries:bool = obj["AllowUnbalancedEntries"]
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.CompanyTaxEntryMode:str = obj["CompanyTaxEntryMode"]
      self.COOneTimeDtl:bool = obj["COOneTimeDtl"]
      """  Field used for Colombia CSF  """  
      self.AllowSiteEntry:bool = obj["AllowSiteEntry"]
      """  Defines site entry allowed on journal  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlAllocationsRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      self.BookID:str = obj["BookID"]
      self.AllocID:str = obj["AllocID"]
      self.Amount:int = obj["Amount"]
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AutoBalance_input:
   """ Required : 
   GroupID
   JournalNum
   JournalLine
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The current group ID  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The current Journal Number  """  
      self.JournalLine:int = obj["JournalLine"]
      """  The current Journal Line  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class AutoBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AutoComplete_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class AutoComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AutocompleteAmortizationSchedule_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class AutocompleteAmortizationSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateAmortizationTotals_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class CalculateAmortizationTotals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateAmountForTaxLineEx_input:
   """ Required : 
   ds
   iLineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.iLineNum:int = obj["iLineNum"]
      """  Line number.  """  
      pass

class CalculateAmountForTaxLineEx_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.dAmountInBookCurr:int = obj["parameters"]
      self.dAmountInTranCurr:int = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeExtCompanyID_input:
   """ Required : 
   ProposedExtCompID
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedExtCompID:str = obj["ProposedExtCompID"]
      """  The proposed External Company ID  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeExtCompanyID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExtGlAcct_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeExtGlAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGlAcct1_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeGlAcct1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.currCodeChanged:bool = obj["currCodeChanged"]
      pass

      """  output parameters  """  

class ChangeGlRefCode_input:
   """ Required : 
   ProposedRefCode
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedRefCode:str = obj["ProposedRefCode"]
      """  The proposed G/L Reference Code  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeGlRefCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLinkedLineAmnts_input:
   """ Required : 
   iLineNum
   updateTaxableOnly
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.updateTaxableOnly:bool = obj["updateTaxableOnly"]
      """  Indicates if only the taxable amount will be updated  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeLinkedLineAmnts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMultiCompany_input:
   """ Required : 
   ProposedMulti
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedMulti:bool = obj["ProposedMulti"]
      """  The proposed Multi-Company flag  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal line number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeMultiCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeReverse_input:
   """ Required : 
   ProposedReverse
   ds
   """  
   def __init__(self, obj):
      self.ProposedReverse:bool = obj["ProposedReverse"]
      """  The proposed Reverse value  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ChangeReverse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxCode_input:
   """ Required : 
   ipTaxCode
   """  
   def __init__(self, obj):
      self.ipTaxCode:str = obj["ipTaxCode"]
      """  TaxCode id  """  
      pass

class ChangeTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRateCode:str = obj["parameters"]
      self.opRateDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckAllocations_input:
   """ Required : 
   ipBookID
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  The current COACode  """  
      pass

class CheckAllocations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opAlloc:bool = obj["opAlloc"]
      pass

      """  output parameters  """  

class CheckCurrencyAccount2_input:
   """ Required : 
   ipCOACode
   ipSegValue
   ipCurrency
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA code  """  
      self.ipSegValue:str = obj["ipSegValue"]
      """  Segment value  """  
      self.ipCurrency:str = obj["ipCurrency"]
      """  Transactional currency  """  
      pass

class CheckCurrencyAccount2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrAcct:bool = obj["opCurrAcct"]
      pass

      """  output parameters  """  

class CheckCurrencyAccountExt_input:
   """ Required : 
   ds
   iLineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.iLineNum:int = obj["iLineNum"]
      """  lineNum  """  
      pass

class CheckCurrencyAccountExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCurrencyAccountForTaxLine_input:
   """ Required : 
   ipBookID
   ipJournalCode
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalCalendarID
   ipJournalNum
   ipCurrCode
   ipTaxableLine
   ipCOACode
   ipSegValue
   ipPublishEx
   ipGLAccount
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  """  
      self.ipJournalCode:str = obj["ipJournalCode"]
      """  Journal code  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Fiscal Calendar  """  
      self.ipJournalNum:int = obj["ipJournalNum"]
      """  Journal number  """  
      self.ipCurrCode:str = obj["ipCurrCode"]
      """  Book currency code  """  
      self.ipTaxableLine:str = obj["ipTaxableLine"]
      """  Taxable line number  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA code  """  
      self.ipSegValue:str = obj["ipSegValue"]
      """  Segment value  """  
      self.ipPublishEx:bool = obj["ipPublishEx"]
      """  True - raise exeption if error  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      pass

class CheckCurrencyAccountForTaxLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrAcct:bool = obj["opCurrAcct"]
      self.opTranCurrCode:str = obj["parameters"]
      self.opTranCurrDescr:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCurrencyAccount_input:
   """ Required : 
   ipCOACode
   ipSegValue
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  The current COACode  """  
      self.ipSegValue:str = obj["ipSegValue"]
      """  The current segment value one  """  
      pass

class CheckCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurr:bool = obj["opCurr"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   keyValue2
   keyValue3
   keyValue4
   keyValue5
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  GroupID  """  
      self.keyValue2:str = obj["keyValue2"]
      """  BookID  """  
      self.keyValue3:str = obj["keyValue3"]
      """  FiscalYear  """  
      self.keyValue4:str = obj["keyValue4"]
      """  JournalCode  """  
      self.keyValue5:str = obj["keyValue5"]
      """  JournalNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckDtlBeforeUpdate_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class CheckDtlBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.OpMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPartOfDual_input:
   """ Required : 
   cPartOfDual
   """  
   def __init__(self, obj):
      self.cPartOfDual:str = obj["cPartOfDual"]
      """  In/Out value  """  
      pass

class CheckPartOfDual_output:
   def __init__(self, obj):
      pass

class CheckReportingModule_input:
   """ Required : 
   cReportingModule
   ipTaxLiability
   """  
   def __init__(self, obj):
      self.cReportingModule:str = obj["cReportingModule"]
      """  Reporting Module value  """  
      self.ipTaxLiability:str = obj["ipTaxLiability"]
      """  Tax Liability code  """  
      pass

class CheckReportingModule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckStatUOMAccount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class CheckStatUOMAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTaxAmountSign_input:
   """ Required : 
   ipBookID
   ipJournalCode
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalCalendarID
   ipJournalNum
   ipJournalLine
   ipTaxType
   ipTaxRate
   ipPartOfDual
   ipTaxableLine
   ipTaxableAmountStatus
   ipTaxAmountStatus
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID value  """  
      self.ipJournalCode:str = obj["ipJournalCode"]
      """  Jornal code  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Fiscal calendar ID  """  
      self.ipJournalNum:int = obj["ipJournalNum"]
      """  Journal number  """  
      self.ipJournalLine:int = obj["ipJournalLine"]
      """  Journal line number  """  
      self.ipTaxType:str = obj["ipTaxType"]
      """  Tax code  """  
      self.ipTaxRate:str = obj["ipTaxRate"]
      """  Tax rate code  """  
      self.ipPartOfDual:str = obj["ipPartOfDual"]
      """  In/Out value  """  
      self.ipTaxableLine:str = obj["ipTaxableLine"]
      """  Taxable line number  """  
      self.ipTaxableAmountStatus:int = obj["ipTaxableAmountStatus"]
      """  Taxable amount status: -1(credit)/ 1(debit)/ 0(not calculated)  """  
      self.ipTaxAmountStatus:int = obj["ipTaxAmountStatus"]
      """  Tax amount status: -1(credit)/ 1(debit)/ 0(not calculated)  """  
      pass

class CheckTaxAmountSign_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTaxLiability_input:
   """ Required : 
   cTaxLiabilityCode
   """  
   def __init__(self, obj):
      self.cTaxLiabilityCode:str = obj["cTaxLiabilityCode"]
      """  Tax Liability code  """  
      pass

class CheckTaxLiability_output:
   def __init__(self, obj):
      pass

class CheckTaxPointDate_input:
   """ Required : 
   cTaxTypeCode
   cTaxRateCode
   dTaxPointDate
   """  
   def __init__(self, obj):
      self.cTaxTypeCode:str = obj["cTaxTypeCode"]
      """  Tax Type code  """  
      self.cTaxRateCode:str = obj["cTaxRateCode"]
      """  Tax Rate code  """  
      self.dTaxPointDate:str = obj["dTaxPointDate"]
      """  Tax point date  """  
      pass

class CheckTaxPointDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTaxRate_input:
   """ Required : 
   cTaxTypeCode
   cTaxRateCode
   dTaxPointDate
   """  
   def __init__(self, obj):
      self.cTaxTypeCode:str = obj["cTaxTypeCode"]
      """  Tax Type code  """  
      self.cTaxRateCode:str = obj["cTaxRateCode"]
      """  ax Rate code  """  
      self.dTaxPointDate:str = obj["dTaxPointDate"]
      """  Tax point date  """  
      pass

class CheckTaxRate_output:
   def __init__(self, obj):
      pass

class CheckTaxType_input:
   """ Required : 
   cTaxLiabilityCode
   cTaxTypeCode
   """  
   def __init__(self, obj):
      self.cTaxLiabilityCode:str = obj["cTaxLiabilityCode"]
      """  Tax Liability code  """  
      self.cTaxTypeCode:str = obj["cTaxTypeCode"]
      """  Tax Type code  """  
      pass

class CheckTaxType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTaxableLine_input:
   """ Required : 
   ipBookID
   ipJournalCode
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalCalendarID
   ipJournalNum
   ipJournalLine
   ipCurrCode
   ipTaxableLine
   ipCOACode
   ipSegValue
   ipGLAccount
   ipTaxType
   ipTaxRate
   ipPartOfDual
   ipTaxAmountStatus
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID value  """  
      self.ipJournalCode:str = obj["ipJournalCode"]
      """  Jornal code  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Fiscal calendar ID  """  
      self.ipJournalNum:int = obj["ipJournalNum"]
      """  Journal number  """  
      self.ipJournalLine:int = obj["ipJournalLine"]
      """  Journal line number  """  
      self.ipCurrCode:str = obj["ipCurrCode"]
      """  Book currency code  """  
      self.ipTaxableLine:str = obj["ipTaxableLine"]
      """  Taxable line number  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA code  """  
      self.ipSegValue:str = obj["ipSegValue"]
      """  Segment value  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ipTaxType:str = obj["ipTaxType"]
      """  Tax code  """  
      self.ipTaxRate:str = obj["ipTaxRate"]
      """  Tax rate code  """  
      self.ipPartOfDual:str = obj["ipPartOfDual"]
      """  In/Out value  """  
      self.ipTaxAmountStatus:int = obj["ipTaxAmountStatus"]
      """  Tax amount status: -1(credit)/ 1(debit)/ 0(not calculated)  """  
      pass

class CheckTaxableLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ConvertCreditAmount_input:
   """ Required : 
   proposedAmount
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.proposedAmount:int = obj["proposedAmount"]
      """  The proposed  Amount  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ConvertCreditAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertDebitAmount_input:
   """ Required : 
   proposedAmount
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.proposedAmount:int = obj["proposedAmount"]
      """  The proposed  Amount  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ConvertDebitAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateDetailLineFromAllocation_input:
   """ Required : 
   ds
   journalNum
   groupID
   allocID
   allocAmount
   allocGLAccount
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.journalNum:int = obj["journalNum"]
      """  Current Journal Number  """  
      self.groupID:str = obj["groupID"]
      """  Current Group ID  """  
      self.allocID:str = obj["allocID"]
      """  Selected Allocation ID  """  
      self.allocAmount:int = obj["allocAmount"]
      """  Selected Allocation Amount  """  
      self.allocGLAccount:str = obj["allocGLAccount"]
      """  Selected Allocation Account  """  
      pass

class CreateDetailLineFromAllocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteAmortizationSchedule_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class DeleteAmortizationSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLJournalEntryTableset:
   def __init__(self, obj):
      self.GLJrnHed:list[Erp_Tablesets_GLJrnHedRow] = obj["GLJrnHed"]
      self.GLJrnHedAttch:list[Erp_Tablesets_GLJrnHedAttchRow] = obj["GLJrnHedAttch"]
      self.GLJrnDtlMnl:list[Erp_Tablesets_GLJrnDtlMnlRow] = obj["GLJrnDtlMnl"]
      self.GLJrnDtlMnlAttch:list[Erp_Tablesets_GLJrnDtlMnlAttchRow] = obj["GLJrnDtlMnlAttch"]
      self.GLJrnDtlMnlDEASch:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["GLJrnDtlMnlDEASch"]
      self.GLJrnDtlMnlTranGLC:list[Erp_Tablesets_GLJrnDtlMnlTranGLCRow] = obj["GLJrnDtlMnlTranGLC"]
      self.GlAllocations:list[Erp_Tablesets_GlAllocationsRow] = obj["GlAllocations"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnDtlMnlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
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

class Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  AmortSeq  """  
      self.SchFiscalCalendarID:str = obj["SchFiscalCalendarID"]
      """  SchFiscalCalendarID  """  
      self.SchFiscalYear:int = obj["SchFiscalYear"]
      """  SchFiscalYear  """  
      self.SchFiscalYearSuffix:str = obj["SchFiscalYearSuffix"]
      """  SchFiscalYearSuffix  """  
      self.SchFiscalPeriod:int = obj["SchFiscalPeriod"]
      """  SchFiscalPeriod  """  
      self.AmortDate:str = obj["AmortDate"]
      """  AmortDate  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  AmortPercent  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  AmortAmt  """  
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      """  DocAmortAmt  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  PostedDate  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  Rpt1AmortAmt  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Document currency  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  Rpt2AmortAmt  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  Rpt3AmortAmt  """  
      self.GLBookID:str = obj["GLBookID"]
      """  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  """  
      self.GLJournalNum:int = obj["GLJournalNum"]
      """  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  """  
      self.DispAmortAmt:int = obj["DispAmortAmt"]
      """  DispAmortAmt  """  
      self.DispDocAmortAmt:int = obj["DispDocAmortAmt"]
      """  DispDocAmortAmt  """  
      self.HasReverseLines:bool = obj["HasReverseLines"]
      """  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  Account Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMnlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Flag that indicate if the account is a curency account  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  identifies the currency for the Currency Account.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.DocTransAmt:int = obj["DocTransAmt"]
      """  Transaction amount in document currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.SkipBalances:bool = obj["SkipBalances"]
      """  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  Chart of Account ID  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full External GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the External GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartOfDual:str = obj["PartOfDual"]
      """  Possible values: 0`In~1`Out  """  
      self.ReportingModule:str = obj["ReportingModule"]
      """  Tax Journal Line reporting module.  Possible values: 0`AP~1`AR  """  
      self.TaxableAmtBookCurr:str = obj["TaxableAmtBookCurr"]
      """  Book Currency for Taxable Amount  """  
      self.TaxableAmtCurr:str = obj["TaxableAmtCurr"]
      """  Transactional Currency for Taxable Amount  """  
      self.TaxableAmtInBookCurr:int = obj["TaxableAmtInBookCurr"]
      """  Taxable Amount In Book Currency  """  
      self.TaxableAmtInTranCurr:int = obj["TaxableAmtInTranCurr"]
      """  Taxable Amount InTransactional Currency  """  
      self.TaxableLine:str = obj["TaxableLine"]
      """  Taxable Line. It is used for tax Jornal Line.  """  
      self.TaxLiability:str = obj["TaxLiability"]
      """  Tax Liability. It is used for tax Jornal Line.  """  
      self.TaxLine:bool = obj["TaxLine"]
      """  Inducate that it is Tax Journal Line  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  Tax Percent. It is used for tax Jornal Line.  """  
      self.TaxPointDate:str = obj["TaxPointDate"]
      """  Tax Point Date. It is used for tax Jornal Line.  """  
      self.TaxRate:str = obj["TaxRate"]
      """  Tax Rate. It is used for tax Jornal Line.  """  
      self.TaxType:str = obj["TaxType"]
      """  Tax Type. It is used for tax Jornal Line.  """  
      self.OverrideGLAcct:bool = obj["OverrideGLAcct"]
      """  OverrideGLAcct  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  OneTimeID  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  DeferredExp  """  
      self.DEACode:str = obj["DEACode"]
      """  DEACode  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEAStartDate  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEAEndDate  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  Malaysia Industry Code  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.LineReferenceType:str = obj["LineReferenceType"]
      """  GL Journal Line Reference Type  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.COLTaxTranType:str = obj["COLTaxTranType"]
      """  Colombia Loc Field.  """  
      self.CurrencyCodeAcctList:str = obj["CurrencyCodeAcctList"]
      self.DEAScheduled:bool = obj["DEAScheduled"]
      """  Is Deferred Expense Amortization Scheduled  """  
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.ExtRefAcctChart:str = obj["ExtRefAcctChart"]
      self.ExtRefAcctDept:str = obj["ExtRefAcctDept"]
      self.ExtRefAcctDiv:str = obj["ExtRefAcctDiv"]
      self.ExtRefCodeStatus:str = obj["ExtRefCodeStatus"]
      self.GlbGLAccountDesc:str = obj["GlbGLAccountDesc"]
      self.PartOfDualEnabled:bool = obj["PartOfDualEnabled"]
      """  Flag: true - control In/Out is enabled, else disabled  """  
      self.RateCode:str = obj["RateCode"]
      """  Colombia Loc Field.  """  
      self.RateDescription:str = obj["RateDescription"]
      """  Colombia Loc Field.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.StatAmount:int = obj["StatAmount"]
      """  Statistical Amount. UI display value.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Colombia Loc Field.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Used for Colombia CSF  """  
      self.TaxLiabilityDescr:str = obj["TaxLiabilityDescr"]
      self.TaxLiabilityTaxCodes:str = obj["TaxLiabilityTaxCodes"]
      """  The list of tax codes for Tax Liability  """  
      self.TaxRateDescr:str = obj["TaxRateDescr"]
      self.TaxTypeDescr:str = obj["TaxTypeDescr"]
      self.TaxTypeTaxRates:str = obj["TaxTypeTaxRates"]
      """  The list of tax rates for Tax code  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotCurrCredit:int = obj["TotCurrCredit"]
      self.TotCurrDebit:int = obj["TotCurrDebit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.COIsTaxLn:bool = obj["COIsTaxLn"]
      """  Colombia Loc Field.  """  
      self.LineReferenceHolder:str = obj["LineReferenceHolder"]
      """  GL Journal Line Reference Holder.  """  
      self.LineReferenceHolderName:str = obj["LineReferenceHolderName"]
      """  GL Journal Line Reference Holder Name.  """  
      self.LineReference:str = obj["LineReference"]
      """  GL Journal Line Reference.  """  
      self.RefSourceJrnLine:str = obj["RefSourceJrnLine"]
      """  Source GL Journal Line to copy reference data.  """  
      self.InvalidGLAccount:bool = obj["InvalidGLAccount"]
      """  Result of account validation. False if account is valid.  """  
      self.InvalidGLAccountMessage:str = obj["InvalidGLAccountMessage"]
      """  Result of account validation. Empty if account is valid.  """  
      self.InvalidExtGLAccount:bool = obj["InvalidExtGLAccount"]
      """  Result of external account validation. False if account is valid.  """  
      self.InvalidExtGLAccountMessage:str = obj["InvalidExtGLAccountMessage"]
      """  Result of external account validation. Empty if account is valid.  """  
      self.CorrAcctOddLine:bool = obj["CorrAcctOddLine"]
      """  Calculated field for correspondence accounting journals. Determines if the current line an odd one.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AcctCurrCurrencyID:str = obj["AcctCurrCurrencyID"]
      self.AcctCurrCurrSymbol:str = obj["AcctCurrCurrSymbol"]
      self.AcctCurrCurrDesc:str = obj["AcctCurrCurrDesc"]
      self.AcctCurrCurrName:str = obj["AcctCurrCurrName"]
      self.AcctCurrDocumentDesc:str = obj["AcctCurrDocumentDesc"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DEACodeDescRADesc:str = obj["DEACodeDescRADesc"]
      self.ExtRefCodeRefCodeDesc:str = obj["ExtRefCodeRefCodeDesc"]
      self.GLGLAcctDisp:str = obj["GLGLAcctDisp"]
      self.GLGLShortAcct:str = obj["GLGLShortAcct"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.GlRefCodeDescRefCodeDesc:str = obj["GlRefCodeDescRefCodeDesc"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMnlTranGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.GroupID:str = obj["GroupID"]
      self.BookMode:str = obj["BookMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
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

class Erp_Tablesets_GLJrnHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  """  
      self.JEDate:str = obj["JEDate"]
      """  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.Override:bool = obj["Override"]
      """  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.EnteredBy:str = obj["EnteredBy"]
      """  User ID that created the record.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  """  
      self.GlbPostedDate:str = obj["GlbPostedDate"]
      """  Date that this transaction was posted from the external company to the G/L files.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  Global Vendor ID.  Used by Multi-Company Journal.  """  
      self.GlbVendorName:str = obj["GlbVendorName"]
      """  Global Vendor Name.  Used by the Multi-Company Journal.  """  
      self.GlbAPLegalNumber:str = obj["GlbAPLegalNumber"]
      """  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  """  
      self.GlbAPInvDesc:str = obj["GlbAPInvDesc"]
      """  Global AP Invoice description.  Used by Multi-Company Journal.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.GlbJournalCodeDesc:str = obj["GlbJournalCodeDesc"]
      """  Global Journal Code Description.  """  
      self.GlbEnteredBy:str = obj["GlbEnteredBy"]
      """  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if the record was posted.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date when record was posted.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.ProcessType:int = obj["ProcessType"]
      """  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Display total debit.  """  
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Display total credit.  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowUnbalancedEntries:bool = obj["AllowUnbalancedEntries"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnHedListTableset:
   def __init__(self, obj):
      self.GLJrnHedList:list[Erp_Tablesets_GLJrnHedListRow] = obj["GLJrnHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year for this journal transaction header. Assigned from GLJrnGrp.FiscalYear.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system.  The Journal Number is a way of relating the detail entries into a group that would normally balance.  When we need to assign a new number the system  finds the journalnum of the last record (GLJrnDtl) for the fiscal year and adds one.  When creating GLJrnDtl from other modules this number is assigned note that this find last is performed on the GLJrnDtl because the GLJrnHed records only exist until the group is posted.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction.  Used as a default for the GLJrnDtl.Description field.  """  
      self.JEDate:str = obj["JEDate"]
      """  The Date for this journal transaction entry.  Defaulted from GLJrnGrp.JEDate.  Can be overridden during entry, but it must be a valid date for the fiscal period that is assigned to this group.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLJrnDtl.TranAmt in the related GLJrnDtl records.  Primarily used for visual verification.  """  
      self.Override:bool = obj["Override"]
      """  Indicates that this is a non-balancing journal entry that the user indicated is valid to post.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.EnteredBy:str = obj["EnteredBy"]
      """  User ID that created the record.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this journal transaction set should create reversing entries for the next fiscal period.  This happens during the posting process.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that journal lines appearing under this journal header may have multi-company journals entered at the target external company.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  """  
      self.GlbPostedDate:str = obj["GlbPostedDate"]
      """  Date that this transaction was posted from the external company to the G/L files.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  Global Vendor ID.  Used by Multi-Company Journal.  """  
      self.GlbVendorName:str = obj["GlbVendorName"]
      """  Global Vendor Name.  Used by the Multi-Company Journal.  """  
      self.GlbAPLegalNumber:str = obj["GlbAPLegalNumber"]
      """  Legal Number used by the source AP Invoice.  Used by the Multi-Company Journal.  """  
      self.GlbAPInvDesc:str = obj["GlbAPInvDesc"]
      """  Global AP Invoice description.  Used by Multi-Company Journal.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.GlbJournalCodeDesc:str = obj["GlbJournalCodeDesc"]
      """  Global Journal Code Description.  """  
      self.GlbEnteredBy:str = obj["GlbEnteredBy"]
      """  User ID that created the Multi-Company Journal record from the source company.  This may not be a valid UserId in the target company.  Used by the Multi-Company GJ and AP.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  if yes it means that during posting for each line debit and credit amounts should be saved with opposite signs.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if the record was posted.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date when record was posted.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.ProcessType:int = obj["ProcessType"]
      """  0 - Manual Entry; 1 - Revaluation Process; 2 - Consolidation Process.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxHandling:str = obj["TaxHandling"]
      """  Tax Handling: 0 - No Tax; 1 - Journal Includes Taxes; 2 - Tax adlustment Journal  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.Statistical:bool = obj["Statistical"]
      """  Indicate, that this Journal can have only lines with Statistical Accounts. Legal Number creation for Statistical Journals should be skipped.  """  
      self.TransferredToParent:bool = obj["TransferredToParent"]
      """  TransferredToParent  """  
      self.TransferredDate:str = obj["TransferredDate"]
      """  TransferredDate  """  
      self.TransferredPerson:str = obj["TransferredPerson"]
      """  TransferredPerson  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.JournalHeld:bool = obj["JournalHeld"]
      """  If box is checked, this journal has been marked as on hold.  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Display total credit.  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Display total debit.  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableCorrAccounting:bool = obj["EnableCorrAccounting"]
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      """  Used by UI to determine if the Red Storno checkbox is to be enabled.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  """  
      self.AllowUnbalancedEntries:bool = obj["AllowUnbalancedEntries"]
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.CompanyTaxEntryMode:str = obj["CompanyTaxEntryMode"]
      self.COOneTimeDtl:bool = obj["COOneTimeDtl"]
      """  Field used for Colombia CSF  """  
      self.AllowSiteEntry:bool = obj["AllowSiteEntry"]
      """  Defines site entry allowed on journal  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlAllocationsRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      self.BookID:str = obj["BookID"]
      self.AllocID:str = obj["AllocID"]
      self.Amount:int = obj["Amount"]
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtGLJournalEntryTableset:
   def __init__(self, obj):
      self.GLJrnHed:list[Erp_Tablesets_GLJrnHedRow] = obj["GLJrnHed"]
      self.GLJrnHedAttch:list[Erp_Tablesets_GLJrnHedAttchRow] = obj["GLJrnHedAttch"]
      self.GLJrnDtlMnl:list[Erp_Tablesets_GLJrnDtlMnlRow] = obj["GLJrnDtlMnl"]
      self.GLJrnDtlMnlAttch:list[Erp_Tablesets_GLJrnDtlMnlAttchRow] = obj["GLJrnDtlMnlAttch"]
      self.GLJrnDtlMnlDEASch:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["GLJrnDtlMnlDEASch"]
      self.GLJrnDtlMnlTranGLC:list[Erp_Tablesets_GLJrnDtlMnlTranGLCRow] = obj["GLJrnDtlMnlTranGLC"]
      self.GlAllocations:list[Erp_Tablesets_GlAllocationsRow] = obj["GlAllocations"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenLegalNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class GenLegalNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateAmortizationSchedule_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class GenerateAmortizationSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAllocations_input:
   """ Required : 
   bookID
   ds
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class GetAllocations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailableCurrencies_input:
   """ Required : 
   ipCOACode
   ipSegValue
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSegValue:str = obj["ipSegValue"]
      pass

class GetAvailableCurrencies_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetByGroupID_input:
   """ Required : 
   GroupID
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  Current Group ID  """  
      pass

class GetByGroupID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJournalEntryTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJournalEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLJournalEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLJournalEntryTableset] = obj["returnObj"]
      pass

class GetDefaultAccount_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class GetDefaultAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_GLJrnHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnlAttch_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   journalLine
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetNewGLJrnDtlMnlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnlDEASchPopulated_input:
   """ Required : 
   ds
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetNewGLJrnDtlMnlDEASchPopulated_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnlDEASch_input:
   """ Required : 
   ds
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   glBookID
   journalCode
   glJournalNum
   journalLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.glBookID:str = obj["glBookID"]
      self.journalCode:str = obj["journalCode"]
      self.glJournalNum:int = obj["glJournalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetNewGLJrnDtlMnlDEASch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnlTranGLC_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class GetNewGLJrnDtlMnlTranGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnl_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   journalLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetNewGLJrnDtlMnl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnHedAttch_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetNewGLJrnHedAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnHed_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      pass

class GetNewGLJrnHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlJrnHedTran_input:
   """ Required : 
   ds
   GroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.GroupID:str = obj["GroupID"]
      """  Current Group ID  """  
      pass

class GetNewGlJrnHedTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewStatisticalGLJrnHed_input:
   """ Required : 
   ds
   GroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.GroupID:str = obj["GroupID"]
      pass

class GetNewStatisticalGLJrnHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRefSourceJrnLineList_input:
   """ Required : 
   guid
   """  
   def __init__(self, obj):
      self.guid:str = obj["guid"]
      """  Current Journal Line guid  """  
      pass

class GetRefSourceJrnLineList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseGLJrnHed
   whereClauseGLJrnHedAttch
   whereClauseGLJrnDtlMnl
   whereClauseGLJrnDtlMnlAttch
   whereClauseGLJrnDtlMnlDEASch
   whereClauseGLJrnDtlMnlTranGLC
   whereClauseGlAllocations
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLJrnHed:str = obj["whereClauseGLJrnHed"]
      self.whereClauseGLJrnHedAttch:str = obj["whereClauseGLJrnHedAttch"]
      self.whereClauseGLJrnDtlMnl:str = obj["whereClauseGLJrnDtlMnl"]
      self.whereClauseGLJrnDtlMnlAttch:str = obj["whereClauseGLJrnDtlMnlAttch"]
      self.whereClauseGLJrnDtlMnlDEASch:str = obj["whereClauseGLJrnDtlMnlDEASch"]
      self.whereClauseGLJrnDtlMnlTranGLC:str = obj["whereClauseGLJrnDtlMnlTranGLC"]
      self.whereClauseGlAllocations:str = obj["whereClauseGlAllocations"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJournalEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaxEntryMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMode:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTaxRatesList_input:
   """ Required : 
   cTaxType
   dTaxPointDate
   """  
   def __init__(self, obj):
      self.cTaxType:str = obj["cTaxType"]
      """  Tax type  """  
      self.dTaxPointDate:str = obj["dTaxPointDate"]
      """  Tax point date  """  
      pass

class GetTaxRatesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cTaxRatesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTaxTypesList_input:
   """ Required : 
   cTaxLiability
   """  
   def __init__(self, obj):
      self.cTaxLiability:str = obj["cTaxLiability"]
      """  Tax Liability.  """  
      pass

class GetTaxTypesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cTaxTypesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTaxaHandlingList_input:
   """ Required : 
   ipCompanyTaxEntryMode
   """  
   def __init__(self, obj):
      self.ipCompanyTaxEntryMode:str = obj["ipCompanyTaxEntryMode"]
      pass

class GetTaxaHandlingList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTaxableLinesListWithParams_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   ipJournalCode
   ipJournalNum
   ipJournalLine
   ipFiscalCalendarID
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipJournalCode:str = obj["ipJournalCode"]
      self.ipJournalNum:int = obj["ipJournalNum"]
      self.ipJournalLine:int = obj["ipJournalLine"]
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      pass

class GetTaxableLinesListWithParams_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTaxableLinesList_input:
   """ Required : 
   guid
   """  
   def __init__(self, obj):
      self.guid:str = obj["guid"]
      """  Current Journal Line guid  """  
      pass

class GetTaxableLinesList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class OnChangeCurrencyAcct_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeCurrencyAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDEAScheduleLineAmount_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   amortSeq
   srcField
   propValue
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.amortSeq:int = obj["amortSeq"]
      self.srcField:str = obj["srcField"]
      self.propValue:int = obj["propValue"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeDEAScheduleLineAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDEAScheduleLineFiscalPeriod_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   amortSeq
   srcField
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.amortSeq:int = obj["amortSeq"]
      self.srcField:str = obj["srcField"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeDEAScheduleLineFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLineDEAAccount_input:
   """ Required : 
   glJournalDtlMnlSysRowID
   segValue1
   ds
   """  
   def __init__(self, obj):
      self.glJournalDtlMnlSysRowID:str = obj["glJournalDtlMnlSysRowID"]
      self.segValue1:str = obj["segValue1"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeLineDEAAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLineDEACode_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   deaCode
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.deaCode:str = obj["deaCode"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeLineDEACode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLineDEAStartDate_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   startDate
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.startDate:str = obj["startDate"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeLineDEAStartDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLineDefferedExp_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   bookID
   journalCode
   journalNum
   journalLine
   ipDefExp
   ds
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.bookID:str = obj["bookID"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      self.ipDefExp:bool = obj["ipDefExp"]
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeLineDefferedExp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLineReferenceHolder_input:
   """ Required : 
   proposedRefHolder
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.proposedRefHolder:str = obj["proposedRefHolder"]
      """  proposed Reference Holder  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeLineReferenceHolder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLineReference_input:
   """ Required : 
   proposedReference
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.proposedReference:str = obj["proposedReference"]
      """  proposed Reference  """  
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeLineReference_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxLiability_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeTaxLiability_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxRate_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeTaxRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxType_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeTaxType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxableAmntInTranCurr_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeTaxableAmntInTranCurr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxableLine_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeTaxableLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class OnChangeTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreGenLegalNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class PreGenLegalNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class ResetMYIndustryCode_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class ResetMYIndustryCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetDefaultsForTaxLine_input:
   """ Required : 
   iLineNum
   ds
   """  
   def __init__(self, obj):
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class SetDefaultsForTaxLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateAmountForTaxLine_input:
   """ Required : 
   ds
   iLineNum
   dAmountInBookCurr
   dAmountInTranCurr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.iLineNum:int = obj["iLineNum"]
      """  Journal Line Number  """  
      self.dAmountInBookCurr:int = obj["dAmountInBookCurr"]
      """  Line amount in book currency.  """  
      self.dAmountInTranCurr:int = obj["dAmountInTranCurr"]
      """  Line amount in transactional currency.  """  
      pass

class UpdateAmountForTaxLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLJournalEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLJournalEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAccountForAllocation_input:
   """ Required : 
   ipCOACode
   ipSegValue1
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COACode  """  
      self.ipSegValue1:str = obj["ipSegValue1"]
      """  SegValue1  """  
      pass

class ValidateAccountForAllocation_output:
   def __init__(self, obj):
      pass

class ValidateAccountForStatJournal_input:
   """ Required : 
   ipCOACode
   ipSegValue1
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COACode  """  
      self.ipSegValue1:str = obj["ipSegValue1"]
      """  SegValue1  """  
      pass

class ValidateAccountForStatJournal_output:
   def __init__(self, obj):
      pass

class ValidateCurrencyAccount_input:
   """ Required : 
   ds
   ipCurrency
   lineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.ipCurrency:str = obj["ipCurrency"]
      """  The proposed Currency value  """  
      self.lineNum:int = obj["lineNum"]
      """  Lournal Line  """  
      pass

class ValidateCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ipVoidedReason
   ds
   """  
   def __init__(self, obj):
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJournalEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

