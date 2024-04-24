import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JPAPPerBillStmtSvc
// Description: Japan Localization - Payment Proposal Statement Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/$metadata", {
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
   Description: Get JPAPPerBillStmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtGrpRow
   */  
export function get_JPAPPerBillStmts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPAPPerBillStmts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts", {
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
   Summary: Calls GetByID to retrieve the JPAPPerBillStmt item
   Description: Calls GetByID to retrieve the JPAPPerBillStmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
   */  
export function get_JPAPPerBillStmts_Company_PerBillStmtGrpID(Company:string, PerBillStmtGrpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JPAPPerBillStmt for the service
   Description: Calls UpdateExt to update JPAPPerBillStmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JPAPPerBillStmts_Company_PerBillStmtGrpID(Company:string, PerBillStmtGrpID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", {
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
   Summary: Call UpdateExt to delete JPAPPerBillStmt item
   Description: Call UpdateExt to delete JPAPPerBillStmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JPAPPerBillStmts_Company_PerBillStmtGrpID(Company:string, PerBillStmtGrpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")", {
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
   Description: Get JPAPPerBillStmtHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillStmtHeads1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtHeadRow
   */  
export function get_JPAPPerBillStmts_Company_PerBillStmtGrpID_JPAPPerBillStmtHeads(Company:string, PerBillStmtGrpID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/JPAPPerBillStmtHeads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtHead item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtHead1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   */  
export function get_JPAPPerBillStmts_Company_PerBillStmtGrpID_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmts(" + Company + "," + PerBillStmtGrpID + ")/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillStmtHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmtHeads
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtHeadRow
   */  
export function get_JPAPPerBillStmtHeads(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmtHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPAPPerBillStmtHeads(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads", {
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
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtHead item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   */  
export function get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JPAPPerBillStmtHead for the service
   Description: Calls UpdateExt to update JPAPPerBillStmtHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmtHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")", {
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
   Summary: Call UpdateExt to delete JPAPPerBillStmtHead item
   Description: Call UpdateExt to delete JPAPPerBillStmtHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmtHead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")", {
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
   Description: Get JPAPPerBillStmtDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillStmtDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtDtlRow
   */  
export function get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtDtls(Company:string, PerBillStmtGrpID:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtDtl item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   */  
export function get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get JPAPPerBillStmtPays items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JPAPPerBillStmtPays1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtPayRow
   */  
export function get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtPays(Company:string, PerBillStmtGrpID:string, VendorNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtPays", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtPay item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtPay1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   */  
export function get_JPAPPerBillStmtHeads_Company_PerBillStmtGrpID_VendorNum_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, StmtPayLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtHeads(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + ")/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get JPAPPerBillStmtDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmtDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtDtlRow
   */  
export function get_JPAPPerBillStmtDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmtDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPAPPerBillStmtDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls", {
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
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtDtl item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   */  
export function get_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JPAPPerBillStmtDtl for the service
   Description: Calls UpdateExt to update JPAPPerBillStmtDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmtDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, InvoiceNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete JPAPPerBillStmtDtl item
   Description: Call UpdateExt to delete JPAPPerBillStmtDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmtDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JPAPPerBillStmtDtls_Company_PerBillStmtGrpID_VendorNum_InvoiceNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtDtls(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Description: Get JPAPPerBillStmtPays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JPAPPerBillStmtPays
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtPayRow
   */  
export function get_JPAPPerBillStmtPays(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JPAPPerBillStmtPays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JPAPPerBillStmtPays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays", {
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
   Summary: Calls GetByID to retrieve the JPAPPerBillStmtPay item
   Description: Calls GetByID to retrieve the JPAPPerBillStmtPay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JPAPPerBillStmtPay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   */  
export function get_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, StmtPayLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JPAPPerBillStmtPayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JPAPPerBillStmtPayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JPAPPerBillStmtPay for the service
   Description: Calls UpdateExt to update JPAPPerBillStmtPay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JPAPPerBillStmtPay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JPAPPerBillStmtPayRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, StmtPayLineNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")", {
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
   Summary: Call UpdateExt to delete JPAPPerBillStmtPay item
   Description: Call UpdateExt to delete JPAPPerBillStmtPay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JPAPPerBillStmtPay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerBillStmtGrpID Desc: PerBillStmtGrpID   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param StmtPayLineNum Desc: StmtPayLineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JPAPPerBillStmtPays_Company_PerBillStmtGrpID_VendorNum_StmtPayLineNum(Company:string, PerBillStmtGrpID:string, VendorNum:string, StmtPayLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/JPAPPerBillStmtPays(" + Company + "," + PerBillStmtGrpID + "," + VendorNum + "," + StmtPayLineNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JPAPPerBillStmtGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseJPAPPerBillStmtGrp:string, whereClauseJPAPPerBillStmtHead:string, whereClauseJPAPPerBillStmtDtl:string, whereClauseJPAPPerBillStmtPay:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJPAPPerBillStmtGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJPAPPerBillStmtGrp=" + whereClauseJPAPPerBillStmtGrp
   }
   if(typeof whereClauseJPAPPerBillStmtHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJPAPPerBillStmtHead=" + whereClauseJPAPPerBillStmtHead
   }
   if(typeof whereClauseJPAPPerBillStmtDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJPAPPerBillStmtDtl=" + whereClauseJPAPPerBillStmtDtl
   }
   if(typeof whereClauseJPAPPerBillStmtPay!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJPAPPerBillStmtPay=" + whereClauseJPAPPerBillStmtPay
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetList" + params, {
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
   Summary: Invoke method GetSuppliers
   Description: Synchronize the DueDate and Billing date HeadInvoice with the values of the  PerBillStmtDtl table.
   OperationID: GetSuppliers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSuppliers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSuppliers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSuppliers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetSuppliers", {
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
   Summary: Invoke method ValidateBillingDate
   OperationID: ValidateBillingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBillingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBillingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBillingDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/ValidateBillingDate", {
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
   Summary: Invoke method ValidateVendorID
   Description: Validates Vendor ID
   OperationID: ValidateVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateVendorID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/ValidateVendorID", {
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
   Summary: Invoke method ValidateVendorNum
   Description: Validates Vendor No
   OperationID: ValidateVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/ValidateVendorNum", {
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
   Summary: Invoke method ValidateDueDate
   Description: Validate that the due date is not lower than the billing date.
   OperationID: ValidateDueDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDueDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/ValidateDueDate", {
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
   Summary: Invoke method ValidateReadyToBill
   Description: Validate that all the invoices are syncronized before setting the customer to "ready to bill.
   OperationID: ValidateReadyToBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReadyToBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReadyToBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateReadyToBill(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/ValidateReadyToBill", {
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
   Summary: Invoke method CheckJPConsumptionTax
   Description: Check Japan Consumption Tax exists.
   OperationID: CheckJPConsumptionTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/CheckJPConsumptionTax", {
          method: 'post',
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
   Summary: Invoke method GetNewJPAPPerBillStmtGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJPAPPerBillStmtGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetNewJPAPPerBillStmtGrp", {
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
   Summary: Invoke method GetNewJPAPPerBillStmtHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJPAPPerBillStmtHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetNewJPAPPerBillStmtHead", {
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
   Summary: Invoke method GetNewJPAPPerBillStmtDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJPAPPerBillStmtDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetNewJPAPPerBillStmtDtl", {
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
   Summary: Invoke method GetNewJPAPPerBillStmtPay
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJPAPPerBillStmtPay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJPAPPerBillStmtPay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJPAPPerBillStmtPay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJPAPPerBillStmtPay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetNewJPAPPerBillStmtPay", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JPAPPerBillStmtSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JPAPPerBillStmtDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JPAPPerBillStmtGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JPAPPerBillStmtGrpRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JPAPPerBillStmtHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JPAPPerBillStmtPayRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JPAPPerBillStmtPayRow[],
}

export interface Erp_Tablesets_JPAPPerBillStmtDtlRow{
      /**  Company  */  
   "Company":string,
      /**  PerBillStmtGrpID  */  
   "PerBillStmtGrpID":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  InvoiceNum  */  
   "InvoiceNum":string,
      /**  BillingNumber  */  
   "BillingNumber":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "APInvHedInvoiceDate":string,
   "APInvHedInvoiceAmt":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JPAPPerBillStmtGrpListRow{
      /**  Company  */  
   "Company":string,
      /**  PerBillStmtGrpID  */  
   "PerBillStmtGrpID":string,
      /**  BillingDate  */  
   "BillingDate":string,
      /**  SummarizationDate  */  
   "SummarizationDate":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JPAPPerBillStmtGrpRow{
      /**  Company  */  
   "Company":string,
      /**  PerBillStmtGrpID  */  
   "PerBillStmtGrpID":string,
      /**  BillingDate  */  
   "BillingDate":string,
      /**  SummarizationDate  */  
   "SummarizationDate":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JPAPPerBillStmtHeadRow{
      /**  Company  */  
   "Company":string,
      /**  PerBillStmtGrpID  */  
   "PerBillStmtGrpID":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  BillingDate  */  
   "BillingDate":string,
      /**  SummarizationDate  */  
   "SummarizationDate":string,
      /**  BillingNumber  */  
   "BillingNumber":string,
      /**  ReadyToBill  */  
   "ReadyToBill":boolean,
      /**  SummarizationDay  */  
   "SummarizationDay":number,
      /**  DueDate  */  
   "DueDate":string,
      /**  StartSumDate  */  
   "StartSumDate":string,
      /**  EndSumDate  */  
   "EndSumDate":string,
      /**  AmountToPay  */  
   "AmountToPay":number,
      /**  CalcTaxGlb  */  
   "CalcTaxGlb":boolean,
      /**  AdjInvoiceNum  */  
   "AdjInvoiceNum":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DspBillingDate":string,
   "TermsDescription":string,
   "BitFlag":number,
   "JPAPPerBillHeadDueDateCriteria":string,
   "SummDayTermsCode":string,
   "TranDocTypeDescription":string,
   "VendorVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JPAPPerBillStmtPayRow{
      /**  Company  */  
   "Company":string,
      /**  PerBillStmtGrpID  */  
   "PerBillStmtGrpID":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  StmtPayLineNum  */  
   "StmtPayLineNum":number,
      /**  PayHeadNum  */  
   "PayHeadNum":number,
      /**  PayInvoiceNum  */  
   "PayInvoiceNum":string,
      /**  PayVoided  */  
   "PayVoided":boolean,
      /**  PayAPTranNo  */  
   "PayAPTranNo":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




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

export interface Erp_Tablesets_JPAPPerBillStmtDtlRow{
      /**  Company  */  
   Company:string,
      /**  PerBillStmtGrpID  */  
   PerBillStmtGrpID:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  InvoiceNum  */  
   InvoiceNum:string,
      /**  BillingNumber  */  
   BillingNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   APInvHedInvoiceDate:string,
   APInvHedInvoiceAmt:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JPAPPerBillStmtGrpListRow{
      /**  Company  */  
   Company:string,
      /**  PerBillStmtGrpID  */  
   PerBillStmtGrpID:string,
      /**  BillingDate  */  
   BillingDate:string,
      /**  SummarizationDate  */  
   SummarizationDate:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JPAPPerBillStmtGrpListTableset{
   JPAPPerBillStmtGrpList:Erp_Tablesets_JPAPPerBillStmtGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JPAPPerBillStmtGrpRow{
      /**  Company  */  
   Company:string,
      /**  PerBillStmtGrpID  */  
   PerBillStmtGrpID:string,
      /**  BillingDate  */  
   BillingDate:string,
      /**  SummarizationDate  */  
   SummarizationDate:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JPAPPerBillStmtHeadRow{
      /**  Company  */  
   Company:string,
      /**  PerBillStmtGrpID  */  
   PerBillStmtGrpID:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  BillingDate  */  
   BillingDate:string,
      /**  SummarizationDate  */  
   SummarizationDate:string,
      /**  BillingNumber  */  
   BillingNumber:string,
      /**  ReadyToBill  */  
   ReadyToBill:boolean,
      /**  SummarizationDay  */  
   SummarizationDay:number,
      /**  DueDate  */  
   DueDate:string,
      /**  StartSumDate  */  
   StartSumDate:string,
      /**  EndSumDate  */  
   EndSumDate:string,
      /**  AmountToPay  */  
   AmountToPay:number,
      /**  CalcTaxGlb  */  
   CalcTaxGlb:boolean,
      /**  AdjInvoiceNum  */  
   AdjInvoiceNum:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DspBillingDate:string,
   TermsDescription:string,
   BitFlag:number,
   JPAPPerBillHeadDueDateCriteria:string,
   SummDayTermsCode:string,
   TranDocTypeDescription:string,
   VendorVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JPAPPerBillStmtPayRow{
      /**  Company  */  
   Company:string,
      /**  PerBillStmtGrpID  */  
   PerBillStmtGrpID:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  StmtPayLineNum  */  
   StmtPayLineNum:number,
      /**  PayHeadNum  */  
   PayHeadNum:number,
      /**  PayInvoiceNum  */  
   PayInvoiceNum:string,
      /**  PayVoided  */  
   PayVoided:boolean,
      /**  PayAPTranNo  */  
   PayAPTranNo:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JPAPPerBillStmtTableset{
   JPAPPerBillStmtGrp:Erp_Tablesets_JPAPPerBillStmtGrpRow[],
   JPAPPerBillStmtHead:Erp_Tablesets_JPAPPerBillStmtHeadRow[],
   JPAPPerBillStmtDtl:Erp_Tablesets_JPAPPerBillStmtDtlRow[],
   JPAPPerBillStmtPay:Erp_Tablesets_JPAPPerBillStmtPayRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJPAPPerBillStmtTableset{
   JPAPPerBillStmtGrp:Erp_Tablesets_JPAPPerBillStmtGrpRow[],
   JPAPPerBillStmtHead:Erp_Tablesets_JPAPPerBillStmtHeadRow[],
   JPAPPerBillStmtDtl:Erp_Tablesets_JPAPPerBillStmtDtlRow[],
   JPAPPerBillStmtPay:Erp_Tablesets_JPAPPerBillStmtPayRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param perBillStmtGrpID
   */  
export interface GetByID_input{
   perBillStmtGrpID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JPAPPerBillStmtTableset[],
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
   returnObj:Erp_Tablesets_JPAPPerBillStmtGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param perBillStmtGrpID
      @param vendorNum
   */  
export interface GetNewJPAPPerBillStmtDtl_input{
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
   perBillStmtGrpID:string,
   vendorNum:number,
}

export interface GetNewJPAPPerBillStmtDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJPAPPerBillStmtGrp_input{
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface GetNewJPAPPerBillStmtGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ds
      @param perBillStmtGrpID
   */  
export interface GetNewJPAPPerBillStmtHead_input{
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
   perBillStmtGrpID:string,
}

export interface GetNewJPAPPerBillStmtHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ds
      @param perBillStmtGrpID
      @param vendorNum
   */  
export interface GetNewJPAPPerBillStmtPay_input{
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
   perBillStmtGrpID:string,
   vendorNum:number,
}

export interface GetNewJPAPPerBillStmtPay_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param whereClauseJPAPPerBillStmtGrp
      @param whereClauseJPAPPerBillStmtHead
      @param whereClauseJPAPPerBillStmtDtl
      @param whereClauseJPAPPerBillStmtPay
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJPAPPerBillStmtGrp:string,
   whereClauseJPAPPerBillStmtHead:string,
   whereClauseJPAPPerBillStmtDtl:string,
   whereClauseJPAPPerBillStmtPay:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JPAPPerBillStmtTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipGrpID
      @param ds
   */  
export interface GetSuppliers_input{
      /**  Group ID  */  
   ipGrpID:string,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface GetSuppliers_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
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
   ds:Erp_Tablesets_UpdExtJPAPPerBillStmtTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJPAPPerBillStmtTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ipBillingDate
      @param ds
   */  
export interface ValidateBillingDate_input{
   ipBillingDate:string,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface ValidateBillingDate_output{
parameters : {
      /**  output parameters  */  
   opDueDate:string,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ipDueDate
      @param ds
   */  
export interface ValidateDueDate_input{
      /**  Proposed DueDate  */  
   ipDueDate:string,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface ValidateDueDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ipReadyToBill
      @param ds
   */  
export interface ValidateReadyToBill_input{
      /**  Proposed Ready To Bill status  */  
   ipReadyToBill:boolean,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface ValidateReadyToBill_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ipVendorID
      @param ds
   */  
export interface ValidateVendorID_input{
      /**  Vendor ID  */  
   ipVendorID:string,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface ValidateVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

   /** Required : 
      @param ipVendorNum
      @param ds
   */  
export interface ValidateVendorNum_input{
      /**  Vendor No  */  
   ipVendorNum:number,
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}

export interface ValidateVendorNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JPAPPerBillStmtTableset[],
}
}

