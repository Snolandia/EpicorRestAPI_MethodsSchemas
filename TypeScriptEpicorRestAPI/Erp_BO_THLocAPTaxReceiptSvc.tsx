import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.THLocAPTaxReceiptSvc
// Description: TH AP Tax Receipt Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/$metadata", {
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
   Description: Get THLocAPTaxReceipts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_THLocAPTaxReceipts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   */  
export function get_THLocAPTaxReceipts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/THLocAPTaxReceipts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_THLocAPTaxReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_THLocAPTaxReceipts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/THLocAPTaxReceipts", {
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
   Summary: Calls GetByID to retrieve the THLocAPTaxReceipt item
   Description: Calls GetByID to retrieve the THLocAPTaxReceipt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_THLocAPTaxReceipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranRow
   */  
export function get_THLocAPTaxReceipts_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/THLocAPTaxReceipts(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update THLocAPTaxReceipt for the service
   Description: Calls UpdateExt to update THLocAPTaxReceipt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_THLocAPTaxReceipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_THLocAPTaxReceipts_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/THLocAPTaxReceipts(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Summary: Call UpdateExt to delete THLocAPTaxReceipt item
   Description: Call UpdateExt to delete THLocAPTaxReceipt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_THLocAPTaxReceipt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranNo Desc: APTranNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_THLocAPTaxReceipts_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranNo:string, InvoiceNum:string, Voided:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/THLocAPTaxReceipts(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseAPTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTran=" + whereClauseAPTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(headNum:string, apTranNo:string, invoiceNum:string, voided:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }
   if(typeof apTranNo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "apTranNo=" + apTranNo
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
   if(typeof voided!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "voided=" + voided
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAPTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/GetNewAPTran", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.THLocAPTaxReceiptSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranRow[],
}

export interface Erp_Tablesets_APTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   "TranType":string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   "HeadNum":number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   "APTranNo":number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   "InvoiceNum":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   "Posted":boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "TranAmt":number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "DocTranAmt":number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DiscAmt":number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DocDiscAmt":number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   "Description":string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number of the related CheckHed.  */  
   "CheckNum":number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   "TranDate":string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   "GLPosted":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   "Voided":boolean,
      /**  UserID that created this APTran record.  */  
   "EntryPerson":string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   "VendorNum":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   "Comment":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Sales Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  The Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Indicates that this is prepayment.  */  
   "PrePayment":boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   "ContractRef":string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   "ContractRefDate":string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   "RefPONum":number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   "WHTCertificateNo":string,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Legal Number for the adjustment.  */  
   "AdjLegalNumber":string,
      /**  Transaction Document Type for the adjustment.  */  
   "AdjTranDocTypeID":string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Remarks  */  
   "Remarks":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Rate Group Code for transactions of type ADJ  */  
   "RateGrpCode":string,
      /**  Generation 1099 Date  */  
   "Gen1099Date":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from APInvHed  */  
   "CurrSymbol":string,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "InvoiceAmt":number,
   "DocInvoiceAmt":number,
   "InvoiceBal":number,
   "DocInvoiceBal":number,
   "NewBalance":number,
   "DocNewBalance":number,
      /**  Indicates if posting GL transactions.  */  
   "PostToGL":boolean,
   "DispTranAmt":number,
   "DocDispTranAmt":number,
   "CurrencyGainLoss":number,
   "AmtToAP":number,
   "DiscountDate":string,
   "DueDate":string,
   "TermsCode":string,
   "LockRate":boolean,
   "ExchangeRate":number,
   "ExpenseAmount":number,
   "DocExpenseAmount":number,
   "RefCodeEnabled":boolean,
   "TaxLinesExist":boolean,
   "MiscPayment":boolean,
   "NetAmount":number,
   "DocNetAmount":number,
      /**  Delimited list of possible Ref codes.  */  
   "RefCodeList":string,
   "DiscountAvailable":boolean,
   "GroupID":string,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   "ChangeExchangeRateResponse":string,
   "DebitMemo":boolean,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnPostedBal":number,
   "DocUnPostedBal":number,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolDocumentDesc":string,
   "CurrSymbolCurrDesc":string,
   "CurrSymbolCurrName":string,
   "CurrSymbolCurrSymbol":string,
   "CurrSymbolDocumentDesc":string,
   "TermsCodeDescription":string,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   "CPayLinked":boolean,
      /**  This is the source Company of the Central Payment linked invoice  */  
   "GlbCompany":string,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  The display gl account.  */  
   "DispGLAcct":string,
   "Rpt1DispTranAmt":number,
   "Rpt2DispTranAmt":number,
   "Rpt3DispTranAmt":number,
   "Rpt1NewBalance":number,
   "Rpt2NewBalance":number,
   "Rpt3NewBalance":number,
   "ApplyDate":string,
   "BaseSelfAssessedTax":number,
   "DocBaseSelfAssessedTax":number,
   "DocSelfAssessedTax":number,
   "SelfAssessedTax":number,
   "DocWithHoldTax":number,
   "WithHoldTax":number,
   "LegalNumMessage":string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   "LegalNumStyle":string,
      /**  Posting Error Message  */  
   "PostErrMess":string,
      /**  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  */  
   "PaymentDesc":string,
   "XRateLabel":string,
   "InvExchangeRate":number,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "InvoiceNumDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
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
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   "TranType":string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   "HeadNum":number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   "APTranNo":number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   "InvoiceNum":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   "Posted":boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "TranAmt":number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   "DocTranAmt":number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DiscAmt":number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   "DocDiscAmt":number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   "Description":string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number of the related CheckHed.  */  
   "CheckNum":number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   "TranDate":string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   "FiscalPeriod":number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   "GLPosted":boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   "Voided":boolean,
      /**  UserID that created this APTran record.  */  
   "EntryPerson":string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   "VendorNum":number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   "Comment":string,
      /**  The Tax Region for this payment.  */  
   "TaxRegionCode":string,
      /**  Sales Tax Amount.  */  
   "TaxAmt":number,
      /**  Tax Amount in the vendors currency.  */  
   "DocTaxAmt":number,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   "RoundDiff":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TranAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TranAmt":number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  The Legal Number for the record.  */  
   "LegalNumber":string,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "DocSelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt1SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt2SelfAssessAmt":number,
      /**  Self Assessment Tax Amount.  */  
   "Rpt3SelfAssessAmt":number,
      /**  Red Storno Flag  */  
   "RedStorno":boolean,
      /**  Indicates that this is prepayment.  */  
   "PrePayment":boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   "ContractRef":string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   "ContractRefDate":string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   "RefPONum":number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   "TaxReceiptDate":string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   "TaxReceiptNo":string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   "WHTCertificateDate":string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   "WHTCertificateNo":string,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   "GainLossType":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   "ReverseGL":boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   "RevalueDate":string,
      /**  Invoice Balance at the time of revaluation  */  
   "RevalueBal":number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   "DocRevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt1RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt2RevalueBal":number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   "Rpt3RevalueBal":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Legal Number for the adjustment.  */  
   "AdjLegalNumber":string,
      /**  Transaction Document Type for the adjustment.  */  
   "AdjTranDocTypeID":string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   "TranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Remarks  */  
   "Remarks":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  UrgentPayment  */  
   "UrgentPayment":boolean,
      /**  InvoiceRef  */  
   "InvoiceRef":string,
      /**  Rate Group Code for transactions of type ADJ  */  
   "RateGrpCode":string,
      /**  CNCFICode  */  
   "CNCFICode":string,
      /**  Generation 1099 Date  */  
   "Gen1099Date":string,
      /**  NOTranReason  */  
   "NOTranReason":string,
      /**  PEIsDetractionPayment  */  
   "PEIsDetractionPayment":boolean,
      /**  Code1099ID  */  
   "Code1099ID":string,
      /**  FormTypeID  */  
   "FormTypeID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  DocWhManAddAmt  */  
   "DocWhManAddAmt":number,
      /**  WhManAddAmt  */  
   "WhManAddAmt":number,
      /**  Rpt1WhManAddAmt  */  
   "Rpt1WhManAddAmt":number,
      /**  Rpt2WhManAddAmt  */  
   "Rpt2WhManAddAmt":number,
      /**  Rpt3WhManAddAmt  */  
   "Rpt3WhManAddAmt":number,
   "BaseAdjustAmt":number,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolDocumentDesc":string,
   "BaseSelfAssessedTax":number,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   "ChangeExchangeRateResponse":string,
   "CNCFICodeDescription":string,
      /**  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  */  
   "CopyRate":boolean,
      /**  The flag to indicate if this payment line is realted to Correction invoice with negative amount  */  
   "CorrectionInv":boolean,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   "CPayLinked":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyGainLoss":number,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from APInvHed  */  
   "CurrSymbol":string,
   "CurrSymbolCurrDesc":string,
   "CurrSymbolCurrName":string,
   "CurrSymbolCurrSymbol":string,
   "CurrSymbolDocumentDesc":string,
   "DebitMemo":boolean,
   "DisableFieldsForPCashDoc":boolean,
   "DiscountAvailable":boolean,
   "DiscountDate":string,
      /**  The display gl account.  */  
   "DispGLAcct":string,
   "DispTranAmt":number,
   "DocBaseSelfAssessedTax":number,
   "DocDispTranAmt":number,
   "DocExpenseAmount":number,
   "DocGainLossAmt":number,
   "DocInvoiceAmt":number,
   "DocInvoiceBal":number,
   "DocNetAmount":number,
   "DocNewBalance":number,
   "DocSelfAssessedTax":number,
   "DocUnPostedBal":number,
   "DocWithHoldTax":number,
      /**  If this flag is true then Copy Rate checkbox is Read Only  */  
   "DsblCopyRate":boolean,
   "DueDate":string,
   "ExchangeRate":number,
   "ExpenseAmount":number,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   "FullyPaid":boolean,
   "GainLossAmt":number,
      /**  This is the source Company of the Central Payment linked invoice  */  
   "GlbCompany":string,
   "GroupID":string,
      /**  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  */  
   "InitUrgentPayment":boolean,
   "InvExchangeRate":number,
   "InvoiceAmt":number,
   "InvoiceBal":number,
   "isDiscountforDebitM":boolean,
   "LegalNumMessage":string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   "LegalNumStyle":string,
   "LockRate":boolean,
   "MiscPayment":boolean,
   "NetAmount":number,
   "NewBalance":number,
      /**  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  */  
   "PaymentDesc":string,
      /**  Posting Error Message  */  
   "PostErrMess":string,
      /**  Indicates if posting GL transactions.  */  
   "PostToGL":boolean,
      /**  Print 1099  */  
   "Print1099":boolean,
   "RateGroupDescription":string,
   "RefCodeEnabled":boolean,
      /**  Delimited list of possible Ref codes.  */  
   "RefCodeList":string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   "RefCodeStatus":string,
   "Rpt1DispTranAmt":number,
   "Rpt1GainLossAmt":number,
   "Rpt1InvoiceAmt":number,
      /**  Invoice balance before adjustment in Rpt1 currency  */  
   "Rpt1InvoiceBal":number,
   "Rpt1NewBalance":number,
   "Rpt2DispTranAmt":number,
   "Rpt2GainLossAmt":number,
   "Rpt2InvoiceAmt":number,
      /**  Invoice balance before adjustment in Rpt2 currency  */  
   "Rpt2InvoiceBal":number,
   "Rpt2NewBalance":number,
   "Rpt3DispTranAmt":number,
   "Rpt3GainLossAmt":number,
   "Rpt3InvoiceAmt":number,
      /**  Report balance before adjustment in rpt3 currency  */  
   "Rpt3InvoiceBal":number,
   "Rpt3NewBalance":number,
   "SelfAssessedTax":number,
      /**  Indicates if tax records are created and posted for AP Invoice adjustment  */  
   "TaxableTransaction":boolean,
   "TaxLinesExist":boolean,
   "TermsCode":string,
   "TermsCodeDescription":string,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnPostedBal":number,
   "WithHoldTax":number,
   "XRateLabel":string,
   "AmtToAP":number,
   "ApplyDate":string,
   "InvoiceLegalNumber":string,
   "PLInvoiceReference":string,
      /**  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  */  
   "isPrecalcTax":boolean,
      /**  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  */  
   "PrepayApld":boolean,
      /**  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  */  
   "ManualTaxAdj":boolean,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "Code1099Description":string,
   "FormTypeDescription":string,
   "InvoiceNumDescription":string,
   "TaxRegionCodeDescription":string,
   "VendorNumState":string,
   "VendorNumCity":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param voided
   */  
export interface DeleteByID_input{
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
   voided:boolean,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   TranType:string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   HeadNum:number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   APTranNo:number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   InvoiceNum:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   Posted:boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   TranAmt:number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   DocTranAmt:number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DiscAmt:number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DocDiscAmt:number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   Description:string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number of the related CheckHed.  */  
   CheckNum:number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   TranDate:string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   FiscalYear:number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   GLPosted:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   Voided:boolean,
      /**  UserID that created this APTran record.  */  
   EntryPerson:string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   VendorNum:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   Comment:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Sales Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  The Legal Number for the record.  */  
   LegalNumber:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Indicates that this is prepayment.  */  
   PrePayment:boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   ContractRef:string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   ContractRefDate:string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   RefPONum:number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Legal Number for the adjustment.  */  
   AdjLegalNumber:string,
      /**  Transaction Document Type for the adjustment.  */  
   AdjTranDocTypeID:string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Remarks  */  
   Remarks:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Rate Group Code for transactions of type ADJ  */  
   RateGrpCode:string,
      /**  Generation 1099 Date  */  
   Gen1099Date:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from APInvHed  */  
   CurrSymbol:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   InvoiceAmt:number,
   DocInvoiceAmt:number,
   InvoiceBal:number,
   DocInvoiceBal:number,
   NewBalance:number,
   DocNewBalance:number,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
   DispTranAmt:number,
   DocDispTranAmt:number,
   CurrencyGainLoss:number,
   AmtToAP:number,
   DiscountDate:string,
   DueDate:string,
   TermsCode:string,
   LockRate:boolean,
   ExchangeRate:number,
   ExpenseAmount:number,
   DocExpenseAmount:number,
   RefCodeEnabled:boolean,
   TaxLinesExist:boolean,
   MiscPayment:boolean,
   NetAmount:number,
   DocNetAmount:number,
      /**  Delimited list of possible Ref codes.  */  
   RefCodeList:string,
   DiscountAvailable:boolean,
   GroupID:string,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   ChangeExchangeRateResponse:string,
   DebitMemo:boolean,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnPostedBal:number,
   DocUnPostedBal:number,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolDocumentDesc:string,
   CurrSymbolCurrDesc:string,
   CurrSymbolCurrName:string,
   CurrSymbolCurrSymbol:string,
   CurrSymbolDocumentDesc:string,
   TermsCodeDescription:string,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   CPayLinked:boolean,
      /**  This is the source Company of the Central Payment linked invoice  */  
   GlbCompany:string,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  The display gl account.  */  
   DispGLAcct:string,
   Rpt1DispTranAmt:number,
   Rpt2DispTranAmt:number,
   Rpt3DispTranAmt:number,
   Rpt1NewBalance:number,
   Rpt2NewBalance:number,
   Rpt3NewBalance:number,
   ApplyDate:string,
   BaseSelfAssessedTax:number,
   DocBaseSelfAssessedTax:number,
   DocSelfAssessedTax:number,
   SelfAssessedTax:number,
   DocWithHoldTax:number,
   WithHoldTax:number,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  */  
   PaymentDesc:string,
   XRateLabel:string,
   InvExchangeRate:number,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   InvoiceNumDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APTranListTableset{
   APTranList:Erp_Tablesets_APTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  */  
   TranType:string,
      /**  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  */  
   HeadNum:number,
      /**  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  */  
   APTranNo:number,
      /**  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  */  
   InvoiceNum:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  */  
   Posted:boolean,
      /**  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   TranAmt:number,
      /**  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  */  
   DocTranAmt:number,
      /**  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DiscAmt:number,
      /**  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  */  
   DocDiscAmt:number,
      /**  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  */  
   Description:string,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number of the related CheckHed.  */  
   CheckNum:number,
      /**  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  */  
   TranDate:string,
      /**   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  */  
   FiscalYear:number,
      /**  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  */  
   GLPosted:boolean,
      /**   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  */  
   Voided:boolean,
      /**  UserID that created this APTran record.  */  
   EntryPerson:string,
      /**  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  */  
   VendorNum:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  */  
   Comment:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Sales Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  The Legal Number for the record.  */  
   LegalNumber:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Indicates that this is prepayment.  */  
   PrePayment:boolean,
      /**  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  */  
   ContractRef:string,
      /**  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  */  
   ContractRefDate:string,
      /**  Reference Purchase Order Number for Prepayments.  */  
   RefPONum:number,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt Number (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate Number (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Legal Number for the adjustment.  */  
   AdjLegalNumber:string,
      /**  Transaction Document Type for the adjustment.  */  
   AdjTranDocTypeID:string,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Remarks  */  
   Remarks:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  UrgentPayment  */  
   UrgentPayment:boolean,
      /**  InvoiceRef  */  
   InvoiceRef:string,
      /**  Rate Group Code for transactions of type ADJ  */  
   RateGrpCode:string,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  Generation 1099 Date  */  
   Gen1099Date:string,
      /**  NOTranReason  */  
   NOTranReason:string,
      /**  PEIsDetractionPayment  */  
   PEIsDetractionPayment:boolean,
      /**  Code1099ID  */  
   Code1099ID:string,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  DocWhManAddAmt  */  
   DocWhManAddAmt:number,
      /**  WhManAddAmt  */  
   WhManAddAmt:number,
      /**  Rpt1WhManAddAmt  */  
   Rpt1WhManAddAmt:number,
      /**  Rpt2WhManAddAmt  */  
   Rpt2WhManAddAmt:number,
      /**  Rpt3WhManAddAmt  */  
   Rpt3WhManAddAmt:number,
   BaseAdjustAmt:number,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolDocumentDesc:string,
   BaseSelfAssessedTax:number,
      /**  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  */  
   ChangeExchangeRateResponse:string,
   CNCFICodeDescription:string,
      /**  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  */  
   CopyRate:boolean,
      /**  The flag to indicate if this payment line is realted to Correction invoice with negative amount  */  
   CorrectionInv:boolean,
      /**  Indicates if the related invoice is linked to a Central Payment invoice  */  
   CPayLinked:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyGainLoss:number,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from APInvHed  */  
   CurrSymbol:string,
   CurrSymbolCurrDesc:string,
   CurrSymbolCurrName:string,
   CurrSymbolCurrSymbol:string,
   CurrSymbolDocumentDesc:string,
   DebitMemo:boolean,
   DisableFieldsForPCashDoc:boolean,
   DiscountAvailable:boolean,
   DiscountDate:string,
      /**  The display gl account.  */  
   DispGLAcct:string,
   DispTranAmt:number,
   DocBaseSelfAssessedTax:number,
   DocDispTranAmt:number,
   DocExpenseAmount:number,
   DocGainLossAmt:number,
   DocInvoiceAmt:number,
   DocInvoiceBal:number,
   DocNetAmount:number,
   DocNewBalance:number,
   DocSelfAssessedTax:number,
   DocUnPostedBal:number,
   DocWithHoldTax:number,
      /**  If this flag is true then Copy Rate checkbox is Read Only  */  
   DsblCopyRate:boolean,
   DueDate:string,
   ExchangeRate:number,
   ExpenseAmount:number,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
   GainLossAmt:number,
      /**  This is the source Company of the Central Payment linked invoice  */  
   GlbCompany:string,
   GroupID:string,
      /**  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  */  
   InitUrgentPayment:boolean,
   InvExchangeRate:number,
   InvoiceAmt:number,
   InvoiceBal:number,
   isDiscountforDebitM:boolean,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
   LockRate:boolean,
   MiscPayment:boolean,
   NetAmount:number,
   NewBalance:number,
      /**  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  */  
   PaymentDesc:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
      /**  Print 1099  */  
   Print1099:boolean,
   RateGroupDescription:string,
   RefCodeEnabled:boolean,
      /**  Delimited list of possible Ref codes.  */  
   RefCodeList:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
   Rpt1DispTranAmt:number,
   Rpt1GainLossAmt:number,
   Rpt1InvoiceAmt:number,
      /**  Invoice balance before adjustment in Rpt1 currency  */  
   Rpt1InvoiceBal:number,
   Rpt1NewBalance:number,
   Rpt2DispTranAmt:number,
   Rpt2GainLossAmt:number,
   Rpt2InvoiceAmt:number,
      /**  Invoice balance before adjustment in Rpt2 currency  */  
   Rpt2InvoiceBal:number,
   Rpt2NewBalance:number,
   Rpt3DispTranAmt:number,
   Rpt3GainLossAmt:number,
   Rpt3InvoiceAmt:number,
      /**  Report balance before adjustment in rpt3 currency  */  
   Rpt3InvoiceBal:number,
   Rpt3NewBalance:number,
   SelfAssessedTax:number,
      /**  Indicates if tax records are created and posted for AP Invoice adjustment  */  
   TaxableTransaction:boolean,
   TaxLinesExist:boolean,
   TermsCode:string,
   TermsCodeDescription:string,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnPostedBal:number,
   WithHoldTax:number,
   XRateLabel:string,
   AmtToAP:number,
   ApplyDate:string,
   InvoiceLegalNumber:string,
   PLInvoiceReference:string,
      /**  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  */  
   isPrecalcTax:boolean,
      /**  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  */  
   PrepayApld:boolean,
      /**  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  */  
   ManualTaxAdj:boolean,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   Code1099Description:string,
   FormTypeDescription:string,
   InvoiceNumDescription:string,
   TaxRegionCodeDescription:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_THLocAPTaxReceiptTableset{
   APTran:Erp_Tablesets_APTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTHLocAPTaxReceiptTableset{
   APTran:Erp_Tablesets_APTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param headNum
      @param apTranNo
      @param invoiceNum
      @param voided
   */  
export interface GetByID_input{
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
   voided:boolean,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_THLocAPTaxReceiptTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_THLocAPTaxReceiptTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_THLocAPTaxReceiptTableset[],
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
   returnObj:Erp_Tablesets_APTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param apTranNo
      @param invoiceNum
   */  
export interface GetNewAPTran_input{
   ds:Erp_Tablesets_THLocAPTaxReceiptTableset[],
   headNum:number,
   apTranNo:number,
   invoiceNum:string,
}

export interface GetNewAPTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_THLocAPTaxReceiptTableset[],
}
}

   /** Required : 
      @param whereClauseAPTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_THLocAPTaxReceiptTableset[],
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
   ds:Erp_Tablesets_UpdExtTHLocAPTaxReceiptTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTHLocAPTaxReceiptTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_THLocAPTaxReceiptTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_THLocAPTaxReceiptTableset[],
}
}

