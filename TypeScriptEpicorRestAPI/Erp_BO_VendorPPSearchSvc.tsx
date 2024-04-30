import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.VendorPPSearchSvc
// Description: Vendor Purchase Points Search
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/$metadata", {
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
   Description: Get VendorPPSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendorPPSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPRow
   */  
export function get_VendorPPSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendorPPSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.VendorPPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendorPPSearches(requestBody:Erp_Tablesets_VendorPPRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches", {
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
   Summary: Calls GetByID to retrieve the VendorPPSearch item
   Description: Calls GetByID to retrieve the VendorPPSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorPPSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.VendorPPRow
   */  
export function get_VendorPPSearches_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_VendorPPRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
         resolve(data as Erp_Tablesets_VendorPPRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VendorPPSearch for the service
   Description: Calls UpdateExt to update VendorPPSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendorPPSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VendorPPSearches_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, requestBody:Erp_Tablesets_VendorPPRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
   Summary: Call UpdateExt to delete VendorPPSearch item
   Description: Call UpdateExt to delete VendorPPSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendorPPSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VendorPPSearches_Company_VendorNum_PurPoint(Company:string, VendorNum:string, PurPoint:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches(" + Company + "," + VendorNum + "," + PurPoint + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPListRow)
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
export function get_GetRows(whereClauseVendorPP:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseVendorPP!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseVendorPP=" + whereClauseVendorPP
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, purPoint:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof purPoint!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "purPoint=" + purPoint
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListForActiveSuppliers
   Description: Called to retrieve Purchase Points for active vendors
   OperationID: GetListForActiveSuppliers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForActiveSuppliers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForActiveSuppliers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForActiveSuppliers(requestBody:GetListForActiveSuppliers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForActiveSuppliers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetListForActiveSuppliers", {
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
         resolve(data as GetListForActiveSuppliers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VendorPPListGetList
   Description: Called to retrieve GetList with VendorID within the WhereClause.
   OperationID: VendorPPListGetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VendorPPListGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VendorPPListGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VendorPPListGetList(requestBody:VendorPPListGetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VendorPPListGetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPListGetList", {
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
         resolve(data as VendorPPListGetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewVendorPP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendorPP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewVendorPP(requestBody:GetNewVendorPP_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewVendorPP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetNewVendorPP", {
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
         resolve(data as GetNewVendorPP_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendorPPListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow{
   "odatametadata":string,
   "value":Erp_Tablesets_VendorPPRow,
}

export interface Erp_Tablesets_VendorPPListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Purchase Point Name...can't be blank.  */  
   "Name":string,
      /**  First address line  */  
   "Address1":string,
      /**  Second address line  */  
   "Address2":string,
      /**  Third address line  */  
   "Address3":string,
      /**  City portion of the address  */  
   "City":string,
      /**  State portion of the address  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address  */  
   "Zip":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "Country":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PrimPCon":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
      /**  Email address of the vendor purchase point.  */  
   "EMailAddress":string,
      /**  Unique Identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  */  
   "OverrideService":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Indicates if the shipment is international.  */  
   "IntrntlShip":boolean,
      /**  Certificate of Origin flag  */  
   "CertOfOrigin":boolean,
      /**  Commercial Invoice flag.  */  
   "CommercialInvoice":boolean,
      /**  Ship Export Declaration flag  */  
   "ShipExprtDeclartn":boolean,
      /**  Letter of Instruction flag  */  
   "LetterOfInstr":boolean,
      /**  Freight Forwarder ID  */  
   "FFID":string,
      /**  Freight Forwarder Company Name  */  
   "FFCompName":string,
      /**  Freight Forwarder contact person  */  
   "FFContact":string,
      /**  First address line of the Freight Forwarder  */  
   "FFAddress1":string,
      /**  Second address line of the Freight Forwarder  */  
   "FFAddress2":string,
      /**  Third address line of the Freight Forwarder  */  
   "FFAddress3":string,
      /**  Freight Forwarder city portion of address.  */  
   "FFCity":string,
      /**  Freight Forwarder state portion of address.  */  
   "FFState":string,
      /**  Freight Forwarder Zip code portion of the address  */  
   "FFZip":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountry":string,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Phone Number  */  
   "FFPhoneNum":string,
      /**  Freight Forwarder Country Number  */  
   "FFCountryNum":number,
      /**  Legal Name  */  
   "LegalName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "IntegrationFlag":boolean,
   "PrimaryPP":boolean,
      /**  Indicates if ShipTo is a global record  */  
   "GlbFlag":boolean,
   "VendAttrString":string,
      /**  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  */  
   "GlbLink":string,
   "PhoneNum":string,
   "GroupCode":string,
      /**  Country name  */  
   "CountryNumDescription":string,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  Language Name Description  */  
   "LangNameIDDescription":string,
      /**  Long Description of the tax authority code.  */  
   "TACodeTaxAuthorityDescription":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
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
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_VendorPPRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Purchase Point Name...can't be blank.  */  
   "Name":string,
      /**  First address line  */  
   "Address1":string,
      /**  Second address line  */  
   "Address2":string,
      /**  Third address line  */  
   "Address3":string,
      /**  City portion of the address  */  
   "City":string,
      /**  State portion of the address  */  
   "State":string,
      /**  Postal Code or Zip code portion of the address  */  
   "Zip":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "Country":string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PrimPCon":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
      /**  Email address of the vendor purchase point.  */  
   "EMailAddress":string,
      /**  Unique Identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  */  
   "OverrideService":boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Indicates if the shipment is international.  */  
   "IntrntlShip":boolean,
      /**  Certificate of Origin flag  */  
   "CertOfOrigin":boolean,
      /**  Commercial Invoice flag.  */  
   "CommercialInvoice":boolean,
      /**  Ship Export Declaration flag  */  
   "ShipExprtDeclartn":boolean,
      /**  Letter of Instruction flag  */  
   "LetterOfInstr":boolean,
      /**  Freight Forwarder ID  */  
   "FFID":string,
      /**  Freight Forwarder Company Name  */  
   "FFCompName":string,
      /**  Freight Forwarder contact person  */  
   "FFContact":string,
      /**  First address line of the Freight Forwarder  */  
   "FFAddress1":string,
      /**  Second address line of the Freight Forwarder  */  
   "FFAddress2":string,
      /**  Third address line of the Freight Forwarder  */  
   "FFAddress3":string,
      /**  Freight Forwarder city portion of address.  */  
   "FFCity":string,
      /**  Freight Forwarder state portion of address.  */  
   "FFState":string,
      /**  Freight Forwarder Zip code portion of the address  */  
   "FFZip":string,
      /**  Freight Forwarder Country portion of the address  */  
   "FFCountry":string,
      /**  Non Standard Packaging  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling flag  */  
   "AddlHdlgFlag":boolean,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Freight Forwarder Phone Number  */  
   "FFPhoneNum":string,
      /**  Freight Forwarder Country Number  */  
   "FFCountryNum":number,
      /**  Legal Name  */  
   "LegalName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  INExciseRegNumber  */  
   "INExciseRegNumber":string,
      /**  INExciseDivision  */  
   "INExciseDivision":string,
      /**  INExciseRange  */  
   "INExciseRange":string,
      /**  INCommissionarate  */  
   "INCommissionarate":string,
      /**  INVATNumber  */  
   "INVATNumber":string,
      /**  INServiceTaxRegNum  */  
   "INServiceTaxRegNum":string,
      /**  INTaxRegionCode  */  
   "INTaxRegionCode":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  Municipio Code  */  
   "MXMunicipio":string,
   "GroupCode":string,
   "IntegrationFlag":boolean,
   "PhoneNum":string,
   "PrimaryPP":boolean,
   "VendAttrString":string,
      /**  Indicates if ShipTo is a global record  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  */  
   "GlbLink":string,
      /**  Sales Tax ID  */  
   "SalesTaxID":string,
      /**  Service Tax ID  */  
   "ServiceTaxID":string,
   "LangNameIDDescription":string,
   "BitFlag":number,
   "CountryNumDescription":string,
   "DeliveryTypeDescription":string,
   "INTaxRegionCodeDescription":string,
   "TACodeTaxAuthorityDescription":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumName":string,
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
      @param vendorNum
      @param purPoint
   */  
export interface DeleteByID_input{
   vendorNum:number,
   purPoint:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtVendorPPSearchTableset{
   VendorPP:Erp_Tablesets_VendorPPRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendorPPListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Purchase Point Name...can't be blank.  */  
   Name:string,
      /**  First address line  */  
   Address1:string,
      /**  Second address line  */  
   Address2:string,
      /**  Third address line  */  
   Address3:string,
      /**  City portion of the address  */  
   City:string,
      /**  State portion of the address  */  
   State:string,
      /**  Postal Code or Zip code portion of the address  */  
   Zip:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   Country:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PrimPCon:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Email address of the vendor purchase point.  */  
   EMailAddress:string,
      /**  Unique Identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  */  
   OverrideService:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Indicates if the shipment is international.  */  
   IntrntlShip:boolean,
      /**  Certificate of Origin flag  */  
   CertOfOrigin:boolean,
      /**  Commercial Invoice flag.  */  
   CommercialInvoice:boolean,
      /**  Ship Export Declaration flag  */  
   ShipExprtDeclartn:boolean,
      /**  Letter of Instruction flag  */  
   LetterOfInstr:boolean,
      /**  Freight Forwarder ID  */  
   FFID:string,
      /**  Freight Forwarder Company Name  */  
   FFCompName:string,
      /**  Freight Forwarder contact person  */  
   FFContact:string,
      /**  First address line of the Freight Forwarder  */  
   FFAddress1:string,
      /**  Second address line of the Freight Forwarder  */  
   FFAddress2:string,
      /**  Third address line of the Freight Forwarder  */  
   FFAddress3:string,
      /**  Freight Forwarder city portion of address.  */  
   FFCity:string,
      /**  Freight Forwarder state portion of address.  */  
   FFState:string,
      /**  Freight Forwarder Zip code portion of the address  */  
   FFZip:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountry:string,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Phone Number  */  
   FFPhoneNum:string,
      /**  Freight Forwarder Country Number  */  
   FFCountryNum:number,
      /**  Legal Name  */  
   LegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   IntegrationFlag:boolean,
   PrimaryPP:boolean,
      /**  Indicates if ShipTo is a global record  */  
   GlbFlag:boolean,
   VendAttrString:string,
      /**  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  */  
   GlbLink:string,
   PhoneNum:string,
   GroupCode:string,
      /**  Country name  */  
   CountryNumDescription:string,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  Language Name Description  */  
   LangNameIDDescription:string,
      /**  Long Description of the tax authority code.  */  
   TACodeTaxAuthorityDescription:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
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
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendorPPListTableset{
   VendorPPList:Erp_Tablesets_VendorPPListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VendorPPRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Purchase Point Name...can't be blank.  */  
   Name:string,
      /**  First address line  */  
   Address1:string,
      /**  Second address line  */  
   Address2:string,
      /**  Third address line  */  
   Address3:string,
      /**  City portion of the address  */  
   City:string,
      /**  State portion of the address  */  
   State:string,
      /**  Postal Code or Zip code portion of the address  */  
   Zip:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   Country:string,
      /**  The internal key used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PrimPCon:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Email address of the vendor purchase point.  */  
   EMailAddress:string,
      /**  Unique Identifier from an external G/L interface  */  
   ExternalId:string,
      /**  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  */  
   OverrideService:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Indicates if the shipment is international.  */  
   IntrntlShip:boolean,
      /**  Certificate of Origin flag  */  
   CertOfOrigin:boolean,
      /**  Commercial Invoice flag.  */  
   CommercialInvoice:boolean,
      /**  Ship Export Declaration flag  */  
   ShipExprtDeclartn:boolean,
      /**  Letter of Instruction flag  */  
   LetterOfInstr:boolean,
      /**  Freight Forwarder ID  */  
   FFID:string,
      /**  Freight Forwarder Company Name  */  
   FFCompName:string,
      /**  Freight Forwarder contact person  */  
   FFContact:string,
      /**  First address line of the Freight Forwarder  */  
   FFAddress1:string,
      /**  Second address line of the Freight Forwarder  */  
   FFAddress2:string,
      /**  Third address line of the Freight Forwarder  */  
   FFAddress3:string,
      /**  Freight Forwarder city portion of address.  */  
   FFCity:string,
      /**  Freight Forwarder state portion of address.  */  
   FFState:string,
      /**  Freight Forwarder Zip code portion of the address  */  
   FFZip:string,
      /**  Freight Forwarder Country portion of the address  */  
   FFCountry:string,
      /**  Non Standard Packaging  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling flag  */  
   AddlHdlgFlag:boolean,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Freight Forwarder Phone Number  */  
   FFPhoneNum:string,
      /**  Freight Forwarder Country Number  */  
   FFCountryNum:number,
      /**  Legal Name  */  
   LegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  INExciseRegNumber  */  
   INExciseRegNumber:string,
      /**  INExciseDivision  */  
   INExciseDivision:string,
      /**  INExciseRange  */  
   INExciseRange:string,
      /**  INCommissionarate  */  
   INCommissionarate:string,
      /**  INVATNumber  */  
   INVATNumber:string,
      /**  INServiceTaxRegNum  */  
   INServiceTaxRegNum:string,
      /**  INTaxRegionCode  */  
   INTaxRegionCode:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  Municipio Code  */  
   MXMunicipio:string,
   GroupCode:string,
   IntegrationFlag:boolean,
   PhoneNum:string,
   PrimaryPP:boolean,
   VendAttrString:string,
      /**  Indicates if ShipTo is a global record  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  */  
   GlbLink:string,
      /**  Sales Tax ID  */  
   SalesTaxID:string,
      /**  Service Tax ID  */  
   ServiceTaxID:string,
   LangNameIDDescription:string,
   BitFlag:number,
   CountryNumDescription:string,
   DeliveryTypeDescription:string,
   INTaxRegionCodeDescription:string,
   TACodeTaxAuthorityDescription:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VendorPPSearchTableset{
   VendorPP:Erp_Tablesets_VendorPPRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param purPoint
   */  
export interface GetByID_input{
   vendorNum:number,
   purPoint:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VendorPPSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VendorPPSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VendorPPSearchTableset[],
}

   /** Required : 
      @param whereClauseVendorPP
      @param pageSize
      @param absolutePage
   */  
export interface GetListForActiveSuppliers_input{
      /**  Whereclause for VendorPP table.  */  
   whereClauseVendorPP:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListForActiveSuppliers_output{
   returnObj:Erp_Tablesets_VendorPPListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
   returnObj:Erp_Tablesets_VendorPPListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewVendorPP_input{
   ds:Erp_Tablesets_VendorPPSearchTableset[],
   vendorNum:number,
}

export interface GetNewVendorPP_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorPPSearchTableset,
}
}

   /** Required : 
      @param whereClauseVendorPP
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseVendorPP:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VendorPPSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtVendorPPSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVendorPPSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VendorPPSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VendorPPSearchTableset,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface VendorPPListGetList_input{
      /**  Whereclause for VendorPP table.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface VendorPPListGetList_output{
   returnObj:Erp_Tablesets_VendorPPListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

