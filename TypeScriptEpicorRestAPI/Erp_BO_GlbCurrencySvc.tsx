import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GlbCurrencySvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/$metadata", {
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
   Description: Get GlbCurrencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrencies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrencyRow
   */  
export function get_GlbCurrencies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrencies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies", {
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
   Summary: Calls GetByID to retrieve the GlbCurrency item
   Description: Calls GetByID to retrieve the GlbCurrency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbCurrencyCode Desc: GlbCurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
   */  
export function get_GlbCurrencies_Company_GlbCompany_GlbCurrencyCode(Company:string, GlbCompany:string, GlbCurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies(" + Company + "," + GlbCompany + "," + GlbCurrencyCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCurrency for the service
   Description: Calls UpdateExt to update GlbCurrency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbCurrencyCode Desc: GlbCurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCurrencies_Company_GlbCompany_GlbCurrencyCode(Company:string, GlbCompany:string, GlbCurrencyCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies(" + Company + "," + GlbCompany + "," + GlbCurrencyCode + ")", {
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
   Summary: Call UpdateExt to delete GlbCurrency item
   Description: Call UpdateExt to delete GlbCurrency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbCurrencyCode Desc: GlbCurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCurrencies_Company_GlbCompany_GlbCurrencyCode(Company:string, GlbCompany:string, GlbCurrencyCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies(" + Company + "," + GlbCompany + "," + GlbCurrencyCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrencyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyListRow)
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
export function get_GetRows(whereClauseGlbCurrency:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbCurrency!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCurrency=" + whereClauseGlbCurrency
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(glbCompany:string, glbCurrencyCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof glbCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCompany=" + glbCompany
   }
   if(typeof glbCurrencyCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCurrencyCode=" + glbCurrencyCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GetList" + params, {
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
   Summary: Invoke method GetNewGlbCurrency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCurrency(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GetNewGlbCurrency", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrencyListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrencyRow[],
}

export interface Erp_Tablesets_GlbCurrencyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "DocumentDesc":string,
      /**  Notes the about the Currency.  */  
   "Note":string,
      /**   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  */  
   "UnRealLossDiv":string,
      /**   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   "UnRealLossDept":string,
      /**   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   "UnRealLossChart":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**  Indicates if the currency is active  */  
   "Inactive":boolean,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   "MaintRate":boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "BaseCurr":boolean,
      /**  Indicates if this is a reporting currency  */  
   "ReportCurr":boolean,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   "GlobalCurr":boolean,
      /**  Determines whether or not this currency record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Currency Code from Source Company  */  
   "GlbCurrencyCode":string,
      /**  Currency ID from Source Company  */  
   "GlbCurrencyID":string,
      /**  Source Company  */  
   "GlbCompany":string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   "Skipped":boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   "ReportCurrPos":number,
   "DecimalsCost":number,
   "DecimalsGeneral":number,
   "DecimalsPrice":number,
   "RoundMltpExtPrice":number,
   "RoundMltpExtTax":number,
   "RoundMltpTotalAmt":number,
   "RoundMltpTotalTax":number,
   "RoundMltpUnitPrice":number,
   "RoundMltpUnitTax":number,
   "RoundRuleExtPrice":number,
   "RoundRuleExtTax":number,
   "RoundRuleTotalAmt":number,
   "RoundRuleTotalTax":number,
   "RoundRuleUnitPrice":number,
   "RoundRuleUnitTax":number,
   "RoundTolerance":number,
   "ISONumber":number,
   "StoreID":string,
   "RoundMltpAnnualCharge":number,
   "RoundMltpPeriodCharge":number,
   "RoundRuleAnnualCharge":number,
   "RoundRulePeriodCharge":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency.CurrencyID to link to (new or existing)  */  
   "LinkCurrencyID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCurrencyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "DocumentDesc":string,
      /**  Notes the about the Currency.  */  
   "Note":string,
      /**   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  */  
   "UnRealLossDiv":string,
      /**   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   "UnRealLossDept":string,
      /**   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   "UnRealLossChart":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**  Indicates if the currency is active  */  
   "Inactive":boolean,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   "MaintRate":boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "BaseCurr":boolean,
      /**  Indicates if this is a reporting currency  */  
   "ReportCurr":boolean,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   "GlobalCurr":boolean,
      /**  Determines whether or not this currency record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Currency Code from Source Company  */  
   "GlbCurrencyCode":string,
      /**  Currency ID from Source Company  */  
   "GlbCurrencyID":string,
      /**  Source Company  */  
   "GlbCompany":string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   "Skipped":boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   "ReportCurrPos":number,
   "DecimalsCost":number,
   "DecimalsGeneral":number,
   "DecimalsPrice":number,
   "RoundMltpExtPrice":number,
   "RoundMltpExtTax":number,
   "RoundMltpTotalAmt":number,
   "RoundMltpTotalTax":number,
   "RoundMltpUnitPrice":number,
   "RoundMltpUnitTax":number,
   "RoundRuleExtPrice":number,
   "RoundRuleExtTax":number,
   "RoundRuleTotalAmt":number,
   "RoundRuleTotalTax":number,
   "RoundRuleUnitPrice":number,
   "RoundRuleUnitTax":number,
   "RoundTolerance":number,
   "ISONumber":number,
   "StoreID":string,
   "RoundMltpAnnualCharge":number,
   "RoundMltpPeriodCharge":number,
   "RoundRuleAnnualCharge":number,
   "RoundRulePeriodCharge":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAFIPCode  */  
   "AGAFIPCode":string,
      /**  ISOCurrCode  */  
   "ISOCurrCode":string,
      /**  ProcessorNum  */  
   "ProcessorNum":number,
      /**  Currency.CurrencyCode to link to (new or existing)  */  
   "LinkCurrencyCode":string,
      /**  Currency.CurrencyID to link to (new or existing)  */  
   "LinkCurrencyID":string,
      /**  Description of the local Currency  */  
   "LocalDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
   */  
export interface DeleteByID_input{
   glbCompany:string,
   glbCurrencyCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbCurrencyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  Notes the about the Currency.  */  
   Note:string,
      /**   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  */  
   UnRealLossDiv:string,
      /**   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   UnRealLossDept:string,
      /**   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   UnRealLossChart:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   MaintRate:boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   GlobalCurr:boolean,
      /**  Determines whether or not this currency record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Currency Code from Source Company  */  
   GlbCurrencyCode:string,
      /**  Currency ID from Source Company  */  
   GlbCurrencyID:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   Skipped:boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
   DecimalsCost:number,
   DecimalsGeneral:number,
   DecimalsPrice:number,
   RoundMltpExtPrice:number,
   RoundMltpExtTax:number,
   RoundMltpTotalAmt:number,
   RoundMltpTotalTax:number,
   RoundMltpUnitPrice:number,
   RoundMltpUnitTax:number,
   RoundRuleExtPrice:number,
   RoundRuleExtTax:number,
   RoundRuleTotalAmt:number,
   RoundRuleTotalTax:number,
   RoundRuleUnitPrice:number,
   RoundRuleUnitTax:number,
   RoundTolerance:number,
   ISONumber:number,
   StoreID:string,
   RoundMltpAnnualCharge:number,
   RoundMltpPeriodCharge:number,
   RoundRuleAnnualCharge:number,
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency.CurrencyID to link to (new or existing)  */  
   LinkCurrencyID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrencyListTableset{
   GlbCurrencyList:Erp_Tablesets_GlbCurrencyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbCurrencyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  Notes the about the Currency.  */  
   Note:string,
      /**   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  */  
   UnRealLossDiv:string,
      /**   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   UnRealLossDept:string,
      /**   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  */  
   UnRealLossChart:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   MaintRate:boolean,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   GlobalCurr:boolean,
      /**  Determines whether or not this currency record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Currency Code from Source Company  */  
   GlbCurrencyCode:string,
      /**  Currency ID from Source Company  */  
   GlbCurrencyID:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   Skipped:boolean,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
   DecimalsCost:number,
   DecimalsGeneral:number,
   DecimalsPrice:number,
   RoundMltpExtPrice:number,
   RoundMltpExtTax:number,
   RoundMltpTotalAmt:number,
   RoundMltpTotalTax:number,
   RoundMltpUnitPrice:number,
   RoundMltpUnitTax:number,
   RoundRuleExtPrice:number,
   RoundRuleExtTax:number,
   RoundRuleTotalAmt:number,
   RoundRuleTotalTax:number,
   RoundRuleUnitPrice:number,
   RoundRuleUnitTax:number,
   RoundTolerance:number,
   ISONumber:number,
   StoreID:string,
   RoundMltpAnnualCharge:number,
   RoundMltpPeriodCharge:number,
   RoundRuleAnnualCharge:number,
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAFIPCode  */  
   AGAFIPCode:string,
      /**  ISOCurrCode  */  
   ISOCurrCode:string,
      /**  ProcessorNum  */  
   ProcessorNum:number,
      /**  Currency.CurrencyCode to link to (new or existing)  */  
   LinkCurrencyCode:string,
      /**  Currency.CurrencyID to link to (new or existing)  */  
   LinkCurrencyID:string,
      /**  Description of the local Currency  */  
   LocalDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrencyTableset{
   GlbCurrency:Erp_Tablesets_GlbCurrencyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbCurrencyTableset{
   GlbCurrency:Erp_Tablesets_GlbCurrencyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param glbCompany
      @param glbCurrencyCode
   */  
export interface GetByID_input{
   glbCompany:string,
   glbCurrencyCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbCurrencyTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbCurrencyTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbCurrencyTableset[],
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
   returnObj:Erp_Tablesets_GlbCurrencyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewGlbCurrency_input{
   ds:Erp_Tablesets_GlbCurrencyTableset[],
   glbCompany:string,
}

export interface GetNewGlbCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}
}

   /** Required : 
      @param whereClauseGlbCurrency
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbCurrency:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbCurrencyTableset[],
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
   ds:Erp_Tablesets_UpdExtGlbCurrencyTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbCurrencyTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrencyTableset[],
}
}

