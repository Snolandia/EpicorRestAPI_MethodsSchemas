import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GLBCOASegmentSearchSvc
// Description: shell object for searching the Global segments
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/$metadata", {
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
   Description: Get GLBCOASegmentSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegmentSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentSearchRow
   */  
export function get_GLBCOASegmentSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegmentSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBCOASegmentSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches", {
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
   Summary: Calls GetByID to retrieve the GLBCOASegmentSearch item
   Description: Calls GetByID to retrieve the GLBCOASegmentSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegmentSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
   */  
export function get_GLBCOASegmentSearches_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegmentSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GLBCOASegmentSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBCOASegmentSearch for the service
   Description: Calls UpdateExt to update GLBCOASegmentSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegmentSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBCOASegmentSearches_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
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
   Summary: Call UpdateExt to delete GLBCOASegmentSearch item
   Description: Call UpdateExt to delete GLBCOASegmentSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegmentSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBCOASegmentSearches_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GLBCOASegmentSearches(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchListRow)
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
export function get_GetRows(whereClauseGLBCOASegmentSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLBCOASegmentSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBCOASegmentSearch=" + whereClauseGLBCOASegmentSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(extCompanyID:string, coACode:string, segmentNbr:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof extCompanyID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "extCompanyID=" + extCompanyID
   }
   if(typeof coACode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coACode=" + coACode
   }
   if(typeof segmentNbr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "segmentNbr=" + segmentNbr
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLBCOASegmentSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegmentSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegmentSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegmentSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBCOASegmentSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GetNewGLBCOASegmentSearch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegmentSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegmentSearchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegmentSearchRow[],
}

export interface Erp_Tablesets_GLBCOASegmentSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Name of Segment  */  
   "SegmentName":string,
      /**  Short name of segment.  */  
   "Abbreviation":string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   "MaxLength":number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   "MinLength":number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   "Dynamic":boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   "UseRefEntity":boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   "RefEntity":string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   "AllowAlpha":boolean,
      /**  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  */  
   "EntryControl":string,
      /**  Indicates if journal entries are automatically balanced.  */  
   "SegSelfBal":boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   "Level":number,
      /**  Indicates if this segment is included in the standard trial balance account.  */  
   "SummaryBal":boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   "DetailBal":boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  */  
   "KeepOpenBal":boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   "DisplayOrder":number,
      /**  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  */  
   "MultiCompany":boolean,
      /**  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   "AutoCreateSegVals":boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   "SelfBalAcct":string,
      /**  Balance Seg Value 1  */  
   "BalSegValue1":string,
      /**  Balance Seg Value 2  */  
   "BalSegValue2":string,
      /**  Balance Seg Value 3  */  
   "BalSegValue3":string,
      /**  Balance Seg Value 4  */  
   "BalSegValue4":string,
      /**  Balance Seg Value 5  */  
   "BalSegValue5":string,
      /**  Balance Seg Value 6  */  
   "BalSegValue6":string,
      /**  Balance Seg Value 7  */  
   "BalSegValue7":string,
      /**  Balance Seg Value 8  */  
   "BalSegValue8":string,
      /**  Balance Seg Value 9  */  
   "BalSegValue9":string,
      /**  Balance Seg Value 10  */  
   "BalSegValue10":string,
      /**  Balance Seg Value 11  */  
   "BalSegValue11":string,
      /**  Balance Seg Value 12  */  
   "BalSegValue12":string,
      /**  Balance Seg Value 13  */  
   "BalSegValue13":string,
      /**  Balance Seg Value 14  */  
   "BalSegValue14":string,
      /**  Balance Seg Value 15  */  
   "BalSegValue15":string,
      /**  Balance Seg Value 16  */  
   "BalSegValue16":string,
      /**  Balance Seg Value 17  */  
   "BalSegValue17":string,
      /**  Balance Seg Value 18  */  
   "BalSegValue18":string,
      /**  Balance Seg Value 19  */  
   "BalSegValue19":string,
      /**  Balance Seg Value 20  */  
   "BalSegValue20":string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   "SelfOffAcct":string,
      /**  Offset Segment Value 1  */  
   "OffSegValue1":string,
      /**  Offset Segment Value 2  */  
   "OffSegValue2":string,
      /**  Offset Segment Value 3  */  
   "OffSegValue3":string,
      /**  Offset Segment Value 4  */  
   "OffSegValue4":string,
      /**  Offset Segment Value 5  */  
   "OffSegValue5":string,
      /**  Offset Segment Value 6  */  
   "OffSegValue6":string,
      /**  Offset Segment Value 7  */  
   "OffSegValue7":string,
      /**  Offset Segment Value 8  */  
   "OffSegValue8":string,
      /**  Offset Segment Value 9  */  
   "OffSegValue9":string,
      /**  Offset Segment Value 10  */  
   "OffSegValue10":string,
      /**  Offset Segment Value 11  */  
   "OffSegValue11":string,
      /**  Offset Segment Value 12  */  
   "OffSegValue12":string,
      /**  Offset Segment Value 13  */  
   "OffSegValue13":string,
      /**  Offset Segment Value 14  */  
   "OffSegValue14":string,
      /**  Offset Segment Value 15  */  
   "OffSegValue15":string,
      /**  Offset Segment Value 16  */  
   "OffSegValue16":string,
      /**  Offset Segment Value 17  */  
   "OffSegValue17":string,
      /**  Offset Segment Value 18  */  
   "OffSegValue18":string,
      /**  Offset Segment Value 19  */  
   "OffSegValue19":string,
      /**  Offset Segment Value 20  */  
   "OffSegValue20":string,
   "ReverseCategoryID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLBCOASegmentSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Name of Segment  */  
   "SegmentName":string,
      /**  Short name of segment.  */  
   "Abbreviation":string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   "MaxLength":number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   "MinLength":number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   "Dynamic":boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   "UseRefEntity":boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   "RefEntity":string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   "AllowAlpha":boolean,
      /**  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  */  
   "EntryControl":string,
      /**  Indicates if journal entries are automatically balanced.  */  
   "SegSelfBal":boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   "Level":number,
      /**  Indicates if this segment is included in the standard trial balance account.  */  
   "SummaryBal":boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   "DetailBal":boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  */  
   "KeepOpenBal":boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   "DisplayOrder":number,
      /**  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  */  
   "MultiCompany":boolean,
      /**  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   "AutoCreateSegVals":boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   "SelfBalAcct":string,
      /**  Balance Seg Value 1  */  
   "BalSegValue1":string,
      /**  Balance Seg Value 2  */  
   "BalSegValue2":string,
      /**  Balance Seg Value 3  */  
   "BalSegValue3":string,
      /**  Balance Seg Value 4  */  
   "BalSegValue4":string,
      /**  Balance Seg Value 5  */  
   "BalSegValue5":string,
      /**  Balance Seg Value 6  */  
   "BalSegValue6":string,
      /**  Balance Seg Value 7  */  
   "BalSegValue7":string,
      /**  Balance Seg Value 8  */  
   "BalSegValue8":string,
      /**  Balance Seg Value 9  */  
   "BalSegValue9":string,
      /**  Balance Seg Value 10  */  
   "BalSegValue10":string,
      /**  Balance Seg Value 11  */  
   "BalSegValue11":string,
      /**  Balance Seg Value 12  */  
   "BalSegValue12":string,
      /**  Balance Seg Value 13  */  
   "BalSegValue13":string,
      /**  Balance Seg Value 14  */  
   "BalSegValue14":string,
      /**  Balance Seg Value 15  */  
   "BalSegValue15":string,
      /**  Balance Seg Value 16  */  
   "BalSegValue16":string,
      /**  Balance Seg Value 17  */  
   "BalSegValue17":string,
      /**  Balance Seg Value 18  */  
   "BalSegValue18":string,
      /**  Balance Seg Value 19  */  
   "BalSegValue19":string,
      /**  Balance Seg Value 20  */  
   "BalSegValue20":string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   "SelfOffAcct":string,
      /**  Offset Segment Value 1  */  
   "OffSegValue1":string,
      /**  Offset Segment Value 2  */  
   "OffSegValue2":string,
      /**  Offset Segment Value 3  */  
   "OffSegValue3":string,
      /**  Offset Segment Value 4  */  
   "OffSegValue4":string,
      /**  Offset Segment Value 5  */  
   "OffSegValue5":string,
      /**  Offset Segment Value 6  */  
   "OffSegValue6":string,
      /**  Offset Segment Value 7  */  
   "OffSegValue7":string,
      /**  Offset Segment Value 8  */  
   "OffSegValue8":string,
      /**  Offset Segment Value 9  */  
   "OffSegValue9":string,
      /**  Offset Segment Value 10  */  
   "OffSegValue10":string,
      /**  Offset Segment Value 11  */  
   "OffSegValue11":string,
      /**  Offset Segment Value 12  */  
   "OffSegValue12":string,
      /**  Offset Segment Value 13  */  
   "OffSegValue13":string,
      /**  Offset Segment Value 14  */  
   "OffSegValue14":string,
      /**  Offset Segment Value 15  */  
   "OffSegValue15":string,
      /**  Offset Segment Value 16  */  
   "OffSegValue16":string,
      /**  Offset Segment Value 17  */  
   "OffSegValue17":string,
      /**  Offset Segment Value 18  */  
   "OffSegValue18":string,
      /**  Offset Segment Value 19  */  
   "OffSegValue19":string,
      /**  Offset Segment Value 20  */  
   "OffSegValue20":string,
   "ReverseCategoryID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CNIsCFICode  */  
   "CNIsCFICode":boolean,
      /**  SegValueField  */  
   "SegValueField":string,
      /**  DescFieldName  */  
   "DescFieldName":string,
      /**  GlobalCOASegment  */  
   "GlobalCOASegment":boolean,
      /**  GlobalCOASegmentValues  */  
   "GlobalCOASegmentValues":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  GlobalValuesLock  */  
   "GlobalValuesLock":boolean,
      /**  SiteSegment  */  
   "SiteSegment":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param extCompanyID
      @param coACode
      @param segmentNbr
   */  
export interface DeleteByID_input{
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLBCOASegmentSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Name of Segment  */  
   SegmentName:string,
      /**  Short name of segment.  */  
   Abbreviation:string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   MaxLength:number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   MinLength:number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   Dynamic:boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   UseRefEntity:boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   RefEntity:string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   AllowAlpha:boolean,
      /**  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  */  
   EntryControl:string,
      /**  Indicates if journal entries are automatically balanced.  */  
   SegSelfBal:boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   Level:number,
      /**  Indicates if this segment is included in the standard trial balance account.  */  
   SummaryBal:boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   DetailBal:boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  */  
   KeepOpenBal:boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   DisplayOrder:number,
      /**  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  */  
   MultiCompany:boolean,
      /**  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   AutoCreateSegVals:boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   SelfBalAcct:string,
      /**  Balance Seg Value 1  */  
   BalSegValue1:string,
      /**  Balance Seg Value 2  */  
   BalSegValue2:string,
      /**  Balance Seg Value 3  */  
   BalSegValue3:string,
      /**  Balance Seg Value 4  */  
   BalSegValue4:string,
      /**  Balance Seg Value 5  */  
   BalSegValue5:string,
      /**  Balance Seg Value 6  */  
   BalSegValue6:string,
      /**  Balance Seg Value 7  */  
   BalSegValue7:string,
      /**  Balance Seg Value 8  */  
   BalSegValue8:string,
      /**  Balance Seg Value 9  */  
   BalSegValue9:string,
      /**  Balance Seg Value 10  */  
   BalSegValue10:string,
      /**  Balance Seg Value 11  */  
   BalSegValue11:string,
      /**  Balance Seg Value 12  */  
   BalSegValue12:string,
      /**  Balance Seg Value 13  */  
   BalSegValue13:string,
      /**  Balance Seg Value 14  */  
   BalSegValue14:string,
      /**  Balance Seg Value 15  */  
   BalSegValue15:string,
      /**  Balance Seg Value 16  */  
   BalSegValue16:string,
      /**  Balance Seg Value 17  */  
   BalSegValue17:string,
      /**  Balance Seg Value 18  */  
   BalSegValue18:string,
      /**  Balance Seg Value 19  */  
   BalSegValue19:string,
      /**  Balance Seg Value 20  */  
   BalSegValue20:string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   SelfOffAcct:string,
      /**  Offset Segment Value 1  */  
   OffSegValue1:string,
      /**  Offset Segment Value 2  */  
   OffSegValue2:string,
      /**  Offset Segment Value 3  */  
   OffSegValue3:string,
      /**  Offset Segment Value 4  */  
   OffSegValue4:string,
      /**  Offset Segment Value 5  */  
   OffSegValue5:string,
      /**  Offset Segment Value 6  */  
   OffSegValue6:string,
      /**  Offset Segment Value 7  */  
   OffSegValue7:string,
      /**  Offset Segment Value 8  */  
   OffSegValue8:string,
      /**  Offset Segment Value 9  */  
   OffSegValue9:string,
      /**  Offset Segment Value 10  */  
   OffSegValue10:string,
      /**  Offset Segment Value 11  */  
   OffSegValue11:string,
      /**  Offset Segment Value 12  */  
   OffSegValue12:string,
      /**  Offset Segment Value 13  */  
   OffSegValue13:string,
      /**  Offset Segment Value 14  */  
   OffSegValue14:string,
      /**  Offset Segment Value 15  */  
   OffSegValue15:string,
      /**  Offset Segment Value 16  */  
   OffSegValue16:string,
      /**  Offset Segment Value 17  */  
   OffSegValue17:string,
      /**  Offset Segment Value 18  */  
   OffSegValue18:string,
      /**  Offset Segment Value 19  */  
   OffSegValue19:string,
      /**  Offset Segment Value 20  */  
   OffSegValue20:string,
   ReverseCategoryID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOASegmentSearchListTableset{
   GLBCOASegmentSearchList:Erp_Tablesets_GLBCOASegmentSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLBCOASegmentSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Name of Segment  */  
   SegmentName:string,
      /**  Short name of segment.  */  
   Abbreviation:string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   MaxLength:number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   MinLength:number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   Dynamic:boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   UseRefEntity:boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   RefEntity:string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   AllowAlpha:boolean,
      /**  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  */  
   EntryControl:string,
      /**  Indicates if journal entries are automatically balanced.  */  
   SegSelfBal:boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   Level:number,
      /**  Indicates if this segment is included in the standard trial balance account.  */  
   SummaryBal:boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   DetailBal:boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  */  
   KeepOpenBal:boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   DisplayOrder:number,
      /**  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  */  
   MultiCompany:boolean,
      /**  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   AutoCreateSegVals:boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   SelfBalAcct:string,
      /**  Balance Seg Value 1  */  
   BalSegValue1:string,
      /**  Balance Seg Value 2  */  
   BalSegValue2:string,
      /**  Balance Seg Value 3  */  
   BalSegValue3:string,
      /**  Balance Seg Value 4  */  
   BalSegValue4:string,
      /**  Balance Seg Value 5  */  
   BalSegValue5:string,
      /**  Balance Seg Value 6  */  
   BalSegValue6:string,
      /**  Balance Seg Value 7  */  
   BalSegValue7:string,
      /**  Balance Seg Value 8  */  
   BalSegValue8:string,
      /**  Balance Seg Value 9  */  
   BalSegValue9:string,
      /**  Balance Seg Value 10  */  
   BalSegValue10:string,
      /**  Balance Seg Value 11  */  
   BalSegValue11:string,
      /**  Balance Seg Value 12  */  
   BalSegValue12:string,
      /**  Balance Seg Value 13  */  
   BalSegValue13:string,
      /**  Balance Seg Value 14  */  
   BalSegValue14:string,
      /**  Balance Seg Value 15  */  
   BalSegValue15:string,
      /**  Balance Seg Value 16  */  
   BalSegValue16:string,
      /**  Balance Seg Value 17  */  
   BalSegValue17:string,
      /**  Balance Seg Value 18  */  
   BalSegValue18:string,
      /**  Balance Seg Value 19  */  
   BalSegValue19:string,
      /**  Balance Seg Value 20  */  
   BalSegValue20:string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   SelfOffAcct:string,
      /**  Offset Segment Value 1  */  
   OffSegValue1:string,
      /**  Offset Segment Value 2  */  
   OffSegValue2:string,
      /**  Offset Segment Value 3  */  
   OffSegValue3:string,
      /**  Offset Segment Value 4  */  
   OffSegValue4:string,
      /**  Offset Segment Value 5  */  
   OffSegValue5:string,
      /**  Offset Segment Value 6  */  
   OffSegValue6:string,
      /**  Offset Segment Value 7  */  
   OffSegValue7:string,
      /**  Offset Segment Value 8  */  
   OffSegValue8:string,
      /**  Offset Segment Value 9  */  
   OffSegValue9:string,
      /**  Offset Segment Value 10  */  
   OffSegValue10:string,
      /**  Offset Segment Value 11  */  
   OffSegValue11:string,
      /**  Offset Segment Value 12  */  
   OffSegValue12:string,
      /**  Offset Segment Value 13  */  
   OffSegValue13:string,
      /**  Offset Segment Value 14  */  
   OffSegValue14:string,
      /**  Offset Segment Value 15  */  
   OffSegValue15:string,
      /**  Offset Segment Value 16  */  
   OffSegValue16:string,
      /**  Offset Segment Value 17  */  
   OffSegValue17:string,
      /**  Offset Segment Value 18  */  
   OffSegValue18:string,
      /**  Offset Segment Value 19  */  
   OffSegValue19:string,
      /**  Offset Segment Value 20  */  
   OffSegValue20:string,
   ReverseCategoryID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CNIsCFICode  */  
   CNIsCFICode:boolean,
      /**  SegValueField  */  
   SegValueField:string,
      /**  DescFieldName  */  
   DescFieldName:string,
      /**  GlobalCOASegment  */  
   GlobalCOASegment:boolean,
      /**  GlobalCOASegmentValues  */  
   GlobalCOASegmentValues:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  GlobalValuesLock  */  
   GlobalValuesLock:boolean,
      /**  SiteSegment  */  
   SiteSegment:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOASegmentSearchTableset{
   GLBCOASegmentSearch:Erp_Tablesets_GLBCOASegmentSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLBCOASegmentSearchTableset{
   GLBCOASegmentSearch:Erp_Tablesets_GLBCOASegmentSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param extCompanyID
      @param coACode
      @param segmentNbr
   */  
export interface GetByID_input{
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLBCOASegmentSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLBCOASegmentSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLBCOASegmentSearchTableset[],
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
   returnObj:Erp_Tablesets_GLBCOASegmentSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param coACode
   */  
export interface GetNewGLBCOASegmentSearch_input{
   ds:Erp_Tablesets_GLBCOASegmentSearchTableset[],
   extCompanyID:string,
   coACode:string,
}

export interface GetNewGLBCOASegmentSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOASegmentSearchTableset[],
}
}

   /** Required : 
      @param whereClauseGLBCOASegmentSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLBCOASegmentSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLBCOASegmentSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtGLBCOASegmentSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLBCOASegmentSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLBCOASegmentSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOASegmentSearchTableset[],
}
}

