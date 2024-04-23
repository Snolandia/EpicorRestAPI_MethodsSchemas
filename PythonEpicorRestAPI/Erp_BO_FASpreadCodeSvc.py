import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FASpreadCodeSvc
# Description: FASpreadCode Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FASpreadCodes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FASpreadCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FASpreadCodes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASpreadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes",headers=creds) as resp:
           return await resp.json()

async def post_FASpreadCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FASpreadCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FASpreadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FASpreadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FASpreadCodes_Company_SpreadCode(Company, SpreadCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FASpreadCode item
   Description: Calls GetByID to retrieve the FASpreadCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FASpreadCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FASpreadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FASpreadCodes_Company_SpreadCode(Company, SpreadCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FASpreadCode for the service
   Description: Calls UpdateExt to update FASpreadCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FASpreadCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FASpreadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FASpreadCodes_Company_SpreadCode(Company, SpreadCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FASpreadCode item
   Description: Call UpdateExt to delete FASpreadCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FASpreadCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_FASpreadCodes_Company_SpreadCode_FASprdDies(Company, SpreadCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FASprdDies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FASprdDies1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASprdDyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")/FASprdDies",headers=creds) as resp:
           return await resp.json()

async def get_FASpreadCodes_Company_SpreadCode_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SpreadCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FASprdDy item
   Description: Calls GetByID to retrieve the FASprdDy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FASprdDy1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASpreadCodes(" + Company + "," + SpreadCode + ")/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FASprdDies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FASprdDies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FASprdDies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASprdDyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies",headers=creds) as resp:
           return await resp.json()

async def post_FASprdDies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FASprdDies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SpreadCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FASprdDy item
   Description: Calls GetByID to retrieve the FASprdDy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FASprdDy
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SpreadCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FASprdDy for the service
   Description: Calls UpdateExt to update FASprdDy. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FASprdDy
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FASprdDyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FASprdDies_Company_SpreadCode_FiscalYear_FiscalYearSuffix_FiscalPeriod_FiscalCalendarID(Company, SpreadCode, FiscalYear, FiscalYearSuffix, FiscalPeriod, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FASprdDy item
   Description: Call UpdateExt to delete FASprdDy item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FASprdDy
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SpreadCode: Desc: SpreadCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/FASprdDies(" + Company + "," + SpreadCode + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + FiscalCalendarID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FASpreadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFASpread, whereClauseFASprdDy, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFASpread=" + whereClauseFASpread
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFASprdDy=" + whereClauseFASprdDy
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(spreadCode, epicorHeaders = None):
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
   params += "spreadCode=" + spreadCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFASprdDy(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFASprdDy
   Description: This is to delete ttFASprdDy record based on the SpreadCode, Fiscal Year and Period.
   OperationID: DeleteFASprdDy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFASprdDy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFASprdDy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportSpreadCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportSpreadCode
   Description: Exports the Spread Code data to a CSV file.
   OperationID: ExportSpreadCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSpreadCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSpreadCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSprdDy(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSprdDy
   Description: This procedure is to generate ttFASprdDy records based on the Spread Type and
the parameters entered by the user in the Generate Values form.
   OperationID: GenerateSprdDy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSprdDy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSprdDy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectList
   Description: Get list of descriptions for the Export combos.
   OperationID: GetSelectList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Desc List
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportSpreadCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportSpreadCode
   Description: Imports the Spread Code data from a CSV file.
   OperationID: ImportSpreadCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportSpreadCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSpreadCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDefaultsForGenerate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDefaultsForGenerate
   Description: This procedure sets the Defalut values of the Parameters in the Generate Values form.
   OperationID: SetDefaultsForGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDefaultsForGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultsForGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportCall
   Description: Import Call
   OperationID: ImportCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportCall
   Description: Export Call
   OperationID: ExportCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFASpread(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFASpread
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFASpread
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFASpread_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFASpread_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFASprdDy(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFASprdDy
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFASprdDy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFASprdDy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFASprdDy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FASpreadCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASprdDyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FASprdDyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FASpreadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FASpreadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FASpreadRow] = obj["value"]
      pass

class Erp_Tablesets_FASprdDyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code spread days.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  Identifier of the spread code table.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the spread code.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the spread day.  """  
      self.Days:int = obj["Days"]
      """  Day factor. The factor is used to calculate the fiscal periods depreciation amount from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SpreadValue:int = obj["SpreadValue"]
      """  This could be the number of days, annual charge, period charge or any value that will be used to calculate the fiscal periods depreciation amount. This factor could be used in multiple scenarios but one common usage would be to calculate period depreciations from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  """  
      self.GlobalFASprdDy:bool = obj["GlobalFASprdDy"]
      """  Marks this FASprdDy as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.SpreadCodeDescription:str = obj["SpreadCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FASpreadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code table.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  identifier of the spread code table.  """  
      self.Description:str = obj["Description"]
      """  Description of the spread code.  """  
      self.SpreadType:str = obj["SpreadType"]
      """  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  """  
      self.GlobalFASpread:bool = obj["GlobalFASpread"]
      """  Marks this FASpread as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssignValues:str = obj["AssignValues"]
      """  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  """  
      self.AssignedValue:int = obj["AssignedValue"]
      """  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  """  
      self.StartYear:int = obj["StartYear"]
      """  Start Year parameter for Spread Code Entry Generate Values  """  
      self.StartYearSuffix:str = obj["StartYearSuffix"]
      """  Start Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.EndYear:int = obj["EndYear"]
      """  End Year parameter for Spread Code Entry Generate Values  """  
      self.EndYearSuffix:str = obj["EndYearSuffix"]
      """  End Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.OverrideValues:bool = obj["OverrideValues"]
      """  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FASpreadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code table.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  identifier of the spread code table.  """  
      self.Description:str = obj["Description"]
      """  Description of the spread code.  """  
      self.SpreadType:str = obj["SpreadType"]
      """  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  """  
      self.GlobalFASpread:bool = obj["GlobalFASpread"]
      """  Marks this FASpread as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssignValues:str = obj["AssignValues"]
      """  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  """  
      self.AssignedValue:int = obj["AssignedValue"]
      """  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  """  
      self.StartYear:int = obj["StartYear"]
      """  Start Year parameter for Spread Code Entry Generate Values  """  
      self.StartYearSuffix:str = obj["StartYearSuffix"]
      """  Start Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.EndYear:int = obj["EndYear"]
      """  End Year parameter for Spread Code Entry Generate Values  """  
      self.EndYearSuffix:str = obj["EndYearSuffix"]
      """  End Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.OverrideValues:bool = obj["OverrideValues"]
      """  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   spreadCode
   """  
   def __init__(self, obj):
      self.spreadCode:str = obj["spreadCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteFASprdDy_input:
   """ Required : 
   spreadCode
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.spreadCode:str = obj["spreadCode"]
      """  SpreadCode of record that is being updated.  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  FiscalYear of record that is being updated.  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  FiscalYearSuffix of record that is being updated.  """  
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      """  FiscalPeriod of record that is being updated.  """  
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

class DeleteFASprdDy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_FASprdDyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code spread days.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  Identifier of the spread code table.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the spread code.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the spread day.  """  
      self.Days:int = obj["Days"]
      """  Day factor. The factor is used to calculate the fiscal periods depreciation amount from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SpreadValue:int = obj["SpreadValue"]
      """  This could be the number of days, annual charge, period charge or any value that will be used to calculate the fiscal periods depreciation amount. This factor could be used in multiple scenarios but one common usage would be to calculate period depreciations from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  """  
      self.GlobalFASprdDy:bool = obj["GlobalFASprdDy"]
      """  Marks this FASprdDy as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.SpreadCodeDescription:str = obj["SpreadCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FASpreadCodeTableset:
   def __init__(self, obj):
      self.FASpread:list[Erp_Tablesets_FASpreadRow] = obj["FASpread"]
      self.FASprdDy:list[Erp_Tablesets_FASprdDyRow] = obj["FASprdDy"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FASpreadImExDataTableset:
   def __init__(self, obj):
      self.FaSprdDyImEx:list[Erp_Tablesets_FaSprdDyImExRow] = obj["FaSprdDyImEx"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FASpreadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code table.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  identifier of the spread code table.  """  
      self.Description:str = obj["Description"]
      """  Description of the spread code.  """  
      self.SpreadType:str = obj["SpreadType"]
      """  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  """  
      self.GlobalFASpread:bool = obj["GlobalFASpread"]
      """  Marks this FASpread as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssignValues:str = obj["AssignValues"]
      """  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  """  
      self.AssignedValue:int = obj["AssignedValue"]
      """  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  """  
      self.StartYear:int = obj["StartYear"]
      """  Start Year parameter for Spread Code Entry Generate Values  """  
      self.StartYearSuffix:str = obj["StartYearSuffix"]
      """  Start Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.EndYear:int = obj["EndYear"]
      """  End Year parameter for Spread Code Entry Generate Values  """  
      self.EndYearSuffix:str = obj["EndYearSuffix"]
      """  End Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.OverrideValues:bool = obj["OverrideValues"]
      """  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FASpreadListTableset:
   def __init__(self, obj):
      self.FASpreadList:list[Erp_Tablesets_FASpreadListRow] = obj["FASpreadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FASpreadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code table.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  identifier of the spread code table.  """  
      self.Description:str = obj["Description"]
      """  Description of the spread code.  """  
      self.SpreadType:str = obj["SpreadType"]
      """  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "ANNUAL"  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  """  
      self.GlobalFASpread:bool = obj["GlobalFASpread"]
      """  Marks this FASpread as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssignValues:str = obj["AssignValues"]
      """  Parameter for Spread Code Entry Generate Values to determine how the detail values are going to be generated. Valid values are: "NUMDAYS", "PROAMT" or NOTASSIGN.  """  
      self.AssignedValue:int = obj["AssignedValue"]
      """  Parameter for Spread Code Entry Generate Values that contains the amount entered by the user that is going to be prorated.  """  
      self.StartYear:int = obj["StartYear"]
      """  Start Year parameter for Spread Code Entry Generate Values  """  
      self.StartYearSuffix:str = obj["StartYearSuffix"]
      """  Start Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.EndYear:int = obj["EndYear"]
      """  End Year parameter for Spread Code Entry Generate Values  """  
      self.EndYearSuffix:str = obj["EndYearSuffix"]
      """  End Year Suffix parameter for Spread Code Entry Generate Values  """  
      self.OverrideValues:bool = obj["OverrideValues"]
      """  Parameter for Spread Code Entry Generate Values that indicates if the already existin values are going to be overridden.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FaSprdDyImExRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the spread code spread days.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  Identifier of the spread code table.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the spread code.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the spread day.  """  
      self.Days:int = obj["Days"]
      """  Day factor. The factor is used to calculate the fiscal periods depreciation amount from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SpreadValue:int = obj["SpreadValue"]
      """  This could be the number of days, annual charge, period charge or any value that will be used to calculate the fiscal periods depreciation amount. This factor could be used in multiple scenarios but one common usage would be to calculate period depreciations from the year depreciation amount. When there are 200 working days in a year and 15 working days in a fiscal period then the depreciation amount of the fiscal period is 15 / 200 * year depreciation amount.  """  
      self.GlobalFASprdDy:bool = obj["GlobalFASprdDy"]
      """  Marks this FASprdDy as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpreadType:str = obj["SpreadType"]
      """  Identifies the type of Spread Code.  This will define whether the spread will be done over years or periods.  Valid values are: "PERIOD" or "YEAR"  """  
      self.Description:str = obj["Description"]
      """  Description of the spread code.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtFASpreadCodeTableset:
   def __init__(self, obj):
      self.FASpread:list[Erp_Tablesets_FASpreadRow] = obj["FASpread"]
      self.FASprdDy:list[Erp_Tablesets_FASprdDyRow] = obj["FASprdDy"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportCall_input:
   """ Required : 
   fileName
   inStartCode
   inEndCode
   inSelectBy
   inSelectType
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      self.inStartCode:str = obj["inStartCode"]
      self.inEndCode:str = obj["inEndCode"]
      self.inSelectBy:str = obj["inSelectBy"]
      self.inSelectType:str = obj["inSelectType"]
      pass

class ExportCall_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ExportSpreadCode_input:
   """ Required : 
   inStartCode
   inEndCode
   inSelectBy
   inSelectType
   """  
   def __init__(self, obj):
      self.inStartCode:str = obj["inStartCode"]
      """  Starting Spread Code  """  
      self.inEndCode:str = obj["inEndCode"]
      """  Ending Spread Code  """  
      self.inSelectBy:str = obj["inSelectBy"]
      """  Select By option  """  
      self.inSelectType:str = obj["inSelectType"]
      """  Select Type option  """  
      pass

class ExportSpreadCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FASpreadImExDataTableset] = obj["returnObj"]
      pass

class GenerateSprdDy_input:
   """ Required : 
   iPSpreadCode
   ds
   """  
   def __init__(self, obj):
      self.iPSpreadCode:str = obj["iPSpreadCode"]
      """  SpreadCode of record that is being updated.  """  
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

class GenerateSprdDy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   spreadCode
   """  
   def __init__(self, obj):
      self.spreadCode:str = obj["spreadCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FASpreadCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FASpreadCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FASpreadCodeTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Code Description List  """  
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
      self.returnObj:list[Erp_Tablesets_FASpreadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFASprdDy_input:
   """ Required : 
   ds
   spreadCode
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      self.spreadCode:str = obj["spreadCode"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class GetNewFASprdDy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFASpread_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

class GetNewFASpread_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFASpread
   whereClauseFASprdDy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFASpread:str = obj["whereClauseFASpread"]
      self.whereClauseFASprdDy:str = obj["whereClauseFASprdDy"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FASpreadCodeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectList_input:
   """ Required : 
   inListType
   """  
   def __init__(self, obj):
      self.inListType:str = obj["inListType"]
      """  The type of list that is going to be returned  """  
      pass

class GetSelectList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.selectList:str = obj["parameters"]
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

class ImportCall_input:
   """ Required : 
   fileName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      pass

class ImportCall_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.allImported:bool = obj["allImported"]
      pass

      """  output parameters  """  

class ImportSpreadCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadImExDataTableset] = obj["ds"]
      pass

class ImportSpreadCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FASpreadCodeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.allImported:bool = obj["allImported"]
      self.ds:list[Erp_Tablesets_FASpreadImExDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetDefaultsForGenerate_input:
   """ Required : 
   inCalendarID
   inSpreadType
   """  
   def __init__(self, obj):
      self.inCalendarID:str = obj["inCalendarID"]
      """  Fiscal Calendar ID  """  
      self.inSpreadType:str = obj["inSpreadType"]
      """  Spread Code Type  """  
      pass

class SetDefaultsForGenerate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outCurrYear:int = obj["parameters"]
      self.outCurrYearSuffix:str = obj["parameters"]
      self.outLastYear:int = obj["parameters"]
      self.outLastYearSuffix:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFASpreadCodeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFASpreadCodeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FASpreadCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

