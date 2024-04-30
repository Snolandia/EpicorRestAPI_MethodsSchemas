import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DynAttrClassDtlSearchSvc
// Description: Search class for DynAttrClassDtl
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get DynAttrClassDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlRow
   */  
export function get_DynAttrClassDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynAttrClassDtlSearches(requestBody:Erp_Tablesets_DynAttrClassDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlSearch item
   Description: Calls GetByID to retrieve the DynAttrClassDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   */  
export function get_DynAttrClassDtlSearches_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DynAttrClassDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_DynAttrClassDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynAttrClassDtlSearch for the service
   Description: Calls UpdateExt to update DynAttrClassDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynAttrClassDtlSearches_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, requestBody:Erp_Tablesets_DynAttrClassDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete DynAttrClassDtlSearch item
   Description: Call UpdateExt to delete DynAttrClassDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AttrClassID Desc: AttrClassID   Required: True   Allow empty value : True
      @param AttributeID Desc: AttributeID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynAttrClassDtlSearches_Company_AttrClassID_AttributeID(Company:string, AttrClassID:string, AttributeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DynAttrClassDtlSearches(" + Company + "," + AttrClassID + "," + AttributeID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDynAttrClassDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynAttrClassDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrClassDtl=" + whereClauseDynAttrClassDtl
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(attrClassID:string, attributeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof attrClassID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attrClassID=" + attrClassID
   }
   if(typeof attributeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attributeID=" + attributeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildAttributeDelimitedString
   Description: Builds a list of attributes separated by ~.  Each attribute is made up of the following separated by `:
1. SysRowID of DynAttrClassDtl record
2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
3. The attribute value to filter on
   OperationID: BuildAttributeDelimitedString
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildAttributeDelimitedString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeDelimitedString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAttributeDelimitedString(requestBody:BuildAttributeDelimitedString_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildAttributeDelimitedString_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/BuildAttributeDelimitedString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildAttributeDelimitedString_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildAttributeDelimitedStringDisplayString
   Description: 1. Builds a list of selected attributes and values for display.
2. Builds a list of attributes separated by ~.  Each attribute is made up of the following separated by `:
a. SysRowID of DynAttrClassDtl record
b. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
c. The attribute value to filter on
   OperationID: BuildAttributeDelimitedStringDisplayString
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildAttributeDelimitedStringDisplayString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeDelimitedStringDisplayString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAttributeDelimitedStringDisplayString(requestBody:BuildAttributeDelimitedStringDisplayString_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildAttributeDelimitedStringDisplayString_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/BuildAttributeDelimitedStringDisplayString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildAttributeDelimitedStringDisplayString_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildAttributeWhereClause
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause
   OperationID: BuildAttributeWhereClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildAttributeWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAttributeWhereClause(requestBody:BuildAttributeWhereClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildAttributeWhereClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/BuildAttributeWhereClause", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildAttributeWhereClause_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildAttributeWhereClauseForLotTracker
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause
   OperationID: BuildAttributeWhereClauseForLotTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildAttributeWhereClauseForLotTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAttributeWhereClauseForLotTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAttributeWhereClauseForLotTracker(requestBody:BuildAttributeWhereClauseForLotTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildAttributeWhereClauseForLotTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/BuildAttributeWhereClauseForLotTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BuildAttributeWhereClauseForLotTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMetaFxDynamicWebPanelContent
   Description: Returns a string containing MetaFX json for use in a dynamic panel. This will contains a list of controls for each attribute available
in the selected attribute class
   OperationID: GetMetaFxDynamicWebPanelContent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMetaFxDynamicWebPanelContent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMetaFxDynamicWebPanelContent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMetaFxDynamicWebPanelContent(requestBody:GetMetaFxDynamicWebPanelContent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMetaFxDynamicWebPanelContent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetMetaFxDynamicWebPanelContent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetMetaFxDynamicWebPanelContent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDynAttrClassDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClassDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClassDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClassDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDynAttrClassDtl(requestBody:GetNewDynAttrClassDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDynAttrClassDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetNewDynAttrClassDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDynAttrClassDtl_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassDtlSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DynAttrClassDtlRow,
}

export interface Erp_Tablesets_DynAttrClassDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ID of parent Attribute Class  */  
   "AttrClassID":string,
      /**  Unique ID of attribute for this class  */  
   "AttributeID":string,
      /**  Schema name for the related table.  */  
   "RelatedToSchemaName":string,
      /**  Table name for the related table.  */  
   "RelatedToTableName":string,
      /**  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  */  
   "Active":boolean,
      /**  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  */  
   "Description":string,
      /**  Date type for this attribute field.  */  
   "FieldDataType":string,
      /**  Format for the given date type for this attribute field.  */  
   "FieldFormat":string,
      /**  Defines the field lablel for this attribute.  */  
   "FieldLabel":string,
      /**  The value that determines the increments used when linked to a numeric input.  */  
   "IncrPrec":number,
      /**  Initial character value.  */  
   "InitialCharacter":string,
      /**  Initial date value.  */  
   "InitialDate":string,
      /**  Initial decimal value.  */  
   "InitialDecimal":number,
      /**  Initial integer value.  */  
   "InitialInteger":number,
      /**  Initial logical value.  */  
   "InitialLogical":boolean,
      /**  The user defined maximum acceptable value when linked to a date input.  */  
   "MaxDate":string,
      /**  The user defined maximum acceptable value when linked to a decimal input.  */  
   "MaxDecimal":number,
      /**  The user defined maximum acceptable value when linked to an integer input.  */  
   "MaxInteger":number,
      /**  The user defined minimum acceptable value when linked to a date input.  */  
   "MinDate":string,
      /**  The user defined minimum acceptable value when linked to a decimal input.  */  
   "MinDecimal":number,
      /**  The user defined minimum acceptable value when linked to an integer input.  */  
   "MinInteger":number,
      /**  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  */  
   "WebAttribute":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Further defines the business use of the field, valid values are "Quantity,UOM"  */  
   "BizType":string,
      /**  Attribute ID of related UOM linked to quantity.  */  
   "UOMAttributeID":string,
      /**  Controls the order attributes are displayed and updated.  */  
   "SortSeq":number,
      /**  If attribute is used in planning.  */  
   "UsedInPlanning":boolean,
      /**  Indicated this attribute will be used as a calculated field.  */  
   "IsCalculated":boolean,
      /**  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  */  
   "PlanningBaseUOM":string,
      /**  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  */  
   "PlanningType":string,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevDecimal01":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  The actual transaction value for the attribute set.  */  
   "IsActual":boolean,
      /**  Indicates if this attribute will be visible in attribute entry.  */  
   "IsViewable":boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  */  
   "IsReadOnly":boolean,
      /**  Resuable Attribute linked to this class attribute.  */  
   "MasterDtlLinked":string,
      /**  Indicates if changes made to Reusable Attributes are synch to this class attribute.  */  
   "MasterDtlSync":boolean,
      /**  Indicates a pre-defined System Attribute Class.  */  
   "SystemFlag":boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  */  
   "IncludeListValueCodeInShortDesc":boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  */  
   "IncludeListValueDescriptionInShortDesc":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DynAttrClassDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ID of parent Attribute Class  */  
   "AttrClassID":string,
      /**  Unique ID of attribute for this class  */  
   "AttributeID":string,
      /**  Schema name for the related table.  */  
   "RelatedToSchemaName":string,
      /**  Table name for the related table.  */  
   "RelatedToTableName":string,
      /**  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  */  
   "Active":boolean,
      /**  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  */  
   "Description":string,
      /**  Date type for this attribute field.  */  
   "FieldDataType":string,
      /**  Format for the given date type for this attribute field.  */  
   "FieldFormat":string,
      /**  Defines the field lablel for this attribute.  */  
   "FieldLabel":string,
      /**  The value that determines the increments used when linked to a numeric input.  */  
   "IncrPrec":number,
      /**  Initial character value.  */  
   "InitialCharacter":string,
      /**  Initial date value.  */  
   "InitialDate":string,
      /**  Initial decimal value.  */  
   "InitialDecimal":number,
      /**  Initial integer value.  */  
   "InitialInteger":number,
      /**  Initial logical value.  */  
   "InitialLogical":boolean,
      /**  The user defined maximum acceptable value when linked to a date input.  */  
   "MaxDate":string,
      /**  The user defined maximum acceptable value when linked to a decimal input.  */  
   "MaxDecimal":number,
      /**  The user defined maximum acceptable value when linked to an integer input.  */  
   "MaxInteger":number,
      /**  The user defined minimum acceptable value when linked to a date input.  */  
   "MinDate":string,
      /**  The user defined minimum acceptable value when linked to a decimal input.  */  
   "MinDecimal":number,
      /**  The user defined minimum acceptable value when linked to an integer input.  */  
   "MinInteger":number,
      /**  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  */  
   "WebAttribute":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Further defines the business use of the field, valid values are "Quantity,UOM"  */  
   "BizType":string,
      /**  Attribute ID of related UOM linked to quantity.  */  
   "UOMAttributeID":string,
      /**  Controls the order attributes are displayed and updated.  */  
   "SortSeq":number,
      /**  If attribute is used in planning.  */  
   "UsedInPlanning":boolean,
      /**  Indicated this attribute will be used as a calculated field.  */  
   "IsCalculated":boolean,
      /**  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  */  
   "PlanningBaseUOM":string,
      /**  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  */  
   "PlanningType":string,
      /**  Development use only.  */  
   "DevCharacter01":string,
      /**  Development use only.  */  
   "DevDecimal01":number,
      /**  Development use only.  */  
   "DevBoolean01":boolean,
      /**  The actual transaction value for the attribute set.  */  
   "IsActual":boolean,
      /**  Indicates if this attribute will be visible in attribute entry.  */  
   "IsViewable":boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  */  
   "IsReadOnly":boolean,
      /**  Resuable Attribute linked to this class attribute.  */  
   "MasterDtlLinked":string,
      /**  Indicates if changes made to Reusable Attributes are synch to this class attribute.  */  
   "MasterDtlSync":boolean,
      /**  Indicates a pre-defined System Attribute Class.  */  
   "SystemFlag":boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  */  
   "IncludeListValueCodeInShortDesc":boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  */  
   "IncludeListValueDescriptionInShortDesc":boolean,
      /**  Used for setting Epi Shape to highlight attribute has been used.  */  
   "InUse":boolean,
      /**  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  */  
   "ListValues":string,
      /**  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  */  
   "IsFinalExpression":boolean,
      /**  The UOM used with final expression, used to calculate inventory quantity.  */  
   "FinalExpressionUOM":string,
      /**  List of available Required At codes.  */  
   "RequiredAtAvailableCodes":string,
      /**  List of available Required at descriptions.  */  
   "RequiredAtAvailableDesc":string,
      /**  List of Required At codes selected.  */  
   "RequiredAtSelectedCodes":string,
      /**  List of Required At descriptions selected.  */  
   "RequiredAtSelectedDesc":string,
      /**  Indicates if this calculated field has a Formula Expression already been added or not.  */  
   "IsExpressionDefined":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param attrClassID
      @param dt
   */  
export interface BuildAttributeDelimitedStringDisplayString_input{
   attrClassID:string,
   dt:any,      //schema had no properties on an object.
}

export interface BuildAttributeDelimitedStringDisplayString_output{
parameters : {
      /**  output parameters  */  
   attributeDelimitedList:string,
   attributeDisplayValues:string,
}
}

   /** Required : 
      @param dt
   */  
export interface BuildAttributeDelimitedString_input{
   dt:any,      //schema had no properties on an object.
}

export interface BuildAttributeDelimitedString_output{
   returnObj:string,
}

   /** Required : 
      @param attrClassID
      @param attributeListString
      @param whereClause
   */  
export interface BuildAttributeWhereClauseForLotTracker_input{
      /**  AttrClassID value  */  
   attrClassID:string,
      /**  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  */  
   attributeListString:string,
      /**  The whereClause to append to  */  
   whereClause:string,
}

export interface BuildAttributeWhereClauseForLotTracker_output{
   returnObj:string,
}

   /** Required : 
      @param attrClassID
      @param attributeListString
      @param whereClause
   */  
export interface BuildAttributeWhereClause_input{
      /**  AttrClassID value  */  
   attrClassID:string,
      /**  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  */  
   attributeListString:string,
      /**  The whereClause to append to  */  
   whereClause:string,
}

export interface BuildAttributeWhereClause_output{
   returnObj:string,
}

   /** Required : 
      @param attrClassID
      @param attributeID
   */  
export interface DeleteByID_input{
   attrClassID:string,
   attributeID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DynAttrClassDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  Unique ID of attribute for this class  */  
   AttributeID:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
      /**  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  */  
   Active:boolean,
      /**  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  */  
   Description:string,
      /**  Date type for this attribute field.  */  
   FieldDataType:string,
      /**  Format for the given date type for this attribute field.  */  
   FieldFormat:string,
      /**  Defines the field lablel for this attribute.  */  
   FieldLabel:string,
      /**  The value that determines the increments used when linked to a numeric input.  */  
   IncrPrec:number,
      /**  Initial character value.  */  
   InitialCharacter:string,
      /**  Initial date value.  */  
   InitialDate:string,
      /**  Initial decimal value.  */  
   InitialDecimal:number,
      /**  Initial integer value.  */  
   InitialInteger:number,
      /**  Initial logical value.  */  
   InitialLogical:boolean,
      /**  The user defined maximum acceptable value when linked to a date input.  */  
   MaxDate:string,
      /**  The user defined maximum acceptable value when linked to a decimal input.  */  
   MaxDecimal:number,
      /**  The user defined maximum acceptable value when linked to an integer input.  */  
   MaxInteger:number,
      /**  The user defined minimum acceptable value when linked to a date input.  */  
   MinDate:string,
      /**  The user defined minimum acceptable value when linked to a decimal input.  */  
   MinDecimal:number,
      /**  The user defined minimum acceptable value when linked to an integer input.  */  
   MinInteger:number,
      /**  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  */  
   WebAttribute:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Further defines the business use of the field, valid values are "Quantity,UOM"  */  
   BizType:string,
      /**  Attribute ID of related UOM linked to quantity.  */  
   UOMAttributeID:string,
      /**  Controls the order attributes are displayed and updated.  */  
   SortSeq:number,
      /**  If attribute is used in planning.  */  
   UsedInPlanning:boolean,
      /**  Indicated this attribute will be used as a calculated field.  */  
   IsCalculated:boolean,
      /**  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  */  
   PlanningBaseUOM:string,
      /**  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  */  
   PlanningType:string,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevDecimal01:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  The actual transaction value for the attribute set.  */  
   IsActual:boolean,
      /**  Indicates if this attribute will be visible in attribute entry.  */  
   IsViewable:boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  */  
   IsReadOnly:boolean,
      /**  Resuable Attribute linked to this class attribute.  */  
   MasterDtlLinked:string,
      /**  Indicates if changes made to Reusable Attributes are synch to this class attribute.  */  
   MasterDtlSync:boolean,
      /**  Indicates a pre-defined System Attribute Class.  */  
   SystemFlag:boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  */  
   IncludeListValueCodeInShortDesc:boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  */  
   IncludeListValueDescriptionInShortDesc:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassDtlListTableset{
   DynAttrClassDtlList:Erp_Tablesets_DynAttrClassDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DynAttrClassDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ID of parent Attribute Class  */  
   AttrClassID:string,
      /**  Unique ID of attribute for this class  */  
   AttributeID:string,
      /**  Schema name for the related table.  */  
   RelatedToSchemaName:string,
      /**  Table name for the related table.  */  
   RelatedToTableName:string,
      /**  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  */  
   Active:boolean,
      /**  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  */  
   Description:string,
      /**  Date type for this attribute field.  */  
   FieldDataType:string,
      /**  Format for the given date type for this attribute field.  */  
   FieldFormat:string,
      /**  Defines the field lablel for this attribute.  */  
   FieldLabel:string,
      /**  The value that determines the increments used when linked to a numeric input.  */  
   IncrPrec:number,
      /**  Initial character value.  */  
   InitialCharacter:string,
      /**  Initial date value.  */  
   InitialDate:string,
      /**  Initial decimal value.  */  
   InitialDecimal:number,
      /**  Initial integer value.  */  
   InitialInteger:number,
      /**  Initial logical value.  */  
   InitialLogical:boolean,
      /**  The user defined maximum acceptable value when linked to a date input.  */  
   MaxDate:string,
      /**  The user defined maximum acceptable value when linked to a decimal input.  */  
   MaxDecimal:number,
      /**  The user defined maximum acceptable value when linked to an integer input.  */  
   MaxInteger:number,
      /**  The user defined minimum acceptable value when linked to a date input.  */  
   MinDate:string,
      /**  The user defined minimum acceptable value when linked to a decimal input.  */  
   MinDecimal:number,
      /**  The user defined minimum acceptable value when linked to an integer input.  */  
   MinInteger:number,
      /**  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  */  
   WebAttribute:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Further defines the business use of the field, valid values are "Quantity,UOM"  */  
   BizType:string,
      /**  Attribute ID of related UOM linked to quantity.  */  
   UOMAttributeID:string,
      /**  Controls the order attributes are displayed and updated.  */  
   SortSeq:number,
      /**  If attribute is used in planning.  */  
   UsedInPlanning:boolean,
      /**  Indicated this attribute will be used as a calculated field.  */  
   IsCalculated:boolean,
      /**  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  */  
   PlanningBaseUOM:string,
      /**  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  */  
   PlanningType:string,
      /**  Development use only.  */  
   DevCharacter01:string,
      /**  Development use only.  */  
   DevDecimal01:number,
      /**  Development use only.  */  
   DevBoolean01:boolean,
      /**  The actual transaction value for the attribute set.  */  
   IsActual:boolean,
      /**  Indicates if this attribute will be visible in attribute entry.  */  
   IsViewable:boolean,
      /**  Indicates if this attribute will be read only in attribute entry.  */  
   IsReadOnly:boolean,
      /**  Resuable Attribute linked to this class attribute.  */  
   MasterDtlLinked:string,
      /**  Indicates if changes made to Reusable Attributes are synch to this class attribute.  */  
   MasterDtlSync:boolean,
      /**  Indicates a pre-defined System Attribute Class.  */  
   SystemFlag:boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  */  
   IncludeListValueCodeInShortDesc:boolean,
      /**  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  */  
   IncludeListValueDescriptionInShortDesc:boolean,
      /**  Used for setting Epi Shape to highlight attribute has been used.  */  
   InUse:boolean,
      /**  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  */  
   ListValues:string,
      /**  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  */  
   IsFinalExpression:boolean,
      /**  The UOM used with final expression, used to calculate inventory quantity.  */  
   FinalExpressionUOM:string,
      /**  List of available Required At codes.  */  
   RequiredAtAvailableCodes:string,
      /**  List of available Required at descriptions.  */  
   RequiredAtAvailableDesc:string,
      /**  List of Required At codes selected.  */  
   RequiredAtSelectedCodes:string,
      /**  List of Required At descriptions selected.  */  
   RequiredAtSelectedDesc:string,
      /**  Indicates if this calculated field has a Formula Expression already been added or not.  */  
   IsExpressionDefined:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynAttrClassDtlSearchTableset{
   DynAttrClassDtl:Erp_Tablesets_DynAttrClassDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDynAttrClassDtlSearchTableset{
   DynAttrClassDtl:Erp_Tablesets_DynAttrClassDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param attrClassID
      @param attributeID
   */  
export interface GetByID_input{
   attrClassID:string,
   attributeID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DynAttrClassDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DynAttrClassDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DynAttrClassDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_DynAttrClassDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param attrClassID
   */  
export interface GetMetaFxDynamicWebPanelContent_input{
   attrClassID:string,
}

export interface GetMetaFxDynamicWebPanelContent_output{
parameters : {
      /**  output parameters  */  
   sContent:string,
}
}

   /** Required : 
      @param ds
      @param attrClassID
   */  
export interface GetNewDynAttrClassDtl_input{
   ds:Erp_Tablesets_DynAttrClassDtlSearchTableset[],
   attrClassID:string,
}

export interface GetNewDynAttrClassDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassDtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseDynAttrClassDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDynAttrClassDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DynAttrClassDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtDynAttrClassDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDynAttrClassDtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DynAttrClassDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynAttrClassDtlSearchTableset,
}
}

