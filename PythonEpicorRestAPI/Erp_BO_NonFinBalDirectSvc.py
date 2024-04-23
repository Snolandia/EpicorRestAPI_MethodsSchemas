import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.NonFinBalDirectSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_NonFinBalDirects(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NonFinBalDirects items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NonFinBalDirects
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects",headers=creds) as resp:
           return await resp.json()

async def post_NonFinBalDirects(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NonFinBalDirects
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NonFinBalDirect item
   Description: Calls GetByID to retrieve the NonFinBalDirect item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonFinBalDirect
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NonFinBalDirect for the service
   Description: Calls UpdateExt to update NonFinBalDirect. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NonFinBalDirect
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NonFinBalDirect item
   Description: Call UpdateExt to delete NonFinBalDirect item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NonFinBalDirect
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls",headers=creds) as resp:
           return await resp.json()

async def get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, JournalLine, select = None, filter = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnlSims(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlMnlSims items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlMnlSims1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnlSims",headers=creds) as resp:
           return await resp.json()

async def get_NonFinBalDirects_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, JournalLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlSim item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlSim1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param JournalLine: Desc: JournalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/NonFinBalDirects(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnls
      :param select: Desc: Odata select comma delimited list of fields
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnls_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, select = None, filter = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnls(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlSims(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnlSims items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlSims
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlMnlSims(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlSims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlSim item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlSim
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlMnlSim for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlSim. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlSim
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlSimRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlMnlSims_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlMnlSim item
   Description: Call UpdateExt to delete GLJrnDtlMnlSim item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlSim
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/GLJrnDtlMnlSims(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + FiscalCalendarID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLJrnHed, whereClauseGLJrnDtlMnl, whereClauseGLJrnDtlMnlSim, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLJrnHed=" + whereClauseGLJrnHed
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
   params += "whereClauseGLJrnDtlMnlSim=" + whereClauseGLJrnDtlMnlSim
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnlSim(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnlSim
   OperationID: GetNewGLJrnDtlMnlSim
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlSim_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlSim_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJournal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournal
   Description: This method is called in place of the GetByID method, requiring only the
the GL Group ID.
   OperationID: GetJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGLAccount
   OperationID: OnChangeGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnFormClose(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnFormClose
   Description: Delete stat rows with zero amounts
   OperationID: OnFormClose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnFormClose_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnFormClose_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonFinBalDirectSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlSimRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlSimRow] = obj["value"]
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

class Erp_Tablesets_GLJrnDtlMnlSimRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GLAccount:str = obj["GLAccount"]
      self.CurrStatBalance:int = obj["CurrStatBalance"]
      self.NewStatBalance:int = obj["NewStatBalance"]
      self.StatUOMCode:str = obj["StatUOMCode"]
      self.StatUOMDesc:str = obj["StatUOMDesc"]
      self.Reverse:bool = obj["Reverse"]
      self.BookID:str = obj["BookID"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.JournalCode:str = obj["JournalCode"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.COACode:str = obj["COACode"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.SegValue1:str = obj["SegValue1"]
      self.Statistical:int = obj["Statistical"]
      self.GroupID:str = obj["GroupID"]
      self.JEDate:str = obj["JEDate"]
      self.SegValue2:str = obj["SegValue2"]
      self.SegValue3:str = obj["SegValue3"]
      self.SegValue4:str = obj["SegValue4"]
      self.SegValue5:str = obj["SegValue5"]
      self.SegValue6:str = obj["SegValue6"]
      self.SegValue7:str = obj["SegValue7"]
      self.SegValue8:str = obj["SegValue8"]
      self.SegValue9:str = obj["SegValue9"]
      self.SegValue10:str = obj["SegValue10"]
      self.SegValue11:str = obj["SegValue11"]
      self.SegValue12:str = obj["SegValue12"]
      self.SegValue13:str = obj["SegValue13"]
      self.SegValue14:str = obj["SegValue14"]
      self.SegValue15:str = obj["SegValue15"]
      self.SegValue16:str = obj["SegValue16"]
      self.SegValue17:str = obj["SegValue17"]
      self.SegValue18:str = obj["SegValue18"]
      self.SegValue19:str = obj["SegValue19"]
      self.SegValue20:str = obj["SegValue20"]
      self.Description:str = obj["Description"]
      self.CreateDate:str = obj["CreateDate"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Summarized:bool = obj["Summarized"]
      """  Means this line is agglutinate from many lines with the same GL Account. Uses in statistical logic.  """  
      self.SysRowID:str = obj["SysRowID"]
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




#########################################################################
# Custom Schemas:
#########################################################################
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

class Erp_Tablesets_GLJrnDtlMnlSimRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GLAccount:str = obj["GLAccount"]
      self.CurrStatBalance:int = obj["CurrStatBalance"]
      self.NewStatBalance:int = obj["NewStatBalance"]
      self.StatUOMCode:str = obj["StatUOMCode"]
      self.StatUOMDesc:str = obj["StatUOMDesc"]
      self.Reverse:bool = obj["Reverse"]
      self.BookID:str = obj["BookID"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.JournalCode:str = obj["JournalCode"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.COACode:str = obj["COACode"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.SegValue1:str = obj["SegValue1"]
      self.Statistical:int = obj["Statistical"]
      self.GroupID:str = obj["GroupID"]
      self.JEDate:str = obj["JEDate"]
      self.SegValue2:str = obj["SegValue2"]
      self.SegValue3:str = obj["SegValue3"]
      self.SegValue4:str = obj["SegValue4"]
      self.SegValue5:str = obj["SegValue5"]
      self.SegValue6:str = obj["SegValue6"]
      self.SegValue7:str = obj["SegValue7"]
      self.SegValue8:str = obj["SegValue8"]
      self.SegValue9:str = obj["SegValue9"]
      self.SegValue10:str = obj["SegValue10"]
      self.SegValue11:str = obj["SegValue11"]
      self.SegValue12:str = obj["SegValue12"]
      self.SegValue13:str = obj["SegValue13"]
      self.SegValue14:str = obj["SegValue14"]
      self.SegValue15:str = obj["SegValue15"]
      self.SegValue16:str = obj["SegValue16"]
      self.SegValue17:str = obj["SegValue17"]
      self.SegValue18:str = obj["SegValue18"]
      self.SegValue19:str = obj["SegValue19"]
      self.SegValue20:str = obj["SegValue20"]
      self.Description:str = obj["Description"]
      self.CreateDate:str = obj["CreateDate"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Summarized:bool = obj["Summarized"]
      """  Means this line is agglutinate from many lines with the same GL Account. Uses in statistical logic.  """  
      self.SysRowID:str = obj["SysRowID"]
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

class Erp_Tablesets_NonFinBalDirectTableset:
   def __init__(self, obj):
      self.GLJrnHed:list[Erp_Tablesets_GLJrnHedRow] = obj["GLJrnHed"]
      self.GLJrnDtlMnl:list[Erp_Tablesets_GLJrnDtlMnlRow] = obj["GLJrnDtlMnl"]
      self.GLJrnDtlMnlSim:list[Erp_Tablesets_GLJrnDtlMnlSimRow] = obj["GLJrnDtlMnlSim"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtNonFinBalDirectTableset:
   def __init__(self, obj):
      self.GLJrnHed:list[Erp_Tablesets_GLJrnHedRow] = obj["GLJrnHed"]
      self.GLJrnDtlMnl:list[Erp_Tablesets_GLJrnDtlMnlRow] = obj["GLJrnDtlMnl"]
      self.GLJrnDtlMnlSim:list[Erp_Tablesets_GLJrnDtlMnlSimRow] = obj["GLJrnDtlMnlSim"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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
      self.returnObj:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetJournal_input:
   """ Required : 
   groupID
   journalNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.journalNum:int = obj["journalNum"]
      pass

class GetJournal_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLJrnHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnlSim_input:
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
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetNewGLJrnDtlMnlSim_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLJrnHed
   whereClauseGLJrnDtlMnl
   whereClauseGLJrnDtlMnlSim
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLJrnHed:str = obj["whereClauseGLJrnHed"]
      self.whereClauseGLJrnDtlMnl:str = obj["whereClauseGLJrnDtlMnl"]
      self.whereClauseGLJrnDtlMnlSim:str = obj["whereClauseGLJrnDtlMnlSim"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["returnObj"]
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

class OnChangeGLAccount_input:
   """ Required : 
   glAccount
   ds
   """  
   def __init__(self, obj):
      self.glAccount:str = obj["glAccount"]
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

class OnChangeGLAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnFormClose_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

class OnFormClose_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNonFinBalDirectTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNonFinBalDirectTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonFinBalDirectTableset] = obj["ds"]
      pass

      """  output parameters  """  

