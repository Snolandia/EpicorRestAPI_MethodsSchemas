import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PickedOrdersSvc
// Description: Picked Orders contains the quantities that have been picked for shipment of sales order releases.
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PickedOrders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PickedOrders
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PickedOrdersRow
   */  
export function get_PickedOrders(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PickedOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PickedOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PickedOrder item
   Description: Calls GetByID to retrieve the PickedOrder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PickedOrder
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
   */  
export function get_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID(Company:string, Plant:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, LotNum:string, PCID:string, AttributeSetID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PickedOrdersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PickedOrdersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PickedOrder for the service
   Description: Calls UpdateExt to update PickedOrder. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PickedOrder
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PickedOrdersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID(Company:string, Plant:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, LotNum:string, PCID:string, AttributeSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PickedOrder item
   Description: Call UpdateExt to delete PickedOrder item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PickedOrder
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID(Company:string, Plant:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, LotNum:string, PCID:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MtlQueues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MtlQueues1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   */  
export function get_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID_MtlQueues(Company:string, Plant:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, LotNum:string, PCID:string, AttributeSetID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")/MtlQueues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MtlQueue item
   Description: Calls GetByID to retrieve the MtlQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MtlQueue1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   */  
export function get_PickedOrders_Company_Plant_OrderNum_OrderLine_OrderRelNum_WarehouseCode_BinNum_SupplyJobNum_LotNum_PCID_AttributeSetID_MtlQueues_Company_MtlQueueSeq(Company:string, Plant:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, LotNum:string, PCID:string, AttributeSetID:string, MtlQueueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MtlQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/PickedOrders(" + Company + "," + Plant + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + LotNum + "," + PCID + "," + AttributeSetID + ")/MtlQueues(" + Company + "," + MtlQueueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MtlQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MtlQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MtlQueues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   */  
export function get_MtlQueues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MtlQueues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MtlQueues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MtlQueue item
   Description: Calls GetByID to retrieve the MtlQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MtlQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   */  
export function get_MtlQueues_Company_MtlQueueSeq(Company:string, MtlQueueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MtlQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues(" + Company + "," + MtlQueueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MtlQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MtlQueue for the service
   Description: Calls UpdateExt to update MtlQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MtlQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MtlQueues_Company_MtlQueueSeq(Company:string, MtlQueueSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues(" + Company + "," + MtlQueueSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete MtlQueue item
   Description: Call UpdateExt to delete MtlQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MtlQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MtlQueueSeq Desc: MtlQueueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MtlQueues_Company_MtlQueueSeq(Company:string, MtlQueueSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/MtlQueues(" + Company + "," + MtlQueueSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PickedOrdersListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
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
   */  
export function get_GetRows(whereClausePickedOrders:string, whereClauseMtlQueue:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePickedOrders!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePickedOrders=" + whereClausePickedOrders
   }
   if(typeof whereClauseMtlQueue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMtlQueue=" + whereClauseMtlQueue
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
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
   */  
export function get_GetByID(plant:string, orderNum:string, orderLine:string, orderRelNum:string, warehouseCode:string, binNum:string, supplyJobNum:string, lotNum:string, pcID:string, attributeSetID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof orderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderNum=" + orderNum
   }
   if(typeof orderLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderLine=" + orderLine
   }
   if(typeof orderRelNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderRelNum=" + orderRelNum
   }
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }
   if(typeof binNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "binNum=" + binNum
   }
   if(typeof supplyJobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "supplyJobNum=" + supplyJobNum
   }
   if(typeof lotNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lotNum=" + lotNum
   }
   if(typeof pcID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcID=" + pcID
   }
   if(typeof attributeSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attributeSetID=" + attributeSetID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrdersWithNoPickingLines
   Description: This method creates the packing slip for the selected picked order
   OperationID: GetOrdersWithNoPickingLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrdersWithNoPickingLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrdersWithNoPickingLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrdersWithNoPickingLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetOrdersWithNoPickingLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPickedOrders
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPickedOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPickedOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPickedOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPickedOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetNewPickedOrders", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMtlQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMtlQueue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetNewMtlQueue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PickedOrdersSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MtlQueueRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PickedOrdersListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PickedOrdersRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PickedOrdersRow[],
}

export interface Erp_Tablesets_MtlQueueRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   "SysTime":number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   "MtlQueueSeq":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Part Number of item in the container.  */  
   "PartNum":string,
      /**  Quantity  */  
   "Quantity":number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   "TranType":string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   "ReferencePrefix":string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   "Reference":string,
      /**  Employee ID that made the request.  */  
   "RequestedByEmpID":string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   "SelectedByEmpID":string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   "JobNum":string,
      /**  Job Assembly Sequence.  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   "JobSeq":number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   "FromWhse":string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   "FromBinNum":string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   "ToWhse":string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   "ToBinNum":string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   "NextAssemblySeq":number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   "NextJobSeq":number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   "NeedByDate":string,
      /**  Time (seconds since midnight) that request is need by.  */  
   "NeedByTime":number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   "VendorNum":number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   "PurPoint":string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   "PackSlip":string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   "PackLine":number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
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
Provides relationship to the JobProd for "make to order" requirements.  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
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
Provides relationship to the JobProd for "make to Job" requirements.  */  
   "TargetJobNum":string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetAssemblySeq":number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetMtlSeq":number,
      /**  Part Revision number  */  
   "RevisionNum":string,
      /**  A description of the Part.  */  
   "PartDescription":string,
      /**  Internal unit of measure.  */  
   "IUM":string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   "Visible":boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   "RMANum":number,
      /**  Line number of the related RMADtl record.  */  
   "RMALine":number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   "RMAReceipt":number,
      /**  RMADisp number of the related RMADisp record.  */  
   "RMADisp":number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   "NCTranID":number,
      /**  Lot Number of the part.  */  
   "LotNum":string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   "Lock":boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   "QueueID":string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   "QueuePickSeq":number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   "ReleaseForPickingSeq":number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   "WhseGroupCode":string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   "TranStatus":string,
      /**  The Wave that was assigned during the allocation process.  */  
   "WaveNum":number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   "Priority":number,
      /**  Transaction Source  */  
   "TranSource":string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   "LastMgrChangeEmpID":string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   "AssignedToEmpID":string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   "TargetTFOrdNum":string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   "TargetTFOrdLine":number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   "PackStation":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  Last Used PCID on the selected line.  */  
   "LastUsedPCID":string,
      /**  The PCID from which the material movement will occur.  */  
   "FromPCID":string,
      /**  The PCID to which the material movement will occur.  */  
   "ToPCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  AttributeValueSeq  */  
   "AttributeValueSeq":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
   "CustID":string,
   "CustTerritoryID":string,
      /**  Indicates whether Transfer Order Selector Flag should be disabled.  */  
   "DisableTO":boolean,
      /**  From Inventory Selector Flag  */  
   "FromInv":boolean,
      /**  From Manufacturing Selector Flag  */  
   "FromJob":boolean,
      /**  From Purchasing Selector Flag  */  
   "FromPO":boolean,
      /**  From Transfer Order Selector Flag  */  
   "FromTO":boolean,
   "FromWhseDesc":string,
      /**  Service Order Number from FSA. Only available in FSA Request Workbench.  */  
   "FSAServiceOrderNumber":number,
      /**  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  */  
   "FSAServiceOrderResourceNum":number,
   "HoldStatus":boolean,
   "LeadTime":number,
   "MaxMfgLotSize":number,
   "MfgLeadTime":number,
   "MinMfgLotSize":number,
   "NeedByTimeDisp":string,
   "NonStock":boolean,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   "OkToProcess":boolean,
   "OnHandQtySite":number,
   "OnHandQtyWhse":number,
   "PlantName":string,
   "PrimWhseCode":string,
   "PrimWhseDesc":string,
   "RequestedByEmpName":string,
      /**  Indicates whether an error occured in processing.  */  
   "RequestError":boolean,
      /**  Message used to return status information after processing.  */  
   "RequestMsg":string,
      /**  Is this material queue row part of the employees warehouse group  */  
   "SameWhseGroupEmp":boolean,
   "SelectedByEmpName":string,
      /**  Used by user to select rows for mass processing  */  
   "SelectedForProcessing":boolean,
   "ShipToCity":string,
   "ShipToCountry":string,
      /**  Customer Ship To Name  */  
   "ShipToName":string,
   "ShipToNum":string,
   "ShipToState":string,
   "ShipToZIP":string,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   "SortByPriority":number,
      /**  Transfer, Sales Kit, Manufactured or Purchased.  */  
   "SourceTypeDesc":string,
   "ToWhseDesc":string,
   "TransferLeadTime":number,
   "TransferPlant":string,
      /**  Readable tran type (used in Replenishment Workbench)  */  
   "TranTypeDesc":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   "WaveRelated":boolean,
      /**  Customer Sales Territory Region Code  */  
   "CustRegionCode":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Display (decimal) number of pieces for inventory tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "JobNumPartDescription":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumAttrClassID":string,
   "POLinePartNum":string,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "RMALineLineDesc":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumAddress3":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumVendorID_":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
   "VendorNumName_":string,
   "VendorNumAddress2":string,
   "WarehouseGroupCodeWhseGroupDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PickedOrdersListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   "OrderRelNum":number,
      /**  Warehouse picked item is located in.  */  
   "WarehouseCode":string,
      /**  Warehouse Bin picked item is located in.  */  
   "BinNum":string,
      /**  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  */  
   "SupplyJobNum":string,
      /**  Lot Number of the parts that were picked.  */  
   "LotNum":string,
      /**  Picked quantity.  Our units.  */  
   "Quantity":number,
      /**  Unit of Measure that Quantity is specified in. Must be a valid UOM.  */  
   "UOM":string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  */  
   "ReqDate":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  */  
   "CustNum":number,
      /**   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  */  
   "ShipToNum":string,
      /**  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  */  
   "ShipViaCode":string,
      /**  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  */  
   "PartNum":string,
      /**  Sales Order Release has been picked.  */  
   "Complete":boolean,
      /**  Populated from OrderHed.BTCustNum  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "IsSelected":boolean,
      /**  The ProjectID  */  
   "ProjectID":string,
      /**  The Invoicing Method of the Project  */  
   "ConInvMeth":string,
      /**  The Hold Product Invoices flag value for the Project  */  
   "HoldPrdInv":boolean,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PickedOrdersRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   "OrderRelNum":number,
      /**  Warehouse picked item is located in.  */  
   "WarehouseCode":string,
      /**  Warehouse Bin picked item is located in.  */  
   "BinNum":string,
      /**  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  */  
   "SupplyJobNum":string,
      /**  Lot Number of the parts that were picked.  */  
   "LotNum":string,
      /**  Picked quantity.  Our units.  */  
   "Quantity":number,
      /**  Unit of Measure that Quantity is specified in. Must be a valid UOM.  */  
   "UOM":string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  */  
   "ReqDate":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  */  
   "CustNum":number,
      /**   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  */  
   "ShipToNum":string,
      /**  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  */  
   "ShipViaCode":string,
      /**  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  */  
   "PartNum":string,
      /**  Sales Order Release has been picked.  */  
   "Complete":boolean,
      /**  Populated from OrderHed.BTCustNum  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  The Hold Product Invoices flag value for the Project  */  
   "HoldPrdInv":boolean,
   "IsSelected":boolean,
   "IsVisible":boolean,
      /**  Contains OTS address  */  
   "OTSAddr":string,
   "ParentPCID":string,
      /**  The ProjectID  */  
   "ProjectID":string,
      /**  The Invoicing Method of the Project  */  
   "ConInvMeth":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param plant
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param warehouseCode
      @param binNum
      @param supplyJobNum
      @param lotNum
      @param pcID
      @param attributeSetID
   */  
export interface DeleteByID_input{
   plant:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   warehouseCode:string,
   binNum:string,
   supplyJobNum:string,
   lotNum:string,
   pcID:string,
   attributeSetID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MtlQueueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time(seconds since midnight) when transaction was created.  */  
   SysTime:number,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   MtlQueueSeq:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Part Number of item in the container.  */  
   PartNum:string,
      /**  Quantity  */  
   Quantity:number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   TranType:string,
      /**   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  */  
   ReferencePrefix:string,
      /**  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  */  
   Reference:string,
      /**  Employee ID that made the request.  */  
   RequestedByEmpID:string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   SelectedByEmpID:string,
      /**  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  */  
   JobNum:string,
      /**  Job Assembly Sequence.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  */  
   JobSeq:number,
      /**  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  */  
   FromWhse:string,
      /**  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  */  
   FromBinNum:string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   ToWhse:string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   ToBinNum:string,
      /**  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  */  
   NextAssemblySeq:number,
      /**  Sequence of the operation that completed quantity of the job operation will be moved to.  */  
   NextJobSeq:number,
      /**  Date the this request is needed by.  Defaults, to current system date.  */  
   NeedByDate:string,
      /**  Time (seconds since midnight) that request is need by.  */  
   NeedByTime:number,
      /**  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  */  
   VendorNum:number,
      /**  Vendor purchase point id of the related purchase receipt (RcvDtl).  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the related RcvDtl.  */  
   PackSlip:string,
      /**  Vendors Packing Slip line  # of the related RcvDtl.  */  
   PackLine:number,
      /**   Order number job is making parts for. (See JobProd.OrderNum).
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
Provides relationship to the JobProd for "make to order" requirements.  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Job that this job is making parts for. (See JobProd.TargetJobNum).
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
Provides relationship to the JobProd for "make to Job" requirements.  */  
   TargetJobNum:string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetAssemblySeq:number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetMtlSeq:number,
      /**  Part Revision number  */  
   RevisionNum:string,
      /**  A description of the Part.  */  
   PartDescription:string,
      /**  Internal unit of measure.  */  
   IUM:string,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  */  
   Visible:boolean,
      /**  Return Material Authorization number of related RMAHead.  */  
   RMANum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMAReceipt number of the related RMARcpt record.  */  
   RMAReceipt:number,
      /**  RMADisp number of the related RMADisp record.  */  
   RMADisp:number,
      /**  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  */  
   NCTranID:number,
      /**  Lot Number of the part.  */  
   LotNum:string,
      /**  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  */  
   Lock:boolean,
      /**  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  */  
   QueueID:string,
      /**  Sequence of this record within an Advanced Shipping Queue.  */  
   QueuePickSeq:number,
      /**  This is an internal sequence number for grouping MtlQueue records.  */  
   ReleaseForPickingSeq:number,
      /**  Warehouse Group that was assigned to this transaction.  */  
   WhseGroupCode:string,
      /**   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  */  
   TranStatus:string,
      /**  The Wave that was assigned during the allocation process.  */  
   WaveNum:number,
      /**  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   Priority:number,
      /**  Transaction Source  */  
   TranSource:string,
      /**  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  */  
   LastMgrChangeEmpID:string,
      /**  Employee ID that was selected by the Warehouse Manager to process record from the queue.  */  
   AssignedToEmpID:string,
      /**  Transfer Order for which Demand is being satisfied.  */  
   TargetTFOrdNum:string,
      /**  Transfer Order Line for which Demand is being satisfied.  */  
   TargetTFOrdLine:number,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Last Used PCID on the selected line.  */  
   LastUsedPCID:string,
      /**  The PCID from which the material movement will occur.  */  
   FromPCID:string,
      /**  The PCID to which the material movement will occur.  */  
   ToPCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  AttributeValueSeq  */  
   AttributeValueSeq:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
   CustID:string,
   CustTerritoryID:string,
      /**  Indicates whether Transfer Order Selector Flag should be disabled.  */  
   DisableTO:boolean,
      /**  From Inventory Selector Flag  */  
   FromInv:boolean,
      /**  From Manufacturing Selector Flag  */  
   FromJob:boolean,
      /**  From Purchasing Selector Flag  */  
   FromPO:boolean,
      /**  From Transfer Order Selector Flag  */  
   FromTO:boolean,
   FromWhseDesc:string,
      /**  Service Order Number from FSA. Only available in FSA Request Workbench.  */  
   FSAServiceOrderNumber:number,
      /**  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  */  
   FSAServiceOrderResourceNum:number,
   HoldStatus:boolean,
   LeadTime:number,
   MaxMfgLotSize:number,
   MfgLeadTime:number,
   MinMfgLotSize:number,
   NeedByTimeDisp:string,
   NonStock:boolean,
      /**  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  */  
   OkToProcess:boolean,
   OnHandQtySite:number,
   OnHandQtyWhse:number,
   PlantName:string,
   PrimWhseCode:string,
   PrimWhseDesc:string,
   RequestedByEmpName:string,
      /**  Indicates whether an error occured in processing.  */  
   RequestError:boolean,
      /**  Message used to return status information after processing.  */  
   RequestMsg:string,
      /**  Is this material queue row part of the employees warehouse group  */  
   SameWhseGroupEmp:boolean,
   SelectedByEmpName:string,
      /**  Used by user to select rows for mass processing  */  
   SelectedForProcessing:boolean,
   ShipToCity:string,
   ShipToCountry:string,
      /**  Customer Ship To Name  */  
   ShipToName:string,
   ShipToNum:string,
   ShipToState:string,
   ShipToZIP:string,
      /**  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  */  
   SortByPriority:number,
      /**  Transfer, Sales Kit, Manufactured or Purchased.  */  
   SourceTypeDesc:string,
   ToWhseDesc:string,
   TransferLeadTime:number,
   TransferPlant:string,
      /**  Readable tran type (used in Replenishment Workbench)  */  
   TranTypeDesc:string,
   VendorNumName:string,
   VendorNumVendorID:string,
      /**  Value is true if this mtlqueue record is related to a wave. False if it is not.  */  
   WaveRelated:boolean,
      /**  Customer Sales Territory Region Code  */  
   CustRegionCode:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Display (decimal) number of pieces for inventory tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
   POLinePartNum:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   RMALineLineDesc:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumVendorID_:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumName_:string,
   VendorNumAddress2:string,
   WarehouseGroupCodeWhseGroupDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PickedOrdersListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Warehouse picked item is located in.  */  
   WarehouseCode:string,
      /**  Warehouse Bin picked item is located in.  */  
   BinNum:string,
      /**  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  */  
   SupplyJobNum:string,
      /**  Lot Number of the parts that were picked.  */  
   LotNum:string,
      /**  Picked quantity.  Our units.  */  
   Quantity:number,
      /**  Unit of Measure that Quantity is specified in. Must be a valid UOM.  */  
   UOM:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  */  
   ReqDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  */  
   CustNum:number,
      /**   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  */  
   ShipToNum:string,
      /**  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  */  
   ShipViaCode:string,
      /**  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  */  
   PartNum:string,
      /**  Sales Order Release has been picked.  */  
   Complete:boolean,
      /**  Populated from OrderHed.BTCustNum  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   IsSelected:boolean,
      /**  The ProjectID  */  
   ProjectID:string,
      /**  The Invoicing Method of the Project  */  
   ConInvMeth:string,
      /**  The Hold Product Invoices flag value for the Project  */  
   HoldPrdInv:boolean,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PickedOrdersListTableset{
   PickedOrdersList:Erp_Tablesets_PickedOrdersListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PickedOrdersRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Warehouse picked item is located in.  */  
   WarehouseCode:string,
      /**  Warehouse Bin picked item is located in.  */  
   BinNum:string,
      /**  Job that is supplying the allocated quantity.  This is blank for a shipment from stock.  */  
   SupplyJobNum:string,
      /**  Lot Number of the parts that were picked.  */  
   LotNum:string,
      /**  Picked quantity.  Our units.  */  
   Quantity:number,
      /**  Unit of Measure that Quantity is specified in. Must be a valid UOM.  */  
   UOM:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Mirror image of OrderRel.ReqDate.  Duplicated here for sorting purposes.  */  
   ReqDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum for sorting purposes.  */  
   CustNum:number,
      /**   ShipTo ID of sales order release.
Duplicated from OrderRel.ShipToNum for sorting purposes.  */  
   ShipToNum:string,
      /**  Ship Via ID duplicated from the OrderRel.ShipViaCode.  Used in the process of generating packing slips from the PickedOrder table.  Each PickedOrders record will become a ShipDtl.   A new Packing slip will be created for each break of Company/Site/Ship Da  */  
   ShipViaCode:string,
      /**  The picked part number.  Normally this would be the same as what's on the related OrderDtl. However, it may be different to allow for substitute parts.  */  
   PartNum:string,
      /**  Sales Order Release has been picked.  */  
   Complete:boolean,
      /**  Populated from OrderHed.BTCustNum  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The Hold Product Invoices flag value for the Project  */  
   HoldPrdInv:boolean,
   IsSelected:boolean,
   IsVisible:boolean,
      /**  Contains OTS address  */  
   OTSAddr:string,
   ParentPCID:string,
      /**  The ProjectID  */  
   ProjectID:string,
      /**  The Invoicing Method of the Project  */  
   ConInvMeth:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
   BinNumDescription:string,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PickedOrdersTableset{
   PickedOrders:Erp_Tablesets_PickedOrdersRow[],
   MtlQueue:Erp_Tablesets_MtlQueueRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPickedOrdersTableset{
   PickedOrders:Erp_Tablesets_PickedOrdersRow[],
   MtlQueue:Erp_Tablesets_MtlQueueRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param warehouseCode
      @param binNum
      @param supplyJobNum
      @param lotNum
      @param pcID
      @param attributeSetID
   */  
export interface GetByID_input{
   plant:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   warehouseCode:string,
   binNum:string,
   supplyJobNum:string,
   lotNum:string,
   pcID:string,
   attributeSetID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PickedOrdersTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PickedOrdersTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PickedOrdersTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PickedOrdersListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMtlQueue_input{
   ds:Erp_Tablesets_PickedOrdersTableset[],
}

export interface GetNewMtlQueue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PickedOrdersTableset[],
}
}

   /** Required : 
      @param ds
      @param plant
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param warehouseCode
      @param binNum
      @param supplyJobNum
      @param lotNum
      @param pcID
   */  
export interface GetNewPickedOrders_input{
   ds:Erp_Tablesets_PickedOrdersTableset[],
   plant:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   warehouseCode:string,
   binNum:string,
   supplyJobNum:string,
   lotNum:string,
   pcID:string,
}

export interface GetNewPickedOrders_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PickedOrdersTableset[],
}
}

   /** Required : 
      @param plant
      @param whseCode
   */  
export interface GetOrdersWithNoPickingLines_input{
      /**  Picked Order Plant  */  
   plant:string,
      /**  Picked Order Warehouse (optional)  */  
   whseCode:string,
}

export interface GetOrdersWithNoPickingLines_output{
   returnObj:Erp_Tablesets_PickedOrdersTableset[],
}

   /** Required : 
      @param whereClausePickedOrders
      @param whereClauseMtlQueue
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePickedOrders:string,
   whereClauseMtlQueue:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PickedOrdersTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPickedOrdersTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPickedOrdersTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PickedOrdersTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PickedOrdersTableset[],
}
}

