import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AccountBudgetSvc
# Description: class AccountBudgetSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AccountBudgets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AccountBudgets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AccountBudgets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetHdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets",headers=creds) as resp:
           return await resp.json()

async def post_AccountBudgets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AccountBudgets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalCalendarID, BudgetCodeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AccountBudget item
   Description: Calls GetByID to retrieve the AccountBudget item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AccountBudget
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalCalendarID, BudgetCodeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AccountBudget for the service
   Description: Calls UpdateExt to update AccountBudget. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AccountBudget
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBudgetHdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalCalendarID, BudgetCodeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AccountBudget item
   Description: Call UpdateExt to delete AccountBudget item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AccountBudget
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID_GLBudgetDtls(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalCalendarID, BudgetCodeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLBudgetDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBudgetDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")/GLBudgetDtls",headers=creds) as resp:
           return await resp.json()

async def get_AccountBudgets_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalCalendarID_BudgetCodeID_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalCalendarID, BudgetCodeID, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBudgetDtl item
   Description: Calls GetByID to retrieve the GLBudgetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBudgetDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/AccountBudgets(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalCalendarID + "," + BudgetCodeID + ")/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBudgetDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBudgetDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBudgetDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls",headers=creds) as resp:
           return await resp.json()

async def post_GLBudgetDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBudgetDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, BudgetCodeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBudgetDtl item
   Description: Calls GetByID to retrieve the GLBudgetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBudgetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, BudgetCodeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBudgetDtl for the service
   Description: Calls UpdateExt to update GLBudgetDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBudgetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBudgetDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBudgetDtls_Company_BookID_BalanceAcct_BalanceType_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID_BudgetCodeID(Company, BookID, BalanceAcct, BalanceType, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, BudgetCodeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBudgetDtl item
   Description: Call UpdateExt to delete GLBudgetDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBudgetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BalanceAcct: Desc: BalanceAcct   Required: True   Allow empty value : True
      :param BalanceType: Desc: BalanceType   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param BudgetCodeID: Desc: BudgetCodeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/GLBudgetDtls(" + Company + "," + BookID + "," + BalanceAcct + "," + BalanceType + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + "," + BudgetCodeID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBudgetHdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBudgetHd, whereClauseGLBudgetDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseGLBudgetHd=" + whereClauseGLBudgetHd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBudgetDtl=" + whereClauseGLBudgetDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bookID, balanceAcct, balanceType, fiscalYear, fiscalYearSuffix, fiscalCalendarID, budgetCodeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
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
   params += "bookID=" + bookID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "balanceAcct=" + balanceAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "balanceType=" + balanceType
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
   params += "fiscalCalendarID=" + fiscalCalendarID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "budgetCodeID=" + budgetCodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBudgetHdEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBudgetHdEx
   Description: GetNewGLBudgetHd with all key parameters
   OperationID: GetNewGLBudgetHdEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBudgetHdEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBudgetHdEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteBudget(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteBudget
   Description: This method deletes the entire Budget of a valid fiscal year.
   OperationID: DeleteBudget
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBudget_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBudget_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlBudgetAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlBudgetAmt
   Description: This method updates the DispTotalBudgetAmt and the BudgetAmt of the GLBudgetHd
when the GLBudgetDtl.BudgetAmt changes.
   OperationID: ChangeDtlBudgetAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlBudgetAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlBudgetAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlBudgetStatAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlBudgetStatAmt
   Description: This method updates the DispTotalBudgetStatAmt and the BudgetStatAmt of the GLBudgetHd
when the GLBudgetDtl.BudgetStatAmt changes.
   OperationID: ChangeDtlBudgetStatAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlBudgetStatAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlBudgetStatAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePerCodeOrAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePerCodeOrAmount
   Description: This method updates the DispTotalBudgetAmt when the BudgetPerCode or BudgetAmt or BudgetStatAmt changes.
   OperationID: ChangePerCodeOrAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePerCodeOrAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePerCodeOrAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBalanceAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBalanceAcct
   Description: This method updates the StatUOM information when BalanceAcct is changed.
   OperationID: ChangeBalanceAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBalanceAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBalanceAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGLAccount
   Description: Validate account and budget
   OperationID: ValidateGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGLBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGLBook
   Description: ValidateGLBook
   OperationID: ValidateGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBudgetCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBudgetCode
   Description: Validate BudgetCode
   OperationID: ValidateBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTargetBudgetCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTargetBudgetCode
   Description: Return target budget code
   OperationID: GetTargetBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBudgetHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBudgetHd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBudgetHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBudgetHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBudgetHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBudgetDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBudgetDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBudgetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBudgetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBudgetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AccountBudgetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBudgetDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBudgetHdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBudgetHdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBudgetHdRow] = obj["value"]
      pass

class Erp_Tablesets_GLBudgetDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  GLBook ID  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  The budget GL Account.  Only balance accounts can have a budget.  """  
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this period balance record  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  Identifier of Budget Code  """  
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
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.BudgetAmt:int = obj["BudgetAmt"]
      """  Budget amount.  Credits are negative,  Debits are positive.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BudgetStatAmt:int = obj["BudgetStatAmt"]
      """  Budget statistical amount.  Credits are negative,  Debits are positive.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.BudgetCodeInactive:bool = obj["BudgetCodeInactive"]
      self.BudgetCodeIsDefault:bool = obj["BudgetCodeIsDefault"]
      self.BudgetCodeBudgetCodeDesc:str = obj["BudgetCodeBudgetCodeDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBudgetHdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  GLBook ID  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  The budget GL Account.  Only balance accounts can have a budget.  """  
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this period balance record  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  Identifier of Budget Code  """  
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
      self.TotalBudgetAmt:int = obj["TotalBudgetAmt"]
      """  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  """  
      self.BudgetPerCode:str = obj["BudgetPerCode"]
      """  Indicates if the budget amount is period or annual amount.  """  
      self.CashFlow:bool = obj["CashFlow"]
      """  Whether or not to include in the Cash Flow Analysis  .  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BudgetAmt:int = obj["BudgetAmt"]
      self.DispTotalBudgetAmt:int = obj["DispTotalBudgetAmt"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  """  
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      """  Text that describes the account.  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBudgetHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  GLBook ID  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  The budget GL Account.  Only balance accounts can have a budget.  """  
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this period balance record  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  Identifier of Budget Code  """  
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
      self.TotalBudgetAmt:int = obj["TotalBudgetAmt"]
      """  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  """  
      self.BudgetPerCode:str = obj["BudgetPerCode"]
      """  Indicates if the budget amount is period or annual amount.  """  
      self.CashFlow:bool = obj["CashFlow"]
      """  Whether or not to include in the Cash Flow Analysis  .  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalBudgetStatAmt:int = obj["TotalBudgetStatAmt"]
      """  Total Budget Statistical amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetStatAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  """  
      self.BudgetStatAmt:int = obj["BudgetStatAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DispTotalBudgetAmt:int = obj["DispTotalBudgetAmt"]
      self.DispTotalBudgetStatAmt:int = obj["DispTotalBudgetStatAmt"]
      self.Statistical:int = obj["Statistical"]
      self.StatUOMCode:str = obj["StatUOMCode"]
      self.StatUOMDesc:str = obj["StatUOMDesc"]
      self.StatUOMNumOfDec:int = obj["StatUOMNumOfDec"]
      self.BudgetAmt:int = obj["BudgetAmt"]
      self.TreeViewField:str = obj["TreeViewField"]
      self.BitFlag:int = obj["BitFlag"]
      self.BudgetCodeInactive:bool = obj["BudgetCodeInactive"]
      self.BudgetCodeBudgetCodeDesc:str = obj["BudgetCodeBudgetCodeDesc"]
      self.BudgetCodeIsDefault:bool = obj["BudgetCodeIsDefault"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBalanceAcct_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

class ChangeBalanceAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlBudgetAmt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

class ChangeDtlBudgetAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlBudgetStatAmt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

class ChangeDtlBudgetStatAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePerCodeOrAmount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

class ChangePerCodeOrAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteBudget_input:
   """ Required : 
   inpBookID
   inpBudgetCodeID
   inpFiscalYear
   inpFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.inpBookID:str = obj["inpBookID"]
      """  The Book ID of the Budget to delete.  """  
      self.inpBudgetCodeID:str = obj["inpBudgetCodeID"]
      """  The Budget Code ID of the Budget to delete.  """  
      self.inpFiscalYear:int = obj["inpFiscalYear"]
      """  The Fiscal Year of the Budget to delete.  """  
      self.inpFiscalYearSuffix:str = obj["inpFiscalYearSuffix"]
      """  The Fiscal Year Suffix of the Budget to delete.  """  
      pass

class DeleteBudget_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AccountBudgetTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   bookID
   balanceAcct
   balanceType
   fiscalYear
   fiscalYearSuffix
   fiscalCalendarID
   budgetCodeID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.balanceAcct:str = obj["balanceAcct"]
      self.balanceType:str = obj["balanceType"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.budgetCodeID:str = obj["budgetCodeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AccountBudgetTableset:
   def __init__(self, obj):
      self.GLBudgetHd:list[Erp_Tablesets_GLBudgetHdRow] = obj["GLBudgetHd"]
      self.GLBudgetDtl:list[Erp_Tablesets_GLBudgetDtlRow] = obj["GLBudgetDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBudgetDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  GLBook ID  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  The budget GL Account.  Only balance accounts can have a budget.  """  
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this period balance record  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  Identifier of Budget Code  """  
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
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.BudgetAmt:int = obj["BudgetAmt"]
      """  Budget amount.  Credits are negative,  Debits are positive.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BudgetStatAmt:int = obj["BudgetStatAmt"]
      """  Budget statistical amount.  Credits are negative,  Debits are positive.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.BudgetCodeInactive:bool = obj["BudgetCodeInactive"]
      self.BudgetCodeIsDefault:bool = obj["BudgetCodeIsDefault"]
      self.BudgetCodeBudgetCodeDesc:str = obj["BudgetCodeBudgetCodeDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBudgetHdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  GLBook ID  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  The budget GL Account.  Only balance accounts can have a budget.  """  
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this period balance record  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  Identifier of Budget Code  """  
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
      self.TotalBudgetAmt:int = obj["TotalBudgetAmt"]
      """  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  """  
      self.BudgetPerCode:str = obj["BudgetPerCode"]
      """  Indicates if the budget amount is period or annual amount.  """  
      self.CashFlow:bool = obj["CashFlow"]
      """  Whether or not to include in the Cash Flow Analysis  .  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BudgetAmt:int = obj["BudgetAmt"]
      self.DispTotalBudgetAmt:int = obj["DispTotalBudgetAmt"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  """  
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      """  Text that describes the account.  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBudgetHdListTableset:
   def __init__(self, obj):
      self.GLBudgetHdList:list[Erp_Tablesets_GLBudgetHdListRow] = obj["GLBudgetHdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBudgetHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  GLBook ID  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  The budget GL Account.  Only balance accounts can have a budget.  """  
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies the type of balance stored on this record.  S = Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this period balance record  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  Identifier of Budget Code  """  
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
      self.TotalBudgetAmt:int = obj["TotalBudgetAmt"]
      """  Total Budget amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  """  
      self.BudgetPerCode:str = obj["BudgetPerCode"]
      """  Indicates if the budget amount is period or annual amount.  """  
      self.CashFlow:bool = obj["CashFlow"]
      """  Whether or not to include in the Cash Flow Analysis  .  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalBudgetStatAmt:int = obj["TotalBudgetStatAmt"]
      """  Total Budget Statistical amount for the fiscal year.  This is a summary of GLBudgetDtl.BudgetStatAmt. Indirectly maintained via GLBudgetDtl write trigger.  Credits are negative,  Debits are positive.  """  
      self.BudgetStatAmt:int = obj["BudgetStatAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DispTotalBudgetAmt:int = obj["DispTotalBudgetAmt"]
      self.DispTotalBudgetStatAmt:int = obj["DispTotalBudgetStatAmt"]
      self.Statistical:int = obj["Statistical"]
      self.StatUOMCode:str = obj["StatUOMCode"]
      self.StatUOMDesc:str = obj["StatUOMDesc"]
      self.StatUOMNumOfDec:int = obj["StatUOMNumOfDec"]
      self.BudgetAmt:int = obj["BudgetAmt"]
      self.TreeViewField:str = obj["TreeViewField"]
      self.BitFlag:int = obj["BitFlag"]
      self.BudgetCodeInactive:bool = obj["BudgetCodeInactive"]
      self.BudgetCodeBudgetCodeDesc:str = obj["BudgetCodeBudgetCodeDesc"]
      self.BudgetCodeIsDefault:bool = obj["BudgetCodeIsDefault"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAccountBudgetTableset:
   def __init__(self, obj):
      self.GLBudgetHd:list[Erp_Tablesets_GLBudgetHdRow] = obj["GLBudgetHd"]
      self.GLBudgetDtl:list[Erp_Tablesets_GLBudgetDtlRow] = obj["GLBudgetDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   bookID
   balanceAcct
   balanceType
   fiscalYear
   fiscalYearSuffix
   fiscalCalendarID
   budgetCodeID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.balanceAcct:str = obj["balanceAcct"]
      self.balanceType:str = obj["balanceType"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.budgetCodeID:str = obj["budgetCodeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AccountBudgetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AccountBudgetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AccountBudgetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBudgetHdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBudgetDtl_input:
   """ Required : 
   ds
   bookID
   balanceAcct
   balanceType
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.balanceAcct:str = obj["balanceAcct"]
      self.balanceType:str = obj["balanceType"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetNewGLBudgetDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBudgetHdEx_input:
   """ Required : 
   ds
   bookID
   balanceAcct
   balanceType
   fiscalYear
   fiscalYearSuffix
   fiscalCalendarID
   budgetCodeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.balanceAcct:str = obj["balanceAcct"]
      self.balanceType:str = obj["balanceType"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.budgetCodeID:str = obj["budgetCodeID"]
      pass

class GetNewGLBudgetHdEx_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBudgetHd_input:
   """ Required : 
   ds
   bookID
   balanceAcct
   balanceType
   fiscalYear
   fiscalYearSuffix
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.balanceAcct:str = obj["balanceAcct"]
      self.balanceType:str = obj["balanceType"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetNewGLBudgetHd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBudgetHd
   whereClauseGLBudgetDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBudgetHd:str = obj["whereClauseGLBudgetHd"]
      self.whereClauseGLBudgetDtl:str = obj["whereClauseGLBudgetDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AccountBudgetTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTargetBudgetCode_input:
   """ Required : 
   sourceBudget
   """  
   def __init__(self, obj):
      self.sourceBudget:str = obj["sourceBudget"]
      """  Source Budget Code  """  
      pass

class GetTargetBudgetCode_output:
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAccountBudgetTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAccountBudgetTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AccountBudgetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBudgetCode_input:
   """ Required : 
   budgetCode
   throwEx
   """  
   def __init__(self, obj):
      self.budgetCode:str = obj["budgetCode"]
      self.throwEx:bool = obj["throwEx"]
      pass

class ValidateBudgetCode_output:
   def __init__(self, obj):
      pass

class ValidateGLAccount_input:
   """ Required : 
   bookID
   budgetCodeID
   account
   balanceType
   fiscalYear
   fiscalYearSuffix
   budgetAmt
   budgetStatAmt
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  Book ID  """  
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code ID  """  
      self.account:str = obj["account"]
      """  New value Balance Account  """  
      self.balanceType:str = obj["balanceType"]
      """  Balance Type  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.budgetAmt:int = obj["budgetAmt"]
      """  Current Budget Amount  """  
      self.budgetStatAmt:int = obj["budgetStatAmt"]
      """  Current Budget Statistical Amount  """  
      pass

class ValidateGLAccount_output:
   def __init__(self, obj):
      pass

class ValidateGLBook_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  bookID  """  
      pass

class ValidateGLBook_output:
   def __init__(self, obj):
      pass

