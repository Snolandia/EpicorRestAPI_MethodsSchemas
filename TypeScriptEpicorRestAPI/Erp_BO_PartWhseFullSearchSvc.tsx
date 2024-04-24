import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartWhseFullSearchSvc
// Description: BO to retrieve the records from PartWhse, unlike PartWhseSearch this BO
           does NOT filter the plants by cur-plant.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/$metadata", {
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
   Description: Get PartWhseFullSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartWhseFullSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWhseSearchRow
   */  
export function get_PartWhseFullSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartWhseFullSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartWhseFullSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches", {
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
   Summary: Calls GetByID to retrieve the PartWhseFullSearch item
   Description: Calls GetByID to retrieve the PartWhseFullSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWhseFullSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
   */  
export function get_PartWhseFullSearches_Company_PartNum_WarehouseCode(Company:string, PartNum:string, WarehouseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartWhseSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches(" + Company + "," + PartNum + "," + WarehouseCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartWhseSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartWhseFullSearch for the service
   Description: Calls UpdateExt to update PartWhseFullSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartWhseFullSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartWhseFullSearches_Company_PartNum_WarehouseCode(Company:string, PartNum:string, WarehouseCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches(" + Company + "," + PartNum + "," + WarehouseCode + ")", {
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
   Summary: Call UpdateExt to delete PartWhseFullSearch item
   Description: Call UpdateExt to delete PartWhseFullSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartWhseFullSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartWhseFullSearches_Company_PartNum_WarehouseCode(Company:string, PartNum:string, WarehouseCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches(" + Company + "," + PartNum + "," + WarehouseCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWhseSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchListRow)
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
export function get_GetRows(whereClausePartWhseSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartWhseSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartWhseSearch=" + whereClausePartWhseSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/GetRows" + params, {
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
export function get_GetByID(partNum:string, warehouseCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPartWhseSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartWhseSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartWhseSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartWhseSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartWhseSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/GetNewPartWhseSearch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartWhseSearchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartWhseSearchRow[],
}

export interface Erp_Tablesets_PartWhseSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Warehouse  */  
   "WarehouseCode":string,
      /**  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  */  
   "CountedDate":string,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   "OnHandQty":number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   "NonNettableQty":number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesReservedQty":number,
      /**   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickingQty":number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickedQty":number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   "JobReservedQty":number,
      /**  Uniquely indentifies the record.  */  
   "KBCode":string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   "MinimumQty":number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   "MaximumQty":number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   "SafetyQty":number,
      /**  Purchase order number  that the detail line item is linked to.  */  
   "KBPONUM":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "KBPOLine":number,
      /**  Kanban Warehouse  */  
   "KBWarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "KBBinNum":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "KBPlant":string,
      /**  Indicates the desired minimum on-hand Kanban quantity.  */  
   "KBQty":number,
   "AllocQty":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SalesAllocQty":number,
   "JobAllocQty":number,
   "JobUnfirmAllocQty":number,
      /**  Filled in by BO, not physically in the database  */  
   "Plant":string,
   "DefaultWhse":boolean,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  Determine if this Warehouse is a Shared Warehouse  */  
   "SharedWarehouse":boolean,
      /**  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  */  
   "RemotePlant":string,
      /**  Determines if a User has the rights to perform Adjustments on this Warehouse  */  
   "IsUserAllowed":boolean,
      /**  Plant Name  */  
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartWhseSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Warehouse  */  
   "WarehouseCode":string,
      /**  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  */  
   "CountedDate":string,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   "OnHandQty":number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   "NonNettableQty":number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesReservedQty":number,
      /**   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickingQty":number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickedQty":number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   "JobReservedQty":number,
      /**  Uniquely indentifies the record.  */  
   "KBCode":string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   "MinimumQty":number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   "MaximumQty":number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   "SafetyQty":number,
      /**  Purchase order number  that the detail line item is linked to.  */  
   "KBPONUM":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "KBPOLine":number,
      /**  Kanban Warehouse  */  
   "KBWarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "KBBinNum":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "KBPlant":string,
      /**  Indicates the desired minimum on-hand Kanban quantity.  */  
   "KBQty":number,
   "AllocQty":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SalesAllocQty":number,
   "JobAllocQty":number,
   "JobUnfirmAllocQty":number,
      /**  Filled in by BO, not physically in the database  */  
   "Plant":string,
   "DefaultWhse":boolean,
      /**  Determines if a User has the rights to perform Adjustments on this Warehouse  */  
   "IsUserAllowed":boolean,
      /**  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  */  
   "RemotePlant":string,
      /**  Determine if this Warehouse is a Shared Warehouse  */  
   "SharedWarehouse":boolean,
   "BitFlag":number,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param partNum
      @param warehouseCode
   */  
export interface DeleteByID_input{
   partNum:string,
   warehouseCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartWhseFullSearchTableset{
   PartWhseSearch:Erp_Tablesets_PartWhseSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartWhseSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Warehouse  */  
   WarehouseCode:string,
      /**  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  */  
   CountedDate:string,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   OnHandQty:number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   NonNettableQty:number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesReservedQty:number,
      /**   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickingQty:number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickedQty:number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   JobReservedQty:number,
      /**  Uniquely indentifies the record.  */  
   KBCode:string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   MinimumQty:number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   MaximumQty:number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   SafetyQty:number,
      /**  Purchase order number  that the detail line item is linked to.  */  
   KBPONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   KBPOLine:number,
      /**  Kanban Warehouse  */  
   KBWarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   KBBinNum:string,
      /**  Site Identifier. This field cannot be blank.  */  
   KBPlant:string,
      /**  Indicates the desired minimum on-hand Kanban quantity.  */  
   KBQty:number,
   AllocQty:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SalesAllocQty:number,
   JobAllocQty:number,
   JobUnfirmAllocQty:number,
      /**  Filled in by BO, not physically in the database  */  
   Plant:string,
   DefaultWhse:boolean,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  Determine if this Warehouse is a Shared Warehouse  */  
   SharedWarehouse:boolean,
      /**  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  */  
   RemotePlant:string,
      /**  Determines if a User has the rights to perform Adjustments on this Warehouse  */  
   IsUserAllowed:boolean,
      /**  Plant Name  */  
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartWhseSearchListTableset{
   PartWhseSearchList:Erp_Tablesets_PartWhseSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartWhseSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Warehouse  */  
   WarehouseCode:string,
      /**  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  */  
   CountedDate:string,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   OnHandQty:number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   NonNettableQty:number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesReservedQty:number,
      /**   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickingQty:number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickedQty:number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   JobReservedQty:number,
      /**  Uniquely indentifies the record.  */  
   KBCode:string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   MinimumQty:number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   MaximumQty:number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   SafetyQty:number,
      /**  Purchase order number  that the detail line item is linked to.  */  
   KBPONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   KBPOLine:number,
      /**  Kanban Warehouse  */  
   KBWarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   KBBinNum:string,
      /**  Site Identifier. This field cannot be blank.  */  
   KBPlant:string,
      /**  Indicates the desired minimum on-hand Kanban quantity.  */  
   KBQty:number,
   AllocQty:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SalesAllocQty:number,
   JobAllocQty:number,
   JobUnfirmAllocQty:number,
      /**  Filled in by BO, not physically in the database  */  
   Plant:string,
   DefaultWhse:boolean,
      /**  Determines if a User has the rights to perform Adjustments on this Warehouse  */  
   IsUserAllowed:boolean,
      /**  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  */  
   RemotePlant:string,
      /**  Determine if this Warehouse is a Shared Warehouse  */  
   SharedWarehouse:boolean,
   BitFlag:number,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPartWhseFullSearchTableset{
   PartWhseSearch:Erp_Tablesets_PartWhseSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param warehouseCode
   */  
export interface GetByID_input{
   partNum:string,
   warehouseCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartWhseFullSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartWhseFullSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartWhseFullSearchTableset[],
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
   returnObj:Erp_Tablesets_PartWhseSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
   */  
export interface GetNewPartWhseSearch_input{
   ds:Erp_Tablesets_PartWhseFullSearchTableset[],
   partNum:string,
}

export interface GetNewPartWhseSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartWhseFullSearchTableset[],
}
}

   /** Required : 
      @param whereClausePartWhseSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartWhseSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartWhseFullSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPartWhseFullSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartWhseFullSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartWhseFullSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartWhseFullSearchTableset[],
}
}

