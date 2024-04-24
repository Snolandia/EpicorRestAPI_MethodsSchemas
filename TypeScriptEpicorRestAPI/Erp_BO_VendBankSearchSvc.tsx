import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.VendBankSearchSvc
// Description: Search of Vendor Bank
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/$metadata", {
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
   Description: Get VendBankSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendBankSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankRow
   */  
export function get_VendBankSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendBankSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendBankRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendBankSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches", {
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
   Summary: Calls GetByID to retrieve the VendBankSearch item
   Description: Calls GetByID to retrieve the VendBankSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBankSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendBankRow
   */  
export function get_VendBankSearches_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendBankRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches(" + Company + "," + VendorNum + "," + BankID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_VendBankRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendBankSearch for the service
   Description: Calls UpdateExt to update VendBankSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendBankSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendBankSearches_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches(" + Company + "," + VendorNum + "," + BankID + ")", {
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
   Summary: Call UpdateExt to delete VendBankSearch item
   Description: Call UpdateExt to delete VendBankSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendBankSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param BankID Desc: BankID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendBankSearches_Company_VendorNum_BankID(Company:string, VendorNum:string, BankID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches(" + Company + "," + VendorNum + "," + BankID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankListRow)
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
export function get_GetRows(whereClauseVendBank:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseVendBank!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendBank=" + whereClauseVendBank
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, bankID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof bankID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bankID=" + bankID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewVendBank
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendBank(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/GetNewVendBank", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendBankListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendBankRow[],
}

export interface Erp_Tablesets_VendBankListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Supplier Number  */  
   "VendorNum":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Supplier Bank Name  */  
   "BankName":string,
      /**  First Address Line of the Supplier Bank  */  
   "Address1":string,
      /**  Second Address Line of the Supplier Bank  */  
   "Address2":string,
      /**  Third Address Line of the Supplier Bank  */  
   "Address3":string,
      /**  City portion of the address of the Supplier Bank  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address of the Supplier Bank  */  
   "PostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "BankAcctNumber":string,
      /**  Name on the Bank Account.  */  
   "NameOnAccount":string,
      /**  Swift number of the bank.  */  
   "SwiftNum":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Bank Branch Code of the Supplier Bank  */  
   "BankBranchCode":string,
      /**  IBAN Code of the Supplier Bank  */  
   "IBANCode":string,
      /**  Sweden localization field, Credit Transfer Number  */  
   "SECreditTransNum":string,
      /**  Full Legal name  */  
   "LegalName":string,
      /**  Correspondence Account of the Supplier Bank  */  
   "CorrespAccount":string,
      /**  Local BIC of the Supplier Bank  */  
   "LocalBIC":string,
      /**  Free Form Bank Person Code. Used in localizations.  */  
   "BankPersonCode":string,
      /**  Supplier bank Account Type. Used in localizations.  */  
   "VendAccountType":string,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**   Denmark Localization
Bank Reference code  */  
   "BankRefCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress1":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress2":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress3":string,
      /**  Bank Charges (Used for Czech Republic CSF)  */  
   "BankCharges":string,
      /**  Bank Constant Symbol (Used for Czech Republic CSF)  */  
   "BankCnstSymbol":string,
      /**  Bank Special Symbol (Used for Czech Republic CSF)  */  
   "BankSpecSymbol":string,
      /**  Specifies the supplier's bank city.  */  
   "BCity":string,
      /**  Specifies the supplier's bank country.  */  
   "BCountryNum":number,
      /**  Specifies the supplier's postal code.  */  
   "BPostalCode":string,
      /**  Specifies the supplier's bank state/province.  */  
   "BState":string,
      /**  Receiving Bank Number.  Used in Japan localizations.  */  
   "ReceivingBankNum":string,
      /**  Receiving Branch Number.  Used in Japan localizations.  */  
   "ReceivingBranchNum":string,
   "PrimaryBank":boolean,
      /**  Bank Branch Code  */  
   "BankBranchCodeDescBankBranchCode":string,
      /**  Bank Branch Description  */  
   "BankBranchCodeDescDescription":string,
      /**  Country name  */  
   "CountryNumDescription":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  Name of the payment method  */  
   "PayMethodName":string,
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
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendBankRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Supplier Number  */  
   "VendorNum":number,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Supplier Bank Name  */  
   "BankName":string,
      /**  First Address Line of the Supplier Bank  */  
   "Address1":string,
      /**  Second Address Line of the Supplier Bank  */  
   "Address2":string,
      /**  Third Address Line of the Supplier Bank  */  
   "Address3":string,
      /**  City portion of the address of the Supplier Bank  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address of the Supplier Bank  */  
   "PostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "BankAcctNumber":string,
      /**  Name on the Bank Account.  */  
   "NameOnAccount":string,
      /**  Swift number of the bank.  */  
   "SwiftNum":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Bank Branch Code of the Supplier Bank  */  
   "BankBranchCode":string,
      /**  IBAN Code of the Supplier Bank  */  
   "IBANCode":string,
      /**  Sweden localization field, Credit Transfer Number  */  
   "SECreditTransNum":string,
      /**  Full Legal name  */  
   "LegalName":string,
      /**  Correspondence Account of the Supplier Bank  */  
   "CorrespAccount":string,
      /**  Local BIC of the Supplier Bank  */  
   "LocalBIC":string,
      /**  Free Form Bank Person Code. Used in localizations.  */  
   "BankPersonCode":string,
      /**  Supplier bank Account Type. Used in localizations.  */  
   "VendAccountType":string,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**   Denmark Localization
Bank Reference code  */  
   "BankRefCode":string,
      /**  AllowAsAltRemitToBank  */  
   "AllowAsAltRemitToBank":boolean,
      /**  DFIIdentification  */  
   "DFIIdentification":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHDTAID  */  
   "CHDTAID":string,
      /**  CHISRPartyID  */  
   "CHISRPartyID":string,
      /**  FeeOwnership  */  
   "FeeOwnership":string,
      /**  POBankAcctNum  */  
   "POBankAcctNum":string,
      /**  BankCustNum  */  
   "BankCustNum":string,
      /**  BankCustNumberStartPos  */  
   "BankCustNumberStartPos":number,
      /**  BankCustNumberLen  */  
   "BankCustNumberLen":number,
      /**  Specifies the supplier's bank address.  */  
   "BAddress1":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress2":string,
      /**  Specifies the supplier's bank address.  */  
   "BAddress3":string,
      /**  Bank Charges (Used for Czech Republic CSF)  */  
   "BankCharges":string,
      /**  Bank Constant Symbol (Used for Czech Republic CSF)  */  
   "BankCnstSymbol":string,
      /**  Bank Special Symbol (Used for Czech Republic CSF)  */  
   "BankSpecSymbol":string,
      /**  Bank type of electronic payment transactions  */  
   "BankType":string,
      /**  Specifies the supplier's bank city.  */  
   "BCity":string,
      /**  Specifies the supplier's bank country.  */  
   "BCountryNum":number,
      /**  Specifies the supplier's postal code.  */  
   "BPostalCode":string,
      /**  Specifies the supplier's bank state/province.  */  
   "BState":string,
      /**  Norway CSF: Determines where bank cheque is sent.  */  
   "NOChequeCode":string,
      /**  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  */  
   "NOFeeCostCode":string,
      /**  Receiver Name.  Used in Japan localizations.  */  
   "ReceiverName":string,
      /**  Receiving Bank Name.  Used in Japan localizations.  */  
   "ReceivingBankName":string,
      /**  Receiving Bank Number.  Used in Japan localizations.  */  
   "ReceivingBankNum":string,
      /**  Receiving Branch Name.  Used in Japan localizations.  */  
   "ReceivingBranchName":string,
      /**  Receiving Branch Number.  Used in Japan localizations.  */  
   "ReceivingBranchNum":string,
      /**  SEBankFeeCostOwner  */  
   "SEBankFeeCostOwner":string,
      /**  PEDetractionsNBA  */  
   "PEDetractionsNBA":boolean,
      /**  MX SAT Code  */  
   "MXSATCode":string,
      /**  MX SAT Name Short  */  
   "MXSATNameShort":string,
      /**  MX SAT Name Full  */  
   "MXSATNameFull":string,
      /**  DKCreditorNum  */  
   "DKCreditorNum":string,
      /**  A supplier alias used to make and receive payments.  */  
   "PayID":string,
      /**  ClearSystemIDCode  */  
   "ClearSystemIDCode":string,
      /**  MemberID  */  
   "MemberID":string,
   "BCountry":number,
      /**  Postal Account Number in format XX-#####V-P (CSF Switzerland)  */  
   "CHScrPOBankAcctNum":string,
   "PrimaryBank":boolean,
      /**  ISR Party Number in format XX-#####V-P (CSF Switzerland)  */  
   "CHScrISRPartyID":string,
   "BitFlag":number,
   "BankBranchCodeDescDescription":string,
   "BankBranchCodeDescBankBranchCode":string,
   "BCountryNumDescription":string,
   "CountryNumDescription":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "VendorNumCity":string,
   "VendorNumState":string,
   "VendorNumVendorID":string,
   "VendorNumAddress1":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCountry":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param vendorNum
      @param bankID
   */  
export interface DeleteByID_input{
   vendorNum:number,
   bankID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtVendBankSearchTableset{
   VendBank:Erp_Tablesets_VendBankRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendBankListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Supplier Number  */  
   VendorNum:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Supplier Bank Name  */  
   BankName:string,
      /**  First Address Line of the Supplier Bank  */  
   Address1:string,
      /**  Second Address Line of the Supplier Bank  */  
   Address2:string,
      /**  Third Address Line of the Supplier Bank  */  
   Address3:string,
      /**  City portion of the address of the Supplier Bank  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of the address of the Supplier Bank  */  
   PostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   BankAcctNumber:string,
      /**  Name on the Bank Account.  */  
   NameOnAccount:string,
      /**  Swift number of the bank.  */  
   SwiftNum:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Bank Branch Code of the Supplier Bank  */  
   BankBranchCode:string,
      /**  IBAN Code of the Supplier Bank  */  
   IBANCode:string,
      /**  Sweden localization field, Credit Transfer Number  */  
   SECreditTransNum:string,
      /**  Full Legal name  */  
   LegalName:string,
      /**  Correspondence Account of the Supplier Bank  */  
   CorrespAccount:string,
      /**  Local BIC of the Supplier Bank  */  
   LocalBIC:string,
      /**  Free Form Bank Person Code. Used in localizations.  */  
   BankPersonCode:string,
      /**  Supplier bank Account Type. Used in localizations.  */  
   VendAccountType:string,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**   Denmark Localization
Bank Reference code  */  
   BankRefCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress1:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress2:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress3:string,
      /**  Bank Charges (Used for Czech Republic CSF)  */  
   BankCharges:string,
      /**  Bank Constant Symbol (Used for Czech Republic CSF)  */  
   BankCnstSymbol:string,
      /**  Bank Special Symbol (Used for Czech Republic CSF)  */  
   BankSpecSymbol:string,
      /**  Specifies the supplier's bank city.  */  
   BCity:string,
      /**  Specifies the supplier's bank country.  */  
   BCountryNum:number,
      /**  Specifies the supplier's postal code.  */  
   BPostalCode:string,
      /**  Specifies the supplier's bank state/province.  */  
   BState:string,
      /**  Receiving Bank Number.  Used in Japan localizations.  */  
   ReceivingBankNum:string,
      /**  Receiving Branch Number.  Used in Japan localizations.  */  
   ReceivingBranchNum:string,
   PrimaryBank:boolean,
      /**  Bank Branch Code  */  
   BankBranchCodeDescBankBranchCode:string,
      /**  Bank Branch Description  */  
   BankBranchCodeDescDescription:string,
      /**  Country name  */  
   CountryNumDescription:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  Name of the payment method  */  
   PayMethodName:string,
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
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendBankListTableset{
   VendBankList:Erp_Tablesets_VendBankListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendBankRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Supplier Number  */  
   VendorNum:number,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Supplier Bank Name  */  
   BankName:string,
      /**  First Address Line of the Supplier Bank  */  
   Address1:string,
      /**  Second Address Line of the Supplier Bank  */  
   Address2:string,
      /**  Third Address Line of the Supplier Bank  */  
   Address3:string,
      /**  City portion of the address of the Supplier Bank  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of the address of the Supplier Bank  */  
   PostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   BankAcctNumber:string,
      /**  Name on the Bank Account.  */  
   NameOnAccount:string,
      /**  Swift number of the bank.  */  
   SwiftNum:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Bank Branch Code of the Supplier Bank  */  
   BankBranchCode:string,
      /**  IBAN Code of the Supplier Bank  */  
   IBANCode:string,
      /**  Sweden localization field, Credit Transfer Number  */  
   SECreditTransNum:string,
      /**  Full Legal name  */  
   LegalName:string,
      /**  Correspondence Account of the Supplier Bank  */  
   CorrespAccount:string,
      /**  Local BIC of the Supplier Bank  */  
   LocalBIC:string,
      /**  Free Form Bank Person Code. Used in localizations.  */  
   BankPersonCode:string,
      /**  Supplier bank Account Type. Used in localizations.  */  
   VendAccountType:string,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**   Denmark Localization
Bank Reference code  */  
   BankRefCode:string,
      /**  AllowAsAltRemitToBank  */  
   AllowAsAltRemitToBank:boolean,
      /**  DFIIdentification  */  
   DFIIdentification:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHDTAID  */  
   CHDTAID:string,
      /**  CHISRPartyID  */  
   CHISRPartyID:string,
      /**  FeeOwnership  */  
   FeeOwnership:string,
      /**  POBankAcctNum  */  
   POBankAcctNum:string,
      /**  BankCustNum  */  
   BankCustNum:string,
      /**  BankCustNumberStartPos  */  
   BankCustNumberStartPos:number,
      /**  BankCustNumberLen  */  
   BankCustNumberLen:number,
      /**  Specifies the supplier's bank address.  */  
   BAddress1:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress2:string,
      /**  Specifies the supplier's bank address.  */  
   BAddress3:string,
      /**  Bank Charges (Used for Czech Republic CSF)  */  
   BankCharges:string,
      /**  Bank Constant Symbol (Used for Czech Republic CSF)  */  
   BankCnstSymbol:string,
      /**  Bank Special Symbol (Used for Czech Republic CSF)  */  
   BankSpecSymbol:string,
      /**  Bank type of electronic payment transactions  */  
   BankType:string,
      /**  Specifies the supplier's bank city.  */  
   BCity:string,
      /**  Specifies the supplier's bank country.  */  
   BCountryNum:number,
      /**  Specifies the supplier's postal code.  */  
   BPostalCode:string,
      /**  Specifies the supplier's bank state/province.  */  
   BState:string,
      /**  Norway CSF: Determines where bank cheque is sent.  */  
   NOChequeCode:string,
      /**  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  */  
   NOFeeCostCode:string,
      /**  Receiver Name.  Used in Japan localizations.  */  
   ReceiverName:string,
      /**  Receiving Bank Name.  Used in Japan localizations.  */  
   ReceivingBankName:string,
      /**  Receiving Bank Number.  Used in Japan localizations.  */  
   ReceivingBankNum:string,
      /**  Receiving Branch Name.  Used in Japan localizations.  */  
   ReceivingBranchName:string,
      /**  Receiving Branch Number.  Used in Japan localizations.  */  
   ReceivingBranchNum:string,
      /**  SEBankFeeCostOwner  */  
   SEBankFeeCostOwner:string,
      /**  PEDetractionsNBA  */  
   PEDetractionsNBA:boolean,
      /**  MX SAT Code  */  
   MXSATCode:string,
      /**  MX SAT Name Short  */  
   MXSATNameShort:string,
      /**  MX SAT Name Full  */  
   MXSATNameFull:string,
      /**  DKCreditorNum  */  
   DKCreditorNum:string,
      /**  A supplier alias used to make and receive payments.  */  
   PayID:string,
      /**  ClearSystemIDCode  */  
   ClearSystemIDCode:string,
      /**  MemberID  */  
   MemberID:string,
   BCountry:number,
      /**  Postal Account Number in format XX-#####V-P (CSF Switzerland)  */  
   CHScrPOBankAcctNum:string,
   PrimaryBank:boolean,
      /**  ISR Party Number in format XX-#####V-P (CSF Switzerland)  */  
   CHScrISRPartyID:string,
   BitFlag:number,
   BankBranchCodeDescDescription:string,
   BankBranchCodeDescBankBranchCode:string,
   BCountryNumDescription:string,
   CountryNumDescription:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   VendorNumCity:string,
   VendorNumState:string,
   VendorNumVendorID:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendBankSearchTableset{
   VendBank:Erp_Tablesets_VendBankRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param bankID
   */  
export interface GetByID_input{
   vendorNum:number,
   bankID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VendBankSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VendBankSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VendBankSearchTableset[],
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
   returnObj:Erp_Tablesets_VendBankListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendBank_input{
   ds:Erp_Tablesets_VendBankSearchTableset[],
   vendorNum:number,
}

export interface GetNewVendBank_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendBankSearchTableset[],
}
}

   /** Required : 
      @param whereClauseVendBank
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseVendBank:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VendBankSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtVendBankSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVendBankSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VendBankSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendBankSearchTableset[],
}
}

