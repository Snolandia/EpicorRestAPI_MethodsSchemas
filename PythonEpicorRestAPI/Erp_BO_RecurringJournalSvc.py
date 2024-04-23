import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RecurringJournalSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RecurringJournals(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RecurringJournals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RecurringJournals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals",headers=creds) as resp:
           return await resp.json()

async def post_RecurringJournals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RecurringJournals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RecurringJournals_Company_RecurNum(Company, RecurNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RecurringJournal item
   Description: Calls GetByID to retrieve the RecurringJournal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RecurringJournal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RecurringJournals_Company_RecurNum(Company, RecurNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RecurringJournal for the service
   Description: Calls UpdateExt to update RecurringJournal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RecurringJournal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRecHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RecurringJournals_Company_RecurNum(Company, RecurNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RecurringJournal item
   Description: Call UpdateExt to delete RecurringJournal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RecurringJournal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RecurringJournals_Company_RecurNum_GLRecDtls(Company, RecurNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLRecDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRecDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecDtls",headers=creds) as resp:
           return await resp.json()

async def get_RecurringJournals_Company_RecurNum_GLRecDtls_Company_RecurNum_RecurLine(Company, RecurNum, RecurLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRecDtl item
   Description: Calls GetByID to retrieve the GLRecDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param RecurLine: Desc: RecurLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RecurringJournals_Company_RecurNum_GLRecScheds(Company, RecurNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLRecScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRecScheds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecScheds",headers=creds) as resp:
           return await resp.json()

async def get_RecurringJournals_Company_RecurNum_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, RecurNum, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRecSched item
   Description: Calls GetByID to retrieve the GLRecSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecSched1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/RecurringJournals(" + Company + "," + RecurNum + ")/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLRecDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLRecDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRecDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls",headers=creds) as resp:
           return await resp.json()

async def post_GLRecDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRecDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLRecDtls_Company_RecurNum_RecurLine(Company, RecurNum, RecurLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRecDtl item
   Description: Calls GetByID to retrieve the GLRecDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param RecurLine: Desc: RecurLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLRecDtls_Company_RecurNum_RecurLine(Company, RecurNum, RecurLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLRecDtl for the service
   Description: Calls UpdateExt to update GLRecDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRecDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param RecurLine: Desc: RecurLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRecDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLRecDtls_Company_RecurNum_RecurLine(Company, RecurNum, RecurLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLRecDtl item
   Description: Call UpdateExt to delete GLRecDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRecDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param RecurLine: Desc: RecurLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecDtls(" + Company + "," + RecurNum + "," + RecurLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLRecScheds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLRecScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRecScheds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds",headers=creds) as resp:
           return await resp.json()

async def post_GLRecScheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRecScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, RecurNum, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRecSched item
   Description: Calls GetByID to retrieve the GLRecSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRecSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, RecurNum, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLRecSched for the service
   Description: Calls UpdateExt to update GLRecSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRecSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRecSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLRecScheds_Company_RecurNum_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, RecurNum, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLRecSched item
   Description: Call UpdateExt to delete GLRecSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRecSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecurNum: Desc: RecurNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/GLRecScheds(" + Company + "," + RecurNum + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRecHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLRecHed, whereClauseGLRecDtl, whereClauseGLRecSched, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLRecHed=" + whereClauseGLRecHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLRecDtl=" + whereClauseGLRecDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLRecSched=" + whereClauseGLRecSched
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(recurNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "recurNum=" + recurNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AutoBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoBalance
   Description: This method does Auto Balance for Recurring Journal record with number recurNum
and with line recurLine.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBookID
   Description: This method updates the Fiscal Calendar when the book changes.  Book can be blank.
A blank book indicates use of the company fiscal calendar.
   OperationID: ChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEntryMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEntryMode
   Description: Method to call when changing the Entry Mode.
   OperationID: ChangeEntryMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGlAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGlAcct
   Description: This method resets the G/L Reference Type and Code when the G/L
Account changes.  Depending on the new GL account, the Reference Type/Code
can become mandatory or optional.  Make sure to call the GetMaskRefCodes method
of the GLRefTypBusiness Object to get the new list of all GL Reference Codes
related to the entered Account number.  This method will also return values for
GlRecDtl.RefCodeStatus and GlRecDtl.RefAcctDiv/RefAcctDept/RefAcctChart. Enable
update of GlRecDtl.GLRefCode if the value returned for RefCodeStatus is either "M"
for Mandatory or "O" for Optional.
   OperationID: ChangeGlAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateType
   Description: Method to call when changing the Rate Type.
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBalance
   Description: Before updating the GlRecHed record, CheckBalance will have to be called.
The CheckBalance method will check to make sure the TotCredit and TotDebit
fields are equal.
   OperationID: CheckBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyAccount
   Description: This procudura validata if the Account is a currency Account
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyAccountExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyAccountExt
   Description: This procudure validate if the Account is a currency Account, define list of available currencies.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckStatUOMAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckStatUOMAccount
   Description: This procedure check selected account is a Statistical account
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckEAD(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEAD
   Description: Validates if the passed date is not earlier than earliest apply date.
   OperationID: CheckEAD
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEAD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEAD_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGroupPrefixChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGroupPrefixChange
   Description: This method checks if the group prefix on the recurring journal header changed
and if there are other recurring journals created for the book/multi-book.
If there are the group prefix on those records will be updated to the new value,
but check with user before performing this action.
   OperationID: CheckGroupPrefixChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupPrefixChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupPrefixChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSchedForYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSchedForYear
   Description: This method created GLRecSched records given a fiscal year.
   OperationID: CreateSchedForYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSchedForYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSchedForYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLRecSchedGenerate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLRecSchedGenerate
   Description: This method returns the generate schedule dataset.
   OperationID: GetGLRecSchedGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLRecSchedGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLRecSchedGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Renumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Renumber
   Description: This method renumbers lines in Recurring Journal record with number recurNum.
   OperationID: Renumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Renumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Renumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Gets the code/description list of the specified column translated to the user's language.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLRecHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLRecHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRecHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRecHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRecHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLRecDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLRecDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRecDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRecDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRecDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLRecSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLRecSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRecSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRecSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRecSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RecurringJournalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRecDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRecHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRecHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRecSchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRecSchedRow] = obj["value"]
      pass

class Erp_Tablesets_GLRecDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl records must be kept in synchronization.  Cannot be zero(0).  """  
      self.RecurLine:int = obj["RecurLine"]
      """  Unique ID of entry within a Recur Number.  Allow user to change number at any time.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  Cannot be zero(0).  """  
      self.Description:str = obj["Description"]
      """  Default from GLRecHed description.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Zero/Positive = Debit, Negative = Credit.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Flag that indicate if the account is a curency account  """  
      self.DocTransAmt:int = obj["DocTransAmt"]
      """  Document Transaction amount.  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  A unique code that identifies the currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
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
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  """  
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
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.TotCurrDebit:int = obj["TotCurrDebit"]
      self.TotCurrCredit:int = obj["TotCurrCredit"]
      self.StatAmount:int = obj["StatAmount"]
      """  Statistical Amount. UI display value.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.CurrencyCodeAcctList:str = obj["CurrencyCodeAcctList"]
      self.BitFlag:int = obj["BitFlag"]
      self.AcctCurrCurrName:str = obj["AcctCurrCurrName"]
      self.AcctCurrCurrencyID:str = obj["AcctCurrCurrencyID"]
      self.AcctCurrCurrSymbol:str = obj["AcctCurrCurrSymbol"]
      self.AcctCurrCurrDesc:str = obj["AcctCurrCurrDesc"]
      self.AcctCurrDocumentDesc:str = obj["AcctCurrDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.GLGLAcctDisp:str = obj["GLGLAcctDisp"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.GLGLShortAcct:str = obj["GLGLShortAcct"]
      self.GlRefCodeDescRefCodeDesc:str = obj["GlRefCodeDescRefCodeDesc"]
      self.RecurNumDescription:str = obj["RecurNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  """  
      self.Description:str = obj["Description"]
      """  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  """  
      self.ActiveEntry:bool = obj["ActiveEntry"]
      """  Indicates that the recurring entry is active and will be selected during the next period close.  """  
      self.SelectedPeriodList:str = obj["SelectedPeriodList"]
      """  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GroupPrefix:str = obj["GroupPrefix"]
      """  The prefix of the group (GLJrnGrp) created for recurring journal entries.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows the Total Debit statistical amount.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows the Total Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SelectedToggleBoxes:str = obj["SelectedToggleBoxes"]
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Displays the Total Credit as positive.  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Displays the Total Debit.  """  
      self.MultipleBooks:bool = obj["MultipleBooks"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the book.  """  
      self.BookIDDescription:str = obj["BookIDDescription"]
      """  Descripiton of Book  """  
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  """  
      self.Description:str = obj["Description"]
      """  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  """  
      self.ActiveEntry:bool = obj["ActiveEntry"]
      """  Indicates that the recurring entry is active and will be selected during the next period close.  """  
      self.SelectedPeriodList:str = obj["SelectedPeriodList"]
      """  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GroupPrefix:str = obj["GroupPrefix"]
      """  The prefix of the group (GLJrnGrp) created for recurring journal entries.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows the Total Debit statistical amount.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows the Total Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SelectedToggleBoxes:str = obj["SelectedToggleBoxes"]
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Displays the Total Credit as positive.  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Displays the Total Debit.  """  
      self.MultipleBooks:bool = obj["MultipleBooks"]
      self.BitFlag:int = obj["BitFlag"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      self.BookIDDescription:str = obj["BookIDDescription"]
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Identifier of GLRecHed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date to apply the entry to GL.  """  
      self.ReversalApplyDate:str = obj["ReversalApplyDate"]
      """  The date the reversal is applied to GL.  """  
      self.ScheduleDate:str = obj["ScheduleDate"]
      """  The date this entry is scheduled to create the journal entry record.  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date the journal entry record was created.  System assigned.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """   Scheduled status.  Assigned by the user.  Values are:
S = Scheduled
NS = Not Scheduled  """  
      self.ProcStatus:str = obj["ProcStatus"]
      """   Indicates the processing status.  System assigned.  Values are:
D = Done.  Record has been processed and converted into a journal detail.
I = Ignored.  Record was ignored during apply recurring journal process.
F = Fail.  An error occurred on this record during the apply recurring journal process.  """  
      self.FailureReason:str = obj["FailureReason"]
      """  Indicates the reason a gl journal entry record could not be created for the year/period.  Assigned by the system.  Will be populated only when Status = "Fail".  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
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
class AutoBalance_input:
   """ Required : 
   recurNum
   recurLine
   ds
   """  
   def __init__(self, obj):
      self.recurNum:int = obj["recurNum"]
      """  Recurring Journal record number  """  
      self.recurLine:int = obj["recurLine"]
      """  Recurring Journal record line number  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class AutoBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeBookID_input:
   """ Required : 
   ProposedBookID
   ds
   """  
   def __init__(self, obj):
      self.ProposedBookID:str = obj["ProposedBookID"]
      """  The proposed Book  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class ChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEntryMode_input:
   """ Required : 
   proposedBookMode
   ds
   """  
   def __init__(self, obj):
      self.proposedBookMode:str = obj["proposedBookMode"]
      """  The proposed Entry Mode  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class ChangeEntryMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGlAcct_input:
   """ Required : 
   ProposedDispAcct
   ds
   """  
   def __init__(self, obj):
      self.ProposedDispAcct:str = obj["ProposedDispAcct"]
      """  The proposed G/L Display Account  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class ChangeGlAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRateType_input:
   """ Required : 
   proposedRateType
   ds
   """  
   def __init__(self, obj):
      self.proposedRateType:str = obj["proposedRateType"]
      """  The proposed Rate Type  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class ChangeRateType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBalance_input:
   """ Required : 
   ds
   RecurNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      self.RecurNum:int = obj["RecurNum"]
      """  The current recurring journal number  """  
      pass

class CheckBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCurrencyAccountExt_input:
   """ Required : 
   ds
   iLineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      self.iLineNum:int = obj["iLineNum"]
      """  lineNum  """  
      pass

class CheckCurrencyAccountExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
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

class CheckEAD_input:
   """ Required : 
   ipDate
   """  
   def __init__(self, obj):
      self.ipDate:str = obj["ipDate"]
      """  The date to validate  """  
      pass

class CheckEAD_output:
   def __init__(self, obj):
      pass

class CheckGroupPrefixChange_input:
   """ Required : 
   inRecurNum
   inBookID
   inGroupPrefix
   """  
   def __init__(self, obj):
      self.inRecurNum:int = obj["inRecurNum"]
      """  The recurring journal entry number  """  
      self.inBookID:str = obj["inBookID"]
      """  The book id  """  
      self.inGroupPrefix:str = obj["inGroupPrefix"]
      """  The proposed group prefix  """  
      pass

class CheckGroupPrefixChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckStatUOMAccount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class CheckStatUOMAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertCreditAmount_input:
   """ Required : 
   proposedAmount
   ds
   """  
   def __init__(self, obj):
      self.proposedAmount:int = obj["proposedAmount"]
      """  The proposed  Amount  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class ConvertCreditAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertDebitAmount_input:
   """ Required : 
   proposedAmount
   ds
   """  
   def __init__(self, obj):
      self.proposedAmount:int = obj["proposedAmount"]
      """  The proposed  Amount  """  
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class ConvertDebitAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateSchedForYear_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLRecSchedGenerateTableset] = obj["ds"]
      pass

class CreateSchedForYear_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RecurringJournalTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLRecSchedGenerateTableset] = obj["ds"]
      self.cOutMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   recurNum
   """  
   def __init__(self, obj):
      self.recurNum:int = obj["recurNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLRecDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl records must be kept in synchronization.  Cannot be zero(0).  """  
      self.RecurLine:int = obj["RecurLine"]
      """  Unique ID of entry within a Recur Number.  Allow user to change number at any time.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  Cannot be zero(0).  """  
      self.Description:str = obj["Description"]
      """  Default from GLRecHed description.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Zero/Positive = Debit, Negative = Credit.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Flag that indicate if the account is a curency account  """  
      self.DocTransAmt:int = obj["DocTransAmt"]
      """  Document Transaction amount.  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  A unique code that identifies the currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
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
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  """  
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
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.TotCurrDebit:int = obj["TotCurrDebit"]
      self.TotCurrCredit:int = obj["TotCurrCredit"]
      self.StatAmount:int = obj["StatAmount"]
      """  Statistical Amount. UI display value.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.CurrencyCodeAcctList:str = obj["CurrencyCodeAcctList"]
      self.BitFlag:int = obj["BitFlag"]
      self.AcctCurrCurrName:str = obj["AcctCurrCurrName"]
      self.AcctCurrCurrencyID:str = obj["AcctCurrCurrencyID"]
      self.AcctCurrCurrSymbol:str = obj["AcctCurrCurrSymbol"]
      self.AcctCurrCurrDesc:str = obj["AcctCurrCurrDesc"]
      self.AcctCurrDocumentDesc:str = obj["AcctCurrDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.GLGLAcctDisp:str = obj["GLGLAcctDisp"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.GLGLShortAcct:str = obj["GLGLShortAcct"]
      self.GlRefCodeDescRefCodeDesc:str = obj["GlRefCodeDescRefCodeDesc"]
      self.RecurNumDescription:str = obj["RecurNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  """  
      self.Description:str = obj["Description"]
      """  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  """  
      self.ActiveEntry:bool = obj["ActiveEntry"]
      """  Indicates that the recurring entry is active and will be selected during the next period close.  """  
      self.SelectedPeriodList:str = obj["SelectedPeriodList"]
      """  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GroupPrefix:str = obj["GroupPrefix"]
      """  The prefix of the group (GLJrnGrp) created for recurring journal entries.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows the Total Debit statistical amount.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows the Total Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SelectedToggleBoxes:str = obj["SelectedToggleBoxes"]
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Displays the Total Credit as positive.  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Displays the Total Debit.  """  
      self.MultipleBooks:bool = obj["MultipleBooks"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the book.  """  
      self.BookIDDescription:str = obj["BookIDDescription"]
      """  Descripiton of Book  """  
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecHedListTableset:
   def __init__(self, obj):
      self.GLRecHedList:list[Erp_Tablesets_GLRecHedListRow] = obj["GLRecHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLRecHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Number that is assigned by the system.  Defaults to ten(10) greater than the highest number (i.e. 10, 20, 30, etc.).  User can change number at any time, but GLRecDtl and GLRecSched records must be kept in synchronization.  Cannot be zero(0).  """  
      self.Description:str = obj["Description"]
      """  Describes the Recurring Entry.  Used as a default for the GLRecDtl.Description field.  """  
      self.TotDebit:int = obj["TotDebit"]
      """  The Total Debits.  A summary of the positive GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.TotCredit:int = obj["TotCredit"]
      """  The Total Credit.  A summary of negative GLRecDtl.TranAmt in the related GLRecDtl records.  Primarily used for visual verification.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that this Recurring Entry set should create reversing entries for the next fiscal period when it is posted in G/L Journal Entry.  """  
      self.ActiveEntry:bool = obj["ActiveEntry"]
      """  Indicates that the recurring entry is active and will be selected during the next period close.  """  
      self.SelectedPeriodList:str = obj["SelectedPeriodList"]
      """  A LIST-DELIM delimited list of periods that the entry is to be selected in.  When this list is blank it means ALL periods are selected.  To set NO periods selected use the ActiveEntry flag.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.
NOT ACTIVE  AS OF 3.20RESERVED FOR FUTURE USE.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GroupPrefix:str = obj["GroupPrefix"]
      """  The prefix of the group (GLJrnGrp) created for recurring journal entries.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows the Total Debit statistical amount.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Default is the first date of the next period. A date entered in this fields should be greater than the journal?s apply date.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows the Total Credit statistical amount.  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the journal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SelectedToggleBoxes:str = obj["SelectedToggleBoxes"]
      self.Balance:int = obj["Balance"]
      """  TotDebit - TotCredit = Balance  """  
      self.DispTotCredit:int = obj["DispTotCredit"]
      """  Displays the Total Credit as positive.  """  
      self.DispTotDebit:int = obj["DispTotDebit"]
      """  Displays the Total Debit.  """  
      self.MultipleBooks:bool = obj["MultipleBooks"]
      self.BitFlag:int = obj["BitFlag"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      self.BookIDDescription:str = obj["BookIDDescription"]
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecSchedGenerateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RecurNum:int = obj["RecurNum"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRecSchedGenerateTableset:
   def __init__(self, obj):
      self.GLRecSchedGenerate:list[Erp_Tablesets_GLRecSchedGenerateRow] = obj["GLRecSchedGenerate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLRecSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecurNum:int = obj["RecurNum"]
      """  Identifier of GLRecHed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date to apply the entry to GL.  """  
      self.ReversalApplyDate:str = obj["ReversalApplyDate"]
      """  The date the reversal is applied to GL.  """  
      self.ScheduleDate:str = obj["ScheduleDate"]
      """  The date this entry is scheduled to create the journal entry record.  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date the journal entry record was created.  System assigned.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """   Scheduled status.  Assigned by the user.  Values are:
S = Scheduled
NS = Not Scheduled  """  
      self.ProcStatus:str = obj["ProcStatus"]
      """   Indicates the processing status.  System assigned.  Values are:
D = Done.  Record has been processed and converted into a journal detail.
I = Ignored.  Record was ignored during apply recurring journal process.
F = Fail.  An error occurred on this record during the apply recurring journal process.  """  
      self.FailureReason:str = obj["FailureReason"]
      """  Indicates the reason a gl journal entry record could not be created for the year/period.  Assigned by the system.  Will be populated only when Status = "Fail".  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RecurringJournalTableset:
   def __init__(self, obj):
      self.GLRecHed:list[Erp_Tablesets_GLRecHedRow] = obj["GLRecHed"]
      self.GLRecDtl:list[Erp_Tablesets_GLRecDtlRow] = obj["GLRecDtl"]
      self.GLRecSched:list[Erp_Tablesets_GLRecSchedRow] = obj["GLRecSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRecurringJournalTableset:
   def __init__(self, obj):
      self.GLRecHed:list[Erp_Tablesets_GLRecHedRow] = obj["GLRecHed"]
      self.GLRecDtl:list[Erp_Tablesets_GLRecDtlRow] = obj["GLRecDtl"]
      self.GLRecSched:list[Erp_Tablesets_GLRecSchedRow] = obj["GLRecSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class GetByID_input:
   """ Required : 
   recurNum
   """  
   def __init__(self, obj):
      self.recurNum:int = obj["recurNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RecurringJournalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RecurringJournalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RecurringJournalTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The name of the table.  """  
      self.fieldName:str = obj["fieldName"]
      """  The name of the column.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Empty string is returned if the column is not found.  """  
      pass

class GetGLRecSchedGenerate_input:
   """ Required : 
   inRecurNum
   """  
   def __init__(self, obj):
      self.inRecurNum:int = obj["inRecurNum"]
      """  The GLRecHed number  """  
      pass

class GetGLRecSchedGenerate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLRecSchedGenerateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLRecHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLRecDtl_input:
   """ Required : 
   ds
   recurNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      self.recurNum:int = obj["recurNum"]
      pass

class GetNewGLRecDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLRecHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class GetNewGLRecHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLRecSched_input:
   """ Required : 
   ds
   recurNum
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      self.recurNum:int = obj["recurNum"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetNewGLRecSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLRecHed
   whereClauseGLRecDtl
   whereClauseGLRecSched
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLRecHed:str = obj["whereClauseGLRecHed"]
      self.whereClauseGLRecDtl:str = obj["whereClauseGLRecDtl"]
      self.whereClauseGLRecSched:str = obj["whereClauseGLRecSched"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RecurringJournalTableset] = obj["returnObj"]
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

class Renumber_input:
   """ Required : 
   recurNum
   """  
   def __init__(self, obj):
      self.recurNum:int = obj["recurNum"]
      """  Recurring Journal record number  """  
      pass

class Renumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RecurringJournalTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRecurringJournalTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRecurringJournalTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCurrencyAccount_input:
   """ Required : 
   ds
   ipCurrency
   lineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      self.ipCurrency:str = obj["ipCurrency"]
      """  The proposed Currency value  """  
      self.lineNum:int = obj["lineNum"]
      """  Lournal Line  """  
      pass

class ValidateCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RecurringJournalTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

