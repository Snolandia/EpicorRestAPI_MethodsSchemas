import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLAcctDispSvc
# Description: Business Object Used by GL Searches
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLAcctDisps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAcctDisps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAcctDisps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAcctDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/GLAcctDisps",headers=creds) as resp:
           return await resp.json()

async def post_GLAcctDisps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAcctDisps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAcctDispRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAcctDispRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/GLAcctDisps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAcctDisps_Company_COACode_GLAccount(Company, COACode, GLAccount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAcctDisp item
   Description: Calls GetByID to retrieve the GLAcctDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAcctDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAcctDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/GLAcctDisps(" + Company + "," + COACode + "," + GLAccount + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAcctDisps_Company_COACode_GLAccount(Company, COACode, GLAccount, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAcctDisp for the service
   Description: Calls UpdateExt to update GLAcctDisp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAcctDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAcctDispRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/GLAcctDisps(" + Company + "," + COACode + "," + GLAccount + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAcctDisps_Company_COACode_GLAccount(Company, COACode, GLAccount, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAcctDisp item
   Description: Call UpdateExt to delete GLAcctDisp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAcctDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/GLAcctDisps(" + Company + "," + COACode + "," + GLAccount + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAcctDispListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLAcctDisp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseGLAcctDisp=" + whereClauseGLAcctDisp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, glAccount, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glAccount=" + glAccount

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_InvokeBalanceAcctSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InvokeBalanceAcctSearch
   Description: Purpose:
Parameters:
<param name="WhereClauseGLAcctDisp">GLAcctDisp search clause</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: InvokeBalanceAcctSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvokeBalanceAcctSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeBalanceAcctSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList2
   Description: Purpose:
Parameters:
<param name="WhereClause">GLAcctDisp search clause</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="includeInactive">includeInactive</param><param name="morePages">More Pages</param>
Notes:
   OperationID: GetList2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCBOnly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCBOnly
   Description: Purpose:
Parameters:
<param name="WhereClause">GLAcctDisp search clause</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="includeDynamic">Include Dynamic</param><param name="morePages">More Pages</param>
Notes:
   OperationID: GetListCBOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCBOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCBOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchList
   Description: Search GLAccount in DataSetList mode.  This will include dynamic segments unless excluded via where clause.
   OperationID: GLAccountSearchList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDispAccountGeneral(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDispAccountGeneral
   Description: Public method for calling GL library - GLAcctLib and method CheckDispAccountGeneral from UI GL plug-in.
   OperationID: CheckDispAccountGeneral
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDispAccountGeneral_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDispAccountGeneral_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDispAcctGLB(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDispAcctGLB
   Description: Public method for calling GL library - GLAcctLib and method CheckDispAcctGLB from UI GL plug-in.
   OperationID: CheckDispAcctGLB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDispAcctGLB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDispAcctGLB_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchListPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchListPeriod
   Description: Search GLAccount used by Kinetic. List search type
   OperationID: GLAccountSearchListPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchListPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchListPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchRowsPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchRowsPeriod
   Description: Search GLAccount used by Kinetic. Rows search type
   OperationID: GLAccountSearchRowsPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchRowsPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchRowsPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchFilter
   Description: Search GLAccount with account filter applied
   OperationID: GLAccountSearchFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCBOnlyPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCBOnlyPeriod
   Description: Search GLAccount CBOnlyPeriod
   OperationID: GetListCBOnlyPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCBOnlyPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCBOnlyPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAcctDisp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAcctDisp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAcctDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAcctDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAcctDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAcctDispSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAcctDispListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAcctDispListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAcctDispRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAcctDispRow] = obj["value"]
      pass

class Erp_Tablesets_GLAcctDispListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to the max length of 65.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
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
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies whether or not this display account is a balance anccount and the type of balance it represents.  S= Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  A null value indicates the GL Account is not a balance account but an actual GL Account.  """  
      self.CatType:str = obj["CatType"]
      """   Indicates if this cateory is reatled to a balance sheet account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.IsGLAccount:bool = obj["IsGLAccount"]
      """  Indicates if this display account record is a valid GL Account.  this may be a valid GL Account for the controlled sequence and/or a fully resolved GL Account by the Posting Engine.  """  
      self.IsBalanceAcct:bool = obj["IsBalanceAcct"]
      """  Indicates if this record is a valid balance account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACategory:str = obj["COACategory"]
      """  Chart Category  """  
      self.CanUseCarryFwdBal:bool = obj["CanUseCarryFwdBal"]
      self.NormalBalance:str = obj["NormalBalance"]
      self.CategoryDesc:str = obj["CategoryDesc"]
      self.NormalBalDesc:str = obj["NormalBalDesc"]
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAcctDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.GLAcctDisp1:str = obj["GLAcctDisp1"]
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to the max length of 65.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
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
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies whether or not this display account is a balance anccount and the type of balance it represents.  S= Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  A null value indicates the GL Account is not a balance account but an actual GL Account.  """  
      self.CatType:str = obj["CatType"]
      """   Indicates if this cateory is reatled to a balance sheet account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.IsGLAccount:bool = obj["IsGLAccount"]
      """  Indicates if this display account record is a valid GL Account.  this may be a valid GL Account for the controlled sequence and/or a fully resolved GL Account by the Posting Engine.  """  
      self.IsBalanceAcct:bool = obj["IsBalanceAcct"]
      """  Indicates if this record is a valid balance account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACategory:str = obj["COACategory"]
      """  Chart Category  """  
      self.CanUseCarryFwdBal:bool = obj["CanUseCarryFwdBal"]
      self.NormalBalance:str = obj["NormalBalance"]
      self.CategoryDesc:str = obj["CategoryDesc"]
      self.NormalBalDesc:str = obj["NormalBalDesc"]
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckDispAccountGeneral_input:
   """ Required : 
   chk_Company
   chk_CoaCode
   chk_GLAccount
   """  
   def __init__(self, obj):
      self.chk_Company:str = obj["chk_Company"]
      self.chk_CoaCode:str = obj["chk_CoaCode"]
      self.chk_GLAccount:str = obj["chk_GLAccount"]
      pass

class CheckDispAccountGeneral_output:
   def __init__(self, obj):
      pass

class CheckDispAcctGLB_input:
   """ Required : 
   chk_Company
   chk_ExtCompany
   chk_CoaCode
   chk_GLAccount
   """  
   def __init__(self, obj):
      self.chk_Company:str = obj["chk_Company"]
      self.chk_ExtCompany:str = obj["chk_ExtCompany"]
      self.chk_CoaCode:str = obj["chk_CoaCode"]
      self.chk_GLAccount:str = obj["chk_GLAccount"]
      pass

class CheckDispAcctGLB_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   coACode
   glAccount
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.glAccount:str = obj["glAccount"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLAcctDispListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to the max length of 65.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
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
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies whether or not this display account is a balance anccount and the type of balance it represents.  S= Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  A null value indicates the GL Account is not a balance account but an actual GL Account.  """  
      self.CatType:str = obj["CatType"]
      """   Indicates if this cateory is reatled to a balance sheet account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.IsGLAccount:bool = obj["IsGLAccount"]
      """  Indicates if this display account record is a valid GL Account.  this may be a valid GL Account for the controlled sequence and/or a fully resolved GL Account by the Posting Engine.  """  
      self.IsBalanceAcct:bool = obj["IsBalanceAcct"]
      """  Indicates if this record is a valid balance account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACategory:str = obj["COACategory"]
      """  Chart Category  """  
      self.CanUseCarryFwdBal:bool = obj["CanUseCarryFwdBal"]
      self.NormalBalance:str = obj["NormalBalance"]
      self.CategoryDesc:str = obj["CategoryDesc"]
      self.NormalBalDesc:str = obj["NormalBalDesc"]
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAcctDispListTableset:
   def __init__(self, obj):
      self.GLAcctDispList:list[Erp_Tablesets_GLAcctDispListRow] = obj["GLAcctDispList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLAcctDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to the max length of 65.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
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
      self.BalanceType:str = obj["BalanceType"]
      """  Identifies whether or not this display account is a balance anccount and the type of balance it represents.  S= Summary Balance.  D = Detail Balance.  B = Both a Summary and Detail Balance.  A null value indicates the GL Account is not a balance account but an actual GL Account.  """  
      self.CatType:str = obj["CatType"]
      """   Indicates if this cateory is reatled to a balance sheet account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.IsGLAccount:bool = obj["IsGLAccount"]
      """  Indicates if this display account record is a valid GL Account.  this may be a valid GL Account for the controlled sequence and/or a fully resolved GL Account by the Posting Engine.  """  
      self.IsBalanceAcct:bool = obj["IsBalanceAcct"]
      """  Indicates if this record is a valid balance account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACategory:str = obj["COACategory"]
      """  Chart Category  """  
      self.CanUseCarryFwdBal:bool = obj["CanUseCarryFwdBal"]
      self.NormalBalance:str = obj["NormalBalance"]
      self.CategoryDesc:str = obj["CategoryDesc"]
      self.NormalBalDesc:str = obj["NormalBalDesc"]
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAcctDispTableset:
   def __init__(self, obj):
      self.GLAcctDisp:list[Erp_Tablesets_GLAcctDispRow] = obj["GLAcctDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLAcctDispTableset:
   def __init__(self, obj):
      self.GLAcctDisp:list[Erp_Tablesets_GLAcctDispRow] = obj["GLAcctDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GLAccountSearchFilter_input:
   """ Required : 
   whereClause
   descContains
   effFrom
   effTo
   coaCode
   plantList
   pageSize
   absolutePage
   includeDynamic
   accountMask
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.descContains:str = obj["descContains"]
      self.effFrom:str = obj["effFrom"]
      self.effTo:str = obj["effTo"]
      self.coaCode:str = obj["coaCode"]
      """  COACode  """  
      self.plantList:str = obj["plantList"]
      """  COACode  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.includeDynamic:bool = obj["includeDynamic"]
      self.accountMask:str = obj["accountMask"]
      pass

class GLAccountSearchFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GLAccountSearchListPeriod_input:
   """ Required : 
   whereClause
   effFrom
   effTo
   pageSize
   absolutePage
   includeDynamic
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.effFrom:str = obj["effFrom"]
      self.effTo:str = obj["effTo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.includeDynamic:bool = obj["includeDynamic"]
      pass

class GLAccountSearchListPeriod_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GLAccountSearchList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GLAccountSearchList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GLAccountSearchRowsPeriod_input:
   """ Required : 
   whereClause
   effFrom
   effTo
   pageSize
   absolutePage
   includeDynamic
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.effFrom:str = obj["effFrom"]
      self.effTo:str = obj["effTo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.includeDynamic:bool = obj["includeDynamic"]
      pass

class GLAccountSearchRowsPeriod_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   coACode
   glAccount
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.glAccount:str = obj["glAccount"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAcctDispTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAcctDispTableset] = obj["returnObj"]
      pass

class GetList2_input:
   """ Required : 
   WhereClause
   pageSize
   absolutePage
   includeInactive
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.includeInactive:bool = obj["includeInactive"]
      pass

class GetList2_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListCBOnlyPeriod_input:
   """ Required : 
   whereClause
   effFrom
   effTo
   pageSize
   absolutePage
   includeDynamic
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  GLAcctDisp search clause  """  
      self.effFrom:str = obj["effFrom"]
      self.effTo:str = obj["effTo"]
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      self.includeDynamic:bool = obj["includeDynamic"]
      """  Include Dynamic  """  
      pass

class GetListCBOnlyPeriod_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListCBOnly_input:
   """ Required : 
   WhereClause
   pageSize
   absolutePage
   includeDynamic
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.includeDynamic:bool = obj["includeDynamic"]
      pass

class GetListCBOnly_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_GLAcctDispListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLAcctDisp_input:
   """ Required : 
   ds
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAcctDispTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewGLAcctDisp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAcctDispTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLAcctDisp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLAcctDisp:str = obj["whereClauseGLAcctDisp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispTableset] = obj["returnObj"]
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

class InvokeBalanceAcctSearch_input:
   """ Required : 
   WhereClauseGLAcctDisp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClauseGLAcctDisp:str = obj["WhereClauseGLAcctDisp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class InvokeBalanceAcctSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAcctDispTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLAcctDispTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLAcctDispTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAcctDispTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAcctDispTableset] = obj["ds"]
      pass

      """  output parameters  """  

