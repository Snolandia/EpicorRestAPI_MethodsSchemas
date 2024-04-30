import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IStatTrnSvc
// Description: IStatTrn business object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/$metadata", {
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
   Description: Get IStatTrns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IStatTrns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IStatTrnRow
   */  
export function get_IStatTrns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IStatTrns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IStatTrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.IStatTrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IStatTrns(requestBody:Erp_Tablesets_IStatTrnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns", {
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
   Summary: Calls GetByID to retrieve the IStatTrn item
   Description: Calls GetByID to retrieve the IStatTrn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IStatTrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param MemoFlag Desc: MemoFlag   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.IStatTrnRow
   */  
export function get_IStatTrns_Company_SourceModule_InvoiceNum_InvoiceLine_VendorNum_MemoFlag_SeqNum(Company:string, SourceModule:string, InvoiceNum:string, InvoiceLine:string, VendorNum:string, MemoFlag:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_IStatTrnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns(" + Company + "," + SourceModule + "," + InvoiceNum + "," + InvoiceLine + "," + VendorNum + "," + MemoFlag + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_IStatTrnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update IStatTrn for the service
   Description: Calls UpdateExt to update IStatTrn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IStatTrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param MemoFlag Desc: MemoFlag   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.IStatTrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_IStatTrns_Company_SourceModule_InvoiceNum_InvoiceLine_VendorNum_MemoFlag_SeqNum(Company:string, SourceModule:string, InvoiceNum:string, InvoiceLine:string, VendorNum:string, MemoFlag:string, SeqNum:string, requestBody:Erp_Tablesets_IStatTrnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns(" + Company + "," + SourceModule + "," + InvoiceNum + "," + InvoiceLine + "," + VendorNum + "," + MemoFlag + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete IStatTrn item
   Description: Call UpdateExt to delete IStatTrn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IStatTrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SourceModule Desc: SourceModule   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param MemoFlag Desc: MemoFlag   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_IStatTrns_Company_SourceModule_InvoiceNum_InvoiceLine_VendorNum_MemoFlag_SeqNum(Company:string, SourceModule:string, InvoiceNum:string, InvoiceLine:string, VendorNum:string, MemoFlag:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns(" + Company + "," + SourceModule + "," + InvoiceNum + "," + InvoiceLine + "," + VendorNum + "," + MemoFlag + "," + SeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IStatTrnListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseIStatTrn:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseIStatTrn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseIStatTrn=" + whereClauseIStatTrn
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sourceModule:string, invoiceNum:string, invoiceLine:string, vendorNum:string, memoFlag:string, seqNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sourceModule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sourceModule=" + sourceModule
   }
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }
   if(typeof invoiceLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceLine=" + invoiceLine
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
   if(typeof memoFlag!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "memoFlag=" + memoFlag
   }
   if(typeof seqNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "seqNum=" + seqNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetList" + params, {
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
   Summary: Invoke method ExportParamValidation
   Description: Method to call to get validate the IStatTrnExportParam record for the generic or Iris export.
May return a warning message to inform the user that there are unposted entries
outside the fiscal period/date range or that there aren't any posted entries in
the given fiscal period/date range.  This is informational only and does not prevent
the user from continuing.
   OperationID: ExportParamValidation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportParamValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportParamValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportParamValidation(requestBody:ExportParamValidation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportParamValidation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/ExportParamValidation", {
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
         resolve(data as ExportParamValidation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FilterGetRowsRecords
   Description: Method to filter records after GetRows based on given parameters.
   OperationID: FilterGetRowsRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FilterGetRowsRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FilterGetRowsRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FilterGetRowsRecords(requestBody:FilterGetRowsRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FilterGetRowsRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/FilterGetRowsRecords", {
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
         resolve(data as FilterGetRowsRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFlowList
   Description: Method to call to get the Flow List
for the Generic Export.
   OperationID: GetFlowList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFlowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFlowList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFlowList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetFlowList", {
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
         resolve(data as GetFlowList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIStatTrnExportParamGeneric
   Description: Method to call to get an IStatTrnExportParam record to obtain export parameters
for the Generic Export.
   OperationID: GetIStatTrnExportParamGeneric
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIStatTrnExportParamGeneric_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIStatTrnExportParamGeneric(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetIStatTrnExportParamGeneric_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetIStatTrnExportParamGeneric", {
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
         resolve(data as GetIStatTrnExportParamGeneric_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIStatTrnExportParamIris
   Description: Method to call to get an IStatTrnExportParam record to obtain export parameters
for the Iris Export.
   OperationID: GetIStatTrnExportParamIris
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIStatTrnExportParamIris_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIStatTrnExportParamIris(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetIStatTrnExportParamIris_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetIStatTrnExportParamIris", {
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
         resolve(data as GetIStatTrnExportParamIris_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNextRefNum
   Description: This methods generates the next available reference number from the IStatTrn table.
   OperationID: GetNextRefNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextRefNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextRefNum(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextRefNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetNextRefNum", {
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
         resolve(data as GetNextRefNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsFiltered
   Description: Returns IStatTrn records Filtered by advanced parameters.
   OperationID: GetRowsFiltered
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsFiltered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFiltered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFiltered(requestBody:GetRowsFiltered_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsFiltered_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetRowsFiltered", {
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
         resolve(data as GetRowsFiltered_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsCommCodeExist
   Description: Returns message string in case CommCode is not exist
   OperationID: IsCommCodeExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsCommCodeExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCommCodeExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsCommCodeExist(requestBody:IsCommCodeExist_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsCommCodeExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IsCommCodeExist", {
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
         resolve(data as IsCommCodeExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofCommCode
   Description: This methods should be called to validate the new commodity code entered by
the user.
   OperationID: OnChangeofCommCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofCommCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofCommCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofCommCode(requestBody:OnChangeofCommCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofCommCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/OnChangeofCommCode", {
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
         resolve(data as OnChangeofCommCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofTransDate
   Description: This methods should be called to validate the new Transaction date entered by
the user.
   OperationID: OnChangeofTransDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofTransDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofTransDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofTransDate(requestBody:OnChangeofTransDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofTransDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/OnChangeofTransDate", {
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
         resolve(data as OnChangeofTransDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofInvCurrencyCode
   Description: This methods should be called to validate the new currency code entered by
the user.
   OperationID: OnChangeofInvCurrencyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofInvCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofInvCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofInvCurrencyCode(requestBody:OnChangeofInvCurrencyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofInvCurrencyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/OnChangeofInvCurrencyCode", {
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
         resolve(data as OnChangeofInvCurrencyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessExport
   Description: Method to call to perform the export process for the generic or Iris export.
Returns a dataset containing all the records that are to be exported.
   OperationID: ProcessExport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessExport(requestBody:ProcessExport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessExport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/ProcessExport", {
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
         resolve(data as ProcessExport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SortByData
   Description: Return a list of the export sort by options.  Only needs to be called for generic exports.
   OperationID: SortByData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SortByData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SortByData(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SortByData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/SortByData", {
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
         resolve(data as SortByData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRefNum
   Description: This method will validate that the reference number entered not through a search
will be a valid Reference number for the entered Intrastat transaction.
   OperationID: ValidateRefNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRefNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRefNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRefNum(requestBody:ValidateRefNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRefNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/ValidateRefNum", {
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
         resolve(data as ValidateRefNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefExists
   Description: Validate the entered reference number does not exists.
   OperationID: RefExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefExists(requestBody:RefExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/RefExists", {
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
         resolve(data as RefExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewIStatTrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIStatTrn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewIStatTrn(requestBody:GetNewIStatTrn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewIStatTrn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetNewIStatTrn", {
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
         resolve(data as GetNewIStatTrn_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_IStatTrnListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_IStatTrnRow,
}

export interface Erp_Tablesets_IStatTrnListRow{
      /**  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  */  
   "Flow":string,
      /**  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  */  
   "Period":string,
      /**  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   "CommodityCode":string,
      /**  Value of transported goods excluding taxes but including miscellaneous charges.  */  
   "Amount":number,
      /**  Delivery terms.  */  
   "Terms":string,
      /**  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  */  
   "TransactionType":string,
      /**  Weight  */  
   "Weight":number,
      /**  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  */  
   "ISCountryCode":string,
      /**  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  */  
   "ISShipViaCode":string,
      /**  Area/city code from where goods cross the border.  */  
   "BorderCrossing":string,
      /**  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  */  
   "FlowSpec":string,
      /**  Currency indicator. Primarily used to cover the transitional period for the Euro.  */  
   "ISCurrency":string,
      /**  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  */  
   "Description":string,
      /**  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  */  
   "SuppUnits":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  */  
   "SourceModule":string,
      /**  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  */  
   "InvoiceNum":string,
      /**  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  */  
   "InvoiceLine":number,
      /**  Posted Flag  */  
   "Posted":boolean,
      /**  VendorNum duplicated from the corresponding APInvDtl record.  */  
   "VendorNum":number,
      /**   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  */  
   "MemoFlag":boolean,
      /**  Contains the key value of the record in the "ShipVia" table.  */  
   "ShipViaCode":string,
      /**  The code for the FOB policy.  */  
   "FOB":string,
      /**  Optional field used to record the customer/vendor State Tax Identification number.  */  
   "TaxID":string,
      /**  Value of transported goods excluding taxes and miscellaneous charges.  */  
   "InvAmount":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Not Reported Flag  */  
   "NotReported":boolean,
      /**  Intrastat Region  */  
   "ISRegion":string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   "ISOrigCountry":string,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  */  
   "IntCommCode":string,
      /**  Free form stamp to indicate the record has been reported to the authorities.  */  
   "StampID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ManualEntry":boolean,
      /**  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  */  
   "CustIDSuppID":string,
      /**  Full description of the Commodity Code.  */  
   "CommodityCodeDescription":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "InvoiceNumDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaDescription":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_IStatTrnRow{
      /**  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  */  
   "Flow":string,
      /**  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  */  
   "Period":string,
      /**  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   "CommodityCode":string,
      /**  Value of transported goods excluding taxes but including miscellaneous charges.  */  
   "Amount":number,
      /**  Delivery terms.  */  
   "Terms":string,
      /**  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  */  
   "TransactionType":string,
      /**  Weight  */  
   "Weight":number,
      /**  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  */  
   "ISCountryCode":string,
      /**  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  */  
   "ISShipViaCode":string,
      /**  Area/city code from where goods cross the border.  */  
   "BorderCrossing":string,
      /**  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  */  
   "FlowSpec":string,
      /**  Currency indicator. Primarily used to cover the transitional period for the Euro.  */  
   "ISCurrency":string,
      /**  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  */  
   "Description":string,
      /**  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  */  
   "SuppUnits":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  */  
   "SourceModule":string,
      /**  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  */  
   "InvoiceNum":string,
      /**  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  */  
   "InvoiceLine":number,
      /**  Posted Flag  */  
   "Posted":boolean,
      /**  VendorNum duplicated from the corresponding APInvDtl record.  */  
   "VendorNum":number,
      /**   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  */  
   "MemoFlag":boolean,
      /**  Contains the key value of the record in the "ShipVia" table.  */  
   "ShipViaCode":string,
      /**  The code for the FOB policy.  */  
   "FOB":string,
      /**  Optional field used to record the customer/vendor State Tax Identification number.  */  
   "TaxID":string,
      /**  Value of transported goods excluding taxes and miscellaneous charges.  */  
   "InvAmount":number,
      /**  Transaction Date  */  
   "TransDate":string,
      /**  Not Reported Flag  */  
   "NotReported":boolean,
      /**  Intrastat Region  */  
   "ISRegion":string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   "ISOrigCountry":string,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  */  
   "IntCommCode":string,
      /**  Free form stamp to indicate the record has been reported to the authorities.  */  
   "StampID":string,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CommentText  */  
   "CommentText":string,
      /**  European Union integrated tariff.  */  
   "TaricCode":string,
      /**  European Union preference.  */  
   "EUPreference":string,
      /**  Extra trade transaction indicator.  */  
   "ExtraTrade":boolean,
      /**  Commodity flow refers to the nature of a (cross-border) movement of goods.  */  
   "CommodityFlow":string,
      /**  Indicates which requested procedure and preceding procedure applies to the customs declaration.  */  
   "CustomsProcedure":string,
      /**  The country where the customs declaration was filed, where the license for this procedure was issued by customs.  */  
   "ISCustomsDeclCountry":string,
      /**  The EU Country from which the goods were dispatched for export, or to which the goods are ultimately destined for import.  */  
   "ISEUBorderCrossingCountry":string,
      /**  The mode of transport refers to the mode of transport within the EU.  */  
   "IntraEUTransportMode":string,
      /**  Indicates whether or not there is transport by container.  */  
   "ContainerShip":boolean,
      /**  Value of transported goods in invoice currency excluding taxes but including miscellaneous charges.  */  
   "DocAmount":number,
      /**  Value of transported goods  in invoice currency excluding taxes and miscellaneous charges.  */  
   "DocInvAmount":number,
      /**  A unique code that identifies the invoice currency.  */  
   "InvCurrencyCode":string,
      /**  EUThirdParty  */  
   "EUThirdParty":boolean,
      /**  Country description  */  
   "CountryDescr":string,
      /**  Description of country of origin  */  
   "CountryOfOriginDescr":string,
      /**  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  */  
   "CustIDSuppID":string,
   "CustSuppName":string,
      /**  Delivery Terms description  */  
   "DelivTermsDescr":string,
      /**  Entry Point description  */  
   "EntrPointDescr":string,
   "Generate2Line":boolean,
   "LegalNumber":string,
   "ManualEntry":boolean,
      /**  Mode of Transport description  */  
   "ModeOfTransportDescr":string,
   "PartDescription":string,
   "PartNum":string,
      /**  Region description  */  
   "RegionDescr":string,
   "ReportID":string,
      /**  Spec description  */  
   "SpecDescr":string,
      /**  Transaction Type description  */  
   "TranTypeDescr":string,
   "BitFlag":number,
   "CommodityCodeSuppUnitsUOM":string,
   "CommodityCodeDescription":string,
   "FOBDescription":string,
   "InvCurrencyCurrDesc":string,
   "InvCurrencyCurrSymbol":string,
   "InvoiceNumDescription":string,
   "ShipViaDescription":string,
   "ShipViaWebDesc":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress1":string,
   "VendorNumAddress3":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumState":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumName":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
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
      @param sourceModule
      @param invoiceNum
      @param invoiceLine
      @param vendorNum
      @param memoFlag
      @param seqNum
   */  
export interface DeleteByID_input{
   sourceModule:string,
   invoiceNum:string,
   invoiceLine:number,
   vendorNum:number,
   memoFlag:boolean,
   seqNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_IStatTrnExportParamRow{
   ExportType:string,
   FiscalYear:number,
   FiscalPeriod:number,
   StartDate:string,
   EndDate:string,
   FilterFlow:string,
   SortOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IStatTrnExportParamTableset{
   IStatTrnExportParam:Erp_Tablesets_IStatTrnExportParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IStatTrnExportRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Indicates the module that created Intrastat transaction.  This is assigned by the system. 
Values can be; AR, AP.  */  
   SourceModule:string,
      /**  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  */  
   InvoiceNum:string,
      /**  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  */  
   InvoiceLine:number,
      /**  VendorNum duplicated from the corresponding APInvDtl record.  */  
   VendorNum:number,
      /**  Indicates the type of document.  */  
   MemoFlag:boolean,
   ExportType:string,
   ExportData:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IStatTrnExportTableset{
   IStatTrnExport:Erp_Tablesets_IStatTrnExportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IStatTrnListRow{
      /**  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  */  
   Flow:string,
      /**  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  */  
   Period:string,
      /**  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   CommodityCode:string,
      /**  Value of transported goods excluding taxes but including miscellaneous charges.  */  
   Amount:number,
      /**  Delivery terms.  */  
   Terms:string,
      /**  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  */  
   TransactionType:string,
      /**  Weight  */  
   Weight:number,
      /**  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  */  
   ISCountryCode:string,
      /**  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  */  
   ISShipViaCode:string,
      /**  Area/city code from where goods cross the border.  */  
   BorderCrossing:string,
      /**  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  */  
   FlowSpec:string,
      /**  Currency indicator. Primarily used to cover the transitional period for the Euro.  */  
   ISCurrency:string,
      /**  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  */  
   Description:string,
      /**  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  */  
   SuppUnits:number,
      /**  Company Identifier.  */  
   Company:string,
      /**   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  */  
   SourceModule:string,
      /**  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  */  
   InvoiceNum:string,
      /**  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  */  
   InvoiceLine:number,
      /**  Posted Flag  */  
   Posted:boolean,
      /**  VendorNum duplicated from the corresponding APInvDtl record.  */  
   VendorNum:number,
      /**   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  */  
   MemoFlag:boolean,
      /**  Contains the key value of the record in the "ShipVia" table.  */  
   ShipViaCode:string,
      /**  The code for the FOB policy.  */  
   FOB:string,
      /**  Optional field used to record the customer/vendor State Tax Identification number.  */  
   TaxID:string,
      /**  Value of transported goods excluding taxes and miscellaneous charges.  */  
   InvAmount:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Not Reported Flag  */  
   NotReported:boolean,
      /**  Intrastat Region  */  
   ISRegion:string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   ISOrigCountry:string,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  */  
   IntCommCode:string,
      /**  Free form stamp to indicate the record has been reported to the authorities.  */  
   StampID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ManualEntry:boolean,
      /**  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  */  
   CustIDSuppID:string,
      /**  Full description of the Commodity Code.  */  
   CommodityCodeDescription:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   InvoiceNumDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaDescription:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IStatTrnListTableset{
   IStatTrnList:Erp_Tablesets_IStatTrnListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IStatTrnRow{
      /**  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  */  
   Flow:string,
      /**  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  */  
   Period:string,
      /**  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   CommodityCode:string,
      /**  Value of transported goods excluding taxes but including miscellaneous charges.  */  
   Amount:number,
      /**  Delivery terms.  */  
   Terms:string,
      /**  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  */  
   TransactionType:string,
      /**  Weight  */  
   Weight:number,
      /**  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  */  
   ISCountryCode:string,
      /**  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  */  
   ISShipViaCode:string,
      /**  Area/city code from where goods cross the border.  */  
   BorderCrossing:string,
      /**  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  */  
   FlowSpec:string,
      /**  Currency indicator. Primarily used to cover the transitional period for the Euro.  */  
   ISCurrency:string,
      /**  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  */  
   Description:string,
      /**  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  */  
   SuppUnits:number,
      /**  Company Identifier.  */  
   Company:string,
      /**   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  */  
   SourceModule:string,
      /**  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  */  
   InvoiceNum:string,
      /**  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  */  
   InvoiceLine:number,
      /**  Posted Flag  */  
   Posted:boolean,
      /**  VendorNum duplicated from the corresponding APInvDtl record.  */  
   VendorNum:number,
      /**   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  */  
   MemoFlag:boolean,
      /**  Contains the key value of the record in the "ShipVia" table.  */  
   ShipViaCode:string,
      /**  The code for the FOB policy.  */  
   FOB:string,
      /**  Optional field used to record the customer/vendor State Tax Identification number.  */  
   TaxID:string,
      /**  Value of transported goods excluding taxes and miscellaneous charges.  */  
   InvAmount:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Not Reported Flag  */  
   NotReported:boolean,
      /**  Intrastat Region  */  
   ISRegion:string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   ISOrigCountry:string,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  */  
   IntCommCode:string,
      /**  Free form stamp to indicate the record has been reported to the authorities.  */  
   StampID:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CommentText  */  
   CommentText:string,
      /**  European Union integrated tariff.  */  
   TaricCode:string,
      /**  European Union preference.  */  
   EUPreference:string,
      /**  Extra trade transaction indicator.  */  
   ExtraTrade:boolean,
      /**  Commodity flow refers to the nature of a (cross-border) movement of goods.  */  
   CommodityFlow:string,
      /**  Indicates which requested procedure and preceding procedure applies to the customs declaration.  */  
   CustomsProcedure:string,
      /**  The country where the customs declaration was filed, where the license for this procedure was issued by customs.  */  
   ISCustomsDeclCountry:string,
      /**  The EU Country from which the goods were dispatched for export, or to which the goods are ultimately destined for import.  */  
   ISEUBorderCrossingCountry:string,
      /**  The mode of transport refers to the mode of transport within the EU.  */  
   IntraEUTransportMode:string,
      /**  Indicates whether or not there is transport by container.  */  
   ContainerShip:boolean,
      /**  Value of transported goods in invoice currency excluding taxes but including miscellaneous charges.  */  
   DocAmount:number,
      /**  Value of transported goods  in invoice currency excluding taxes and miscellaneous charges.  */  
   DocInvAmount:number,
      /**  A unique code that identifies the invoice currency.  */  
   InvCurrencyCode:string,
      /**  EUThirdParty  */  
   EUThirdParty:boolean,
      /**  Country description  */  
   CountryDescr:string,
      /**  Description of country of origin  */  
   CountryOfOriginDescr:string,
      /**  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  */  
   CustIDSuppID:string,
   CustSuppName:string,
      /**  Delivery Terms description  */  
   DelivTermsDescr:string,
      /**  Entry Point description  */  
   EntrPointDescr:string,
   Generate2Line:boolean,
   LegalNumber:string,
   ManualEntry:boolean,
      /**  Mode of Transport description  */  
   ModeOfTransportDescr:string,
   PartDescription:string,
   PartNum:string,
      /**  Region description  */  
   RegionDescr:string,
   ReportID:string,
      /**  Spec description  */  
   SpecDescr:string,
      /**  Transaction Type description  */  
   TranTypeDescr:string,
   BitFlag:number,
   CommodityCodeSuppUnitsUOM:string,
   CommodityCodeDescription:string,
   FOBDescription:string,
   InvCurrencyCurrDesc:string,
   InvCurrencyCurrSymbol:string,
   InvoiceNumDescription:string,
   ShipViaDescription:string,
   ShipViaWebDesc:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IStatTrnTableset{
   IStatTrn:Erp_Tablesets_IStatTrnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtIStatTrnTableset{
   IStatTrn:Erp_Tablesets_IStatTrnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface ExportParamValidation_input{
   ds:Erp_Tablesets_IStatTrnExportParamTableset[],
}

export interface ExportParamValidation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IStatTrnExportParamTableset,
   warningText:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface FilterGetRowsRecords_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface FilterGetRowsRecords_output{
   returnObj:Erp_Tablesets_IStatTrnTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sourceModule
      @param invoiceNum
      @param invoiceLine
      @param vendorNum
      @param memoFlag
      @param seqNum
   */  
export interface GetByID_input{
   sourceModule:string,
   invoiceNum:string,
   invoiceLine:number,
   vendorNum:number,
   memoFlag:boolean,
   seqNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_IStatTrnTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_IStatTrnTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_IStatTrnTableset[],
}

export interface GetFlowList_output{
      /**  Intrastat Flow List  */  
   returnObj:string,
}

export interface GetIStatTrnExportParamGeneric_output{
   returnObj:Erp_Tablesets_IStatTrnExportParamTableset[],
}

export interface GetIStatTrnExportParamIris_output{
   returnObj:Erp_Tablesets_IStatTrnExportParamTableset[],
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
   returnObj:Erp_Tablesets_IStatTrnListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param sourceModule
      @param invoiceNum
      @param invoiceLine
      @param vendorNum
      @param memoFlag
   */  
export interface GetNewIStatTrn_input{
   ds:Erp_Tablesets_IStatTrnTableset[],
   sourceModule:string,
   invoiceNum:string,
   invoiceLine:number,
   vendorNum:number,
   memoFlag:boolean,
}

export interface GetNewIStatTrn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IStatTrnTableset,
}
}

export interface GetNextRefNum_output{
parameters : {
      /**  output parameters  */  
   opNextRefNum:string,
}
}

   /** Required : 
      @param whereClauseIStatTrn
      @param whereClauseCustSuplNum
      @param whereClauseLegalNumber
      @param whereClauseIncludeExcluded
      @param whereClauseIncludeReported
      @param whereClauseReportIDFrom
      @param whereClauseReportIDTo
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFiltered_input{
      /**  Base Whereclause for IStatTrn table.  */  
   whereClauseIStatTrn:string,
      /**  Cust Num / Supl Num  */  
   whereClauseCustSuplNum:number,
      /**  Legal Number  */  
   whereClauseLegalNumber:string,
      /**  If True - selection should include all items which do not have exclude flag  */  
   whereClauseIncludeExcluded:boolean,
      /**  No – only not reported, Yes – both reported and not reported, Only reported – only reported  */  
   whereClauseIncludeReported:string,
      /**  Min Report ID  */  
   whereClauseReportIDFrom:string,
      /**  Max Report ID  */  
   whereClauseReportIDTo:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsFiltered_output{
   returnObj:Erp_Tablesets_IStatTrnTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseIStatTrn
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseIStatTrn:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_IStatTrnTableset[],
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
   */  
export interface IsCommCodeExist_input{
   ds:Erp_Tablesets_IStatTrnTableset[],
}

export interface IsCommCodeExist_output{
parameters : {
      /**  output parameters  */  
   vErrMessage:string,
   ds:Erp_Tablesets_IStatTrnTableset,
}
}

   /** Required : 
      @param cCommCode
      @param ds
   */  
export interface OnChangeofCommCode_input{
      /**  New Commodity Code.  */  
   cCommCode:string,
   ds:Erp_Tablesets_IStatTrnTableset[],
}

export interface OnChangeofCommCode_output{
parameters : {
      /**  output parameters  */  
   cErrMessage:string,
   cOldCommCode:string,
   ds:Erp_Tablesets_IStatTrnTableset,
}
}

   /** Required : 
      @param newInvCurrencyCode
      @param ds
   */  
export interface OnChangeofInvCurrencyCode_input{
      /**  New Currency Code.  */  
   newInvCurrencyCode:string,
   ds:Erp_Tablesets_IStatTrnTableset[],
}

export interface OnChangeofInvCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IStatTrnTableset,
}
}

   /** Required : 
      @param newTransDate
      @param ds
   */  
export interface OnChangeofTransDate_input{
      /**  New Apply Date.  */  
   newTransDate:string,
   ds:Erp_Tablesets_IStatTrnTableset[],
}

export interface OnChangeofTransDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IStatTrnTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessExport_input{
   ds:Erp_Tablesets_IStatTrnExportParamTableset[],
}

export interface ProcessExport_output{
   returnObj:Erp_Tablesets_IStatTrnExportTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IStatTrnExportParamTableset,
}
}

   /** Required : 
      @param refNum
   */  
export interface RefExists_input{
      /**  Entered reference number  */  
   refNum:string,
}

export interface RefExists_output{
}

export interface SortByData_output{
parameters : {
      /**  output parameters  */  
   cSortByList:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtIStatTrnTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtIStatTrnTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_IStatTrnTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IStatTrnTableset,
}
}

   /** Required : 
      @param ipRefNum
   */  
export interface ValidateRefNum_input{
      /**  The entered reference number.  */  
   ipRefNum:string,
}

export interface ValidateRefNum_output{
parameters : {
      /**  output parameters  */  
   vErrMessage:string,
}
}

