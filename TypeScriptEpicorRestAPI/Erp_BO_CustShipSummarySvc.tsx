import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CustShipSummarySvc
// Description: Customer Shipment Summary Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/$metadata", {
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
   Description: Get CustShipSummaries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustShipSummaries
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustShipSummaryRow
   */  
export function get_CustShipSummaries(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustShipSummaryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustShipSummaryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustShipSummaries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustShipSummaryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustShipSummaryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustShipSummaries(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaries", {
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
   Summary: Calls GetByID to retrieve the CustShipSummary item
   Description: Calls GetByID to retrieve the CustShipSummary item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustShipSummary
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustShipSummaryRow
   */  
export function get_CustShipSummaries_Company_PackNum(Company:string, PackNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustShipSummaryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaries(" + Company + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CustShipSummaryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustShipSummary for the service
   Description: Calls UpdateExt to update CustShipSummary. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustShipSummary
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustShipSummaryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustShipSummaries_Company_PackNum(Company:string, PackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaries(" + Company + "," + PackNum + ")", {
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
   Summary: Call UpdateExt to delete CustShipSummary item
   Description: Call UpdateExt to delete CustShipSummary item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustShipSummary
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustShipSummaries_Company_PackNum(Company:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaries(" + Company + "," + PackNum + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get CustShipSummaryDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustShipSummaryDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustShipSummaryDtlRow
   */  
export function get_CustShipSummaryDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustShipSummaryDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaryDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustShipSummaryDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustShipSummaryDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustShipSummaryDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustShipSummaryDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustShipSummaryDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaryDtls", {
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
   Summary: Calls GetByID to retrieve the CustShipSummaryDtl item
   Description: Calls GetByID to retrieve the CustShipSummaryDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustShipSummaryDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param SalesUM Desc: SalesUM   Required: True   Allow empty value : True
      @param WeightUOM Desc: WeightUOM   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustShipSummaryDtlRow
   */  
export function get_CustShipSummaryDtls_Company_OrderNum_OrderLine_OrderRelNum_SalesUM_WeightUOM(Company:string, OrderNum:string, OrderLine:string, OrderRelNum:string, SalesUM:string, WeightUOM:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustShipSummaryDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaryDtls(" + Company + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + SalesUM + "," + WeightUOM + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CustShipSummaryDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustShipSummaryDtl for the service
   Description: Calls UpdateExt to update CustShipSummaryDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustShipSummaryDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param SalesUM Desc: SalesUM   Required: True   Allow empty value : True
      @param WeightUOM Desc: WeightUOM   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustShipSummaryDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustShipSummaryDtls_Company_OrderNum_OrderLine_OrderRelNum_SalesUM_WeightUOM(Company:string, OrderNum:string, OrderLine:string, OrderRelNum:string, SalesUM:string, WeightUOM:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaryDtls(" + Company + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + SalesUM + "," + WeightUOM + ")", {
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
   Summary: Call UpdateExt to delete CustShipSummaryDtl item
   Description: Call UpdateExt to delete CustShipSummaryDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustShipSummaryDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param SalesUM Desc: SalesUM   Required: True   Allow empty value : True
      @param WeightUOM Desc: WeightUOM   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustShipSummaryDtls_Company_OrderNum_OrderLine_OrderRelNum_SalesUM_WeightUOM(Company:string, OrderNum:string, OrderLine:string, OrderRelNum:string, SalesUM:string, WeightUOM:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/CustShipSummaryDtls(" + Company + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + SalesUM + "," + WeightUOM + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get OrderRelPkgDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderRelPkgDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderRelPkgDetailRow
   */  
export function get_OrderRelPkgDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelPkgDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/OrderRelPkgDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelPkgDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OrderRelPkgDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderRelPkgDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OrderRelPkgDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderRelPkgDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/OrderRelPkgDetails", {
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
   Summary: Calls GetByID to retrieve the OrderRelPkgDetail item
   Description: Calls GetByID to retrieve the OrderRelPkgDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderRelPkgDetail
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OrderRelPkgDetailRow
   */  
export function get_OrderRelPkgDetails_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderRelPkgDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/OrderRelPkgDetails(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_OrderRelPkgDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OrderRelPkgDetail for the service
   Description: Calls UpdateExt to update OrderRelPkgDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OrderRelPkgDetail
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderRelPkgDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OrderRelPkgDetails_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/OrderRelPkgDetails(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete OrderRelPkgDetail item
   Description: Call UpdateExt to delete OrderRelPkgDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OrderRelPkgDetail
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OrderRelPkgDetails_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/OrderRelPkgDetails(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCustShipSummary:string, whereClauseCustShipSummaryDtl:string, whereClauseOrderRelPkgDetail:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCustShipSummary!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustShipSummary=" + whereClauseCustShipSummary
   }
   if(typeof whereClauseCustShipSummaryDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustShipSummaryDtl=" + whereClauseCustShipSummaryDtl
   }
   if(typeof whereClauseOrderRelPkgDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOrderRelPkgDetail=" + whereClauseOrderRelPkgDetail
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(packNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetList" + params, {
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
   Summary: Invoke method BuildShipToList
   Description: If the Order has releases to multiple ShipTo's, this will return the list of available ShipTo's to select from.
   OperationID: BuildShipToList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildShipToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildShipToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildShipToList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/BuildShipToList", {
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
   Summary: Invoke method GetOrderRelPkgDetail
   Description: Get Packaging Detail information for the OrderRel selected
   OperationID: GetOrderRelPkgDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderRelPkgDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderRelPkgDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderRelPkgDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetOrderRelPkgDetail", {
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
   Summary: Invoke method GetNewCustShipSummary
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustShipSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustShipSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustShipSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCustShipSummary(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetNewCustShipSummary", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustShipSummarySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustShipSummaryDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustShipSummaryDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustShipSummaryRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustShipSummaryRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelPkgDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderRelPkgDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipHeadListRow[],
}

export interface Erp_Tablesets_CustShipSummaryDtlRow{
      /**  The part number from the order line for this release.  */  
   "PartNum":string,
      /**  The customer's part number from the first pack line for this release.  */  
   "XPartNum":string,
      /**  The description from the order line for this release.  */  
   "LineDesc":string,
      /**  Sales order number for this order release.  */  
   "OrderNum":number,
      /**  Sales order line for this release.  */  
   "OrderLine":number,
      /**  The number of this release.  */  
   "OrderRelNum":number,
      /**  Ordered quantity for this release.  */  
   "SellingReqQty":number,
      /**  Selling Unit of measure for these shipment lines.  */  
   "SalesUM":string,
      /**  The total quantity packed in this pack for this release.  */  
   "PackSellingShippedQty":number,
      /**  The total quantity packed (in all packs) for this release.  */  
   "TotalSellingShippedQty":number,
      /**  The quantity ordered, minus the total quantity shipped, for this release.  */  
   "SellingRemainQty":number,
      /**  True if any of the shipment lines for this release have been marked as complete.  */  
   "ShipCmpl":boolean,
      /**  The total weight of all the lines on this pack for this release.  */  
   "TotalNetWeight":number,
      /**  The weight unit of measure.  */  
   "WeightUOM":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Selling Unit of measure for this order release.  */  
   "OrderRelSalesUM":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CustShipSummaryRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   "Invoiced":boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  Populated from OrderHed.BTCustNum.  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Package Weight  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   "OTSOrderNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Shipping Address  */  
   "AddrList":string,
      /**  Billing Address  */  
   "BillAddr":string,
      /**  Carton Stage Number.  */  
   "CartonStageNbr":string,
      /**  Comma delimited list of status types for lookup  */  
   "SlipStatus":string,
      /**  Our Supplier Code  */  
   "OurSupplierCode":string,
   "BitFlag":number,
   "CustomerOurSupplierCode":string,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "ShipToName":string,
   "ShipToCustBTName":string,
   "ShipToCustCustID":string,
   "ShipToCustName":string,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Review_c":boolean,
}

export interface Erp_Tablesets_OrderRelPkgDetailRow{
      /**  Checkbox indicating whether the packaging is Expendable  */  
   "ContainerExpendable":boolean,
      /**  Checkbox indicating whether the packaging is Returnable  */  
   "ContainerReturnable":boolean,
      /**  Count of the number of PCIDs in the pack for the selected order/line/rel using that package code  */  
   "Count":number,
      /**  Packaging Code used in at least one of the PCID’s for the Pack/Order/Line/Rel  */  
   "PkgCode":string,
      /**  UOM of the Pack Qty  */  
   "SalesUM":string,
      /**  Quantity packed for the Pack/Order/Line/Rel/Package Code  */  
   "PackQty":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   "Invoiced":boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   "ReadyToInvoice":boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   "Voided":boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External  ID  */  
   "ExternalID":string,
      /**  Iinter Company Received flag  */  
   "ICReceived":boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefPackNum":string,
      /**  Populated from OrderHed.BTCustNum.  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Package Code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Verbal Confirmation required  */  
   "VerbalConf":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Is a Service Saturday delivery acceptable  */  
   "ServSatDelivery":boolean,
      /**  Is a Service Saturday pickup available  */  
   "ServSatPickup":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Auto POD flag  */  
   "ServPOD":boolean,
      /**  AOD  */  
   "ServAOD":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountryNum":number,
      /**  Payer Bill To Third Address line  */  
   "PayBTAddress3":string,
      /**  Payer Bill To Country Number  */  
   "PayBTCountryNum":number,
      /**  Payer Bill To Phone Number  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   "PhantomPack":boolean,
      /**  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  */  
   "ReplicatedFrom":number,
      /**  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  */  
   "ReplicatedStat":string,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   "OTSOrderNum":number,
      /**  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  */  
   "TaxCalculated":boolean,
      /**  Date the taxes were calculated.  Used for informational and audit tracking purposes.  */  
   "TaxCalcDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalTax":number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   "OrderAmt":number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   "DocOrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrderAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrderAmt":number,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalWHTax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalWHTax":number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalSATax":number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalSATax":number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalSATax":number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalTax":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalDiscount":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalDiscount":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  */  
   "PBHoldNoInv":boolean,
      /**  Reconciled quantity for the packing slip  */  
   "ReconcileQty":number,
      /**  Last trading partner demand schedule processed that affected this packing slip  */  
   "ScheduleNumber":string,
      /**  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  */  
   "CounterASN":number,
      /**  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  */  
   "OurBank":string,
      /**  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  */  
   "ERSOrder":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OrderDate":string,
      /**  Comma delimited list of status types for lookup  */  
   "SlipStatus":string,
      /**  Shipping Address  */  
   "AddrList":string,
      /**  Billing Address  */  
   "BillAddr":string,
      /**  Indicates if Customer is on Credit Hold  */  
   "CreditHold":boolean,
      /**  Indicates if Order is on Hold  */  
   "OrderHold":boolean,
      /**  Flag indicating OrderRel's going to more than one shipTo  */  
   "MultipleShippers":boolean,
      /**  Indicates whether to hide/view ExternalDeliveryNote field  */  
   "SendShipment":boolean,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   "BTCustID":string,
      /**  CustName associated with ShipHead.BTCustNum.  */  
   "BTCustomerName":string,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   "CartonContentValue":number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   "LastCartonFlag":boolean,
      /**  Carton Stage Number.  */  
   "CartonStageNbr":string,
   "EnableShipped":boolean,
      /**  Order Number for new cartons.  */  
   "OrderNum":number,
      /**  Indicates whether the Carton has lines or not.  */  
   "HasCartonLines":boolean,
      /**  Displays the contents of XaSyst.StagingReq  */  
   "StagingReq":boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   "EnableWeight":boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   "PkgHeightEnable":number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   "PkgLenEnable":number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   "PkgWidthEnable":number,
      /**  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  */  
   "CtnPkgCode":string,
      /**  Number of packs to replicate  */  
   "ReplicateCount":number,
      /**  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  */  
   "PhantomCasesExist":boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   "EnablePhantom":boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   "MasterpackPackNum":number,
   "PkgSizeUOMEnable":number,
   "ShipToNumName":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for customer shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  */  
   "DocTaxAmt":number,
   "DocWithholdingTaxAmt":number,
      /**  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  */  
   "EnableTax":boolean,
   "TaxAmt":number,
   "Rpt1TaxAmt":number,
   "Rpt2TaxAmt":number,
   "Rpt3TaxAmt":number,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  The flag to indicate if Tax Inclusive Pricing should be on display  */  
   "DisplayInPrice":boolean,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "FreightedShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "FreightedShipViaCodeDescription":string,
      /**  Full description of the bank account.  */  
   "OurBankDescription":string,
      /**  The Bank's full name.  */  
   "OurBankBankName":string,
      /**  Master pack packnum  */  
   "PackToMasterpackDtlPackNum":number,
      /**  The full name of the customer.  */  
   "ShipToCustName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustCustID":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param orderNum
      @param iShipToCustNum
   */  
export interface BuildShipToList_input{
      /**  Order Number  */  
   orderNum:number,
      /**  Ship To Customer ID  */  
   iShipToCustNum:number,
}

export interface BuildShipToList_output{
parameters : {
      /**  output parameters  */  
   shipToList:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface DeleteByID_input{
   packNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CustShipSummaryDtlRow{
      /**  The part number from the order line for this release.  */  
   PartNum:string,
      /**  The customer's part number from the first pack line for this release.  */  
   XPartNum:string,
      /**  The description from the order line for this release.  */  
   LineDesc:string,
      /**  Sales order number for this order release.  */  
   OrderNum:number,
      /**  Sales order line for this release.  */  
   OrderLine:number,
      /**  The number of this release.  */  
   OrderRelNum:number,
      /**  Ordered quantity for this release.  */  
   SellingReqQty:number,
      /**  Selling Unit of measure for these shipment lines.  */  
   SalesUM:string,
      /**  The total quantity packed in this pack for this release.  */  
   PackSellingShippedQty:number,
      /**  The total quantity packed (in all packs) for this release.  */  
   TotalSellingShippedQty:number,
      /**  The quantity ordered, minus the total quantity shipped, for this release.  */  
   SellingRemainQty:number,
      /**  True if any of the shipment lines for this release have been marked as complete.  */  
   ShipCmpl:boolean,
      /**  The total weight of all the lines on this pack for this release.  */  
   TotalNetWeight:number,
      /**  The weight unit of measure.  */  
   WeightUOM:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Selling Unit of measure for this order release.  */  
   OrderRelSalesUM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustShipSummaryListTableset{
   ShipHeadList:Erp_Tablesets_ShipHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustShipSummaryRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Package Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   OTSOrderNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Shipping Address  */  
   AddrList:string,
      /**  Billing Address  */  
   BillAddr:string,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
      /**  Comma delimited list of status types for lookup  */  
   SlipStatus:string,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
   BitFlag:number,
   CustomerOurSupplierCode:string,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
   ShipToName:string,
   ShipToCustBTName:string,
   ShipToCustCustID:string,
   ShipToCustName:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Review_c:boolean,
}

export interface Erp_Tablesets_CustShipSummaryTableset{
   CustShipSummary:Erp_Tablesets_CustShipSummaryRow[],
   CustShipSummaryDtl:Erp_Tablesets_CustShipSummaryDtlRow[],
   OrderRelPkgDetail:Erp_Tablesets_OrderRelPkgDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderRelPkgDetailRow{
      /**  Checkbox indicating whether the packaging is Expendable  */  
   ContainerExpendable:boolean,
      /**  Checkbox indicating whether the packaging is Returnable  */  
   ContainerReturnable:boolean,
      /**  Count of the number of PCIDs in the pack for the selected order/line/rel using that package code  */  
   Count:number,
      /**  Packaging Code used in at least one of the PCID’s for the Pack/Order/Line/Rel  */  
   PkgCode:string,
      /**  UOM of the Pack Qty  */  
   SalesUM:string,
      /**  Quantity packed for the Pack/Order/Line/Rel/Package Code  */  
   PackQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External  ID  */  
   ExternalID:string,
      /**  Iinter Company Received flag  */  
   ICReceived:boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefPackNum:string,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Package Code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountryNum:number,
      /**  Payer Bill To Third Address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To Country Number  */  
   PayBTCountryNum:number,
      /**  Payer Bill To Phone Number  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  */  
   PhantomPack:boolean,
      /**  Pack ID of the pack this pack was replicated from.  This is used as a debugging tool and is not presented to the end user.  */  
   ReplicatedFrom:number,
      /**  Informational field containing either Complete or Partial.  This is only popluated if the ReplicatedFrom field has a value.  This is used as a debugging tool and is not presented to the user.  */  
   ReplicatedStat:string,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  The Sales Order number which contains the One Time ShipTo data. The OTSOrderNum along with the values ShipToNum are used to find the OrderHed or OrderRel to obtain the OTS.  */  
   OTSOrderNum:number,
      /**  Indicates whether or not the taxes for this shipment have been calculated.  This field is used to identify those situations where the tax engine was called but did not generate any taxes because none were needed.  */  
   TaxCalculated:boolean,
      /**  Date the taxes were calculated.  Used for informational and audit tracking purposes.  */  
   TaxCalcDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   OrderAmt:number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocOrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrderAmt:number,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalTax:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalDiscount:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Flag to indicate that project billing Hold Product Invoice flag is true, it prevents this pack slip from being selected for invoicing.  */  
   PBHoldNoInv:boolean,
      /**  Reconciled quantity for the packing slip  */  
   ReconcileQty:number,
      /**  Last trading partner demand schedule processed that affected this packing slip  */  
   ScheduleNumber:string,
      /**  Number of times the customer shipment has been shipped, that means it changed from non shipped status to shipped  */  
   CounterASN:number,
      /**  Bank for Cash Receipts. Default is from 1) Sales Order 2)Bill To Customer 3) System Default(Company).  */  
   OurBank:string,
      /**  It will be used to identify that the shipment will generate an invoice when it got shipped. If the first order release added to a pack belongs to an ERS order, then non ERS order releases will not be allowed in that pack and if the first order release added to a pack belongs to a non ERS order, then ERS order releases will not be allowed in that pack.  */  
   ERSOrder:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OrderDate:string,
      /**  Comma delimited list of status types for lookup  */  
   SlipStatus:string,
      /**  Shipping Address  */  
   AddrList:string,
      /**  Billing Address  */  
   BillAddr:string,
      /**  Indicates if Customer is on Credit Hold  */  
   CreditHold:boolean,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
      /**  Flag indicating OrderRel's going to more than one shipTo  */  
   MultipleShippers:boolean,
      /**  Indicates whether to hide/view ExternalDeliveryNote field  */  
   SendShipment:boolean,
      /**  CustID associated with ShipHeadHead.BTCustNum.  */  
   BTCustID:string,
      /**  CustName associated with ShipHead.BTCustNum.  */  
   BTCustomerName:string,
      /**  Used by the manifest system.  Sum of the value of items in the carton.  Item price - discount + sales tax.  */  
   CartonContentValue:number,
      /**  Set to Y if the carton is the last one being shiped to the customer.  If the sum of the quantity packed does not equal the quantity ordered for each line in the carton the value is No.  */  
   LastCartonFlag:boolean,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
   EnableShipped:boolean,
      /**  Order Number for new cartons.  */  
   OrderNum:number,
      /**  Indicates whether the Carton has lines or not.  */  
   HasCartonLines:boolean,
      /**  Displays the contents of XaSyst.StagingReq  */  
   StagingReq:boolean,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  A zero indicates the Packing height is to be enabled.  */  
   PkgHeightEnable:number,
      /**  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  */  
   PkgLenEnable:number,
      /**  A zero indicates the packaging width field is to be enabled.  */  
   PkgWidthEnable:number,
      /**  Used to enable users to default the Carton Trk Dtl package settings.  Initial value defaults to the ShipHead.PkgCode.  However, this field does NOT have to be the same as the ShipHead.PkgCode.  */  
   CtnPkgCode:string,
      /**  Number of packs to replicate  */  
   ReplicateCount:number,
      /**  Logical indicating if CartonTrkDtl records exist for this pack.  Used by the UI for row rules.  */  
   PhantomCasesExist:boolean,
      /**  Logical indicating if the PhantomPack checkbox is to be enabled.  */  
   EnablePhantom:boolean,
      /**  Pack ID of the Masterpack this shipment is on.  */  
   MasterpackPackNum:number,
   PkgSizeUOMEnable:number,
   ShipToNumName:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for customer shipments  */  
   HasLegNumCnfg:boolean,
      /**  Document Total tax amount from ShipDtl Tax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
   DocWithholdingTaxAmt:number,
      /**  Intended for internal UI use.  Identifies whether or not taxes are generated for shipdtls.  */  
   EnableTax:boolean,
   TaxAmt:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  The flag to indicate if Tax Inclusive Pricing should be on display  */  
   DisplayInPrice:boolean,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   FreightedShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   FreightedShipViaCodeDescription:string,
      /**  Full description of the bank account.  */  
   OurBankDescription:string,
      /**  The Bank's full name.  */  
   OurBankBankName:string,
      /**  Master pack packnum  */  
   PackToMasterpackDtlPackNum:number,
      /**  The full name of the customer.  */  
   ShipToCustName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustCustID:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCustShipSummaryTableset{
   CustShipSummary:Erp_Tablesets_CustShipSummaryRow[],
   CustShipSummaryDtl:Erp_Tablesets_CustShipSummaryDtlRow[],
   OrderRelPkgDetail:Erp_Tablesets_OrderRelPkgDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param packNum
   */  
export interface GetByID_input{
   packNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CustShipSummaryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CustShipSummaryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CustShipSummaryTableset[],
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
   returnObj:Erp_Tablesets_CustShipSummaryListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCustShipSummary_input{
   ds:Erp_Tablesets_CustShipSummaryTableset[],
}

export interface GetNewCustShipSummary_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipSummaryTableset[],
}
}

   /** Required : 
      @param company
      @param packNum
      @param orderNum
      @param orderLine
      @param orderRel
   */  
export interface GetOrderRelPkgDetail_input{
      /**  Current company  */  
   company:string,
      /**  Pack ID  */  
   packNum:number,
      /**  Order Number  */  
   orderNum:number,
      /**  Order Line number  */  
   orderLine:number,
      /**  Order Release number  */  
   orderRel:number,
}

export interface GetOrderRelPkgDetail_output{
   returnObj:Erp_Tablesets_CustShipSummaryTableset[],
}

   /** Required : 
      @param whereClauseCustShipSummary
      @param whereClauseCustShipSummaryDtl
      @param whereClauseOrderRelPkgDetail
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCustShipSummary:string,
   whereClauseCustShipSummaryDtl:string,
   whereClauseOrderRelPkgDetail:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CustShipSummaryTableset[],
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
   ds:Erp_Tablesets_UpdExtCustShipSummaryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCustShipSummaryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CustShipSummaryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustShipSummaryTableset[],
}
}

