import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PcInputsSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/$metadata", {
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
   Description: Get PcInputsSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   */  
export function get_PcInputsSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches", {
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
   Summary: Calls GetByID to retrieve the PcInputsSearch item
   Description: Calls GetByID to retrieve the PcInputsSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   */  
export function get_PcInputsSearches_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches(" + Company + "," + ConfigID + "," + InputName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsSearch for the service
   Description: Calls UpdateExt to update PcInputsSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsSearches_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches(" + Company + "," + ConfigID + "," + InputName + ")", {
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
   Summary: Call UpdateExt to delete PcInputsSearch item
   Description: Call UpdateExt to delete PcInputsSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsSearches_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches(" + Company + "," + ConfigID + "," + InputName + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsListRow)
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
export function get_GetRows(whereClausePcInputs:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcInputs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputs=" + whereClausePcInputs
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/GetRows" + params, {
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
export function get_GetByID(configID:string, inputName:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof configID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "configID=" + configID
   }
   if(typeof inputName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inputName=" + inputName
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPcInputs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/GetNewPcInputs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsRow[],
}

export interface Erp_Tablesets_PcInputsListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   "InputName":string,
      /**  The order that the tab function will step through the inputs.  */  
   "TabOrder":number,
      /**  The type of data that can be stored in the control.  */  
   "DataType":string,
      /**  The format for which the data will be stored.  */  
   "FormatString":string,
      /**  The initial value for the control.  */  
   "InitVal":string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   "StatusText":string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   "Required":boolean,
      /**  On what page does the control exist.  */  
   "PageSeq":number,
      /**  The control's label.  */  
   "SideLabel":string,
      /**  The pixel position for the x axis.  */  
   "xPos":number,
      /**  The pixel position for the Y axis.  */  
   "yPos":number,
      /**  The pixel width of the control.  */  
   "pWidth":number,
      /**  The pixel height of the control.  */  
   "pHeight":number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   "ControlType":string,
      /**  The prompt when expression for the widget.  */  
   "PromptWhen":string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   "ListItems":string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   "StartDec":number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   "EndDec":number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   "IncrPrec":number,
      /**  The starting date for a validated date fill-in.  */  
   "StartDate":string,
      /**  The ending date for a validated date fill-in.  */  
   "EndDate":string,
      /**  The list of valid responses for a validated string input.  */  
   "ValList":string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   "Horizontal":boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   "IsGlobal":boolean,
      /**  The On Leave expression for the control.  */  
   "OnLeave":string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   "WebInputName":string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   "SummaryLabel":string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   "DLRunProgram":boolean,
      /**  The Progress program used for building a dynamic list.  */  
   "DLProgramName":string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   "DLProgramInputs":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   "HideInSummary":boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   "OnLeave2":string,
      /**  If true, the input will not be displayed on the input page  */  
   "Invisible":boolean,
      /**  Comments describing the input  */  
   "Comments":string,
      /**  Global Input Variable  */  
   "GlobalInputVar":boolean,
      /**  Global Input Variable Name  */  
   "GlbInputVarName":string,
      /**  Do not display input in Summary  */  
   "NoDispSummary":boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   "ExternalRef":boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   "AttributeID":string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMinValue":boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMaxValue":boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseIncrValue":boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseInitVal":boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   "UseToolTip":boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseScreenLabel":boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseListValues":boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   "SmartPartSeq":number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   "SmartStringStart":number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   "SmartStringEnd":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  If true then fields on the record may be updated  */  
   "CanUpdate":boolean,
      /**  The initial value of a date field  */  
   "InitDate":string,
      /**  The initial value of a decimal input  */  
   "InitDecimal":number,
      /**  The initial value for a logical input  */  
   "InitLogical":boolean,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   "DispCharVal":string,
   "IsGlobalInputVar":boolean,
   "DspPageSeq":number,
   "TestPlan":boolean,
   "AllowSmartString":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   "InputName":string,
      /**  The order that the tab function will step through the inputs.  */  
   "TabOrder":number,
      /**  The type of data that can be stored in the control.  */  
   "DataType":string,
      /**  The format for which the data will be stored.  */  
   "FormatString":string,
      /**  The initial value for the control.  */  
   "InitVal":string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   "StatusText":string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   "Required":boolean,
      /**  On what page does the control exist.  */  
   "PageSeq":number,
      /**  The control's label.  */  
   "SideLabel":string,
      /**  The pixel position for the x axis.  */  
   "xPos":number,
      /**  The pixel position for the Y axis.  */  
   "yPos":number,
      /**  The pixel width of the control.  */  
   "pWidth":number,
      /**  The pixel height of the control.  */  
   "pHeight":number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   "ControlType":string,
      /**  The prompt when expression for the widget.  */  
   "PromptWhen":string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   "ListItems":string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   "StartDec":number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   "EndDec":number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   "IncrPrec":number,
      /**  The starting date for a validated date fill-in.  */  
   "StartDate":string,
      /**  The ending date for a validated date fill-in.  */  
   "EndDate":string,
      /**  The list of valid responses for a validated string input.  */  
   "ValList":string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   "Horizontal":boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   "IsGlobal":boolean,
      /**  The On Leave expression for the control.  */  
   "OnLeave":string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   "WebInputName":string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   "SummaryLabel":string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   "DLRunProgram":boolean,
      /**  The Progress program used for building a dynamic list.  */  
   "DLProgramName":string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   "DLProgramInputs":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   "HideInSummary":boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   "OnLeave2":string,
      /**  If true, the input will not be displayed on the input page  */  
   "Invisible":boolean,
      /**  Comments describing the input  */  
   "Comments":string,
      /**  Global Input Variable  */  
   "GlobalInputVar":boolean,
      /**  Global Input Variable Name  */  
   "GlbInputVarName":string,
      /**  Do not display input in Summary  */  
   "NoDispSummary":boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   "ExternalRef":boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   "AttributeID":string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMinValue":boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMaxValue":boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseIncrValue":boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseInitVal":boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   "UseToolTip":boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseScreenLabel":boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseListValues":boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   "SmartPartSeq":number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   "SmartStringStart":number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   "SmartStringEnd":number,
      /**  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  */  
   "ShowDistinct":boolean,
      /**  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  */  
   "DesignControlType":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ReadOnly  */  
   "ReadOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AutoSizeList  */  
   "AutoSizeList":boolean,
      /**  ListWidth  */  
   "ListWidth":number,
      /**  ImageSource  */  
   "ImageSource":string,
      /**  ImageLayerID  */  
   "ImageLayerID":string,
   "AllowSmartString":boolean,
   "AttributeDescription":string,
      /**  If true then fields on the record may be updated  */  
   "CanUpdate":boolean,
   "Content":string,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   "DispCharVal":string,
   "DspPageSeq":number,
      /**  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  */  
   "FullInputName":string,
   "ImageMapping":boolean,
      /**  The initial value of a date field  */  
   "InitDate":string,
      /**  The initial value of a decimal input  */  
   "InitDecimal":number,
      /**  The initial value for a logical input  */  
   "InitLogical":boolean,
      /**  Indicates whether or not Input Rules have been defined.  */  
   "InputRules":boolean,
      /**  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  */  
   "InputType":string,
   "IsGlobalInputVar":boolean,
   "OnLaunch":string,
   "PageDisplaySeq":number,
      /**  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  */  
   "PcDynLstCount":number,
   "ReadOnlyExpression":string,
   "TestPlan":boolean,
   "ImageURL":string,
   "BitFlag":number,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param configID
      @param inputName
   */  
export interface DeleteByID_input{
   configID:string,
   inputName:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PcInputsListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  The order that the tab function will step through the inputs.  */  
   TabOrder:number,
      /**  The type of data that can be stored in the control.  */  
   DataType:string,
      /**  The format for which the data will be stored.  */  
   FormatString:string,
      /**  The initial value for the control.  */  
   InitVal:string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   StatusText:string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   Required:boolean,
      /**  On what page does the control exist.  */  
   PageSeq:number,
      /**  The control's label.  */  
   SideLabel:string,
      /**  The pixel position for the x axis.  */  
   xPos:number,
      /**  The pixel position for the Y axis.  */  
   yPos:number,
      /**  The pixel width of the control.  */  
   pWidth:number,
      /**  The pixel height of the control.  */  
   pHeight:number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   ControlType:string,
      /**  The prompt when expression for the widget.  */  
   PromptWhen:string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   ListItems:string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   StartDec:number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   EndDec:number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   IncrPrec:number,
      /**  The starting date for a validated date fill-in.  */  
   StartDate:string,
      /**  The ending date for a validated date fill-in.  */  
   EndDate:string,
      /**  The list of valid responses for a validated string input.  */  
   ValList:string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   Horizontal:boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   IsGlobal:boolean,
      /**  The On Leave expression for the control.  */  
   OnLeave:string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   WebInputName:string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   SummaryLabel:string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   DLRunProgram:boolean,
      /**  The Progress program used for building a dynamic list.  */  
   DLProgramName:string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   DLProgramInputs:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   HideInSummary:boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   OnLeave2:string,
      /**  If true, the input will not be displayed on the input page  */  
   Invisible:boolean,
      /**  Comments describing the input  */  
   Comments:string,
      /**  Global Input Variable  */  
   GlobalInputVar:boolean,
      /**  Global Input Variable Name  */  
   GlbInputVarName:string,
      /**  Do not display input in Summary  */  
   NoDispSummary:boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   ExternalRef:boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   AttributeID:string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMinValue:boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMaxValue:boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseIncrValue:boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseInitVal:boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   UseToolTip:boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseScreenLabel:boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseListValues:boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   SmartPartSeq:number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   SmartStringStart:number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   SmartStringEnd:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If true then fields on the record may be updated  */  
   CanUpdate:boolean,
      /**  The initial value of a date field  */  
   InitDate:string,
      /**  The initial value of a decimal input  */  
   InitDecimal:number,
      /**  The initial value for a logical input  */  
   InitLogical:boolean,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   DispCharVal:string,
   IsGlobalInputVar:boolean,
   DspPageSeq:number,
   TestPlan:boolean,
   AllowSmartString:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsListTableset{
   PcInputsList:Erp_Tablesets_PcInputsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcInputsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  The order that the tab function will step through the inputs.  */  
   TabOrder:number,
      /**  The type of data that can be stored in the control.  */  
   DataType:string,
      /**  The format for which the data will be stored.  */  
   FormatString:string,
      /**  The initial value for the control.  */  
   InitVal:string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   StatusText:string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   Required:boolean,
      /**  On what page does the control exist.  */  
   PageSeq:number,
      /**  The control's label.  */  
   SideLabel:string,
      /**  The pixel position for the x axis.  */  
   xPos:number,
      /**  The pixel position for the Y axis.  */  
   yPos:number,
      /**  The pixel width of the control.  */  
   pWidth:number,
      /**  The pixel height of the control.  */  
   pHeight:number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   ControlType:string,
      /**  The prompt when expression for the widget.  */  
   PromptWhen:string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   ListItems:string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   StartDec:number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   EndDec:number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   IncrPrec:number,
      /**  The starting date for a validated date fill-in.  */  
   StartDate:string,
      /**  The ending date for a validated date fill-in.  */  
   EndDate:string,
      /**  The list of valid responses for a validated string input.  */  
   ValList:string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   Horizontal:boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   IsGlobal:boolean,
      /**  The On Leave expression for the control.  */  
   OnLeave:string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   WebInputName:string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   SummaryLabel:string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   DLRunProgram:boolean,
      /**  The Progress program used for building a dynamic list.  */  
   DLProgramName:string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   DLProgramInputs:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   HideInSummary:boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   OnLeave2:string,
      /**  If true, the input will not be displayed on the input page  */  
   Invisible:boolean,
      /**  Comments describing the input  */  
   Comments:string,
      /**  Global Input Variable  */  
   GlobalInputVar:boolean,
      /**  Global Input Variable Name  */  
   GlbInputVarName:string,
      /**  Do not display input in Summary  */  
   NoDispSummary:boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   ExternalRef:boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   AttributeID:string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMinValue:boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMaxValue:boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseIncrValue:boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseInitVal:boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   UseToolTip:boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseScreenLabel:boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseListValues:boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   SmartPartSeq:number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   SmartStringStart:number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   SmartStringEnd:number,
      /**  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  */  
   ShowDistinct:boolean,
      /**  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  */  
   DesignControlType:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ReadOnly  */  
   ReadOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AutoSizeList  */  
   AutoSizeList:boolean,
      /**  ListWidth  */  
   ListWidth:number,
      /**  ImageSource  */  
   ImageSource:string,
      /**  ImageLayerID  */  
   ImageLayerID:string,
   AllowSmartString:boolean,
   AttributeDescription:string,
      /**  If true then fields on the record may be updated  */  
   CanUpdate:boolean,
   Content:string,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   DispCharVal:string,
   DspPageSeq:number,
      /**  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  */  
   FullInputName:string,
   ImageMapping:boolean,
      /**  The initial value of a date field  */  
   InitDate:string,
      /**  The initial value of a decimal input  */  
   InitDecimal:number,
      /**  The initial value for a logical input  */  
   InitLogical:boolean,
      /**  Indicates whether or not Input Rules have been defined.  */  
   InputRules:boolean,
      /**  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  */  
   InputType:string,
   IsGlobalInputVar:boolean,
   OnLaunch:string,
   PageDisplaySeq:number,
      /**  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  */  
   PcDynLstCount:number,
   ReadOnlyExpression:string,
   TestPlan:boolean,
   ImageURL:string,
   BitFlag:number,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsSearchTableset{
   PcInputs:Erp_Tablesets_PcInputsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPcInputsSearchTableset{
   PcInputs:Erp_Tablesets_PcInputsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param configID
      @param inputName
   */  
export interface GetByID_input{
   configID:string,
   inputName:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PcInputsSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PcInputsSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PcInputsSearchTableset[],
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
   returnObj:Erp_Tablesets_PcInputsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcInputs_input{
   ds:Erp_Tablesets_PcInputsSearchTableset[],
   configID:string,
}

export interface GetNewPcInputs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcInputsSearchTableset[],
}
}

   /** Required : 
      @param whereClausePcInputs
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcInputs:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PcInputsSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPcInputsSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPcInputsSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PcInputsSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcInputsSearchTableset[],
}
}

