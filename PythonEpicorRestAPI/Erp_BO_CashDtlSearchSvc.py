import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CashDtlSearchSvc
# Description: The cash detail search service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CashDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/CashDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_CashDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/CashDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashDtlSearches_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashDtlSearch item
   Description: Calls GetByID to retrieve the CashDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/CashDtlSearches(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashDtlSearches_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashDtlSearch for the service
   Description: Calls UpdateExt to update CashDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/CashDtlSearches(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashDtlSearches_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashDtlSearch item
   Description: Call UpdateExt to delete CashDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/CashDtlSearches(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCashDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCashDtl=" + whereClauseCashDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, invoiceNum, invoiceRef, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceRef=" + invoiceRef

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDtlsForContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDtlsForContactTracker
   Description: Called from Customer tracker instead of GetRows
   OperationID: GetCashDtlsForContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDtlsForContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDtlsForContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Called from Customer tracker instead of GetRows for better performance
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDtlsForCustomerActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDtlsForCustomerActivity
   Description: Called from Customer Activity instead of GetRows
   OperationID: GetCashDtlsForCustomerActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDtlsForCustomerActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDtlsForCustomerActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDtlsForCustomerTrackerAndSort(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDtlsForCustomerTrackerAndSort
   Description: Called from Customer tracker instead of GetRows
   OperationID: GetCashDtlsForCustomerTrackerAndSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDtlsForCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDtlsForCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDtlsForCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDtlsForCustomerTracker
   Description: Called from Customer tracker instead of GetRows
   OperationID: GetCashDtlsForCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDtlsForCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDtlsForCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashDtlRow] = obj["value"]
      pass

class Erp_Tablesets_CashDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLockRate:bool = obj["InvLockRate"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.CreditMemo:bool = obj["CreditMemo"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.NetCash:int = obj["NetCash"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.DocNetCash:int = obj["DocNetCash"]
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      """  Full description for the Tax Region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MX Payment Number for AR Invoice  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  Reference to HeadNum of main CashHead record.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  Taxable Adjustment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseAdjAmt:int = obj["BaseAdjAmt"]
      """  Adjustment amount in Base Currency  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.DispDocSelfAssessAmt:int = obj["DispDocSelfAssessAmt"]
      self.DispDocWithholdAmt:int = obj["DispDocWithholdAmt"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.DispSelfAssessAmt:int = obj["DispSelfAssessAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispWithholdAmt:int = obj["DispWithholdAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  Write Off Amount  """  
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then CopyRate checkbox is Read Only  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.NetCash:int = obj["NetCash"]
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.RecalcTranAmt:bool = obj["RecalcTranAmt"]
      """  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.RemoveForAdjustment:bool = obj["RemoveForAdjustment"]
      """  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1WriteOffGainLossAmt:int = obj["Rpt1WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2WriteOffGainLossAmt:int = obj["Rpt2WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3WriteOffGainLossAmt:int = obj["Rpt3WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffGainLossAmt:int = obj["WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.OldWriteOffAmount:int = obj["OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffAccountDisp:str = obj["WriteOffAccountDisp"]
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      self.TotalGainLossAmt:int = obj["TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.OldWriteOffGainLossAmt:int = obj["OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffGainLossAmt:int = obj["Rpt1OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffGainLossAmt:int = obj["Rpt2OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffGainLossAmt:int = obj["Rpt3OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1TotalGainLossAmt:int = obj["Rpt1TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt2TotalGainLossAmt:int = obj["Rpt2TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt3TotalGainLossAmt:int = obj["Rpt3TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.DocOldWriteOffAmount:int = obj["DocOldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffAmount:int = obj["Rpt1OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffAmount:int = obj["Rpt2OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffAmount:int = obj["Rpt3OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding amount tax was manually modified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumInvoiceType:str = obj["InvoiceNumInvoiceType"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   groupID
   headNum
   invoiceNum
   invoiceRef
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceRef:int = obj["invoiceRef"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CashDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLockRate:bool = obj["InvLockRate"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.CreditMemo:bool = obj["CreditMemo"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.NetCash:int = obj["NetCash"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.DocNetCash:int = obj["DocNetCash"]
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      """  Full description for the Tax Region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashDtlListTableset:
   def __init__(self, obj):
      self.CashDtlList:list[Erp_Tablesets_CashDtlListRow] = obj["CashDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MX Payment Number for AR Invoice  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  Reference to HeadNum of main CashHead record.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  Taxable Adjustment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseAdjAmt:int = obj["BaseAdjAmt"]
      """  Adjustment amount in Base Currency  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.DispDocSelfAssessAmt:int = obj["DispDocSelfAssessAmt"]
      self.DispDocWithholdAmt:int = obj["DispDocWithholdAmt"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.DispSelfAssessAmt:int = obj["DispSelfAssessAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispWithholdAmt:int = obj["DispWithholdAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  Write Off Amount  """  
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then CopyRate checkbox is Read Only  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.NetCash:int = obj["NetCash"]
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.RecalcTranAmt:bool = obj["RecalcTranAmt"]
      """  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.RemoveForAdjustment:bool = obj["RemoveForAdjustment"]
      """  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1WriteOffGainLossAmt:int = obj["Rpt1WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2WriteOffGainLossAmt:int = obj["Rpt2WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3WriteOffGainLossAmt:int = obj["Rpt3WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffGainLossAmt:int = obj["WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.OldWriteOffAmount:int = obj["OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffAccountDisp:str = obj["WriteOffAccountDisp"]
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      self.TotalGainLossAmt:int = obj["TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.OldWriteOffGainLossAmt:int = obj["OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffGainLossAmt:int = obj["Rpt1OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffGainLossAmt:int = obj["Rpt2OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffGainLossAmt:int = obj["Rpt3OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1TotalGainLossAmt:int = obj["Rpt1TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt2TotalGainLossAmt:int = obj["Rpt2TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt3TotalGainLossAmt:int = obj["Rpt3TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.DocOldWriteOffAmount:int = obj["DocOldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffAmount:int = obj["Rpt1OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffAmount:int = obj["Rpt2OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffAmount:int = obj["Rpt3OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding amount tax was manually modified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumInvoiceType:str = obj["InvoiceNumInvoiceType"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashDtlSearchTableset:
   def __init__(self, obj):
      self.CashDtl:list[Erp_Tablesets_CashDtlRow] = obj["CashDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCashDtlSearchTableset:
   def __init__(self, obj):
      self.CashDtl:list[Erp_Tablesets_CashDtlRow] = obj["CashDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   headNum
   invoiceNum
   invoiceRef
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceRef:int = obj["invoiceRef"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
      pass

class GetCashDtlsForContactTracker_input:
   """ Required : 
   company
   custN
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Current company.  """  
      self.custN:str = obj["custN"]
      """  Current customer number.  """  
      self.contactName:str = obj["contactName"]
      """  Current contact name.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetCashDtlsForContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetCashDtlsForCustomerActivity_input:
   """ Required : 
   whereClause
   company
   custN
   dateRange
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where Clause that contains the sort by of CashDtl table.  """  
      self.company:str = obj["company"]
      """  Current company.  """  
      self.custN:str = obj["custN"]
      """  Current customer number.  """  
      self.dateRange:str = obj["dateRange"]
      """  Current Transaction Date Range.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetCashDtlsForCustomerActivity_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetCashDtlsForCustomerTrackerAndSort_input:
   """ Required : 
   company
   custN
   dateRange
   pageSize
   absolutePage
   sortBy
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Current company.  """  
      self.custN:str = obj["custN"]
      """  Current customer number.  """  
      self.dateRange:str = obj["dateRange"]
      """  Current Transaction Date Range.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      self.sortBy:str = obj["sortBy"]
      """  Sort by.  """  
      pass

class GetCashDtlsForCustomerTrackerAndSort_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetCashDtlsForCustomerTracker_input:
   """ Required : 
   company
   custN
   dateRange
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Current company.  """  
      self.custN:str = obj["custN"]
      """  Current customer number.  """  
      self.dateRange:str = obj["dateRange"]
      """  Current Transaction Date Range.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetCashDtlsForCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCashDtl_input:
   """ Required : 
   ds
   groupID
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashDtlSearchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewCashDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseCashDtl
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashDtl:str = obj["whereClauseCashDtl"]
      """  Whereclause for CashDtl table.  """  
      self.contactName:str = obj["contactName"]
      """  Contact to retrieve data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseCashDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashDtl:str = obj["whereClauseCashDtl"]
      """  Whereclause for CashDtl table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCashDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashDtl:str = obj["whereClauseCashDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCashDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCashDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

