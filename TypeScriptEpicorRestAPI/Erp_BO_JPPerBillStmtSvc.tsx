import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.JPPerBillStmtSvc
// Description: Japan Localization - Periodic Billing Statement Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/$metadata", {
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
   Description: Get JPPerBillStmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPPerBillStmts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtGrpRow
   */  
export function get_JPPerBillStmts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPPerBillStmts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPPerBillStmts(requestBody:Erp_Tablesets_PerBillStmtGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts", {
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
   Summary: Calls GetByID to retrieve the JPPerBillStmt item
   Description: Calls GetByID to retrieve the JPPerBillStmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPPerBillStmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
   */  
export function get_JPPerBillStmts_Company_PerBillStmtGrpID(Company:string, PerBillStmtGrpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerBillStmtGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", {
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
         resolve(data as Erp_Tablesets_PerBillStmtGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JPPerBillStmt for the service
   Description: Calls UpdateExt to update JPPerBillStmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPPerBillStmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JPPerBillStmts_Company_PerBillStmtGrpID(Company:string, PerBillStmtGrpID:string, requestBody:Erp_Tablesets_PerBillStmtGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", {
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
   Summary: Call UpdateExt to delete JPPerBillStmt item
   Description: Call UpdateExt to delete JPPerBillStmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPPerBillStmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JPPerBillStmts_Company_PerBillStmtGrpID(Company:string, PerBillStmtGrpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", {
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
   Description: Get PerBillStmtHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerBillStmtHeads1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtHeadRow
   */  
export function get_JPPerBillStmts_Company_PerBillStmtGrpID_PerBillStmtHeads(Company:string, PerBillStmtGrpID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/PerBillStmtHeads", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PerBillStmtHead item
   Description: Calls GetByID to retrieve the PerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtHead1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   */  
export function get_JPPerBillStmts_Company_PerBillStmtGrpID_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company:string, PerBillStmtGrpID:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/JPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")", {
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
         resolve(data as Erp_Tablesets_PerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PerBillStmtHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillStmtHeads
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtHeadRow
   */  
export function get_PerBillStmtHeads(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillStmtHeads
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerBillStmtHeads(requestBody:Erp_Tablesets_PerBillStmtHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads", {
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
   Summary: Calls GetByID to retrieve the PerBillStmtHead item
   Description: Calls GetByID to retrieve the PerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   */  
export function get_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company:string, PerBillStmtGrpID:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")", {
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
         resolve(data as Erp_Tablesets_PerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PerBillStmtHead for the service
   Description: Calls UpdateExt to update PerBillStmtHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillStmtHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company:string, PerBillStmtGrpID:string, CustNum:string, requestBody:Erp_Tablesets_PerBillStmtHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete PerBillStmtHead item
   Description: Call UpdateExt to delete PerBillStmtHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillStmtHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum(Company:string, PerBillStmtGrpID:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")", {
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
   Description: Get PerBillStmtPays items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerBillStmtPays1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtPayRow
   */  
export function get_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum_PerBillStmtPays(Company:string, PerBillStmtGrpID:string, CustNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")/PerBillStmtPays", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PerBillStmtPay item
   Description: Calls GetByID to retrieve the PerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtPay1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   */  
export function get_PerBillStmtHeads_Company_PerBillStmtGrpID_CustNum_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, CustNum:string, StmtPayLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + CustNum + ")/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")", {
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
         resolve(data as Erp_Tablesets_PerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PerBillStmtPays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillStmtPays
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtPayRow
   */  
export function get_PerBillStmtPays(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillStmtPays
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerBillStmtPayRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerBillStmtPays(requestBody:Erp_Tablesets_PerBillStmtPayRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays", {
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
   Summary: Calls GetByID to retrieve the PerBillStmtPay item
   Description: Calls GetByID to retrieve the PerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtPay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   */  
export function get_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, CustNum:string, StmtPayLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")", {
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
         resolve(data as Erp_Tablesets_PerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PerBillStmtPay for the service
   Description: Calls UpdateExt to update PerBillStmtPay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillStmtPay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtPayRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, CustNum:string, StmtPayLineNum:string, requestBody:Erp_Tablesets_PerBillStmtPayRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")", {
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
   Summary: Call UpdateExt to delete PerBillStmtPay item
   Description: Call UpdateExt to delete PerBillStmtPay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillStmtPay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PerBillStmtPays_Company_PerBillStmtGrpID_CustNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, CustNum:string, StmtPayLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + StmtPayLineNum + ")", {
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
   Description: Get PerBillStmtDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerBillStmtDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtDtlRow
   */  
export function get_PerBillStmtDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerBillStmtDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerBillStmtDtls(requestBody:Erp_Tablesets_PerBillStmtDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls", {
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
   Summary: Calls GetByID to retrieve the PerBillStmtDtl item
   Description: Calls GetByID to retrieve the PerBillStmtDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerBillStmtDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
   */  
export function get_PerBillStmtDtls_Company_PerBillStmtGrpID_CustNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, CustNum:string, InvoiceNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerBillStmtDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + InvoiceNum + ")", {
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
         resolve(data as Erp_Tablesets_PerBillStmtDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PerBillStmtDtl for the service
   Description: Calls UpdateExt to update PerBillStmtDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerBillStmtDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerBillStmtDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PerBillStmtDtls_Company_PerBillStmtGrpID_CustNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, CustNum:string, InvoiceNum:string, requestBody:Erp_Tablesets_PerBillStmtDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete PerBillStmtDtl item
   Description: Call UpdateExt to delete PerBillStmtDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerBillStmtDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PerBillStmtDtls_Company_PerBillStmtGrpID_CustNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, CustNum:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/PerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + CustNum + "," + InvoiceNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerBillStmtGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpListRow)
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
export function get_GetRows(whereClausePerBillStmtGrp:string, whereClausePerBillStmtHead:string, whereClausePerBillStmtDtl:string, whereClausePerBillStmtPay:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePerBillStmtGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerBillStmtGrp=" + whereClausePerBillStmtGrp
   }
   if(typeof whereClausePerBillStmtHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerBillStmtHead=" + whereClausePerBillStmtHead
   }
   if(typeof whereClausePerBillStmtDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerBillStmtDtl=" + whereClausePerBillStmtDtl
   }
   if(typeof whereClausePerBillStmtPay!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerBillStmtPay=" + whereClausePerBillStmtPay
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetRows" + params, {
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
export function get_GetByID(perBillStmtGrpID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof perBillStmtGrpID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "perBillStmtGrpID=" + perBillStmtGrpID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetList" + params, {
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
   Summary: Invoke method GetCustomers
   Description: Syncronize the DueDate and Billing date HeadInvoice with the values of the  PerBillStmtDtl table.
   OperationID: GetCustomers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomers(requestBody:GetCustomers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustomers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetCustomers", {
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
         resolve(data as GetCustomers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBillingDate
   OperationID: ValidateBillingDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateBillingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBillingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBillingDate(requestBody:ValidateBillingDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateBillingDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/ValidateBillingDate", {
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
         resolve(data as ValidateBillingDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCustID
   Description: Receives CustId, returns CustNum
   OperationID: ValidateCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCustID(requestBody:ValidateCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/ValidateCustID", {
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
         resolve(data as ValidateCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateDueDate
   Description: Validate that the due date is not lower than the billing date.
   OperationID: ValidateDueDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateDueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDueDate(requestBody:ValidateDueDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateDueDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/ValidateDueDate", {
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
         resolve(data as ValidateDueDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateReadyToBill
   Description: Validate that all the invoices are syncronized before setting the customer to "ready to bill.
   OperationID: ValidateReadyToBill
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateReadyToBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReadyToBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateReadyToBill(requestBody:ValidateReadyToBill_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateReadyToBill_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/ValidateReadyToBill", {
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
         resolve(data as ValidateReadyToBill_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckJPConsumptionTax
   Description: Check Japan Consumption Tax exists.
   OperationID: CheckJPConsumptionTax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJPConsumptionTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckJPConsumptionTax(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckJPConsumptionTax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/CheckJPConsumptionTax", {
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
         resolve(data as CheckJPConsumptionTax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerBillStmtGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerBillStmtGrp(requestBody:GetNewPerBillStmtGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerBillStmtGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetNewPerBillStmtGrp", {
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
         resolve(data as GetNewPerBillStmtGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerBillStmtHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerBillStmtHead(requestBody:GetNewPerBillStmtHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerBillStmtHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetNewPerBillStmtHead", {
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
         resolve(data as GetNewPerBillStmtHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerBillStmtDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerBillStmtDtl(requestBody:GetNewPerBillStmtDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerBillStmtDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetNewPerBillStmtDtl", {
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
         resolve(data as GetNewPerBillStmtDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerBillStmtPay
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerBillStmtPay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerBillStmtPay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerBillStmtPay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerBillStmtPay(requestBody:GetNewPerBillStmtPay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerBillStmtPay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetNewPerBillStmtPay", {
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
         resolve(data as GetNewPerBillStmtPay_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPPerBillStmtSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerBillStmtDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerBillStmtGrpListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerBillStmtGrpRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerBillStmtHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerBillStmtPayRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerBillStmtPayRow,
}

export interface Erp_Tablesets_PerBillStmtDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   "PerBillStmtGrpID":string,
      /**  Date when a company bills the customer  */  
   "BillingDate":string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   "SummarizationDate":string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   "CustNum":number,
      /**  AR Invoice Number  */  
   "InvoiceNum":number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   "BillingNumber":string,
      /**  Ready to Bill  */  
   "ReadyToBill":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag that let us know if the Dates are synchronized with the AR Invoice  */  
   "Synchronized":boolean,
   "DspInvoiceAmt":number,
   "BitFlag":number,
   "InvcHeadTermsCode":string,
   "InvcHeadInvoiceAmt":number,
   "InvcHeadCardMemberName":string,
   "InvcHeadBillingNumber":string,
   "InvcHeadInvoiceDate":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PerBillStmtGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   "PerBillStmtGrpID":string,
      /**  Date when a company bills the customer  */  
   "BillingDate":string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   "SummarizationDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PerBillStmtGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   "PerBillStmtGrpID":string,
      /**  Date when a company bills the customer  */  
   "BillingDate":string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   "SummarizationDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PerBillStmtHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   "PerBillStmtGrpID":string,
      /**  Date when a company bills the customer  */  
   "BillingDate":string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   "SummarizationDate":string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   "CustNum":number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   "BillingNumber":string,
      /**  Ready to Bill  */  
   "ReadyToBill":boolean,
      /**  Summarization Day. A  day when a company sums up accounts receivables for each customer. Used to calculate Billing Period and Date.  */  
   "SummarizationDay":number,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  StartSumDate  */  
   "StartSumDate":string,
      /**  EndSumDate  */  
   "EndSumDate":string,
      /**  AmountToPay  */  
   "AmountToPay":number,
      /**  CalcTaxGlb  */  
   "CalcTaxGlb":boolean,
      /**  AdjInvoiceNum  */  
   "AdjInvoiceNum":number,
   "CustID":string,
      /**  Date when a company bills the customer  */  
   "dispBillingDate":string,
   "TermsDescription":string,
   "BitFlag":number,
   "CustNumCustID":string,
   "CustNumName":string,
   "PerBillHeadDueDateCriteria":string,
   "PerBillHeadPerBillTerms":number,
   "SummDayEndOfMonth":boolean,
   "SummDayTermsCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PerBillStmtPayRow{
      /**  Company  */  
   "Company":string,
      /**  PerBillStmtGrpID  */  
   "PerBillStmtGrpID":string,
      /**  CustNum  */  
   "CustNum":number,
      /**  StmtPayLineNum  */  
   "StmtPayLineNum":number,
      /**  PayGroupID  */  
   "PayGroupID":string,
      /**  PayHeadNum  */  
   "PayHeadNum":number,
      /**  PayInvoiceNum  */  
   "PayInvoiceNum":number,
      /**  PayInvoiceRef  */  
   "PayInvoiceRef":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
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
export interface CheckJPConsumptionTax_output{
}

   /** Required : 
      @param perBillStmtGrpID
   */  
export interface DeleteByID_input{
   perBillStmtGrpID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JPPerBillStmtTableset{
   PerBillStmtGrp:Erp_Tablesets_PerBillStmtGrpRow[],
   PerBillStmtHead:Erp_Tablesets_PerBillStmtHeadRow[],
   PerBillStmtDtl:Erp_Tablesets_PerBillStmtDtlRow[],
   PerBillStmtPay:Erp_Tablesets_PerBillStmtPayRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PerBillStmtDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   PerBillStmtGrpID:string,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  AR Invoice Number  */  
   InvoiceNum:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Ready to Bill  */  
   ReadyToBill:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag that let us know if the Dates are synchronized with the AR Invoice  */  
   Synchronized:boolean,
   DspInvoiceAmt:number,
   BitFlag:number,
   InvcHeadTermsCode:string,
   InvcHeadInvoiceAmt:number,
   InvcHeadCardMemberName:string,
   InvcHeadBillingNumber:string,
   InvcHeadInvoiceDate:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerBillStmtGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   PerBillStmtGrpID:string,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerBillStmtGrpListTableset{
   PerBillStmtGrpList:Erp_Tablesets_PerBillStmtGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PerBillStmtGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   PerBillStmtGrpID:string,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerBillStmtHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before selecting customers to be billed the user establishes a Group ID. The PerBillStmtGrpID is assigned by the user.  The PerBillStmtGrpID is used to Selectively print Billing Statements  */  
   PerBillStmtGrpID:string,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Ready to Bill  */  
   ReadyToBill:boolean,
      /**  Summarization Day. A  day when a company sums up accounts receivables for each customer. Used to calculate Billing Period and Date.  */  
   SummarizationDay:number,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  StartSumDate  */  
   StartSumDate:string,
      /**  EndSumDate  */  
   EndSumDate:string,
      /**  AmountToPay  */  
   AmountToPay:number,
      /**  CalcTaxGlb  */  
   CalcTaxGlb:boolean,
      /**  AdjInvoiceNum  */  
   AdjInvoiceNum:number,
   CustID:string,
      /**  Date when a company bills the customer  */  
   dispBillingDate:string,
   TermsDescription:string,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   PerBillHeadDueDateCriteria:string,
   PerBillHeadPerBillTerms:number,
   SummDayEndOfMonth:boolean,
   SummDayTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerBillStmtPayRow{
      /**  Company  */  
   Company:string,
      /**  PerBillStmtGrpID  */  
   PerBillStmtGrpID:string,
      /**  CustNum  */  
   CustNum:number,
      /**  StmtPayLineNum  */  
   StmtPayLineNum:number,
      /**  PayGroupID  */  
   PayGroupID:string,
      /**  PayHeadNum  */  
   PayHeadNum:number,
      /**  PayInvoiceNum  */  
   PayInvoiceNum:number,
      /**  PayInvoiceRef  */  
   PayInvoiceRef:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtJPPerBillStmtTableset{
   PerBillStmtGrp:Erp_Tablesets_PerBillStmtGrpRow[],
   PerBillStmtHead:Erp_Tablesets_PerBillStmtHeadRow[],
   PerBillStmtDtl:Erp_Tablesets_PerBillStmtDtlRow[],
   PerBillStmtPay:Erp_Tablesets_PerBillStmtPayRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param perBillStmtGrpID
   */  
export interface GetByID_input{
   perBillStmtGrpID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JPPerBillStmtTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JPPerBillStmtTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JPPerBillStmtTableset[],
}

   /** Required : 
      @param ipGrpID
      @param ds
   */  
export interface GetCustomers_input{
      /**  Group ID  */  
   ipGrpID:string,
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface GetCustomers_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_JPPerBillStmtTableset,
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
   returnObj:Erp_Tablesets_PerBillStmtGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param perBillStmtGrpID
      @param custNum
   */  
export interface GetNewPerBillStmtDtl_input{
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
   perBillStmtGrpID:string,
   custNum:number,
}

export interface GetNewPerBillStmtDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPerBillStmtGrp_input{
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface GetNewPerBillStmtGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ds
      @param perBillStmtGrpID
   */  
export interface GetNewPerBillStmtHead_input{
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
   perBillStmtGrpID:string,
}

export interface GetNewPerBillStmtHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ds
      @param perBillStmtGrpID
      @param custNum
   */  
export interface GetNewPerBillStmtPay_input{
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
   perBillStmtGrpID:string,
   custNum:number,
}

export interface GetNewPerBillStmtPay_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param whereClausePerBillStmtGrp
      @param whereClausePerBillStmtHead
      @param whereClausePerBillStmtDtl
      @param whereClausePerBillStmtPay
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePerBillStmtGrp:string,
   whereClausePerBillStmtHead:string,
   whereClausePerBillStmtDtl:string,
   whereClausePerBillStmtPay:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JPPerBillStmtTableset[],
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
   ds:Erp_Tablesets_UpdExtJPPerBillStmtTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJPPerBillStmtTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ipBillingDate
      @param ds
   */  
export interface ValidateBillingDate_input{
   ipBillingDate:string,
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface ValidateBillingDate_output{
parameters : {
      /**  output parameters  */  
   opDueDate:string,
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ipCustID
      @param ds
   */  
export interface ValidateCustID_input{
      /**  Customer ID  */  
   ipCustID:string,
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface ValidateCustID_output{
parameters : {
      /**  output parameters  */  
   opCustNum:number,
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ipDueDate
      @param ds
   */  
export interface ValidateDueDate_input{
      /**  Proposed DueDate  */  
   ipDueDate:string,
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface ValidateDueDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

   /** Required : 
      @param ipReadyToBill
      @param ds
   */  
export interface ValidateReadyToBill_input{
      /**  Proposed Ready To Bill status  */  
   ipReadyToBill:boolean,
   ds:Erp_Tablesets_JPPerBillStmtTableset[],
}

export interface ValidateReadyToBill_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPPerBillStmtTableset,
}
}

