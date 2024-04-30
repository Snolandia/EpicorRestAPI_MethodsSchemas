import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ReqSvc
// Description: Requisition Entry Business object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/$metadata", {
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
   Description: Get Reqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Reqs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadRow
   */  
export function get_Reqs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Reqs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ReqHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Reqs(requestBody:Erp_Tablesets_ReqHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs", {
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
   Summary: Calls GetByID to retrieve the Req item
   Description: Calls GetByID to retrieve the Req item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Req
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqHeadRow
   */  
export function get_Reqs_Company_ReqNum(Company:string, ReqNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")", {
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
         resolve(data as Erp_Tablesets_ReqHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Req for the service
   Description: Calls UpdateExt to update Req. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Req
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Reqs_Company_ReqNum(Company:string, ReqNum:string, requestBody:Erp_Tablesets_ReqHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")", {
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
   Summary: Call UpdateExt to delete Req item
   Description: Call UpdateExt to delete Req item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Req
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Reqs_Company_ReqNum(Company:string, ReqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")", {
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
   Description: Get ReqDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReqDetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailRow
   */  
export function get_Reqs_Company_ReqNum_ReqDetails(Company:string, ReqNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqDetails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReqDetail item
   Description: Calls GetByID to retrieve the ReqDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqDetailRow
   */  
export function get_Reqs_Company_ReqNum_ReqDetails_Company_ReqNum_ReqLine(Company:string, ReqNum:string, ReqLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")", {
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
         resolve(data as Erp_Tablesets_ReqDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ReqHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReqHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadAttchRow
   */  
export function get_Reqs_Company_ReqNum_ReqHeadAttches(Company:string, ReqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReqHeadAttch item
   Description: Calls GetByID to retrieve the ReqHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   */  
export function get_Reqs_Company_ReqNum_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company:string, ReqNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ReqHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ReqDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReqDetails
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailRow
   */  
export function get_ReqDetails(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReqDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ReqDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReqDetails(requestBody:Erp_Tablesets_ReqDetailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails", {
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
   Summary: Calls GetByID to retrieve the ReqDetail item
   Description: Calls GetByID to retrieve the ReqDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqDetailRow
   */  
export function get_ReqDetails_Company_ReqNum_ReqLine(Company:string, ReqNum:string, ReqLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")", {
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
         resolve(data as Erp_Tablesets_ReqDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReqDetail for the service
   Description: Calls UpdateExt to update ReqDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReqDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReqDetails_Company_ReqNum_ReqLine(Company:string, ReqNum:string, ReqLine:string, requestBody:Erp_Tablesets_ReqDetailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")", {
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
   Summary: Call UpdateExt to delete ReqDetail item
   Description: Call UpdateExt to delete ReqDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReqDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReqDetails_Company_ReqNum_ReqLine(Company:string, ReqNum:string, ReqLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")", {
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
   Description: Get ReqDetailAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReqDetailAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailAttchRow
   */  
export function get_ReqDetails_Company_ReqNum_ReqLine_ReqDetailAttches(Company:string, ReqNum:string, ReqLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")/ReqDetailAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReqDetailAttch item
   Description: Calls GetByID to retrieve the ReqDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetailAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   */  
export function get_ReqDetails_Company_ReqNum_ReqLine_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company:string, ReqNum:string, ReqLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ReqDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ReqDetailAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReqDetailAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailAttchRow
   */  
export function get_ReqDetailAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReqDetailAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ReqDetailAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReqDetailAttches(requestBody:Erp_Tablesets_ReqDetailAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches", {
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
   Summary: Calls GetByID to retrieve the ReqDetailAttch item
   Description: Calls GetByID to retrieve the ReqDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   */  
export function get_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company:string, ReqNum:string, ReqLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqDetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ReqDetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReqDetailAttch for the service
   Description: Calls UpdateExt to update ReqDetailAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReqDetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company:string, ReqNum:string, ReqLine:string, DrawingSeq:string, requestBody:Erp_Tablesets_ReqDetailAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ReqDetailAttch item
   Description: Call UpdateExt to delete ReqDetailAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReqDetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param ReqLine Desc: ReqLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company:string, ReqNum:string, ReqLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")", {
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
   Description: Get ReqHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReqHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadAttchRow
   */  
export function get_ReqHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReqHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ReqHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReqHeadAttches(requestBody:Erp_Tablesets_ReqHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches", {
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
   Summary: Calls GetByID to retrieve the ReqHeadAttch item
   Description: Calls GetByID to retrieve the ReqHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   */  
export function get_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company:string, ReqNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ReqHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_ReqHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReqHeadAttch for the service
   Description: Calls UpdateExt to update ReqHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReqHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company:string, ReqNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_ReqHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete ReqHeadAttch item
   Description: Call UpdateExt to delete ReqHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReqHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReqNum Desc: ReqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company:string, ReqNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadListRow)
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
export function get_GetRows(whereClauseReqHead:string, whereClauseReqHeadAttch:string, whereClauseReqDetail:string, whereClauseReqDetailAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseReqHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReqHead=" + whereClauseReqHead
   }
   if(typeof whereClauseReqHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReqHeadAttch=" + whereClauseReqHeadAttch
   }
   if(typeof whereClauseReqDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReqDetail=" + whereClauseReqDetail
   }
   if(typeof whereClauseReqDetailAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReqDetailAttch=" + whereClauseReqDetailAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetRows" + params, {
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
export function get_GetByID(reqNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reqNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reqNum=" + reqNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetList" + params, {
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
   Summary: Invoke method BuildNextDispatcher
   Description: This methods builds next Dispatcher. Returns list of user
ids and list of user names.
   OperationID: BuildNextDispatcher
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildNextDispatcher_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildNextDispatcher_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildNextDispatcher(requestBody:BuildNextDispatcher_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildNextDispatcher_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/BuildNextDispatcher", {
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
         resolve(data as BuildNextDispatcher_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildNextDispatcher_SingleList
   Description: Build list of Dispatcher Ids.
   OperationID: BuildNextDispatcher_SingleList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildNextDispatcher_SingleList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildNextDispatcher_SingleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildNextDispatcher_SingleList(requestBody:BuildNextDispatcher_SingleList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildNextDispatcher_SingleList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/BuildNextDispatcher_SingleList", {
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
         resolve(data as BuildNextDispatcher_SingleList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildReqActionsList
   Description: Build list of Requisition Actions.
   OperationID: BuildReqActionsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildReqActionsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildReqActionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildReqActionsList(requestBody:BuildReqActionsList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildReqActionsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/BuildReqActionsList", {
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
         resolve(data as BuildReqActionsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckJobNum
   Description: This method checks to see if the proposed Job Number is a valid Job
   OperationID: CheckJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckJobNum(requestBody:CheckJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CheckJobNum", {
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
         resolve(data as CheckJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPartStatus
   Description: Perform Part Inactive, Obsolete, Runout validation.
   OperationID: CheckPartStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPartStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartStatus(requestBody:CheckPartStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPartStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CheckPartStatus", {
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
         resolve(data as CheckPartStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseRequisition
   Description: This method closes Requisition.
   OperationID: CloseRequisition
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseRequisition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseRequisition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseRequisition(requestBody:CloseRequisition_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseRequisition_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CloseRequisition", {
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
         resolve(data as CloseRequisition_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteReqLog
   Description: This method deletes Requisition log with given type changedate and changetime.
   OperationID: DeleteReqLog
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteReqLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteReqLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteReqLog(requestBody:DeleteReqLog_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteReqLog_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/DeleteReqLog", {
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
         resolve(data as DeleteReqLog_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostInfo
   Description: This method sets Unit Cost and Extended Cost.
   OperationID: GetCostInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostInfo(requestBody:GetCostInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetCostInfo", {
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
         resolve(data as GetCostInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExchangeRate
   Description: This method gets the Exchange Rate by the given date.
   OperationID: GetExchangeRate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExchangeRate(requestBody:GetExchangeRate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExchangeRate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetExchangeRate", {
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
         resolve(data as GetExchangeRate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartCrossRef
   Description: This method defaults ShipDtl fields when the PartNum field changes
   OperationID: GetPartCrossRef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartCrossRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartCrossRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartCrossRef(requestBody:GetPartCrossRef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartCrossRef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetPartCrossRef", {
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
         resolve(data as GetPartCrossRef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartInfo
   Description: This method defaults ReqDetail part fields.
   OperationID: GetPartInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartInfo(requestBody:GetPartInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetPartInfo", {
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
         resolve(data as GetPartInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDetailOverridePriceList
   Description: Run this method when the override pricelist is unchecked
   OperationID: ChangeDetailOverridePriceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDetailOverridePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOverridePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailOverridePriceList(requestBody:ChangeDetailOverridePriceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDetailOverridePriceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeDetailOverridePriceList", {
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
         resolve(data as ChangeDetailOverridePriceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUnitPriceConfirmOverride
   Description: Checks if the source of the unit price is from a supplier price list, if so
will prompt for confirmation of overriding if flag is set against purchase configuration.
   OperationID: ChangeUnitPriceConfirmOverride
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUnitPriceConfirmOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPriceConfirmOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnitPriceConfirmOverride(requestBody:ChangeUnitPriceConfirmOverride_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUnitPriceConfirmOverride_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeUnitPriceConfirmOverride", {
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
         resolve(data as ChangeUnitPriceConfirmOverride_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMfgNum
   Description: Called when MfgNum is changed. Updates MfgNumName.
   OperationID: ChangeMfgNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMfgNum(requestBody:ChangeMfgNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMfgNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeMfgNum", {
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
         resolve(data as ChangeMfgNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMfgPartNum
   Description: Called when MfgNumPart is changed and need to retrieve Supplier Part
   OperationID: ChangeMfgPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMfgPartNum(requestBody:ChangeMfgPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMfgPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeMfgPartNum", {
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
         resolve(data as ChangeMfgPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartClass
   Description: Run this method when the part Class Changes.
   OperationID: ChangePartClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePartClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartClass(requestBody:ChangePartClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePartClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangePartClass", {
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
         resolve(data as ChangePartClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranType
   Description: Run this method when the Transaction Type Changes
   OperationID: ChangeTranType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranType(requestBody:ChangeTranType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTranType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeTranType", {
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
         resolve(data as ChangeTranType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQtyInfo
   Description: This method applies PurchasingFactor to Qties by given field
that was changed OrderQty or XOrderQty.
   OperationID: GetQtyInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQtyInfo(requestBody:GetQtyInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQtyInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetQtyInfo", {
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
         resolve(data as GetQtyInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/OnChangingAttributeSet", {
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
         resolve(data as OnChangingAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReqDetail
   Description: Validates Inactive Part Class and Checks for attribute tracked parts.
   OperationID: CheckReqDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckReqDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReqDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReqDetail(requestBody:CheckReqDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckReqDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CheckReqDetail", {
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
         resolve(data as CheckReqDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReqDetailAttributeSets
   Description: Checks for attribute tracked parts.
   OperationID: CheckReqDetailAttributeSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckReqDetailAttributeSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReqDetailAttributeSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReqDetailAttributeSets(requestBody:CheckReqDetailAttributeSets_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckReqDetailAttributeSets_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CheckReqDetailAttributeSets", {
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
         resolve(data as CheckReqDetailAttributeSets_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReqLogList
   Description: Public method to get the ReqLog dataset.
   OperationID: GetReqLogList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReqLogList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReqLogList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReqLogList(requestBody:GetReqLogList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReqLogList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetReqLogList", {
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
         resolve(data as GetReqLogList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVendorInfo
   Description: This method update Vendor related field.
   OperationID: GetVendorInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorInfo(requestBody:GetVendorInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVendorInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetVendorInfo", {
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
         resolve(data as GetVendorInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RDMenuFlags
   Description: returns flags indicating whether Reset Dispatching or
Dispatch Requisiton should be enabled or disabled
   OperationID: RDMenuFlags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RDMenuFlags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RDMenuFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RDMenuFlags(requestBody:RDMenuFlags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RDMenuFlags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/RDMenuFlags", {
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
         resolve(data as RDMenuFlags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetDispatching
   Description: This method resets Dispatching.
UI needs to ask before running method "WARNING: This will delete
all entries in the action log and delete all previous Dispatching steps.
Do you wish to continue?"
   OperationID: ResetDispatching
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetDispatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetDispatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetDispatching(requestBody:ResetDispatching_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetDispatching_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ResetDispatching", {
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
         resolve(data as ResetDispatching_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckLine
   OperationID: CheckLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckLine(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CheckLine", {
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
         resolve(data as CheckLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckToDo
   OperationID: CheckToDo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckToDo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckToDo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckToDo(requestBody:CheckToDo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckToDo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/CheckToDo", {
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
         resolve(data as CheckToDo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendorPP
   Description: Method to call when changing the VendorPP.
   OperationID: ChangeVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorPP(requestBody:ChangeVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeVendorPP", {
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
         resolve(data as ChangeVendorPP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCurrencyCode
   Description: Method to call when changing the currency on the ReqLine.  Validates the currency code and
updates ReqLine with default values based on the currency.
   OperationID: ChangeCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyCode(requestBody:ChangeCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ChangeCurrencyCode", {
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
         resolve(data as ChangeCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostInfoExt
   OperationID: GetCostInfoExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostInfoExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostInfoExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostInfoExt(requestBody:GetCostInfoExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostInfoExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetCostInfoExt", {
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
         resolve(data as GetCostInfoExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/OnChangingRevisionNum", {
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
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReqHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReqHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReqHead(requestBody:GetNewReqHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReqHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetNewReqHead", {
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
         resolve(data as GetNewReqHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReqHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReqHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReqHeadAttch(requestBody:GetNewReqHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReqHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetNewReqHeadAttch", {
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
         resolve(data as GetNewReqHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReqDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReqDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReqDetail(requestBody:GetNewReqDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReqDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetNewReqDetail", {
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
         resolve(data as GetNewReqDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReqDetailAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqDetailAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReqDetailAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqDetailAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReqDetailAttch(requestBody:GetNewReqDetailAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReqDetailAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetNewReqDetailAttch", {
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
         resolve(data as GetNewReqDetailAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReqDetailAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReqDetailRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReqHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReqHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReqHeadRow,
}

export interface Erp_Tablesets_ReqDetailAttchRow{
   "Company":string,
   "ReqNum":number,
   "ReqLine":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ReqDetailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user.  This is a mirror of ReqHead.OpenReq and is used for performance reasons.  */  
   "OpenLine":boolean,
      /**  Requisition number that the detail line is linked to.  */  
   "ReqNum":number,
      /**  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  */  
   "ReqLine":number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   "LineDesc":string,
      /**  Issue(Our) Unit Of Measure.  */  
   "IUM":string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   "UnitCost":number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   "DocUnitCost":number,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Requisition UOM  */  
   "RUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the ReqDetail.ReqQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  OUR internal Part number for this item.  */  
   "PartNum":string,
      /**  Supplier Part Number  */  
   "VenPartNum":string,
      /**  Contains comments about the detail request line item.  Defaults  from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget in.  */  
   "Class":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Indicates if  Inspection is required when this requested line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in ReqHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   "VendorNum":number,
      /**  Ties the Requisition line back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.
Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Use the last date entered during the session for the Purchase order as a default.  */  
   "DueDate":string,
      /**  Purchase order number  that the detail line item is linked to.  */  
   "PONUM":number,
      /**  The line # of  PODetail record that the detail line item is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order.  */  
   "PORelNum":number,
      /**  Job Number  */  
   "JobNum":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  */  
   "PrcConNum":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Requisition Date for this requisition line. Initially defaults as "today".  */  
   "ReqDate":string,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  */  
   "OrderQty":number,
      /**  Total Order Quantity for the line item.  This is stored in Our  Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable. As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  */  
   "XOrderQty":number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record, "S" - Subcontract (JobOper) reference or "O" - Other.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, "O " = PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   "JobSeqType":string,
      /**  Indicates what the item is being requested for. Items can be requested for Job Material ("PUR-MTL"), Inventory ("PUR-STK"), or Other ("PUR-UKN"). FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are: M = PUR-MTL, O = PUR-STK, O = PUR-UKN.  */  
   "TranType":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Requisition identifier.  Used in Consolidated Purchasing.  */  
   "GlbReqNum":number,
      /**  Global Requisition Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbReqLine":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCost":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  MfgNum  */  
   "MfgNum":number,
      /**  MfgPartNum  */  
   "MfgPartNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   "OverridePriceList":boolean,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
   "CurrencySwitch":boolean,
   "DocExtCost":number,
      /**  Use Vendor / Class / Qualified Manufacturer / Inspection Plans to determine whether inspection required is enabled / disabled.  */  
   "EnableRcvInspectionReq":boolean,
      /**  Extended Cost  */  
   "ExtCost":number,
      /**  Flag to indicate if part is non master part  */  
   "IsNonMasterPart":boolean,
   "LeadTime":number,
   "MinOrderQty":number,
      /**  Part.PUM  */  
   "PartPUM":string,
      /**  Set based on PartPlant.QtyBearing.  This flag is used in a row rule to disable the Transaction Type when the flag is false.  */  
   "PartQtyBearing":boolean,
   "PostInvtyWipCos":boolean,
   "Rpt1ExtCost":number,
   "Rpt2ExtCost":number,
   "Rpt3ExtCost":number,
      /**  True when there is a UOM override from the Supplier Price List active for line  */  
   "UOMOverrideSPL":boolean,
   "VendorID":string,
      /**  Vendor.Inactive  */  
   "VendorInactive":boolean,
   "VendorName":string,
      /**  Vendor.PayHold  */  
   "VendorPayHold":boolean,
      /**  Currency.CurrSymbol for BASE currency Code  */  
   "BaseDisplaySymbol":string,
      /**  Number of pieces for this attribute set.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "ClassDescription":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobNumPartDescription":string,
   "MfgNumMfgID":string,
   "MfgNumName":string,
   "PartNumPartDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "POLineVenPartNum":string,
   "POLinePartNum":string,
   "POLineLineDesc":string,
   "PONUMShipToConName":string,
   "PONUMShipName":string,
   "RateGrpDescription":string,
   "ReqNumShipToConName":string,
   "ReqNumShipName":string,
   "vrClassDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ReqHeadAttchRow{
   "Company":string,
   "ReqNum":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ReqHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  */  
   "OpenReq":boolean,
      /**  Requisition number that uniquely identifies the requisition.  */  
   "ReqNum":number,
      /**  The ID of the Original Requestor that links to the User master file.  */  
   "RequestorID":string,
      /**  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  */  
   "RequestDate":string,
      /**  Requisition Log Table  */  
   "ReqActionID":string,
      /**  Requisition Action ID  */  
   "CurrDispatcherID":string,
      /**  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  */  
   "StatusType":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  StatusType Description  */  
   "StatusDesc":string,
   "RequestorIDCurMenuID":string,
   "CurrDispatcherCurMenuID":string,
   "CurrDispatcherName":string,
   "ReqActionIDReqActionDesc":string,
   "RequestorIDName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ReqHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  */  
   "OpenReq":boolean,
      /**  Requisition number that uniquely identifies the requisition.  */  
   "ReqNum":number,
      /**  The ID of the Original Requestor that links to the User master file.  */  
   "RequestorID":string,
      /**  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  */  
   "RequestDate":string,
      /**  defaults from the company file.  */  
   "ShipName":string,
      /**  First adress line  */  
   "ShipAddress1":string,
      /**  Second address line  */  
   "ShipAddress2":string,
      /**  Third address line  */  
   "ShipAddress3":string,
      /**  City portion of the address  */  
   "ShipCity":string,
      /**  Statee portion of the address  */  
   "ShipState":string,
      /**  Postal code or Zip code portion of the address  */  
   "ShipZIP":string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   "ShipCountry":string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  */  
   "PrcConNum":number,
      /**  Contains comments about over all requisition.  */  
   "CommentText":string,
      /**  Ship to contact name.  */  
   "ShipToConName":string,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   "ShipCountryNum":number,
      /**  Requisition Log Table  */  
   "ReqActionID":string,
      /**  Requisition Action ID  */  
   "CurrDispatcherID":string,
      /**  Notify upon Receipt flag  */  
   "NotifyUponReceipt":boolean,
      /**  Notes associated with the requisition action log.  */  
   "Note":string,
      /**  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  */  
   "StatusType":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Requisition identifier.  Used in Consolidated Purchasing.  */  
   "GlbReqNum":number,
      /**  Used in Consolidated Purchasing  */  
   "CPDispatcherID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
   "AddrList":string,
   "CurrDispatcherCurMenuID":string,
   "LockLines":boolean,
   "MemoAvailable":boolean,
      /**  Description of NextActionID  */  
   "NextActionDesc":string,
   "NextActionID":string,
   "NextDispatcherID":string,
   "NextDispatcherName":string,
   "NextNote":string,
   "OkToBuy":boolean,
      /**  "A", "R" or "F"  */  
   "ReplyOption":string,
   "RequestorIDCurMenuID":string,
      /**  The current ReqUserId (not same as dcduserid)  */  
   "ReqUserId":string,
      /**  StatusType Description  */  
   "StatusDesc":string,
      /**  Indicates Requests to manage for current user  */  
   "ToDoFlag":boolean,
      /**  Formatted ship to address used in Kinetic UI.  */  
   "ShipToAddressFormatted":string,
   "BitFlag":number,
   "CurrDispatcherName":string,
   "ReqActionIDReqActionDesc":string,
   "RequestorIDName":string,
   "XbSystDisableOverridePriceListOption":boolean,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "ProjectID_c":string,
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
      @param nextActionID
   */  
export interface BuildNextDispatcher_SingleList_input{
   nextActionID:string,
}

export interface BuildNextDispatcher_SingleList_output{
   returnObj:string,
}

   /** Required : 
      @param nextActionID
   */  
export interface BuildNextDispatcher_input{
      /**  The next action ID  */  
   nextActionID:string,
}

export interface BuildNextDispatcher_output{
parameters : {
      /**  output parameters  */  
   dispIDList:string,
   dispNmList:string,
}
}

   /** Required : 
      @param replyOpt
      @param includeSendToPMCond
   */  
export interface BuildReqActionsList_input{
   replyOpt:string,
   includeSendToPMCond:boolean,
}

export interface BuildReqActionsList_output{
   returnObj:string,
}

   /** Required : 
      @param proposedCurrencyCode
      @param ds
   */  
export interface ChangeCurrencyCode_input{
      /**  The proposed currency code  */  
   proposedCurrencyCode:string,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param overridePriceList
      @param ds
   */  
export interface ChangeDetailOverridePriceList_input{
      /**  True is override pricelist has been checked  */  
   overridePriceList:boolean,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeDetailOverridePriceList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ipMfgNum
      @param ds
   */  
export interface ChangeMfgNum_input{
      /**  Manufacturer Number  */  
   ipMfgNum:number,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeMfgNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ipMfgPartNum
      @param ds
   */  
export interface ChangeMfgPartNum_input{
      /**  Manufacturer Number  */  
   ipMfgPartNum:string,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeMfgPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ipClassID
      @param ds
   */  
export interface ChangePartClass_input{
      /**  New Class ID  */  
   ipClassID:string,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangePartClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ipTranType
      @param ds
   */  
export interface ChangeTranType_input{
      /**  New TranType  */  
   ipTranType:string,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeTranType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUnitPriceConfirmOverride_input{
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeUnitPriceConfirmOverride_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
   sConfirmMsg:string,
}
}

   /** Required : 
      @param proposedPurPoint
      @param ds
   */  
export interface ChangeVendorPP_input{
      /**  The proposed Vendor Purchase Point  */  
   proposedPurPoint:string,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface ChangeVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param jobNum
   */  
export interface CheckJobNum_input{
      /**  The proposed Job Number  */  
   jobNum:string,
}

export interface CheckJobNum_output{
}

export interface CheckLine_output{
   returnObj:boolean,
}

   /** Required : 
      @param partNum
   */  
export interface CheckPartStatus_input{
      /**  Part number to be validated  */  
   partNum:string,
}

export interface CheckPartStatus_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   vMessage:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param reqNum
   */  
export interface CheckReqDetailAttributeSets_input{
   reqNum:number,
}

export interface CheckReqDetailAttributeSets_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
}
}

   /** Required : 
      @param reqNum
   */  
export interface CheckReqDetail_input{
   reqNum:number,
}

export interface CheckReqDetail_output{
parameters : {
      /**  output parameters  */  
   warnMsg:string,
}
}

   /** Required : 
      @param dispatchId
   */  
export interface CheckToDo_input{
   dispatchId:string,
}

export interface CheckToDo_output{
   returnObj:boolean,
}

   /** Required : 
      @param reqNum
      @param reqUserId
   */  
export interface CloseRequisition_input{
      /**  The number of Requisition to close  */  
   reqNum:number,
      /**  The ID of user  */  
   reqUserId:string,
}

export interface CloseRequisition_output{
   returnObj:Erp_Tablesets_ReqTableset[],
}

   /** Required : 
      @param reqNum
   */  
export interface DeleteByID_input{
   reqNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param reqNum
      @param changeDate
      @param changeTime
      @param reqLogType
   */  
export interface DeleteReqLog_input{
      /**  The number of Requisition  */  
   reqNum:number,
      /**  The ChangeDate of log to delete  */  
   changeDate:string,
      /**  The ChangeTime of log to delete  */  
   changeTime:number,
      /**  The LogType of log to delete  */  
   reqLogType:string,
}

export interface DeleteReqLog_output{
}

export interface Erp_Tablesets_ReqDetailAttchRow{
   Company:string,
   ReqNum:number,
   ReqLine:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReqDetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user.  This is a mirror of ReqHead.OpenReq and is used for performance reasons.  */  
   OpenLine:boolean,
      /**  Requisition number that the detail line is linked to.  */  
   ReqNum:number,
      /**  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  */  
   ReqLine:number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   LineDesc:string,
      /**  Issue(Our) Unit Of Measure.  */  
   IUM:string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   UnitCost:number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   DocUnitCost:number,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Requisition UOM  */  
   RUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the ReqDetail.ReqQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  OUR internal Part number for this item.  */  
   PartNum:string,
      /**  Supplier Part Number  */  
   VenPartNum:string,
      /**  Contains comments about the detail request line item.  Defaults  from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget in.  */  
   Class:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Indicates if  Inspection is required when this requested line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in ReqHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   VendorNum:number,
      /**  Ties the Requisition line back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.
Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Use the last date entered during the session for the Purchase order as a default.  */  
   DueDate:string,
      /**  Purchase order number  that the detail line item is linked to.  */  
   PONUM:number,
      /**  The line # of  PODetail record that the detail line item is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order.  */  
   PORelNum:number,
      /**  Job Number  */  
   JobNum:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  */  
   PrcConNum:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Requisition Date for this requisition line. Initially defaults as "today".  */  
   ReqDate:string,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  */  
   OrderQty:number,
      /**  Total Order Quantity for the line item.  This is stored in Our  Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable. As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  */  
   XOrderQty:number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record, "S" - Subcontract (JobOper) reference or "O" - Other.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, "O " = PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   JobSeqType:string,
      /**  Indicates what the item is being requested for. Items can be requested for Job Material ("PUR-MTL"), Inventory ("PUR-STK"), or Other ("PUR-UKN"). FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are: M = PUR-MTL, O = PUR-STK, O = PUR-UKN.  */  
   TranType:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Requisition identifier.  Used in Consolidated Purchasing.  */  
   GlbReqNum:number,
      /**  Global Requisition Line identifier.  Used in Consolidated Purchasing.  */  
   GlbReqLine:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCost:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  MfgNum  */  
   MfgNum:number,
      /**  MfgPartNum  */  
   MfgPartNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   OverridePriceList:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
   CurrencySwitch:boolean,
   DocExtCost:number,
      /**  Use Vendor / Class / Qualified Manufacturer / Inspection Plans to determine whether inspection required is enabled / disabled.  */  
   EnableRcvInspectionReq:boolean,
      /**  Extended Cost  */  
   ExtCost:number,
      /**  Flag to indicate if part is non master part  */  
   IsNonMasterPart:boolean,
   LeadTime:number,
   MinOrderQty:number,
      /**  Part.PUM  */  
   PartPUM:string,
      /**  Set based on PartPlant.QtyBearing.  This flag is used in a row rule to disable the Transaction Type when the flag is false.  */  
   PartQtyBearing:boolean,
   PostInvtyWipCos:boolean,
   Rpt1ExtCost:number,
   Rpt2ExtCost:number,
   Rpt3ExtCost:number,
      /**  True when there is a UOM override from the Supplier Price List active for line  */  
   UOMOverrideSPL:boolean,
   VendorID:string,
      /**  Vendor.Inactive  */  
   VendorInactive:boolean,
   VendorName:string,
      /**  Vendor.PayHold  */  
   VendorPayHold:boolean,
      /**  Currency.CurrSymbol for BASE currency Code  */  
   BaseDisplaySymbol:string,
      /**  Number of pieces for this attribute set.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   ClassDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   MfgNumMfgID:string,
   MfgNumName:string,
   PartNumPartDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   PONUMShipToConName:string,
   PONUMShipName:string,
   RateGrpDescription:string,
   ReqNumShipToConName:string,
   ReqNumShipName:string,
   vrClassDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReqHeadAttchRow{
   Company:string,
   ReqNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReqHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  */  
   OpenReq:boolean,
      /**  Requisition number that uniquely identifies the requisition.  */  
   ReqNum:number,
      /**  The ID of the Original Requestor that links to the User master file.  */  
   RequestorID:string,
      /**  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  */  
   RequestDate:string,
      /**  Requisition Log Table  */  
   ReqActionID:string,
      /**  Requisition Action ID  */  
   CurrDispatcherID:string,
      /**  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  */  
   StatusType:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  StatusType Description  */  
   StatusDesc:string,
   RequestorIDCurMenuID:string,
   CurrDispatcherCurMenuID:string,
   CurrDispatcherName:string,
   ReqActionIDReqActionDesc:string,
   RequestorIDName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReqHeadListTableset{
   ReqHeadList:Erp_Tablesets_ReqHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ReqHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  */  
   OpenReq:boolean,
      /**  Requisition number that uniquely identifies the requisition.  */  
   ReqNum:number,
      /**  The ID of the Original Requestor that links to the User master file.  */  
   RequestorID:string,
      /**  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  */  
   RequestDate:string,
      /**  defaults from the company file.  */  
   ShipName:string,
      /**  First adress line  */  
   ShipAddress1:string,
      /**  Second address line  */  
   ShipAddress2:string,
      /**  Third address line  */  
   ShipAddress3:string,
      /**  City portion of the address  */  
   ShipCity:string,
      /**  Statee portion of the address  */  
   ShipState:string,
      /**  Postal code or Zip code portion of the address  */  
   ShipZIP:string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   ShipCountry:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  */  
   PrcConNum:number,
      /**  Contains comments about over all requisition.  */  
   CommentText:string,
      /**  Ship to contact name.  */  
   ShipToConName:string,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   ShipCountryNum:number,
      /**  Requisition Log Table  */  
   ReqActionID:string,
      /**  Requisition Action ID  */  
   CurrDispatcherID:string,
      /**  Notify upon Receipt flag  */  
   NotifyUponReceipt:boolean,
      /**  Notes associated with the requisition action log.  */  
   Note:string,
      /**  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  */  
   StatusType:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Requisition identifier.  Used in Consolidated Purchasing.  */  
   GlbReqNum:number,
      /**  Used in Consolidated Purchasing  */  
   CPDispatcherID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
   AddrList:string,
   CurrDispatcherCurMenuID:string,
   LockLines:boolean,
   MemoAvailable:boolean,
      /**  Description of NextActionID  */  
   NextActionDesc:string,
   NextActionID:string,
   NextDispatcherID:string,
   NextDispatcherName:string,
   NextNote:string,
   OkToBuy:boolean,
      /**  "A", "R" or "F"  */  
   ReplyOption:string,
   RequestorIDCurMenuID:string,
      /**  The current ReqUserId (not same as dcduserid)  */  
   ReqUserId:string,
      /**  StatusType Description  */  
   StatusDesc:string,
      /**  Indicates Requests to manage for current user  */  
   ToDoFlag:boolean,
      /**  Formatted ship to address used in Kinetic UI.  */  
   ShipToAddressFormatted:string,
   BitFlag:number,
   CurrDispatcherName:string,
   ReqActionIDReqActionDesc:string,
   RequestorIDName:string,
   XbSystDisableOverridePriceListOption:boolean,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   ProjectID_c:string,
}

export interface Erp_Tablesets_ReqLogRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Requisition number that uniquely identifies the requisition.  */  
   ReqNum:number,
      /**  Requisition Action ID  */  
   ReqActionID:string,
      /**  Current Dispatcher  */  
   CurrDispatcherID:string,
      /**  UserID who made the changes.  Not maintainable by the user.  */  
   ChangedBy:string,
      /**  System date when this change was made.  */  
   ChangeDate:string,
      /**  System time (seconds since midnight) of when the changes were made.  */  
   ChangeTime:number,
      /**   This filed is ONLY used for a Mandatory Requisition Action.
If a Requisition Action is tagged as Mandatory and this action is not yet in the log for a given requisition OR the last occurrence of this action has Approved equal to NO then this Requisition cannot be sent to Purchase Management.  */  
   Approved:boolean,
      /**  Old Action ID  */  
   OldActionID:string,
      /**  "A" Action, "N" Notify  */  
   ReqLogType:string,
      /**  Current Action  */  
   CurrentAction:boolean,
      /**  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  */  
   StatusType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ReqActionDesc:string,
      /**  ReqHead.Note  */  
   ReqHeadNote:string,
      /**  description of StatusType field  */  
   StatusDesc:string,
      /**  Change Time is display format HH:MM PM  */  
   DispChgTime:string,
   BitFlag:number,
   ChangedByName:string,
   CurrDispatcherName:string,
   ReqActionIDReqActionDesc:string,
   ReqNumShipToConName:string,
   ReqNumShipName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReqLogTableset{
   ReqLog:Erp_Tablesets_ReqLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ReqTableset{
   ReqHead:Erp_Tablesets_ReqHeadRow[],
   ReqHeadAttch:Erp_Tablesets_ReqHeadAttchRow[],
   ReqDetail:Erp_Tablesets_ReqDetailRow[],
   ReqDetailAttch:Erp_Tablesets_ReqDetailAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtReqTableset{
   ReqHead:Erp_Tablesets_ReqHeadRow[],
   ReqHeadAttch:Erp_Tablesets_ReqHeadAttchRow[],
   ReqDetail:Erp_Tablesets_ReqDetailRow[],
   ReqDetailAttch:Erp_Tablesets_ReqDetailAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reqNum
   */  
export interface GetByID_input{
   reqNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ReqTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ReqTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ReqTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface GetCostInfoExt_input{
   proposedValue:number,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface GetCostInfoExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetCostInfo_input{
   ds:Erp_Tablesets_ReqTableset[],
}

export interface GetCostInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
      @param reqDate
   */  
export interface GetExchangeRate_input{
   ds:Erp_Tablesets_ReqTableset[],
      /**  The last date a rate is valid  */  
   reqDate:string,
}

export interface GetExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
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
   returnObj:Erp_Tablesets_ReqHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param reqNum
      @param reqLine
   */  
export interface GetNewReqDetailAttch_input{
   ds:Erp_Tablesets_ReqTableset[],
   reqNum:number,
   reqLine:number,
}

export interface GetNewReqDetailAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
      @param reqNum
   */  
export interface GetNewReqDetail_input{
   ds:Erp_Tablesets_ReqTableset[],
   reqNum:number,
}

export interface GetNewReqDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
      @param reqNum
   */  
export interface GetNewReqHeadAttch_input{
   ds:Erp_Tablesets_ReqTableset[],
   reqNum:number,
}

export interface GetNewReqHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewReqHead_input{
   ds:Erp_Tablesets_ReqTableset[],
}

export interface GetNewReqHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
      @param reqLine
      @param partNum
      @param uomCode
      @param SysRowID
      @param rowType
   */  
export interface GetPartCrossRef_input{
   ds:Erp_Tablesets_ReqTableset[],
      /**  Detail Line Number to update  */  
   reqLine:number,
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  Proposed UOM Code  */  
   uomCode:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartCrossRef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
   partNum:string,
   uomCode:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
      @param uomCode
   */  
export interface GetPartInfo_input{
   ds:Erp_Tablesets_ReqTableset[],
      /**  Proposed Part Cross Reference UOM Code  */  
   uomCode:string,
}

export interface GetPartInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param ds
      @param fieldName
   */  
export interface GetQtyInfo_input{
   ds:Erp_Tablesets_ReqTableset[],
      /**  Indicates field that was changed. Possible values OrderQty or XOrderQty  */  
   fieldName:string,
}

export interface GetQtyInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetReqLogList_input{
      /**  The where clause to restrict data for  */  
   whereClause:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetReqLogList_output{
   returnObj:Erp_Tablesets_ReqLogTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseReqHead
      @param whereClauseReqHeadAttch
      @param whereClauseReqDetail
      @param whereClauseReqDetailAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseReqHead:string,
   whereClauseReqHeadAttch:string,
   whereClauseReqDetail:string,
   whereClauseReqDetailAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ReqTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetVendorInfo_input{
   ds:Erp_Tablesets_ReqTableset[],
}

export interface GetVendorInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
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
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_ReqTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

   /** Required : 
      @param reqNum
      @param reqUserId
   */  
export interface RDMenuFlags_input{
      /**  The number of Requisition to close  */  
   reqNum:number,
      /**  The ID of user  */  
   reqUserId:string,
}

export interface RDMenuFlags_output{
parameters : {
      /**  output parameters  */  
   resetDispatch:boolean,
   dispatchReq:boolean,
}
}

   /** Required : 
      @param reqNum
      @param reqUserId
   */  
export interface ResetDispatching_input{
      /**  The number of Requisition  */  
   reqNum:number,
      /**  The user ID  */  
   reqUserId:string,
}

export interface ResetDispatching_output{
   returnObj:Erp_Tablesets_ReqTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtReqTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtReqTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ReqTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReqTableset,
}
}

