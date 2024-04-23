import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SalesRepQuotaSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SalesRepQuotas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesRepQuotas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesRepQuotas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SRepQHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas",headers=creds) as resp:
           return await resp.json()

async def post_SalesRepQuotas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesRepQuotas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SRepQHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SRepQHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesRepQuotas_Company_SalesRepCode_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, SalesRepCode, FiscalCalendarID, FiscalYear, FiscalYearSuffix, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesRepQuota item
   Description: Calls GetByID to retrieve the SalesRepQuota item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesRepQuota
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SRepQHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas(" + Company + "," + SalesRepCode + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesRepQuotas_Company_SalesRepCode_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, SalesRepCode, FiscalCalendarID, FiscalYear, FiscalYearSuffix, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesRepQuota for the service
   Description: Calls UpdateExt to update SalesRepQuota. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesRepQuota
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SRepQHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas(" + Company + "," + SalesRepCode + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesRepQuotas_Company_SalesRepCode_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, SalesRepCode, FiscalCalendarID, FiscalYear, FiscalYearSuffix, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesRepQuota item
   Description: Call UpdateExt to delete SalesRepQuota item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesRepQuota
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas(" + Company + "," + SalesRepCode + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesRepQuotas_Company_SalesRepCode_FiscalCalendarID_FiscalYear_FiscalYearSuffix_SRepQDtls(Company, SalesRepCode, FiscalCalendarID, FiscalYear, FiscalYearSuffix, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SRepQDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SRepQDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SRepQDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas(" + Company + "," + SalesRepCode + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")/SRepQDtls",headers=creds) as resp:
           return await resp.json()

async def get_SalesRepQuotas_Company_SalesRepCode_FiscalCalendarID_FiscalYear_FiscalYearSuffix_SRepQDtls_Company_SalesRepCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SalesRepCode, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SRepQDtl item
   Description: Calls GetByID to retrieve the SRepQDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SRepQDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SRepQDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SalesRepQuotas(" + Company + "," + SalesRepCode + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")/SRepQDtls(" + Company + "," + SalesRepCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SRepQDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SRepQDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SRepQDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SRepQDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SRepQDtls",headers=creds) as resp:
           return await resp.json()

async def post_SRepQDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SRepQDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SRepQDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SRepQDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SRepQDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SRepQDtls_Company_SalesRepCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SalesRepCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SRepQDtl item
   Description: Calls GetByID to retrieve the SRepQDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SRepQDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SRepQDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SRepQDtls(" + Company + "," + SalesRepCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SRepQDtls_Company_SalesRepCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SalesRepCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SRepQDtl for the service
   Description: Calls UpdateExt to update SRepQDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SRepQDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SRepQDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SRepQDtls(" + Company + "," + SalesRepCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SRepQDtls_Company_SalesRepCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SalesRepCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SRepQDtl item
   Description: Call UpdateExt to delete SRepQDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SRepQDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/SRepQDtls(" + Company + "," + SalesRepCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SRepQHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSRepQHed, whereClauseSRepQDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSRepQHed=" + whereClauseSRepQHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSRepQDtl=" + whereClauseSRepQDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(salesRepCode, fiscalCalendarID, fiscalYear, fiscalYearSuffix, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "salesRepCode=" + salesRepCode
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
   params += "fiscalYear=" + fiscalYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYearSuffix=" + fiscalYearSuffix

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlQuotaAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlQuotaAmt
   Description: This method updates the DispTotalQuotaAmt and the QuotaAmt of the SRepQHed
when the SRepQDtl.QuotaAmt changes.
   OperationID: ChangeDtlQuotaAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlQuotaAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlQuotaAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePerCodeOrAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePerCodeOrAmount
   Description: This method updates the DispTotalQuotaAmt when the QuotaPerCode or QuotaAmt changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSalesRepCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSalesRepCode
   Description: This method validates if sales quota exists when changing the Salesperson field.
   OperationID: ChangeSalesRepCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSalesRepCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSalesRepCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSalesRepCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSalesRepCode
   Description: Validate salesRepCode
   OperationID: ValidateSalesRepCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSalesRepCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSalesRepCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopySalesQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopySalesQuota
   Description: This method copies the entire Sales Quota from a valid fiscal year to a new Fiscal Year.
   OperationID: CopySalesQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopySalesQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopySalesQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSalesQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSalesQuota
   Description: This method deletes the entire Sales Quota of a valid fiscal year.
   OperationID: DeleteSalesQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSalesQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSalesQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalYear(epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalYear
   Description: This method returns fiscal year/suffix based on todays date
   OperationID: GetFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalYear
   Description: This method checks to see if the FiscalYear/FiscalYearSuffix selected is a valid year
   OperationID: ValidateFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSRepQHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSRepQHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSRepQHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSRepQHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSRepQHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSRepQDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSRepQDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSRepQDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSRepQDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSRepQDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepQuotaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SRepQDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SRepQDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SRepQHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SRepQHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SRepQHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SRepQHedRow] = obj["value"]
      pass

class Erp_Tablesets_SRepQDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales rep that this Budget is for.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this Quota balance record.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the Quota record.  """  
      self.QuotaAmt:int = obj["QuotaAmt"]
      """  Quota amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SRepQHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales rep that this Budget is for.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this Quota record.  """  
      self.TotalQuotaAmt:int = obj["TotalQuotaAmt"]
      """  Total Quota amount for the fiscal year.  This is a summary of SRepQDtl.QuotaAmt. Indirectly maintained via SRepQDtl write trigger.  """  
      self.QuotaPerCode:str = obj["QuotaPerCode"]
      """  Indicates if the Quota amount is period or annual amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QuotaAmt:int = obj["QuotaAmt"]
      self.DispTotalQuotaAmt:int = obj["DispTotalQuotaAmt"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      """  Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SRepQHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales rep that this Budget is for.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this Quota record.  """  
      self.TotalQuotaAmt:int = obj["TotalQuotaAmt"]
      """  Total Quota amount for the fiscal year.  This is a summary of SRepQDtl.QuotaAmt. Indirectly maintained via SRepQDtl write trigger.  """  
      self.QuotaPerCode:str = obj["QuotaPerCode"]
      """  Indicates if the Quota amount is period or annual amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QuotaAmt:int = obj["QuotaAmt"]
      self.DispTotalQuotaAmt:int = obj["DispTotalQuotaAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeDtlQuotaAmt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

class ChangeDtlQuotaAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePerCodeOrAmount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

class ChangePerCodeOrAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSalesRepCode_input:
   """ Required : 
   ProposedSalesRepCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedSalesRepCode:str = obj["ProposedSalesRepCode"]
      """  The proposed Salesperson code.  """  
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

class ChangeSalesRepCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopySalesQuota_input:
   """ Required : 
   fromFiscalYear
   fromFiscalYearSuffix
   adjustmentPct
   toFiscalYear
   toFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.fromFiscalYear:int = obj["fromFiscalYear"]
      """  The Fiscal Year of the Sales Quota to copy.  """  
      self.fromFiscalYearSuffix:str = obj["fromFiscalYearSuffix"]
      """  The Fiscal Year Suffix of the Sales Quota to copy.  """  
      self.adjustmentPct:int = obj["adjustmentPct"]
      """  The Adjustment Percentage by which to adjust the numbers
            for the Target Fiscal Year. If 0 then quota will be copied as is.  """  
      self.toFiscalYear:int = obj["toFiscalYear"]
      """  The Target Fiscal Year for the new quota.  """  
      self.toFiscalYearSuffix:str = obj["toFiscalYearSuffix"]
      """  The Target Fiscal Year Suffix for the new quota.  """  
      pass

class CopySalesQuota_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   salesRepCode
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteSalesQuota_input:
   """ Required : 
   inpFiscalYear
   inpFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.inpFiscalYear:int = obj["inpFiscalYear"]
      """  The Fiscal Year of the Sales Quota to delete.  """  
      self.inpFiscalYearSuffix:str = obj["inpFiscalYearSuffix"]
      """  The Fiscal Year Suffix of the Sales Quota to delete.  """  
      pass

class DeleteSalesQuota_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_SRepQDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales rep that this Budget is for.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this Quota balance record.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the Quota record.  """  
      self.QuotaAmt:int = obj["QuotaAmt"]
      """  Quota amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SRepQHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales rep that this Budget is for.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this Quota record.  """  
      self.TotalQuotaAmt:int = obj["TotalQuotaAmt"]
      """  Total Quota amount for the fiscal year.  This is a summary of SRepQDtl.QuotaAmt. Indirectly maintained via SRepQDtl write trigger.  """  
      self.QuotaPerCode:str = obj["QuotaPerCode"]
      """  Indicates if the Quota amount is period or annual amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QuotaAmt:int = obj["QuotaAmt"]
      self.DispTotalQuotaAmt:int = obj["DispTotalQuotaAmt"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      """  Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SRepQHedListTableset:
   def __init__(self, obj):
      self.SRepQHedList:list[Erp_Tablesets_SRepQHedListRow] = obj["SRepQHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SRepQHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales rep that this Budget is for.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this Quota record.  """  
      self.TotalQuotaAmt:int = obj["TotalQuotaAmt"]
      """  Total Quota amount for the fiscal year.  This is a summary of SRepQDtl.QuotaAmt. Indirectly maintained via SRepQDtl write trigger.  """  
      self.QuotaPerCode:str = obj["QuotaPerCode"]
      """  Indicates if the Quota amount is period or annual amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QuotaAmt:int = obj["QuotaAmt"]
      self.DispTotalQuotaAmt:int = obj["DispTotalQuotaAmt"]
      self.BitFlag:int = obj["BitFlag"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesRepQuotaTableset:
   def __init__(self, obj):
      self.SRepQHed:list[Erp_Tablesets_SRepQHedRow] = obj["SRepQHed"]
      self.SRepQDtl:list[Erp_Tablesets_SRepQDtlRow] = obj["SRepQDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSalesRepQuotaTableset:
   def __init__(self, obj):
      self.SRepQHed:list[Erp_Tablesets_SRepQHedRow] = obj["SRepQHed"]
      self.SRepQDtl:list[Erp_Tablesets_SRepQDtlRow] = obj["SRepQDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   salesRepCode
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fiscalCalendarID:str = obj["parameters"]
      self.fiscalYear:int = obj["parameters"]
      self.fiscalYearSuffix:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_SRepQHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSRepQDtl_input:
   """ Required : 
   ds
   salesRepCode
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      self.salesRepCode:str = obj["salesRepCode"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class GetNewSRepQDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSRepQHed_input:
   """ Required : 
   ds
   salesRepCode
   fiscalCalendarID
   fiscalYear
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      self.salesRepCode:str = obj["salesRepCode"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      pass

class GetNewSRepQHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSRepQHed
   whereClauseSRepQDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSRepQHed:str = obj["whereClauseSRepQHed"]
      self.whereClauseSRepQDtl:str = obj["whereClauseSRepQDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesRepQuotaTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesRepQuotaTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepQuotaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFiscalYear_input:
   """ Required : 
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year to test  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix to test  """  
      pass

class ValidateFiscalYear_output:
   def __init__(self, obj):
      pass

class ValidateSalesRepCode_input:
   """ Required : 
   ProposedSalesRepCode
   """  
   def __init__(self, obj):
      self.ProposedSalesRepCode:str = obj["ProposedSalesRepCode"]
      pass

class ValidateSalesRepCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.salesRepName:str = obj["parameters"]
      pass

      """  output parameters  """  

