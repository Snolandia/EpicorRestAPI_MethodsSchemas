import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ClosePeriodSvc
# Description: Close Period BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ClosePeriods(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ClosePeriods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ClosePeriods
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/ClosePeriods",headers=creds) as resp:
           return await resp.json()

async def post_ClosePeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ClosePeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBookPerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBookPerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/ClosePeriods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ClosePeriods_Company_BookID_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, BookID, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ClosePeriod item
   Description: Calls GetByID to retrieve the ClosePeriod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ClosePeriod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/ClosePeriods(" + Company + "," + BookID + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ClosePeriods_Company_BookID_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, BookID, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ClosePeriod for the service
   Description: Calls UpdateExt to update ClosePeriod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ClosePeriod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBookPerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/ClosePeriods(" + Company + "," + BookID + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ClosePeriods_Company_BookID_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, BookID, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ClosePeriod item
   Description: Call UpdateExt to delete ClosePeriod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ClosePeriod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/ClosePeriods(" + Company + "," + BookID + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBookPerParameters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBookPerParameters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBookPerParameters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookPerParametersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/GLBookPerParameters",headers=creds) as resp:
           return await resp.json()

async def post_GLBookPerParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBookPerParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBookPerParametersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBookPerParametersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/GLBookPerParameters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBookPerParameters_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBookPerParameter item
   Description: Calls GetByID to retrieve the GLBookPerParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBookPerParameter
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookPerParametersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/GLBookPerParameters(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBookPerParameters_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBookPerParameter for the service
   Description: Calls UpdateExt to update GLBookPerParameter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBookPerParameter
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBookPerParametersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/GLBookPerParameters(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBookPerParameters_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBookPerParameter item
   Description: Call UpdateExt to delete GLBookPerParameter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBookPerParameter
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/GLBookPerParameters(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookPerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBookPer, whereClauseGLBookPerParameters, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLBookPer=" + whereClauseGLBookPer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBookPerParameters=" + whereClauseGLBookPerParameters
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bookID, fiscalCalendarID, fiscalYear, fiscalYearSuffix, fiscalPeriod, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
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
   params += "bookID=" + bookID
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalPeriod=" + fiscalPeriod

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CloseAllPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseAllPeriods
   Description: Close all periods in a Fiscal Year
   OperationID: CloseAllPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseAllPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAllPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClosedPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClosedPeriod
   Description: Run when the ClosedPeriod field is changed.
   OperationID: OnChangeClosedPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClosedPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClosedPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClosedPeriod_IfCloseLastClosingPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClosedPeriod_IfCloseLastClosingPer
   Description: Check if the period chosen is the last closing period.
   OperationID: OnChangeClosedPeriod_IfCloseLastClosingPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClosedPeriod_IfCloseLastClosingPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClosedPeriod_IfCloseLastClosingPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClosedPeriod_IfCloseWhenPrevOpen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClosedPeriod_IfCloseWhenPrevOpen
   Description: Check, if earlier open periods exist.
   OperationID: OnChangeClosedPeriod_IfCloseWhenPrevOpen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClosedPeriod_IfCloseWhenPrevOpen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClosedPeriod_IfCloseWhenPrevOpen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultParametersWithData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultParametersWithData
   Description: Get default parameters with rows.
   OperationID: GetDefaultParametersWithData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultParametersWithData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultParametersWithData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWithParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWithParams
   Description: Get GLBookPer Rows - extended version, with input parameters.
   OperationID: GetRowsWithParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWithParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDWithParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDWithParams
   Description: Get Close Periods by ID - extended version, with parameters.
   OperationID: GetByIDWithParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDWithParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDWithParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBookPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBookPer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBookPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBookPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBookPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookPerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookPerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookPerParametersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookPerParametersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookPerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookPerRow] = obj["value"]
      pass

class Erp_Tablesets_GLBookPerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  This value will be incremented within the fiscal year/suffix and closing periods of that fiscal year/suffix.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.ClosedPeriod:bool = obj["ClosedPeriod"]
      """  Indicates if the Fiscal Period is closed in the General Ledger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CloseFiscalPeriodDisp:str = obj["CloseFiscalPeriodDisp"]
      """  Display field for CloseFiscalPeriod - if CloseFiscalPeriod <> 0, value is "Yes", otherwise value is "".  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.FiscalYrDescription:str = obj["FiscalYrDescription"]
      """  Fiscal year description.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookPerParametersRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.FiscalCalendarDescription:str = obj["FiscalCalendarDescription"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookPerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  This value will be incremented within the fiscal year/suffix and closing periods of that fiscal year/suffix.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.ClosedPeriod:bool = obj["ClosedPeriod"]
      """  Indicates if the Fiscal Period is closed in the General Ledger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CloseFiscalPeriodDisp:str = obj["CloseFiscalPeriodDisp"]
      """  Display field for CloseFiscalPeriod - if CloseFiscalPeriod <> 0, value is "Yes", otherwise value is "".  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CloseAllPeriods_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  BookID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  FiscalYear  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  ipFiscalYearSuffix  """  
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

class CloseAllPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   bookID
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ClosePeriodTableset:
   def __init__(self, obj):
      self.GLBookPer:list[Erp_Tablesets_GLBookPerRow] = obj["GLBookPer"]
      self.GLBookPerParameters:list[Erp_Tablesets_GLBookPerParametersRow] = obj["GLBookPerParameters"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBookPerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  This value will be incremented within the fiscal year/suffix and closing periods of that fiscal year/suffix.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.ClosedPeriod:bool = obj["ClosedPeriod"]
      """  Indicates if the Fiscal Period is closed in the General Ledger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CloseFiscalPeriodDisp:str = obj["CloseFiscalPeriodDisp"]
      """  Display field for CloseFiscalPeriod - if CloseFiscalPeriod <> 0, value is "Yes", otherwise value is "".  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.FiscalYrDescription:str = obj["FiscalYrDescription"]
      """  Fiscal year description.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookPerListTableset:
   def __init__(self, obj):
      self.GLBookPerList:list[Erp_Tablesets_GLBookPerListRow] = obj["GLBookPerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBookPerParametersRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.FiscalCalendarDescription:str = obj["FiscalCalendarDescription"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookPerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  This value will be incremented within the fiscal year/suffix and closing periods of that fiscal year/suffix.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.ClosedPeriod:bool = obj["ClosedPeriod"]
      """  Indicates if the Fiscal Period is closed in the General Ledger.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CloseFiscalPeriodDisp:str = obj["CloseFiscalPeriodDisp"]
      """  Display field for CloseFiscalPeriod - if CloseFiscalPeriod <> 0, value is "Yes", otherwise value is "".  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtClosePeriodTableset:
   def __init__(self, obj):
      self.GLBookPer:list[Erp_Tablesets_GLBookPerRow] = obj["GLBookPer"]
      self.GLBookPerParameters:list[Erp_Tablesets_GLBookPerParametersRow] = obj["GLBookPerParameters"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDWithParams_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPeriod
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      pass

class GetByIDWithParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   bookID
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
      pass

class GetDefaultParametersWithData_input:
   """ Required : 
   ipBookID
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      pass

class GetDefaultParametersWithData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBookPerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBookPer_input:
   """ Required : 
   ds
   bookID
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetNewGLBookPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsWithParams_input:
   """ Required : 
   bookID
   fiscalCalendarID
   fiscalCalendarDescription
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalCalendarDescription:str = obj["fiscalCalendarDescription"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetRowsWithParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseGLBookPer
   whereClauseGLBookPerParameters
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBookPer:str = obj["whereClauseGLBookPer"]
      self.whereClauseGLBookPerParameters:str = obj["whereClauseGLBookPerParameters"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ClosePeriodTableset] = obj["returnObj"]
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

class OnChangeClosedPeriod_IfCloseLastClosingPer_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPeriod
   ipCloseFiscalPeriod
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      self.ipCloseFiscalPeriod:int = obj["ipCloseFiscalPeriod"]
      pass

class OnChangeClosedPeriod_IfCloseLastClosingPer_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeClosedPeriod_IfCloseWhenPrevOpen_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPeriod
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      pass

class OnChangeClosedPeriod_IfCloseWhenPrevOpen_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeClosedPeriod_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:bool = obj["ipProposedValue"]
      """  Value that the user has entered (yes/no)  """  
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

class OnChangeClosedPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opCloseAll:bool = obj["opCloseAll"]
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtClosePeriodTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtClosePeriodTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

