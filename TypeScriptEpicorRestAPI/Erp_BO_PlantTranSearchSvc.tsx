import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PlantTranSearchSvc
// Description: This BO was created to retrieve the information stored from the
           PartTran table. Uses this BO to retrieve the transactions between plants
           for one or more specified parts.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/$metadata", {
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
   Description: Get PlantTranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantTranSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranRow
   */  
export function get_PlantTranSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantTranSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantTranSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches", {
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
   Summary: Calls GetByID to retrieve the PlantTranSearch item
   Description: Calls GetByID to retrieve the PlantTranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   */  
export function get_PlantTranSearches_Company_TranNum(Company:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches(" + Company + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PlantTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantTranSearch for the service
   Description: Calls UpdateExt to update PlantTranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantTranSearches_Company_TranNum(Company:string, TranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches(" + Company + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete PlantTranSearch item
   Description: Call UpdateExt to delete PlantTranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantTranSearches_Company_TranNum(Company:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches(" + Company + "," + TranNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranListRow)
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
export function get_GetRows(whereClausePlantTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePlantTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantTran=" + whereClausePlantTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/GetRows" + params, {
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
export function get_GetByID(tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPlantTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantTran(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/GetNewPlantTran", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantTranListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantTranRow[],
}

export interface Erp_Tablesets_PlantTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) the record was created.  */  
   "SysTime":number,
      /**  Unique ID  */  
   "TranNum":number,
      /**   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Part Number that this transfer is for.  */  
   "PartNum":string,
      /**  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Site that the transfer is from.  */  
   "FromPlant":string,
      /**  Site that the transfer is to.  */  
   "ToPlant":string,
      /**  The Warehouse the part is being transferred From.  */  
   "FromWarehouseCode":string,
      /**  Identifies the "From" Bin location that this transfer affected.  */  
   "BinNum":string,
      /**  The Job that the material is being transferred from.  */  
   "FromJobNum":string,
      /**  The Job Assembly (zero for final assembly) that the material is being transferred from.  */  
   "FromAssemblySeq":number,
      /**  The Warehouse the part is being transferred To.  */  
   "WarehseCodeTo":string,
      /**  "To" Job Number that this transfer is associated with, if any.  */  
   "JobNum":string,
      /**  Assembly Sequence associated with the JobNum.  */  
   "AssemblySeq":number,
      /**  Sequence number of the specific Job Material record.  */  
   "JobMtl":number,
      /**  Transfer Quantity.  */  
   "TranQty":number,
      /**  Date of transaction.  */  
   "TranDate":string,
      /**  Unit of Measure.  */  
   "UM":string,
      /**  From Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Used to hold a short comment on the Site transfer.  */  
   "PlntTranReference":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  */  
   "EntryPerson":string,
      /**   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  */  
   "TranType":string,
      /**   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  */  
   "InternalPrice":number,
      /**  Pack ID  */  
   "PackNum":number,
      /**  System date at time that record was received.  */  
   "RecSysDate":string,
      /**  System Time (hr-min-sec) when transaction was received.  */  
   "RecSysTime":number,
      /**  date of receipt transaction.  */  
   "RecTranDate":string,
      /**  This field is set equal to the Login ID variable.  It cannot be overridden.  */  
   "RecEntryPerson":string,
      /**  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  */  
   "RecIssuedComplete":boolean,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlMtlBurUnitCost":number,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "calcRequiredQty":number,
   "calcDimTranQty":number,
      /**  The required quantity  */  
   "RequiredQty":number,
      /**  Where to receive item to? (Values:  Stock or Job)  */  
   "ReceiveTo":string,
      /**  The generated legal number  */  
   "LegalNumber":string,
      /**  The warehouse code to receive to.  */  
   "ReceiveToWhseCode":string,
      /**  The bin num to receive to.  */  
   "ReceiveToBinNum":string,
   "ReceiveIssueComplete":boolean,
   "SerialNumTranType":string,
   "LegalNumberMessage":string,
      /**  ReceiveToDescription  */  
   "ReceiveToDescription":string,
      /**  ReceiveToWhseDescription  */  
   "ReceiveToWhseDescription":string,
   "TFRequestedQty":number,
   "TFRequestedQtyUOM":string,
   "ThisTranQty":number,
   "ThisInvtyUOM":string,
   "SerialProcessing":boolean,
      /**  Part tran record's primary key - for the later use in the report  */  
   "PartTranPKs":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
      /**  Description for the dimension code.  */  
   "DimCodeDimCodeDescription":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "PackNumName":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
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
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) the record was created.  */  
   "SysTime":number,
      /**  Unique ID  */  
   "TranNum":number,
      /**   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   "TranStatus":string,
      /**  Part Number that this transfer is for.  */  
   "PartNum":string,
      /**  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Site that the transfer is from.  */  
   "FromPlant":string,
      /**  Site that the transfer is to.  */  
   "ToPlant":string,
      /**  The Warehouse the part is being transferred From.  */  
   "FromWarehouseCode":string,
      /**  Identifies the "From" Bin location that this transfer affected.  */  
   "BinNum":string,
      /**  The Job that the material is being transferred from.  */  
   "FromJobNum":string,
      /**  The Job Assembly (zero for final assembly) that the material is being transferred from.  */  
   "FromAssemblySeq":number,
      /**  The Warehouse the part is being transferred To.  */  
   "WarehseCodeTo":string,
      /**  "To" Job Number that this transfer is associated with, if any.  */  
   "JobNum":string,
      /**  Assembly Sequence associated with the JobNum.  */  
   "AssemblySeq":number,
      /**  Sequence number of the specific Job Material record.  */  
   "JobMtl":number,
      /**  Transfer Quantity.  */  
   "TranQty":number,
      /**  Date of transaction.  */  
   "TranDate":string,
      /**  Unit of Measure.  */  
   "UM":string,
      /**  From Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Used to hold a short comment on the Site transfer.  */  
   "PlntTranReference":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  */  
   "EntryPerson":string,
      /**   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  */  
   "TranType":string,
      /**   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  */  
   "InternalPrice":number,
      /**  Pack ID  */  
   "PackNum":number,
      /**  System date at time that record was received.  */  
   "RecSysDate":string,
      /**  System Time (hr-min-sec) when transaction was received.  */  
   "RecSysTime":number,
      /**  date of receipt transaction.  */  
   "RecTranDate":string,
      /**  This field is set equal to the Login ID variable.  It cannot be overridden.  */  
   "RecEntryPerson":string,
      /**  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  */  
   "RecIssuedComplete":boolean,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlMtlBurUnitCost":number,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "TFOrdNum":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlUnitCost":number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltLbrUnitCost":number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltBurUnitCost":number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltSubUnitCost":number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   "AltMtlBurUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlMtlUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlLabUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlSubUnitCost":number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   "AltMtlBurdenUnitCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  PCID to receive from  */  
   "FromPCID":string,
      /**  PCID to receive to  */  
   "ToPCID":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
   "calcDimTranQty":number,
   "calcRequiredQty":number,
      /**  The generated legal number  */  
   "LegalNumber":string,
   "LegalNumberMessage":string,
      /**  Part tran record's primary key - for the later use in the report  */  
   "PartTranPKs":string,
   "ReceiveIssueComplete":boolean,
      /**  Where to receive item to? (Values:  Stock or Job)  */  
   "ReceiveTo":string,
      /**  The bin num to receive to.  */  
   "ReceiveToBinNum":string,
      /**  ReceiveToDescription  */  
   "ReceiveToDescription":string,
      /**  The warehouse code to receive to.  */  
   "ReceiveToWhseCode":string,
      /**  ReceiveToWhseDescription  */  
   "ReceiveToWhseDescription":string,
      /**  The required quantity  */  
   "RequiredQty":number,
   "SerialNumTranType":string,
   "SerialProcessing":boolean,
   "TFRequestedQty":number,
   "TFRequestedQtyUOM":string,
   "ThisInvtyUOM":string,
   "ThisTranQty":number,
      /**  Transaction Document Type ID  */  
   "TranDocTypeID":string,
      /**  Parent PCID to the FromPCID field.  */  
   "ParentFromPCID":string,
      /**  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  */  
   "SystemTranType":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "DimCodeDimCodeDescription":string,
   "PackNumName":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumAttrClassID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param tranNum
   */  
export interface DeleteByID_input{
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PlantTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) the record was created.  */  
   SysTime:number,
      /**  Unique ID  */  
   TranNum:number,
      /**   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Part Number that this transfer is for.  */  
   PartNum:string,
      /**  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Site that the transfer is from.  */  
   FromPlant:string,
      /**  Site that the transfer is to.  */  
   ToPlant:string,
      /**  The Warehouse the part is being transferred From.  */  
   FromWarehouseCode:string,
      /**  Identifies the "From" Bin location that this transfer affected.  */  
   BinNum:string,
      /**  The Job that the material is being transferred from.  */  
   FromJobNum:string,
      /**  The Job Assembly (zero for final assembly) that the material is being transferred from.  */  
   FromAssemblySeq:number,
      /**  The Warehouse the part is being transferred To.  */  
   WarehseCodeTo:string,
      /**  "To" Job Number that this transfer is associated with, if any.  */  
   JobNum:string,
      /**  Assembly Sequence associated with the JobNum.  */  
   AssemblySeq:number,
      /**  Sequence number of the specific Job Material record.  */  
   JobMtl:number,
      /**  Transfer Quantity.  */  
   TranQty:number,
      /**  Date of transaction.  */  
   TranDate:string,
      /**  Unit of Measure.  */  
   UM:string,
      /**  From Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Used to hold a short comment on the Site transfer.  */  
   PlntTranReference:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  */  
   EntryPerson:string,
      /**   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  */  
   TranType:string,
      /**   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  */  
   InternalPrice:number,
      /**  Pack ID  */  
   PackNum:number,
      /**  System date at time that record was received.  */  
   RecSysDate:string,
      /**  System Time (hr-min-sec) when transaction was received.  */  
   RecSysTime:number,
      /**  date of receipt transaction.  */  
   RecTranDate:string,
      /**  This field is set equal to the Login ID variable.  It cannot be overridden.  */  
   RecEntryPerson:string,
      /**  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  */  
   RecIssuedComplete:boolean,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlMtlBurUnitCost:number,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   calcRequiredQty:number,
   calcDimTranQty:number,
      /**  The required quantity  */  
   RequiredQty:number,
      /**  Where to receive item to? (Values:  Stock or Job)  */  
   ReceiveTo:string,
      /**  The generated legal number  */  
   LegalNumber:string,
      /**  The warehouse code to receive to.  */  
   ReceiveToWhseCode:string,
      /**  The bin num to receive to.  */  
   ReceiveToBinNum:string,
   ReceiveIssueComplete:boolean,
   SerialNumTranType:string,
   LegalNumberMessage:string,
      /**  ReceiveToDescription  */  
   ReceiveToDescription:string,
      /**  ReceiveToWhseDescription  */  
   ReceiveToWhseDescription:string,
   TFRequestedQty:number,
   TFRequestedQtyUOM:string,
   ThisTranQty:number,
   ThisInvtyUOM:string,
   SerialProcessing:boolean,
      /**  Part tran record's primary key - for the later use in the report  */  
   PartTranPKs:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
      /**  Description for the dimension code.  */  
   DimCodeDimCodeDescription:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   PackNumName:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantTranListTableset{
   PlantTranList:Erp_Tablesets_PlantTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlantTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) the record was created.  */  
   SysTime:number,
      /**  Unique ID  */  
   TranNum:number,
      /**   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  */  
   TranStatus:string,
      /**  Part Number that this transfer is for.  */  
   PartNum:string,
      /**  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Site that the transfer is from.  */  
   FromPlant:string,
      /**  Site that the transfer is to.  */  
   ToPlant:string,
      /**  The Warehouse the part is being transferred From.  */  
   FromWarehouseCode:string,
      /**  Identifies the "From" Bin location that this transfer affected.  */  
   BinNum:string,
      /**  The Job that the material is being transferred from.  */  
   FromJobNum:string,
      /**  The Job Assembly (zero for final assembly) that the material is being transferred from.  */  
   FromAssemblySeq:number,
      /**  The Warehouse the part is being transferred To.  */  
   WarehseCodeTo:string,
      /**  "To" Job Number that this transfer is associated with, if any.  */  
   JobNum:string,
      /**  Assembly Sequence associated with the JobNum.  */  
   AssemblySeq:number,
      /**  Sequence number of the specific Job Material record.  */  
   JobMtl:number,
      /**  Transfer Quantity.  */  
   TranQty:number,
      /**  Date of transaction.  */  
   TranDate:string,
      /**  Unit of Measure.  */  
   UM:string,
      /**  From Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Used to hold a short comment on the Site transfer.  */  
   PlntTranReference:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  */  
   EntryPerson:string,
      /**   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  */  
   TranType:string,
      /**   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  */  
   InternalPrice:number,
      /**  Pack ID  */  
   PackNum:number,
      /**  System date at time that record was received.  */  
   RecSysDate:string,
      /**  System Time (hr-min-sec) when transaction was received.  */  
   RecSysTime:number,
      /**  date of receipt transaction.  */  
   RecTranDate:string,
      /**  This field is set equal to the Login ID variable.  It cannot be overridden.  */  
   RecEntryPerson:string,
      /**  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  */  
   RecIssuedComplete:boolean,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlMtlBurUnitCost:number,
      /**  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   TFOrdNum:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  PCID to receive from  */  
   FromPCID:string,
      /**  PCID to receive to  */  
   ToPCID:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
   calcDimTranQty:number,
   calcRequiredQty:number,
      /**  The generated legal number  */  
   LegalNumber:string,
   LegalNumberMessage:string,
      /**  Part tran record's primary key - for the later use in the report  */  
   PartTranPKs:string,
   ReceiveIssueComplete:boolean,
      /**  Where to receive item to? (Values:  Stock or Job)  */  
   ReceiveTo:string,
      /**  The bin num to receive to.  */  
   ReceiveToBinNum:string,
      /**  ReceiveToDescription  */  
   ReceiveToDescription:string,
      /**  The warehouse code to receive to.  */  
   ReceiveToWhseCode:string,
      /**  ReceiveToWhseDescription  */  
   ReceiveToWhseDescription:string,
      /**  The required quantity  */  
   RequiredQty:number,
   SerialNumTranType:string,
   SerialProcessing:boolean,
   TFRequestedQty:number,
   TFRequestedQtyUOM:string,
   ThisInvtyUOM:string,
   ThisTranQty:number,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
      /**  Parent PCID to the FromPCID field.  */  
   ParentFromPCID:string,
      /**  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  */  
   SystemTranType:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   DimCodeDimCodeDescription:string,
   PackNumName:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumAttrClassID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantTranSearchTableset{
   PlantTran:Erp_Tablesets_PlantTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPlantTranSearchTableset{
   PlantTran:Erp_Tablesets_PlantTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param tranNum
   */  
export interface GetByID_input{
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PlantTranSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PlantTranSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PlantTranSearchTableset[],
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
   returnObj:Erp_Tablesets_PlantTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPlantTran_input{
   ds:Erp_Tablesets_PlantTranSearchTableset[],
}

export interface GetNewPlantTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTranSearchTableset[],
}
}

   /** Required : 
      @param whereClausePlantTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePlantTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PlantTranSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPlantTranSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPlantTranSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PlantTranSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantTranSearchTableset[],
}
}

