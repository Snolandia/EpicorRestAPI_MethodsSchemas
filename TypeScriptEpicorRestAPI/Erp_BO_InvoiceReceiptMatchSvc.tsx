import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.InvoiceReceiptMatchSvc
// Description: Invoice Receipt Match business object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/$metadata", {
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
   Description: Get InvoiceReceiptMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvoiceReceiptMatches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceMatchRow
   */  
export function get_InvoiceReceiptMatches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InvoiceReceiptMatch item
   Description: Calls GetByID to retrieve the InvoiceReceiptMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvoiceReceiptMatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvoiceMatchRow
   */  
export function get_InvoiceReceiptMatches_Company_InvoiceNum_InvoiceLine_PONum_POLine_PORelNum(Company:string, InvoiceNum:string, InvoiceLine:string, PONum:string, POLine:string, PORelNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvoiceMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + PONum + "," + POLine + "," + PORelNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvoiceMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get APInvcRcptDtlMatches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APInvcRcptDtlMatches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvcRcptDtlMatchRow
   */  
export function get_InvoiceReceiptMatches_Company_InvoiceNum_InvoiceLine_PONum_POLine_PORelNum_APInvcRcptDtlMatches(Company:string, InvoiceNum:string, InvoiceLine:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvcRcptDtlMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + PONum + "," + POLine + "," + PORelNum + ")/APInvcRcptDtlMatches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvcRcptDtlMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APInvcRcptDtlMatch item
   Description: Calls GetByID to retrieve the APInvcRcptDtlMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvcRcptDtlMatch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvcRcptDtlMatchRow
   */  
export function get_InvoiceReceiptMatches_Company_InvoiceNum_InvoiceLine_PONum_POLine_PORelNum_APInvcRcptDtlMatches_Company_VendorNum_PurPoint_PackSlip_PackLine_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, PONum:string, POLine:string, PORelNum:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvcRcptDtlMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/InvoiceReceiptMatches(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + PONum + "," + POLine + "," + PORelNum + ")/APInvcRcptDtlMatches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvcRcptDtlMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APInvcRcptDtlMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvcRcptDtlMatches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvcRcptDtlMatchRow
   */  
export function get_APInvcRcptDtlMatches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvcRcptDtlMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/APInvcRcptDtlMatches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvcRcptDtlMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APInvcRcptDtlMatch item
   Description: Calls GetByID to retrieve the APInvcRcptDtlMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvcRcptDtlMatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvcRcptDtlMatchRow
   */  
export function get_APInvcRcptDtlMatches_Company_VendorNum_PurPoint_PackSlip_PackLine_InvoiceNum_InvoiceLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvcRcptDtlMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/APInvcRcptDtlMatches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvcRcptDtlMatchRow)
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceMatchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchListRow)
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
   Description: GetRows for Kinetic LandingPage
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/GetRows" + params, {
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
   Description: GetByID
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(invoiceNum:string, invoiceLine:string, vendorNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/GetByID" + params, {
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
   Description: This method returns the Data Schema records
   OperationID: Get_GetList
      @param whereClause Desc: Where clause   Required: True   Allow empty value : True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute Page   Required: True
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/GetList" + params, {
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
   Summary: Invoke method CheckGLInterfaceForPost
   Description: Checks to see if GL interface is available before posting.  Is run before the
PostMatches method.  A question is returned to ask the user if they want to continue
with the post or not if the interface is not available.  If the answer is no, the
PostMatches method is not run.
   OperationID: CheckGLInterfaceForPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterfaceForPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGLInterfaceForPost(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/CheckGLInterfaceForPost", {
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
   Summary: Invoke method GetAPIRMtch
   Description: Get the APIRMtch records.
   OperationID: GetAPIRMtch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPIRMtch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPIRMtch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPIRMtch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/GetAPIRMtch", {
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
   Summary: Invoke method GetInvoiceReceiptMatch
   Description: Get the InvoiceReceipt records from the list dataset.
   OperationID: GetInvoiceReceiptMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoiceReceiptMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoiceReceiptMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoiceReceiptMatch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/GetInvoiceReceiptMatch", {
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
   Summary: Invoke method GetSupplierXRefParts
   Description: This method gets the XRef information for a given supplier part
   OperationID: GetSupplierXRefParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupplierXRefParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplierXRefParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSupplierXRefParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/GetSupplierXRefParts", {
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
   Summary: Invoke method MatchInvoiceReceipt
   Description: Match an invoice and a receipt.
   OperationID: MatchInvoiceReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchInvoiceReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchInvoiceReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchInvoiceReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/MatchInvoiceReceipt", {
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
   Summary: Invoke method PostMatches
   Description: Post the Invoice/Receipt matches.
   OperationID: PostMatches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostMatches_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostMatches_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostMatches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/PostMatches", {
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
   Summary: Invoke method SetSupplierXRefParts
   Description: This method sets the XRef fields for a supplier part
   OperationID: SetSupplierXRefParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSupplierXRefParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSupplierXRefParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSupplierXRefParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/SetSupplierXRefParts", {
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
   Summary: Invoke method UnMatchInvoiceReceipt
   Description: Unmatch an invoice and a receipt.
   OperationID: UnMatchInvoiceReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnMatchInvoiceReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnMatchInvoiceReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnMatchInvoiceReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceReceiptMatchSvc/UnMatchInvoiceReceipt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvcRcptDtlMatchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvcRcptDtlMatchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvoiceMatchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceMatchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvoiceMatchRow[],
}

export interface Erp_Tablesets_APInvcRcptDtlMatchRow{
   "Company":string,
   "VendorNum":number,
   "PurPoint":string,
   "PackSlip":string,
   "PackLine":number,
   "ReceiptDate":string,
   "ReceiptVendorQty":number,
   "QuantitiesMatch":boolean,
   "ReceiptUnitCost":number,
   "VendorPart":string,
   "Matched":boolean,
   "PartNum":string,
   "MatchedReference":string,
   "PONum":number,
   "POLine":number,
   "PORelNum":number,
   "InvoiceNum":string,
   "InvoiceLine":number,
      /**  Receipt Vendor Unit of Measure  */  
   "ReceiptVendorUOM":string,
      /**  Receipt Unit Cost Unit of Measure  */  
   "ReceiptUnitCostUOM":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APInvoiceMatchListRow{
   "Company":string,
   "VendorID":string,
   "InvoiceNum":string,
   "InvoiceLine":number,
   "MatchedReference":string,
   "PONum":number,
   "POLine":number,
   "PORelNum":number,
   "InvoiceVendorQty":number,
   "PartNum":string,
   "InvoiceDate":string,
   "VendorPartNum":string,
   "UnitCost":number,
   "ExtCost":number,
   "LegalNumber":string,
   "VendorNum":number,
   "PurPoint":string,
   "PackSlip":string,
   "PackLine":number,
   "BaseUnitCost":number,
   "BaseExtCost":number,
   "Currency":string,
      /**  Invoice Vendor Unit of Measure  */  
   "InvoiceVendorUOM":string,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APInvoiceMatchRow{
   "Company":string,
   "VendorID":string,
   "InvoiceNum":string,
   "InvoiceLine":number,
   "MatchedReference":string,
   "PONum":number,
   "POLine":number,
   "PORelNum":number,
   "InvoiceVendorQty":number,
   "PartNum":string,
   "InvoiceDate":string,
   "VendorPartNum":string,
   "UnitCost":number,
   "ExtCost":number,
   "LegalNumber":string,
   "VendorNum":number,
   "PurPoint":string,
   "PackSlip":string,
   "PackLine":number,
   "BaseUnitCost":number,
   "BaseExtCost":number,
   "Currency":string,
      /**  Invoice Vendor Unit of Measure  */  
   "InvoiceVendorUOM":string,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface CheckGLInterfaceForPost_output{
parameters : {
      /**  output parameters  */  
   cContinuePostMsg:string,
}
}

export interface Erp_Tablesets_APIRMtchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   InvoiceNum:string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table.  InvoiceLine of the related APInvDtl.  */  
   InvoiceLine:number,
      /**  The Vendors purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  */  
   PurPoint:string,
      /**  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  */  
   PackSlip:string,
      /**  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  */  
   PackLine:number,
      /**  Legal Number for the record.  */  
   LegalNumber:string,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   InvoiceVendorQty:number,
   ReceiptVendorQty:number,
   InvoiceUnitCost:number,
   ReceiptUnitCost:number,
   PartNum:string,
      /**  Receipt Vendor Unit of Measure  */  
   ReceiptVendorUOM:string,
      /**  Invoice Vendor Unit of Measure  */  
   InvoiceVendorUOM:string,
   BitFlag:number,
   InvoiceNumDescription:string,
   VendorNumAddress2:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress3:string,
   VendorNumTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APIRMtchTableset{
   APIRMtch:Erp_Tablesets_APIRMtchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvcRcptDtlMatchRow{
   Company:string,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
   PackLine:number,
   ReceiptDate:string,
   ReceiptVendorQty:number,
   QuantitiesMatch:boolean,
   ReceiptUnitCost:number,
   VendorPart:string,
   Matched:boolean,
   PartNum:string,
   MatchedReference:string,
   PONum:number,
   POLine:number,
   PORelNum:number,
   InvoiceNum:string,
   InvoiceLine:number,
      /**  Receipt Vendor Unit of Measure  */  
   ReceiptVendorUOM:string,
      /**  Receipt Unit Cost Unit of Measure  */  
   ReceiptUnitCostUOM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvoiceMatchListRow{
   Company:string,
   VendorID:string,
   InvoiceNum:string,
   InvoiceLine:number,
   MatchedReference:string,
   PONum:number,
   POLine:number,
   PORelNum:number,
   InvoiceVendorQty:number,
   PartNum:string,
   InvoiceDate:string,
   VendorPartNum:string,
   UnitCost:number,
   ExtCost:number,
   LegalNumber:string,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
   PackLine:number,
   BaseUnitCost:number,
   BaseExtCost:number,
   Currency:string,
      /**  Invoice Vendor Unit of Measure  */  
   InvoiceVendorUOM:string,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvoiceMatchListTableset{
   APInvoiceMatchList:Erp_Tablesets_APInvoiceMatchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvoiceMatchRow{
   Company:string,
   VendorID:string,
   InvoiceNum:string,
   InvoiceLine:number,
   MatchedReference:string,
   PONum:number,
   POLine:number,
   PORelNum:number,
   InvoiceVendorQty:number,
   PartNum:string,
   InvoiceDate:string,
   VendorPartNum:string,
   UnitCost:number,
   ExtCost:number,
   LegalNumber:string,
   VendorNum:number,
   PurPoint:string,
   PackSlip:string,
   PackLine:number,
   BaseUnitCost:number,
   BaseExtCost:number,
   Currency:string,
      /**  Invoice Vendor Unit of Measure  */  
   InvoiceVendorUOM:string,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvoiceReceiptMatchTableset{
   APInvoiceMatch:Erp_Tablesets_APInvoiceMatchRow[],
   APInvcRcptDtlMatch:Erp_Tablesets_APInvcRcptDtlMatchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SupplierXRefRow{
   Company:string,
   MfgID:string,
   MfgName:string,
   MfgNum:number,
   MfgPartNum:string,
   PartNum:string,
   POReference:boolean,
   Receipt:boolean,
   VendNum:number,
   VendPartNum:string,
   Invoice:boolean,
      /**  RcvXRefNum  */  
   RcvXRefNum:number,
   Inspected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SupplierXRefTableset{
   SupplierXRef:Erp_Tablesets_SupplierXRefRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param pageSize
      @param absolutePage
   */  
export interface GetAPIRMtch_input{
      /**  The pageSize parameter  */  
   pageSize:number,
      /**  The absolutePage parameter  */  
   absolutePage:number,
}

export interface GetAPIRMtch_output{
   returnObj:Erp_Tablesets_APIRMtchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param invoiceNum
      @param invoiceLine
      @param vendorNum
   */  
export interface GetByID_input{
   invoiceNum:string,
   invoiceLine:number,
   vendorNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_InvoiceReceiptMatchTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetInvoiceReceiptMatch_input{
   ds:Erp_Tablesets_APInvoiceMatchListTableset[],
}

export interface GetInvoiceReceiptMatch_output{
   returnObj:Erp_Tablesets_InvoiceReceiptMatchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceMatchListTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  Where clause  */  
   whereClause:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_APInvoiceMatchListTableset[],
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
export interface GetRows_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_InvoiceReceiptMatchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param partNum
      @param vendorNum
      @param poNum
      @param poLine
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface GetSupplierXRefParts_input{
      /**  Receipt Part Number  */  
   partNum:string,
      /**  Receipt Supplier Number  */  
   vendorNum:number,
      /**  PO Number  */  
   poNum:number,
      /**  PO Line  */  
   poLine:number,
      /**  Purchase Point  */  
   purPoint:string,
      /**  packing Slip  */  
   packSlip:string,
      /**  packing Line  */  
   packLine:number,
}

export interface GetSupplierXRefParts_output{
   returnObj:Erp_Tablesets_SupplierXRefTableset[],
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
      @param cInvoiceNum
      @param iInvoiceLine
      @param iVendorNum
      @param cPurPoint
      @param cPackSlip
      @param iPackLine
      @param ds
   */  
export interface MatchInvoiceReceipt_input{
      /**  The Invoice Number of the APInvoiceMatch record  */  
   cInvoiceNum:string,
      /**  The Invoice Line Number of the APInvoiceMatch record  */  
   iInvoiceLine:number,
      /**  The Vendor Number of the APInvcRcptDtlMatch record  */  
   iVendorNum:number,
      /**  The Purchase Point of the APInvcRcptDtlMatch record  */  
   cPurPoint:string,
      /**  The Pack Slip of the APInvcRcptDtlMatch record  */  
   cPackSlip:string,
      /**  The Pack Slip Line of the APInvcRcptDtlMatch record  */  
   iPackLine:number,
   ds:Erp_Tablesets_InvoiceReceiptMatchTableset[],
}

export interface MatchInvoiceReceipt_output{
   returnObj:Erp_Tablesets_APIRMtchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvoiceReceiptMatchTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface PostMatches_input{
   ds:Erp_Tablesets_APInvoiceMatchListTableset[],
}

export interface PostMatches_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvoiceMatchListTableset[],
   cPostErrorLog:string,
   cErrorLogMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SetSupplierXRefParts_input{
   ds:Erp_Tablesets_SupplierXRefTableset[],
}

export interface SetSupplierXRefParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SupplierXRefTableset[],
}
}

   /** Required : 
      @param cInvoiceNum
      @param iInvoiceLine
      @param iVendorNum
      @param cPurPoint
      @param cPackSlip
      @param iPackLine
      @param ds
   */  
export interface UnMatchInvoiceReceipt_input{
      /**  The Invoice Number of the APInvcRcptDtlMatch record  */  
   cInvoiceNum:string,
      /**  The Invoice Line of the APInvcRcptDtlMatch record  */  
   iInvoiceLine:number,
      /**  The Vendor Number of the APInvcRcptDtlMatch record  */  
   iVendorNum:number,
      /**  The Purchase Point of the APInvcRcptDtlMatch record  */  
   cPurPoint:string,
      /**  The Pack Slip of the APInvcRcptDtlMatch record  */  
   cPackSlip:string,
      /**  The Pack Slip Line of the APInvcRcptDtlMatch record  */  
   iPackLine:number,
   ds:Erp_Tablesets_InvoiceReceiptMatchTableset[],
}

export interface UnMatchInvoiceReceipt_output{
   returnObj:Erp_Tablesets_APIRMtchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvoiceReceiptMatchTableset[],
}
}

