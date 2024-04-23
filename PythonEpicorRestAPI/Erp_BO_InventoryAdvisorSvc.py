import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InventoryAdvisorSvc
# Description: InventoryAdvisorSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_InventoryAdvisors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InventoryAdvisors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InventoryAdvisors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartQtyAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors",headers=creds) as resp:
           return await resp.json()

async def post_InventoryAdvisors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InventoryAdvisors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartQtyAttrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartQtyAttrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InventoryAdvisors_Company_PartNum_WarehouseCode_DimCode_AttributeSetID(Company, PartNum, WarehouseCode, DimCode, AttributeSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InventoryAdvisor item
   Description: Calls GetByID to retrieve the InventoryAdvisor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InventoryAdvisor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartQtyAttrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors(" + Company + "," + PartNum + "," + WarehouseCode + "," + DimCode + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InventoryAdvisors_Company_PartNum_WarehouseCode_DimCode_AttributeSetID(Company, PartNum, WarehouseCode, DimCode, AttributeSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InventoryAdvisor for the service
   Description: Calls UpdateExt to update InventoryAdvisor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InventoryAdvisor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartQtyAttrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors(" + Company + "," + PartNum + "," + WarehouseCode + "," + DimCode + "," + AttributeSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InventoryAdvisors_Company_PartNum_WarehouseCode_DimCode_AttributeSetID(Company, PartNum, WarehouseCode, DimCode, AttributeSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InventoryAdvisor item
   Description: Call UpdateExt to delete InventoryAdvisor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InventoryAdvisor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors(" + Company + "," + PartNum + "," + WarehouseCode + "," + DimCode + "," + AttributeSetID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartQtyAttrListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartQtyAttr, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartQtyAttr=" + whereClausePartQtyAttr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, warehouseCode, dimCode, attributeSetID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "warehouseCode=" + warehouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "dimCode=" + dimCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attributeSetID=" + attributeSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddToQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddToQuote
   Description: Updates existing Quote with search results from the InventoryAdvisor BO
   OperationID: AddToQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddToQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddToQuoteInventoryDynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddToQuoteInventoryDynAttrValues
   Description: Updates existing Quote with search results from the InventoryAdvisor BO
   OperationID: AddToQuoteInventoryDynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddToQuoteInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToQuoteInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateQuote
   Description: Creates a new Quote and adds lines based on the search results from the InventoryAdvisor BO
   OperationID: CreateQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateQuoteInventoryDynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateQuoteInventoryDynAttrValues
   OperationID: CreateQuoteInventoryDynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuoteInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddToSalesOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddToSalesOrder
   Description: Updates existing Sales Order with search results from the InventoryAdvisor BO
   OperationID: AddToSalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddToSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddToSalesOrderInventoryDynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddToSalesOrderInventoryDynAttrValues
   OperationID: AddToSalesOrderInventoryDynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddToSalesOrderInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToSalesOrderInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSalesOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSalesOrder
   Description: Creates a new Sales Order and adds lines based on the search results from the InventoryAdvisor BO
   OperationID: CreateSalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSalesOrderInventoryDynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSalesOrderInventoryDynAttrValues
   Description: Creates a new Sales Order and adds lines based on the search results from the InventoryAdvisor BO
   OperationID: CreateSalesOrderInventoryDynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSalesOrderInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSalesOrderInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Number Of Pieces changes to calculate a new Action Quantity
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSelectedForActionQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSelectedForActionQty
   Description: Call this method when the Action Quantity changes to calculate a new Number Of Pieces
   OperationID: OnChangingSelectedForActionQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSelectedForActionQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSelectedForActionQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsAdvanced(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsAdvanced
   Description: Get rows using additional search criteria and incorporate with Enterprise Search results
   OperationID: GetRowsAdvanced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsAdvanced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsAdvanced_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsInventoryAdvisor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsInventoryAdvisor
   Description: Get rows using additional search criteria and incorporate with Enterprise Search results
   OperationID: GetRowsInventoryAdvisor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsInventoryAdvisor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsInventoryAdvisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsUsingSearchParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsUsingSearchParams
   Description: Get rows using static Part Attributes and Dynamic Attributes and incorporate with Enterprise Search results
   OperationID: GetRowsUsingSearchParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsUsingSearchParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUsingSearchParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableStructure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableStructure
   Description: Builds dynamic DataTable structure based on class selected
   OperationID: GetTableStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByInventoryAdvisorSysRowIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByInventoryAdvisorSysRowIDs
   Description: Return result in dynamic DataTable based on InventoryAdvisor dataset
   OperationID: GetByInventoryAdvisorSysRowIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByInventoryAdvisorSysRowIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByInventoryAdvisorSysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshInventoryAdvisor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshInventoryAdvisor
   Description: Refresh Inventory Advisor using a list PartQtyAttr and Part SysRowIDs
   OperationID: RefreshInventoryAdvisor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshInventoryAdvisor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshInventoryAdvisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshInventoryAdvisorFromDataset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshInventoryAdvisorFromDataset
   Description: Refresh Inventory Advisor using rows in the dataset
   OperationID: RefreshInventoryAdvisorFromDataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshInventoryAdvisorFromDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshInventoryAdvisorFromDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartQtyAttrListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartQtyAttrRow] = obj["value"]
      pass

class Erp_Tablesets_PartQtyAttrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.DimCode:str = obj["DimCode"]
      """  UOM  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DemandQty:int = obj["DemandQty"]
      """  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  """  
      self.PickingQty:int = obj["PickingQty"]
      """  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  """  
      self.PickedQty:int = obj["PickedQty"]
      """  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.BuyToOrderQty:int = obj["BuyToOrderQty"]
      """  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  """  
      self.SalesDemandQty:int = obj["SalesDemandQty"]
      """  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesAllocatedQty:int = obj["SalesAllocatedQty"]
      """  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobDemandQty:int = obj["JobDemandQty"]
      """  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.JobAllocatedQty:int = obj["JobAllocatedQty"]
      """  New in 9.00.  Summary of stock allocated for jobs.  """  
      self.JobPickingQty:int = obj["JobPickingQty"]
      """  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  """  
      self.JobPickedQty:int = obj["JobPickedQty"]
      """  Stock Quantity picked for jobs.  """  
      self.UnfirmJobDemandQty:int = obj["UnfirmJobDemandQty"]
      """  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  """  
      self.TFOrdDemandQty:int = obj["TFOrdDemandQty"]
      """  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.TFOrdReservedQty:int = obj["TFOrdReservedQty"]
      """  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  """  
      self.TFOrdAllocatedQty:int = obj["TFOrdAllocatedQty"]
      """  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  """  
      self.TFOrdPickingQty:int = obj["TFOrdPickingQty"]
      """  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  """  
      self.TFOrdPickedQty:int = obj["TFOrdPickedQty"]
      """  Stock Quantity picked for transfer orders.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SearchParamAttrClassID:str = obj["SearchParamAttrClassID"]
      """  Attribute Class that was selected in the Search.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartQtyAttrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.DimCode:str = obj["DimCode"]
      """  UOM  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DemandQty:int = obj["DemandQty"]
      """  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  """  
      self.PickingQty:int = obj["PickingQty"]
      """  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  """  
      self.PickedQty:int = obj["PickedQty"]
      """  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.BuyToOrderQty:int = obj["BuyToOrderQty"]
      """  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  """  
      self.SalesDemandQty:int = obj["SalesDemandQty"]
      """  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesAllocatedQty:int = obj["SalesAllocatedQty"]
      """  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobDemandQty:int = obj["JobDemandQty"]
      """  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.JobAllocatedQty:int = obj["JobAllocatedQty"]
      """  New in 9.00.  Summary of stock allocated for jobs.  """  
      self.JobPickingQty:int = obj["JobPickingQty"]
      """  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  """  
      self.JobPickedQty:int = obj["JobPickedQty"]
      """  Stock Quantity picked for jobs.  """  
      self.UnfirmJobDemandQty:int = obj["UnfirmJobDemandQty"]
      """  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  """  
      self.TFOrdDemandQty:int = obj["TFOrdDemandQty"]
      """  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.TFOrdReservedQty:int = obj["TFOrdReservedQty"]
      """  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  """  
      self.TFOrdAllocatedQty:int = obj["TFOrdAllocatedQty"]
      """  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  """  
      self.TFOrdPickingQty:int = obj["TFOrdPickingQty"]
      """  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  """  
      self.TFOrdPickedQty:int = obj["TFOrdPickedQty"]
      """  Stock Quantity picked for transfer orders.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.SelectedForActionQty:int = obj["SelectedForActionQty"]
      self.PlantVendorID:str = obj["PlantVendorID"]
      self.PlantVendorName:str = obj["PlantVendorName"]
      self.PlantLeadTime:int = obj["PlantLeadTime"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts as relates to On Hand Quantity.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      self.PlantName:str = obj["PlantName"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttrClassIDDescription:str = obj["AttrClassIDDescription"]
      self.SearchParamAttrClassID:str = obj["SearchParamAttrClassID"]
      """  Attribute Class that was selected in the Search.  """  
      self.AvailableNbrPcs:int = obj["AvailableNbrPcs"]
      """  Number of pieces for inventory attribute tracked parts as relates to Available Quantity.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttributeSetIDRevisionNum:str = obj["AttributeSetIDRevisionNum"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.PartNumIsSafetyItem:bool = obj["PartNumIsSafetyItem"]
      self.PartNumUnitPrice:int = obj["PartNumUnitPrice"]
      self.PartNumIsGiftCard:bool = obj["PartNumIsGiftCard"]
      self.PartNumDiameterInside:int = obj["PartNumDiameterInside"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumDurometer:str = obj["PartNumDurometer"]
      self.PartNumSysRowID:str = obj["PartNumSysRowID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumProdCode:str = obj["PartNumProdCode"]
      self.PartNumCommercialColor:str = obj["PartNumCommercialColor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumDiameterUM:str = obj["PartNumDiameterUM"]
      self.PartNumPartHeight:int = obj["PartNumPartHeight"]
      self.PartNumCondition:str = obj["PartNumCondition"]
      self.PartNumDualUOMClassID:str = obj["PartNumDualUOMClassID"]
      self.PartNumCommercialBrand:str = obj["PartNumCommercialBrand"]
      self.PartNumCommercialSubBrand:str = obj["PartNumCommercialSubBrand"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumCommercialCategory:str = obj["PartNumCommercialCategory"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumClassID:str = obj["PartNumClassID"]
      self.PartNumPartLength:int = obj["PartNumPartLength"]
      self.PartNumIsRestricted:bool = obj["PartNumIsRestricted"]
      self.PartNumCommentText:str = obj["PartNumCommentText"]
      self.PartNumCommercialSize1:str = obj["PartNumCommercialSize1"]
      self.PartNumEngineeringAlert:str = obj["PartNumEngineeringAlert"]
      self.PartNumPartWidth:int = obj["PartNumPartWidth"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumCommercialSize2:str = obj["PartNumCommercialSize2"]
      self.PartNumPartLengthWidthHeightUM:str = obj["PartNumPartLengthWidthHeightUM"]
      self.PartNumCommercialSubCategory:str = obj["PartNumCommercialSubCategory"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumDiameterOutside:int = obj["PartNumDiameterOutside"]
      self.PartNumCommercialStyle:str = obj["PartNumCommercialStyle"]
      self.PartNumSpecification:str = obj["PartNumSpecification"]
      self.PartNumThicknessUM:str = obj["PartNumThicknessUM"]
      self.PartNumIsCompliant:bool = obj["PartNumIsCompliant"]
      self.PartNumThickness:int = obj["PartNumThickness"]
      self.PartNumThicknessMax:int = obj["PartNumThicknessMax"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WarehouseCodePlant:str = obj["WarehouseCodePlant"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddToQuoteInventoryDynAttrValues_input:
   """ Required : 
   attrClassID
   quoteNum
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.quoteNum:int = obj["quoteNum"]
      self.ds      #schema had no properties on an object.
      pass

class AddToQuoteInventoryDynAttrValues_output:
   def __init__(self, obj):
      pass

class AddToQuote_input:
   """ Required : 
   quoteNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class AddToQuote_output:
   def __init__(self, obj):
      pass

class AddToSalesOrderInventoryDynAttrValues_input:
   """ Required : 
   attrClassID
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.orderNum:int = obj["orderNum"]
      self.ds      #schema had no properties on an object.
      pass

class AddToSalesOrderInventoryDynAttrValues_output:
   def __init__(self, obj):
      pass

class AddToSalesOrder_input:
   """ Required : 
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class AddToSalesOrder_output:
   def __init__(self, obj):
      pass

class CreateQuoteInventoryDynAttrValues_input:
   """ Required : 
   attrClassID
   custID
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.custID:str = obj["custID"]
      self.ds      #schema had no properties on an object.
      pass

class CreateQuoteInventoryDynAttrValues_output:
   def __init__(self, obj):
      pass

class CreateQuote_input:
   """ Required : 
   custID
   ds
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class CreateQuote_output:
   def __init__(self, obj):
      pass

class CreateSalesOrderInventoryDynAttrValues_input:
   """ Required : 
   attrClassID
   custID
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.custID:str = obj["custID"]
      self.ds      #schema had no properties on an object.
      pass

class CreateSalesOrderInventoryDynAttrValues_output:
   def __init__(self, obj):
      pass

class CreateSalesOrder_input:
   """ Required : 
   custID
   ds
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class CreateSalesOrder_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DynFieldAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Required:bool = obj["Required"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.BizType:str = obj["BizType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UomColumn:str = obj["UomColumn"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      self.Seq:int = obj["Seq"]
      self.IsHidden:bool = obj["IsHidden"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldHelpRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.External:bool = obj["External"]
      self.InitialValue:str = obj["InitialValue"]
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      """  The actual generic table name used by the BL  """  
      self.UniqueTableID:str = obj["UniqueTableID"]
      """  Unique identifier for the virtual schema  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InventoryAdvisorListTableset:
   def __init__(self, obj):
      self.PartQtyAttrList:list[Erp_Tablesets_PartQtyAttrListRow] = obj["PartQtyAttrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InventoryAdvisorTableset:
   def __init__(self, obj):
      self.PartQtyAttr:list[Erp_Tablesets_PartQtyAttrRow] = obj["PartQtyAttr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartQtyAttrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.DimCode:str = obj["DimCode"]
      """  UOM  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DemandQty:int = obj["DemandQty"]
      """  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  """  
      self.PickingQty:int = obj["PickingQty"]
      """  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  """  
      self.PickedQty:int = obj["PickedQty"]
      """  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.BuyToOrderQty:int = obj["BuyToOrderQty"]
      """  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  """  
      self.SalesDemandQty:int = obj["SalesDemandQty"]
      """  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesAllocatedQty:int = obj["SalesAllocatedQty"]
      """  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobDemandQty:int = obj["JobDemandQty"]
      """  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.JobAllocatedQty:int = obj["JobAllocatedQty"]
      """  New in 9.00.  Summary of stock allocated for jobs.  """  
      self.JobPickingQty:int = obj["JobPickingQty"]
      """  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  """  
      self.JobPickedQty:int = obj["JobPickedQty"]
      """  Stock Quantity picked for jobs.  """  
      self.UnfirmJobDemandQty:int = obj["UnfirmJobDemandQty"]
      """  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  """  
      self.TFOrdDemandQty:int = obj["TFOrdDemandQty"]
      """  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.TFOrdReservedQty:int = obj["TFOrdReservedQty"]
      """  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  """  
      self.TFOrdAllocatedQty:int = obj["TFOrdAllocatedQty"]
      """  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  """  
      self.TFOrdPickingQty:int = obj["TFOrdPickingQty"]
      """  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  """  
      self.TFOrdPickedQty:int = obj["TFOrdPickedQty"]
      """  Stock Quantity picked for transfer orders.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SearchParamAttrClassID:str = obj["SearchParamAttrClassID"]
      """  Attribute Class that was selected in the Search.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartQtyAttrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.DimCode:str = obj["DimCode"]
      """  UOM  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DemandQty:int = obj["DemandQty"]
      """  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  """  
      self.PickingQty:int = obj["PickingQty"]
      """  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  """  
      self.PickedQty:int = obj["PickedQty"]
      """  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.BuyToOrderQty:int = obj["BuyToOrderQty"]
      """  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  """  
      self.SalesDemandQty:int = obj["SalesDemandQty"]
      """  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesAllocatedQty:int = obj["SalesAllocatedQty"]
      """  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobDemandQty:int = obj["JobDemandQty"]
      """  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.JobAllocatedQty:int = obj["JobAllocatedQty"]
      """  New in 9.00.  Summary of stock allocated for jobs.  """  
      self.JobPickingQty:int = obj["JobPickingQty"]
      """  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  """  
      self.JobPickedQty:int = obj["JobPickedQty"]
      """  Stock Quantity picked for jobs.  """  
      self.UnfirmJobDemandQty:int = obj["UnfirmJobDemandQty"]
      """  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  """  
      self.TFOrdDemandQty:int = obj["TFOrdDemandQty"]
      """  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  """  
      self.TFOrdReservedQty:int = obj["TFOrdReservedQty"]
      """  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  """  
      self.TFOrdAllocatedQty:int = obj["TFOrdAllocatedQty"]
      """  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  """  
      self.TFOrdPickingQty:int = obj["TFOrdPickingQty"]
      """  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  """  
      self.TFOrdPickedQty:int = obj["TFOrdPickedQty"]
      """  Stock Quantity picked for transfer orders.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.SelectedForActionQty:int = obj["SelectedForActionQty"]
      self.PlantVendorID:str = obj["PlantVendorID"]
      self.PlantVendorName:str = obj["PlantVendorName"]
      self.PlantLeadTime:int = obj["PlantLeadTime"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts as relates to On Hand Quantity.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      self.PlantName:str = obj["PlantName"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttrClassIDDescription:str = obj["AttrClassIDDescription"]
      self.SearchParamAttrClassID:str = obj["SearchParamAttrClassID"]
      """  Attribute Class that was selected in the Search.  """  
      self.AvailableNbrPcs:int = obj["AvailableNbrPcs"]
      """  Number of pieces for inventory attribute tracked parts as relates to Available Quantity.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttributeSetIDRevisionNum:str = obj["AttributeSetIDRevisionNum"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.PartNumIsSafetyItem:bool = obj["PartNumIsSafetyItem"]
      self.PartNumUnitPrice:int = obj["PartNumUnitPrice"]
      self.PartNumIsGiftCard:bool = obj["PartNumIsGiftCard"]
      self.PartNumDiameterInside:int = obj["PartNumDiameterInside"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumDurometer:str = obj["PartNumDurometer"]
      self.PartNumSysRowID:str = obj["PartNumSysRowID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumProdCode:str = obj["PartNumProdCode"]
      self.PartNumCommercialColor:str = obj["PartNumCommercialColor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumDiameterUM:str = obj["PartNumDiameterUM"]
      self.PartNumPartHeight:int = obj["PartNumPartHeight"]
      self.PartNumCondition:str = obj["PartNumCondition"]
      self.PartNumDualUOMClassID:str = obj["PartNumDualUOMClassID"]
      self.PartNumCommercialBrand:str = obj["PartNumCommercialBrand"]
      self.PartNumCommercialSubBrand:str = obj["PartNumCommercialSubBrand"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumCommercialCategory:str = obj["PartNumCommercialCategory"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumClassID:str = obj["PartNumClassID"]
      self.PartNumPartLength:int = obj["PartNumPartLength"]
      self.PartNumIsRestricted:bool = obj["PartNumIsRestricted"]
      self.PartNumCommentText:str = obj["PartNumCommentText"]
      self.PartNumCommercialSize1:str = obj["PartNumCommercialSize1"]
      self.PartNumEngineeringAlert:str = obj["PartNumEngineeringAlert"]
      self.PartNumPartWidth:int = obj["PartNumPartWidth"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumCommercialSize2:str = obj["PartNumCommercialSize2"]
      self.PartNumPartLengthWidthHeightUM:str = obj["PartNumPartLengthWidthHeightUM"]
      self.PartNumCommercialSubCategory:str = obj["PartNumCommercialSubCategory"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumDiameterOutside:int = obj["PartNumDiameterOutside"]
      self.PartNumCommercialStyle:str = obj["PartNumCommercialStyle"]
      self.PartNumSpecification:str = obj["PartNumSpecification"]
      self.PartNumThicknessUM:str = obj["PartNumThicknessUM"]
      self.PartNumIsCompliant:bool = obj["PartNumIsCompliant"]
      self.PartNumThickness:int = obj["PartNumThickness"]
      self.PartNumThicknessMax:int = obj["PartNumThicknessMax"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WarehouseCodePlant:str = obj["WarehouseCodePlant"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtInventoryAdvisorTableset:
   def __init__(self, obj):
      self.PartQtyAttr:list[Erp_Tablesets_PartQtyAttrRow] = obj["PartQtyAttr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   warehouseCode
   dimCode
   attributeSetID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.dimCode:str = obj["dimCode"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

class GetByInventoryAdvisorSysRowIDs_input:
   """ Required : 
   attrClassID
   ds
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GetByInventoryAdvisorSysRowIDs_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsAdvanced_input:
   """ Required : 
   startsWith
   partNum
   classID
   prodCode
   attrClassID
   attributeSetIDList
   searchText
   inStockOnly
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.startsWith:str = obj["startsWith"]
      self.partNum:str = obj["partNum"]
      self.classID:str = obj["classID"]
      self.prodCode:str = obj["prodCode"]
      self.attrClassID:str = obj["attrClassID"]
      self.attributeSetIDList:int = obj["attributeSetIDList"]
      self.searchText:str = obj["searchText"]
      self.inStockOnly:bool = obj["inStockOnly"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsAdvanced_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsInventoryAdvisor_input:
   """ Required : 
   startsWith
   partNum
   classID
   prodCode
   attrClassID
   attributeSetIDList
   searchText
   inStockOnly
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.startsWith:str = obj["startsWith"]
      self.partNum:str = obj["partNum"]
      self.classID:str = obj["classID"]
      self.prodCode:str = obj["prodCode"]
      self.attrClassID:str = obj["attrClassID"]
      self.attributeSetIDList:str = obj["attributeSetIDList"]
      self.searchText:str = obj["searchText"]
      self.inStockOnly:bool = obj["inStockOnly"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsInventoryAdvisor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsUsingSearchParams_input:
   """ Required : 
   partNum
   classID
   prodCode
   attrClassID
   partAttrListString
   dynAttrListString
   startsWith
   enterpriseSearchText
   inStockOnly
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.classID:str = obj["classID"]
      self.prodCode:str = obj["prodCode"]
      self.attrClassID:str = obj["attrClassID"]
      self.partAttrListString:str = obj["partAttrListString"]
      self.dynAttrListString:str = obj["dynAttrListString"]
      self.startsWith:str = obj["startsWith"]
      self.enterpriseSearchText:str = obj["enterpriseSearchText"]
      self.inStockOnly:bool = obj["inStockOnly"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsUsingSearchParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartQtyAttr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartQtyAttr:str = obj["whereClausePartQtyAttr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTableStructure_input:
   """ Required : 
   attrClassID
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GetTableStructure_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      self.displayAttrClassID:str = obj["parameters"]
      self.displayAttrClassIDDescription:str = obj["parameters"]
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

class OnChangingNumberOfPieces_input:
   """ Required : 
   attrClassID
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds      #schema had no properties on an object.
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds: UNKNOW TYPE(error 2338) = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSelectedForActionQty_input:
   """ Required : 
   attrClassID
   selectedForActionQty
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.selectedForActionQty:int = obj["selectedForActionQty"]
      self.ds      #schema had no properties on an object.
      pass

class OnChangingSelectedForActionQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds: UNKNOW TYPE(error 2338) = obj["ds"]
      pass

      """  output parameters  """  

class RefreshInventoryAdvisorFromDataset_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class RefreshInventoryAdvisorFromDataset_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

class RefreshInventoryAdvisor_input:
   """ Required : 
   partQtyAttrSysRowIDList
   partSysRowIDList
   ds
   """  
   def __init__(self, obj):
      self.partQtyAttrSysRowIDList:str = obj["partQtyAttrSysRowIDList"]
      """  The list of rows with an associated PartQtyAttr record  """  
      self.partSysRowIDList:str = obj["partSysRowIDList"]
      """  The list of rows without an associated PartQtyAttr record  """  
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class RefreshInventoryAdvisor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtInventoryAdvisorTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtInventoryAdvisorTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryAdvisorTableset] = obj["ds"]
      pass

      """  output parameters  """  

