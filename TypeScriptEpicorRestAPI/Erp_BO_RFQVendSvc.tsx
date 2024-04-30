import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RFQVendSvc
// Description: Purchase Request For Quote Vendor
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/$metadata", {
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
   Description: Get RFQVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQVends
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendRow
   */  
export function get_RFQVends(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQVends
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RFQVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQVends(requestBody:Erp_Tablesets_RFQVendRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends", {
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
   Summary: Calls GetByID to retrieve the RFQVend item
   Description: Calls GetByID to retrieve the RFQVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RFQVendRow
   */  
export function get_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQVendRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
         resolve(data as Erp_Tablesets_RFQVendRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQVend for the service
   Description: Calls UpdateExt to update RFQVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, requestBody:Erp_Tablesets_RFQVendRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Call UpdateExt to delete RFQVend item
   Description: Call UpdateExt to delete RFQVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQVend
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get RFQLinesSelecteds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQLinesSelecteds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQLinesSelectedRow
   */  
export function get_RFQLinesSelecteds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQLinesSelectedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQLinesSelectedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQLinesSelecteds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQLinesSelecteds(requestBody:Erp_Tablesets_RFQLinesSelectedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds", {
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
   Summary: Calls GetByID to retrieve the RFQLinesSelected item
   Description: Calls GetByID to retrieve the RFQLinesSelected item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQLinesSelected
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
   */  
export function get_RFQLinesSelecteds_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQLinesSelectedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
         resolve(data as Erp_Tablesets_RFQLinesSelectedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQLinesSelected for the service
   Description: Calls UpdateExt to update RFQLinesSelected. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQLinesSelected
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQLinesSelecteds_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, requestBody:Erp_Tablesets_RFQLinesSelectedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Call UpdateExt to delete RFQLinesSelected item
   Description: Call UpdateExt to delete RFQLinesSelected item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQLinesSelected
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RFQNum Desc: RFQNum   Required: True
      @param RFQLine Desc: RFQLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQLinesSelecteds_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company:string, RFQNum:string, RFQLine:string, VendorNum:string, PurPoint:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendListRow)
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
export function get_GetRows(whereClauseRFQVend:string, whereClauseRFQLinesSelected:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRFQVend!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQVend=" + whereClauseRFQVend
   }
   if(typeof whereClauseRFQLinesSelected!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQLinesSelected=" + whereClauseRFQLinesSelected
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(rfQNum:string, rfQLine:string, vendorNum:string, purPoint:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rfQNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rfQNum=" + rfQNum
   }
   if(typeof rfQLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rfQLine=" + rfQLine
   }
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof purPoint!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "purPoint=" + purPoint
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetList" + params, {
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
   Summary: Invoke method AvailableResponses
   Description: Return list of available responses.
   OperationID: AvailableResponses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AvailableResponses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AvailableResponses(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AvailableResponses_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/AvailableResponses", {
          method: 'post',
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
         resolve(data as AvailableResponses_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDetailCalcOurQty
   Description: Run this method when our quantity on the detail changes.
   OperationID: ChangeDetailCalcOurQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailCalcOurQty(requestBody:ChangeDetailCalcOurQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDetailCalcOurQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/ChangeDetailCalcOurQty", {
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
         resolve(data as ChangeDetailCalcOurQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDetailCalcVendQty
   Description: Run this method when supplier quantity on the detail changes.
   OperationID: ChangeDetailCalcVendQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcVendQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcVendQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailCalcVendQty(requestBody:ChangeDetailCalcVendQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDetailCalcVendQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/ChangeDetailCalcVendQty", {
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
         resolve(data as ChangeDetailCalcVendQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPOCreation
   Description: This method checks if everything is okay before creating a PO. If there are
any questions to be asked they will be returned in the 2 message parameters.
If the user answers yes to both questions, then CreatePO can be run
   OperationID: CheckPOCreation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPOCreation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPOCreation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPOCreation(requestBody:CheckPOCreation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPOCreation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/CheckPOCreation", {
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
         resolve(data as CheckPOCreation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePO
   Description: This method Creates a PO for the current RFQVend Line.  If a PO is above a person's
approval limit, then the PO will be created but not approved
   OperationID: CreatePO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePO(requestBody:CreatePO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreatePO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/CreatePO", {
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
         resolve(data as CreatePO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FillRFQLinesSelected
   Description: Run this method to Fill RFQLinesSelected Temp Table with records selected to Create PO
   OperationID: FillRFQLinesSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FillRFQLinesSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillRFQLinesSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FillRFQLinesSelected(requestBody:FillRFQLinesSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FillRFQLinesSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/FillRFQLinesSelected", {
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
         resolve(data as FillRFQLinesSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLineQty
   Description: This method gets the Job Qty (if job related) and sets a flag to tell the UI
to update the Qty, duedate and promise date fields
   OperationID: GetLineQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLineQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLineQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLineQty(requestBody:GetLineQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLineQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetLineQty", {
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
         resolve(data as GetLineQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method to allow sort by external columns
   OperationID: GetListCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:GetListCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetListCustom", {
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
         resolve(data as GetListCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRFQsForSupplierTracker
   Description: Called from Supplier tracker instead of RFQVend GetRows
   OperationID: GetRFQsForSupplierTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRFQsForSupplierTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRFQsForSupplierTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRFQsForSupplierTracker(requestBody:GetRFQsForSupplierTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRFQsForSupplierTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetRFQsForSupplierTracker", {
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
         resolve(data as GetRFQsForSupplierTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListOfRFQVend
   Description: This is a copy of GetList modified to have the RFQ Source and RFQ Status search values  be passed as  parameters
instead of being in the where clause. Run This instead of GetList.
UI - DO NOT include 'RFQ source' and 'RFQ status' in the where clause. Instead, pass them as parameters per the following:
   OperationID: ListOfRFQVend
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ListOfRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOfRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListOfRFQVend(requestBody:ListOfRFQVend_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListOfRFQVend_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/ListOfRFQVend", {
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
         resolve(data as ListOfRFQVend_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListOfRFQVendWhereClause
   Description: This is a copy of ListOfRFQVend modified to accept an RFQNum as a parameter and fill the list filtered by that RFQNum.
   OperationID: ListOfRFQVendWhereClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ListOfRFQVendWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOfRFQVendWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListOfRFQVendWhereClause(requestBody:ListOfRFQVendWhereClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListOfRFQVendWhereClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/ListOfRFQVendWhereClause", {
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
         resolve(data as ListOfRFQVendWhereClause_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListOfRFQVendWhereClauseVendor
   Description: This is a copy of ListOfRFQVend modified to accept an RFQNum as a parameter and fill the list filtered by that RFQNum.
   OperationID: ListOfRFQVendWhereClauseVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ListOfRFQVendWhereClauseVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOfRFQVendWhereClauseVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListOfRFQVendWhereClauseVendor(requestBody:ListOfRFQVendWhereClauseVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListOfRFQVendWhereClauseVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/ListOfRFQVendWhereClauseVendor", {
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
         resolve(data as ListOfRFQVendWhereClauseVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshDataset
   Description: This method does refresh for each loaded records.
   OperationID: RefreshDataset
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshDataset(requestBody:RefreshDataset_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshDataset_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RefreshDataset", {
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
         resolve(data as RefreshDataset_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RowsOfRFQVend
   Description: This is a copy of GetRows modified to have the RFQ Source and RFQ Status search values  be passed as  parameters
instead of being in the where clause. can be run instead of GetRows.
UI - DO NOT include 'RFQ source' and 'RFQ status' in the where clause. Instead, pass them as parameters per the following:
            
            
<returns>Returns RFQVendDataSet data set.</returns><param name="whereClause">Where clause to filter the query results.</param><param name="pageSize">page size.</param><param name="absolutePage">absolute page</param><param name="morePages">more pages.</param><param name="rfqSourcein">If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.</param><param name="rfqStatusin">If 'all'  -> input 'A', if 'closed' -> input 'C', if 'open' -> input 'O'. </param>
   OperationID: RowsOfRFQVend
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RowsOfRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RowsOfRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RowsOfRFQVend(requestBody:RowsOfRFQVend_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RowsOfRFQVend_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RowsOfRFQVend", {
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
         resolve(data as RowsOfRFQVend_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRFQVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQVend
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQVend(requestBody:GetNewRFQVend_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRFQVend_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetNewRFQVend", {
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
         resolve(data as GetNewRFQVend_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQLinesSelectedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQLinesSelectedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQVendListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQVendRow,
}

export interface Erp_Tablesets_RFQLinesSelectedRow{
   "Company":string,
   "RFQNum":number,
   "RFQLine":number,
   "VendorNum":number,
   "PurPoint":string,
   "PartNum":string,
   "CalcOurQty":number,
   "CalcVendQty":number,
   "IUM":string,
   "LineDescription":string,
   "OurUOM":string,
   "PUM":string,
   "DueDate":string,
   "PromiseDate":string,
   "EnableOurQty":boolean,
   "AttributeSetID":number,
   "AttributeShortDescription":string,
   "RevisionNum":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQVendListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   "OpenItem":boolean,
      /**   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  */  
   "Response":string,
      /**  RFQ number  that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point ID.  */  
   "PurPoint":string,
      /**  Supplier contact linked to this RFQ  */  
   "ConNum":number,
      /**  Can be "Web" or "Client"  */  
   "RespondVia":string,
      /**  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  */  
   "RespondDate":string,
      /**  Compliance Message  */  
   "ComplianceMsg":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "VendorID":string,
   "VendorName":string,
   "OpenRFQ":boolean,
   "LineDescription":string,
   "PartNum":string,
   "RevisionNum":string,
   "JobNum":string,
   "QuoteNum":number,
   "OpCode":string,
   "OpDescription":string,
   "ResponseDescription":string,
      /**  Vend Part Effective Date  */  
   "EffectiveDate":string,
      /**  Description of the Source field (either Job, Quote or blank)  */  
   "RFQSource":string,
   "RFQStatus":string,
      /**  Buyer Name  */  
   "BuyerID":string,
   "RFQDate":string,
   "RFQDueDate":string,
      /**  Our UOM  */  
   "OurUOM":string,
      /**  Supplier UOM  */  
   "SupplierUOM":string,
      /**  Base UOM Code from Part Master  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  */  
   "PUM":string,
   "CalcOurQty":number,
   "CalcVendQty":number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   "NotCompliant":boolean,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   "RFQLineLineDesc":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
   "AttributeSetID":number,
   "AttributeDescription":string,
   "AttributeShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQVendRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   "OpenItem":boolean,
      /**   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  */  
   "Response":string,
      /**  RFQ number  that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**  Vendor's unique internal number.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point ID.  */  
   "PurPoint":string,
      /**  Supplier contact linked to this RFQ  */  
   "ConNum":number,
      /**  Can be "Web" or "Client"  */  
   "RespondVia":string,
      /**  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  */  
   "RespondDate":string,
      /**  Compliance Message  */  
   "ComplianceMsg":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "VendorID":string,
   "VendorName":string,
   "OpenRFQ":boolean,
   "LineDescription":string,
   "PartNum":string,
   "RevisionNum":string,
   "JobNum":string,
   "QuoteNum":number,
   "OpCode":string,
   "OpDescription":string,
   "ResponseDescription":string,
      /**  Vend Part Effective Date  */  
   "EffectiveDate":string,
      /**  Description of the Source field (either Job, Quote or blank)  */  
   "RFQSource":string,
   "RFQStatus":string,
      /**  Buyer Name  */  
   "BuyerID":string,
   "RFQDate":string,
   "RFQDueDate":string,
      /**  Our UOM  */  
   "OurUOM":string,
      /**  Supplier UOM  */  
   "SupplierUOM":string,
      /**  Base UOM Code from Part Master  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  */  
   "PUM":string,
   "CalcOurQty":number,
   "CalcVendQty":number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   "NotCompliant":boolean,
   "Selected":boolean,
      /**  Supplier Address  */  
   "AddressFormatted":string,
      /**  Valid Response options for combo.  */  
   "ResponseOptions":string,
   "AttributeDescription":string,
   "AttributeSetID":number,
   "AttributeShortDescription":string,
   "BitFlag":number,
   "RFQLineLineDesc":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumName":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
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
export interface AvailableResponses_output{
parameters : {
      /**  output parameters  */  
   responseList:string,
}
}

   /** Required : 
      @param NewCalcOurQty
      @param ds
   */  
export interface ChangeDetailCalcOurQty_input{
      /**  New Quantity  */  
   NewCalcOurQty:number,
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface ChangeDetailCalcOurQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param NewCalcVendQty
      @param ds
   */  
export interface ChangeDetailCalcVendQty_input{
      /**  New Quantity  */  
   NewCalcVendQty:number,
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface ChangeDetailCalcVendQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckPOCreation_input{
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface CheckPOCreation_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
   vendMessage:string,
   vWarningMessage:string,
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CreatePO_input{
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface CreatePO_output{
parameters : {
      /**  output parameters  */  
   msgString:string,
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param rfQNum
      @param rfQLine
      @param vendorNum
      @param purPoint
   */  
export interface DeleteByID_input{
   rfQNum:number,
   rfQLine:number,
   vendorNum:number,
   purPoint:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_RFQLinesSelectedRow{
   Company:string,
   RFQNum:number,
   RFQLine:number,
   VendorNum:number,
   PurPoint:string,
   PartNum:string,
   CalcOurQty:number,
   CalcVendQty:number,
   IUM:string,
   LineDescription:string,
   OurUOM:string,
   PUM:string,
   DueDate:string,
   PromiseDate:string,
   EnableOurQty:boolean,
   AttributeSetID:number,
   AttributeShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQVendListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   OpenItem:boolean,
      /**   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  */  
   Response:string,
      /**  RFQ number  that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Vendor Purchase Point ID.  */  
   PurPoint:string,
      /**  Supplier contact linked to this RFQ  */  
   ConNum:number,
      /**  Can be "Web" or "Client"  */  
   RespondVia:string,
      /**  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  */  
   RespondDate:string,
      /**  Compliance Message  */  
   ComplianceMsg:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   VendorID:string,
   VendorName:string,
   OpenRFQ:boolean,
   LineDescription:string,
   PartNum:string,
   RevisionNum:string,
   JobNum:string,
   QuoteNum:number,
   OpCode:string,
   OpDescription:string,
   ResponseDescription:string,
      /**  Vend Part Effective Date  */  
   EffectiveDate:string,
      /**  Description of the Source field (either Job, Quote or blank)  */  
   RFQSource:string,
   RFQStatus:string,
      /**  Buyer Name  */  
   BuyerID:string,
   RFQDate:string,
   RFQDueDate:string,
      /**  Our UOM  */  
   OurUOM:string,
      /**  Supplier UOM  */  
   SupplierUOM:string,
      /**  Base UOM Code from Part Master  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  */  
   PUM:string,
   CalcOurQty:number,
   CalcVendQty:number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   NotCompliant:boolean,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   RFQLineLineDesc:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
   AttributeSetID:number,
   AttributeDescription:string,
   AttributeShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQVendListTableset{
   RFQVendList:Erp_Tablesets_RFQVendListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RFQVendRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  */  
   OpenItem:boolean,
      /**   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  */  
   Response:string,
      /**  RFQ number  that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Vendor Purchase Point ID.  */  
   PurPoint:string,
      /**  Supplier contact linked to this RFQ  */  
   ConNum:number,
      /**  Can be "Web" or "Client"  */  
   RespondVia:string,
      /**  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  */  
   RespondDate:string,
      /**  Compliance Message  */  
   ComplianceMsg:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   VendorID:string,
   VendorName:string,
   OpenRFQ:boolean,
   LineDescription:string,
   PartNum:string,
   RevisionNum:string,
   JobNum:string,
   QuoteNum:number,
   OpCode:string,
   OpDescription:string,
   ResponseDescription:string,
      /**  Vend Part Effective Date  */  
   EffectiveDate:string,
      /**  Description of the Source field (either Job, Quote or blank)  */  
   RFQSource:string,
   RFQStatus:string,
      /**  Buyer Name  */  
   BuyerID:string,
   RFQDate:string,
   RFQDueDate:string,
      /**  Our UOM  */  
   OurUOM:string,
      /**  Supplier UOM  */  
   SupplierUOM:string,
      /**  Base UOM Code from Part Master  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  */  
   PUM:string,
   CalcOurQty:number,
   CalcVendQty:number,
      /**  Indicates if the item on the line is not compliant on its source.  */  
   NotCompliant:boolean,
   Selected:boolean,
      /**  Supplier Address  */  
   AddressFormatted:string,
      /**  Valid Response options for combo.  */  
   ResponseOptions:string,
   AttributeDescription:string,
   AttributeSetID:number,
   AttributeShortDescription:string,
   BitFlag:number,
   RFQLineLineDesc:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQVendTableset{
   RFQVend:Erp_Tablesets_RFQVendRow[],
   RFQLinesSelected:Erp_Tablesets_RFQLinesSelectedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRFQVendTableset{
   RFQVend:Erp_Tablesets_RFQVendRow[],
   RFQLinesSelected:Erp_Tablesets_RFQLinesSelectedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param strRowsSelected
      @param ds
   */  
export interface FillRFQLinesSelected_input{
      /**  A RowId list of selected RFQVend records.  */  
   strRowsSelected:string,
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface FillRFQLinesSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param rfQNum
      @param rfQLine
      @param vendorNum
      @param purPoint
   */  
export interface GetByID_input{
   rfQNum:number,
   rfQLine:number,
   vendorNum:number,
   purPoint:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RFQVendTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RFQVendTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RFQVendTableset[],
}

   /** Required : 
      @param rfqNum
      @param rfqLine
      @param vendorNum
      @param purPoint
   */  
export interface GetLineQty_input{
      /**  RFQ Number  */  
   rfqNum:number,
      /**  RFQ Line Number  */  
   rfqLine:number,
      /**  Vendor Number  */  
   vendorNum:number,
      /**  Vendor Purchase Point  */  
   purPoint:string,
}

export interface GetLineQty_output{
parameters : {
      /**  output parameters  */  
   tmpLineQty:number,
   promptQty:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  Where clause for RFQVend table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_RFQVendListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
   returnObj:Erp_Tablesets_RFQVendListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rfQNum
      @param rfQLine
      @param vendorNum
   */  
export interface GetNewRFQVend_input{
   ds:Erp_Tablesets_RFQVendTableset[],
   rfQNum:number,
   rfQLine:number,
   vendorNum:number,
}

export interface GetNewRFQVend_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param company
      @param vendN
      @param dateRange
      @param openItem
      @param pageSize
      @param absolutePage
   */  
export interface GetRFQsForSupplierTracker_input{
      /**  Current company.  */  
   company:string,
      /**  Current vendor number.  */  
   vendN:number,
      /**  Current Transaction Date Range.  */  
   dateRange:string,
      /**  Current tab selected: All / Open / Closed.  */  
   openItem:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRFQsForSupplierTracker_output{
   returnObj:Erp_Tablesets_RFQVendTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRFQVend
      @param whereClauseRFQLinesSelected
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRFQVend:string,
   whereClauseRFQLinesSelected:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RFQVendTableset[],
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
      @param whereClause
      @param pageSize
      @param absolutePage
      @param rfqSourcein
      @param rfqStatusin
      @param rfqNum
      @param vendorId
   */  
export interface ListOfRFQVendWhereClauseVendor_input{
      /**  The full where clause  */  
   whereClause:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
      /**  If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.  */  
   rfqSourcein:string,
      /**  If "all'  -> input 'A', if 'closed' -> input 'C', if "open" -> input 'O'.  */  
   rfqStatusin:string,
      /**  The RFQ to filter the list by  */  
   rfqNum:number,
   vendorId:string,
}

export interface ListOfRFQVendWhereClauseVendor_output{
   returnObj:Erp_Tablesets_RFQVendListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param rfqSourcein
      @param rfqStatusin
      @param rfqNum
   */  
export interface ListOfRFQVendWhereClause_input{
      /**  The full where clause  */  
   whereClause:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
      /**  If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.  */  
   rfqSourcein:string,
      /**  If "all'  -> input 'A', if 'closed' -> input 'C', if "open" -> input 'O'.  */  
   rfqStatusin:string,
      /**  The RFQ to filter the list by  */  
   rfqNum:number,
}

export interface ListOfRFQVendWhereClause_output{
   returnObj:Erp_Tablesets_RFQVendListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param rfqSourcein
      @param rfqStatusin
   */  
export interface ListOfRFQVend_input{
      /**  Where clause to filter the query results.  */  
   whereClause:string,
      /**  page size.  */  
   pageSize:number,
      /**  absolute page  */  
   absolutePage:number,
      /**  If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.  */  
   rfqSourcein:string,
      /**  If "all'  -> input 'A', if 'closed' -> input 'C', if "open" -> input 'O'.  */  
   rfqStatusin:string,
}

export interface ListOfRFQVend_output{
   returnObj:Erp_Tablesets_RFQVendListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshDataset_input{
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface RefreshDataset_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQVendTableset,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param rfqSourcein
      @param rfqStatusin
   */  
export interface RowsOfRFQVend_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
   rfqSourcein:string,
   rfqStatusin:string,
}

export interface RowsOfRFQVend_output{
   returnObj:Erp_Tablesets_RFQVendTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtRFQVendTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRFQVendTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RFQVendTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQVendTableset,
}
}

