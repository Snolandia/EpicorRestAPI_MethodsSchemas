import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SalesOrdHedDtlSvc
// Description: BO for Sales Orders containing the header and detail tables only
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get SalesOrdHedDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesOrdHedDtls
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderHedRow
   */  
export function get_SalesOrdHedDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesOrdHedDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OrderHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesOrdHedDtls(requestBody:Erp_Tablesets_OrderHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SalesOrdHedDtl item
   Description: Calls GetByID to retrieve the SalesOrdHedDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesOrdHedDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OrderHedRow
   */  
export function get_SalesOrdHedDtls_Company_OrderNum(Company:string, OrderNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_OrderHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SalesOrdHedDtl for the service
   Description: Calls UpdateExt to update SalesOrdHedDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesOrdHedDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SalesOrdHedDtls_Company_OrderNum(Company:string, OrderNum:string, requestBody:Erp_Tablesets_OrderHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete SalesOrdHedDtl item
   Description: Call UpdateExt to delete SalesOrdHedDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesOrdHedDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SalesOrdHedDtls_Company_OrderNum(Company:string, OrderNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get OrderDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OrderDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlRow
   */  
export function get_SalesOrdHedDtls_Company_OrderNum_OrderDtls(Company:string, OrderNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")/OrderDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OrderDtl item
   Description: Calls GetByID to retrieve the OrderDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OrderDtlRow
   */  
export function get_SalesOrdHedDtls_Company_OrderNum_OrderDtls_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/SalesOrdHedDtls(" + Company + "," + OrderNum + ")/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_OrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get OrderDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlRow
   */  
export function get_OrderDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OrderDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OrderDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderDtls(requestBody:Erp_Tablesets_OrderDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OrderDtl item
   Description: Calls GetByID to retrieve the OrderDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OrderDtlRow
   */  
export function get_OrderDtls_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_OrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OrderDtl for the service
   Description: Calls UpdateExt to update OrderDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OrderDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OrderDtls_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, requestBody:Erp_Tablesets_OrderDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete OrderDtl item
   Description: Call UpdateExt to delete OrderDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OrderDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OrderDtls_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/OrderDtls(" + Company + "," + OrderNum + "," + OrderLine + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseOrderHed:string, whereClauseOrderDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseOrderHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOrderHed=" + whereClauseOrderHed
   }
   if(typeof whereClauseOrderDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOrderDtl=" + whereClauseOrderDtl
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(orderNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof orderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderNum=" + orderNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsContactTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:GetRowsContactTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsContactTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetRowsContactTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsContactTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:GetRowsCustomerTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustomerTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetRowsCustomerTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsCustomerTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOrderHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOrderHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOrderHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrderHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOrderHed(requestBody:GetNewOrderHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOrderHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetNewOrderHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOrderHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOrderDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOrderDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOrderDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrderDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOrderDtl(requestBody:GetNewOrderDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOrderDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetNewOrderDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewOrderDtl_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesOrdHedDtlSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderHedRow,
}

export interface Erp_Tablesets_OrderDtlRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidLine":boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  EDI Reference  */  
   "Reference":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   "Commissionable":boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in
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
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   "OrderQty":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDiscount":number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   "RequestDate":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   "ShipComment":string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   "PickListComment":string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   "TaxCatID":string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   "AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "DocAdvanceBillBal":number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   "QuoteLine":number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   "TMBilling":boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   "OrigWhyNoTax":string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   "NeedByDate":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   "CustNum":number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   "Rework":boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   "RMANum":number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   "RMALine":number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   "SellingQuantity":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   "ShipLineComplete":boolean,
      /**  Quantity from last EDI update.  */  
   "CumeQty":number,
      /**  Date of last update  */  
   "CumeDate":string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  Indicates if the price of the order line can be changed.  */  
   "LockPrice":boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   "DisplaySeq":number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   "KitParentLine":number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   "KitShipComplete":boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitBackFlush":boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPrintCompsInv":boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPricing":string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   "KitQtyPer":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate1":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate2":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate3":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate4":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate5":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit1":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit2":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit3":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit4":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit5":number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   "DemandContractLine":number,
      /**  Create New Job flag  */  
   "CreateNewJob":boolean,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  Get Details flag  */  
   "GetDtls":boolean,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  Schedule Job flag  */  
   "SchedJob":boolean,
      /**  Release Job flag  */  
   "RelJob":boolean,
      /**  Enable New Job flag  */  
   "EnableCreateNewJob":boolean,
      /**  Enable Get Details flag  */  
   "EnableGetDtls":boolean,
      /**  Enable Schedule Job flag  */  
   "EnableSchedJob":boolean,
      /**  Enable Release Job flag  */  
   "EnableRelJob":boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   "CounterSaleWarehouse":string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   "CounterSaleBinNum":string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   "CounterSaleLotNum":string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   "CounterSaleDimCode":string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   "DemandDtlRejected":boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   "KitsLoaded":boolean,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   "DemandHeadSeq":number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   "DemandDtlSeq":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Total Number of releases for the line  */  
   "TotalReleases":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt1UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt2UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt3UnitPrice":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1Discount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2Discount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3Discount":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt1AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt2AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt3AdvanceBillBal":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1ListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2ListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3ListPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3OrdBasedPrice":number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   "ExtPriceDtl":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPriceDtl":number,
      /**  Status of Order Line  */  
   "LineStatus":string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   "InUnitPrice":number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   "DocInUnitPrice":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   "InDiscount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   "DocInDiscount":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   "InListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   "InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   "DocInOrdBasedPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt1InUnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt2InUnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt3InUnitPrice":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1InDiscount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2InDiscount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3InDiscount":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1InListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2InListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3InListPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   "InExtPriceDtl":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   "DocInExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPriceDtl":number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   "OldOurOpenQty":number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   "OldSellingOpenQty":number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   "OldOpenValue":number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   "OldProdCode":string,
      /**  Previous Selling Quantity  */  
   "PrevSellQty":number,
      /**  Previous Part Number  */  
   "PrevPartNum":string,
      /**  Previous Customer Part Number  */  
   "PrevXPartNum":string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   "KitCompOrigSeq":number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   "KitCompOrigPart":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
   "DiscBreakListCode":string,
   "DiscListPrice":number,
   "LockDisc":boolean,
   "OverrideDiscPriceList":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  ECCOrderNum  */  
   "ECCOrderNum":string,
      /**  ECCOrderLine  */  
   "ECCOrderLine":number,
      /**  DupOnJobCrt  */  
   "DupOnJobCrt":boolean,
      /**  UndersPct  */  
   "UndersPct":number,
      /**  Overs  */  
   "Overs":number,
      /**  Unders  */  
   "Unders":number,
      /**  OversUnitPrice  */  
   "OversUnitPrice":number,
      /**  PlanUserID  */  
   "PlanUserID":string,
      /**  PlanGUID  */  
   "PlanGUID":string,
      /**  MOMsourceType  */  
   "MOMsourceType":string,
      /**  MOMsourceEst  */  
   "MOMsourceEst":string,
      /**  DefaultOversPricing  */  
   "DefaultOversPricing":string,
      /**  ECCPlant  */  
   "ECCPlant":string,
      /**  ECCQuoteNum  */  
   "ECCQuoteNum":string,
      /**  ECCQuoteLine  */  
   "ECCQuoteLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MfgJobType  */  
   "MfgJobType":string,
      /**  ProFormaInvComment  */  
   "ProFormaInvComment":string,
      /**  CreateJob  */  
   "CreateJob":boolean,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  DocInAdvanceBillBal  */  
   "DocInAdvanceBillBal":number,
      /**  InAdvanceBillBal  */  
   "InAdvanceBillBal":number,
      /**  Rpt1InAdvanceBillBal  */  
   "Rpt1InAdvanceBillBal":number,
      /**  Rpt2InAdvanceBillBal  */  
   "Rpt2InAdvanceBillBal":number,
      /**  Rpt3InAdvanceBillBal  */  
   "Rpt3InAdvanceBillBal":number,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  Base price before any price breaks and discounts  */  
   "MSRP":number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   "DocMSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   "Rpt1MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   "Rpt2MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   "Rpt3MSRP":number,
      /**  Distributor end customer price.  */  
   "EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   "DocEndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   "Rpt1EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   "Rpt2EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   "Rpt3EndCustomerPrice":number,
      /**  Promotional Price offered to Dealer and Distributors.  */  
   "PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   "DocPromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   "Rpt1PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   "Rpt2PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   "Rpt3PromotionalPrice":number,
      /**  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  */  
   "OrderLineStatusCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   "AttributeSetID":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   "KBOriginalConfigProdID":number,
      /**  TotalCovenantDiscount  */  
   "TotalCovenantDiscount":number,
      /**  DocCovenantDiscount  */  
   "DocCovenantDiscount":number,
      /**  Rpt1CovenantDiscount  */  
   "Rpt1CovenantDiscount":number,
      /**  Rpt2CovenantDiscount  */  
   "Rpt2CovenantDiscount":number,
      /**  Rpt3CovenantDiscount  */  
   "Rpt3CovenantDiscount":number,
      /**  TotalInCovenantDiscount  */  
   "TotalInCovenantDiscount":number,
      /**  DocInCovenantDiscount  */  
   "DocInCovenantDiscount":number,
      /**  Rpt1InCovenantDiscount  */  
   "Rpt1InCovenantDiscount":number,
      /**  Rpt2InCovenantDiscount  */  
   "Rpt2InCovenantDiscount":number,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
   "AvailableQuantity":number,
      /**  Available Price Lists  */  
   "AvailPriceLists":string,
   "AvailUMFromQuote":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
      /**  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   "CalcUnitPrice":number,
   "ConfigType":string,
   "Configured":string,
   "CounterSale":boolean,
      /**  The message text returned by the credit check process.  */  
   "CreditLimitMessage":string,
      /**  The source that put the customer on credit hold.  */  
   "CreditLimitSource":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyID":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DemandQuantity":number,
   "DimCode":string,
   "DimConvFactor":number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DocDspDiscount":number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DocDspUnitPrice":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   "DocInMiscCharges":number,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   "DocLessDiscount":number,
   "DocMiscCharges":number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   "DocTaxAmt":number,
   "DocTotalPrice":number,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DspDiscount":number,
      /**  To display the type of job this is: MFG = Manufacturing, PRJ = Project  */  
   "DspJobType":string,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DspUnitPrice":number,
   "DUM":string,
      /**  Web basket configuration related SysRowID  */  
   "ECCConfigSysRowId":string,
      /**  Additional discount calculated by ECC  */  
   "ECCDiscount":number,
      /**  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  */  
   "ECCPreventRepricing":boolean,
      /**  Allow enable/disable for the button Attibutes in Order Line  */  
   "EnableDynAttrButton":boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableKitUnitPrice":boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableRenewalNbr":boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableSellingQty":boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   "EntryProcess":string,
   "ExtPrice":number,
   "FromQuoteLineFlag":boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   "FSAInstallationCost":number,
   "FSAInstallationOrderLine":number,
   "FSAInstallationOrderNum":number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   "FSAInstallationRequired":boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   "FSAInstallationType":string,
   "FSAInstallationTypeDescription":string,
      /**  Indicates whether the part has at least one Complement  */  
   "HasComplement":boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   "HasDowngrade":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasSubstitute":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasUpgrade":boolean,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   "InMiscCharges":number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   "InPrice":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   "InvtyUOM":string,
   "JobTypeDesc":string,
      /**  If the Job has been already created against this line.  */  
   "JobWasCreated":boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   "KitChangeParms":boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   "KitFlagDescription":string,
   "KitOrderQtyUOM":string,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   "KitStandard":boolean,
      /**  The amount of discount for display which does not include taxes  */  
   "LessDiscount":number,
   "LotNum":string,
   "MiscCharges":number,
   "MultipleReleases":boolean,
   "OnHandQuantity":number,
   "PartExists":boolean,
   "PartTrackDimension":boolean,
   "PartTrackLots":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLineRef":string,
   "PriceListCodeDesc":string,
   "ProcessCounterSale":boolean,
   "ProcessQuickEntry":boolean,
   "QuoteQtyNum":number,
      /**  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  */  
   "RelWasRecInvoiced":boolean,
      /**  Pass Credit Limit check message to the UI  */  
   "RespMessage":string,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt1DspDiscount":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt1DspUnitPrice":number,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   "Rpt1ExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt1InMiscCharges":number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   "Rpt1LessDiscount":number,
      /**  Report currency misc charges  */  
   "Rpt1MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt1TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt1TotalPrice":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt2DspDiscount":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt2DspUnitPrice":number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   "Rpt2ExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt2InMiscCharges":number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   "Rpt2LessDiscount":number,
      /**  Report currency misc charges  */  
   "Rpt2MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt2TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt2TotalPrice":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt3DspDiscount":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt3DspUnitPrice":number,
      /**  Extended price for the order line in Rpt3 currency  */  
   "Rpt3ExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt3InMiscCharges":number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   "Rpt3LessDiscount":number,
      /**  Report Currency misc charges  */  
   "Rpt3MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt3TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt3TotalPrice":number,
   "SalesRepName1":string,
   "SalesRepName2":string,
   "SalesRepName3":string,
   "SalesRepName4":string,
   "SalesRepName5":string,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   "TaxAmt":number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   "ThisOrderInvtyQty":number,
   "TotalPrice":number,
   "TotalShipped":number,
   "WarehouseCode":string,
   "WarehouseDesc":string,
   "BinNum":string,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  */  
   "AttributeMismatch":boolean,
      /**  A string containing the parameters needed to run Job Manager  */  
   "JobManagerString":string,
      /**  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   "CalcOrdBasedPrice":number,
      /**  At least 1 OrderRel for OrderDtl has a PONum assigned.  */  
   "SalesOrderLinked":boolean,
      /**  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  */  
   "InventoryAttributeSetID":number,
   "BitFlag":number,
   "CommodityCodeDescription":string,
   "ContractCodeContractDescription":string,
   "CustNumSendToFSA":boolean,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "DiscBreakListCodeListDescription":string,
   "DiscBreakListCodeEndDate":string,
   "DiscBreakListCodeStartDate":string,
   "MktgCampaignIDCampDescription":string,
   "MktgEvntEvntDescription":string,
   "OrderNumBTCustNum":number,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumSendToFSA":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumDefaultAttributeSetID":number,
   "PartNumFSAEquipment":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PriceBreakListDescription":string,
   "PriceBreakStartDate":string,
   "PriceBreakEndDate":string,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "QuoteNumCurrencyCode":string,
   "SalesCatIDDescription":string,
   "TaxCatIDDescription":string,
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Phase_c":string,
   "ItemID_c":string,
   "TypeCode_c":string,
   "OrigTypeCode_c":string,
   "PhaseID_c":string,
   "SalesCatID_c":string,
   "IndustryShipDate_c":string,
   "CreateDate_c":string,
   "PriceUpdateDate_c":string,
   "CreatedBy_c":string,
   "UpdatedBy_c":string,
}

export interface Erp_Tablesets_OrderHedListRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidOrder":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "OrderNum":number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   "PONum":string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   "OrderHeld":boolean,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "OrderDate":string,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "DepositBal":number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "DocDepositBal":number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   "NeedByDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CustOnCreditHold":boolean,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
      /**  BTCustNumCustID  */  
   "BTCustNumCustID":string,
      /**  BTCustNumName  */  
   "BTCustNumName":string,
      /**  DemandContract  */  
   "DemandContract":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OrderHedRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidOrder":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "OrderNum":number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   "PONum":string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   "OrderHeld":boolean,
      /**   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "OrderDate":string,
      /**  An optional field that describes the FOB policy.  */  
   "FOB":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  */  
   "TermsCode":string,
      /**  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  */  
   "DiscountPercent":number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  Stores the Sales Rep Codes for the order. Up to five codes can be  established. This field is not directly maintainable. Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The first one is defaulted from the Customer master if ship to is blank; otherwise, from the Ship To.  */  
   "SalesRepList":string,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   "ShipComment":string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   "PickListComment":string,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "DepositBal":number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "DocDepositBal":number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   "NeedByDate":string,
      /**  Indicates that the credit hold was overridden for this order.  */  
   "CreditOverride":boolean,
      /**  The USERID of the user that overrode an order credit hold (system set).  */  
   "CreditOverrideUserID":string,
      /**  The date that the user last overrode the customer credit hold (system set).  */  
   "CreditOverrideDate":string,
      /**  The time that the user last overrode the customer credit hold in HH:MM:SS format (system set).  */  
   "CreditOverrideTime":string,
      /**  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  */  
   "CreditOverrideLimit":number,
      /**  Controls if an alert is to be sent when shipments are made for this order.  */  
   "SndAlrtShp":boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   "AllocPriorityCode":string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   "ReservePriorityCode":string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   "ShipOrderComplete":boolean,
      /**  Not editable, When SF Synch creates orders, this flag is set to YES.  */  
   "WebOrder":boolean,
      /**  Updated Via SF Synch.  This is the authorization number from a third party credit card validation service.  */  
   "CCApprovalNum":string,
      /**  Order created from EDI interfaced module.  */  
   "EDIOrder":boolean,
      /**  Updated from EDI module if 855 or 865 created.  */  
   "EDIAck":boolean,
      /**  Indicates if this order header is linked to an inter-company PO header.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   "ICPONum":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  This is the web-login-id (email address) of the person that placed the order.  */  
   "WebEntryPerson":string,
      /**  Indicates whether the email acknowledgement of the order has been sent.  (For web orders)  */  
   "AckEmailSent":boolean,
      /**  Indicates if order based discounting needs to be applied to the order.  */  
   "ApplyOrderBasedDisc":boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**   Indicates Entry method program that used to create the order.
S = Standard, Q = Quick Entry,  C = Counter Sales, D = Demand/EDI  */  
   "EntryMethod":string,
      /**  The help desk case that created this order.  */  
   "HDCaseNum":number,
      /**  Flag used in sales order entry for counter sales orders.  */  
   "CounterSale":boolean,
      /**  Create AR Invoice for counter sales order.  */  
   "CreateInvoice":boolean,
      /**  Create Packing Slip for counter sale.  */  
   "CreatePackingSlip":boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   "CCAmount":number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   "CCFreight":number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   "CCTax":number,
      /**  Total amount being sent to the credit card processor  */  
   "CCTotal":number,
      /**  See CCAmount  */  
   "CCDocAmount":number,
      /**  See CCFreight  */  
   "CCDocFreight":number,
      /**  See CCTax  */  
   "CCDocTax":number,
      /**  See CCTotal  */  
   "CCDocTotal":number,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Bill To Customer Number  */  
   "BTCustNum":number,
      /**  New database field as it can be changed by user.  Default is set to BTCustNum?s primary billing contact.  If a primary billing contact is not set, default is ?None Selected?.  Keep in mind the BTCustNum field may be the same as CustNum (SoldTo) but the default would still be this customer?s primary billing contact where the ConNum field (Contact for sold to) is defaulting the primary purchasing contact.  */  
   "BTConNum":number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   "RepRate4":number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   "RepRate5":number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   "RepSplit1":number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   "RepSplit2":number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   "RepSplit3":number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   "RepSplit4":number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   "RepSplit5":number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   "RepRate1":number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   "RepRate2":number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   "RepRate3":number,
      /**  Incremented whenever an outbound sales document is generated from the order, i.e. Sales Order Acknowledgement, Response to Change, etc.  */  
   "OutboundSalesDocCtr":number,
      /**  Incremented whenever an outbound shipping document is generated from the order, i.e. ASN.  */  
   "OutboundShipDocsCtr":number,
      /**  The demand contract this OrderHed is related to.  */  
   "DemandContractNum":number,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
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
      /**  The date after which the sales order should be canceled.  */  
   "CancelAfterDate":string,
      /**  Indicates if the demand that created/updated this order has been rejected.  */  
   "DemandRejected":boolean,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   "OverrideService":boolean,
      /**  Indicates if the Order is a credit card order  */  
   "CreditCardOrder":boolean,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   "DemandHeadSeq":number,
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
      /**  Freight charges will not be returned if 'yes'  */  
   "DropShip":boolean,
      /**  Added for international shipping  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
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
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Freight Forwarder third address line.  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling Required flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Package flag.  */  
   "NonStdPkg":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
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
      /**  Freight Forwarder country portion of the address  */  
   "FFCountryNum":number,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Payer Bill To  third address line  */  
   "PayBTAddress3":string,
      /**  Payer Bill To country portion of the address  */  
   "PayBTCountryNum":number,
      /**  Payer Bill To phone number  */  
   "PayBTPhone":string,
      /**  UPS Quantity View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Nam  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantity View Memo  */  
   "UPSQVMemo":string,
      /**  This flag will be used to indicate if the order is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the order which could affect taxes (OrderDtl, OrderHed, OrderMisc, etc). It defaults from XASyst.SOReadyToCalcDflt field when an order is created.  */  
   "ReadyToCalc":boolean,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalCharges":number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalMisc":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalDiscount":number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "TotalComm":number,
      /**  Total Advance Billable Balance  */  
   "TotalAdvBill":number,
      /**  Total number of lines on the order  */  
   "TotalLines":number,
      /**  Total Number of releases on order  */  
   "TotalReleases":number,
      /**  Total number of distinct release dates on order  */  
   "TotalRelDates":number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalCharges":number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalMisc":number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalDiscount":number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "DocTotalComm":number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "DocTotalTax":number,
      /**  Total Advance Billable Balance  */  
   "DocTotalAdvBill":number,
      /**  Total Shipped amount  */  
   "TotalShipped":number,
      /**  Total amount of order that has been invoiced  */  
   "TotalInvoiced":number,
      /**  Total number of lines that were commissionable  */  
   "TotalCommLines":number,
      /**  Commission earned for first sales rep  */  
   "SRCommAmt1":number,
      /**  Commission earned for second sales rep  */  
   "SRCommAmt2":number,
      /**  Commission earned for third sales rep  */  
   "SRCommAmt3":number,
      /**  Commission earned for fourth sales rep  */  
   "SRCommAmt4":number,
      /**  Commission earned for fifth sales rep  */  
   "SRCommAmt5":number,
      /**  Total Commissionable Amount for first salesrep  */  
   "SRCommableAmt1":number,
      /**  Total Commissionable Amount for second salesrep  */  
   "SRCommableAmt2":number,
      /**  Total Commissionable Amount for third salesrep  */  
   "SRCommableAmt3":number,
      /**  Total Commissionable Amount for fourth salesrep  */  
   "SRCommableAmt4":number,
      /**  Total Commissionable Amount for fifth salesrep  */  
   "SRCommableAmt5":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Display value contains the deposit balance in a reporting currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "Rpt1DepositBal":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "Rpt2DepositBal":number,
      /**  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "Rpt3DepositBal":number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalCharges":number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalCharges":number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalCharges":number,
      /**  Total Advance Billable Balance  */  
   "Rpt1TotalAdvBill":number,
      /**  Total Advance Billable Balance  */  
   "Rpt2TotalAdvBill":number,
      /**  Total Advance Billable Balance  */  
   "Rpt3TotalAdvBill":number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalMisc":number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalMisc":number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalMisc":number,
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
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalComm":number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalComm":number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalComm":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt1TotalTax":number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt2TotalTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   "Rpt3TotalTax":number,
      /**  See CCAmount  */  
   "Rpt1CCAmount":number,
      /**  See CCAmount  */  
   "Rpt2CCAmount":number,
      /**  See CCAmount  */  
   "Rpt3CCAmount":number,
      /**  See CCFreight  */  
   "Rpt1CCFreight":number,
      /**  See CCFreight  */  
   "Rpt2CCFreight":number,
      /**  See CCFreight  */  
   "Rpt3CCFreight":number,
      /**  See CCTax  */  
   "Rpt1CCTax":number,
      /**  See CCTax  */  
   "Rpt2CCTax":number,
      /**  See CCTax  */  
   "Rpt3CCTax":number,
      /**  See CCTotal  */  
   "Rpt1CCTotal":number,
      /**  See CCTotal  */  
   "Rpt2CCTotal":number,
      /**  See CCTotal  */  
   "Rpt3CCTotal":number,
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
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipment country  */  
   "OTSCountryNum":number,
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
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   "OTSCustSaved":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Status of Order  */  
   "OrderStatus":string,
      /**  Hold Set by Demand  */  
   "HoldSetByDemand":boolean,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Reserved for future use  */  
   "InTotalCharges":number,
      /**  Reserved for future use  */  
   "InTotalMisc":number,
      /**  Reserved for future use  */  
   "InTotalDiscount":number,
      /**  Reserved for future use  */  
   "DocInTotalCharges":number,
      /**  Reserved for future use  */  
   "DocInTotalMisc":number,
      /**  Reserved for future use  */  
   "DocInTotalDiscount":number,
      /**  Reserved for future use  */  
   "Rpt1InTotalCharges":number,
      /**  Reserved for future use  */  
   "Rpt2InTotalCharges":number,
      /**  Reserved for future use  */  
   "Rpt3InTotalCharges":number,
      /**  Reserved for future use  */  
   "Rpt1InTotalMisc":number,
      /**  Reserved for future use  */  
   "Rpt2InTotalMisc":number,
      /**  Reserved for future use  */  
   "Rpt3InTotalMisc":number,
      /**  Reserved for future use  */  
   "Rpt1InTotalDiscount":number,
      /**  Reserved for future use  */  
   "Rpt2InTotalDiscount":number,
      /**  Reserved for future use  */  
   "Rpt3InTotalDiscount":number,
      /**  Letter of Credit ID.  */  
   "ARLOCID":string,
      /**  Bank for Cash Receipts. Default is from Customer(Bill To).  */  
   "OurBank":string,
      /**  It will be used to identify SO that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via DM, the default will be taken from the value in the DM records.  */  
   "ERSOrder":boolean,
      /**  Indicates that order is on hold due to amount exceeding value on Letter of Credit.  */  
   "LOCHold":boolean,
      /**  Currency code used in further packing slips.  */  
   "PSCurrCode":string,
      /**  Currency code used in further AR invoices.  */  
   "InvCurrCode":string,
      /**  Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Transaction Document for the record.  */  
   "TranDocTypeID":string,
      /**  Cross Reference Contract Number.  */  
   "XRefContractNum":string,
      /**  Cross Reference Contract Date.  */  
   "XRefContractDate":string,
      /**  Date in which the related demand was last processed.  */  
   "DemandProcessDate":string,
      /**  System Time when demand was last processed.  */  
   "DemandProcessTime":number,
      /**  Last Schedule Number in which the demand was processed.  */  
   "LastScheduleNumber":string,
      /**  EDI Transaction Control Number  */  
   "LastTCtrlNum":string,
      /**  EDI Batch Control Number  */  
   "LastBatchNum":string,
      /**  ECCOrderNum  */  
   "ECCOrderNum":string,
      /**  ECCPONum  */  
   "ECCPONum":string,
      /**  WIOrder  */  
   "WIOrder":string,
      /**  WIApplication  */  
   "WIApplication":string,
      /**  WIUsername  */  
   "WIUsername":string,
      /**  WIUserID  */  
   "WIUserID":string,
      /**  WICreditCardorder  */  
   "WICreditCardorder":boolean,
      /**  OrderCSR  */  
   "OrderCSR":string,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IsCSRSet  */  
   "IsCSRSet":boolean,
      /**  ECCPaymentMethod  */  
   "ECCPaymentMethod":string,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  OTSShipToNum  */  
   "OTSShipToNum":string,
      /**  ProFormaInvComment  */  
   "ProFormaInvComment":string,
      /**  ccToken  */  
   "ccToken":string,
      /**  InvcOrderCmp  */  
   "InvcOrderCmp":boolean,
      /**  ReprintSOAck  */  
   "ReprintSOAck":boolean,
      /**  CounterSOAck  */  
   "CounterSOAck":number,
      /**  DispatchReason  */  
   "DispatchReason":string,
      /**  Plant  */  
   "Plant":string,
      /**  This flag will be used to indicate if the sales order is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  Ship the good by this time  */  
   "ShipByTime":number,
      /**  Taiwan GUI Calendar Fiscal Year  */  
   "TWFiscalYear":number,
      /**  Taiwan GUI Calendar Fiscal Year Suffix  */  
   "TWFiscalYearSuffix":string,
      /**  Taiwan GUI Calendar Fiscal Period  */  
   "TWFiscalPeriod":number,
      /**  GUI Group of Legal Numbers  */  
   "TWGUIGroup":string,
      /**  Seller GUI Code  */  
   "TWGUIRegNumSeller":string,
      /**  Buyer GUI Code  */  
   "TWGUIRegNumBuyer":string,
      /**  OrderOpenCredit  */  
   "OrderOpenCredit":number,
      /**  ClosedNotShipped  */  
   "ClosedNotShipped":number,
      /**  InvCurrDepositBal  */  
   "InvCurrDepositBal":number,
      /**  Article. 106c  */  
   "PLArticle106c":boolean,
      /**  Invoices are issued by a taxpayer's representative  */  
   "PLInvIssuedByTaxpayer":boolean,
      /**  Invoices issued by the second taxpayer  */  
   "PLInvIssuedBySecondTaxpayer":boolean,
      /**  Tourist Services  */  
   "PLTouristService":boolean,
      /**  Second hand goods, works of art, collectibles or antiques  */  
   "PLSecondHandOrArts":boolean,
      /**  Appropriate Legal Article of the Act  */  
   "PLLegalArticleAct":string,
      /**  Appropriate Legal Article of 2006/112/WE Directive  */  
   "PLLegalArticleWEDirective":string,
      /**  Other Legal Article  */  
   "PLLegalArticleOther":string,
      /**  Name of the Enforcement Authority or the Name of the Judicial Officer  */  
   "PLEnforcementAuthName":string,
      /**  Address of the Enforcement Authority or Judicial Officer  */  
   "PLEnforcementAuthAddr":string,
      /**  Tax Representative Name  */  
   "PLTaxRepresentativeName":string,
      /**  Tax Representative Address  */  
   "PLTaxRepresentativeAddr":string,
      /**  Tax ID of the Tax Representative  */  
   "PLTaxRepresentativeTaxID":string,
      /**  Margin Scheme  */  
   "PLMarginScheme":number,
      /**  Goods or Service VAT exempt  */  
   "PLGoodsOrServiceVATExempt":boolean,
      /**  Credit Card Holder City  */  
   "CCCity":string,
      /**  Credit Card Holder State  */  
   "CCState":string,
      /**  ExtAOEUserID  */  
   "ExtAOEUserID":string,
      /**  ExtAOE  */  
   "ExtAOE":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  Incoterm Code  */  
   "IncotermCode":string,
      /**  Incoterm Location  */  
   "IncotermLocation":string,
      /**  CovenantDiscPercent  */  
   "CovenantDiscPercent":number,
      /**  TotalCovenantDiscount  */  
   "TotalCovenantDiscount":number,
      /**  DocCovenantDiscount  */  
   "DocCovenantDiscount":number,
      /**  Rpt1CovenantDiscount  */  
   "Rpt1CovenantDiscount":number,
      /**  Rpt2CovenantDiscount  */  
   "Rpt2CovenantDiscount":number,
      /**  Rpt3CovenantDiscount  */  
   "Rpt3CovenantDiscount":number,
      /**  TotalInCovenantDiscount  */  
   "TotalInCovenantDiscount":number,
      /**  DocInCovenantDiscount  */  
   "DocInCovenantDiscount":number,
      /**  Rpt1InCovenantDiscount  */  
   "Rpt1InCovenantDiscount":number,
      /**  Rpt2InCovenantDiscount  */  
   "Rpt2InCovenantDiscount":number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   "AvailBTCustList":string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSAddr":string,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "AVSZip":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
      /**  Bill to customer name.  */  
   "BillToCustomerName":string,
      /**  Bill To Address List.  */  
   "BTAddressList":string,
   "BTContactEMailAddress":string,
      /**  Bill to contact fax number.  */  
   "BTContactFaxNum":string,
      /**  Bill to contact name.  */  
   "BTContactName":string,
      /**  Bill to contact phone number.  */  
   "BTContactPhoneNum":string,
      /**  Bill To Customer ID  */  
   "BTCustID":string,
      /**  The flag to indicate if the user can change Tax Liability on the header level after adding a detail line.  */  
   "CanChangeTaxLiab":boolean,
      /**  Stored Credit Card Number  */  
   "CardStore":string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   "CCCSCID":string,
      /**  Tokenized value of CSCID  */  
   "CCCSCIDToken":string,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   "CCIsTraining":boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   "CCResponse":string,
   "CCRounding":number,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   "CCTranID":string,
      /**  Credit Card Transaction Type  */  
   "CCTranType":string,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   "CSCResult":string,
   "CurrencySwitch":boolean,
   "CustAllowOTS":boolean,
   "CustomerPrintAck":boolean,
      /**  If true the customer requires a unique PO on Sales Orders  */  
   "CustomerRequiresPO":boolean,
      /**  When set to true, indicates that this customer does not have credit available from your company.  */  
   "CustOnCreditHold":boolean,
   "CustTradePartnerName":string,
      /**  DemandContract  */  
   "DemandContract":string,
   "DocCCRounding":number,
   "DocTotalNet":number,
   "DocTotalOrder":number,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   "dspBTCustID":string,
      /**  ECC Contact Email - Contains the email address of the ECC login that placed the sales order. This only applies for B2C Orders.  */  
   "ECCEmail":string,
      /**  ECC Payment Description  */  
   "ECCPaymentDesc":string,
      /**  True when Credit Card Procesing module is enabled  */  
   "EnableCreditCard":boolean,
      /**  True when Job Wizard must be enabled  */  
   "EnableJobWizard":boolean,
      /**  True when SoldTo ID must be enabled  */  
   "EnableSoldToID":boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   "EntryProcess":string,
      /**  It will be displayed when the value of the ERS flag at the sales order is different from the value in the customer master file.  */  
   "ERSOverride":boolean,
      /**  Used by UI to disable CurrencyCode  */  
   "HasMiscCharges":boolean,
   "HasOrderLines":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
   "LinkMsg":string,
      /**  Internal field which indicates if Order Tax Liability is not going to be changed even though Ship To is changed.  Related to Tax inclusive pricing. Depends on user response.  */  
   "NoTaxRgnChange":boolean,
   "OTSSaved":boolean,
      /**  OTS Tax Liability Code (Header)  */  
   "OTSTaxRegionCode":string,
      /**  Contains the Parent Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "ParentCustNum":number,
   "ProposedTaxRgn":string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   "ReferencePNRef":string,
      /**  Internal field toindicate if the system should reset Bill to Customer address.  Based on the  user reply for LOC.  */  
   "ResetBTCustAddr":boolean,
      /**  Internal field which indicates if existing Release Tax Region should be se-set to the new Order Header Tax Liability.  Depends on the user reply.  */  
   "ResetRelTaxRgn":boolean,
   "Rpt1CCRounding":number,
   "Rpt1TotalNet":number,
   "Rpt2CCRounding":number,
   "Rpt2TotalNet":number,
   "Rpt3CCRounding":number,
   "Rpt3TotalNet":number,
      /**  Element 1 of SalesRepList  */  
   "SalesRepCode1":string,
      /**  Element 2 of SalesRepList  */  
   "SalesRepCode2":string,
      /**  Element 3 of SalesRepList  */  
   "SalesRepCode3":string,
      /**  Element 4 of SalesRepList  */  
   "SalesRepCode4":string,
      /**  Element 5 of SalesRepList  */  
   "SalesRepCode5":string,
   "SalesRepName1":string,
   "SalesRepName2":string,
   "SalesRepName3":string,
   "SalesRepName4":string,
   "SalesRepName5":string,
   "ShipToAddressList":string,
   "ShipToContactEMailAddress":string,
   "ShipToContactFaxNum":string,
   "ShipToContactName":string,
   "ShipToContactPhoneNum":string,
      /**  Customer Id of the third-party Ship To  */  
   "ShipToCustId":string,
   "ShowApplyOrderDiscountsControl":boolean,
   "SoldToAddressList":string,
   "SoldToContactEMailAddress":string,
   "SoldToContactFaxNum":string,
   "SoldToContactName":string,
   "SoldToContactPhoneNum":string,
      /**  This field defines the type of the term  */  
   "TermsType":string,
   "TotalNet":number,
   "TotalOrder":number,
   "TranDocTypeDescr":string,
      /**  the true discount percent from the order total  */  
   "TrueDiscountPercent":number,
      /**  Taiwan GUI Legal Number Generation Type  */  
   "TWGenerationType":string,
   "UpdateDtlAndRelRecords":boolean,
      /**  Indicates if one or more invoices exist for this order  */  
   "InvoicesExist":boolean,
   "BTAddressFormatted":string,
      /**  The formatted ship to address  */  
   "ShipToAddressFormatted":string,
      /**  The formatted Sold To Address  */  
   "SoldToAddressFormatted":string,
   "TranDate":string,
   "TranNum":number,
   "TranTime":number,
      /**  Indicates there is an OrderRel record that has a non-null NeedByDate  */  
   "OrderRelNeedByDateNotNull":boolean,
      /**  Indicates a customer referenced on the order is inactive.  */  
   "InactiveCustomer":boolean,
      /**  Enable Fulfillment Queue Actions  */  
   "EnableAllocationQueueActions":boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   "CREProcessor":boolean,
      /**  Flag indicating whether to enable Incoterm Location  */  
   "EnableIncotermLocation":boolean,
   "BitFlag":number,
   "BTCustNumCustID":string,
   "BTCustNumName":string,
   "BTCustNumBTName":string,
   "CardTypeDescription":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrDesc":string,
   "CustomerBTName":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "CustomerAllowShipTo3":boolean,
   "FOBDescription":string,
   "HDCaseDescription":string,
   "IncotermsDescription":string,
   "InvCurrCurrDesc":string,
   "OTSCntryISOCode":string,
   "OTSCntryDescription":string,
   "OTSCntryEUMember":boolean,
   "OurBankDescription":string,
   "OurBankBankName":string,
   "PlantName":string,
   "PSCurrCurrDesc":string,
   "RateGrpDescription":string,
   "ReservePriDescription":string,
   "ShipToNumInactive":boolean,
   "ShipViaCodeInactive":boolean,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TaxRegionCodeDescription":string,
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Project_c":string,
   "OriginalOrderNo_c":number,
   "MASFlag_c":boolean,
   "Estimate_c":boolean,
   "ShipOrderComplete_c":boolean,
   "ProjectID_c":string,
   "PhaseID_c":string,
   "SalesCatID__c":string,
   "TaxCatID_c":string,
   "MfgOrder_c":boolean,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param orderNum
   */  
export interface DeleteByID_input{
   orderNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_OrderCustTrkRow{
      /**  from OrderHed.OrderNum  */  
   OrderNum:number,
      /**  from OrderHed.OpenOrder  */  
   OpenOrder:boolean,
      /**  from OrderHed.Company  */  
   Company:string,
      /**  from OrderHed.OrderHeld  */  
   OrderHeld:boolean,
      /**  from OrderHed.PONum  */  
   PONum:string,
      /**  from OrderHed.CustNum  */  
   CustNum:number,
      /**  from OrderHed.ShipToNum  */  
   ShipToNum:string,
      /**  from OrderHed.ShpConNum  */  
   ShpConNum:number,
      /**  from OrderHed.PrcConNum  */  
   PrcConNum:number,
      /**  from OrderHed.OrderDate  */  
   OrderDate:string,
      /**  from OrderHed.NeedByDate  */  
   OrderHedNeedByDate:string,
      /**  from OrderHed.RequestDate  */  
   OrderHedRequestDate:string,
      /**  from OrderHed.Currency  */  
   CurrencyCode:string,
      /**  from OrderDtl.OrderLine  */  
   OrderLine:number,
      /**  from OrderDtl.OpenLine  */  
   OpenLine:boolean,
      /**  from OrderDtl.POLine  */  
   POLine:string,
      /**  from OrderDtl.PartNum  */  
   PartNum:string,
      /**  from OrderDtl.LineDesc  */  
   LineDesc:string,
      /**  from OrderDtl.SellingQuantity  */  
   SellingQuantity:number,
      /**  from OrderDtl.SalesUM  */  
   SalesUM:string,
      /**  from OrderDtl.DocUnitPrice  */  
   DocUnitPrice:number,
      /**  from OrderDtl.ProdCode  */  
   ProdCode:string,
      /**  from OrderDtl.ProdCodeDescription  */  
   ProdCodeDescription:string,
      /**  from OrderDtl.NeedByDate  */  
   OrderDtlNeedByDate:string,
      /**  from OrderDtl.RequestDate  */  
   OrderDtlRequestDate:string,
      /**  from OrderHed.WebOrder  */  
   WebOrder:boolean,
      /**  If OrderHed.CustOnCreditHold = true and OrderHed.CreditOverride = false and OrderHed.OpenOrder = true then true otherwise false  */  
   OnCreditHold:boolean,
      /**  from OrderDtl.RevisionNum  */  
   RevisionNum:string,
      /**  from OrderDtl.XPartNum  */  
   XPartNum:string,
      /**  from OrderDtl.XRevisionNum  */  
   XRevisionNum:string,
      /**  Bill To customer number from OrderHed.  */  
   BTCustNum:number,
      /**  Bill To Customer ID from OrderHed.  */  
   BTCustID:string,
      /**  Bill To Customer Name.  */  
   BTCustomerName:string,
      /**  Bill to address list.  */  
   BTAddressList:string,
      /**  Bill to contact fax number.  */  
   BTContactFaxNum:string,
      /**  Bill to contact phone number  */  
   BTContactPhoneNum:string,
      /**  Bill To Contact name.  */  
   BTContactName:string,
      /**  Bill to contact num.  */  
   BTConNum:number,
   CreditOverride:boolean,
      /**  Sold to customer id.  */  
   SoldToCustID:string,
      /**  Sold to customer name.  */  
   SoldToCustName:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
      /**  The customer ID.  */  
   CustID:string,
      /**  from OrderDtl.POLineRef  */  
   POLineRef:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderCustTrkTableset{
   OrderCustTrk:Erp_Tablesets_OrderCustTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderDtlRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidLine:boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   Commissionable:boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
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
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   OrderQty:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDiscount:number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   PickListComment:string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   TaxCatID:string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   DocAdvanceBillBal:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   QuoteNum:number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   TMBilling:boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   OrigWhyNoTax:string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   NeedByDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   CustNum:number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   Rework:boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   RMANum:number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   RMALine:number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   ProjectID:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   ShipLineComplete:boolean,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  Indicates if the price of the order line can be changed.  */  
   LockPrice:boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   KitPricing:string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   KitQtyPer:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate1:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate2:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate3:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate4:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate5:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit1:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit2:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit3:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit4:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit5:number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   DemandContractLine:number,
      /**  Create New Job flag  */  
   CreateNewJob:boolean,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Get Details flag  */  
   GetDtls:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Schedule Job flag  */  
   SchedJob:boolean,
      /**  Release Job flag  */  
   RelJob:boolean,
      /**  Enable New Job flag  */  
   EnableCreateNewJob:boolean,
      /**  Enable Get Details flag  */  
   EnableGetDtls:boolean,
      /**  Enable Schedule Job flag  */  
   EnableSchedJob:boolean,
      /**  Enable Release Job flag  */  
   EnableRelJob:boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   CounterSaleWarehouse:string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   CounterSaleBinNum:string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   CounterSaleLotNum:string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   CounterSaleDimCode:string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   DemandDtlRejected:boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   KitsLoaded:boolean,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   DemandDtlSeq:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Total Number of releases for the line  */  
   TotalReleases:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3UnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3Discount:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt1AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt2AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt3AdvanceBillBal:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3ListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Status of Order Line  */  
   LineStatus:string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   InUnitPrice:number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   DocInUnitPrice:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   InDiscount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   DocInDiscount:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   InListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   DocInOrdBasedPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3InUnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3InDiscount:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InOrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   InExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   DocInExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPriceDtl:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldOurOpenQty:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldSellingOpenQty:number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   OldOpenValue:number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   OldProdCode:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscBreakListCode:string,
   DiscListPrice:number,
   LockDisc:boolean,
   OverrideDiscPriceList:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  ECCOrderNum  */  
   ECCOrderNum:string,
      /**  ECCOrderLine  */  
   ECCOrderLine:number,
      /**  DupOnJobCrt  */  
   DupOnJobCrt:boolean,
      /**  UndersPct  */  
   UndersPct:number,
      /**  Overs  */  
   Overs:number,
      /**  Unders  */  
   Unders:number,
      /**  OversUnitPrice  */  
   OversUnitPrice:number,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  MOMsourceType  */  
   MOMsourceType:string,
      /**  MOMsourceEst  */  
   MOMsourceEst:string,
      /**  DefaultOversPricing  */  
   DefaultOversPricing:string,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  ECCQuoteNum  */  
   ECCQuoteNum:string,
      /**  ECCQuoteLine  */  
   ECCQuoteLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MfgJobType  */  
   MfgJobType:string,
      /**  ProFormaInvComment  */  
   ProFormaInvComment:string,
      /**  CreateJob  */  
   CreateJob:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  DocInAdvanceBillBal  */  
   DocInAdvanceBillBal:number,
      /**  InAdvanceBillBal  */  
   InAdvanceBillBal:number,
      /**  Rpt1InAdvanceBillBal  */  
   Rpt1InAdvanceBillBal:number,
      /**  Rpt2InAdvanceBillBal  */  
   Rpt2InAdvanceBillBal:number,
      /**  Rpt3InAdvanceBillBal  */  
   Rpt3InAdvanceBillBal:number,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt3EndCustomerPrice:number,
      /**  Promotional Price offered to Dealer and Distributors.  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt3PromotionalPrice:number,
      /**  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  */  
   OrderLineStatusCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
   AvailableQuantity:number,
      /**  Available Price Lists  */  
   AvailPriceLists:string,
   AvailUMFromQuote:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   CalcUnitPrice:number,
   ConfigType:string,
   Configured:string,
   CounterSale:boolean,
      /**  The message text returned by the credit check process.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyID:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DemandQuantity:number,
   DimCode:string,
   DimConvFactor:number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspDiscount:number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspUnitPrice:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   DocInMiscCharges:number,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   DocLessDiscount:number,
   DocMiscCharges:number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   DocTaxAmt:number,
   DocTotalPrice:number,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspDiscount:number,
      /**  To display the type of job this is: MFG = Manufacturing, PRJ = Project  */  
   DspJobType:string,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspUnitPrice:number,
   DUM:string,
      /**  Web basket configuration related SysRowID  */  
   ECCConfigSysRowId:string,
      /**  Additional discount calculated by ECC  */  
   ECCDiscount:number,
      /**  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  */  
   ECCPreventRepricing:boolean,
      /**  Allow enable/disable for the button Attibutes in Order Line  */  
   EnableDynAttrButton:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableKitUnitPrice:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableRenewalNbr:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableSellingQty:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
   ExtPrice:number,
   FromQuoteLineFlag:boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   FSAInstallationCost:number,
   FSAInstallationOrderLine:number,
   FSAInstallationOrderNum:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   FSAInstallationType:string,
   FSAInstallationTypeDescription:string,
      /**  Indicates whether the part has at least one Complement  */  
   HasComplement:boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   HasDowngrade:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasSubstitute:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasUpgrade:boolean,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   InMiscCharges:number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   InPrice:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   InvtyUOM:string,
   JobTypeDesc:string,
      /**  If the Job has been already created against this line.  */  
   JobWasCreated:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
   KitOrderQtyUOM:string,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   KitStandard:boolean,
      /**  The amount of discount for display which does not include taxes  */  
   LessDiscount:number,
   LotNum:string,
   MiscCharges:number,
   MultipleReleases:boolean,
   OnHandQuantity:number,
   PartExists:boolean,
   PartTrackDimension:boolean,
   PartTrackLots:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLineRef:string,
   PriceListCodeDesc:string,
   ProcessCounterSale:boolean,
   ProcessQuickEntry:boolean,
   QuoteQtyNum:number,
      /**  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  */  
   RelWasRecInvoiced:boolean,
      /**  Pass Credit Limit check message to the UI  */  
   RespMessage:string,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspUnitPrice:number,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   Rpt1ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt1InMiscCharges:number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   Rpt1LessDiscount:number,
      /**  Report currency misc charges  */  
   Rpt1MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt1TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt1TotalPrice:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspUnitPrice:number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   Rpt2ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt2InMiscCharges:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt2LessDiscount:number,
      /**  Report currency misc charges  */  
   Rpt2MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt2TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt2TotalPrice:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspUnitPrice:number,
      /**  Extended price for the order line in Rpt3 currency  */  
   Rpt3ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt3InMiscCharges:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt3LessDiscount:number,
      /**  Report Currency misc charges  */  
   Rpt3MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt3TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt3TotalPrice:number,
   SalesRepName1:string,
   SalesRepName2:string,
   SalesRepName3:string,
   SalesRepName4:string,
   SalesRepName5:string,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   TaxAmt:number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   ThisOrderInvtyQty:number,
   TotalPrice:number,
   TotalShipped:number,
   WarehouseCode:string,
   WarehouseDesc:string,
   BinNum:string,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  */  
   AttributeMismatch:boolean,
      /**  A string containing the parameters needed to run Job Manager  */  
   JobManagerString:string,
      /**  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   CalcOrdBasedPrice:number,
      /**  At least 1 OrderRel for OrderDtl has a PONum assigned.  */  
   SalesOrderLinked:boolean,
      /**  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  */  
   InventoryAttributeSetID:number,
   BitFlag:number,
   CommodityCodeDescription:string,
   ContractCodeContractDescription:string,
   CustNumSendToFSA:boolean,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   DiscBreakListCodeListDescription:string,
   DiscBreakListCodeEndDate:string,
   DiscBreakListCodeStartDate:string,
   MktgCampaignIDCampDescription:string,
   MktgEvntEvntDescription:string,
   OrderNumBTCustNum:number,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumSendToFSA:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumDefaultAttributeSetID:number,
   PartNumFSAEquipment:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PriceBreakListDescription:string,
   PriceBreakStartDate:string,
   PriceBreakEndDate:string,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   QuoteNumCurrencyCode:string,
   SalesCatIDDescription:string,
   TaxCatIDDescription:string,
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Phase_c:string,
   ItemID_c:string,
   TypeCode_c:string,
   OrigTypeCode_c:string,
   PhaseID_c:string,
   SalesCatID_c:string,
   IndustryShipDate_c:string,
   CreateDate_c:string,
   PriceUpdateDate_c:string,
   CreatedBy_c:string,
   UpdatedBy_c:string,
}

export interface Erp_Tablesets_OrderHedListRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidOrder:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   OrderNum:number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   PONum:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   OrderHeld:boolean,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DepositBal:number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DocDepositBal:number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustOnCreditHold:boolean,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
      /**  BTCustNumCustID  */  
   BTCustNumCustID:string,
      /**  BTCustNumName  */  
   BTCustNumName:string,
      /**  DemandContract  */  
   DemandContract:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderHedListTableset{
   OrderHedList:Erp_Tablesets_OrderHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderHedRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidOrder:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   OrderNum:number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   PONum:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   OrderHeld:boolean,
      /**   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  */  
   TermsCode:string,
      /**  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  */  
   DiscountPercent:number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Stores the Sales Rep Codes for the order. Up to five codes can be  established. This field is not directly maintainable. Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The first one is defaulted from the Customer master if ship to is blank; otherwise, from the Ship To.  */  
   SalesRepList:string,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   PickListComment:string,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DepositBal:number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DocDepositBal:number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Indicates that the credit hold was overridden for this order.  */  
   CreditOverride:boolean,
      /**  The USERID of the user that overrode an order credit hold (system set).  */  
   CreditOverrideUserID:string,
      /**  The date that the user last overrode the customer credit hold (system set).  */  
   CreditOverrideDate:string,
      /**  The time that the user last overrode the customer credit hold in HH:MM:SS format (system set).  */  
   CreditOverrideTime:string,
      /**  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  */  
   CreditOverrideLimit:number,
      /**  Controls if an alert is to be sent when shipments are made for this order.  */  
   SndAlrtShp:boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   ReservePriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Not editable, When SF Synch creates orders, this flag is set to YES.  */  
   WebOrder:boolean,
      /**  Updated Via SF Synch.  This is the authorization number from a third party credit card validation service.  */  
   CCApprovalNum:string,
      /**  Order created from EDI interfaced module.  */  
   EDIOrder:boolean,
      /**  Updated from EDI module if 855 or 865 created.  */  
   EDIAck:boolean,
      /**  Indicates if this order header is linked to an inter-company PO header.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   ICPONum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  This is the web-login-id (email address) of the person that placed the order.  */  
   WebEntryPerson:string,
      /**  Indicates whether the email acknowledgement of the order has been sent.  (For web orders)  */  
   AckEmailSent:boolean,
      /**  Indicates if order based discounting needs to be applied to the order.  */  
   ApplyOrderBasedDisc:boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**   Indicates Entry method program that used to create the order.
S = Standard, Q = Quick Entry,  C = Counter Sales, D = Demand/EDI  */  
   EntryMethod:string,
      /**  The help desk case that created this order.  */  
   HDCaseNum:number,
      /**  Flag used in sales order entry for counter sales orders.  */  
   CounterSale:boolean,
      /**  Create AR Invoice for counter sales order.  */  
   CreateInvoice:boolean,
      /**  Create Packing Slip for counter sale.  */  
   CreatePackingSlip:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  New database field as it can be changed by user.  Default is set to BTCustNum?s primary billing contact.  If a primary billing contact is not set, default is ?None Selected?.  Keep in mind the BTCustNum field may be the same as CustNum (SoldTo) but the default would still be this customer?s primary billing contact where the ConNum field (Contact for sold to) is defaulting the primary purchasing contact.  */  
   BTConNum:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate4:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate5:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit1:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit2:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit3:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit4:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit5:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate1:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate2:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate3:number,
      /**  Incremented whenever an outbound sales document is generated from the order, i.e. Sales Order Acknowledgement, Response to Change, etc.  */  
   OutboundSalesDocCtr:number,
      /**  Incremented whenever an outbound shipping document is generated from the order, i.e. ASN.  */  
   OutboundShipDocsCtr:number,
      /**  The demand contract this OrderHed is related to.  */  
   DemandContractNum:number,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
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
      /**  The date after which the sales order should be canceled.  */  
   CancelAfterDate:string,
      /**  Indicates if the demand that created/updated this order has been rejected.  */  
   DemandRejected:boolean,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  Indicates if the Order is a credit card order  */  
   CreditCardOrder:boolean,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
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
      /**  Freight charges will not be returned if 'yes'  */  
   DropShip:boolean,
      /**  Added for international shipping  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
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
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder third address line.  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling Required flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Package flag.  */  
   NonStdPkg:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
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
      /**  Freight Forwarder country portion of the address  */  
   FFCountryNum:number,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Payer Bill To  third address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To country portion of the address  */  
   PayBTCountryNum:number,
      /**  Payer Bill To phone number  */  
   PayBTPhone:string,
      /**  UPS Quantity View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Nam  */  
   UPSQVShipFromName:string,
      /**  UPS Quantity View Memo  */  
   UPSQVMemo:string,
      /**  This flag will be used to indicate if the order is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the order which could affect taxes (OrderDtl, OrderHed, OrderMisc, etc). It defaults from XASyst.SOReadyToCalcDflt field when an order is created.  */  
   ReadyToCalc:boolean,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalCharges:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalMisc:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalDiscount:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalComm:number,
      /**  Total Advance Billable Balance  */  
   TotalAdvBill:number,
      /**  Total number of lines on the order  */  
   TotalLines:number,
      /**  Total Number of releases on order  */  
   TotalReleases:number,
      /**  Total number of distinct release dates on order  */  
   TotalRelDates:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalCharges:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalMisc:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalDiscount:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalComm:number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalTax:number,
      /**  Total Advance Billable Balance  */  
   DocTotalAdvBill:number,
      /**  Total Shipped amount  */  
   TotalShipped:number,
      /**  Total amount of order that has been invoiced  */  
   TotalInvoiced:number,
      /**  Total number of lines that were commissionable  */  
   TotalCommLines:number,
      /**  Commission earned for first sales rep  */  
   SRCommAmt1:number,
      /**  Commission earned for second sales rep  */  
   SRCommAmt2:number,
      /**  Commission earned for third sales rep  */  
   SRCommAmt3:number,
      /**  Commission earned for fourth sales rep  */  
   SRCommAmt4:number,
      /**  Commission earned for fifth sales rep  */  
   SRCommAmt5:number,
      /**  Total Commissionable Amount for first salesrep  */  
   SRCommableAmt1:number,
      /**  Total Commissionable Amount for second salesrep  */  
   SRCommableAmt2:number,
      /**  Total Commissionable Amount for third salesrep  */  
   SRCommableAmt3:number,
      /**  Total Commissionable Amount for fourth salesrep  */  
   SRCommableAmt4:number,
      /**  Total Commissionable Amount for fifth salesrep  */  
   SRCommableAmt5:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Display value contains the deposit balance in a reporting currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   Rpt1DepositBal:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   Rpt2DepositBal:number,
      /**  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   Rpt3DepositBal:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalCharges:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalCharges:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalCharges:number,
      /**  Total Advance Billable Balance  */  
   Rpt1TotalAdvBill:number,
      /**  Total Advance Billable Balance  */  
   Rpt2TotalAdvBill:number,
      /**  Total Advance Billable Balance  */  
   Rpt3TotalAdvBill:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalMisc:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalMisc:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalMisc:number,
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
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalComm:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalComm:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalComm:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
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
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
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
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Status of Order  */  
   OrderStatus:string,
      /**  Hold Set by Demand  */  
   HoldSetByDemand:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Reserved for future use  */  
   InTotalCharges:number,
      /**  Reserved for future use  */  
   InTotalMisc:number,
      /**  Reserved for future use  */  
   InTotalDiscount:number,
      /**  Reserved for future use  */  
   DocInTotalCharges:number,
      /**  Reserved for future use  */  
   DocInTotalMisc:number,
      /**  Reserved for future use  */  
   DocInTotalDiscount:number,
      /**  Reserved for future use  */  
   Rpt1InTotalCharges:number,
      /**  Reserved for future use  */  
   Rpt2InTotalCharges:number,
      /**  Reserved for future use  */  
   Rpt3InTotalCharges:number,
      /**  Reserved for future use  */  
   Rpt1InTotalMisc:number,
      /**  Reserved for future use  */  
   Rpt2InTotalMisc:number,
      /**  Reserved for future use  */  
   Rpt3InTotalMisc:number,
      /**  Reserved for future use  */  
   Rpt1InTotalDiscount:number,
      /**  Reserved for future use  */  
   Rpt2InTotalDiscount:number,
      /**  Reserved for future use  */  
   Rpt3InTotalDiscount:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  Bank for Cash Receipts. Default is from Customer(Bill To).  */  
   OurBank:string,
      /**  It will be used to identify SO that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via DM, the default will be taken from the value in the DM records.  */  
   ERSOrder:boolean,
      /**  Indicates that order is on hold due to amount exceeding value on Letter of Credit.  */  
   LOCHold:boolean,
      /**  Currency code used in further packing slips.  */  
   PSCurrCode:string,
      /**  Currency code used in further AR invoices.  */  
   InvCurrCode:string,
      /**  Legal Number for the record.  */  
   LegalNumber:string,
      /**  Transaction Document for the record.  */  
   TranDocTypeID:string,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  Last Schedule Number in which the demand was processed.  */  
   LastScheduleNumber:string,
      /**  EDI Transaction Control Number  */  
   LastTCtrlNum:string,
      /**  EDI Batch Control Number  */  
   LastBatchNum:string,
      /**  ECCOrderNum  */  
   ECCOrderNum:string,
      /**  ECCPONum  */  
   ECCPONum:string,
      /**  WIOrder  */  
   WIOrder:string,
      /**  WIApplication  */  
   WIApplication:string,
      /**  WIUsername  */  
   WIUsername:string,
      /**  WIUserID  */  
   WIUserID:string,
      /**  WICreditCardorder  */  
   WICreditCardorder:boolean,
      /**  OrderCSR  */  
   OrderCSR:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IsCSRSet  */  
   IsCSRSet:boolean,
      /**  ECCPaymentMethod  */  
   ECCPaymentMethod:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  ProFormaInvComment  */  
   ProFormaInvComment:string,
      /**  ccToken  */  
   ccToken:string,
      /**  InvcOrderCmp  */  
   InvcOrderCmp:boolean,
      /**  ReprintSOAck  */  
   ReprintSOAck:boolean,
      /**  CounterSOAck  */  
   CounterSOAck:number,
      /**  DispatchReason  */  
   DispatchReason:string,
      /**  Plant  */  
   Plant:string,
      /**  This flag will be used to indicate if the sales order is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  Ship the good by this time  */  
   ShipByTime:number,
      /**  Taiwan GUI Calendar Fiscal Year  */  
   TWFiscalYear:number,
      /**  Taiwan GUI Calendar Fiscal Year Suffix  */  
   TWFiscalYearSuffix:string,
      /**  Taiwan GUI Calendar Fiscal Period  */  
   TWFiscalPeriod:number,
      /**  GUI Group of Legal Numbers  */  
   TWGUIGroup:string,
      /**  Seller GUI Code  */  
   TWGUIRegNumSeller:string,
      /**  Buyer GUI Code  */  
   TWGUIRegNumBuyer:string,
      /**  OrderOpenCredit  */  
   OrderOpenCredit:number,
      /**  ClosedNotShipped  */  
   ClosedNotShipped:number,
      /**  InvCurrDepositBal  */  
   InvCurrDepositBal:number,
      /**  Article. 106c  */  
   PLArticle106c:boolean,
      /**  Invoices are issued by a taxpayer's representative  */  
   PLInvIssuedByTaxpayer:boolean,
      /**  Invoices issued by the second taxpayer  */  
   PLInvIssuedBySecondTaxpayer:boolean,
      /**  Tourist Services  */  
   PLTouristService:boolean,
      /**  Second hand goods, works of art, collectibles or antiques  */  
   PLSecondHandOrArts:boolean,
      /**  Appropriate Legal Article of the Act  */  
   PLLegalArticleAct:string,
      /**  Appropriate Legal Article of 2006/112/WE Directive  */  
   PLLegalArticleWEDirective:string,
      /**  Other Legal Article  */  
   PLLegalArticleOther:string,
      /**  Name of the Enforcement Authority or the Name of the Judicial Officer  */  
   PLEnforcementAuthName:string,
      /**  Address of the Enforcement Authority or Judicial Officer  */  
   PLEnforcementAuthAddr:string,
      /**  Tax Representative Name  */  
   PLTaxRepresentativeName:string,
      /**  Tax Representative Address  */  
   PLTaxRepresentativeAddr:string,
      /**  Tax ID of the Tax Representative  */  
   PLTaxRepresentativeTaxID:string,
      /**  Margin Scheme  */  
   PLMarginScheme:number,
      /**  Goods or Service VAT exempt  */  
   PLGoodsOrServiceVATExempt:boolean,
      /**  Credit Card Holder City  */  
   CCCity:string,
      /**  Credit Card Holder State  */  
   CCState:string,
      /**  ExtAOEUserID  */  
   ExtAOEUserID:string,
      /**  ExtAOE  */  
   ExtAOE:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Bill to customer name.  */  
   BillToCustomerName:string,
      /**  Bill To Address List.  */  
   BTAddressList:string,
   BTContactEMailAddress:string,
      /**  Bill to contact fax number.  */  
   BTContactFaxNum:string,
      /**  Bill to contact name.  */  
   BTContactName:string,
      /**  Bill to contact phone number.  */  
   BTContactPhoneNum:string,
      /**  Bill To Customer ID  */  
   BTCustID:string,
      /**  The flag to indicate if the user can change Tax Liability on the header level after adding a detail line.  */  
   CanChangeTaxLiab:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Tokenized value of CSCID  */  
   CCCSCIDToken:string,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   CCIsTraining:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
   CCRounding:number,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
   CurrencySwitch:boolean,
   CustAllowOTS:boolean,
   CustomerPrintAck:boolean,
      /**  If true the customer requires a unique PO on Sales Orders  */  
   CustomerRequiresPO:boolean,
      /**  When set to true, indicates that this customer does not have credit available from your company.  */  
   CustOnCreditHold:boolean,
   CustTradePartnerName:string,
      /**  DemandContract  */  
   DemandContract:string,
   DocCCRounding:number,
   DocTotalNet:number,
   DocTotalOrder:number,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspBTCustID:string,
      /**  ECC Contact Email - Contains the email address of the ECC login that placed the sales order. This only applies for B2C Orders.  */  
   ECCEmail:string,
      /**  ECC Payment Description  */  
   ECCPaymentDesc:string,
      /**  True when Credit Card Procesing module is enabled  */  
   EnableCreditCard:boolean,
      /**  True when Job Wizard must be enabled  */  
   EnableJobWizard:boolean,
      /**  True when SoldTo ID must be enabled  */  
   EnableSoldToID:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
      /**  It will be displayed when the value of the ERS flag at the sales order is different from the value in the customer master file.  */  
   ERSOverride:boolean,
      /**  Used by UI to disable CurrencyCode  */  
   HasMiscCharges:boolean,
   HasOrderLines:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
   LinkMsg:string,
      /**  Internal field which indicates if Order Tax Liability is not going to be changed even though Ship To is changed.  Related to Tax inclusive pricing. Depends on user response.  */  
   NoTaxRgnChange:boolean,
   OTSSaved:boolean,
      /**  OTS Tax Liability Code (Header)  */  
   OTSTaxRegionCode:string,
      /**  Contains the Parent Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   ParentCustNum:number,
   ProposedTaxRgn:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
      /**  Internal field toindicate if the system should reset Bill to Customer address.  Based on the  user reply for LOC.  */  
   ResetBTCustAddr:boolean,
      /**  Internal field which indicates if existing Release Tax Region should be se-set to the new Order Header Tax Liability.  Depends on the user reply.  */  
   ResetRelTaxRgn:boolean,
   Rpt1CCRounding:number,
   Rpt1TotalNet:number,
   Rpt2CCRounding:number,
   Rpt2TotalNet:number,
   Rpt3CCRounding:number,
   Rpt3TotalNet:number,
      /**  Element 1 of SalesRepList  */  
   SalesRepCode1:string,
      /**  Element 2 of SalesRepList  */  
   SalesRepCode2:string,
      /**  Element 3 of SalesRepList  */  
   SalesRepCode3:string,
      /**  Element 4 of SalesRepList  */  
   SalesRepCode4:string,
      /**  Element 5 of SalesRepList  */  
   SalesRepCode5:string,
   SalesRepName1:string,
   SalesRepName2:string,
   SalesRepName3:string,
   SalesRepName4:string,
   SalesRepName5:string,
   ShipToAddressList:string,
   ShipToContactEMailAddress:string,
   ShipToContactFaxNum:string,
   ShipToContactName:string,
   ShipToContactPhoneNum:string,
      /**  Customer Id of the third-party Ship To  */  
   ShipToCustId:string,
   ShowApplyOrderDiscountsControl:boolean,
   SoldToAddressList:string,
   SoldToContactEMailAddress:string,
   SoldToContactFaxNum:string,
   SoldToContactName:string,
   SoldToContactPhoneNum:string,
      /**  This field defines the type of the term  */  
   TermsType:string,
   TotalNet:number,
   TotalOrder:number,
   TranDocTypeDescr:string,
      /**  the true discount percent from the order total  */  
   TrueDiscountPercent:number,
      /**  Taiwan GUI Legal Number Generation Type  */  
   TWGenerationType:string,
   UpdateDtlAndRelRecords:boolean,
      /**  Indicates if one or more invoices exist for this order  */  
   InvoicesExist:boolean,
   BTAddressFormatted:string,
      /**  The formatted ship to address  */  
   ShipToAddressFormatted:string,
      /**  The formatted Sold To Address  */  
   SoldToAddressFormatted:string,
   TranDate:string,
   TranNum:number,
   TranTime:number,
      /**  Indicates there is an OrderRel record that has a non-null NeedByDate  */  
   OrderRelNeedByDateNotNull:boolean,
      /**  Indicates a customer referenced on the order is inactive.  */  
   InactiveCustomer:boolean,
      /**  Enable Fulfillment Queue Actions  */  
   EnableAllocationQueueActions:boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   CREProcessor:boolean,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
   BitFlag:number,
   BTCustNumCustID:string,
   BTCustNumName:string,
   BTCustNumBTName:string,
   CardTypeDescription:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrDesc:string,
   CustomerBTName:string,
   CustomerCustID:string,
   CustomerName:string,
   CustomerAllowShipTo3:boolean,
   FOBDescription:string,
   HDCaseDescription:string,
   IncotermsDescription:string,
   InvCurrCurrDesc:string,
   OTSCntryISOCode:string,
   OTSCntryDescription:string,
   OTSCntryEUMember:boolean,
   OurBankDescription:string,
   OurBankBankName:string,
   PlantName:string,
   PSCurrCurrDesc:string,
   RateGrpDescription:string,
   ReservePriDescription:string,
   ShipToNumInactive:boolean,
   ShipViaCodeInactive:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TaxRegionCodeDescription:string,
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Project_c:string,
   OriginalOrderNo_c:number,
   MASFlag_c:boolean,
   Estimate_c:boolean,
   ShipOrderComplete_c:boolean,
   ProjectID_c:string,
   PhaseID_c:string,
   SalesCatID__c:string,
   TaxCatID_c:string,
   MfgOrder_c:boolean,
}

export interface Erp_Tablesets_SalesOrdHedDtlTableset{
   OrderHed:Erp_Tablesets_OrderHedRow[],
   OrderDtl:Erp_Tablesets_OrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtSalesOrdHedDtlTableset{
   OrderHed:Erp_Tablesets_OrderHedRow[],
   OrderDtl:Erp_Tablesets_OrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param orderNum
   */  
export interface GetByID_input{
   orderNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_SalesOrdHedDtlTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_SalesOrdHedDtlTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_SalesOrdHedDtlTableset[],
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
   returnObj:Erp_Tablesets_OrderHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param orderNum
   */  
export interface GetNewOrderDtl_input{
   ds:Erp_Tablesets_SalesOrdHedDtlTableset[],
   orderNum:number,
}

export interface GetNewOrderDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesOrdHedDtlTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewOrderHed_input{
   ds:Erp_Tablesets_SalesOrdHedDtlTableset[],
}

export interface GetNewOrderHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesOrdHedDtlTableset,
}
}

   /** Required : 
      @param whereClauseOrderHed
      @param whereClauseOrderDtl
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for OrderHed table.  */  
   whereClauseOrderHed:string,
      /**  Whereclause for OrderDtl table.  */  
   whereClauseOrderDtl:string,
      /**  The contact name to return orders for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_OrderCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseOrderHed
      @param whereClauseOrderDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for OrderHed table.  */  
   whereClauseOrderHed:string,
      /**  Whereclause for OrderDtl table.  */  
   whereClauseOrderDtl:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_OrderCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseOrderHed
      @param whereClauseOrderDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseOrderHed:string,
   whereClauseOrderDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_SalesOrdHedDtlTableset[],
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
   ds:Erp_Tablesets_UpdExtSalesOrdHedDtlTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtSalesOrdHedDtlTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_SalesOrdHedDtlTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SalesOrdHedDtlTableset,
}
}

