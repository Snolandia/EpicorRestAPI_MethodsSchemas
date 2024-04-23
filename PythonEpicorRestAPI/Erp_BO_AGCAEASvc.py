import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AGCAEASvc
# Description: AGCAEA Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AGCAEAs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AGCAEAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AGCAEAs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCAEARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs",headers=creds) as resp:
           return await resp.json()

async def post_AGCAEAs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AGCAEAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AGCAEARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AGCAEARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AGCAEAs_Company_Period_Fortnight(Company, Period, Fortnight, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AGCAEA item
   Description: Calls GetByID to retrieve the AGCAEA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCAEA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AGCAEARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs(" + Company + "," + Period + "," + Fortnight + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AGCAEAs_Company_Period_Fortnight(Company, Period, Fortnight, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AGCAEA for the service
   Description: Calls UpdateExt to update AGCAEA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AGCAEA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AGCAEARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs(" + Company + "," + Period + "," + Fortnight + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AGCAEAs_Company_Period_Fortnight(Company, Period, Fortnight, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AGCAEA item
   Description: Call UpdateExt to delete AGCAEA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AGCAEA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs(" + Company + "," + Period + "," + Fortnight + ")",headers=creds) as resp:
           return await resp.json()

async def get_AGCAEAs_Company_Period_Fortnight_AGCAEASubmitResults(Company, Period, Fortnight, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AGCAEASubmitResults items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AGCAEASubmitResults1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCAEASubmitResultRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs(" + Company + "," + Period + "," + Fortnight + ")/AGCAEASubmitResults",headers=creds) as resp:
           return await resp.json()

async def get_AGCAEAs_Company_Period_Fortnight_AGCAEASubmitResults_Company_Period_Fortnight_InvoicingPointCode_AFIPCode(Company, Period, Fortnight, InvoicingPointCode, AFIPCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AGCAEASubmitResult item
   Description: Calls GetByID to retrieve the AGCAEASubmitResult item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCAEASubmitResult1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param InvoicingPointCode: Desc: InvoicingPointCode   Required: True   Allow empty value : True
      :param AFIPCode: Desc: AFIPCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AGCAEASubmitResultRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEAs(" + Company + "," + Period + "," + Fortnight + ")/AGCAEASubmitResults(" + Company + "," + Period + "," + Fortnight + "," + InvoicingPointCode + "," + AFIPCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AGCAEASubmitResults(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AGCAEASubmitResults items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AGCAEASubmitResults
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCAEASubmitResultRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEASubmitResults",headers=creds) as resp:
           return await resp.json()

async def post_AGCAEASubmitResults(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AGCAEASubmitResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AGCAEASubmitResultRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AGCAEASubmitResultRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEASubmitResults", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AGCAEASubmitResults_Company_Period_Fortnight_InvoicingPointCode_AFIPCode(Company, Period, Fortnight, InvoicingPointCode, AFIPCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AGCAEASubmitResult item
   Description: Calls GetByID to retrieve the AGCAEASubmitResult item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCAEASubmitResult
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param InvoicingPointCode: Desc: InvoicingPointCode   Required: True   Allow empty value : True
      :param AFIPCode: Desc: AFIPCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AGCAEASubmitResultRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEASubmitResults(" + Company + "," + Period + "," + Fortnight + "," + InvoicingPointCode + "," + AFIPCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AGCAEASubmitResults_Company_Period_Fortnight_InvoicingPointCode_AFIPCode(Company, Period, Fortnight, InvoicingPointCode, AFIPCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AGCAEASubmitResult for the service
   Description: Calls UpdateExt to update AGCAEASubmitResult. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AGCAEASubmitResult
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param InvoicingPointCode: Desc: InvoicingPointCode   Required: True   Allow empty value : True
      :param AFIPCode: Desc: AFIPCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AGCAEASubmitResultRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEASubmitResults(" + Company + "," + Period + "," + Fortnight + "," + InvoicingPointCode + "," + AFIPCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AGCAEASubmitResults_Company_Period_Fortnight_InvoicingPointCode_AFIPCode(Company, Period, Fortnight, InvoicingPointCode, AFIPCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AGCAEASubmitResult item
   Description: Call UpdateExt to delete AGCAEASubmitResult item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AGCAEASubmitResult
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Period: Desc: Period   Required: True   Allow empty value : True
      :param Fortnight: Desc: Fortnight   Required: True
      :param InvoicingPointCode: Desc: InvoicingPointCode   Required: True   Allow empty value : True
      :param AFIPCode: Desc: AFIPCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/AGCAEASubmitResults(" + Company + "," + Period + "," + Fortnight + "," + InvoicingPointCode + "," + AFIPCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCAEAListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAGCAEA, whereClauseAGCAEASubmitResult, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAGCAEA=" + whereClauseAGCAEA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAGCAEASubmitResult=" + whereClauseAGCAEASubmitResult
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(period, fortnight, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "period=" + period
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fortnight=" + fortnight

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveCAEA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveCAEA
   Description: Retrieving CAEA
   OperationID: RetrieveCAEA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveCAEA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveCAEA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Retrieve(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Retrieve
   Description: Retrieving
   OperationID: Retrieve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Retrieve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Retrieve_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPeriodStartDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPeriodStartDate
   Description: Return Period Start Date for Kinetic
   OperationID: GetPeriodStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPeriodStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeriodStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_checkIfCAEAHasBeenAssigned(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method checkIfCAEAHasBeenAssigned
   Description: Check if CAEA Code has been assigned on ARInvoice (Submission Mode = "A"), Apply Date in selected period and Invoice has been posted
   OperationID: checkIfCAEAHasBeenAssigned
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkIfCAEAHasBeenAssigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkIfCAEAHasBeenAssigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAGCAEA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAGCAEA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAGCAEA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAGCAEA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAGCAEA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAGCAEASubmitResult(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAGCAEASubmitResult
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAGCAEASubmitResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAGCAEASubmitResult_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAGCAEASubmitResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AGCAEASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCAEAListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AGCAEAListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCAEARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AGCAEARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCAEASubmitResultRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AGCAEASubmitResultRow] = obj["value"]
      pass

class Erp_Tablesets_AGCAEAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Period:str = obj["Period"]
      """  Period  """  
      self.Fortnight:int = obj["Fortnight"]
      """  Fortnight  """  
      self.PeriodStartDate:str = obj["PeriodStartDate"]
      """  PeriodStartDate  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  PeriodEndDate  """  
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  ProcessDate  """  
      self.CAEA:str = obj["CAEA"]
      """  CAEA  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Key:str = obj["Key"]
      """  CAEAPeriod. Period + Fortnight  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AGCAEARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Period:str = obj["Period"]
      """  Period  """  
      self.Fortnight:int = obj["Fortnight"]
      """  Fortnight  """  
      self.PeriodStartDate:str = obj["PeriodStartDate"]
      """  PeriodStartDate  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  PeriodEndDate  """  
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  ProcessDate  """  
      self.CAEA:str = obj["CAEA"]
      """  CAEA  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Year:int = obj["Year"]
      """  Year  """  
      self.Month:int = obj["Month"]
      """  Month  """  
      self.Key:str = obj["Key"]
      """  CAEAPeriod. Period + Fortnight  """  
      self.Message:str = obj["Message"]
      """  Retrieved from AFIP result  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AGCAEASubmitResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Period:str = obj["Period"]
      """  Period  """  
      self.Fortnight:int = obj["Fortnight"]
      """  Fortnight  """  
      self.InvoicingPointCode:str = obj["InvoicingPointCode"]
      """  InvoicingPointCode  """  
      self.AFIPCode:str = obj["AFIPCode"]
      """  AFIPCode  """  
      self.SubmitDate:str = obj["SubmitDate"]
      """  SubmitDate  """  
      self.InvoiceCount:int = obj["InvoiceCount"]
      """  InvoiceCount  """  
      self.Result:str = obj["Result"]
      """  Result  """  
      self.Message:str = obj["Message"]
      """  Message  """  
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
   period
   fortnight
   """  
   def __init__(self, obj):
      self.period:str = obj["period"]
      self.fortnight:int = obj["fortnight"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AGCAEAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Period:str = obj["Period"]
      """  Period  """  
      self.Fortnight:int = obj["Fortnight"]
      """  Fortnight  """  
      self.PeriodStartDate:str = obj["PeriodStartDate"]
      """  PeriodStartDate  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  PeriodEndDate  """  
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  ProcessDate  """  
      self.CAEA:str = obj["CAEA"]
      """  CAEA  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Key:str = obj["Key"]
      """  CAEAPeriod. Period + Fortnight  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AGCAEAListTableset:
   def __init__(self, obj):
      self.AGCAEAList:list[Erp_Tablesets_AGCAEAListRow] = obj["AGCAEAList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AGCAEARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Period:str = obj["Period"]
      """  Period  """  
      self.Fortnight:int = obj["Fortnight"]
      """  Fortnight  """  
      self.PeriodStartDate:str = obj["PeriodStartDate"]
      """  PeriodStartDate  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  PeriodEndDate  """  
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  ProcessDate  """  
      self.CAEA:str = obj["CAEA"]
      """  CAEA  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Year:int = obj["Year"]
      """  Year  """  
      self.Month:int = obj["Month"]
      """  Month  """  
      self.Key:str = obj["Key"]
      """  CAEAPeriod. Period + Fortnight  """  
      self.Message:str = obj["Message"]
      """  Retrieved from AFIP result  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AGCAEASubmitResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Period:str = obj["Period"]
      """  Period  """  
      self.Fortnight:int = obj["Fortnight"]
      """  Fortnight  """  
      self.InvoicingPointCode:str = obj["InvoicingPointCode"]
      """  InvoicingPointCode  """  
      self.AFIPCode:str = obj["AFIPCode"]
      """  AFIPCode  """  
      self.SubmitDate:str = obj["SubmitDate"]
      """  SubmitDate  """  
      self.InvoiceCount:int = obj["InvoiceCount"]
      """  InvoiceCount  """  
      self.Result:str = obj["Result"]
      """  Result  """  
      self.Message:str = obj["Message"]
      """  Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AGCAEATableset:
   def __init__(self, obj):
      self.AGCAEA:list[Erp_Tablesets_AGCAEARow] = obj["AGCAEA"]
      self.AGCAEASubmitResult:list[Erp_Tablesets_AGCAEASubmitResultRow] = obj["AGCAEASubmitResult"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAGCAEATableset:
   def __init__(self, obj):
      self.AGCAEA:list[Erp_Tablesets_AGCAEARow] = obj["AGCAEA"]
      self.AGCAEASubmitResult:list[Erp_Tablesets_AGCAEASubmitResultRow] = obj["AGCAEASubmitResult"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   period
   fortnight
   """  
   def __init__(self, obj):
      self.period:str = obj["period"]
      self.fortnight:int = obj["fortnight"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AGCAEATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AGCAEATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AGCAEATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AGCAEAListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAGCAEASubmitResult_input:
   """ Required : 
   ds
   period
   fortnight
   invoicingPointCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      self.period:str = obj["period"]
      self.fortnight:int = obj["fortnight"]
      self.invoicingPointCode:str = obj["invoicingPointCode"]
      pass

class GetNewAGCAEASubmitResult_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAGCAEA_input:
   """ Required : 
   ds
   period
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      self.period:str = obj["period"]
      pass

class GetNewAGCAEA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPeriodStartDate_input:
   """ Required : 
   fortnight
   year
   month
   """  
   def __init__(self, obj):
      self.fortnight:int = obj["fortnight"]
      """  fortnight  """  
      self.year:int = obj["year"]
      """  year  """  
      self.month:int = obj["month"]
      """  month  """  
      pass

class GetPeriodStartDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseAGCAEA
   whereClauseAGCAEASubmitResult
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAGCAEA:str = obj["whereClauseAGCAEA"]
      self.whereClauseAGCAEASubmitResult:str = obj["whereClauseAGCAEASubmitResult"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AGCAEATableset] = obj["returnObj"]
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

class RetrieveCAEA_input:
   """ Required : 
   year
   month
   fortnight
   ds
   """  
   def __init__(self, obj):
      self.year:int = obj["year"]
      self.month:int = obj["month"]
      self.fortnight:int = obj["fortnight"]
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

class RetrieveCAEA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

      """  output parameters  """  

class Retrieve_input:
   """ Required : 
   period
   fortnight
   ds
   """  
   def __init__(self, obj):
      self.period:str = obj["period"]
      self.fortnight:int = obj["fortnight"]
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

class Retrieve_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAGCAEATableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAGCAEATableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AGCAEATableset] = obj["ds"]
      pass

      """  output parameters  """  

class checkIfCAEAHasBeenAssigned_input:
   """ Required : 
   CAEA
   periodStartDate
   periodEndDate
   """  
   def __init__(self, obj):
      self.CAEA:str = obj["CAEA"]
      """  CAEA Code  """  
      self.periodStartDate:str = obj["periodStartDate"]
      """  period Start Date  """  
      self.periodEndDate:str = obj["periodEndDate"]
      """  Period End Date  """  
      pass

class checkIfCAEAHasBeenAssigned_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

