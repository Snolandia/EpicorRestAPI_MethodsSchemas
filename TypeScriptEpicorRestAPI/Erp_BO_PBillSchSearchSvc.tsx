import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PBillSchSearchSvc
// Description: The PBillSchSearch bo. Used for the PBillSchSearch Combo.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/$metadata", {
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
   Description: Get PBillSchSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBillSchSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBillSchRow
   */  
export function get_PBillSchSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBillSchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/PBillSchSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBillSchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBillSchSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBillSchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBillSchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBillSchSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/PBillSchSearches", {
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
   Summary: Calls GetByID to retrieve the PBillSchSearch item
   Description: Calls GetByID to retrieve the PBillSchSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBillSchSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param BillSchedID Desc: BillSchedID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBillSchRow
   */  
export function get_PBillSchSearches_Company_ProjectID_BillSchedID(Company:string, ProjectID:string, BillSchedID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBillSchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/PBillSchSearches(" + Company + "," + ProjectID + "," + BillSchedID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBillSchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBillSchSearch for the service
   Description: Calls UpdateExt to update PBillSchSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBillSchSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param BillSchedID Desc: BillSchedID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBillSchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBillSchSearches_Company_ProjectID_BillSchedID(Company:string, ProjectID:string, BillSchedID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/PBillSchSearches(" + Company + "," + ProjectID + "," + BillSchedID + ")", {
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
   Summary: Call UpdateExt to delete PBillSchSearch item
   Description: Call UpdateExt to delete PBillSchSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBillSchSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param BillSchedID Desc: BillSchedID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBillSchSearches_Company_ProjectID_BillSchedID(Company:string, ProjectID:string, BillSchedID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/PBillSchSearches(" + Company + "," + ProjectID + "," + BillSchedID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBillSchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBillSchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBillSchListRow)
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
export function get_GetRows(whereClausePBillSch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePBillSch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBillSch=" + whereClausePBillSch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/GetRows" + params, {
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
export function get_GetByID(projectID:string, billSchedID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof projectID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "projectID=" + projectID
   }
   if(typeof billSchedID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "billSchedID=" + billSchedID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPBillSch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBillSch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBillSch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBillSch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPBillSch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/GetNewPBillSch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBillSchSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBillSchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBillSchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBillSchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBillSchRow[],
}

export interface Erp_Tablesets_PBillSchListRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Project ID  */  
   "ProjectID":string,
      /**  User defined ID to be used for this Billing Schedule.  */  
   "BillSchedID":string,
      /**  It indicates whether the Billing Schedule is inactive. If true it will be excluded from the invoice generation process.  */  
   "InActive":boolean,
      /**  Billing Schedule description  */  
   "Description":string,
      /**  Billing Schedule frequency.Code/Desc:W = Weekly, M = Monthly, Q = Quarterly, A = Annually  */  
   "SchedFreq":string,
      /**  Number of periods in months for defect liability. For reference only.  */  
   "LiabilityMonths":number,
      /**  This is the date that the user wants to the first invoice to be generated. This will be controlled by the field ?Invoiced to Date? is greater than zero.  */  
   "StartDate":string,
      /**  System generated field. When the record is first created this will default to the Start Date field value. When the Project Entry ? Invoice Generation Process has been run in ?Update? mode the system will set this field dependant on the Schedule Frequency defined.  */  
   "NextDate":string,
      /**  Total contractual value for this  Billing Schedule  */  
   "TotValue":number,
      /**  Percentage of the invoice that is to be retained  */  
   "RetentionPcnt":number,
      /**  When it's set to true the invoice process will reduce the invoice amount by the retention value.  */  
   "ReduceInvByRet":boolean,
      /**  Shows the number of invoices that have been produced. (System generated).  */  
   "NumInvoices":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated).  */  
   "TotInvoiced":number,
      /**  Total Retention  */  
   "TotRetention":number,
      /**  Sales order number  */  
   "OrderNum":number,
      /**  Sales order number  */  
   "OrderLine":number,
      /**  Product Group that will be used for the invoice posting and the posting or retentions and also the deferred revenue.  */  
   "ProdCode":string,
      /**  Setting this to true will cause a General Journal to be produced as part of the Billing Schedule process to post the Retentions to the Product Group Retentions account.  */  
   "PostRetProdGrp":boolean,
      /**  Billing Schedule manager  */  
   "Manager":string,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Project currency  */  
   "DocTotInvoiced":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   "Rpt1TotInvoiced":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   "Rpt2TotInvoiced":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   "Rpt3TotInvoiced":number,
      /**  in the Project currency  */  
   "DocTotRetention":number,
      /**  in the Reporting currency  */  
   "Rpt1TotRetention":number,
      /**  in the Reporting currency  */  
   "Rpt2TotRetention":number,
      /**  in the Reporting currency  */  
   "Rpt3TotRetention":number,
      /**  Total contractual value for this  Billing Schedule in the Project currency  */  
   "DocTotValue":number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   "Rpt1TotValue":number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   "Rpt2TotValue":number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   "Rpt3TotValue":number,
      /**  Indicates the billling schedule has been closed and no further activity can take place.  */  
   "Closed":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "ManagerName":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBillSchRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Project ID  */  
   "ProjectID":string,
      /**  User defined ID to be used for this Billing Schedule.  */  
   "BillSchedID":string,
      /**  It indicates whether the Billing Schedule is inactive. If true it will be excluded from the invoice generation process.  */  
   "InActive":boolean,
      /**  Billing Schedule description  */  
   "Description":string,
      /**  Billing Schedule frequency.Code/Desc:W = Weekly, M = Monthly, Q = Quarterly, A = Annually  */  
   "SchedFreq":string,
      /**  Number of periods in months for defect liability. For reference only.  */  
   "LiabilityMonths":number,
      /**  This is the date that the user wants to the first invoice to be generated. This will be controlled by the field ?Invoiced to Date? is greater than zero.  */  
   "StartDate":string,
      /**  System generated field. When the record is first created this will default to the Start Date field value. When the Project Entry ? Invoice Generation Process has been run in ?Update? mode the system will set this field dependant on the Schedule Frequency defined.  */  
   "NextDate":string,
      /**  Total contractual value for this  Billing Schedule  */  
   "TotValue":number,
      /**  Percentage of the invoice that is to be retained  */  
   "RetentionPcnt":number,
      /**  When it's set to true the invoice process will reduce the invoice amount by the retention value.  */  
   "ReduceInvByRet":boolean,
      /**  Shows the number of invoices that have been produced. (System generated).  */  
   "NumInvoices":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated).  */  
   "TotInvoiced":number,
      /**  Total Retention  */  
   "TotRetention":number,
      /**  Sales order number  */  
   "OrderNum":number,
      /**  Sales order number  */  
   "OrderLine":number,
      /**  Product Group that will be used for the invoice posting and the posting or retentions and also the deferred revenue.  */  
   "ProdCode":string,
      /**  Setting this to true will cause a General Journal to be produced as part of the Billing Schedule process to post the Retentions to the Product Group Retentions account.  */  
   "PostRetProdGrp":boolean,
      /**  Billing Schedule manager  */  
   "Manager":string,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Project currency  */  
   "DocTotInvoiced":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   "Rpt1TotInvoiced":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   "Rpt2TotInvoiced":number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   "Rpt3TotInvoiced":number,
      /**  in the Project currency  */  
   "DocTotRetention":number,
      /**  in the Reporting currency  */  
   "Rpt1TotRetention":number,
      /**  in the Reporting currency  */  
   "Rpt2TotRetention":number,
      /**  in the Reporting currency  */  
   "Rpt3TotRetention":number,
      /**  Total contractual value for this  Billing Schedule in the Project currency  */  
   "DocTotValue":number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   "Rpt1TotValue":number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   "Rpt2TotValue":number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   "Rpt3TotValue":number,
      /**  Indicates the billling schedule has been closed and no further activity can take place.  */  
   "Closed":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
      /**  Project Phase (Patch Field)  */  
   "PhaseID":string,
   "BitFlag":number,
   "ManagerName":string,
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param projectID
      @param billSchedID
   */  
export interface DeleteByID_input{
   projectID:string,
   billSchedID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PBillSchListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Project ID  */  
   ProjectID:string,
      /**  User defined ID to be used for this Billing Schedule.  */  
   BillSchedID:string,
      /**  It indicates whether the Billing Schedule is inactive. If true it will be excluded from the invoice generation process.  */  
   InActive:boolean,
      /**  Billing Schedule description  */  
   Description:string,
      /**  Billing Schedule frequency.Code/Desc:W = Weekly, M = Monthly, Q = Quarterly, A = Annually  */  
   SchedFreq:string,
      /**  Number of periods in months for defect liability. For reference only.  */  
   LiabilityMonths:number,
      /**  This is the date that the user wants to the first invoice to be generated. This will be controlled by the field ?Invoiced to Date? is greater than zero.  */  
   StartDate:string,
      /**  System generated field. When the record is first created this will default to the Start Date field value. When the Project Entry ? Invoice Generation Process has been run in ?Update? mode the system will set this field dependant on the Schedule Frequency defined.  */  
   NextDate:string,
      /**  Total contractual value for this  Billing Schedule  */  
   TotValue:number,
      /**  Percentage of the invoice that is to be retained  */  
   RetentionPcnt:number,
      /**  When it's set to true the invoice process will reduce the invoice amount by the retention value.  */  
   ReduceInvByRet:boolean,
      /**  Shows the number of invoices that have been produced. (System generated).  */  
   NumInvoices:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated).  */  
   TotInvoiced:number,
      /**  Total Retention  */  
   TotRetention:number,
      /**  Sales order number  */  
   OrderNum:number,
      /**  Sales order number  */  
   OrderLine:number,
      /**  Product Group that will be used for the invoice posting and the posting or retentions and also the deferred revenue.  */  
   ProdCode:string,
      /**  Setting this to true will cause a General Journal to be produced as part of the Billing Schedule process to post the Retentions to the Product Group Retentions account.  */  
   PostRetProdGrp:boolean,
      /**  Billing Schedule manager  */  
   Manager:string,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Project currency  */  
   DocTotInvoiced:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   Rpt1TotInvoiced:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   Rpt2TotInvoiced:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   Rpt3TotInvoiced:number,
      /**  in the Project currency  */  
   DocTotRetention:number,
      /**  in the Reporting currency  */  
   Rpt1TotRetention:number,
      /**  in the Reporting currency  */  
   Rpt2TotRetention:number,
      /**  in the Reporting currency  */  
   Rpt3TotRetention:number,
      /**  Total contractual value for this  Billing Schedule in the Project currency  */  
   DocTotValue:number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   Rpt1TotValue:number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   Rpt2TotValue:number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   Rpt3TotValue:number,
      /**  Indicates the billling schedule has been closed and no further activity can take place.  */  
   Closed:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   ManagerName:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBillSchListTableset{
   PBillSchList:Erp_Tablesets_PBillSchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PBillSchRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Project ID  */  
   ProjectID:string,
      /**  User defined ID to be used for this Billing Schedule.  */  
   BillSchedID:string,
      /**  It indicates whether the Billing Schedule is inactive. If true it will be excluded from the invoice generation process.  */  
   InActive:boolean,
      /**  Billing Schedule description  */  
   Description:string,
      /**  Billing Schedule frequency.Code/Desc:W = Weekly, M = Monthly, Q = Quarterly, A = Annually  */  
   SchedFreq:string,
      /**  Number of periods in months for defect liability. For reference only.  */  
   LiabilityMonths:number,
      /**  This is the date that the user wants to the first invoice to be generated. This will be controlled by the field ?Invoiced to Date? is greater than zero.  */  
   StartDate:string,
      /**  System generated field. When the record is first created this will default to the Start Date field value. When the Project Entry ? Invoice Generation Process has been run in ?Update? mode the system will set this field dependant on the Schedule Frequency defined.  */  
   NextDate:string,
      /**  Total contractual value for this  Billing Schedule  */  
   TotValue:number,
      /**  Percentage of the invoice that is to be retained  */  
   RetentionPcnt:number,
      /**  When it's set to true the invoice process will reduce the invoice amount by the retention value.  */  
   ReduceInvByRet:boolean,
      /**  Shows the number of invoices that have been produced. (System generated).  */  
   NumInvoices:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated).  */  
   TotInvoiced:number,
      /**  Total Retention  */  
   TotRetention:number,
      /**  Sales order number  */  
   OrderNum:number,
      /**  Sales order number  */  
   OrderLine:number,
      /**  Product Group that will be used for the invoice posting and the posting or retentions and also the deferred revenue.  */  
   ProdCode:string,
      /**  Setting this to true will cause a General Journal to be produced as part of the Billing Schedule process to post the Retentions to the Product Group Retentions account.  */  
   PostRetProdGrp:boolean,
      /**  Billing Schedule manager  */  
   Manager:string,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Project currency  */  
   DocTotInvoiced:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   Rpt1TotInvoiced:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   Rpt2TotInvoiced:number,
      /**  Shows the total value of all posted invoices made against this Billing Schedule (system generated). in the Reporting currency  */  
   Rpt3TotInvoiced:number,
      /**  in the Project currency  */  
   DocTotRetention:number,
      /**  in the Reporting currency  */  
   Rpt1TotRetention:number,
      /**  in the Reporting currency  */  
   Rpt2TotRetention:number,
      /**  in the Reporting currency  */  
   Rpt3TotRetention:number,
      /**  Total contractual value for this  Billing Schedule in the Project currency  */  
   DocTotValue:number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   Rpt1TotValue:number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   Rpt2TotValue:number,
      /**  Total contractual value for this  Billing Schedule in the Reporting currency  */  
   Rpt3TotValue:number,
      /**  Indicates the billling schedule has been closed and no further activity can take place.  */  
   Closed:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
      /**  Project Phase (Patch Field)  */  
   PhaseID:string,
   BitFlag:number,
   ManagerName:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBillSchSearchTableset{
   PBillSch:Erp_Tablesets_PBillSchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPBillSchSearchTableset{
   PBillSch:Erp_Tablesets_PBillSchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param projectID
      @param billSchedID
   */  
export interface GetByID_input{
   projectID:string,
   billSchedID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PBillSchSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PBillSchSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PBillSchSearchTableset[],
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
   returnObj:Erp_Tablesets_PBillSchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param projectID
   */  
export interface GetNewPBillSch_input{
   ds:Erp_Tablesets_PBillSchSearchTableset[],
   projectID:string,
}

export interface GetNewPBillSch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBillSchSearchTableset[],
}
}

   /** Required : 
      @param whereClausePBillSch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePBillSch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PBillSchSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPBillSchSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPBillSchSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PBillSchSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBillSchSearchTableset[],
}
}

