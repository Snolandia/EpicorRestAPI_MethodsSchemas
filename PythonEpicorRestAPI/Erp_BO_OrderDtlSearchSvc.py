import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OrderDtlSearchSvc
# Description: Job dataset for Customer Tracker UI.
           This object does not have update capabilities.
           Only record retrieval is available.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_OrderDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OrderDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_OrderDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OrderDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OrderDtlSearches_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OrderDtlSearch item
   Description: Calls GetByID to retrieve the OrderDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches(" + Company + "," + OrderNum + "," + OrderLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OrderDtlSearches_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OrderDtlSearch for the service
   Description: Calls UpdateExt to update OrderDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OrderDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches(" + Company + "," + OrderNum + "," + OrderLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OrderDtlSearches_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OrderDtlSearch item
   Description: Call UpdateExt to delete OrderDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OrderDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches(" + Company + "," + OrderNum + "," + OrderLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseOrderDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseOrderDtl=" + whereClauseOrderDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(orderNum, orderLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "orderNum=" + orderNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderLine=" + orderLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_getBreakListCodeDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getBreakListCodeDesc
   Description: getBreakListCodeDesc
   OperationID: getBreakListCodeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getBreakListCodeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getBreakListCodeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerActivity
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer activity.
   OperationID: GetRowsCustomerActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTrackerAndSort(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTrackerAndSort
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTrackerAndSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOrderDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOrderDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOrderDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrderDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrderDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderDtlRow] = obj["value"]
      pass

class Erp_Tablesets_OrderDtlListRow:
   def __init__(self, obj):
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  """  
      self.AdvanceBillBal:int = obj["AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  """  
      self.DocAdvanceBillBal:int = obj["DocAdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  """  
      self.OrigWhyNoTax:str = obj["OrigWhyNoTax"]
      """  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  """  
      self.Rework:bool = obj["Rework"]
      """   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  """  
      self.RMANum:int = obj["RMANum"]
      """   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  The line item of the RMA detail that this order line item is fulfilling.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this OrderDtl record. Can be blank.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days"," Months", "Years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order line is linked to an inter-company PO line.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the order line can be changed.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  The Demand Contract Detail record this OrderDtl is related to.  """  
      self.CreateNewJob:bool = obj["CreateNewJob"]
      """  Create New Job flag  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.GetDtls:bool = obj["GetDtls"]
      """  Get Details flag  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.SchedJob:bool = obj["SchedJob"]
      """  Schedule Job flag  """  
      self.RelJob:bool = obj["RelJob"]
      """  Release Job flag  """  
      self.EnableCreateNewJob:bool = obj["EnableCreateNewJob"]
      """  Enable New Job flag  """  
      self.EnableGetDtls:bool = obj["EnableGetDtls"]
      """  Enable Get Details flag  """  
      self.EnableSchedJob:bool = obj["EnableSchedJob"]
      """  Enable Schedule Job flag  """  
      self.EnableRelJob:bool = obj["EnableRelJob"]
      """  Enable Release Job flag  """  
      self.CounterSaleWarehouse:str = obj["CounterSaleWarehouse"]
      """  Indicates the warehouse selected for a counter sale order line.  """  
      self.CounterSaleBinNum:str = obj["CounterSaleBinNum"]
      """  Identifies the Bin selected for a counter sale order line.  """  
      self.CounterSaleLotNum:str = obj["CounterSaleLotNum"]
      """  Indicates the lot number selected for a counter sale order line.  """  
      self.CounterSaleDimCode:str = obj["CounterSaleDimCode"]
      """  Indicates the dimension code selected for a counter sales order line.  """  
      self.DemandDtlRejected:bool = obj["DemandDtlRejected"]
      """  Indicates if the demand detail that created/updated this order line has been rejected.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.TotalReleases:int = obj["TotalReleases"]
      """  Total Number of releases for the line  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1AdvanceBillBal:int = obj["Rpt1AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt2AdvanceBillBal:int = obj["Rpt2AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt3AdvanceBillBal:int = obj["Rpt3AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Status of Order Line  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Same as DocUnit price except that this field contains the unit price including taxes  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency -including taxes.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied. including taxes  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.OldOurOpenQty:int = obj["OldOurOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldSellingOpenQty:int = obj["OldSellingOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldOpenValue:int = obj["OldOpenValue"]
      """  Used to store open value setting assigned in product configuration programs  """  
      self.OldProdCode:str = obj["OldProdCode"]
      """  Used to store prod code value assigned in product configuration programs  """  
      self.PrevSellQty:int = obj["PrevSellQty"]
      """  Previous Selling Quantity  """  
      self.PrevPartNum:str = obj["PrevPartNum"]
      """  Previous Part Number  """  
      self.PrevXPartNum:str = obj["PrevXPartNum"]
      """  Previous Customer Part Number  """  
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.LockDisc:bool = obj["LockDisc"]
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.TotalShipped:int = obj["TotalShipped"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.MiscCharges:int = obj["MiscCharges"]
      self.TotalPrice:int = obj["TotalPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.DocMiscCharges:int = obj["DocMiscCharges"]
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.Configured:str = obj["Configured"]
      self.QuoteQtyNum:int = obj["QuoteQtyNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DUM:str = obj["DUM"]
      self.ProcessQuickEntry:bool = obj["ProcessQuickEntry"]
      self.CounterSale:bool = obj["CounterSale"]
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Available Price Lists  """  
      self.ProcessCounterSale:bool = obj["ProcessCounterSale"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.DemandQuantity:int = obj["DemandQuantity"]
      self.AvailUMFromQuote:str = obj["AvailUMFromQuote"]
      self.FromQuoteLineFlag:bool = obj["FromQuoteLineFlag"]
      self.MultipleReleases:bool = obj["MultipleReleases"]
      self.PartExists:bool = obj["PartExists"]
      self.SalesRepName1:str = obj["SalesRepName1"]
      self.SalesRepName2:str = obj["SalesRepName2"]
      self.SalesRepName3:str = obj["SalesRepName3"]
      self.SalesRepName4:str = obj["SalesRepName4"]
      self.SalesRepName5:str = obj["SalesRepName5"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.CreditLimitMessage:str = obj["CreditLimitMessage"]
      """  The message text returned by the credit check process.  """  
      self.CreditLimitSource:str = obj["CreditLimitSource"]
      """  The source that put the customer on credit hold.  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  Kit Flag Description. "P" = Parent, "C" = Component.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitStandard:bool = obj["KitStandard"]
      """  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.PriceListCodeDesc:str = obj["PriceListCodeDesc"]
      self.EnableSellingQty:bool = obj["EnableSellingQty"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the line.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  """  
      self.EnableKitUnitPrice:bool = obj["EnableKitUnitPrice"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.Rpt1MiscCharges:int = obj["Rpt1MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt2MiscCharges:int = obj["Rpt2MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt3MiscCharges:int = obj["Rpt3MiscCharges"]
      """  Report Currency misc charges  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      """  Report currency line total price  """  
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  The Sales Order Quantity expressed in the Inventory Unit of Measure  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Order Detail is allocated against.  """  
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Extended Price for the Order Line in Rpt1 currency  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Extended Price for the orderLine in Rpt2 currency.  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Extended price for the order line in Rpt3 currency  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencyID:str = obj["CurrencyID"]
      self.POLineRef:str = obj["POLineRef"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      """  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      """  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.InPrice:bool = obj["InPrice"]
      """  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  """  
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in document currency which does not include taxes  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display which does not include taxes  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display which does not include taxes (report currency)  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.DocInMiscCharges:int = obj["DocInMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  """  
      self.InMiscCharges:int = obj["InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line  """  
      self.Rpt1InMiscCharges:int = obj["Rpt1InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt2InMiscCharges:int = obj["Rpt2InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt3InMiscCharges:int = obj["Rpt3InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      """  Description of the Marketing campaign  """  
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      """  Description.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      """  Description of the sales category.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      """  Description of the warranty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderDtlRow:
   def __init__(self, obj):
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  """  
      self.AdvanceBillBal:int = obj["AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  """  
      self.DocAdvanceBillBal:int = obj["DocAdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  """  
      self.OrigWhyNoTax:str = obj["OrigWhyNoTax"]
      """  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  """  
      self.Rework:bool = obj["Rework"]
      """   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  """  
      self.RMANum:int = obj["RMANum"]
      """   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  The line item of the RMA detail that this order line item is fulfilling.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this OrderDtl record. Can be blank.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days"," Months", "Years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order line is linked to an inter-company PO line.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the order line can be changed.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  The Demand Contract Detail record this OrderDtl is related to.  """  
      self.CreateNewJob:bool = obj["CreateNewJob"]
      """  Create New Job flag  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.GetDtls:bool = obj["GetDtls"]
      """  Get Details flag  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.SchedJob:bool = obj["SchedJob"]
      """  Schedule Job flag  """  
      self.RelJob:bool = obj["RelJob"]
      """  Release Job flag  """  
      self.EnableCreateNewJob:bool = obj["EnableCreateNewJob"]
      """  Enable New Job flag  """  
      self.EnableGetDtls:bool = obj["EnableGetDtls"]
      """  Enable Get Details flag  """  
      self.EnableSchedJob:bool = obj["EnableSchedJob"]
      """  Enable Schedule Job flag  """  
      self.EnableRelJob:bool = obj["EnableRelJob"]
      """  Enable Release Job flag  """  
      self.CounterSaleWarehouse:str = obj["CounterSaleWarehouse"]
      """  Indicates the warehouse selected for a counter sale order line.  """  
      self.CounterSaleBinNum:str = obj["CounterSaleBinNum"]
      """  Identifies the Bin selected for a counter sale order line.  """  
      self.CounterSaleLotNum:str = obj["CounterSaleLotNum"]
      """  Indicates the lot number selected for a counter sale order line.  """  
      self.CounterSaleDimCode:str = obj["CounterSaleDimCode"]
      """  Indicates the dimension code selected for a counter sales order line.  """  
      self.DemandDtlRejected:bool = obj["DemandDtlRejected"]
      """  Indicates if the demand detail that created/updated this order line has been rejected.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.TotalReleases:int = obj["TotalReleases"]
      """  Total Number of releases for the line  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1AdvanceBillBal:int = obj["Rpt1AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt2AdvanceBillBal:int = obj["Rpt2AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt3AdvanceBillBal:int = obj["Rpt3AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Status of Order Line  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Same as DocUnit price except that this field contains the unit price including taxes  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency -including taxes.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied. including taxes  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.OldOurOpenQty:int = obj["OldOurOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldSellingOpenQty:int = obj["OldSellingOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldOpenValue:int = obj["OldOpenValue"]
      """  Used to store open value setting assigned in product configuration programs  """  
      self.OldProdCode:str = obj["OldProdCode"]
      """  Used to store prod code value assigned in product configuration programs  """  
      self.PrevSellQty:int = obj["PrevSellQty"]
      """  Previous Selling Quantity  """  
      self.PrevPartNum:str = obj["PrevPartNum"]
      """  Previous Part Number  """  
      self.PrevXPartNum:str = obj["PrevXPartNum"]
      """  Previous Customer Part Number  """  
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.LockDisc:bool = obj["LockDisc"]
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.ECCOrderNum:str = obj["ECCOrderNum"]
      """  ECCOrderNum  """  
      self.ECCOrderLine:int = obj["ECCOrderLine"]
      """  ECCOrderLine  """  
      self.DupOnJobCrt:bool = obj["DupOnJobCrt"]
      """  DupOnJobCrt  """  
      self.UndersPct:int = obj["UndersPct"]
      """  UndersPct  """  
      self.Overs:int = obj["Overs"]
      """  Overs  """  
      self.Unders:int = obj["Unders"]
      """  Unders  """  
      self.OversUnitPrice:int = obj["OversUnitPrice"]
      """  OversUnitPrice  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.MOMsourceType:str = obj["MOMsourceType"]
      """  MOMsourceType  """  
      self.MOMsourceEst:str = obj["MOMsourceEst"]
      """  MOMsourceEst  """  
      self.DefaultOversPricing:str = obj["DefaultOversPricing"]
      """  DefaultOversPricing  """  
      self.ECCPlant:str = obj["ECCPlant"]
      """  ECCPlant  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECCQuoteNum  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECCQuoteLine  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MfgJobType:str = obj["MfgJobType"]
      """  MfgJobType  """  
      self.ProFormaInvComment:str = obj["ProFormaInvComment"]
      """  ProFormaInvComment  """  
      self.CreateJob:bool = obj["CreateJob"]
      """  CreateJob  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.DocInAdvanceBillBal:int = obj["DocInAdvanceBillBal"]
      """  DocInAdvanceBillBal  """  
      self.InAdvanceBillBal:int = obj["InAdvanceBillBal"]
      """  InAdvanceBillBal  """  
      self.Rpt1InAdvanceBillBal:int = obj["Rpt1InAdvanceBillBal"]
      """  Rpt1InAdvanceBillBal  """  
      self.Rpt2InAdvanceBillBal:int = obj["Rpt2InAdvanceBillBal"]
      """  Rpt2InAdvanceBillBal  """  
      self.Rpt3InAdvanceBillBal:int = obj["Rpt3InAdvanceBillBal"]
      """  Rpt3InAdvanceBillBal  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency.  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency.  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency.  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency.  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors.  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  """  
      self.OrderLineStatusCode:str = obj["OrderLineStatusCode"]
      """  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Available Price Lists  """  
      self.AvailUMFromQuote:str = obj["AvailUMFromQuote"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CalcUnitPrice:int = obj["CalcUnitPrice"]
      """  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  """  
      self.ConfigType:str = obj["ConfigType"]
      self.Configured:str = obj["Configured"]
      self.CounterSale:bool = obj["CounterSale"]
      self.CreditLimitMessage:str = obj["CreditLimitMessage"]
      """  The message text returned by the credit check process.  """  
      self.CreditLimitSource:str = obj["CreditLimitSource"]
      """  The source that put the customer on credit hold.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DemandQuantity:int = obj["DemandQuantity"]
      self.DimCode:str = obj["DimCode"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      """  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.DocInMiscCharges:int = obj["DocInMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in document currency which does not include taxes  """  
      self.DocMiscCharges:int = obj["DocMiscCharges"]
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  """  
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.DspDiscount:int = obj["DspDiscount"]
      """  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DspJobType:str = obj["DspJobType"]
      """  To display the type of job this is: MFG = Manufacturing, PRJ = Project  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      """  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DUM:str = obj["DUM"]
      self.ECCConfigSysRowId:str = obj["ECCConfigSysRowId"]
      """  Web basket configuration related SysRowID  """  
      self.ECCDiscount:int = obj["ECCDiscount"]
      """  Additional discount calculated by ECC  """  
      self.ECCPreventRepricing:bool = obj["ECCPreventRepricing"]
      """  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the button Attibutes in Order Line  """  
      self.EnableKitUnitPrice:bool = obj["EnableKitUnitPrice"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.EnableRenewalNbr:bool = obj["EnableRenewalNbr"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.EnableSellingQty:bool = obj["EnableSellingQty"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.ExtPrice:int = obj["ExtPrice"]
      self.FromQuoteLineFlag:bool = obj["FromQuoteLineFlag"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      """  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  """  
      self.FSAInstallationOrderLine:int = obj["FSAInstallationOrderLine"]
      self.FSAInstallationOrderNum:int = obj["FSAInstallationOrderNum"]
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      """  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  """  
      self.FSAInstallationTypeDescription:str = obj["FSAInstallationTypeDescription"]
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.InMiscCharges:int = obj["InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line  """  
      self.InPrice:bool = obj["InPrice"]
      """  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Order Detail is allocated against.  """  
      self.JobTypeDesc:str = obj["JobTypeDesc"]
      self.JobWasCreated:bool = obj["JobWasCreated"]
      """  If the Job has been already created against this line.  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  Kit Flag Description. "P" = Parent, "C" = Component.  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.KitStandard:bool = obj["KitStandard"]
      """  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display which does not include taxes  """  
      self.LotNum:str = obj["LotNum"]
      self.MiscCharges:int = obj["MiscCharges"]
      self.MultipleReleases:bool = obj["MultipleReleases"]
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.PartExists:bool = obj["PartExists"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.POLineRef:str = obj["POLineRef"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.PriceListCodeDesc:str = obj["PriceListCodeDesc"]
      self.ProcessCounterSale:bool = obj["ProcessCounterSale"]
      self.ProcessQuickEntry:bool = obj["ProcessQuickEntry"]
      self.QuoteQtyNum:int = obj["QuoteQtyNum"]
      self.RelWasRecInvoiced:bool = obj["RelWasRecInvoiced"]
      """  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  """  
      self.RespMessage:str = obj["RespMessage"]
      """  Pass Credit Limit check message to the UI  """  
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Extended Price for the Order Line in Rpt1 currency  """  
      self.Rpt1InMiscCharges:int = obj["Rpt1InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display which does not include taxes (report currency)  """  
      self.Rpt1MiscCharges:int = obj["Rpt1MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Extended Price for the orderLine in Rpt2 currency.  """  
      self.Rpt2InMiscCharges:int = obj["Rpt2InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.Rpt2MiscCharges:int = obj["Rpt2MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Extended price for the order line in Rpt3 currency  """  
      self.Rpt3InMiscCharges:int = obj["Rpt3InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.Rpt3MiscCharges:int = obj["Rpt3MiscCharges"]
      """  Report Currency misc charges  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      """  Report currency line total price  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      self.SalesRepName2:str = obj["SalesRepName2"]
      self.SalesRepName3:str = obj["SalesRepName3"]
      self.SalesRepName4:str = obj["SalesRepName4"]
      self.SalesRepName5:str = obj["SalesRepName5"]
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the line.  """  
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  The Sales Order Quantity expressed in the Inventory Unit of Measure  """  
      self.TotalPrice:int = obj["TotalPrice"]
      self.TotalShipped:int = obj["TotalShipped"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.BinNum:str = obj["BinNum"]
      self.AttributeMismatch:bool = obj["AttributeMismatch"]
      """  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  """  
      self.JobManagerString:str = obj["JobManagerString"]
      """  A string containing the parameters needed to run Job Manager  """  
      self.CalcOrdBasedPrice:int = obj["CalcOrdBasedPrice"]
      """  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  """  
      self.SalesOrderLinked:bool = obj["SalesOrderLinked"]
      """  At least 1 OrderRel for OrderDtl has a PONum assigned.  """  
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      """  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.DiscBreakListCodeListDescription:str = obj["DiscBreakListCodeListDescription"]
      self.DiscBreakListCodeEndDate:str = obj["DiscBreakListCodeEndDate"]
      self.DiscBreakListCodeStartDate:str = obj["DiscBreakListCodeStartDate"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.OrderNumBTCustNum:int = obj["OrderNumBTCustNum"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumSendToFSA:bool = obj["PartNumSendToFSA"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumDefaultAttributeSetID:int = obj["PartNumDefaultAttributeSetID"]
      self.PartNumFSAEquipment:bool = obj["PartNumFSAEquipment"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      self.PriceBreakStartDate:str = obj["PriceBreakStartDate"]
      self.PriceBreakEndDate:str = obj["PriceBreakEndDate"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Phase_c:str = obj["Phase_c"]
      self.ItemID_c:str = obj["ItemID_c"]
      self.TypeCode_c:str = obj["TypeCode_c"]
      self.OrigTypeCode_c:str = obj["OrigTypeCode_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID_c:str = obj["SalesCatID_c"]
      self.IndustryShipDate_c:str = obj["IndustryShipDate_c"]
      self.CreateDate_c:str = obj["CreateDate_c"]
      self.PriceUpdateDate_c:str = obj["PriceUpdateDate_c"]
      self.CreatedBy_c:str = obj["CreatedBy_c"]
      self.UpdatedBy_c:str = obj["UpdatedBy_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   orderNum
   orderLine
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobCustTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  From JobProd.Company  """  
      self.JobNum:str = obj["JobNum"]
      """  From JobProd.JobNum  """  
      self.ProdQty:int = obj["ProdQty"]
      """  From JobProd.ProdQty  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  From JobProd.ShippedQty  """  
      self.OrderNum:int = obj["OrderNum"]
      """  From JobProd.OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  From JobProd.OrderLine  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  From JobProd.OrderRelNum  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  From OrderRel.NeedByDate  """  
      self.ReqDate:str = obj["ReqDate"]
      """  From OrderRel.ReqDate  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  From OrderRel.RevisionNum  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  From OrderRel.OurReqQty  """  
      self.PartNum:str = obj["PartNum"]
      """  From JobProd.PartNum  """  
      self.LineDesc:str = obj["LineDesc"]
      """  From JobProd.OrderLineLineDesc  """  
      self.IUM:str = obj["IUM"]
      """  From OrderDtl.IUM  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  From JobHead.ReqDueDate  """  
      self.StartDate:str = obj["StartDate"]
      """  From JobHead.StartDate  """  
      self.DueDate:str = obj["DueDate"]
      """  From JobHead.DueDate  """  
      self.Plant:str = obj["Plant"]
      """  From JobHead.Plant  """  
      self.CustNum:int = obj["CustNum"]
      """  From OrderDtl.CustNum  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  From OrderRel.OpenRelease  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  From JobHead.JobFirm  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  From JobHead.JobEngineered  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  From JobHead.JobReleased  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  From JobHead.JobComplete  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  From JobHead.JobClosed  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  From JobHead.JobHeld  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobCustTrkTableset:
   def __init__(self, obj):
      self.JobCustTrk:list[Erp_Tablesets_JobCustTrkRow] = obj["JobCustTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OrderDtlListRow:
   def __init__(self, obj):
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  """  
      self.AdvanceBillBal:int = obj["AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  """  
      self.DocAdvanceBillBal:int = obj["DocAdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  """  
      self.OrigWhyNoTax:str = obj["OrigWhyNoTax"]
      """  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  """  
      self.Rework:bool = obj["Rework"]
      """   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  """  
      self.RMANum:int = obj["RMANum"]
      """   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  The line item of the RMA detail that this order line item is fulfilling.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this OrderDtl record. Can be blank.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days"," Months", "Years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order line is linked to an inter-company PO line.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the order line can be changed.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  The Demand Contract Detail record this OrderDtl is related to.  """  
      self.CreateNewJob:bool = obj["CreateNewJob"]
      """  Create New Job flag  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.GetDtls:bool = obj["GetDtls"]
      """  Get Details flag  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.SchedJob:bool = obj["SchedJob"]
      """  Schedule Job flag  """  
      self.RelJob:bool = obj["RelJob"]
      """  Release Job flag  """  
      self.EnableCreateNewJob:bool = obj["EnableCreateNewJob"]
      """  Enable New Job flag  """  
      self.EnableGetDtls:bool = obj["EnableGetDtls"]
      """  Enable Get Details flag  """  
      self.EnableSchedJob:bool = obj["EnableSchedJob"]
      """  Enable Schedule Job flag  """  
      self.EnableRelJob:bool = obj["EnableRelJob"]
      """  Enable Release Job flag  """  
      self.CounterSaleWarehouse:str = obj["CounterSaleWarehouse"]
      """  Indicates the warehouse selected for a counter sale order line.  """  
      self.CounterSaleBinNum:str = obj["CounterSaleBinNum"]
      """  Identifies the Bin selected for a counter sale order line.  """  
      self.CounterSaleLotNum:str = obj["CounterSaleLotNum"]
      """  Indicates the lot number selected for a counter sale order line.  """  
      self.CounterSaleDimCode:str = obj["CounterSaleDimCode"]
      """  Indicates the dimension code selected for a counter sales order line.  """  
      self.DemandDtlRejected:bool = obj["DemandDtlRejected"]
      """  Indicates if the demand detail that created/updated this order line has been rejected.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.TotalReleases:int = obj["TotalReleases"]
      """  Total Number of releases for the line  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1AdvanceBillBal:int = obj["Rpt1AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt2AdvanceBillBal:int = obj["Rpt2AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt3AdvanceBillBal:int = obj["Rpt3AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Status of Order Line  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Same as DocUnit price except that this field contains the unit price including taxes  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency -including taxes.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied. including taxes  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.OldOurOpenQty:int = obj["OldOurOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldSellingOpenQty:int = obj["OldSellingOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldOpenValue:int = obj["OldOpenValue"]
      """  Used to store open value setting assigned in product configuration programs  """  
      self.OldProdCode:str = obj["OldProdCode"]
      """  Used to store prod code value assigned in product configuration programs  """  
      self.PrevSellQty:int = obj["PrevSellQty"]
      """  Previous Selling Quantity  """  
      self.PrevPartNum:str = obj["PrevPartNum"]
      """  Previous Part Number  """  
      self.PrevXPartNum:str = obj["PrevXPartNum"]
      """  Previous Customer Part Number  """  
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.LockDisc:bool = obj["LockDisc"]
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.TotalShipped:int = obj["TotalShipped"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.MiscCharges:int = obj["MiscCharges"]
      self.TotalPrice:int = obj["TotalPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.DocMiscCharges:int = obj["DocMiscCharges"]
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.Configured:str = obj["Configured"]
      self.QuoteQtyNum:int = obj["QuoteQtyNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DUM:str = obj["DUM"]
      self.ProcessQuickEntry:bool = obj["ProcessQuickEntry"]
      self.CounterSale:bool = obj["CounterSale"]
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Available Price Lists  """  
      self.ProcessCounterSale:bool = obj["ProcessCounterSale"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.DemandQuantity:int = obj["DemandQuantity"]
      self.AvailUMFromQuote:str = obj["AvailUMFromQuote"]
      self.FromQuoteLineFlag:bool = obj["FromQuoteLineFlag"]
      self.MultipleReleases:bool = obj["MultipleReleases"]
      self.PartExists:bool = obj["PartExists"]
      self.SalesRepName1:str = obj["SalesRepName1"]
      self.SalesRepName2:str = obj["SalesRepName2"]
      self.SalesRepName3:str = obj["SalesRepName3"]
      self.SalesRepName4:str = obj["SalesRepName4"]
      self.SalesRepName5:str = obj["SalesRepName5"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.CreditLimitMessage:str = obj["CreditLimitMessage"]
      """  The message text returned by the credit check process.  """  
      self.CreditLimitSource:str = obj["CreditLimitSource"]
      """  The source that put the customer on credit hold.  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  Kit Flag Description. "P" = Parent, "C" = Component.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitStandard:bool = obj["KitStandard"]
      """  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.PriceListCodeDesc:str = obj["PriceListCodeDesc"]
      self.EnableSellingQty:bool = obj["EnableSellingQty"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the line.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  """  
      self.EnableKitUnitPrice:bool = obj["EnableKitUnitPrice"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.Rpt1MiscCharges:int = obj["Rpt1MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt2MiscCharges:int = obj["Rpt2MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt3MiscCharges:int = obj["Rpt3MiscCharges"]
      """  Report Currency misc charges  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      """  Report currency line total price  """  
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  The Sales Order Quantity expressed in the Inventory Unit of Measure  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Order Detail is allocated against.  """  
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Extended Price for the Order Line in Rpt1 currency  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Extended Price for the orderLine in Rpt2 currency.  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Extended price for the order line in Rpt3 currency  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencyID:str = obj["CurrencyID"]
      self.POLineRef:str = obj["POLineRef"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      """  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      """  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.InPrice:bool = obj["InPrice"]
      """  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  """  
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in document currency which does not include taxes  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display which does not include taxes  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display which does not include taxes (report currency)  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.DocInMiscCharges:int = obj["DocInMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  """  
      self.InMiscCharges:int = obj["InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line  """  
      self.Rpt1InMiscCharges:int = obj["Rpt1InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt2InMiscCharges:int = obj["Rpt2InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt3InMiscCharges:int = obj["Rpt3InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      """  Description of the Marketing campaign  """  
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      """  Description.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      """  Description of the sales category.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      """  Description of the warranty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderDtlListTableset:
   def __init__(self, obj):
      self.OrderDtlList:list[Erp_Tablesets_OrderDtlListRow] = obj["OrderDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OrderDtlRow:
   def __init__(self, obj):
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  """  
      self.AdvanceBillBal:int = obj["AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  """  
      self.DocAdvanceBillBal:int = obj["DocAdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  """  
      self.OrigWhyNoTax:str = obj["OrigWhyNoTax"]
      """  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  """  
      self.Rework:bool = obj["Rework"]
      """   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  """  
      self.RMANum:int = obj["RMANum"]
      """   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  The line item of the RMA detail that this order line item is fulfilling.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this OrderDtl record. Can be blank.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days"," Months", "Years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order line is linked to an inter-company PO line.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the order line can be changed.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  The Demand Contract Detail record this OrderDtl is related to.  """  
      self.CreateNewJob:bool = obj["CreateNewJob"]
      """  Create New Job flag  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.GetDtls:bool = obj["GetDtls"]
      """  Get Details flag  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.SchedJob:bool = obj["SchedJob"]
      """  Schedule Job flag  """  
      self.RelJob:bool = obj["RelJob"]
      """  Release Job flag  """  
      self.EnableCreateNewJob:bool = obj["EnableCreateNewJob"]
      """  Enable New Job flag  """  
      self.EnableGetDtls:bool = obj["EnableGetDtls"]
      """  Enable Get Details flag  """  
      self.EnableSchedJob:bool = obj["EnableSchedJob"]
      """  Enable Schedule Job flag  """  
      self.EnableRelJob:bool = obj["EnableRelJob"]
      """  Enable Release Job flag  """  
      self.CounterSaleWarehouse:str = obj["CounterSaleWarehouse"]
      """  Indicates the warehouse selected for a counter sale order line.  """  
      self.CounterSaleBinNum:str = obj["CounterSaleBinNum"]
      """  Identifies the Bin selected for a counter sale order line.  """  
      self.CounterSaleLotNum:str = obj["CounterSaleLotNum"]
      """  Indicates the lot number selected for a counter sale order line.  """  
      self.CounterSaleDimCode:str = obj["CounterSaleDimCode"]
      """  Indicates the dimension code selected for a counter sales order line.  """  
      self.DemandDtlRejected:bool = obj["DemandDtlRejected"]
      """  Indicates if the demand detail that created/updated this order line has been rejected.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.TotalReleases:int = obj["TotalReleases"]
      """  Total Number of releases for the line  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1AdvanceBillBal:int = obj["Rpt1AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt2AdvanceBillBal:int = obj["Rpt2AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt3AdvanceBillBal:int = obj["Rpt3AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Status of Order Line  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Same as DocUnit price except that this field contains the unit price including taxes  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency -including taxes.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied. including taxes  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.OldOurOpenQty:int = obj["OldOurOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldSellingOpenQty:int = obj["OldSellingOpenQty"]
      """  Used to store selling open quantity value setting assigned in product configuration programs  """  
      self.OldOpenValue:int = obj["OldOpenValue"]
      """  Used to store open value setting assigned in product configuration programs  """  
      self.OldProdCode:str = obj["OldProdCode"]
      """  Used to store prod code value assigned in product configuration programs  """  
      self.PrevSellQty:int = obj["PrevSellQty"]
      """  Previous Selling Quantity  """  
      self.PrevPartNum:str = obj["PrevPartNum"]
      """  Previous Part Number  """  
      self.PrevXPartNum:str = obj["PrevXPartNum"]
      """  Previous Customer Part Number  """  
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.LockDisc:bool = obj["LockDisc"]
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.ECCOrderNum:str = obj["ECCOrderNum"]
      """  ECCOrderNum  """  
      self.ECCOrderLine:int = obj["ECCOrderLine"]
      """  ECCOrderLine  """  
      self.DupOnJobCrt:bool = obj["DupOnJobCrt"]
      """  DupOnJobCrt  """  
      self.UndersPct:int = obj["UndersPct"]
      """  UndersPct  """  
      self.Overs:int = obj["Overs"]
      """  Overs  """  
      self.Unders:int = obj["Unders"]
      """  Unders  """  
      self.OversUnitPrice:int = obj["OversUnitPrice"]
      """  OversUnitPrice  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.MOMsourceType:str = obj["MOMsourceType"]
      """  MOMsourceType  """  
      self.MOMsourceEst:str = obj["MOMsourceEst"]
      """  MOMsourceEst  """  
      self.DefaultOversPricing:str = obj["DefaultOversPricing"]
      """  DefaultOversPricing  """  
      self.ECCPlant:str = obj["ECCPlant"]
      """  ECCPlant  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECCQuoteNum  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECCQuoteLine  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MfgJobType:str = obj["MfgJobType"]
      """  MfgJobType  """  
      self.ProFormaInvComment:str = obj["ProFormaInvComment"]
      """  ProFormaInvComment  """  
      self.CreateJob:bool = obj["CreateJob"]
      """  CreateJob  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.DocInAdvanceBillBal:int = obj["DocInAdvanceBillBal"]
      """  DocInAdvanceBillBal  """  
      self.InAdvanceBillBal:int = obj["InAdvanceBillBal"]
      """  InAdvanceBillBal  """  
      self.Rpt1InAdvanceBillBal:int = obj["Rpt1InAdvanceBillBal"]
      """  Rpt1InAdvanceBillBal  """  
      self.Rpt2InAdvanceBillBal:int = obj["Rpt2InAdvanceBillBal"]
      """  Rpt2InAdvanceBillBal  """  
      self.Rpt3InAdvanceBillBal:int = obj["Rpt3InAdvanceBillBal"]
      """  Rpt3InAdvanceBillBal  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency.  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency.  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency.  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency.  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors.  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  """  
      self.OrderLineStatusCode:str = obj["OrderLineStatusCode"]
      """  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Available Price Lists  """  
      self.AvailUMFromQuote:str = obj["AvailUMFromQuote"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CalcUnitPrice:int = obj["CalcUnitPrice"]
      """  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  """  
      self.ConfigType:str = obj["ConfigType"]
      self.Configured:str = obj["Configured"]
      self.CounterSale:bool = obj["CounterSale"]
      self.CreditLimitMessage:str = obj["CreditLimitMessage"]
      """  The message text returned by the credit check process.  """  
      self.CreditLimitSource:str = obj["CreditLimitSource"]
      """  The source that put the customer on credit hold.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DemandQuantity:int = obj["DemandQuantity"]
      self.DimCode:str = obj["DimCode"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      """  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.DocInMiscCharges:int = obj["DocInMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in document currency which does not include taxes  """  
      self.DocMiscCharges:int = obj["DocMiscCharges"]
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  """  
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.DspDiscount:int = obj["DspDiscount"]
      """  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DspJobType:str = obj["DspJobType"]
      """  To display the type of job this is: MFG = Manufacturing, PRJ = Project  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      """  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.DUM:str = obj["DUM"]
      self.ECCConfigSysRowId:str = obj["ECCConfigSysRowId"]
      """  Web basket configuration related SysRowID  """  
      self.ECCDiscount:int = obj["ECCDiscount"]
      """  Additional discount calculated by ECC  """  
      self.ECCPreventRepricing:bool = obj["ECCPreventRepricing"]
      """  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the button Attibutes in Order Line  """  
      self.EnableKitUnitPrice:bool = obj["EnableKitUnitPrice"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.EnableRenewalNbr:bool = obj["EnableRenewalNbr"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.EnableSellingQty:bool = obj["EnableSellingQty"]
      """  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  """  
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.ExtPrice:int = obj["ExtPrice"]
      self.FromQuoteLineFlag:bool = obj["FromQuoteLineFlag"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      """  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  """  
      self.FSAInstallationOrderLine:int = obj["FSAInstallationOrderLine"]
      self.FSAInstallationOrderNum:int = obj["FSAInstallationOrderNum"]
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      """  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  """  
      self.FSAInstallationTypeDescription:str = obj["FSAInstallationTypeDescription"]
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.InMiscCharges:int = obj["InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line  """  
      self.InPrice:bool = obj["InPrice"]
      """  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Order Detail is allocated against.  """  
      self.JobTypeDesc:str = obj["JobTypeDesc"]
      self.JobWasCreated:bool = obj["JobWasCreated"]
      """  If the Job has been already created against this line.  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  Kit Flag Description. "P" = Parent, "C" = Component.  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.KitStandard:bool = obj["KitStandard"]
      """  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display which does not include taxes  """  
      self.LotNum:str = obj["LotNum"]
      self.MiscCharges:int = obj["MiscCharges"]
      self.MultipleReleases:bool = obj["MultipleReleases"]
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.PartExists:bool = obj["PartExists"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.POLineRef:str = obj["POLineRef"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.PriceListCodeDesc:str = obj["PriceListCodeDesc"]
      self.ProcessCounterSale:bool = obj["ProcessCounterSale"]
      self.ProcessQuickEntry:bool = obj["ProcessQuickEntry"]
      self.QuoteQtyNum:int = obj["QuoteQtyNum"]
      self.RelWasRecInvoiced:bool = obj["RelWasRecInvoiced"]
      """  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  """  
      self.RespMessage:str = obj["RespMessage"]
      """  Pass Credit Limit check message to the UI  """  
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Extended Price for the Order Line in Rpt1 currency  """  
      self.Rpt1InMiscCharges:int = obj["Rpt1InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display which does not include taxes (report currency)  """  
      self.Rpt1MiscCharges:int = obj["Rpt1MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Extended Price for the orderLine in Rpt2 currency.  """  
      self.Rpt2InMiscCharges:int = obj["Rpt2InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.Rpt2MiscCharges:int = obj["Rpt2MiscCharges"]
      """  Report currency misc charges  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      """  Report currency line total price  """  
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      """  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Extended price for the order line in Rpt3 currency  """  
      self.Rpt3InMiscCharges:int = obj["Rpt3InMiscCharges"]
      """  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in report currency which does not include taxes (report currency)  """  
      self.Rpt3MiscCharges:int = obj["Rpt3MiscCharges"]
      """  Report Currency misc charges  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Report currency line tax amount  """  
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      """  Report currency line total price  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      self.SalesRepName2:str = obj["SalesRepName2"]
      self.SalesRepName3:str = obj["SalesRepName3"]
      self.SalesRepName4:str = obj["SalesRepName4"]
      self.SalesRepName5:str = obj["SalesRepName5"]
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the line.  """  
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  The Sales Order Quantity expressed in the Inventory Unit of Measure  """  
      self.TotalPrice:int = obj["TotalPrice"]
      self.TotalShipped:int = obj["TotalShipped"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.BinNum:str = obj["BinNum"]
      self.AttributeMismatch:bool = obj["AttributeMismatch"]
      """  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  """  
      self.JobManagerString:str = obj["JobManagerString"]
      """  A string containing the parameters needed to run Job Manager  """  
      self.CalcOrdBasedPrice:int = obj["CalcOrdBasedPrice"]
      """  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  """  
      self.SalesOrderLinked:bool = obj["SalesOrderLinked"]
      """  At least 1 OrderRel for OrderDtl has a PONum assigned.  """  
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      """  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.DiscBreakListCodeListDescription:str = obj["DiscBreakListCodeListDescription"]
      self.DiscBreakListCodeEndDate:str = obj["DiscBreakListCodeEndDate"]
      self.DiscBreakListCodeStartDate:str = obj["DiscBreakListCodeStartDate"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.OrderNumBTCustNum:int = obj["OrderNumBTCustNum"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumSendToFSA:bool = obj["PartNumSendToFSA"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumDefaultAttributeSetID:int = obj["PartNumDefaultAttributeSetID"]
      self.PartNumFSAEquipment:bool = obj["PartNumFSAEquipment"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      self.PriceBreakStartDate:str = obj["PriceBreakStartDate"]
      self.PriceBreakEndDate:str = obj["PriceBreakEndDate"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Phase_c:str = obj["Phase_c"]
      self.ItemID_c:str = obj["ItemID_c"]
      self.TypeCode_c:str = obj["TypeCode_c"]
      self.OrigTypeCode_c:str = obj["OrigTypeCode_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID_c:str = obj["SalesCatID_c"]
      self.IndustryShipDate_c:str = obj["IndustryShipDate_c"]
      self.CreateDate_c:str = obj["CreateDate_c"]
      self.PriceUpdateDate_c:str = obj["PriceUpdateDate_c"]
      self.CreatedBy_c:str = obj["CreatedBy_c"]
      self.UpdatedBy_c:str = obj["UpdatedBy_c"]
      pass

class Erp_Tablesets_OrderDtlSearchTableset:
   def __init__(self, obj):
      self.OrderDtl:list[Erp_Tablesets_OrderDtlRow] = obj["OrderDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtOrderDtlSearchTableset:
   def __init__(self, obj):
      self.OrderDtl:list[Erp_Tablesets_OrderDtlRow] = obj["OrderDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   orderNum
   orderLine
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OrderDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewOrderDtl_input:
   """ Required : 
   ds
   orderNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["ds"]
      self.orderNum:int = obj["orderNum"]
      pass

class GetNewOrderDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseOrderDtl
   whereClauseOrderRel
   jobWhereClause
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  Whereclause for OrderDtl table.  """  
      self.whereClauseOrderRel:str = obj["whereClauseOrderRel"]
      """  Whereclause for OrderRel table.  """  
      self.jobWhereClause:str = obj["jobWhereClause"]
      """  Whereclause for Job table.  """  
      self.contactName:str = obj["contactName"]
      """  Contact name to return records for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerActivity_input:
   """ Required : 
   whereClause
   whereClauseOrderDtl
   whereClauseOrderRel
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause for Job table.  """  
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  Whereclause for OrderDtl table.  """  
      self.whereClauseOrderRel:str = obj["whereClauseOrderRel"]
      """  Whereclause for OrderRel table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerActivity_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTrackerAndSort_input:
   """ Required : 
   whereClauseOrderDtl
   whereClauseOrderRel
   jobWhereClause
   sortBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  Whereclause for OrderDtl table.  """  
      self.whereClauseOrderRel:str = obj["whereClauseOrderRel"]
      """  Whereclause for OrderRel table.  """  
      self.jobWhereClause:str = obj["jobWhereClause"]
      """  Whereclause for Job table.  """  
      self.sortBy:str = obj["sortBy"]
      """  Page size.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTrackerAndSort_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseOrderDtl
   whereClauseOrderRel
   jobWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  Whereclause for OrderDtl table.  """  
      self.whereClauseOrderRel:str = obj["whereClauseOrderRel"]
      """  Whereclause for OrderRel table.  """  
      self.jobWhereClause:str = obj["jobWhereClause"]
      """  Whereclause for Job table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseOrderDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtOrderDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtOrderDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getBreakListCodeDesc_input:
   """ Required : 
   pcListCode
   pcPartNum
   pcLineWarehouse
   pcCurrencyCode
   pdtOrderDate
   """  
   def __init__(self, obj):
      self.pcListCode:str = obj["pcListCode"]
      """  pcListCode  """  
      self.pcPartNum:str = obj["pcPartNum"]
      """  pcPartNum  """  
      self.pcLineWarehouse:str = obj["pcLineWarehouse"]
      """  pcLineWarehouse  """  
      self.pcCurrencyCode:str = obj["pcCurrencyCode"]
      """  pcCurrencyCode  """  
      self.pdtOrderDate:str = obj["pdtOrderDate"]
      """  pdtOrderDate  """  
      pass

class getBreakListCodeDesc_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A list in a string  """  
      pass

