import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.RFQSuggSvc
// Description: Search engine for RFQ Entry, no maintenance allowed
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/$metadata", {
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
   Description: Get RFQSuggs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQSuggs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSuggRow
   */  
export function get_RFQSuggs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQSuggs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQSuggs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs", {
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
   Summary: Calls GetByID to retrieve the RFQSugg item
   Description: Calls GetByID to retrieve the RFQSugg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQSugg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
   */  
export function get_RFQSuggs_Company_SugNum(Company:string, SugNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RFQSuggRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs(" + Company + "," + SugNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RFQSuggRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQSugg for the service
   Description: Calls UpdateExt to update RFQSugg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQSugg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQSuggs_Company_SugNum(Company:string, SugNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs(" + Company + "," + SugNum + ")", {
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
   Summary: Call UpdateExt to delete RFQSugg item
   Description: Call UpdateExt to delete RFQSugg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQSugg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SugNum Desc: SugNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQSuggs_Company_SugNum(Company:string, SugNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs(" + Company + "," + SugNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSuggListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggListRow)
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
export function get_GetRows(whereClauseRFQSugg:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRFQSugg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRFQSugg=" + whereClauseRFQSugg
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sugNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sugNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sugNum=" + sugNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/GetList" + params, {
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
   Summary: Invoke method GetNewRFQSugg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQSugg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQSugg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQSugg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRFQSugg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/GetNewRFQSugg", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQSuggListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RFQSuggRow[],
}

export interface Erp_Tablesets_RFQSuggListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   "LineDesc":string,
      /**  Issue (our) unit of measure.  */  
   "IUM":string,
      /**  OUR internal part number for this item.  */  
   "PartNum":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  */  
   "Class":string,
      /**  Related job number.  */  
   "JobNum":string,
      /**  Related Customer QuoteNum.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  */  
   "JobSeq":number,
      /**  Mtl = Material, Sub = Subcontract  */  
   "ItemType":string,
      /**  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The number of vendor quotes that are required.  */  
   "RFQVendQuotes":number,
      /**  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  */  
   "ProcessRFQ":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Used to initialize RFQVend records  */  
   "PurPoint":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  */  
   "OpCode":string,
      /**  Delimited list of Quantity breaks to default the RFQQty table  */  
   "QtyList":string,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   "GlbSuggestion":boolean,
      /**  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  */  
   "RequiredQty":number,
      /**  Indicates if inspection is required when items are received.  Used when create PODetail records  */  
   "RcvInspectionReq":boolean,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  */  
   "GlbJobPartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "GlbJobRevisionNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "GlbJobPartDescription":string,
      /**  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  */  
   "GlbJobProdQty":number,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "GlbJobStartDate":string,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "GlbJobProjectID":string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   "GlbQuoteDueDate":string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   "GlbQuoteQuoted":boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   "GlbQuoteDateQuoted":string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  */  
   "GlbQuoteExpirationDate":string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   "GlbQuoteFollowUpDate":string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   "GlbQuoteReference":string,
      /**  The full name of the customer.  */  
   "GlbQuoteName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  Full description of the part class.  */  
   "ClassDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "QuoteLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "QuoteNumCurrencyCode":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  Full description of the part class.  */  
   "vrClassDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RFQSuggRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   "SugNum":number,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   "LineDesc":string,
      /**  Issue (our) unit of measure.  */  
   "IUM":string,
      /**  OUR internal part number for this item.  */  
   "PartNum":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  */  
   "Class":string,
      /**  Related job number.  */  
   "JobNum":string,
      /**  Related Customer QuoteNum.  */  
   "QuoteNum":number,
      /**  The QuoteLine that record is related to.  */  
   "QuoteLine":number,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  */  
   "JobSeq":number,
      /**  Mtl = Material, Sub = Subcontract  */  
   "ItemType":string,
      /**  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The number of vendor quotes that are required.  */  
   "RFQVendQuotes":number,
      /**  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  */  
   "ProcessRFQ":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Used to initialize RFQVend records  */  
   "PurPoint":string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  */  
   "OpCode":string,
      /**  Delimited list of Quantity breaks to default the RFQQty table  */  
   "QtyList":string,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   "GlbSuggestion":boolean,
      /**  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  */  
   "RequiredQty":number,
      /**  Indicates if inspection is required when items are received.  Used when create PODetail records  */  
   "RcvInspectionReq":boolean,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  */  
   "GlbJobPartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "GlbJobRevisionNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "GlbJobPartDescription":string,
      /**  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  */  
   "GlbJobProdQty":number,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "GlbJobStartDate":string,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "GlbJobProjectID":string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   "GlbQuoteDueDate":string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   "GlbQuoteQuoted":boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   "GlbQuoteDateQuoted":string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  */  
   "GlbQuoteExpirationDate":string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   "GlbQuoteFollowUpDate":string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   "GlbQuoteReference":string,
      /**  The full name of the customer.  */  
   "GlbQuoteName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Requisition Number from where the RFQ Suggestion comes from.  */  
   "ReqNum":number,
      /**  Requisition Line from where the RFQ Suggestion comes from.  */  
   "ReqLine":number,
      /**  The Id that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "AttributeSetIDDescription":string,
   "AttributeSetIDShortDescription":string,
   "ClassDescription":string,
   "JobNumPartDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryByRevision":boolean,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumCountry":string,
   "VendorNumState":string,
   "VendorNumName":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumDefaultFOB":string,
   "VendorNumTermsCode":string,
   "VendorNumZIP":string,
   "vrClassDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param sugNum
   */  
export interface DeleteByID_input{
   sugNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_RFQSuggListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   LineDesc:string,
      /**  Issue (our) unit of measure.  */  
   IUM:string,
      /**  OUR internal part number for this item.  */  
   PartNum:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  */  
   Class:string,
      /**  Related job number.  */  
   JobNum:string,
      /**  Related Customer QuoteNum.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  */  
   JobSeq:number,
      /**  Mtl = Material, Sub = Subcontract  */  
   ItemType:string,
      /**  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  */  
   VendorNum:number,
      /**  The number of vendor quotes that are required.  */  
   RFQVendQuotes:number,
      /**  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  */  
   ProcessRFQ:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Used to initialize RFQVend records  */  
   PurPoint:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  */  
   OpCode:string,
      /**  Delimited list of Quantity breaks to default the RFQQty table  */  
   QtyList:string,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   GlbSuggestion:boolean,
      /**  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  */  
   RequiredQty:number,
      /**  Indicates if inspection is required when items are received.  Used when create PODetail records  */  
   RcvInspectionReq:boolean,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  */  
   GlbJobPartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   GlbJobRevisionNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   GlbJobPartDescription:string,
      /**  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  */  
   GlbJobProdQty:number,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   GlbJobStartDate:string,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   GlbJobProjectID:string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   GlbQuoteDueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   GlbQuoteQuoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   GlbQuoteDateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  */  
   GlbQuoteExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   GlbQuoteFollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   GlbQuoteReference:string,
      /**  The full name of the customer.  */  
   GlbQuoteName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  Full description of the part class.  */  
   ClassDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   QuoteLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   QuoteNumCurrencyCode:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  Full description of the part class.  */  
   vrClassDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQSuggListTableset{
   RFQSuggList:Erp_Tablesets_RFQSuggListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RFQSuggRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   LineDesc:string,
      /**  Issue (our) unit of measure.  */  
   IUM:string,
      /**  OUR internal part number for this item.  */  
   PartNum:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  */  
   Class:string,
      /**  Related job number.  */  
   JobNum:string,
      /**  Related Customer QuoteNum.  */  
   QuoteNum:number,
      /**  The QuoteLine that record is related to.  */  
   QuoteLine:number,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  */  
   JobSeq:number,
      /**  Mtl = Material, Sub = Subcontract  */  
   ItemType:string,
      /**  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  */  
   VendorNum:number,
      /**  The number of vendor quotes that are required.  */  
   RFQVendQuotes:number,
      /**  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  */  
   ProcessRFQ:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Used to initialize RFQVend records  */  
   PurPoint:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  */  
   OpCode:string,
      /**  Delimited list of Quantity breaks to default the RFQQty table  */  
   QtyList:string,
      /**  Global Suggestion flag.  Used in Consolidated Purchasing.  */  
   GlbSuggestion:boolean,
      /**  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  */  
   RequiredQty:number,
      /**  Indicates if inspection is required when items are received.  Used when create PODetail records  */  
   RcvInspectionReq:boolean,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  */  
   GlbJobPartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   GlbJobRevisionNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   GlbJobPartDescription:string,
      /**  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  */  
   GlbJobProdQty:number,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   GlbJobStartDate:string,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   GlbJobProjectID:string,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   GlbQuoteDueDate:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   GlbQuoteQuoted:boolean,
      /**  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  */  
   GlbQuoteDateQuoted:string,
      /**   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  */  
   GlbQuoteExpirationDate:string,
      /**  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  */  
   GlbQuoteFollowUpDate:string,
      /**  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  */  
   GlbQuoteReference:string,
      /**  The full name of the customer.  */  
   GlbQuoteName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Requisition Number from where the RFQ Suggestion comes from.  */  
   ReqNum:number,
      /**  Requisition Line from where the RFQ Suggestion comes from.  */  
   ReqLine:number,
      /**  The Id that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   ClassDescription:string,
   JobNumPartDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumTrackInventoryByRevision:boolean,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumName:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumTermsCode:string,
   VendorNumZIP:string,
   vrClassDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQSuggTableset{
   RFQSugg:Erp_Tablesets_RFQSuggRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRFQSuggTableset{
   RFQSugg:Erp_Tablesets_RFQSuggRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sugNum
   */  
export interface GetByID_input{
   sugNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RFQSuggTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RFQSuggTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RFQSuggTableset[],
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
   returnObj:Erp_Tablesets_RFQSuggListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRFQSugg_input{
   ds:Erp_Tablesets_RFQSuggTableset[],
}

export interface GetNewRFQSugg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQSuggTableset[],
}
}

   /** Required : 
      @param whereClauseRFQSugg
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRFQSugg:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RFQSuggTableset[],
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
   ds:Erp_Tablesets_UpdExtRFQSuggTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRFQSuggTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RFQSuggTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQSuggTableset[],
}
}

