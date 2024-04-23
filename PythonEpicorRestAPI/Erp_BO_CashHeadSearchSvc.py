import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CashHeadSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CashHeadSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashHeadSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches",headers=creds) as resp:
           return await resp.json()

async def post_CashHeadSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashHeadSearches_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashHeadSearch item
   Description: Calls GetByID to retrieve the CashHeadSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashHeadSearches_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashHeadSearch for the service
   Description: Calls UpdateExt to update CashHeadSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashHeadSearches_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashHeadSearch item
   Description: Call UpdateExt to delete CashHeadSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/CashHeadSearches(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCashHead, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCashHead=" + whereClauseCashHead
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, epicorHeaders = None):
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCashReceiptRelationshipMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashReceiptRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Cash Receipt
   OperationID: GetCashReceiptRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashReceiptRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashReceiptRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListByInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByInvoice
   OperationID: GetListByInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListByInvoiceWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByInvoiceWhereClause
   Description: Receives a where clause string and extracts the variables needed to run GetListByInvoice
   OperationID: GetListByInvoiceWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByInvoiceWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByInvoiceWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupHeadQuery(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupHeadQuery
   OperationID: GetGroupHeadQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupHeadQuery_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupHeadQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForInvoice
   Description: Invokes GetRows filtering on Cash Receipts for the specified Invoice
   OperationID: GetRowsForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForQuote
   Description: Invokes GetRows filtering on Cash Receipts for the specified Quote
   OperationID: GetRowsForQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForSalesOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForSalesOrder
   Description: Invokes GetRows filtering on Cash Receipts for the specified Sales Order
   OperationID: GetRowsForSalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForShipment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForShipment
   Description: Invokes GetRows filtering on Cash Receipts for the specified Customer Shipment
   OperationID: GetRowsForShipment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashHeadSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashHeadRow] = obj["value"]
      pass

class Erp_Tablesets_CashHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
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
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
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
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAcctDesc:str = obj["BankAcctDesc"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      """  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PaymentMethod:str = obj["PaymentMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
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
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
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
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  The amount of the cash receipt applied to invoices in receipt currency  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  The amount of the cash receipt that is unapplied in receipt currency  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MX Method of Payment: single, multiple, etc.  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  If TRUE then MX Electronic Payment XML is required  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MX UUID of the original Receipt being corrected  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MX Confirmation Code for special Cash Receipts  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MX Customer’s Bank ID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  Text entered by the user to indicate the reason Cash receipt was Reversed.  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City.  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State.  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Indicates this record is an adjustment CashHead.  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  Reference to cash receipt which had been adjusted.  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  The reason for the adjustment entered by the user  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Total Check Write Off Amount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Mexico Certified Timestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  Mexico SAT Seal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Mexico Digital Seal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  Mexico SAT Certificate Serial Number  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  Mexico Original String Timbre Fiscal Digital  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Mexico Certificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Mexico Certificate Serial Number  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  ID of the Customer's bank.  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  The Bank account number for the Customer.  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  The Bank account IBAN Code  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  First address line of customer bank.  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  Second address line of customer bank.  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  Third address line of customer bank.  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  Bank City  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  Bank State/Prov  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  Postal Code or zip code  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  Bank account Country Number.  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  Customer Bank Name  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  Receipt Amount in Bank Currency  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  E-invoice Service Provider Status  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  E-invoice Status  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  E-invoice Updated On  """  
      self.AdjustmentCustName:str = obj["AdjustmentCustName"]
      """  Adjustment Customer Name  """  
      self.AdjustmentCustNum:int = obj["AdjustmentCustNum"]
      """  Customer to which the new invoices will be applied.  """  
      self.AdjustmentDate:str = obj["AdjustmentDate"]
      """  Date the adjustment was made.  """  
      self.AdjustmentDocUnAppliedAmt:int = obj["AdjustmentDocUnAppliedAmt"]
      """  Displays the amount available to apply to the invoices.  """  
      self.AdjustmentOnAccount:bool = obj["AdjustmentOnAccount"]
      """  On Account  """  
      self.AdjustmentTranDocTypeID:str = obj["AdjustmentTranDocTypeID"]
      """  Temp TranDocTypeID used when adjusting a Cash Rececipt  """  
      self.AllocDepBal:int = obj["AllocDepBal"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.AmtToAlloc:int = obj["AmtToAlloc"]
      """  Amount to Allocate  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Base Currency Symbol  """  
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CentralCollectionCheck:bool = obj["CentralCollectionCheck"]
      """  Check Box on the UI to filter records by Central Collection flag  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrAmtSelected:int = obj["CurrAmtSelected"]
      """  Current Amount Selected on Invoice Select Tab  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      """  Displays the address of the customer that paid the receipt.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocAllocDepBal:int = obj["DocAllocDepBal"]
      self.DocAmtToAlloc:int = obj["DocAmtToAlloc"]
      """  Doc Amount to Allocate  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Displays the discount applied to the receipt.  """  
      self.DocReceipt:int = obj["DocReceipt"]
      """  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  """  
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DocWhldTax:int = obj["DocWhldTax"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableGetDefaultAcct:bool = obj["EnableGetDefaultAcct"]
      """  Indicates if the option to get the default account is enable.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.GLRefCodeDescription:str = obj["GLRefCodeDescription"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      self.MXECEPXml:str = obj["MXECEPXml"]
      """  MXECEPXml  """  
      self.MXOriginalRefNum:str = obj["MXOriginalRefNum"]
      """  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1AllocDepBal:int = obj["Rpt1AllocDepBal"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1WhldTax:int = obj["Rpt1WhldTax"]
      self.Rpt2AllocDepBal:int = obj["Rpt2AllocDepBal"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2WhldTax:int = obj["Rpt2WhldTax"]
      self.Rpt3AllocDepBal:int = obj["Rpt3AllocDepBal"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3WhldTax:int = obj["Rpt3WhldTax"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.SystemTranType:str = obj["SystemTranType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.WhldTax:int = obj["WhldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AdjustmentCustID:str = obj["AdjustmentCustID"]
      """  Displays the customer ID.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.CustFullAddrFormatted:str = obj["CustFullAddrFormatted"]
      """  Displays the address of the customer that paid the receipt with newline delimiter.  """  
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding tax was manually modified.  """  
      self.TranTypeDescCaption:str = obj["TranTypeDescCaption"]
      """  Payment type description, displayed in the Details page header.  """  
      self.AdjustmentCustAddress:str = obj["AdjustmentCustAddress"]
      self.MXSubstGroupId:str = obj["MXSubstGroupId"]
      """  Substitution Cash Receipt Group ID  """  
      self.MXSubstCheckRef:str = obj["MXSubstCheckRef"]
      """  Substitution Cash Receipt CheckRef  """  
      self.MXSubstFiscalFolio:str = obj["MXSubstFiscalFolio"]
      """  Substitution Cash Receipt UUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CashBHedPosted:bool = obj["CashBHedPosted"]
      self.CashBHedCashBookNum:int = obj["CashBHedCashBookNum"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PCashDocDirection:str = obj["PCashDocDirection"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.PMUIDMXSATCode:str = obj["PMUIDMXSATCode"]
      self.PMUIDSummarizePerCustomer:bool = obj["PMUIDSummarizePerCustomer"]
      self.PMUIDType:int = obj["PMUIDType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      self.ReverseMXCancelReasonCode:str = obj["ReverseMXCancelReasonCode"]
      self.ReverseMXCancellationMode:str = obj["ReverseMXCancellationMode"]
      self.SourceTranDateTranDate:str = obj["SourceTranDateTranDate"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
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
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CashHeadListAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
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

class Erp_Tablesets_CashHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
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
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
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
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAcctDesc:str = obj["BankAcctDesc"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      """  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PaymentMethod:str = obj["PaymentMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
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
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
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
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  The amount of the cash receipt applied to invoices in receipt currency  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  The amount of the cash receipt that is unapplied in receipt currency  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MX Method of Payment: single, multiple, etc.  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  If TRUE then MX Electronic Payment XML is required  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MX UUID of the original Receipt being corrected  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MX Confirmation Code for special Cash Receipts  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MX Customer’s Bank ID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  Text entered by the user to indicate the reason Cash receipt was Reversed.  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City.  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State.  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Indicates this record is an adjustment CashHead.  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  Reference to cash receipt which had been adjusted.  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  The reason for the adjustment entered by the user  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Total Check Write Off Amount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Mexico Certified Timestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  Mexico SAT Seal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Mexico Digital Seal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  Mexico SAT Certificate Serial Number  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  Mexico Original String Timbre Fiscal Digital  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Mexico Certificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Mexico Certificate Serial Number  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  ID of the Customer's bank.  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  The Bank account number for the Customer.  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  The Bank account IBAN Code  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  First address line of customer bank.  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  Second address line of customer bank.  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  Third address line of customer bank.  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  Bank City  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  Bank State/Prov  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  Postal Code or zip code  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  Bank account Country Number.  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  Customer Bank Name  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  Receipt Amount in Bank Currency  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  E-invoice Service Provider Status  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  E-invoice Status  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  E-invoice Updated On  """  
      self.AdjustmentCustName:str = obj["AdjustmentCustName"]
      """  Adjustment Customer Name  """  
      self.AdjustmentCustNum:int = obj["AdjustmentCustNum"]
      """  Customer to which the new invoices will be applied.  """  
      self.AdjustmentDate:str = obj["AdjustmentDate"]
      """  Date the adjustment was made.  """  
      self.AdjustmentDocUnAppliedAmt:int = obj["AdjustmentDocUnAppliedAmt"]
      """  Displays the amount available to apply to the invoices.  """  
      self.AdjustmentOnAccount:bool = obj["AdjustmentOnAccount"]
      """  On Account  """  
      self.AdjustmentTranDocTypeID:str = obj["AdjustmentTranDocTypeID"]
      """  Temp TranDocTypeID used when adjusting a Cash Rececipt  """  
      self.AllocDepBal:int = obj["AllocDepBal"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.AmtToAlloc:int = obj["AmtToAlloc"]
      """  Amount to Allocate  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Base Currency Symbol  """  
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CentralCollectionCheck:bool = obj["CentralCollectionCheck"]
      """  Check Box on the UI to filter records by Central Collection flag  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrAmtSelected:int = obj["CurrAmtSelected"]
      """  Current Amount Selected on Invoice Select Tab  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      """  Displays the address of the customer that paid the receipt.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocAllocDepBal:int = obj["DocAllocDepBal"]
      self.DocAmtToAlloc:int = obj["DocAmtToAlloc"]
      """  Doc Amount to Allocate  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Displays the discount applied to the receipt.  """  
      self.DocReceipt:int = obj["DocReceipt"]
      """  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  """  
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DocWhldTax:int = obj["DocWhldTax"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableGetDefaultAcct:bool = obj["EnableGetDefaultAcct"]
      """  Indicates if the option to get the default account is enable.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.GLRefCodeDescription:str = obj["GLRefCodeDescription"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      self.MXECEPXml:str = obj["MXECEPXml"]
      """  MXECEPXml  """  
      self.MXOriginalRefNum:str = obj["MXOriginalRefNum"]
      """  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1AllocDepBal:int = obj["Rpt1AllocDepBal"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1WhldTax:int = obj["Rpt1WhldTax"]
      self.Rpt2AllocDepBal:int = obj["Rpt2AllocDepBal"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2WhldTax:int = obj["Rpt2WhldTax"]
      self.Rpt3AllocDepBal:int = obj["Rpt3AllocDepBal"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3WhldTax:int = obj["Rpt3WhldTax"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.SystemTranType:str = obj["SystemTranType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.WhldTax:int = obj["WhldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AdjustmentCustID:str = obj["AdjustmentCustID"]
      """  Displays the customer ID.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.CustFullAddrFormatted:str = obj["CustFullAddrFormatted"]
      """  Displays the address of the customer that paid the receipt with newline delimiter.  """  
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding tax was manually modified.  """  
      self.TranTypeDescCaption:str = obj["TranTypeDescCaption"]
      """  Payment type description, displayed in the Details page header.  """  
      self.AdjustmentCustAddress:str = obj["AdjustmentCustAddress"]
      self.MXSubstGroupId:str = obj["MXSubstGroupId"]
      """  Substitution Cash Receipt Group ID  """  
      self.MXSubstCheckRef:str = obj["MXSubstCheckRef"]
      """  Substitution Cash Receipt CheckRef  """  
      self.MXSubstFiscalFolio:str = obj["MXSubstFiscalFolio"]
      """  Substitution Cash Receipt UUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CashBHedPosted:bool = obj["CashBHedPosted"]
      self.CashBHedCashBookNum:int = obj["CashBHedCashBookNum"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PCashDocDirection:str = obj["PCashDocDirection"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.PMUIDMXSATCode:str = obj["PMUIDMXSATCode"]
      self.PMUIDSummarizePerCustomer:bool = obj["PMUIDSummarizePerCustomer"]
      self.PMUIDType:int = obj["PMUIDType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      self.ReverseMXCancelReasonCode:str = obj["ReverseMXCancelReasonCode"]
      self.ReverseMXCancellationMode:str = obj["ReverseMXCancellationMode"]
      self.SourceTranDateTranDate:str = obj["SourceTranDateTranDate"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadSearchListTableset:
   def __init__(self, obj):
      self.CashHeadList:list[Erp_Tablesets_CashHeadListRow] = obj["CashHeadList"]
      self.CashHeadListAttch:list[Erp_Tablesets_CashHeadListAttchRow] = obj["CashHeadListAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashHeadSearchTableset:
   def __init__(self, obj):
      self.CashHead:list[Erp_Tablesets_CashHeadRow] = obj["CashHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCashHeadSearchTableset:
   def __init__(self, obj):
      self.CashHead:list[Erp_Tablesets_CashHeadRow] = obj["CashHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
      pass

class GetCashReceiptRelationshipMap_input:
   """ Required : 
   groupID
   headNum
   maxNumOfCards
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.maxNumOfCards:int = obj["maxNumOfCards"]
      pass

class GetCashReceiptRelationshipMap_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetGroupHeadQuery_input:
   """ Required : 
   checkRef
   """  
   def __init__(self, obj):
      self.checkRef:str = obj["checkRef"]
      pass

class GetGroupHeadQuery_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchListTableset] = obj["returnObj"]
      pass

class GetListByInvoiceWhereClause_input:
   """ Required : 
   whereClause
   startingAtValue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Full where clause  """  
      self.startingAtValue:str = obj["startingAtValue"]
      """  Value to filter the start of the results  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetListByInvoiceWhereClause_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListByInvoice_input:
   """ Required : 
   whereClauseVendorPP
   pmUID
   custId
   bankAcctID
   tranType
   fromDate
   toDate
   invoiceNum
   checkRef
   startingAt
   startingAtValue
   mandateRef
   pageSize
   absolutePage
   multipleChecks
   """  
   def __init__(self, obj):
      self.whereClauseVendorPP:str = obj["whereClauseVendorPP"]
      self.pmUID:int = obj["pmUID"]
      self.custId:str = obj["custId"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranType:str = obj["tranType"]
      self.fromDate:str = obj["fromDate"]
      self.toDate:str = obj["toDate"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.checkRef:str = obj["checkRef"]
      self.startingAt:str = obj["startingAt"]
      self.startingAtValue:str = obj["startingAtValue"]
      self.mandateRef:str = obj["mandateRef"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.multipleChecks:bool = obj["multipleChecks"]
      pass

class GetListByInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CashHeadSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCashHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashHeadSearchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewCashHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashHeadSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsForInvoice_input:
   """ Required : 
   whereClauseCashHead
   invoiceNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashHead:str = obj["whereClauseCashHead"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForQuote_input:
   """ Required : 
   whereClauseCashHead
   quoteNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashHead:str = obj["whereClauseCashHead"]
      self.quoteNum:int = obj["quoteNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForQuote_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForSalesOrder_input:
   """ Required : 
   whereClauseCashHead
   orderNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashHead:str = obj["whereClauseCashHead"]
      self.orderNum:int = obj["orderNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForSalesOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForShipment_input:
   """ Required : 
   whereClauseCashHead
   packNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashHead:str = obj["whereClauseCashHead"]
      self.packNum:int = obj["packNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForShipment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCashHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashHead:str = obj["whereClauseCashHead"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCashHeadSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCashHeadSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashHeadSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashHeadSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

