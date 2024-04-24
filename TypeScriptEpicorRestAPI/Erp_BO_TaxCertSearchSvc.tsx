import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TaxCertSearchSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/$metadata", {
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
   Description: Get TaxCertSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxCertSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxTranRow
   */  
export function get_TaxCertSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxCertSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxCertSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches", {
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
   Summary: Calls GetByID to retrieve the TaxCertSearch item
   Description: Calls GetByID to retrieve the TaxCertSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxCertSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxTranRow
   */  
export function get_TaxCertSearches_Company_TranDate_TranNum(Company:string, TranDate:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches(" + Company + "," + TranDate + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaxTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxCertSearch for the service
   Description: Calls UpdateExt to update TaxCertSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxCertSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxCertSearches_Company_TranDate_TranNum(Company:string, TranDate:string, TranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches(" + Company + "," + TranDate + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete TaxCertSearch item
   Description: Call UpdateExt to delete TaxCertSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxCertSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDate Desc: TranDate   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxCertSearches_Company_TranDate_TranNum(Company:string, TranDate:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches(" + Company + "," + TranDate + "," + TranNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranListRow)
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
export function get_GetRows(whereClauseTaxTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTaxTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxTran=" + whereClauseTaxTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(tranDate:string, tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tranDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranDate=" + tranDate
   }
   if(typeof tranNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranNum=" + tranNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListPercCertificates
   Description: Returns List of AR Perception Certificates.
   OperationID: GetListPercCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListPercCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPercCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListPercCertificates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetListPercCertificates", {
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
   Summary: Invoke method GetNewTaxTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetNewTaxTran", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxTranListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxTranRow[],
}

export interface Erp_Tablesets_TaxTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  date of transaction.  */  
   "TranDate":string,
      /**  a number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "ARInvoiceNum":number,
      /**  identifies a Tax Region master record.  */  
   "TaxRegionCode":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  */  
   "SourceModule":string,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "TaxableAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "TaxAmt":number,
      /**  Company Tax ID  */  
   "CompTaxID":string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   "VendorTaxID":string,
      /**  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  */  
   "CustomerTaxID":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Sales tax report ID  */  
   "ReportID":string,
      /**  Tax Report Date  */  
   "ReportDate":string,
      /**  Invoice Line Number associated with this TaxTran  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this TaxTran.  */  
   "SeqNum":number,
      /**  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  */  
   "InvoiceMemo":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  */  
   "TaxCatID":string,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Legal Number for tax statement  */  
   "LegalNumber":string,
      /**  Date Tax Document was printed  */  
   "TaxPrintDate":string,
      /**  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  Key to link to Payment  */  
   "HeadNum":number,
      /**  Field To save the AR Invoice Date  */  
   "ARInvoiceDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  date of transaction.  */  
   "TranDate":string,
      /**  a number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "ARInvoiceNum":number,
      /**  Tax Region is in the European Community.  */  
   "InEC":boolean,
      /**  identifies a Tax Region master record.  */  
   "TaxRegionCode":string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  */  
   "SourceModule":string,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "TaxableAmt":number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   "DocTaxableAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   "DocTaxAmt":number,
      /**  Company Tax ID  */  
   "CompTaxID":string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   "VendorTaxID":string,
      /**  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  */  
   "CustomerTaxID":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Exchange rate that will be used for this invoice.  Defaults from CurrRate.CurrentRate.  */  
   "ExchangeRate":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Sales tax report ID  */  
   "ReportID":string,
      /**  Indicates if this report closed.  */  
   "Posted":boolean,
      /**  Posting Date  */  
   "PostDate":string,
      /**  Tax Report Date  */  
   "ReportDate":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.   Allow the VAT report to Keep seperate totals for the 2 records used for this transaction.  */  
   "ECAcquisitionSeq":number,
      /**  Invoice Line Number associated with this TaxTran  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this TaxTran.  */  
   "SeqNum":number,
      /**  Indicates if this tax transaction is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  The reportable sales amount to the tax jurisdiction.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  */  
   "DocReportableAmt":number,
      /**  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  */  
   "InvoiceMemo":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  */  
   "TaxCatID":string,
      /**  Rate Code  */  
   "RateCode":string,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Tax Rate Date  */  
   "TaxRateDate":string,
      /**  Legal Number for tax statement  */  
   "LegalNumber":string,
      /**  Date Tax Document was printed  */  
   "TaxPrintDate":string,
      /**  Indicates if Tax Statement was posted  */  
   "TaxPosted":boolean,
      /**  Date Tax Statement was posted  */  
   "TaxPostDate":string,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution Date  */  
   "ResolutionDate":string,
      /**  EU Third Party flag  */  
   "EUThirdParty":boolean,
      /**  If field is non-blank it is considered exempt.  */  
   "TaxExempt":string,
      /**  Key to link to Payment  */  
   "HeadNum":number,
      /**  The amount of tax recoverable (deductible).  */  
   "RecoverableAmt":number,
      /**  The amount of tax recoverable (deductible)  */  
   "DocRecoverableAmt":number,
      /**  The amout of tax recoverable (deductible) in Rpt1 currency  */  
   "Rpt1RecoverableAmt":number,
      /**  Tha amount of tax recoverable (deductible) in RPT2 currency.  */  
   "Rpt2RecoverableAmt":number,
      /**  The amount of tax recoverable (deductible) in RPT3 currency  */  
   "Rpt3RecoverableAmt":number,
      /**  Field To save the AR Invoice Date  */  
   "ARInvoiceDate":string,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt1TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt2TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "Rpt3TaxAmtVar":number,
      /**  Reverse Tax Report Category  */  
   "RevRptCatCode":string,
      /**  APTranNo  */  
   "APTranNo":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Return Flag  */  
   "ReturnFlag":boolean,
      /**  BookID  */  
   "BookID":string,
      /**  GL Journal Code  associated with this TaxTran  */  
   "JournalCode":string,
      /**  GL Journal Number  associated with this TaxTran  */  
   "JournalNum":number,
      /**  GL Journal Line  associated with this TaxTran  */  
   "JournalLine":number,
      /**  OneTimeID  */  
   "COOneTimeID":string,
      /**  Vendor Tax ID  */  
   "TempVendorTaxID":string,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  Indicate that record was created for Reverse transaction  */  
   "Reverse":boolean,
      /**  TranType  */  
   "TranType":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  NLICPReportID  */  
   "NLICPReportID":string,
      /**  MscNum  */  
   "MscNum":number,
      /**  MiscCode  */  
   "MiscCode":string,
   "SourceTranDocTypeID":string,
   "TransactionSource":string,
   "SourceLegalNumber":string,
   "BitFlag":number,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "ReportIDDescription":string,
   "TaxRateCodeDescription":string,
   "TaxRegionCodeDescription":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCity":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCountry":string,
   "VendorNumAddress1":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param tranDate
      @param tranNum
   */  
export interface DeleteByID_input{
   tranDate:string,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaxCertListTableset{
   TaxTranList:Erp_Tablesets_TaxTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxCertSearchTableset{
   TaxTran:Erp_Tablesets_TaxTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaxTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  date of transaction.  */  
   TranDate:string,
      /**  a number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  identifies a Tax Region master record.  */  
   TaxRegionCode:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  */  
   SourceModule:string,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   TaxableAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   TaxAmt:number,
      /**  Company Tax ID  */  
   CompTaxID:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   VendorTaxID:string,
      /**  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  */  
   CustomerTaxID:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Sales tax report ID  */  
   ReportID:string,
      /**  Tax Report Date  */  
   ReportDate:string,
      /**  Invoice Line Number associated with this TaxTran  */  
   InvoiceLine:number,
      /**  The sequence number associated with this TaxTran.  */  
   SeqNum:number,
      /**  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  */  
   InvoiceMemo:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  */  
   TaxCatID:string,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Legal Number for tax statement  */  
   LegalNumber:string,
      /**  Date Tax Document was printed  */  
   TaxPrintDate:string,
      /**  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  Key to link to Payment  */  
   HeadNum:number,
      /**  Field To save the AR Invoice Date  */  
   ARInvoiceDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  date of transaction.  */  
   TranDate:string,
      /**  a number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  Tax Region is in the European Community.  */  
   InEC:boolean,
      /**  identifies a Tax Region master record.  */  
   TaxRegionCode:string,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  */  
   SourceModule:string,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   TaxableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   DocTaxableAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   DocTaxAmt:number,
      /**  Company Tax ID  */  
   CompTaxID:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   VendorTaxID:string,
      /**  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  */  
   CustomerTaxID:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Exchange rate that will be used for this invoice.  Defaults from CurrRate.CurrentRate.  */  
   ExchangeRate:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Sales tax report ID  */  
   ReportID:string,
      /**  Indicates if this report closed.  */  
   Posted:boolean,
      /**  Posting Date  */  
   PostDate:string,
      /**  Tax Report Date  */  
   ReportDate:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.   Allow the VAT report to Keep seperate totals for the 2 records used for this transaction.  */  
   ECAcquisitionSeq:number,
      /**  Invoice Line Number associated with this TaxTran  */  
   InvoiceLine:number,
      /**  The sequence number associated with this TaxTran.  */  
   SeqNum:number,
      /**  Indicates if this tax transaction is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  The reportable sales amount to the tax jurisdiction.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  */  
   DocReportableAmt:number,
      /**  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  */  
   InvoiceMemo:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  */  
   TaxCatID:string,
      /**  Rate Code  */  
   RateCode:string,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Tax Rate Date  */  
   TaxRateDate:string,
      /**  Legal Number for tax statement  */  
   LegalNumber:string,
      /**  Date Tax Document was printed  */  
   TaxPrintDate:string,
      /**  Indicates if Tax Statement was posted  */  
   TaxPosted:boolean,
      /**  Date Tax Statement was posted  */  
   TaxPostDate:string,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution Date  */  
   ResolutionDate:string,
      /**  EU Third Party flag  */  
   EUThirdParty:boolean,
      /**  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  Key to link to Payment  */  
   HeadNum:number,
      /**  The amount of tax recoverable (deductible).  */  
   RecoverableAmt:number,
      /**  The amount of tax recoverable (deductible)  */  
   DocRecoverableAmt:number,
      /**  The amout of tax recoverable (deductible) in Rpt1 currency  */  
   Rpt1RecoverableAmt:number,
      /**  Tha amount of tax recoverable (deductible) in RPT2 currency.  */  
   Rpt2RecoverableAmt:number,
      /**  The amount of tax recoverable (deductible) in RPT3 currency  */  
   Rpt3RecoverableAmt:number,
      /**  Field To save the AR Invoice Date  */  
   ARInvoiceDate:string,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt1TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt2TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt3TaxAmtVar:number,
      /**  Reverse Tax Report Category  */  
   RevRptCatCode:string,
      /**  APTranNo  */  
   APTranNo:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Return Flag  */  
   ReturnFlag:boolean,
      /**  BookID  */  
   BookID:string,
      /**  GL Journal Code  associated with this TaxTran  */  
   JournalCode:string,
      /**  GL Journal Number  associated with this TaxTran  */  
   JournalNum:number,
      /**  GL Journal Line  associated with this TaxTran  */  
   JournalLine:number,
      /**  OneTimeID  */  
   COOneTimeID:string,
      /**  Vendor Tax ID  */  
   TempVendorTaxID:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  Indicate that record was created for Reverse transaction  */  
   Reverse:boolean,
      /**  TranType  */  
   TranType:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  NLICPReportID  */  
   NLICPReportID:string,
      /**  MscNum  */  
   MscNum:number,
      /**  MiscCode  */  
   MiscCode:string,
   SourceTranDocTypeID:string,
   TransactionSource:string,
   SourceLegalNumber:string,
   BitFlag:number,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   ReportIDDescription:string,
   TaxRateCodeDescription:string,
   TaxRegionCodeDescription:string,
   VendorNumDefaultFOB:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumAddress1:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
   VendorNumZIP:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtTaxCertSearchTableset{
   TaxTran:Erp_Tablesets_TaxTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param tranDate
      @param tranNum
   */  
export interface GetByID_input{
   tranDate:string,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TaxCertSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TaxCertSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TaxCertSearchTableset[],
}

   /** Required : 
      @param taxTranWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListPercCertificates_input{
   taxTranWhereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListPercCertificates_output{
   returnObj:Erp_Tablesets_TaxCertListTableset[],
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
   returnObj:Erp_Tablesets_TaxCertListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param tranDate
   */  
export interface GetNewTaxTran_input{
   ds:Erp_Tablesets_TaxCertSearchTableset[],
   tranDate:string,
}

export interface GetNewTaxTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxCertSearchTableset[],
}
}

   /** Required : 
      @param whereClauseTaxTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTaxTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TaxCertSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtTaxCertSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTaxCertSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TaxCertSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxCertSearchTableset[],
}
}

