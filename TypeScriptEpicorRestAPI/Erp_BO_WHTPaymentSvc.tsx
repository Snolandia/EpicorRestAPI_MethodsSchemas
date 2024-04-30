import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.WHTPaymentSvc
// Description: Withholding Tax Payment Report BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/$metadata", {
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
   Description: Get WHTPayments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WHTPayments
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentHeadRow
   */  
export function get_WHTPayments(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WHTPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WHTPayments(requestBody:Erp_Tablesets_WHTPaymentHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments", {
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
   Summary: Calls GetByID to retrieve the WHTPayment item
   Description: Calls GetByID to retrieve the WHTPayment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPayment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
   */  
export function get_WHTPayments_Company_ReportID(Company:string, ReportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WHTPaymentHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")", {
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
         resolve(data as Erp_Tablesets_WHTPaymentHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WHTPayment for the service
   Description: Calls UpdateExt to update WHTPayment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WHTPayment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WHTPayments_Company_ReportID(Company:string, ReportID:string, requestBody:Erp_Tablesets_WHTPaymentHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")", {
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
   Summary: Call UpdateExt to delete WHTPayment item
   Description: Call UpdateExt to delete WHTPayment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WHTPayment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WHTPayments_Company_ReportID(Company:string, ReportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")", {
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
   Description: Get WHTPaymentDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WHTPaymentDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentDtlRow
   */  
export function get_WHTPayments_Company_ReportID_WHTPaymentDtls(Company:string, ReportID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")/WHTPaymentDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WHTPaymentDtl item
   Description: Calls GetByID to retrieve the WHTPaymentDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   */  
export function get_WHTPayments_Company_ReportID_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company:string, ReportID:string, TranDate:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WHTPaymentDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")", {
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
         resolve(data as Erp_Tablesets_WHTPaymentDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get WHTPaymentDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WHTPaymentDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentDtlRow
   */  
export function get_WHTPaymentDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WHTPaymentDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WHTPaymentDtls(requestBody:Erp_Tablesets_WHTPaymentDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls", {
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
   Summary: Calls GetByID to retrieve the WHTPaymentDtl item
   Description: Calls GetByID to retrieve the WHTPaymentDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   */  
export function get_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company:string, ReportID:string, TranDate:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WHTPaymentDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")", {
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
         resolve(data as Erp_Tablesets_WHTPaymentDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WHTPaymentDtl for the service
   Description: Calls UpdateExt to update WHTPaymentDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WHTPaymentDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company:string, ReportID:string, TranDate:string, TranNum:string, requestBody:Erp_Tablesets_WHTPaymentDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete WHTPaymentDtl item
   Description: Call UpdateExt to delete WHTPaymentDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WHTPaymentDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company:string, ReportID:string, TranDate:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadListRow)
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
export function get_GetRows(whereClauseWHTPaymentHead:string, whereClauseWHTPaymentDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseWHTPaymentHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWHTPaymentHead=" + whereClauseWHTPaymentHead
   }
   if(typeof whereClauseWHTPaymentDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWHTPaymentDtl=" + whereClauseWHTPaymentDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(reportID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reportID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reportID=" + reportID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetList" + params, {
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
   Summary: Invoke method OnChangeBankAcctID
   Description: Call this method when the user changes the Bank Account.
   OperationID: OnChangeBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankAcctID(requestBody:OnChangeBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/OnChangeBankAcctID", {
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
         resolve(data as OnChangeBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaxCode
   Description: Call this method when the user changes the Tax Code.
   OperationID: OnChangeTaxCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaxCode(requestBody:OnChangeTaxCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaxCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/OnChangeTaxCode", {
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
         resolve(data as OnChangeTaxCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWHTaxRecords
   Description: This method get Withholding Tax Records for specific period
   OperationID: GetWHTaxRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWHTaxRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWHTaxRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWHTaxRecords(requestBody:GetWHTaxRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWHTaxRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetWHTaxRecords", {
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
         resolve(data as GetWHTaxRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveUnPaidWHTaxRecords
   Description: This method remove UnPaid Withholding Tax Records from the report
   OperationID: RemoveUnPaidWHTaxRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveUnPaidWHTaxRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveUnPaidWHTaxRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveUnPaidWHTaxRecords(requestBody:RemoveUnPaidWHTaxRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveUnPaidWHTaxRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/RemoveUnPaidWHTaxRecords", {
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
         resolve(data as RemoveUnPaidWHTaxRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveSelectedWHTaxRecords
   Description: This method remove selected Withholding Tax Records from the report
   OperationID: RemoveSelectedWHTaxRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveSelectedWHTaxRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSelectedWHTaxRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveSelectedWHTaxRecords(requestBody:RemoveSelectedWHTaxRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveSelectedWHTaxRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/RemoveSelectedWHTaxRecords", {
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
         resolve(data as RemoveSelectedWHTaxRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWHTPaymentAPInvData
   Description: Get submitted withholding tax reports linked to specific AP Invoice.
   OperationID: GetWHTPaymentAPInvData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWHTPaymentAPInvData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWHTPaymentAPInvData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWHTPaymentAPInvData(requestBody:GetWHTPaymentAPInvData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWHTPaymentAPInvData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetWHTPaymentAPInvData", {
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
         resolve(data as GetWHTPaymentAPInvData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewWHTPaymentHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWHTPaymentHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewWHTPaymentHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWHTPaymentHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWHTPaymentHead(requestBody:GetNewWHTPaymentHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewWHTPaymentHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetNewWHTPaymentHead", {
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
         resolve(data as GetNewWHTPaymentHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewWHTPaymentDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWHTPaymentDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewWHTPaymentDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWHTPaymentDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWHTPaymentDtl(requestBody:GetNewWHTPaymentDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewWHTPaymentDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetNewWHTPaymentDtl", {
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
         resolve(data as GetNewWHTPaymentDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WHTPaymentDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WHTPaymentHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WHTPaymentHeadRow,
}

export interface Erp_Tablesets_WHTPaymentDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  WHT Report ID.  */  
   "ReportID":string,
      /**  TranDate from Erp.TaxTran table.  */  
   "TranDate":string,
      /**  TranNum from Erp.TaxTran table.  */  
   "TranNum":number,
      /**  Whether the tax line is paid to government.  */  
   "IsPaid":boolean,
      /**  Tax Line comment.  */  
   "Notes":string,
      /**  The user who added the line to report.  */  
   "CreatedBy":string,
      /**  The date and time of adding.  */  
   "CreatedOn":string,
      /**  The last user who changed the report line.  */  
   "ChangedBy":string,
      /**  The date and time of last changing.  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Transaction belongs to Invoice.  */  
   "IsInvoice":boolean,
      /**  Transaction belongs to Debit Memo.  */  
   "IsDM":boolean,
      /**  Transaction belongs to Credit Memo.  */  
   "IsCM":boolean,
      /**  Transaction belongs to Correction Invoice.  */  
   "IsCorrection":boolean,
      /**  Transaction belongs to Payment.  */  
   "IsPayment":boolean,
      /**  Customer/Supplier ID.  */  
   "PartyID":string,
      /**  Customer/Supplier Name.  */  
   "PartyName":string,
      /**  Customer/Supplier PAN Number.  */  
   "PartyPAN":string,
      /**  Customer/Supplier Tax Entity Type.  */  
   "PartyTaxEntityType":string,
      /**  Invoice/Payment Number.  */  
   "DocumentNum":string,
      /**  Invoice/Payment Date.  */  
   "DocumentDate":string,
      /**  Invoice/Payment Description.  */  
   "DocumentDescription":string,
      /**  Invoice/Payment Legal Number.  */  
   "DocumentLN":string,
      /**  Invoice/Payment Document Amount.  */  
   "DocumentAmt":number,
      /**  Document type name.  */  
   "DocumentTypeName":string,
      /**  Invoice Pre-Payment check number.  */  
   "BoENumber":string,
      /**  Transaction Apply Date.  */  
   "ApplyDate":string,
      /**  Transaction Tax Point Date.  */  
   "TaxPoint":string,
      /**  Transaction Tax Rate Percent.  */  
   "TaxRatePercent":number,
      /**  Transaction Taxable Amount.  */  
   "TaxableAmt":number,
      /**  Transaction Tax Amount.  */  
   "TaxAmt":number,
      /**  Transaction Tax Liability Code.  */  
   "TaxRegionCode":string,
      /**  Transaction Tax Liability Description.  */  
   "TaxRegionDescription":string,
      /**  Transaction Tax Type ID.  */  
   "TaxTypeCode":string,
      /**  Transaction Tax Type Description.  */  
   "TaxTypeDescription":string,
      /**  Transaction Tax Type Legal Text Code.  */  
   "TaxTextCode":string,
      /**  Transaction Tax Type Legal Text.  */  
   "TaxTextDescription":string,
      /**  Transaction Tax Type Report Category Code.  */  
   "TaxRptCatCode":string,
      /**  Transaction Tax Type Report Category Description.  */  
   "TaxRptCatDescription":string,
      /**  Transaction selected.  */  
   "Selected":boolean,
      /**  Customer/Supplier Number.  */  
   "PartyNum":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WHTPaymentHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  WHT Report ID.  */  
   "ReportID":string,
      /**  Start date of the report period.  */  
   "StartDate":string,
      /**  End date of the report period.  */  
   "EndDate":string,
      /**  Report Description.  */  
   "Description":string,
      /**  Report date.  */  
   "ReportDate":string,
      /**  Module AR or AP.  */  
   "Module":string,
      /**  Tax Entity Type.  */  
   "TaxEntityType":string,
      /**  The amount of WHT paid to the government.  */  
   "WHTPaymentAmount":number,
      /**  Unique identifier of the bank account.  */  
   "BankAcctID":string,
      /**  Bank receipt number.  */  
   "ReceiptNumber":string,
      /**  Bank receipt date.  */  
   "ReceiptDate":string,
      /**  Bank transaction reference number (BSR Code).  */  
   "BankTranRefNum":string,
      /**  Report payment date.  */  
   "PaymentDate":string,
      /**  Cheque Number  */  
   "ChequeNumber":string,
      /**  Cheque or ECS Date  */  
   "ChequeDate":string,
      /**  Additional transaction reference (ECS).  */  
   "AdditionalTranRef":string,
      /**  The user who submitted the report.  */  
   "SubmittedBy":string,
      /**  The date and time of submitting.  */  
   "SubmittedOn":string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   "ReportStatus":number,
      /**  The charge paid for late filing of the tax returns.  */  
   "LatePaymentCharge":number,
      /**  Nature of Remittance.  */  
   "NatureOfRemittance":string,
      /**  Tax Type ID.  */  
   "TaxCode":string,
      /**  Submitted Report ID.  */  
   "SubmitReportID":string,
      /**  The user who created the report.  */  
   "CreatedBy":string,
      /**  The date and time of creating.  */  
   "CreatedOn":string,
      /**  The last user who changed the report.  */  
   "ChangedBy":string,
      /**  The date and time of last changing.  */  
   "ChangedOn":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Penalty amount.  */  
   "PenaltyAmount":number,
      /**  Report was submitted or not.  */  
   "IsSubmitted":boolean,
      /**  Report is closed for changing or not.  */  
   "IsClosed":boolean,
      /**  Mark report to ready for submitting.  */  
   "IsReady":boolean,
      /**  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  */  
   "TotalPaymentAmt":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WHTPaymentHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  WHT Report ID.  */  
   "ReportID":string,
      /**  Start date of the report period.  */  
   "StartDate":string,
      /**  End date of the report period.  */  
   "EndDate":string,
      /**  Report Description.  */  
   "Description":string,
      /**  Report date.  */  
   "ReportDate":string,
      /**  Module AR or AP.  */  
   "Module":string,
      /**  Tax Entity Type.  */  
   "TaxEntityType":string,
      /**  The amount of WHT paid to the government.  */  
   "WHTPaymentAmount":number,
      /**  Unique identifier of the bank account.  */  
   "BankAcctID":string,
      /**  Bank receipt number.  */  
   "ReceiptNumber":string,
      /**  Bank receipt date.  */  
   "ReceiptDate":string,
      /**  Bank transaction reference number (BSR Code).  */  
   "BankTranRefNum":string,
      /**  Report payment date.  */  
   "PaymentDate":string,
      /**  Cheque Number  */  
   "ChequeNumber":string,
      /**  Cheque or ECS Date  */  
   "ChequeDate":string,
      /**  Additional transaction reference (ECS).  */  
   "AdditionalTranRef":string,
      /**  The user who submitted the report.  */  
   "SubmittedBy":string,
      /**  The date and time of submitting.  */  
   "SubmittedOn":string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   "ReportStatus":number,
      /**  Report comment.  */  
   "Notes":string,
      /**  The charge paid for late filing of the tax returns.  */  
   "LatePaymentCharge":number,
      /**  Nature of Remittance.  */  
   "NatureOfRemittance":string,
      /**  Customer filter.  */  
   "CustomerList":string,
      /**  Supplier filter.  */  
   "SupplierList":string,
      /**  Tax Type ID.  */  
   "TaxCode":string,
      /**  Tax Liability filter.  */  
   "TaxLiabilityList":string,
      /**  Submitted Report ID.  */  
   "SubmitReportID":string,
      /**  The user who created the report.  */  
   "CreatedBy":string,
      /**  The date and time of creating.  */  
   "CreatedOn":string,
      /**  The last user who changed the report.  */  
   "ChangedBy":string,
      /**  The date and time of last changing.  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Penalty amount.  */  
   "PenaltyAmount":number,
      /**  Currency Symbol of base Currency.  */  
   "BaseCurrSymbol":string,
      /**  Main Book ID.  */  
   "BookID":string,
      /**  Report is closed for changing or not.  */  
   "IsClosed":boolean,
      /**  Mark report to ready for submitting.  */  
   "IsReady":boolean,
      /**  Report was submitted or not.  */  
   "IsSubmitted":boolean,
      /**  Report Lines total amount.  */  
   "LineTotalAmt":number,
      /**  Select/Deselect all detail rows.  */  
   "SelectAll":boolean,
      /**  Tax Type description.  */  
   "TaxCodeDescription":string,
      /**  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  */  
   "TotalPaymentAmt":number,
      /**  Currency Code of base Currency.  */  
   "BaseCurrCode":string,
      /**  Currency ID of base Currency.  */  
   "BaseCurrID":string,
   "BitFlag":number,
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
   /** Required : 
      @param reportID
   */  
export interface DeleteByID_input{
   reportID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtWHTPaymentTableset{
   WHTPaymentHead:Erp_Tablesets_WHTPaymentHeadRow[],
   WHTPaymentDtl:Erp_Tablesets_WHTPaymentDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WHTPaymentDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  WHT Report ID.  */  
   ReportID:string,
      /**  TranDate from Erp.TaxTran table.  */  
   TranDate:string,
      /**  TranNum from Erp.TaxTran table.  */  
   TranNum:number,
      /**  Whether the tax line is paid to government.  */  
   IsPaid:boolean,
      /**  Tax Line comment.  */  
   Notes:string,
      /**  The user who added the line to report.  */  
   CreatedBy:string,
      /**  The date and time of adding.  */  
   CreatedOn:string,
      /**  The last user who changed the report line.  */  
   ChangedBy:string,
      /**  The date and time of last changing.  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Transaction belongs to Invoice.  */  
   IsInvoice:boolean,
      /**  Transaction belongs to Debit Memo.  */  
   IsDM:boolean,
      /**  Transaction belongs to Credit Memo.  */  
   IsCM:boolean,
      /**  Transaction belongs to Correction Invoice.  */  
   IsCorrection:boolean,
      /**  Transaction belongs to Payment.  */  
   IsPayment:boolean,
      /**  Customer/Supplier ID.  */  
   PartyID:string,
      /**  Customer/Supplier Name.  */  
   PartyName:string,
      /**  Customer/Supplier PAN Number.  */  
   PartyPAN:string,
      /**  Customer/Supplier Tax Entity Type.  */  
   PartyTaxEntityType:string,
      /**  Invoice/Payment Number.  */  
   DocumentNum:string,
      /**  Invoice/Payment Date.  */  
   DocumentDate:string,
      /**  Invoice/Payment Description.  */  
   DocumentDescription:string,
      /**  Invoice/Payment Legal Number.  */  
   DocumentLN:string,
      /**  Invoice/Payment Document Amount.  */  
   DocumentAmt:number,
      /**  Document type name.  */  
   DocumentTypeName:string,
      /**  Invoice Pre-Payment check number.  */  
   BoENumber:string,
      /**  Transaction Apply Date.  */  
   ApplyDate:string,
      /**  Transaction Tax Point Date.  */  
   TaxPoint:string,
      /**  Transaction Tax Rate Percent.  */  
   TaxRatePercent:number,
      /**  Transaction Taxable Amount.  */  
   TaxableAmt:number,
      /**  Transaction Tax Amount.  */  
   TaxAmt:number,
      /**  Transaction Tax Liability Code.  */  
   TaxRegionCode:string,
      /**  Transaction Tax Liability Description.  */  
   TaxRegionDescription:string,
      /**  Transaction Tax Type ID.  */  
   TaxTypeCode:string,
      /**  Transaction Tax Type Description.  */  
   TaxTypeDescription:string,
      /**  Transaction Tax Type Legal Text Code.  */  
   TaxTextCode:string,
      /**  Transaction Tax Type Legal Text.  */  
   TaxTextDescription:string,
      /**  Transaction Tax Type Report Category Code.  */  
   TaxRptCatCode:string,
      /**  Transaction Tax Type Report Category Description.  */  
   TaxRptCatDescription:string,
      /**  Transaction selected.  */  
   Selected:boolean,
      /**  Customer/Supplier Number.  */  
   PartyNum:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WHTPaymentHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  WHT Report ID.  */  
   ReportID:string,
      /**  Start date of the report period.  */  
   StartDate:string,
      /**  End date of the report period.  */  
   EndDate:string,
      /**  Report Description.  */  
   Description:string,
      /**  Report date.  */  
   ReportDate:string,
      /**  Module AR or AP.  */  
   Module:string,
      /**  Tax Entity Type.  */  
   TaxEntityType:string,
      /**  The amount of WHT paid to the government.  */  
   WHTPaymentAmount:number,
      /**  Unique identifier of the bank account.  */  
   BankAcctID:string,
      /**  Bank receipt number.  */  
   ReceiptNumber:string,
      /**  Bank receipt date.  */  
   ReceiptDate:string,
      /**  Bank transaction reference number (BSR Code).  */  
   BankTranRefNum:string,
      /**  Report payment date.  */  
   PaymentDate:string,
      /**  Cheque Number  */  
   ChequeNumber:string,
      /**  Cheque or ECS Date  */  
   ChequeDate:string,
      /**  Additional transaction reference (ECS).  */  
   AdditionalTranRef:string,
      /**  The user who submitted the report.  */  
   SubmittedBy:string,
      /**  The date and time of submitting.  */  
   SubmittedOn:string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   ReportStatus:number,
      /**  The charge paid for late filing of the tax returns.  */  
   LatePaymentCharge:number,
      /**  Nature of Remittance.  */  
   NatureOfRemittance:string,
      /**  Tax Type ID.  */  
   TaxCode:string,
      /**  Submitted Report ID.  */  
   SubmitReportID:string,
      /**  The user who created the report.  */  
   CreatedBy:string,
      /**  The date and time of creating.  */  
   CreatedOn:string,
      /**  The last user who changed the report.  */  
   ChangedBy:string,
      /**  The date and time of last changing.  */  
   ChangedOn:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Penalty amount.  */  
   PenaltyAmount:number,
      /**  Report was submitted or not.  */  
   IsSubmitted:boolean,
      /**  Report is closed for changing or not.  */  
   IsClosed:boolean,
      /**  Mark report to ready for submitting.  */  
   IsReady:boolean,
      /**  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  */  
   TotalPaymentAmt:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WHTPaymentHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  WHT Report ID.  */  
   ReportID:string,
      /**  Start date of the report period.  */  
   StartDate:string,
      /**  End date of the report period.  */  
   EndDate:string,
      /**  Report Description.  */  
   Description:string,
      /**  Report date.  */  
   ReportDate:string,
      /**  Module AR or AP.  */  
   Module:string,
      /**  Tax Entity Type.  */  
   TaxEntityType:string,
      /**  The amount of WHT paid to the government.  */  
   WHTPaymentAmount:number,
      /**  Unique identifier of the bank account.  */  
   BankAcctID:string,
      /**  Bank receipt number.  */  
   ReceiptNumber:string,
      /**  Bank receipt date.  */  
   ReceiptDate:string,
      /**  Bank transaction reference number (BSR Code).  */  
   BankTranRefNum:string,
      /**  Report payment date.  */  
   PaymentDate:string,
      /**  Cheque Number  */  
   ChequeNumber:string,
      /**  Cheque or ECS Date  */  
   ChequeDate:string,
      /**  Additional transaction reference (ECS).  */  
   AdditionalTranRef:string,
      /**  The user who submitted the report.  */  
   SubmittedBy:string,
      /**  The date and time of submitting.  */  
   SubmittedOn:string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   ReportStatus:number,
      /**  Report comment.  */  
   Notes:string,
      /**  The charge paid for late filing of the tax returns.  */  
   LatePaymentCharge:number,
      /**  Nature of Remittance.  */  
   NatureOfRemittance:string,
      /**  Customer filter.  */  
   CustomerList:string,
      /**  Supplier filter.  */  
   SupplierList:string,
      /**  Tax Type ID.  */  
   TaxCode:string,
      /**  Tax Liability filter.  */  
   TaxLiabilityList:string,
      /**  Submitted Report ID.  */  
   SubmitReportID:string,
      /**  The user who created the report.  */  
   CreatedBy:string,
      /**  The date and time of creating.  */  
   CreatedOn:string,
      /**  The last user who changed the report.  */  
   ChangedBy:string,
      /**  The date and time of last changing.  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Penalty amount.  */  
   PenaltyAmount:number,
      /**  Currency Symbol of base Currency.  */  
   BaseCurrSymbol:string,
      /**  Main Book ID.  */  
   BookID:string,
      /**  Report is closed for changing or not.  */  
   IsClosed:boolean,
      /**  Mark report to ready for submitting.  */  
   IsReady:boolean,
      /**  Report was submitted or not.  */  
   IsSubmitted:boolean,
      /**  Report Lines total amount.  */  
   LineTotalAmt:number,
      /**  Select/Deselect all detail rows.  */  
   SelectAll:boolean,
      /**  Tax Type description.  */  
   TaxCodeDescription:string,
      /**  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  */  
   TotalPaymentAmt:number,
      /**  Currency Code of base Currency.  */  
   BaseCurrCode:string,
      /**  Currency ID of base Currency.  */  
   BaseCurrID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WHTPaymentInvDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  WHT Report ID.  */  
   ReportID:string,
      /**  Start date of the report period.  */  
   StartDate:string,
      /**  End date of the report period.  */  
   EndDate:string,
      /**  Report Description.  */  
   Description:string,
      /**  Tax Entity Type.  */  
   TaxEntityType:string,
      /**  Unique identifier of the bank account.  */  
   BankAcctID:string,
      /**  Bank receipt number.  */  
   ReceiptNumber:string,
      /**  Bank receipt date.  */  
   ReceiptDate:string,
      /**  Bank transaction reference number (BSR Code).  */  
   BankTranRefNum:string,
      /**  Report payment date.  */  
   PaymentDate:string,
      /**  Cheque Number  */  
   ChequeNumber:string,
      /**  Cheque or ECS Date  */  
   ChequeDate:string,
      /**  Additional transaction reference (ECS).  */  
   AdditionalTranRef:string,
      /**  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  */  
   ReportStatus:number,
      /**  Nature of Remittance.  */  
   NatureOfRemittance:string,
      /**  Tax Type ID.  */  
   TaxCode:string,
      /**  Submitted Report ID.  */  
   SubmitReportID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Transaction Taxable Amount.  */  
   TaxableAmt:number,
      /**  Transaction Tax Amount.  */  
   TaxAmt:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WHTPaymentInvDtlTableset{
   WHTPaymentInvDtl:Erp_Tablesets_WHTPaymentInvDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WHTPaymentListTableset{
   WHTPaymentHeadList:Erp_Tablesets_WHTPaymentHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WHTPaymentTableset{
   WHTPaymentHead:Erp_Tablesets_WHTPaymentHeadRow[],
   WHTPaymentDtl:Erp_Tablesets_WHTPaymentDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reportID
   */  
export interface GetByID_input{
   reportID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
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
   returnObj:Erp_Tablesets_WHTPaymentListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param reportID
      @param tranDate
   */  
export interface GetNewWHTPaymentDtl_input{
   ds:Erp_Tablesets_WHTPaymentTableset[],
   reportID:string,
   tranDate:string,
}

export interface GetNewWHTPaymentDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewWHTPaymentHead_input{
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface GetNewWHTPaymentHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentTableset,
}
}

   /** Required : 
      @param whereClauseWHTPaymentHead
      @param whereClauseWHTPaymentDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseWHTPaymentHead:string,
   whereClauseWHTPaymentDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
   */  
export interface GetWHTPaymentAPInvData_input{
      /**  The Vendor Number  */  
   vendorNum:number,
      /**  The AP Invoice Number  */  
   invoiceNum:string,
}

export interface GetWHTPaymentAPInvData_output{
   returnObj:Erp_Tablesets_WHTPaymentInvDtlTableset[],
}

   /** Required : 
      @param reportID
      @param ds
   */  
export interface GetWHTaxRecords_input{
      /**  WHT Report ID  */  
   reportID:string,
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface GetWHTaxRecords_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentTableset,
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
      @param bankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
      /**  The proposed value of BankAcctID  */  
   bankAcctID:string,
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentTableset,
}
}

   /** Required : 
      @param taxCode
      @param ds
   */  
export interface OnChangeTaxCode_input{
      /**  The proposed value of TaxCode  */  
   taxCode:string,
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface OnChangeTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface RemoveSelectedWHTaxRecords_input{
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface RemoveSelectedWHTaxRecords_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
}

   /** Required : 
      @param ds
   */  
export interface RemoveUnPaidWHTaxRecords_input{
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface RemoveUnPaidWHTaxRecords_output{
   returnObj:Erp_Tablesets_WHTPaymentTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtWHTPaymentTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtWHTPaymentTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_WHTPaymentTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WHTPaymentTableset,
}
}

