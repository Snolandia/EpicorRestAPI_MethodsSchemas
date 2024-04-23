import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SalesOrdHedDtlSvc
# Description: BO for Sales Orders containing the header and detail tables only
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SalesOrdHedDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesOrdHedDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesOrdHedDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls",headers=creds) as resp:
           return await resp.json()

async def post_SalesOrdHedDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesOrdHedDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OrderHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesOrdHedDtls_Company_OrderNum(Company, OrderNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesOrdHedDtl item
   Description: Calls GetByID to retrieve the SalesOrdHedDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesOrdHedDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OrderHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesOrdHedDtls_Company_OrderNum(Company, OrderNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesOrdHedDtl for the service
   Description: Calls UpdateExt to update SalesOrdHedDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesOrdHedDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesOrdHedDtls_Company_OrderNum(Company, OrderNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesOrdHedDtl item
   Description: Call UpdateExt to delete SalesOrdHedDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesOrdHedDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesOrdHedDtls_Company_OrderNum_OrderDtls(Company, OrderNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OrderDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OrderDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")/OrderDtls",headers=creds) as resp:
           return await resp.json()

async def get_SalesOrdHedDtls_Company_OrderNum_OrderDtls_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OrderDtl item
   Description: Calls GetByID to retrieve the OrderDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtl1
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_OrderDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OrderDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderDtls
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls",headers=creds) as resp:
           return await resp.json()

async def post_OrderDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OrderDtls
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OrderDtls_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OrderDtl item
   Description: Calls GetByID to retrieve the OrderDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OrderDtls_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OrderDtl for the service
   Description: Calls UpdateExt to update OrderDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OrderDtl
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OrderDtls_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OrderDtl item
   Description: Call UpdateExt to delete OrderDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OrderDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseOrderHed, whereClauseOrderDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseOrderHed=" + whereClauseOrderHed
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(orderNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOrderHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOrderHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOrderHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrderHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrderHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderHedRow] = obj["value"]
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

class Erp_Tablesets_OrderHedListRow:
   def __init__(self, obj):
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.DepositBal:int = obj["DepositBal"]
      """  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.DocDepositBal:int = obj["DocDepositBal"]
      """  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      """  BTCustNumCustID  """  
      self.BTCustNumName:str = obj["BTCustNumName"]
      """  BTCustNumName  """  
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderHedRow:
   def __init__(self, obj):
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the order. Up to five codes can be  established. This field is not directly maintainable. Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The first one is defaulted from the Customer master if ship to is blank; otherwise, from the Ship To.  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.DepositBal:int = obj["DepositBal"]
      """  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.DocDepositBal:int = obj["DocDepositBal"]
      """  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this order.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The USERID of the user that overrode an order credit hold (system set).  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  The date that the user last overrode the customer credit hold (system set).  """  
      self.CreditOverrideTime:str = obj["CreditOverrideTime"]
      """  The time that the user last overrode the customer credit hold in HH:MM:SS format (system set).  """  
      self.CreditOverrideLimit:int = obj["CreditOverrideLimit"]
      """  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  """  
      self.SndAlrtShp:bool = obj["SndAlrtShp"]
      """  Controls if an alert is to be sent when shipments are made for this order.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
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
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.WebOrder:bool = obj["WebOrder"]
      """  Not editable, When SF Synch creates orders, this flag is set to YES.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      """  Updated Via SF Synch.  This is the authorization number from a third party credit card validation service.  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  Order created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module if 855 or 865 created.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order header is linked to an inter-company PO header.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.WebEntryPerson:str = obj["WebEntryPerson"]
      """  This is the web-login-id (email address) of the person that placed the order.  """  
      self.AckEmailSent:bool = obj["AckEmailSent"]
      """  Indicates whether the email acknowledgement of the order has been sent.  (For web orders)  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the order.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.EntryMethod:str = obj["EntryMethod"]
      """   Indicates Entry method program that used to create the order.
S = Standard, Q = Quick Entry,  C = Counter Sales, D = Demand/EDI  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this order.  """  
      self.CounterSale:bool = obj["CounterSale"]
      """  Flag used in sales order entry for counter sales orders.  """  
      self.CreateInvoice:bool = obj["CreateInvoice"]
      """  Create AR Invoice for counter sales order.  """  
      self.CreatePackingSlip:bool = obj["CreatePackingSlip"]
      """  Create Packing Slip for counter sale.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
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
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.BTConNum:int = obj["BTConNum"]
      """  New database field as it can be changed by user.  Default is set to BTCustNum?s primary billing contact.  If a primary billing contact is not set, default is ?None Selected?.  Keep in mind the BTCustNum field may be the same as CustNum (SoldTo) but the default would still be this customer?s primary billing contact where the ConNum field (Contact for sold to) is defaulting the primary purchasing contact.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.OutboundSalesDocCtr:int = obj["OutboundSalesDocCtr"]
      """  Incremented whenever an outbound sales document is generated from the order, i.e. Sales Order Acknowledgement, Response to Change, etc.  """  
      self.OutboundShipDocsCtr:int = obj["OutboundShipDocsCtr"]
      """  Incremented whenever an outbound shipping document is generated from the order, i.e. ASN.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this OrderHed is related to.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  The date after which the sales order should be canceled.  """  
      self.DemandRejected:bool = obj["DemandRejected"]
      """  Indicates if the demand that created/updated this order has been rejected.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      """  Indicates if the Order is a credit card order  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder third address line.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder country portion of the address  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To  third address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To country portion of the address  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To phone number  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Nam  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the order is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the order which could affect taxes (OrderDtl, OrderHed, OrderMisc, etc). It defaults from XASyst.SOReadyToCalcDflt field when an order is created.  """  
      self.TotalCharges:int = obj["TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalMisc:int = obj["TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalComm:int = obj["TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalAdvBill:int = obj["TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.TotalLines:int = obj["TotalLines"]
      """  Total number of lines on the order  """  
      self.TotalReleases:int = obj["TotalReleases"]
      """  Total Number of releases on order  """  
      self.TotalRelDates:int = obj["TotalRelDates"]
      """  Total number of distinct release dates on order  """  
      self.DocTotalCharges:int = obj["DocTotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalMisc:int = obj["DocTotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalComm:int = obj["DocTotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalAdvBill:int = obj["DocTotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.TotalShipped:int = obj["TotalShipped"]
      """  Total Shipped amount  """  
      self.TotalInvoiced:int = obj["TotalInvoiced"]
      """  Total amount of order that has been invoiced  """  
      self.TotalCommLines:int = obj["TotalCommLines"]
      """  Total number of lines that were commissionable  """  
      self.SRCommAmt1:int = obj["SRCommAmt1"]
      """  Commission earned for first sales rep  """  
      self.SRCommAmt2:int = obj["SRCommAmt2"]
      """  Commission earned for second sales rep  """  
      self.SRCommAmt3:int = obj["SRCommAmt3"]
      """  Commission earned for third sales rep  """  
      self.SRCommAmt4:int = obj["SRCommAmt4"]
      """  Commission earned for fourth sales rep  """  
      self.SRCommAmt5:int = obj["SRCommAmt5"]
      """  Commission earned for fifth sales rep  """  
      self.SRCommableAmt1:int = obj["SRCommableAmt1"]
      """  Total Commissionable Amount for first salesrep  """  
      self.SRCommableAmt2:int = obj["SRCommableAmt2"]
      """  Total Commissionable Amount for second salesrep  """  
      self.SRCommableAmt3:int = obj["SRCommableAmt3"]
      """  Total Commissionable Amount for third salesrep  """  
      self.SRCommableAmt4:int = obj["SRCommableAmt4"]
      """  Total Commissionable Amount for fourth salesrep  """  
      self.SRCommableAmt5:int = obj["SRCommableAmt5"]
      """  Total Commissionable Amount for fifth salesrep  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1DepositBal:int = obj["Rpt1DepositBal"]
      """  Display value contains the deposit balance in a reporting currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt2DepositBal:int = obj["Rpt2DepositBal"]
      """  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.Rpt3DepositBal:int = obj["Rpt3DepositBal"]
      """  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.Rpt1TotalCharges:int = obj["Rpt1TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalCharges:int = obj["Rpt2TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalCharges:int = obj["Rpt3TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalAdvBill:int = obj["Rpt1TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.Rpt2TotalAdvBill:int = obj["Rpt2TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.Rpt3TotalAdvBill:int = obj["Rpt3TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.Rpt1TotalMisc:int = obj["Rpt1TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalMisc:int = obj["Rpt2TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalMisc:int = obj["Rpt3TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalComm:int = obj["Rpt1TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalComm:int = obj["Rpt2TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalComm:int = obj["Rpt3TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
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
      self.OrderAmt:int = obj["OrderAmt"]
      """  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  """  
      self.DocOrderAmt:int = obj["DocOrderAmt"]
      """  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1OrderAmt:int = obj["Rpt1OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrderAmt:int = obj["Rpt2OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrderAmt:int = obj["Rpt3OrderAmt"]
      """  Reporting currency value of this field  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipment country  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.OrderStatus:str = obj["OrderStatus"]
      """  Status of Order  """  
      self.HoldSetByDemand:bool = obj["HoldSetByDemand"]
      """  Hold Set by Demand  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.InTotalCharges:int = obj["InTotalCharges"]
      """  Reserved for future use  """  
      self.InTotalMisc:int = obj["InTotalMisc"]
      """  Reserved for future use  """  
      self.InTotalDiscount:int = obj["InTotalDiscount"]
      """  Reserved for future use  """  
      self.DocInTotalCharges:int = obj["DocInTotalCharges"]
      """  Reserved for future use  """  
      self.DocInTotalMisc:int = obj["DocInTotalMisc"]
      """  Reserved for future use  """  
      self.DocInTotalDiscount:int = obj["DocInTotalDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InTotalCharges:int = obj["Rpt1InTotalCharges"]
      """  Reserved for future use  """  
      self.Rpt2InTotalCharges:int = obj["Rpt2InTotalCharges"]
      """  Reserved for future use  """  
      self.Rpt3InTotalCharges:int = obj["Rpt3InTotalCharges"]
      """  Reserved for future use  """  
      self.Rpt1InTotalMisc:int = obj["Rpt1InTotalMisc"]
      """  Reserved for future use  """  
      self.Rpt2InTotalMisc:int = obj["Rpt2InTotalMisc"]
      """  Reserved for future use  """  
      self.Rpt3InTotalMisc:int = obj["Rpt3InTotalMisc"]
      """  Reserved for future use  """  
      self.Rpt1InTotalDiscount:int = obj["Rpt1InTotalDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InTotalDiscount:int = obj["Rpt2InTotalDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InTotalDiscount:int = obj["Rpt3InTotalDiscount"]
      """  Reserved for future use  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. Default is from Customer(Bill To).  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify SO that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via DM, the default will be taken from the value in the DM records.  """  
      self.LOCHold:bool = obj["LOCHold"]
      """  Indicates that order is on hold due to amount exceeding value on Letter of Credit.  """  
      self.PSCurrCode:str = obj["PSCurrCode"]
      """  Currency code used in further packing slips.  """  
      self.InvCurrCode:str = obj["InvCurrCode"]
      """  Currency code used in further AR invoices.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastScheduleNumber:str = obj["LastScheduleNumber"]
      """  Last Schedule Number in which the demand was processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.ECCOrderNum:str = obj["ECCOrderNum"]
      """  ECCOrderNum  """  
      self.ECCPONum:str = obj["ECCPONum"]
      """  ECCPONum  """  
      self.WIOrder:str = obj["WIOrder"]
      """  WIOrder  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WIUsername:str = obj["WIUsername"]
      """  WIUsername  """  
      self.WIUserID:str = obj["WIUserID"]
      """  WIUserID  """  
      self.WICreditCardorder:bool = obj["WICreditCardorder"]
      """  WICreditCardorder  """  
      self.OrderCSR:str = obj["OrderCSR"]
      """  OrderCSR  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.ECCPaymentMethod:str = obj["ECCPaymentMethod"]
      """  ECCPaymentMethod  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.ProFormaInvComment:str = obj["ProFormaInvComment"]
      """  ProFormaInvComment  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.InvcOrderCmp:bool = obj["InvcOrderCmp"]
      """  InvcOrderCmp  """  
      self.ReprintSOAck:bool = obj["ReprintSOAck"]
      """  ReprintSOAck  """  
      self.CounterSOAck:int = obj["CounterSOAck"]
      """  CounterSOAck  """  
      self.DispatchReason:str = obj["DispatchReason"]
      """  DispatchReason  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag will be used to indicate if the sales order is ready to be fulfilled.  """  
      self.ShipByTime:int = obj["ShipByTime"]
      """  Ship the good by this time  """  
      self.TWFiscalYear:int = obj["TWFiscalYear"]
      """  Taiwan GUI Calendar Fiscal Year  """  
      self.TWFiscalYearSuffix:str = obj["TWFiscalYearSuffix"]
      """  Taiwan GUI Calendar Fiscal Year Suffix  """  
      self.TWFiscalPeriod:int = obj["TWFiscalPeriod"]
      """  Taiwan GUI Calendar Fiscal Period  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  GUI Group of Legal Numbers  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  Seller GUI Code  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  Buyer GUI Code  """  
      self.OrderOpenCredit:int = obj["OrderOpenCredit"]
      """  OrderOpenCredit  """  
      self.ClosedNotShipped:int = obj["ClosedNotShipped"]
      """  ClosedNotShipped  """  
      self.InvCurrDepositBal:int = obj["InvCurrDepositBal"]
      """  InvCurrDepositBal  """  
      self.PLArticle106c:bool = obj["PLArticle106c"]
      """  Article. 106c  """  
      self.PLInvIssuedByTaxpayer:bool = obj["PLInvIssuedByTaxpayer"]
      """  Invoices are issued by a taxpayer's representative  """  
      self.PLInvIssuedBySecondTaxpayer:bool = obj["PLInvIssuedBySecondTaxpayer"]
      """  Invoices issued by the second taxpayer  """  
      self.PLTouristService:bool = obj["PLTouristService"]
      """  Tourist Services  """  
      self.PLSecondHandOrArts:bool = obj["PLSecondHandOrArts"]
      """  Second hand goods, works of art, collectibles or antiques  """  
      self.PLLegalArticleAct:str = obj["PLLegalArticleAct"]
      """  Appropriate Legal Article of the Act  """  
      self.PLLegalArticleWEDirective:str = obj["PLLegalArticleWEDirective"]
      """  Appropriate Legal Article of 2006/112/WE Directive  """  
      self.PLLegalArticleOther:str = obj["PLLegalArticleOther"]
      """  Other Legal Article  """  
      self.PLEnforcementAuthName:str = obj["PLEnforcementAuthName"]
      """  Name of the Enforcement Authority or the Name of the Judicial Officer  """  
      self.PLEnforcementAuthAddr:str = obj["PLEnforcementAuthAddr"]
      """  Address of the Enforcement Authority or Judicial Officer  """  
      self.PLTaxRepresentativeName:str = obj["PLTaxRepresentativeName"]
      """  Tax Representative Name  """  
      self.PLTaxRepresentativeAddr:str = obj["PLTaxRepresentativeAddr"]
      """  Tax Representative Address  """  
      self.PLTaxRepresentativeTaxID:str = obj["PLTaxRepresentativeTaxID"]
      """  Tax ID of the Tax Representative  """  
      self.PLMarginScheme:int = obj["PLMarginScheme"]
      """  Margin Scheme  """  
      self.PLGoodsOrServiceVATExempt:bool = obj["PLGoodsOrServiceVATExempt"]
      """  Goods or Service VAT exempt  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State  """  
      self.ExtAOEUserID:str = obj["ExtAOEUserID"]
      """  ExtAOEUserID  """  
      self.ExtAOE:str = obj["ExtAOE"]
      """  ExtAOE  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
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
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      """  Bill to customer name.  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill To Address List.  """  
      self.BTContactEMailAddress:str = obj["BTContactEMailAddress"]
      self.BTContactFaxNum:str = obj["BTContactFaxNum"]
      """  Bill to contact fax number.  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Bill to contact name.  """  
      self.BTContactPhoneNum:str = obj["BTContactPhoneNum"]
      """  Bill to contact phone number.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.CanChangeTaxLiab:bool = obj["CanChangeTaxLiab"]
      """  The flag to indicate if the user can change Tax Liability on the header level after adding a detail line.  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCRounding:int = obj["CCRounding"]
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustomerPrintAck:bool = obj["CustomerPrintAck"]
      self.CustomerRequiresPO:bool = obj["CustomerRequiresPO"]
      """  If true the customer requires a unique PO on Sales Orders  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      """  When set to true, indicates that this customer does not have credit available from your company.  """  
      self.CustTradePartnerName:str = obj["CustTradePartnerName"]
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.DocCCRounding:int = obj["DocCCRounding"]
      self.DocTotalNet:int = obj["DocTotalNet"]
      self.DocTotalOrder:int = obj["DocTotalOrder"]
      self.dspBTCustID:str = obj["dspBTCustID"]
      """  If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.ECCEmail:str = obj["ECCEmail"]
      """  ECC Contact Email - Contains the email address of the ECC login that placed the sales order. This only applies for B2C Orders.  """  
      self.ECCPaymentDesc:str = obj["ECCPaymentDesc"]
      """  ECC Payment Description  """  
      self.EnableCreditCard:bool = obj["EnableCreditCard"]
      """  True when Credit Card Procesing module is enabled  """  
      self.EnableJobWizard:bool = obj["EnableJobWizard"]
      """  True when Job Wizard must be enabled  """  
      self.EnableSoldToID:bool = obj["EnableSoldToID"]
      """  True when SoldTo ID must be enabled  """  
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.ERSOverride:bool = obj["ERSOverride"]
      """  It will be displayed when the value of the ERS flag at the sales order is different from the value in the customer master file.  """  
      self.HasMiscCharges:bool = obj["HasMiscCharges"]
      """  Used by UI to disable CurrencyCode  """  
      self.HasOrderLines:bool = obj["HasOrderLines"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.LinkMsg:str = obj["LinkMsg"]
      self.NoTaxRgnChange:bool = obj["NoTaxRgnChange"]
      """  Internal field which indicates if Order Tax Liability is not going to be changed even though Ship To is changed.  Related to Tax inclusive pricing. Depends on user response.  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Header)  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  Contains the Parent Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ProposedTaxRgn:str = obj["ProposedTaxRgn"]
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.ResetBTCustAddr:bool = obj["ResetBTCustAddr"]
      """  Internal field toindicate if the system should reset Bill to Customer address.  Based on the  user reply for LOC.  """  
      self.ResetRelTaxRgn:bool = obj["ResetRelTaxRgn"]
      """  Internal field which indicates if existing Release Tax Region should be se-set to the new Order Header Tax Liability.  Depends on the user reply.  """  
      self.Rpt1CCRounding:int = obj["Rpt1CCRounding"]
      self.Rpt1TotalNet:int = obj["Rpt1TotalNet"]
      self.Rpt2CCRounding:int = obj["Rpt2CCRounding"]
      self.Rpt2TotalNet:int = obj["Rpt2TotalNet"]
      self.Rpt3CCRounding:int = obj["Rpt3CCRounding"]
      self.Rpt3TotalNet:int = obj["Rpt3TotalNet"]
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  Element 1 of SalesRepList  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  Element 2 of SalesRepList  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  Element 3 of SalesRepList  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  Element 4 of SalesRepList  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  Element 5 of SalesRepList  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      self.SalesRepName2:str = obj["SalesRepName2"]
      self.SalesRepName3:str = obj["SalesRepName3"]
      self.SalesRepName4:str = obj["SalesRepName4"]
      self.SalesRepName5:str = obj["SalesRepName5"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShipToCustId:str = obj["ShipToCustId"]
      """  Customer Id of the third-party Ship To  """  
      self.ShowApplyOrderDiscountsControl:bool = obj["ShowApplyOrderDiscountsControl"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      self.SoldToContactEMailAddress:str = obj["SoldToContactEMailAddress"]
      self.SoldToContactFaxNum:str = obj["SoldToContactFaxNum"]
      self.SoldToContactName:str = obj["SoldToContactName"]
      self.SoldToContactPhoneNum:str = obj["SoldToContactPhoneNum"]
      self.TermsType:str = obj["TermsType"]
      """  This field defines the type of the term  """  
      self.TotalNet:int = obj["TotalNet"]
      self.TotalOrder:int = obj["TotalOrder"]
      self.TranDocTypeDescr:str = obj["TranDocTypeDescr"]
      self.TrueDiscountPercent:int = obj["TrueDiscountPercent"]
      """  the true discount percent from the order total  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  Taiwan GUI Legal Number Generation Type  """  
      self.UpdateDtlAndRelRecords:bool = obj["UpdateDtlAndRelRecords"]
      self.InvoicesExist:bool = obj["InvoicesExist"]
      """  Indicates if one or more invoices exist for this order  """  
      self.BTAddressFormatted:str = obj["BTAddressFormatted"]
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  The formatted ship to address  """  
      self.SoldToAddressFormatted:str = obj["SoldToAddressFormatted"]
      """  The formatted Sold To Address  """  
      self.TranDate:str = obj["TranDate"]
      self.TranNum:int = obj["TranNum"]
      self.TranTime:int = obj["TranTime"]
      self.OrderRelNeedByDateNotNull:bool = obj["OrderRelNeedByDateNotNull"]
      """  Indicates there is an OrderRel record that has a non-null NeedByDate  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the order is inactive.  """  
      self.EnableAllocationQueueActions:bool = obj["EnableAllocationQueueActions"]
      """  Enable Fulfillment Queue Actions  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      self.BTCustNumName:str = obj["BTCustNumName"]
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.InvCurrCurrDesc:str = obj["InvCurrCurrDesc"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.PlantName:str = obj["PlantName"]
      self.PSCurrCurrDesc:str = obj["PSCurrCurrDesc"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeInactive:bool = obj["ShipViaCodeInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Project_c:str = obj["Project_c"]
      self.OriginalOrderNo_c:int = obj["OriginalOrderNo_c"]
      self.MASFlag_c:bool = obj["MASFlag_c"]
      self.Estimate_c:bool = obj["Estimate_c"]
      self.ShipOrderComplete_c:bool = obj["ShipOrderComplete_c"]
      self.ProjectID_c:str = obj["ProjectID_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID__c:str = obj["SalesCatID__c"]
      self.TaxCatID_c:str = obj["TaxCatID_c"]
      self.MfgOrder_c:bool = obj["MfgOrder_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   orderNum
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_OrderCustTrkRow:
   def __init__(self, obj):
      self.OrderNum:int = obj["OrderNum"]
      """  from OrderHed.OrderNum  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  from OrderHed.OpenOrder  """  
      self.Company:str = obj["Company"]
      """  from OrderHed.Company  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  from OrderHed.OrderHeld  """  
      self.PONum:str = obj["PONum"]
      """  from OrderHed.PONum  """  
      self.CustNum:int = obj["CustNum"]
      """  from OrderHed.CustNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  from OrderHed.ShipToNum  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  from OrderHed.ShpConNum  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  from OrderHed.PrcConNum  """  
      self.OrderDate:str = obj["OrderDate"]
      """  from OrderHed.OrderDate  """  
      self.OrderHedNeedByDate:str = obj["OrderHedNeedByDate"]
      """  from OrderHed.NeedByDate  """  
      self.OrderHedRequestDate:str = obj["OrderHedRequestDate"]
      """  from OrderHed.RequestDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  from OrderHed.Currency  """  
      self.OrderLine:int = obj["OrderLine"]
      """  from OrderDtl.OrderLine  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  from OrderDtl.OpenLine  """  
      self.POLine:str = obj["POLine"]
      """  from OrderDtl.POLine  """  
      self.PartNum:str = obj["PartNum"]
      """  from OrderDtl.PartNum  """  
      self.LineDesc:str = obj["LineDesc"]
      """  from OrderDtl.LineDesc  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  from OrderDtl.SellingQuantity  """  
      self.SalesUM:str = obj["SalesUM"]
      """  from OrderDtl.SalesUM  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  from OrderDtl.DocUnitPrice  """  
      self.ProdCode:str = obj["ProdCode"]
      """  from OrderDtl.ProdCode  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  from OrderDtl.ProdCodeDescription  """  
      self.OrderDtlNeedByDate:str = obj["OrderDtlNeedByDate"]
      """  from OrderDtl.NeedByDate  """  
      self.OrderDtlRequestDate:str = obj["OrderDtlRequestDate"]
      """  from OrderDtl.RequestDate  """  
      self.WebOrder:bool = obj["WebOrder"]
      """  from OrderHed.WebOrder  """  
      self.OnCreditHold:bool = obj["OnCreditHold"]
      """  If OrderHed.CustOnCreditHold = true and OrderHed.CreditOverride = false and OrderHed.OpenOrder = true then true otherwise false  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  from OrderDtl.RevisionNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  from OrderDtl.XPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  from OrderDtl.XRevisionNum  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To customer number from OrderHed.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID from OrderHed.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill To Customer Name.  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill to address list.  """  
      self.BTContactFaxNum:str = obj["BTContactFaxNum"]
      """  Bill to contact fax number.  """  
      self.BTContactPhoneNum:str = obj["BTContactPhoneNum"]
      """  Bill to contact phone number  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Bill To Contact name.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill to contact num.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  Sold to customer id.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Sold to customer name.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.POLineRef:str = obj["POLineRef"]
      """  from OrderDtl.POLineRef  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderCustTrkTableset:
   def __init__(self, obj):
      self.OrderCustTrk:list[Erp_Tablesets_OrderCustTrkRow] = obj["OrderCustTrk"]
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

class Erp_Tablesets_OrderHedListRow:
   def __init__(self, obj):
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.DepositBal:int = obj["DepositBal"]
      """  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.DocDepositBal:int = obj["DocDepositBal"]
      """  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      """  BTCustNumCustID  """  
      self.BTCustNumName:str = obj["BTCustNumName"]
      """  BTCustNumName  """  
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderHedListTableset:
   def __init__(self, obj):
      self.OrderHedList:list[Erp_Tablesets_OrderHedListRow] = obj["OrderHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OrderHedRow:
   def __init__(self, obj):
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the order. Up to five codes can be  established. This field is not directly maintainable. Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The first one is defaulted from the Customer master if ship to is blank; otherwise, from the Ship To.  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.DepositBal:int = obj["DepositBal"]
      """  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.DocDepositBal:int = obj["DocDepositBal"]
      """  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this order.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The USERID of the user that overrode an order credit hold (system set).  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  The date that the user last overrode the customer credit hold (system set).  """  
      self.CreditOverrideTime:str = obj["CreditOverrideTime"]
      """  The time that the user last overrode the customer credit hold in HH:MM:SS format (system set).  """  
      self.CreditOverrideLimit:int = obj["CreditOverrideLimit"]
      """  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  """  
      self.SndAlrtShp:bool = obj["SndAlrtShp"]
      """  Controls if an alert is to be sent when shipments are made for this order.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
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
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.WebOrder:bool = obj["WebOrder"]
      """  Not editable, When SF Synch creates orders, this flag is set to YES.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      """  Updated Via SF Synch.  This is the authorization number from a third party credit card validation service.  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  Order created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module if 855 or 865 created.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order header is linked to an inter-company PO header.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.WebEntryPerson:str = obj["WebEntryPerson"]
      """  This is the web-login-id (email address) of the person that placed the order.  """  
      self.AckEmailSent:bool = obj["AckEmailSent"]
      """  Indicates whether the email acknowledgement of the order has been sent.  (For web orders)  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the order.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.EntryMethod:str = obj["EntryMethod"]
      """   Indicates Entry method program that used to create the order.
S = Standard, Q = Quick Entry,  C = Counter Sales, D = Demand/EDI  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this order.  """  
      self.CounterSale:bool = obj["CounterSale"]
      """  Flag used in sales order entry for counter sales orders.  """  
      self.CreateInvoice:bool = obj["CreateInvoice"]
      """  Create AR Invoice for counter sales order.  """  
      self.CreatePackingSlip:bool = obj["CreatePackingSlip"]
      """  Create Packing Slip for counter sale.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
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
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.BTConNum:int = obj["BTConNum"]
      """  New database field as it can be changed by user.  Default is set to BTCustNum?s primary billing contact.  If a primary billing contact is not set, default is ?None Selected?.  Keep in mind the BTCustNum field may be the same as CustNum (SoldTo) but the default would still be this customer?s primary billing contact where the ConNum field (Contact for sold to) is defaulting the primary purchasing contact.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.OutboundSalesDocCtr:int = obj["OutboundSalesDocCtr"]
      """  Incremented whenever an outbound sales document is generated from the order, i.e. Sales Order Acknowledgement, Response to Change, etc.  """  
      self.OutboundShipDocsCtr:int = obj["OutboundShipDocsCtr"]
      """  Incremented whenever an outbound shipping document is generated from the order, i.e. ASN.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this OrderHed is related to.  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  The date before which the order cannot be shipped.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  The date after which the order cannot be shipped.  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  The date after which the sales order should be canceled.  """  
      self.DemandRejected:bool = obj["DemandRejected"]
      """  Indicates if the demand that created/updated this order has been rejected.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      """  Indicates if the Order is a credit card order  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder third address line.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder country portion of the address  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To  third address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To country portion of the address  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To phone number  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Nam  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the order is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the order which could affect taxes (OrderDtl, OrderHed, OrderMisc, etc). It defaults from XASyst.SOReadyToCalcDflt field when an order is created.  """  
      self.TotalCharges:int = obj["TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalMisc:int = obj["TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalComm:int = obj["TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalAdvBill:int = obj["TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.TotalLines:int = obj["TotalLines"]
      """  Total number of lines on the order  """  
      self.TotalReleases:int = obj["TotalReleases"]
      """  Total Number of releases on order  """  
      self.TotalRelDates:int = obj["TotalRelDates"]
      """  Total number of distinct release dates on order  """  
      self.DocTotalCharges:int = obj["DocTotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalMisc:int = obj["DocTotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.DocTotalComm:int = obj["DocTotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalAdvBill:int = obj["DocTotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.TotalShipped:int = obj["TotalShipped"]
      """  Total Shipped amount  """  
      self.TotalInvoiced:int = obj["TotalInvoiced"]
      """  Total amount of order that has been invoiced  """  
      self.TotalCommLines:int = obj["TotalCommLines"]
      """  Total number of lines that were commissionable  """  
      self.SRCommAmt1:int = obj["SRCommAmt1"]
      """  Commission earned for first sales rep  """  
      self.SRCommAmt2:int = obj["SRCommAmt2"]
      """  Commission earned for second sales rep  """  
      self.SRCommAmt3:int = obj["SRCommAmt3"]
      """  Commission earned for third sales rep  """  
      self.SRCommAmt4:int = obj["SRCommAmt4"]
      """  Commission earned for fourth sales rep  """  
      self.SRCommAmt5:int = obj["SRCommAmt5"]
      """  Commission earned for fifth sales rep  """  
      self.SRCommableAmt1:int = obj["SRCommableAmt1"]
      """  Total Commissionable Amount for first salesrep  """  
      self.SRCommableAmt2:int = obj["SRCommableAmt2"]
      """  Total Commissionable Amount for second salesrep  """  
      self.SRCommableAmt3:int = obj["SRCommableAmt3"]
      """  Total Commissionable Amount for third salesrep  """  
      self.SRCommableAmt4:int = obj["SRCommableAmt4"]
      """  Total Commissionable Amount for fourth salesrep  """  
      self.SRCommableAmt5:int = obj["SRCommableAmt5"]
      """  Total Commissionable Amount for fifth salesrep  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1DepositBal:int = obj["Rpt1DepositBal"]
      """  Display value contains the deposit balance in a reporting currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt2DepositBal:int = obj["Rpt2DepositBal"]
      """  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.Rpt3DepositBal:int = obj["Rpt3DepositBal"]
      """  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.Rpt1TotalCharges:int = obj["Rpt1TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalCharges:int = obj["Rpt2TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalCharges:int = obj["Rpt3TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalAdvBill:int = obj["Rpt1TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.Rpt2TotalAdvBill:int = obj["Rpt2TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.Rpt3TotalAdvBill:int = obj["Rpt3TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.Rpt1TotalMisc:int = obj["Rpt1TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalMisc:int = obj["Rpt2TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalMisc:int = obj["Rpt3TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalComm:int = obj["Rpt1TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalComm:int = obj["Rpt2TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalComm:int = obj["Rpt3TotalComm"]
      """   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
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
      self.OrderAmt:int = obj["OrderAmt"]
      """  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  """  
      self.DocOrderAmt:int = obj["DocOrderAmt"]
      """  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1OrderAmt:int = obj["Rpt1OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrderAmt:int = obj["Rpt2OrderAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrderAmt:int = obj["Rpt3OrderAmt"]
      """  Reporting currency value of this field  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipment country  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.OrderStatus:str = obj["OrderStatus"]
      """  Status of Order  """  
      self.HoldSetByDemand:bool = obj["HoldSetByDemand"]
      """  Hold Set by Demand  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.InTotalCharges:int = obj["InTotalCharges"]
      """  Reserved for future use  """  
      self.InTotalMisc:int = obj["InTotalMisc"]
      """  Reserved for future use  """  
      self.InTotalDiscount:int = obj["InTotalDiscount"]
      """  Reserved for future use  """  
      self.DocInTotalCharges:int = obj["DocInTotalCharges"]
      """  Reserved for future use  """  
      self.DocInTotalMisc:int = obj["DocInTotalMisc"]
      """  Reserved for future use  """  
      self.DocInTotalDiscount:int = obj["DocInTotalDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InTotalCharges:int = obj["Rpt1InTotalCharges"]
      """  Reserved for future use  """  
      self.Rpt2InTotalCharges:int = obj["Rpt2InTotalCharges"]
      """  Reserved for future use  """  
      self.Rpt3InTotalCharges:int = obj["Rpt3InTotalCharges"]
      """  Reserved for future use  """  
      self.Rpt1InTotalMisc:int = obj["Rpt1InTotalMisc"]
      """  Reserved for future use  """  
      self.Rpt2InTotalMisc:int = obj["Rpt2InTotalMisc"]
      """  Reserved for future use  """  
      self.Rpt3InTotalMisc:int = obj["Rpt3InTotalMisc"]
      """  Reserved for future use  """  
      self.Rpt1InTotalDiscount:int = obj["Rpt1InTotalDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InTotalDiscount:int = obj["Rpt2InTotalDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InTotalDiscount:int = obj["Rpt3InTotalDiscount"]
      """  Reserved for future use  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. Default is from Customer(Bill To).  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  It will be used to identify SO that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via DM, the default will be taken from the value in the DM records.  """  
      self.LOCHold:bool = obj["LOCHold"]
      """  Indicates that order is on hold due to amount exceeding value on Letter of Credit.  """  
      self.PSCurrCode:str = obj["PSCurrCode"]
      """  Currency code used in further packing slips.  """  
      self.InvCurrCode:str = obj["InvCurrCode"]
      """  Currency code used in further AR invoices.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastScheduleNumber:str = obj["LastScheduleNumber"]
      """  Last Schedule Number in which the demand was processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.ECCOrderNum:str = obj["ECCOrderNum"]
      """  ECCOrderNum  """  
      self.ECCPONum:str = obj["ECCPONum"]
      """  ECCPONum  """  
      self.WIOrder:str = obj["WIOrder"]
      """  WIOrder  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WIUsername:str = obj["WIUsername"]
      """  WIUsername  """  
      self.WIUserID:str = obj["WIUserID"]
      """  WIUserID  """  
      self.WICreditCardorder:bool = obj["WICreditCardorder"]
      """  WICreditCardorder  """  
      self.OrderCSR:str = obj["OrderCSR"]
      """  OrderCSR  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.ECCPaymentMethod:str = obj["ECCPaymentMethod"]
      """  ECCPaymentMethod  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.ProFormaInvComment:str = obj["ProFormaInvComment"]
      """  ProFormaInvComment  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.InvcOrderCmp:bool = obj["InvcOrderCmp"]
      """  InvcOrderCmp  """  
      self.ReprintSOAck:bool = obj["ReprintSOAck"]
      """  ReprintSOAck  """  
      self.CounterSOAck:int = obj["CounterSOAck"]
      """  CounterSOAck  """  
      self.DispatchReason:str = obj["DispatchReason"]
      """  DispatchReason  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag will be used to indicate if the sales order is ready to be fulfilled.  """  
      self.ShipByTime:int = obj["ShipByTime"]
      """  Ship the good by this time  """  
      self.TWFiscalYear:int = obj["TWFiscalYear"]
      """  Taiwan GUI Calendar Fiscal Year  """  
      self.TWFiscalYearSuffix:str = obj["TWFiscalYearSuffix"]
      """  Taiwan GUI Calendar Fiscal Year Suffix  """  
      self.TWFiscalPeriod:int = obj["TWFiscalPeriod"]
      """  Taiwan GUI Calendar Fiscal Period  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  GUI Group of Legal Numbers  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  Seller GUI Code  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  Buyer GUI Code  """  
      self.OrderOpenCredit:int = obj["OrderOpenCredit"]
      """  OrderOpenCredit  """  
      self.ClosedNotShipped:int = obj["ClosedNotShipped"]
      """  ClosedNotShipped  """  
      self.InvCurrDepositBal:int = obj["InvCurrDepositBal"]
      """  InvCurrDepositBal  """  
      self.PLArticle106c:bool = obj["PLArticle106c"]
      """  Article. 106c  """  
      self.PLInvIssuedByTaxpayer:bool = obj["PLInvIssuedByTaxpayer"]
      """  Invoices are issued by a taxpayer's representative  """  
      self.PLInvIssuedBySecondTaxpayer:bool = obj["PLInvIssuedBySecondTaxpayer"]
      """  Invoices issued by the second taxpayer  """  
      self.PLTouristService:bool = obj["PLTouristService"]
      """  Tourist Services  """  
      self.PLSecondHandOrArts:bool = obj["PLSecondHandOrArts"]
      """  Second hand goods, works of art, collectibles or antiques  """  
      self.PLLegalArticleAct:str = obj["PLLegalArticleAct"]
      """  Appropriate Legal Article of the Act  """  
      self.PLLegalArticleWEDirective:str = obj["PLLegalArticleWEDirective"]
      """  Appropriate Legal Article of 2006/112/WE Directive  """  
      self.PLLegalArticleOther:str = obj["PLLegalArticleOther"]
      """  Other Legal Article  """  
      self.PLEnforcementAuthName:str = obj["PLEnforcementAuthName"]
      """  Name of the Enforcement Authority or the Name of the Judicial Officer  """  
      self.PLEnforcementAuthAddr:str = obj["PLEnforcementAuthAddr"]
      """  Address of the Enforcement Authority or Judicial Officer  """  
      self.PLTaxRepresentativeName:str = obj["PLTaxRepresentativeName"]
      """  Tax Representative Name  """  
      self.PLTaxRepresentativeAddr:str = obj["PLTaxRepresentativeAddr"]
      """  Tax Representative Address  """  
      self.PLTaxRepresentativeTaxID:str = obj["PLTaxRepresentativeTaxID"]
      """  Tax ID of the Tax Representative  """  
      self.PLMarginScheme:int = obj["PLMarginScheme"]
      """  Margin Scheme  """  
      self.PLGoodsOrServiceVATExempt:bool = obj["PLGoodsOrServiceVATExempt"]
      """  Goods or Service VAT exempt  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State  """  
      self.ExtAOEUserID:str = obj["ExtAOEUserID"]
      """  ExtAOEUserID  """  
      self.ExtAOE:str = obj["ExtAOE"]
      """  ExtAOE  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
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
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      """  Bill to customer name.  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill To Address List.  """  
      self.BTContactEMailAddress:str = obj["BTContactEMailAddress"]
      self.BTContactFaxNum:str = obj["BTContactFaxNum"]
      """  Bill to contact fax number.  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Bill to contact name.  """  
      self.BTContactPhoneNum:str = obj["BTContactPhoneNum"]
      """  Bill to contact phone number.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.CanChangeTaxLiab:bool = obj["CanChangeTaxLiab"]
      """  The flag to indicate if the user can change Tax Liability on the header level after adding a detail line.  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCRounding:int = obj["CCRounding"]
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustomerPrintAck:bool = obj["CustomerPrintAck"]
      self.CustomerRequiresPO:bool = obj["CustomerRequiresPO"]
      """  If true the customer requires a unique PO on Sales Orders  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      """  When set to true, indicates that this customer does not have credit available from your company.  """  
      self.CustTradePartnerName:str = obj["CustTradePartnerName"]
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.DocCCRounding:int = obj["DocCCRounding"]
      self.DocTotalNet:int = obj["DocTotalNet"]
      self.DocTotalOrder:int = obj["DocTotalOrder"]
      self.dspBTCustID:str = obj["dspBTCustID"]
      """  If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.ECCEmail:str = obj["ECCEmail"]
      """  ECC Contact Email - Contains the email address of the ECC login that placed the sales order. This only applies for B2C Orders.  """  
      self.ECCPaymentDesc:str = obj["ECCPaymentDesc"]
      """  ECC Payment Description  """  
      self.EnableCreditCard:bool = obj["EnableCreditCard"]
      """  True when Credit Card Procesing module is enabled  """  
      self.EnableJobWizard:bool = obj["EnableJobWizard"]
      """  True when Job Wizard must be enabled  """  
      self.EnableSoldToID:bool = obj["EnableSoldToID"]
      """  True when SoldTo ID must be enabled  """  
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.ERSOverride:bool = obj["ERSOverride"]
      """  It will be displayed when the value of the ERS flag at the sales order is different from the value in the customer master file.  """  
      self.HasMiscCharges:bool = obj["HasMiscCharges"]
      """  Used by UI to disable CurrencyCode  """  
      self.HasOrderLines:bool = obj["HasOrderLines"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.LinkMsg:str = obj["LinkMsg"]
      self.NoTaxRgnChange:bool = obj["NoTaxRgnChange"]
      """  Internal field which indicates if Order Tax Liability is not going to be changed even though Ship To is changed.  Related to Tax inclusive pricing. Depends on user response.  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Header)  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  Contains the Parent Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ProposedTaxRgn:str = obj["ProposedTaxRgn"]
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.ResetBTCustAddr:bool = obj["ResetBTCustAddr"]
      """  Internal field toindicate if the system should reset Bill to Customer address.  Based on the  user reply for LOC.  """  
      self.ResetRelTaxRgn:bool = obj["ResetRelTaxRgn"]
      """  Internal field which indicates if existing Release Tax Region should be se-set to the new Order Header Tax Liability.  Depends on the user reply.  """  
      self.Rpt1CCRounding:int = obj["Rpt1CCRounding"]
      self.Rpt1TotalNet:int = obj["Rpt1TotalNet"]
      self.Rpt2CCRounding:int = obj["Rpt2CCRounding"]
      self.Rpt2TotalNet:int = obj["Rpt2TotalNet"]
      self.Rpt3CCRounding:int = obj["Rpt3CCRounding"]
      self.Rpt3TotalNet:int = obj["Rpt3TotalNet"]
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  Element 1 of SalesRepList  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  Element 2 of SalesRepList  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  Element 3 of SalesRepList  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  Element 4 of SalesRepList  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  Element 5 of SalesRepList  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      self.SalesRepName2:str = obj["SalesRepName2"]
      self.SalesRepName3:str = obj["SalesRepName3"]
      self.SalesRepName4:str = obj["SalesRepName4"]
      self.SalesRepName5:str = obj["SalesRepName5"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShipToCustId:str = obj["ShipToCustId"]
      """  Customer Id of the third-party Ship To  """  
      self.ShowApplyOrderDiscountsControl:bool = obj["ShowApplyOrderDiscountsControl"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      self.SoldToContactEMailAddress:str = obj["SoldToContactEMailAddress"]
      self.SoldToContactFaxNum:str = obj["SoldToContactFaxNum"]
      self.SoldToContactName:str = obj["SoldToContactName"]
      self.SoldToContactPhoneNum:str = obj["SoldToContactPhoneNum"]
      self.TermsType:str = obj["TermsType"]
      """  This field defines the type of the term  """  
      self.TotalNet:int = obj["TotalNet"]
      self.TotalOrder:int = obj["TotalOrder"]
      self.TranDocTypeDescr:str = obj["TranDocTypeDescr"]
      self.TrueDiscountPercent:int = obj["TrueDiscountPercent"]
      """  the true discount percent from the order total  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  Taiwan GUI Legal Number Generation Type  """  
      self.UpdateDtlAndRelRecords:bool = obj["UpdateDtlAndRelRecords"]
      self.InvoicesExist:bool = obj["InvoicesExist"]
      """  Indicates if one or more invoices exist for this order  """  
      self.BTAddressFormatted:str = obj["BTAddressFormatted"]
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  The formatted ship to address  """  
      self.SoldToAddressFormatted:str = obj["SoldToAddressFormatted"]
      """  The formatted Sold To Address  """  
      self.TranDate:str = obj["TranDate"]
      self.TranNum:int = obj["TranNum"]
      self.TranTime:int = obj["TranTime"]
      self.OrderRelNeedByDateNotNull:bool = obj["OrderRelNeedByDateNotNull"]
      """  Indicates there is an OrderRel record that has a non-null NeedByDate  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the order is inactive.  """  
      self.EnableAllocationQueueActions:bool = obj["EnableAllocationQueueActions"]
      """  Enable Fulfillment Queue Actions  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      self.BTCustNumName:str = obj["BTCustNumName"]
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.InvCurrCurrDesc:str = obj["InvCurrCurrDesc"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.PlantName:str = obj["PlantName"]
      self.PSCurrCurrDesc:str = obj["PSCurrCurrDesc"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeInactive:bool = obj["ShipViaCodeInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Project_c:str = obj["Project_c"]
      self.OriginalOrderNo_c:int = obj["OriginalOrderNo_c"]
      self.MASFlag_c:bool = obj["MASFlag_c"]
      self.Estimate_c:bool = obj["Estimate_c"]
      self.ShipOrderComplete_c:bool = obj["ShipOrderComplete_c"]
      self.ProjectID_c:str = obj["ProjectID_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID__c:str = obj["SalesCatID__c"]
      self.TaxCatID_c:str = obj["TaxCatID_c"]
      self.MfgOrder_c:bool = obj["MfgOrder_c"]
      pass

class Erp_Tablesets_SalesOrdHedDtlTableset:
   def __init__(self, obj):
      self.OrderHed:list[Erp_Tablesets_OrderHedRow] = obj["OrderHed"]
      self.OrderDtl:list[Erp_Tablesets_OrderDtlRow] = obj["OrderDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSalesOrdHedDtlTableset:
   def __init__(self, obj):
      self.OrderHed:list[Erp_Tablesets_OrderHedRow] = obj["OrderHed"]
      self.OrderDtl:list[Erp_Tablesets_OrderDtlRow] = obj["OrderDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   orderNum
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OrderHedListTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["ds"]
      self.orderNum:int = obj["orderNum"]
      pass

class GetNewOrderDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOrderHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["ds"]
      pass

class GetNewOrderHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseOrderHed
   whereClauseOrderDtl
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderHed:str = obj["whereClauseOrderHed"]
      """  Whereclause for OrderHed table.  """  
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  Whereclause for OrderDtl table.  """  
      self.contactName:str = obj["contactName"]
      """  The contact name to return orders for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseOrderHed
   whereClauseOrderDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderHed:str = obj["whereClauseOrderHed"]
      """  Whereclause for OrderHed table.  """  
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      """  Whereclause for OrderDtl table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseOrderHed
   whereClauseOrderDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderHed:str = obj["whereClauseOrderHed"]
      self.whereClauseOrderDtl:str = obj["whereClauseOrderDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtSalesOrdHedDtlTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesOrdHedDtlTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesOrdHedDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

