import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PickedOrdersSvc
# Description: Picked Orders contains the quantities that have been picked for shipment of sales order releases.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PickedOrders(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PickedOrders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PickedOrders
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PickedOrdersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders",headers=creds) as resp:
           return await resp.json()

async def post_PickedOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PickedOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID(Company, Plant, OrderNum, OrderLine, OrderRelNum, WarehouseCode, BinNum, SupplyJobNum, LotNum, PCID, AttributeSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PickedOrder item
   Description: Calls GetByID to retrieve the PickedOrder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PickedOrder
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID(Company, Plant, OrderNum, OrderLine, OrderRelNum, WarehouseCode, BinNum, SupplyJobNum, LotNum, PCID, AttributeSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PickedOrder for the service
   Description: Calls UpdateExt to update PickedOrder. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PickedOrder
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID(Company, Plant, OrderNum, OrderLine, OrderRelNum, WarehouseCode, BinNum, SupplyJobNum, LotNum, PCID, AttributeSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PickedOrder item
   Description: Call UpdateExt to delete PickedOrder item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PickedOrder
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID_MtlQueues(Company, Plant, OrderNum, OrderLine, OrderRelNum, WarehouseCode, BinNum, SupplyJobNum, LotNum, PCID, AttributeSetID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MtlQueues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MtlQueues1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")/MtlQueues",headers=creds) as resp:
           return await resp.json()

async def get_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID_MtlQueues_Company_MtlQueueSeq(Company, Plant, OrderNum, OrderLine, OrderRelNum, WarehouseCode, BinNum, SupplyJobNum, LotNum, PCID, AttributeSetID, MtlQueueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MtlQueue item
   Description: Calls GetByID to retrieve the MtlQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MtlQueue1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")/MtlQueues(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MtlQueues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MtlQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MtlQueues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues",headers=creds) as resp:
           return await resp.json()

async def post_MtlQueues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MtlQueues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MtlQueues_Company_MtlQueueSeq(Company, MtlQueueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MtlQueue item
   Description: Calls GetByID to retrieve the MtlQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MtlQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MtlQueues_Company_MtlQueueSeq(Company, MtlQueueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MtlQueue for the service
   Description: Calls UpdateExt to update MtlQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MtlQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues(" + Company + "," + MtlQueueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MtlQueues_Company_MtlQueueSeq(Company, MtlQueueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MtlQueue item
   Description: Call UpdateExt to delete MtlQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MtlQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PickedOrdersListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePickedOrders, whereClauseMtlQueue, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePickedOrders=" + whereClausePickedOrders
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMtlQueue=" + whereClauseMtlQueue
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, orderNum, orderLine, orderRelNum, warehouseCode, binNum, supplyJobNum, lotNum, pcID, attributeSetID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderRelNum=" + orderRelNum
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
   params += "binNum=" + binNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "supplyJobNum=" + supplyJobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "lotNum=" + lotNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcID=" + pcID
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetOrdersWithNoPickingLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrdersWithNoPickingLines
   Description: This method creates the packing slip for the selected picked order
   OperationID: GetOrdersWithNoPickingLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrdersWithNoPickingLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrdersWithNoPickingLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPickedOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPickedOrders
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPickedOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPickedOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPickedOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMtlQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMtlQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MtlQueueRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PickedOrdersListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PickedOrdersRow] = obj["value"]
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PickedOrdersListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse picked item is located in.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin picked item is located in.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the parts that were picked.  """  
      self.Quantity:int = obj["Quantity"]
      """  Picked quantity.  Our units.  """  
      self.UOM:str = obj["UOM"]
      """  Unit of Measure that Quantity is specified in. Must be a valid UOM.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  """  
      self.PartNum:str = obj["PartNum"]
      """  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  """  
      self.Complete:bool = obj["Complete"]
      """  Sales Order Release has been picked.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.ProjectID:str = obj["ProjectID"]
      """  The ProjectID  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """  The Invoicing Method of the Project  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """  The Hold Product Invoices flag value for the Project  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
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
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PickedOrdersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse picked item is located in.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin picked item is located in.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the parts that were picked.  """  
      self.Quantity:int = obj["Quantity"]
      """  Picked quantity.  Our units.  """  
      self.UOM:str = obj["UOM"]
      """  Unit of Measure that Quantity is specified in. Must be a valid UOM.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  """  
      self.PartNum:str = obj["PartNum"]
      """  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  """  
      self.Complete:bool = obj["Complete"]
      """  Sales Order Release has been picked.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """  The Hold Product Invoices flag value for the Project  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.IsVisible:bool = obj["IsVisible"]
      self.OTSAddr:str = obj["OTSAddr"]
      """  Contains OTS address  """  
      self.ParentPCID:str = obj["ParentPCID"]
      self.ProjectID:str = obj["ProjectID"]
      """  The ProjectID  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """  The Invoicing Method of the Project  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   orderNum
   orderLine
   orderRelNum
   warehouseCode
   binNum
   supplyJobNum
   lotNum
   pcID
   attributeSetID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      self.lotNum:str = obj["lotNum"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PickedOrdersListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse picked item is located in.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin picked item is located in.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the parts that were picked.  """  
      self.Quantity:int = obj["Quantity"]
      """  Picked quantity.  Our units.  """  
      self.UOM:str = obj["UOM"]
      """  Unit of Measure that Quantity is specified in. Must be a valid UOM.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  """  
      self.PartNum:str = obj["PartNum"]
      """  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  """  
      self.Complete:bool = obj["Complete"]
      """  Sales Order Release has been picked.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.ProjectID:str = obj["ProjectID"]
      """  The ProjectID  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """  The Invoicing Method of the Project  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """  The Hold Product Invoices flag value for the Project  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
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
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PickedOrdersListTableset:
   def __init__(self, obj):
      self.PickedOrdersList:list[Erp_Tablesets_PickedOrdersListRow] = obj["PickedOrdersList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PickedOrdersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse picked item is located in.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin picked item is located in.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the parts that were picked.  """  
      self.Quantity:int = obj["Quantity"]
      """  Picked quantity.  Our units.  """  
      self.UOM:str = obj["UOM"]
      """  Unit of Measure that Quantity is specified in. Must be a valid UOM.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  """  
      self.PartNum:str = obj["PartNum"]
      """  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  """  
      self.Complete:bool = obj["Complete"]
      """  Sales Order Release has been picked.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """  The Hold Product Invoices flag value for the Project  """  
      self.IsSelected:bool = obj["IsSelected"]
      self.IsVisible:bool = obj["IsVisible"]
      self.OTSAddr:str = obj["OTSAddr"]
      """  Contains OTS address  """  
      self.ParentPCID:str = obj["ParentPCID"]
      self.ProjectID:str = obj["ProjectID"]
      """  The ProjectID  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """  The Invoicing Method of the Project  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PickedOrdersTableset:
   def __init__(self, obj):
      self.PickedOrders:list[Erp_Tablesets_PickedOrdersRow] = obj["PickedOrders"]
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPickedOrdersTableset:
   def __init__(self, obj):
      self.PickedOrders:list[Erp_Tablesets_PickedOrdersRow] = obj["PickedOrders"]
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   orderNum
   orderLine
   orderRelNum
   warehouseCode
   binNum
   supplyJobNum
   lotNum
   pcID
   attributeSetID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      self.lotNum:str = obj["lotNum"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PickedOrdersTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PickedOrdersTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PickedOrdersTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PickedOrdersListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMtlQueue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PickedOrdersTableset] = obj["ds"]
      pass

class GetNewMtlQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PickedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPickedOrders_input:
   """ Required : 
   ds
   plant
   orderNum
   orderLine
   orderRelNum
   warehouseCode
   binNum
   supplyJobNum
   lotNum
   pcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PickedOrdersTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      self.lotNum:str = obj["lotNum"]
      self.pcID:str = obj["pcID"]
      pass

class GetNewPickedOrders_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PickedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrdersWithNoPickingLines_input:
   """ Required : 
   plant
   whseCode
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      """  Picked Order Plant  """  
      self.whseCode:str = obj["whseCode"]
      """  Picked Order Warehouse (optional)  """  
      pass

class GetOrdersWithNoPickingLines_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PickedOrdersTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePickedOrders
   whereClauseMtlQueue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePickedOrders:str = obj["whereClausePickedOrders"]
      self.whereClauseMtlQueue:str = obj["whereClauseMtlQueue"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PickedOrdersTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPickedOrdersTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPickedOrdersTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PickedOrdersTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PickedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

