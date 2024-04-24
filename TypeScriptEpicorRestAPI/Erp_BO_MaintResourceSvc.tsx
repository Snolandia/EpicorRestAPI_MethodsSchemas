import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MaintResourceSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/$metadata", {
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
   Description: Get MaintResources items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaintResources
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceRow
   */  
export function get_MaintResources(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/MaintResources", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaintResources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MaintResources(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/MaintResources", {
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
   Summary: Calls GetByID to retrieve the MaintResource item
   Description: Calls GetByID to retrieve the MaintResource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintResource
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceRow
   */  
export function get_MaintResources_Company_ResourceID(Company:string, ResourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ResourceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/MaintResources(" + Company + "," + ResourceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ResourceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MaintResource for the service
   Description: Calls UpdateExt to update MaintResource. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaintResource
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MaintResources_Company_ResourceID(Company:string, ResourceID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/MaintResources(" + Company + "," + ResourceID + ")", {
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
   Summary: Call UpdateExt to delete MaintResource item
   Description: Call UpdateExt to delete MaintResource item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaintResource
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MaintResources_Company_ResourceID(Company:string, ResourceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/MaintResources(" + Company + "," + ResourceID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceListRow)
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
export function get_GetRows(whereClauseResource:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseResource!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseResource=" + whereClauseResource
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(resourceID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof resourceID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "resourceID=" + resourceID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/GetList" + params, {
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
   Summary: Invoke method GetNewResource
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewResource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/GetNewResource", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MaintResourceSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ResourceRow[],
}

export interface Erp_Tablesets_ResourceListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  Full description of Resource.  */  
   "Description":string,
      /**   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  */  
   "Inactive":boolean,
      /**  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  */  
   "NextMaintDate":string,
      /**  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  */  
   "ResourceType":string,
      /**  Indicates the production quantities produced by this Resource will be tracked.  */  
   "TrackProdQty":boolean,
      /**  Links this Resource to a Part, which must be valid in the Part table.  */  
   "LinkedPart":string,
      /**  Location  */  
   "Location":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
   "ResourceGrpDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ResourceRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  Full description of Resource.  */  
   "Description":string,
      /**   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  */  
   "Inactive":boolean,
      /**  If yes then this Resource is scheduled as though it has finite production capacity.  */  
   "Finite":boolean,
      /**  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  */  
   "AllowManualOverride":boolean,
      /**  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  */  
   "NextMaintDate":string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   "OutputWhse":string,
      /**  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  */  
   "OutputBinNum":string,
      /**  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  */  
   "BackflushWhse":string,
      /**  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  */  
   "BackflushBinNum":string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   "InputWhse":string,
      /**  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  */  
   "InputBinNum":string,
      /**  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  */  
   "ResourceType":string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   "ConcurrentCapacity":number,
      /**  Indicates the production quantities produced by this Resource will be tracked.  */  
   "TrackProdQty":boolean,
      /**  Links this Resource to a Part, which must be valid in the Part table.  */  
   "LinkedPart":string,
      /**  Asset number of the Resource.  Links the Resource to a Fixed Asset.  */  
   "AssetNum":string,
      /**  The burden rate for production.  */  
   "ProdBurRate":number,
      /**  The labor rate for production.  */  
   "ProdLabRate":number,
      /**  Default burden rate for Setup time.  */  
   "SetupBurRate":number,
      /**  Default labor rate for setup time.  */  
   "SetupLabRate":number,
      /**   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdBurRate":number,
      /**   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QProdLabRate":number,
      /**   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupBurRate":number,
      /**   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   "QSetupLabRate":number,
      /**  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  */  
   "QBurdenType":string,
      /**  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   "GetDefaultBurdenFromGroup":boolean,
      /**  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  */  
   "VendorNum":number,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   "BurdenType":string,
      /**  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  */  
   "CalendarID":string,
      /**  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  */  
   "MoveHours":number,
      /**  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  */  
   "QueHours":number,
      /**  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  */  
   "GetDefaultMQFromGroup":boolean,
      /**  Indicates that the Resource is visible in Overload Informer.  */  
   "InformOverload":boolean,
      /**  The minimum overload threshold before a day shows up in the Overload Informer.  */  
   "MinOverloadPerc":number,
      /**   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  */  
   "OpCode":string,
      /**   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  */  
   "OpStdID":string,
      /**  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   "GetDefaultLaborFromGroup":boolean,
      /**  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  */  
   "FiniteHorizon":number,
      /**  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  */  
   "AutoMove":boolean,
      /**  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  */  
   "SplitOperations":boolean,
      /**  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  */  
   "DailyProdQty":number,
      /**  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  */  
   "BillLaborRate":number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   "DailyProdRate":number,
      /**  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   "GetDefaultWhseFromGroup":boolean,
      /**  Location  */  
   "Location":boolean,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  */  
   "EquipID":string,
      /**  URL  */  
   "URL":string,
      /**  JDFDevice  */  
   "JDFDevice":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  NumCavs  */  
   "NumCavs":number,
      /**  RunnerWt  */  
   "RunnerWt":number,
      /**  SetupTime  */  
   "SetupTime":number,
      /**  TearDownTime  */  
   "TearDownTime":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  Brand  */  
   "Brand":string,
      /**  LocID  */  
   "LocID":string,
      /**  PmMapNo  */  
   "PmMapNo":number,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MobileResource  */  
   "MobileResource":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  MESQueue  */  
   "MESQueue":boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   "CharacteristicAttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CharacteristicAttributeSetID":number,
      /**  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  */  
   "ECPCEnabled":boolean,
      /**  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  */  
   "EquipCreate":boolean,
      /**  Plant from Resource Group  */  
   "Plant":string,
   "ReadOnlyFields":string,
   "BitFlag":number,
   "LinkedPartTrackLots":boolean,
   "LinkedPartPartDescription":string,
   "LinkedPartIUM":string,
   "LinkedPartTrackSerialNum":boolean,
   "LinkedPartTrackDimension":boolean,
   "LinkedPartSellingFactor":number,
   "LinkedPartSalesUM":string,
   "LinkedPartPricePerCode":string,
   "OpCodeOpDesc":string,
   "OpStdDescription":string,
   "ProdCalDescription":string,
   "ResourceTypeDescription":string,
   "ResourceTypeExternalMESType":string,
   "WhseBackflushWhseDescDescription":string,
   "WhseInputWhseDescDescription":string,
   "WhseOutputWhseDescDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param resourceID
   */  
export interface DeleteByID_input{
   resourceID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ResourceListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  Full description of Resource.  */  
   Description:string,
      /**   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  */  
   Inactive:boolean,
      /**  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  */  
   NextMaintDate:string,
      /**  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  */  
   ResourceType:string,
      /**  Indicates the production quantities produced by this Resource will be tracked.  */  
   TrackProdQty:boolean,
      /**  Links this Resource to a Part, which must be valid in the Part table.  */  
   LinkedPart:string,
      /**  Location  */  
   Location:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
   ResourceGrpDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceListTableset{
   ResourceList:Erp_Tablesets_ResourceListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ResourceRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  Full description of Resource.  */  
   Description:string,
      /**   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  */  
   Inactive:boolean,
      /**  If yes then this Resource is scheduled as though it has finite production capacity.  */  
   Finite:boolean,
      /**  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  */  
   AllowManualOverride:boolean,
      /**  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  */  
   NextMaintDate:string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   OutputWhse:string,
      /**  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  */  
   OutputBinNum:string,
      /**  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  */  
   BackflushWhse:string,
      /**  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  */  
   BackflushBinNum:string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   InputWhse:string,
      /**  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  */  
   InputBinNum:string,
      /**  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  */  
   ResourceType:string,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  Indicates the production quantities produced by this Resource will be tracked.  */  
   TrackProdQty:boolean,
      /**  Links this Resource to a Part, which must be valid in the Part table.  */  
   LinkedPart:string,
      /**  Asset number of the Resource.  Links the Resource to a Fixed Asset.  */  
   AssetNum:string,
      /**  The burden rate for production.  */  
   ProdBurRate:number,
      /**  The labor rate for production.  */  
   ProdLabRate:number,
      /**  Default burden rate for Setup time.  */  
   SetupBurRate:number,
      /**  Default labor rate for setup time.  */  
   SetupLabRate:number,
      /**   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdBurRate:number,
      /**   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdLabRate:number,
      /**   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupBurRate:number,
      /**   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupLabRate:number,
      /**  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  */  
   QBurdenType:string,
      /**  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   GetDefaultBurdenFromGroup:boolean,
      /**  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  */  
   VendorNum:number,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   BurdenType:string,
      /**  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  */  
   CalendarID:string,
      /**  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  */  
   MoveHours:number,
      /**  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  */  
   QueHours:number,
      /**  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  */  
   GetDefaultMQFromGroup:boolean,
      /**  Indicates that the Resource is visible in Overload Informer.  */  
   InformOverload:boolean,
      /**  The minimum overload threshold before a day shows up in the Overload Informer.  */  
   MinOverloadPerc:number,
      /**   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  */  
   OpCode:string,
      /**   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  */  
   OpStdID:string,
      /**  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   GetDefaultLaborFromGroup:boolean,
      /**  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  */  
   FiniteHorizon:number,
      /**  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  */  
   AutoMove:boolean,
      /**  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  */  
   SplitOperations:boolean,
      /**  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  */  
   DailyProdQty:number,
      /**  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  */  
   BillLaborRate:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  */  
   GetDefaultWhseFromGroup:boolean,
      /**  Location  */  
   Location:boolean,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  */  
   EquipID:string,
      /**  URL  */  
   URL:string,
      /**  JDFDevice  */  
   JDFDevice:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  NumCavs  */  
   NumCavs:number,
      /**  RunnerWt  */  
   RunnerWt:number,
      /**  SetupTime  */  
   SetupTime:number,
      /**  TearDownTime  */  
   TearDownTime:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  Brand  */  
   Brand:string,
      /**  LocID  */  
   LocID:string,
      /**  PmMapNo  */  
   PmMapNo:number,
      /**  SetupURL  */  
   SetupURL:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MobileResource  */  
   MobileResource:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  MESQueue  */  
   MESQueue:boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
      /**  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  */  
   ECPCEnabled:boolean,
      /**  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  */  
   EquipCreate:boolean,
      /**  Plant from Resource Group  */  
   Plant:string,
   ReadOnlyFields:string,
   BitFlag:number,
   LinkedPartTrackLots:boolean,
   LinkedPartPartDescription:string,
   LinkedPartIUM:string,
   LinkedPartTrackSerialNum:boolean,
   LinkedPartTrackDimension:boolean,
   LinkedPartSellingFactor:number,
   LinkedPartSalesUM:string,
   LinkedPartPricePerCode:string,
   OpCodeOpDesc:string,
   OpStdDescription:string,
   ProdCalDescription:string,
   ResourceTypeDescription:string,
   ResourceTypeExternalMESType:string,
   WhseBackflushWhseDescDescription:string,
   WhseInputWhseDescDescription:string,
   WhseOutputWhseDescDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceTableset{
   Resource:Erp_Tablesets_ResourceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtResourceTableset{
   Resource:Erp_Tablesets_ResourceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param resourceID
   */  
export interface GetByID_input{
   resourceID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ResourceTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ResourceTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ResourceTableset[],
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
   returnObj:Erp_Tablesets_ResourceListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewResource_input{
   ds:Erp_Tablesets_ResourceTableset[],
}

export interface GetNewResource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceTableset[],
}
}

   /** Required : 
      @param whereClauseResource
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseResource:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ResourceTableset[],
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
   ds:Erp_Tablesets_UpdExtResourceTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtResourceTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ResourceTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ResourceTableset[],
}
}

