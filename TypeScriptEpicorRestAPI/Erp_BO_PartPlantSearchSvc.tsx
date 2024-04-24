import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartPlantSearchSvc
// Description: Part Plant Search object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/$metadata", {
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
   Description: Get PartPlantSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartPlantSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartPlantRow
   */  
export function get_PartPlantSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartPlantSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartPlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartPlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartPlantSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches", {
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
   Summary: Calls GetByID to retrieve the PartPlantSearch item
   Description: Calls GetByID to retrieve the PartPlantSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartPlantSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartPlantRow
   */  
export function get_PartPlantSearches_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartPlantRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches(" + Company + "," + PartNum + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartPlantRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartPlantSearch for the service
   Description: Calls UpdateExt to update PartPlantSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartPlantSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartPlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartPlantSearches_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches(" + Company + "," + PartNum + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete PartPlantSearch item
   Description: Call UpdateExt to delete PartPlantSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartPlantSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartPlantSearches_Company_PartNum_Plant(Company:string, PartNum:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches(" + Company + "," + PartNum + "," + Plant + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartPlantListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantListRow)
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
export function get_GetRows(whereClausePartPlant:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartPlant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartPlant=" + whereClausePartPlant
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetRows" + params, {
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
export function get_GetByID(partNum:string, plant:string, epicorHeaders?:Headers){
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
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetActiveParts
   Description: Calls the standard GetRows and filters the Inactive parts
   OperationID: GetActiveParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActiveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActiveParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetActiveParts", {
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
   Summary: Invoke method GetPartPlantPlanningParameters
   Description: Returns either base PartPlant data or attribute PartPlantPlanningAttribute data, depending if attributeSetID is supplied.
   OperationID: GetPartPlantPlanningParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartPlantPlanningParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartPlantPlanningParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartPlantPlanningParameters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetPartPlantPlanningParameters", {
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
   Summary: Invoke method GetNewPartPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetNewPartPlant", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartPlantListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartPlantRow[],
}

export interface Erp_Tablesets_PartPlantListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  */  
   "PrimWhse":string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   "MinimumQty":number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   "MaximumQty":number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   "SafetyQty":number,
      /**  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  */  
   "MinOrderQty":number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "LeadTime":number,
      /**  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  */  
   "VendorNum":number,
      /**  Default Vendor purchase point ID.  */  
   "PurPoint":string,
      /**  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  */  
   "BackFlush":boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   "MfgLotSize":number,
      /**  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   "MinMfgLotSize":number,
      /**  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   "MaxMfgLotSize":number,
      /**  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  */  
   "MfgLotMultiple":number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "DaysOfSupply":number,
      /**  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  */  
   "ReOrderLevel":boolean,
      /**  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  */  
   "MRPRecalcNeeded":boolean,
      /**  Flag indicating if MRP should process this part.  */  
   "ProcessMRP":boolean,
      /**  Flag indicating if PO suggestion should be generated for this part.  */  
   "GenerateSugg":boolean,
      /**  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  */  
   "GetFromLocalWhse":boolean,
      /**  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  */  
   "ForecastTime":number,
      /**  Default Site that part is transfered from when it is obtained via Site transfer.  */  
   "TransferPlant":string,
      /**   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  */  
   "SourceType":string,
      /**  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  */  
   "TransferLeadTime":number,
      /**  Used to determine the start date  */  
   "PrepTime":number,
      /**  Days needed to move part to stock or next job.  Deducted from Due Date.  */  
   "ReceiveTime":number,
      /**  Days out from the current date when dates on jobs, PO, TO cannot be changed  */  
   "PlanTimeFence":number,
      /**  MRP parameter not to reschedule if number of days change below  */  
   "ReschedOutDelta":number,
      /**  Same as ReschedOutDelta but for messages  */  
   "ReschedInDelta":number,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  */  
   "BuyerID":string,
      /**   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  */  
   "PersonID":string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   "CostMethod":string,
      /**  Alternate Routing method to be used for this Part/Site  */  
   "AltMethod":string,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   "KitTime":number,
      /**  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  */  
   "KitShipComplete":boolean,
      /**  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  */  
   "KitAllowChangeParms":boolean,
      /**  Indicates if all components are to be backflushed when a kit parent item is shipped.  */  
   "KitBackFlush":boolean,
      /**  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  */  
   "KitPricing":string,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   "KitPrintCompsInv":boolean,
      /**  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  */  
   "ShortHorizonDays":number,
      /**  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   "ShortHorizonMinMfgLotSize":number,
      /**  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   "ShortHorizonMaxMfgLotSize":number,
      /**  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  */  
   "LimitProdYldRecalc":boolean,
      /**  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  */  
   "QtyBearing":boolean,
      /**  System date on which the last MRP processing was run.  */  
   "MRPLastRunDate":string,
      /**  System Time (hr-min-sec) when the last MRP process was run.  */  
   "MRPLastRunTime":number,
      /**  Scheduled Date used in last MRP run  */  
   "MRPLastScheduledDate":string,
      /**  Cut Off Date used in last MRP run  */  
   "MRPLastCutOffDate":string,
      /**  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "ShortHorizonDaysSupp":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   "SNFormat":string,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
      /**  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  */  
   "UseMaskSeq":boolean,
      /**  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  */  
   "BuyToOrder":boolean,
      /**  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  */  
   "DropShip":boolean,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  */  
   "PcntTolerance":number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  */  
   "CalcPcnt":boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  */  
   "CalcQty":boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  */  
   "CalcValue":boolean,
      /**  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  */  
   "QtyAdjTolerance":number,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  */  
   "QtyTolerance":number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  */  
   "ValueTolerance":number,
      /**  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  */  
   "DemandQty":number,
      /**  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  */  
   "ReservedQty":number,
      /**  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  */  
   "AllocatedQty":number,
      /**  Cross Reference Part Number  */  
   "XRefPartNum":string,
      /**  Cross Reference Part Type  */  
   "XRefPartType":string,
      /**  System flag future use  */  
   "NeverReuseMRPJob":boolean,
      /**  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  */  
   "DeleteMRPJobs":boolean,
      /**  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  */  
   "TotMfgLeadTimeSys":number,
      /**  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  */  
   "TotMfgLeadTimeMnl":number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  */  
   "LvlMfgLeadTimeSys":number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  */  
   "LvlMfgLeadTimeMnl":number,
      /**  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  */  
   "MfgLeadTimeCalcDate":string,
      /**  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  */  
   "MfgLeadTimeMnlDate":string,
      /**  Auto consume available stock when MRP runs and creates a job.  */  
   "AutoConsumeStock":boolean,
      /**  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  */  
   "StartMinLotQty":boolean,
      /**  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  */  
   "MinLotLeadTime":number,
      /**  Indicates manufacturing lead times are entered manually by the user.  */  
   "MfgLeadTimeMnl":boolean,
      /**  Userid of user who entered manual manufacturing lead times.  */  
   "MfgLeadTimeEnteredBy":string,
      /**  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  */  
   "MinStartQty":number,
      /**  Raw Material  */  
   "RawMaterial":boolean,
      /**  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  */  
   "MultiLevelCTP":boolean,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Indicates if MRP should allow consumption of safety stock within the purchase lead time  */  
   "ConsumeSafety":boolean,
      /**  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  */  
   "SLTVendorNum":number,
      /**  Default Vendor purchase point ID.  */  
   "SLTPurPoint":string,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "ShortLeadTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  */  
   "OnHandQty":number,
   "ICTrader":boolean,
   "InActive":boolean,
   "DisableQtyBrng":boolean,
      /**  Used to indicate if the Serial Number format button should be enabled.  */  
   "EnableSerialNum":boolean,
      /**  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  */  
   "SNLeadingZeros":boolean,
      /**  Used to designate the number of digits for an Integer or Mask type serial number format.  */  
   "SNNumODigits":number,
   "PlantConfCtrlSerialTracking":number,
      /**  Base UOM Code from Part Master  */  
   "BaseUOMCode":string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   "BuyerIDName":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartPartDescription":string,
      /**   Name of person.

Purchasing: This is printed on the PO by the authorized signature 
line.
Alerts: Used as email address for recipients not defined on global alert  */  
   "PersonName":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Description.  */  
   "PrimWhseDescription":string,
      /**  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  */  
   "SerialMaskDescription":string,
      /**   Determines how the mask is being used. It can either be a validation type or generation type. 
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  */  
   "SerialMaskMaskType":number,
      /**  The Plant name. Used on shipping reports.  */  
   "TransferPlantName":string,
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
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartPlantRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   "PartNum":string,
      /**  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  */  
   "PrimWhse":string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   "MinimumQty":number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   "MaximumQty":number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   "SafetyQty":number,
      /**  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  */  
   "MinOrderQty":number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "LeadTime":number,
      /**  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  */  
   "VendorNum":number,
      /**  Default Vendor purchase point ID.  */  
   "PurPoint":string,
      /**  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  */  
   "BackFlush":boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   "MfgLotSize":number,
      /**  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   "MinMfgLotSize":number,
      /**  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   "MaxMfgLotSize":number,
      /**  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  */  
   "MfgLotMultiple":number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "DaysOfSupply":number,
      /**  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  */  
   "ReOrderLevel":boolean,
      /**  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  */  
   "MRPRecalcNeeded":boolean,
      /**  Flag indicating if MRP should process this part.  */  
   "ProcessMRP":boolean,
      /**  Flag indicating if PO suggestion should be generated for this part.  */  
   "GenerateSugg":boolean,
      /**  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  */  
   "GetFromLocalWhse":boolean,
      /**  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  */  
   "ForecastTime":number,
      /**  Default Site that part is transfered from when it is obtained via Site transfer.  */  
   "TransferPlant":string,
      /**   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  */  
   "SourceType":string,
      /**  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  */  
   "TransferLeadTime":number,
      /**  Used to determine the start date  */  
   "PrepTime":number,
      /**  Days needed to move part to stock or next job.  Deducted from Due Date.  */  
   "ReceiveTime":number,
      /**  Days out from the current date when dates on jobs, PO, TO cannot be changed  */  
   "PlanTimeFence":number,
      /**  MRP parameter not to reschedule if number of days change below  */  
   "ReschedOutDelta":number,
      /**  Same as ReschedOutDelta but for messages  */  
   "ReschedInDelta":number,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  */  
   "BuyerID":string,
      /**   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  */  
   "PersonID":string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   "CostMethod":string,
      /**  Alternate Routing method to be used for this Part/Site  */  
   "AltMethod":string,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   "KitTime":number,
      /**  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  */  
   "KitShipComplete":boolean,
      /**  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  */  
   "KitAllowChangeParms":boolean,
      /**  Indicates if all components are to be backflushed when a kit parent item is shipped.  */  
   "KitBackFlush":boolean,
      /**  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  */  
   "KitPricing":string,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   "KitPrintCompsInv":boolean,
      /**  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  */  
   "ShortHorizonDays":number,
      /**  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   "ShortHorizonMinMfgLotSize":number,
      /**  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   "ShortHorizonMaxMfgLotSize":number,
      /**  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  */  
   "LimitProdYldRecalc":boolean,
      /**  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  */  
   "QtyBearing":boolean,
      /**  System date on which the last MRP processing was run.  */  
   "MRPLastRunDate":string,
      /**  System Time (hr-min-sec) when the last MRP process was run.  */  
   "MRPLastRunTime":number,
      /**  Scheduled Date used in last MRP run  */  
   "MRPLastScheduledDate":string,
      /**  Cut Off Date used in last MRP run  */  
   "MRPLastCutOffDate":string,
      /**  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "ShortHorizonDaysSupp":number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   "SNBaseDataType":string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   "SNFormat":string,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   "SNPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   "SNLastUsedSeq":string,
      /**  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  */  
   "UseMaskSeq":boolean,
      /**  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  */  
   "BuyToOrder":boolean,
      /**  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  */  
   "DropShip":boolean,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  */  
   "PcntTolerance":number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  */  
   "CalcPcnt":boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  */  
   "CalcQty":boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  */  
   "CalcValue":boolean,
      /**  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  */  
   "QtyAdjTolerance":number,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  */  
   "QtyTolerance":number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  */  
   "ValueTolerance":number,
      /**  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  */  
   "DemandQty":number,
      /**  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  */  
   "ReservedQty":number,
      /**  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  */  
   "AllocatedQty":number,
      /**  Cross Reference Part Number  */  
   "XRefPartNum":string,
      /**  Cross Reference Part Type  */  
   "XRefPartType":string,
      /**  System flag future use  */  
   "NeverReuseMRPJob":boolean,
      /**  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  */  
   "DeleteMRPJobs":boolean,
      /**  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  */  
   "TotMfgLeadTimeSys":number,
      /**  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  */  
   "TotMfgLeadTimeMnl":number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  */  
   "LvlMfgLeadTimeSys":number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  */  
   "LvlMfgLeadTimeMnl":number,
      /**  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  */  
   "MfgLeadTimeCalcDate":string,
      /**  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  */  
   "MfgLeadTimeMnlDate":string,
      /**  Auto consume available stock when MRP runs and creates a job.  */  
   "AutoConsumeStock":boolean,
      /**  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  */  
   "StartMinLotQty":boolean,
      /**  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  */  
   "MinLotLeadTime":number,
      /**  Indicates manufacturing lead times are entered manually by the user.  */  
   "MfgLeadTimeMnl":boolean,
      /**  Userid of user who entered manual manufacturing lead times.  */  
   "MfgLeadTimeEnteredBy":string,
      /**  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  */  
   "MinStartQty":number,
      /**  Raw Material  */  
   "RawMaterial":boolean,
      /**  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  */  
   "MultiLevelCTP":boolean,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Indicates if MRP should allow consumption of safety stock within the purchase lead time  */  
   "ConsumeSafety":boolean,
      /**  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  */  
   "SLTVendorNum":number,
      /**  Default Vendor purchase point ID.  */  
   "SLTPurPoint":string,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "ShortLeadTime":number,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This is the lead time used when generating a new suggestion within the lead time window.  If this field is 0 and the Supplier is determined from the Supplier Price List, the suggestion will use the lead time from the price list.  */  
   "UrgentLeadTime":number,
      /**  This is the minimum qty required when generating a new suggestion within the lead time window.  */  
   "UrgentMinOrdQty":number,
      /**  This is used to calculate the suggestion qty to the nearest multiple when generating a new suggestion within the lead time window.  */  
   "UrgentMultQty":number,
      /**  See UrgentVendorNum  */  
   "UrgentPurPoint":string,
      /**  If this field is not populated then the system will use the standard Supplier from PartPlant, or the last Supplier the part was purchased from, or the Supplier from the first Price list found for the part.  */  
   "UrgentVendorNum":number,
      /**  PartRunMRP  */  
   "PartRunMRP":boolean,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  Indicates if this part will be excluded in the Inventory Min/Max/Safety calculation.  */  
   "MMSExclude":boolean,
      /**  Indicates if sales history for this part will be included in the Inventory Min/Max/Safety calculation.  */  
   "MMSSales":boolean,
      /**  Indicates if job materials history for this part will be included in the Inventory Min/Max/Safety calculation.  */  
   "MMSIssue":boolean,
      /**  User defined number in days, of how far back to look in usage history.  */  
   "MMSHistory":number,
      /**  User defined, percentage of MIN to be set as Safety stock value.  */  
   "MMSSafetyFactor":number,
      /**  User defined, used in calculation to defined MAX stock value.  */  
   "MMSMaxFactor":number,
      /**  WIll hold the proposed Min when the Min/Max/Safety process is ran  */  
   "SavedMinimumQty":number,
      /**  WIll hold the proposed Max when the Min/Max/Safety process is ran  */  
   "SavedMaximumQty":number,
      /**  WIll hold the proposed Safety when the Min/Max/Safety process is ran  */  
   "SavedSafetyQty":number,
      /**  It will hold the last TotalUsage used for the Saved Min/Max/Safety  */  
   "SavedCalculatedUsageQty":number,
      /**  Last Date when the Saved Min/Max/Safety were updated  */  
   "SavedOnDateTime":string,
      /**  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  */  
   "ACWPercentage":number,
      /**  Auto consume window days, this is the number of days that scheduling engine will take in consideration to look for available quantity to consume.  */  
   "ACWDays":number,
      /**  GenNewPCIDDelaySeconds  */  
   "GenNewPCIDDelaySeconds":number,
      /**  GenNewPCIDLimitDays  */  
   "GenNewPCIDLimitDays":number,
      /**  System calculated manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only.  Does not include the time on lower level parts.  Not editable by the user.  */  
   "TopLvlMfgLeadTimeSys":number,
      /**  Manually entered manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only. Does not include the time on lower level parts. Directly maintained by the user.  */  
   "TopLvlMfgLeadTimeMnl":number,
      /**  Actual Costing Category ID  */  
   "ActualCostingCategoryID":string,
      /**  Included Into Allocation Base  */  
   "IncludedIntoAllocationBase":boolean,
      /**  Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce forecast.  */  
   "ForecastDaysBefore":number,
      /**  Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days after of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  */  
   "ForecastDaysAfter":number,
      /**  RcvInspectionReqPart  */  
   "RcvInspectionReqPart":string,
      /**  Base UOM Code from Part Master  */  
   "BaseUOMCode":string,
      /**  Used to calculate the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   "CalculatedLeadTime":number,
   "ExtLeadTime":number,
      /**  Used to designate the number of digits for an Integer or Mask type serial number format.  */  
   "SNNumODigits":number,
   "UrgentVendorName":string,
   "UrgentVendorVendorID":string,
   "DisableQtyBrng":boolean,
      /**  Used to indicate if the Serial Number format button should be enabled.  */  
   "EnableSerialNum":boolean,
   "ICTrader":boolean,
   "InActive":boolean,
      /**  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  */  
   "OnHandQty":number,
   "PlantConfCtrlSerialTracking":number,
      /**  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  */  
   "SNLeadingZeros":boolean,
      /**  Indicates if there is any quantity on hand for this part  */  
   "HasOnHandQty":boolean,
   "IsActCostingAllocEnabled":boolean,
      /**  Number of Pieces for MaximumQty  */  
   "MaximumQtyNofP":number,
      /**  Number of Pieces for MaxMfgLotSize  */  
   "MaxMfgLotSizeNofP":number,
      /**  Number of Pieces for MfgLotMultiple  */  
   "MfgLotMultipleNofP":number,
      /**  Number of Pieces for MinimumQty  */  
   "MinimumQtyNofP":number,
      /**  Number of Pieces for MinMfgLotSize  */  
   "MinMfgLotSizeNofP":number,
      /**  Number of Pieces for MinOrderQty  */  
   "MinOrderQtyNofP":number,
      /**  Number of Pieces for MinStartQty  */  
   "MinStartQtyNofP":number,
   "QtyDisplayOption":string,
      /**  Number of Pieces for SafetyQty  */  
   "SafetyQtyNofP":number,
      /**  Number of Pieces for ShortHorizonMaxMfgLotSize  */  
   "ShortHorizonMaxMfgLotSizeNofP":number,
      /**  Number of Pieces for ShortHorizonMinMfgLotSize  */  
   "ShortHorizonMinMfgLotSizeNofP":number,
      /**  Number of Pieces for UrgentMinOrdQty  */  
   "UrgentMinOrdQtyNofP":number,
      /**  Number of Pieces for UrgentMultQty  */  
   "UrgentMultQtyNofP":number,
   "BitFlag":number,
   "BuyerIDName":string,
   "PartTrackInventoryAttributes":boolean,
   "PartAttrClassID":string,
   "PartSellingFactor":number,
   "PartTrackLots":boolean,
   "PartTrackSerialNum":boolean,
   "PartTrackDimension":boolean,
   "PartIUM":string,
   "PartPricePerCode":string,
   "PartPartDescription":string,
   "PartSalesUM":string,
   "PersonName":string,
   "PlantName":string,
   "PrimWhseDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskDescription":string,
   "TransferPlantName":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress2":string,
   "VendorNumZIP":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress3":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param partNum
      @param plant
   */  
export interface DeleteByID_input{
   partNum:string,
   plant:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartPlantListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  */  
   PrimWhse:string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   MinimumQty:number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   MaximumQty:number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   SafetyQty:number,
      /**  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  */  
   MinOrderQty:number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   LeadTime:number,
      /**  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  */  
   VendorNum:number,
      /**  Default Vendor purchase point ID.  */  
   PurPoint:string,
      /**  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  */  
   BackFlush:boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   MfgLotSize:number,
      /**  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   MinMfgLotSize:number,
      /**  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   MaxMfgLotSize:number,
      /**  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  */  
   MfgLotMultiple:number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   DaysOfSupply:number,
      /**  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  */  
   ReOrderLevel:boolean,
      /**  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  */  
   MRPRecalcNeeded:boolean,
      /**  Flag indicating if MRP should process this part.  */  
   ProcessMRP:boolean,
      /**  Flag indicating if PO suggestion should be generated for this part.  */  
   GenerateSugg:boolean,
      /**  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  */  
   GetFromLocalWhse:boolean,
      /**  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  */  
   ForecastTime:number,
      /**  Default Site that part is transfered from when it is obtained via Site transfer.  */  
   TransferPlant:string,
      /**   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  */  
   SourceType:string,
      /**  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  */  
   TransferLeadTime:number,
      /**  Used to determine the start date  */  
   PrepTime:number,
      /**  Days needed to move part to stock or next job.  Deducted from Due Date.  */  
   ReceiveTime:number,
      /**  Days out from the current date when dates on jobs, PO, TO cannot be changed  */  
   PlanTimeFence:number,
      /**  MRP parameter not to reschedule if number of days change below  */  
   ReschedOutDelta:number,
      /**  Same as ReschedOutDelta but for messages  */  
   ReschedInDelta:number,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  */  
   BuyerID:string,
      /**   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  */  
   PersonID:string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   CostMethod:string,
      /**  Alternate Routing method to be used for this Part/Site  */  
   AltMethod:string,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   KitTime:number,
      /**  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  */  
   KitShipComplete:boolean,
      /**  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  */  
   KitAllowChangeParms:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent item is shipped.  */  
   KitBackFlush:boolean,
      /**  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  */  
   KitPricing:string,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   KitPrintCompsInv:boolean,
      /**  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  */  
   ShortHorizonDays:number,
      /**  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   ShortHorizonMinMfgLotSize:number,
      /**  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   ShortHorizonMaxMfgLotSize:number,
      /**  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  */  
   LimitProdYldRecalc:boolean,
      /**  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  */  
   QtyBearing:boolean,
      /**  System date on which the last MRP processing was run.  */  
   MRPLastRunDate:string,
      /**  System Time (hr-min-sec) when the last MRP process was run.  */  
   MRPLastRunTime:number,
      /**  Scheduled Date used in last MRP run  */  
   MRPLastScheduledDate:string,
      /**  Cut Off Date used in last MRP run  */  
   MRPLastCutOffDate:string,
      /**  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   ShortHorizonDaysSupp:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
      /**  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  */  
   UseMaskSeq:boolean,
      /**  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  */  
   BuyToOrder:boolean,
      /**  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  */  
   DropShip:boolean,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  */  
   PcntTolerance:number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  */  
   CalcPcnt:boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  */  
   CalcQty:boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  */  
   CalcValue:boolean,
      /**  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  */  
   QtyAdjTolerance:number,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  */  
   QtyTolerance:number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  */  
   ValueTolerance:number,
      /**  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  */  
   DemandQty:number,
      /**  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  */  
   ReservedQty:number,
      /**  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  */  
   AllocatedQty:number,
      /**  Cross Reference Part Number  */  
   XRefPartNum:string,
      /**  Cross Reference Part Type  */  
   XRefPartType:string,
      /**  System flag future use  */  
   NeverReuseMRPJob:boolean,
      /**  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  */  
   DeleteMRPJobs:boolean,
      /**  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  */  
   TotMfgLeadTimeSys:number,
      /**  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  */  
   TotMfgLeadTimeMnl:number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  */  
   LvlMfgLeadTimeSys:number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  */  
   LvlMfgLeadTimeMnl:number,
      /**  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  */  
   MfgLeadTimeCalcDate:string,
      /**  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  */  
   MfgLeadTimeMnlDate:string,
      /**  Auto consume available stock when MRP runs and creates a job.  */  
   AutoConsumeStock:boolean,
      /**  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  */  
   StartMinLotQty:boolean,
      /**  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  */  
   MinLotLeadTime:number,
      /**  Indicates manufacturing lead times are entered manually by the user.  */  
   MfgLeadTimeMnl:boolean,
      /**  Userid of user who entered manual manufacturing lead times.  */  
   MfgLeadTimeEnteredBy:string,
      /**  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  */  
   MinStartQty:number,
      /**  Raw Material  */  
   RawMaterial:boolean,
      /**  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  */  
   MultiLevelCTP:boolean,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Indicates if MRP should allow consumption of safety stock within the purchase lead time  */  
   ConsumeSafety:boolean,
      /**  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  */  
   SLTVendorNum:number,
      /**  Default Vendor purchase point ID.  */  
   SLTPurPoint:string,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   ShortLeadTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  */  
   OnHandQty:number,
   ICTrader:boolean,
   InActive:boolean,
   DisableQtyBrng:boolean,
      /**  Used to indicate if the Serial Number format button should be enabled.  */  
   EnableSerialNum:boolean,
      /**  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  */  
   SNLeadingZeros:boolean,
      /**  Used to designate the number of digits for an Integer or Mask type serial number format.  */  
   SNNumODigits:number,
   PlantConfCtrlSerialTracking:number,
      /**  Base UOM Code from Part Master  */  
   BaseUOMCode:string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   BuyerIDName:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartTrackLots:boolean,
      /**  Describes the Part.  */  
   PartPartDescription:string,
      /**   Name of person.

Purchasing: This is printed on the PO by the authorized signature 
line.
Alerts: Used as email address for recipients not defined on global alert  */  
   PersonName:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Description.  */  
   PrimWhseDescription:string,
      /**  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  */  
   SerialMaskDescription:string,
      /**   Determines how the mask is being used. It can either be a validation type or generation type. 
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  */  
   SerialMaskMaskType:number,
      /**  The Plant name. Used on shipping reports.  */  
   TransferPlantName:string,
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
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartPlantListTableset{
   PartPlantList:Erp_Tablesets_PartPlantListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartPlantRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  */  
   PrimWhse:string,
      /**  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  */  
   MinimumQty:number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  */  
   MaximumQty:number,
      /**   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  */  
   SafetyQty:number,
      /**  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  */  
   MinOrderQty:number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   LeadTime:number,
      /**  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  */  
   VendorNum:number,
      /**  Default Vendor purchase point ID.  */  
   PurPoint:string,
      /**  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  */  
   BackFlush:boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   MfgLotSize:number,
      /**  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   MinMfgLotSize:number,
      /**  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   MaxMfgLotSize:number,
      /**  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  */  
   MfgLotMultiple:number,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   DaysOfSupply:number,
      /**  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  */  
   ReOrderLevel:boolean,
      /**  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  */  
   MRPRecalcNeeded:boolean,
      /**  Flag indicating if MRP should process this part.  */  
   ProcessMRP:boolean,
      /**  Flag indicating if PO suggestion should be generated for this part.  */  
   GenerateSugg:boolean,
      /**  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  */  
   GetFromLocalWhse:boolean,
      /**  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  */  
   ForecastTime:number,
      /**  Default Site that part is transfered from when it is obtained via Site transfer.  */  
   TransferPlant:string,
      /**   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  */  
   SourceType:string,
      /**  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  */  
   TransferLeadTime:number,
      /**  Used to determine the start date  */  
   PrepTime:number,
      /**  Days needed to move part to stock or next job.  Deducted from Due Date.  */  
   ReceiveTime:number,
      /**  Days out from the current date when dates on jobs, PO, TO cannot be changed  */  
   PlanTimeFence:number,
      /**  MRP parameter not to reschedule if number of days change below  */  
   ReschedOutDelta:number,
      /**  Same as ReschedOutDelta but for messages  */  
   ReschedInDelta:number,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  */  
   BuyerID:string,
      /**   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  */  
   PersonID:string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   CostMethod:string,
      /**  Alternate Routing method to be used for this Part/Site  */  
   AltMethod:string,
      /**  For Manufactured Parts to determine the Due date of the material  */  
   KitTime:number,
      /**  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  */  
   KitShipComplete:boolean,
      /**  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  */  
   KitAllowChangeParms:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent item is shipped.  */  
   KitBackFlush:boolean,
      /**  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  */  
   KitPricing:string,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  */  
   KitPrintCompsInv:boolean,
      /**  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  */  
   ShortHorizonDays:number,
      /**  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  */  
   ShortHorizonMinMfgLotSize:number,
      /**  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  */  
   ShortHorizonMaxMfgLotSize:number,
      /**  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  */  
   LimitProdYldRecalc:boolean,
      /**  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  */  
   QtyBearing:boolean,
      /**  System date on which the last MRP processing was run.  */  
   MRPLastRunDate:string,
      /**  System Time (hr-min-sec) when the last MRP process was run.  */  
   MRPLastRunTime:number,
      /**  Scheduled Date used in last MRP run  */  
   MRPLastScheduledDate:string,
      /**  Cut Off Date used in last MRP run  */  
   MRPLastCutOffDate:string,
      /**  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   ShortHorizonDaysSupp:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
      /**  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  */  
   UseMaskSeq:boolean,
      /**  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  */  
   BuyToOrder:boolean,
      /**  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  */  
   DropShip:boolean,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  */  
   PcntTolerance:number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  */  
   CalcPcnt:boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  */  
   CalcQty:boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  */  
   CalcValue:boolean,
      /**  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  */  
   QtyAdjTolerance:number,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  */  
   QtyTolerance:number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  */  
   ValueTolerance:number,
      /**  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  */  
   DemandQty:number,
      /**  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  */  
   ReservedQty:number,
      /**  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  */  
   AllocatedQty:number,
      /**  Cross Reference Part Number  */  
   XRefPartNum:string,
      /**  Cross Reference Part Type  */  
   XRefPartType:string,
      /**  System flag future use  */  
   NeverReuseMRPJob:boolean,
      /**  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  */  
   DeleteMRPJobs:boolean,
      /**  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  */  
   TotMfgLeadTimeSys:number,
      /**  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  */  
   TotMfgLeadTimeMnl:number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  */  
   LvlMfgLeadTimeSys:number,
      /**  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  */  
   LvlMfgLeadTimeMnl:number,
      /**  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  */  
   MfgLeadTimeCalcDate:string,
      /**  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  */  
   MfgLeadTimeMnlDate:string,
      /**  Auto consume available stock when MRP runs and creates a job.  */  
   AutoConsumeStock:boolean,
      /**  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  */  
   StartMinLotQty:boolean,
      /**  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  */  
   MinLotLeadTime:number,
      /**  Indicates manufacturing lead times are entered manually by the user.  */  
   MfgLeadTimeMnl:boolean,
      /**  Userid of user who entered manual manufacturing lead times.  */  
   MfgLeadTimeEnteredBy:string,
      /**  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  */  
   MinStartQty:number,
      /**  Raw Material  */  
   RawMaterial:boolean,
      /**  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  */  
   MultiLevelCTP:boolean,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Indicates if MRP should allow consumption of safety stock within the purchase lead time  */  
   ConsumeSafety:boolean,
      /**  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  */  
   SLTVendorNum:number,
      /**  Default Vendor purchase point ID.  */  
   SLTPurPoint:string,
      /**  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   ShortLeadTime:number,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This is the lead time used when generating a new suggestion within the lead time window.  If this field is 0 and the Supplier is determined from the Supplier Price List, the suggestion will use the lead time from the price list.  */  
   UrgentLeadTime:number,
      /**  This is the minimum qty required when generating a new suggestion within the lead time window.  */  
   UrgentMinOrdQty:number,
      /**  This is used to calculate the suggestion qty to the nearest multiple when generating a new suggestion within the lead time window.  */  
   UrgentMultQty:number,
      /**  See UrgentVendorNum  */  
   UrgentPurPoint:string,
      /**  If this field is not populated then the system will use the standard Supplier from PartPlant, or the last Supplier the part was purchased from, or the Supplier from the first Price list found for the part.  */  
   UrgentVendorNum:number,
      /**  PartRunMRP  */  
   PartRunMRP:boolean,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  Indicates if this part will be excluded in the Inventory Min/Max/Safety calculation.  */  
   MMSExclude:boolean,
      /**  Indicates if sales history for this part will be included in the Inventory Min/Max/Safety calculation.  */  
   MMSSales:boolean,
      /**  Indicates if job materials history for this part will be included in the Inventory Min/Max/Safety calculation.  */  
   MMSIssue:boolean,
      /**  User defined number in days, of how far back to look in usage history.  */  
   MMSHistory:number,
      /**  User defined, percentage of MIN to be set as Safety stock value.  */  
   MMSSafetyFactor:number,
      /**  User defined, used in calculation to defined MAX stock value.  */  
   MMSMaxFactor:number,
      /**  WIll hold the proposed Min when the Min/Max/Safety process is ran  */  
   SavedMinimumQty:number,
      /**  WIll hold the proposed Max when the Min/Max/Safety process is ran  */  
   SavedMaximumQty:number,
      /**  WIll hold the proposed Safety when the Min/Max/Safety process is ran  */  
   SavedSafetyQty:number,
      /**  It will hold the last TotalUsage used for the Saved Min/Max/Safety  */  
   SavedCalculatedUsageQty:number,
      /**  Last Date when the Saved Min/Max/Safety were updated  */  
   SavedOnDateTime:string,
      /**  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  */  
   ACWPercentage:number,
      /**  Auto consume window days, this is the number of days that scheduling engine will take in consideration to look for available quantity to consume.  */  
   ACWDays:number,
      /**  GenNewPCIDDelaySeconds  */  
   GenNewPCIDDelaySeconds:number,
      /**  GenNewPCIDLimitDays  */  
   GenNewPCIDLimitDays:number,
      /**  System calculated manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only.  Does not include the time on lower level parts.  Not editable by the user.  */  
   TopLvlMfgLeadTimeSys:number,
      /**  Manually entered manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only. Does not include the time on lower level parts. Directly maintained by the user.  */  
   TopLvlMfgLeadTimeMnl:number,
      /**  Actual Costing Category ID  */  
   ActualCostingCategoryID:string,
      /**  Included Into Allocation Base  */  
   IncludedIntoAllocationBase:boolean,
      /**  Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce forecast.  */  
   ForecastDaysBefore:number,
      /**  Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days after of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  */  
   ForecastDaysAfter:number,
      /**  RcvInspectionReqPart  */  
   RcvInspectionReqPart:string,
      /**  Base UOM Code from Part Master  */  
   BaseUOMCode:string,
      /**  Used to calculate the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   CalculatedLeadTime:number,
   ExtLeadTime:number,
      /**  Used to designate the number of digits for an Integer or Mask type serial number format.  */  
   SNNumODigits:number,
   UrgentVendorName:string,
   UrgentVendorVendorID:string,
   DisableQtyBrng:boolean,
      /**  Used to indicate if the Serial Number format button should be enabled.  */  
   EnableSerialNum:boolean,
   ICTrader:boolean,
   InActive:boolean,
      /**  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  */  
   OnHandQty:number,
   PlantConfCtrlSerialTracking:number,
      /**  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  */  
   SNLeadingZeros:boolean,
      /**  Indicates if there is any quantity on hand for this part  */  
   HasOnHandQty:boolean,
   IsActCostingAllocEnabled:boolean,
      /**  Number of Pieces for MaximumQty  */  
   MaximumQtyNofP:number,
      /**  Number of Pieces for MaxMfgLotSize  */  
   MaxMfgLotSizeNofP:number,
      /**  Number of Pieces for MfgLotMultiple  */  
   MfgLotMultipleNofP:number,
      /**  Number of Pieces for MinimumQty  */  
   MinimumQtyNofP:number,
      /**  Number of Pieces for MinMfgLotSize  */  
   MinMfgLotSizeNofP:number,
      /**  Number of Pieces for MinOrderQty  */  
   MinOrderQtyNofP:number,
      /**  Number of Pieces for MinStartQty  */  
   MinStartQtyNofP:number,
   QtyDisplayOption:string,
      /**  Number of Pieces for SafetyQty  */  
   SafetyQtyNofP:number,
      /**  Number of Pieces for ShortHorizonMaxMfgLotSize  */  
   ShortHorizonMaxMfgLotSizeNofP:number,
      /**  Number of Pieces for ShortHorizonMinMfgLotSize  */  
   ShortHorizonMinMfgLotSizeNofP:number,
      /**  Number of Pieces for UrgentMinOrdQty  */  
   UrgentMinOrdQtyNofP:number,
      /**  Number of Pieces for UrgentMultQty  */  
   UrgentMultQtyNofP:number,
   BitFlag:number,
   BuyerIDName:string,
   PartTrackInventoryAttributes:boolean,
   PartAttrClassID:string,
   PartSellingFactor:number,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartIUM:string,
   PartPricePerCode:string,
   PartPartDescription:string,
   PartSalesUM:string,
   PersonName:string,
   PlantName:string,
   PrimWhseDescription:string,
   SerialMaskMaskType:number,
   SerialMaskDescription:string,
   TransferPlantName:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress2:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorNumAddress3:string,
   VendorNumName:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartPlantSearchTableset{
   PartPlant:Erp_Tablesets_PartPlantRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartPlantSearchTableset{
   PartPlant:Erp_Tablesets_PartPlantRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param WhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GetActiveParts_input{
      /**  Whereclause.  */  
   WhereClause:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
}

export interface GetActiveParts_output{
   returnObj:Erp_Tablesets_PartPlantSearchTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param partNum
      @param plant
   */  
export interface GetByID_input{
   partNum:string,
   plant:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartPlantSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartPlantSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartPlantSearchTableset[],
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
   returnObj:Erp_Tablesets_PartPlantListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
   */  
export interface GetNewPartPlant_input{
   ds:Erp_Tablesets_PartPlantSearchTableset[],
   partNum:string,
}

export interface GetNewPartPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartPlantSearchTableset[],
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param plant
   */  
export interface GetPartPlantPlanningParameters_input{
   partNum:string,
   attributeSetID:number,
   plant:string,
}

export interface GetPartPlantPlanningParameters_output{
   returnObj:Erp_Tablesets_PartPlantSearchTableset[],
}

   /** Required : 
      @param whereClausePartPlant
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartPlant:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartPlantSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPartPlantSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartPlantSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartPlantSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartPlantSearchTableset[],
}
}

