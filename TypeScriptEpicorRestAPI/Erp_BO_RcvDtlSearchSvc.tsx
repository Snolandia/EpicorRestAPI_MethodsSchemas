import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.RcvDtlSearchSvc
// Description: bo/RcvDtlSearch/RcvDtlSearch.p
           RcvDtl Search Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/$metadata", {
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
   Description: Get RcvDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlRow
   */  
export function get_RcvDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvDtlSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches", {
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
   Summary: Calls GetByID to retrieve the RcvDtlSearch item
   Description: Calls GetByID to retrieve the RcvDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   */  
export function get_RcvDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RcvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RcvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RcvDtlSearch for the service
   Description: Calls UpdateExt to update RcvDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RcvDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete RcvDtlSearch item
   Description: Call UpdateExt to delete RcvDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RcvDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlListRow)
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
export function get_GetRows(whereClauseRcvDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRcvDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRcvDtl=" + whereClauseRcvDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, purPoint:string, packSlip:string, packLine:string, epicorHeaders?:Headers){
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
   if(typeof packSlip!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packSlip=" + packSlip
   }
   if(typeof packLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packLine=" + packLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewRcvDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRcvDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/GetNewRcvDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RcvDtlRow[],
}

export interface Erp_Tablesets_RcvDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   "Invoiced":boolean,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   "InvoiceNum":string,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   "InvoiceLine":number,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   "PartNum":string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   "BinNum":string,
      /**  Receipt quantity in our unit of measure.  */  
   "OurQty":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "OurUnitCost":number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   "JobNum":string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   "JobSeq":number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "VendorQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   "VendorUnitCost":number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   "ReceiptType":string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   "ReceivedTo":string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "ReceivedComplete":boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "IssuedComplete":boolean,
      /**  Vendor's selling Unit of Measure.  */  
   "PUM":string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   "VenPartNum":string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   "CostPerCode":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Number of labels  */  
   "NumLabels":number,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   "InspectionReq":boolean,
      /**   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   "InspectionPending":boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  Date when item was inspected.  */  
   "InspectedDate":string,
      /**   Time of day when inspection transaction was recorded.
(seconds since midnight format)  */  
   "InspectedTime":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  */  
   "ReceiptDate":string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   "ReasonCode":string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   "TotCostVariance":number,
      /**  Weight  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   "NonConformnce":boolean,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   "OurMtlBurUnitCost":number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   "GlbPurPoint":string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackSlip":string,
      /**  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackLine":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocUnitCost":number,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCost":number,
      /**  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderNum":number,
      /**  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderLine":number,
      /**  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderRelNum":number,
      /**  Country Number of the Origin Country (defaults from Part Country of Origin).  */  
   "OrigCountryNum":number,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  Duty Amount portion of the landed cost for this receipt line.  */  
   "LCDutyAmt":number,
      /**  Indirect Cost portion of the landed cost for this receipt line.  */  
   "LCIndCost":number,
      /**  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "POTransValue":number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   "ExtTransValue":number,
      /**  Flag to indicate that the receipt line has been received.  */  
   "Received":boolean,
      /**  Harmonized System (HS) goods classification code.  */  
   "CommodityCode":string,
      /**  Identifier of associated PO ('Std', 'CMI', 'SMI')  */  
   "POType":string,
      /**  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  */  
   "AutoReceipt":boolean,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   "VolumeUOM":string,
      /**  The date the shipment detail arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCSpecLineDutyAmt":number,
      /**  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCUpliftIndCost":number,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCAmt":number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   "LCMtlBurUnitCost":number,
      /**  PO currency value of this field  */  
   "DocVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1VendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2VendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3VendorUnitCost":number,
      /**  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  */  
   "NotCompliant":boolean,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  */  
   "MangCustNum":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  */  
   "LegalNumber":string,
      /**  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  */  
   "ICPackNum":number,
      /**  Shipment Received  */  
   "ShipRcv":string,
      /**  Stores the number of the import document.  Can be different from value on header.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  Can be different from value on header.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  Can be different from Header value.  */  
   "ImportedFromDesc":string,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  */  
   "GrossWeightUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SearchPONum":number,
      /**  OurQty not divided by dimension conversion factor for entry  */  
   "InputOurQty":number,
      /**  Indicates whether to Enable the Serial Number button  */  
   "EnableSN":boolean,
      /**  Indicates whether the IUM or DUM field should be displayed/enabled  */  
   "DisplayUMField":string,
   "EnableLot":boolean,
   "JobRequiredQty":number,
   "JobIUM":string,
   "UsePurchaseCode":boolean,
   "EnableBin":boolean,
   "EnableWhse":boolean,
      /**  MtlSeq used in PrintTag option  */  
   "TagMtlSeq":number,
      /**  Operation Sequence used in PrintTag  */  
   "TagOprSeq":number,
      /**  Flag used to switch other Received To's to Pur-Ins  */  
   "InspectionFlag":boolean,
      /**  PO Line Due Date  */  
   "PODueDate":string,
   "VenRemQty":number,
      /**  Our Remaining Quantity  */  
   "OurRemQty":number,
   "POPUM":string,
   "POIUM":string,
   "POFactor":number,
   "JobPartNum":string,
   "POHold":boolean,
   "OrderQty":number,
      /**  PORel Received Qty for MassReceipts  */  
   "ReceivedQty":number,
      /**  Interger value of CostPerCode  */  
   "CostPerFactor":number,
      /**  Link to the IMRcvDtl table  */  
   "IntQueID":number,
      /**  Indicates whether to enable/disable the dimension fields  */  
   "EnableDim":boolean,
   "POComment":string,
      /**  Indicates if created through Mass Receipts  */  
   "MassReceipt":boolean,
   "AsmPartDescription":string,
      /**  Flag to set disable/enable the InspectionReq field.  */  
   "DisableInspection":boolean,
      /**  The Plant to which the warehouse belongs to  */  
   "Plant":string,
      /**  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  */  
   "SetToLocation":boolean,
   "OpenRelease":boolean,
      /**  PORel.DueDate  */  
   "DueDate":string,
   "OnTime":string,
      /**  Container Detail Landed Cost Amount  */  
   "ContainerLCAmt":number,
   "POFactorDirection":string,
      /**  This is the extended cost of the container detail item this RcvDtl entry is tied to.  */  
   "ContainerExtCost":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "ThisTranQty":number,
   "ThisTranUOM":string,
   "SNStusChanged":boolean,
      /**  DropShipment  */  
   "DropShipment":boolean,
   "RcvdSMIQty":number,
   "RemainingSMIQty":number,
   "ContractOrder":boolean,
   "SMIComplete":boolean,
      /**  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  */  
   "AllowUpdSuppPrice":boolean,
      /**  Flag to indicate if landed cost info can be updated.  */  
   "AllowLCUpdate":boolean,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   "EnableTransValue":boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   "EnableUplift":boolean,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   "ManualLC":boolean,
      /**  Extended receipt detail cost.  */  
   "ExtCost":number,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
   "VendorCurrSymbol":string,
   "Selected":boolean,
   "MangCustID":string,
   "MangCustName":string,
   "LegalNumberMessage":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
      /**  Full description of the Commodity Code.  */  
   "CommodityDescription":string,
      /**  Country name  */  
   "CountryNumDescription":string,
      /**  Description for the dimension code.  */  
   "DimCodeDimCodeDescription":string,
      /**  Inspector's Full Name.  */  
   "InspectorIDName":string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "InvoiceNumDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
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
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  defaults from the company file.  */  
   "PONumShipName":string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "PONumShipToConName":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "PORelNumRefCodeDesc":string,
      /**  Description of the purchase type. Appears in drop-down lists for selection.  */  
   "PurchCodePurchDesc":string,
      /**  Third address line  */  
   "PurPointAddress3":string,
      /**  Purchase Point Name...can't be blank.  */  
   "PurPointName":string,
      /**  Postal Code or Zip code portion of the address  */  
   "PurPointZip":string,
      /**  First address line  */  
   "PurPointAddress1":string,
      /**  City portion of the address  */  
   "PurPointCity":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PurPointPrimPCon":number,
      /**  Second address line  */  
   "PurPointAddress2":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "PurPointCountry":string,
      /**  State portion of the address  */  
   "PurPointState":string,
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
      /**  Description.  */  
   "WareHouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RcvDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   "Invoiced":boolean,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   "InvoiceNum":string,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   "InvoiceLine":number,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   "PartNum":string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   "BinNum":string,
      /**  Receipt quantity in our unit of measure.  */  
   "OurQty":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "OurUnitCost":number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   "JobNum":string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   "AssemblySeq":number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   "JobSeq":number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   "PONum":number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being received.  */  
   "PORelNum":number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   "PartDescription":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   "RevisionNum":string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "VendorQty":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   "VendorUnitCost":number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   "ReceiptType":string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   "ReceivedTo":string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "ReceivedComplete":boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   "IssuedComplete":boolean,
      /**  Vendor's selling Unit of Measure.  */  
   "PUM":string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   "VenPartNum":string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   "CostPerCode":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Number of labels  */  
   "NumLabels":number,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   "InspectionReq":boolean,
      /**   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   "InspectionPending":boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   "InspectorID":string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   "InspectedBy":string,
      /**  Date when item was inspected.  */  
   "InspectedDate":string,
      /**   Time of day when inspection transaction was recorded.
(seconds since midnight format)  */  
   "InspectedTime":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  */  
   "ReceiptDate":string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   "ReasonCode":string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   "TotCostVariance":number,
      /**  Weight  */  
   "Weight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   "NonConformnce":boolean,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   "OurMtlBurUnitCost":number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   "GlbPurPoint":string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackSlip":string,
      /**  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbPackLine":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocUnitCost":number,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   "ContainerID":number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   "Volume":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCost":number,
      /**  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderNum":number,
      /**  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderLine":number,
      /**  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   "OrderRelNum":number,
      /**  Country Number of the Origin Country (defaults from Part Country of Origin).  */  
   "OrigCountryNum":number,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   "UpliftPercent":number,
      /**  Duty Amount portion of the landed cost for this receipt line.  */  
   "LCDutyAmt":number,
      /**  Indirect Cost portion of the landed cost for this receipt line.  */  
   "LCIndCost":number,
      /**  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "POTransValue":number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   "ExtTransValue":number,
      /**  Flag to indicate that the receipt line has been received.  */  
   "Received":boolean,
      /**  Harmonized System (HS) goods classification code.  */  
   "CommodityCode":string,
      /**  Identifier of associated PO ('Std', 'CMI', 'SMI')  */  
   "POType":string,
      /**  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  */  
   "AutoReceipt":boolean,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   "VolumeUOM":string,
      /**  The date the shipment detail arrived. Defaults as current system date.  */  
   "ArrivedDate":string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCSpecLineDutyAmt":number,
      /**  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   "AppliedRcptLCAmt":number,
      /**  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCUpliftIndCost":number,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "LCAmt":number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   "AppliedLCVariance":number,
      /**  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   "LCMtlBurUnitCost":number,
      /**  PO currency value of this field  */  
   "DocVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1VendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2VendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3VendorUnitCost":number,
      /**  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  */  
   "NotCompliant":boolean,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  */  
   "MangCustNum":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  */  
   "LegalNumber":string,
      /**  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  */  
   "ICPackNum":number,
      /**  Shipment Received  */  
   "ShipRcv":string,
      /**  Stores the number of the import document.  Can be different from value on header.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  Can be different from value on header.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  Can be different from Header value.  */  
   "ImportedFromDesc":string,
      /**  Gross Weight  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  */  
   "GrossWeightUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   "QtyOption":string,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   "ConvOverride":boolean,
      /**  ContractID  */  
   "ContractID":string,
      /**  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  */  
   "SMITransNum":number,
      /**  PCID  */  
   "PCID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  Delivered  */  
   "Delivered":boolean,
      /**  DeliveredComments  */  
   "DeliveredComments":string,
      /**  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "InOurCost":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocInUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitCost":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   "InVendorUnitCost":number,
      /**  PO currency value of this field  */  
   "DocInVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InVendorUnitCost":number,
      /**  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  */  
   "SupplierUnInvcReceiptQty":number,
      /**  Value that indicates the un-invoiced quantity of the receipt.  */  
   "OurUnInvcReceiptQty":number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  */  
   "TaxRegionCode":string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  Indicates if the Receipt line is Taxable  */  
   "Taxable":boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   "TaxExempt":string,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   "NoTaxRecalc":boolean,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   "InAppliedLCVariance":number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   "InAppliedRcptLCAmt":number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCAmt":number,
      /**  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  */  
   "InLCDutyAmt":number,
      /**  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  */  
   "InLCIndCost":number,
      /**  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   "InLCMtlBurUnitCost":number,
      /**  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCSpecLineDutyAmt":number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   "InLCUpliftIndCost":number,
      /**  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   "InPOTransValue":number,
      /**  ProjProcessed  */  
   "ProjProcessed":boolean,
      /**  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  */  
   "ExtNonRecoverableCost":number,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  AttributeBackoutRequired  */  
   "AttributeBackoutRequired":boolean,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   "AllowLCUpdate":boolean,
   "AsmPartDescription":string,
      /**  Consolidated PO flag.  Used in Consolidated Purchasing.  */  
   "ConsolidatedPO":boolean,
      /**  This is the extended cost of the container detail item this RcvDtl entry is tied to.  */  
   "ContainerExtCost":number,
      /**  Container Detail Landed Cost Amount  */  
   "ContainerLCAmt":number,
   "ContractOrder":boolean,
      /**  Interger value of CostPerCode  */  
   "CostPerFactor":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Flag to set disable/enable the InspectionReq field.  */  
   "DisableInspection":boolean,
      /**  Indicates whether the IUM or DUM field should be displayed/enabled  */  
   "DisplayUMField":string,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocScrUnitCost":number,
      /**  PO currency value of this field  */  
   "DocScrVendorUnitCost":number,
      /**  DropShipment  */  
   "DropShipment":boolean,
      /**  PORel.DueDate  */  
   "DueDate":string,
   "EnableBin":boolean,
      /**  Indicates whether to enable/disable the dimension fields  */  
   "EnableDim":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableInventoryAttributes":boolean,
   "EnableLot":boolean,
      /**  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  */  
   "EnablePCID":boolean,
      /**  Indicates whether to Enable the Serial Number button  */  
   "EnableSN":boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   "EnableTransValue":boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   "EnableUplift":boolean,
   "EnableWhse":boolean,
      /**  Extended receipt detail cost.  */  
   "ExtCost":number,
      /**  This is true when using the Receive To PCID option in HH PO Receipt.  */  
   "HHReceiveToPCID":boolean,
      /**  OurQty not divided by dimension conversion factor for entry.  */  
   "InputOurQty":number,
      /**  Flag used to switch other Received To's to Pur-Ins  */  
   "InspectionFlag":boolean,
      /**  Link to the IMRcvDtl table  */  
   "IntQueID":number,
   "JobIUM":string,
   "JobPartNum":string,
   "JobRequiredQty":number,
   "LegalNumberMessage":string,
   "MangCustID":string,
   "MangCustName":string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   "ManualLC":boolean,
      /**  Indicates if created through Mass Receipts  */  
   "MassReceipt":boolean,
   "OnTime":string,
   "OpenRelease":boolean,
   "OrderQty":number,
      /**  Our Remaining Quantity  */  
   "OurRemQty":number,
      /**  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  */  
   "PCIDOutboundContainer":boolean,
      /**  Package Control Header Status  */  
   "PkgControlStatus":string,
      /**  The Plant to which the warehouse belongs to  */  
   "Plant":string,
   "POComment":string,
      /**  PO Line Due Date  */  
   "PODueDate":string,
   "POFactor":number,
   "POFactorDirection":string,
   "POHold":boolean,
   "POIUM":string,
   "POPUM":string,
      /**  The total quantity that has arrived for this purchase order release.  */  
   "PORelArrivedQty":number,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  */  
   "PORelStatus":string,
   "RcvdSMIQty":number,
      /**  PORel Received Qty for MassReceipts  */  
   "ReceivedQty":number,
   "RemainingSMIQty":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ScrUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ScrVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ScrUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ScrVendorUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ScrUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ScrVendorUnitCost":number,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   "ScrOurUnitCost":number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  */  
   "ScrVendorUnitCost":number,
   "SearchPONum":number,
   "Selected":boolean,
      /**  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  */  
   "SetToLocation":boolean,
      /**  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  */  
   "SkipMaterialQueueCreation":boolean,
   "SMIComplete":boolean,
   "SNStusChanged":boolean,
      /**  MtlSeq used in PrintTag option  */  
   "TagMtlSeq":number,
      /**  Operation Sequence used in PrintTag  */  
   "TagOprSeq":number,
   "ThisTranQty":number,
   "ThisTranUOM":string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   "TotalAmt":number,
      /**  Total dedicated Tax amount.  */  
   "TotDedTaxAmt":number,
      /**  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  */  
   "TotDutiesAmt":number,
      /**  Receipt line amount using vendor unit cost.  */  
   "TotLineAmt":number,
      /**  Total Self Assessed Tax amount  */  
   "TotSATaxAmt":number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   "TotTaxAmt":number,
      /**  Total WithHolding Tax amount  */  
   "TotWHTaxAmt":number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   "TranType":string,
   "UsePurchaseCode":boolean,
   "VendorCurrSymbol":string,
   "VenRemQty":number,
      /**  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  */  
   "AllowUpdSuppPrice":boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   "AttributeQtyMismatch":boolean,
      /**  Indicates if the status of the PCID has changed since the receipt took place.  */  
   "PCIDStatusChanged":boolean,
   "CNDeclarationBill":string,
   "SerialNoAttributeSetID":number,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CommodityDescription":string,
   "CountryNumDescription":string,
   "DimCodeDimCodeDescription":string,
   "InspectorIDName":string,
   "InvoiceNumDescription":string,
   "JobNumPartDescription":string,
   "PackSlipInPrice":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumAttrClassID":string,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "POLinePartNum":string,
   "PONumConfirmed":boolean,
   "PONumApprovalStatus":string,
   "PONumShipToConName":string,
   "PONumShipName":string,
   "PONumApprove":boolean,
   "PurchCodePurchDesc":string,
   "PurPointZip":string,
   "PurPointState":string,
   "PurPointCity":string,
   "PurPointPrimPCon":number,
   "PurPointAddress2":string,
   "PurPointAddress3":string,
   "PurPointAddress1":string,
   "PurPointCountry":string,
   "PurPointName":string,
   "TaxCatIDDescription":string,
   "VendorNumCurrencyCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress1":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "WareHouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface DeleteByID_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_RcvDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   Invoiced:boolean,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   InvoiceNum:string,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   InvoiceLine:number,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   PartNum:string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   WareHouseCode:string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   BinNum:string,
      /**  Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   OurUnitCost:number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   JobNum:string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   JobSeq:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   VendorUnitCost:number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   ReceiptType:string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   ReceivedTo:string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   ReceivedComplete:boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   IssuedComplete:boolean,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   VenPartNum:string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Number of labels  */  
   NumLabels:number,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   InspectionReq:boolean,
      /**   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   InspectionPending:boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  Date when item was inspected.  */  
   InspectedDate:string,
      /**   Time of day when inspection transaction was recorded.
(seconds since midnight format)  */  
   InspectedTime:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  */  
   ReceiptDate:string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   ReasonCode:string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   TotCostVariance:number,
      /**  Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   NonConformnce:boolean,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   OurMtlBurUnitCost:number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   GlbPurPoint:string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   GlbPackSlip:string,
      /**  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  */  
   GlbPackLine:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocUnitCost:number,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCost:number,
      /**  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderNum:number,
      /**  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderLine:number,
      /**  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderRelNum:number,
      /**  Country Number of the Origin Country (defaults from Part Country of Origin).  */  
   OrigCountryNum:number,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  Duty Amount portion of the landed cost for this receipt line.  */  
   LCDutyAmt:number,
      /**  Indirect Cost portion of the landed cost for this receipt line.  */  
   LCIndCost:number,
      /**  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   POTransValue:number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   ExtTransValue:number,
      /**  Flag to indicate that the receipt line has been received.  */  
   Received:boolean,
      /**  Harmonized System (HS) goods classification code.  */  
   CommodityCode:string,
      /**  Identifier of associated PO ('Std', 'CMI', 'SMI')  */  
   POType:string,
      /**  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  */  
   AutoReceipt:boolean,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   VolumeUOM:string,
      /**  The date the shipment detail arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCSpecLineDutyAmt:number,
      /**  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCAmt:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   LCMtlBurUnitCost:number,
      /**  PO currency value of this field  */  
   DocVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1VendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2VendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3VendorUnitCost:number,
      /**  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  */  
   NotCompliant:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  */  
   MangCustNum:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  */  
   LegalNumber:string,
      /**  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  */  
   ICPackNum:number,
      /**  Shipment Received  */  
   ShipRcv:string,
      /**  Stores the number of the import document.  Can be different from value on header.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  Can be different from value on header.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  Can be different from Header value.  */  
   ImportedFromDesc:string,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SearchPONum:number,
      /**  OurQty not divided by dimension conversion factor for entry  */  
   InputOurQty:number,
      /**  Indicates whether to Enable the Serial Number button  */  
   EnableSN:boolean,
      /**  Indicates whether the IUM or DUM field should be displayed/enabled  */  
   DisplayUMField:string,
   EnableLot:boolean,
   JobRequiredQty:number,
   JobIUM:string,
   UsePurchaseCode:boolean,
   EnableBin:boolean,
   EnableWhse:boolean,
      /**  MtlSeq used in PrintTag option  */  
   TagMtlSeq:number,
      /**  Operation Sequence used in PrintTag  */  
   TagOprSeq:number,
      /**  Flag used to switch other Received To's to Pur-Ins  */  
   InspectionFlag:boolean,
      /**  PO Line Due Date  */  
   PODueDate:string,
   VenRemQty:number,
      /**  Our Remaining Quantity  */  
   OurRemQty:number,
   POPUM:string,
   POIUM:string,
   POFactor:number,
   JobPartNum:string,
   POHold:boolean,
   OrderQty:number,
      /**  PORel Received Qty for MassReceipts  */  
   ReceivedQty:number,
      /**  Interger value of CostPerCode  */  
   CostPerFactor:number,
      /**  Link to the IMRcvDtl table  */  
   IntQueID:number,
      /**  Indicates whether to enable/disable the dimension fields  */  
   EnableDim:boolean,
   POComment:string,
      /**  Indicates if created through Mass Receipts  */  
   MassReceipt:boolean,
   AsmPartDescription:string,
      /**  Flag to set disable/enable the InspectionReq field.  */  
   DisableInspection:boolean,
      /**  The Plant to which the warehouse belongs to  */  
   Plant:string,
      /**  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  */  
   SetToLocation:boolean,
   OpenRelease:boolean,
      /**  PORel.DueDate  */  
   DueDate:string,
   OnTime:string,
      /**  Container Detail Landed Cost Amount  */  
   ContainerLCAmt:number,
   POFactorDirection:string,
      /**  This is the extended cost of the container detail item this RcvDtl entry is tied to.  */  
   ContainerExtCost:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   ThisTranQty:number,
   ThisTranUOM:string,
   SNStusChanged:boolean,
      /**  DropShipment  */  
   DropShipment:boolean,
   RcvdSMIQty:number,
   RemainingSMIQty:number,
   ContractOrder:boolean,
   SMIComplete:boolean,
      /**  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  */  
   AllowUpdSuppPrice:boolean,
      /**  Flag to indicate if landed cost info can be updated.  */  
   AllowLCUpdate:boolean,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   EnableTransValue:boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   EnableUplift:boolean,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   ManualLC:boolean,
      /**  Extended receipt detail cost.  */  
   ExtCost:number,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
   VendorCurrSymbol:string,
   Selected:boolean,
   MangCustID:string,
   MangCustName:string,
   LegalNumberMessage:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
      /**  Full description of the Commodity Code.  */  
   CommodityDescription:string,
      /**  Country name  */  
   CountryNumDescription:string,
      /**  Description for the dimension code.  */  
   DimCodeDimCodeDescription:string,
      /**  Inspector's Full Name.  */  
   InspectorIDName:string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   InvoiceNumDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
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
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  defaults from the company file.  */  
   PONumShipName:string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   PONumShipToConName:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   PORelNumRefCodeDesc:string,
      /**  Description of the purchase type. Appears in drop-down lists for selection.  */  
   PurchCodePurchDesc:string,
      /**  Third address line  */  
   PurPointAddress3:string,
      /**  Purchase Point Name...can't be blank.  */  
   PurPointName:string,
      /**  Postal Code or Zip code portion of the address  */  
   PurPointZip:string,
      /**  First address line  */  
   PurPointAddress1:string,
      /**  City portion of the address  */  
   PurPointCity:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PurPointPrimPCon:number,
      /**  Second address line  */  
   PurPointAddress2:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   PurPointCountry:string,
      /**  State portion of the address  */  
   PurPointState:string,
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
      /**  Description.  */  
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvDtlListTableset{
   RcvDtlList:Erp_Tablesets_RcvDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RcvDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  */  
   Invoiced:boolean,
      /**  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  */  
   InvoiceNum:string,
      /**  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  */  
   InvoiceLine:number,
      /**  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  */  
   PartNum:string,
      /**  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  */  
   WareHouseCode:string,
      /**  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  */  
   BinNum:string,
      /**  Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   OurUnitCost:number,
      /**  Job Number that received the item. Only applicable for receipt to Job.  */  
   JobNum:string,
      /**  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  */  
   JobSeq:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order Release # which is being received.  */  
   PORelNum:number,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  */  
   RevisionNum:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   VendorUnitCost:number,
      /**  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  */  
   ReceiptType:string,
      /**  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  */  
   ReceivedTo:string,
      /**   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   ReceivedComplete:boolean,
      /**   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  */  
   IssuedComplete:boolean,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Vendor's Part Number. Defaulted from PODetail.  */  
   VenPartNum:string,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Number of labels  */  
   NumLabels:number,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  */  
   InspectionReq:boolean,
      /**   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  */  
   InspectionPending:boolean,
      /**  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  */  
   InspectorID:string,
      /**  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  */  
   InspectedBy:string,
      /**  Date when item was inspected.  */  
   InspectedDate:string,
      /**   Time of day when inspection transaction was recorded.
(seconds since midnight format)  */  
   InspectedTime:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  */  
   ReceiptDate:string,
      /**  DMRs use Reason type "D".  Only used if failing quantity from inspection.  */  
   ReasonCode:string,
      /**  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  */  
   TotCostVariance:number,
      /**  Weight  */  
   Weight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Indicates if the transaction is a non-conformance type transaction.  */  
   NonConformnce:boolean,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  */  
   OurMtlBurUnitCost:number,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   GlbPurPoint:string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   GlbPackSlip:string,
      /**  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  */  
   GlbPackLine:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocUnitCost:number,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Container volume, frequently specified in cubic sq feet.  */  
   Volume:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCost:number,
      /**  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderNum:number,
      /**  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderLine:number,
      /**  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  */  
   OrderRelNum:number,
      /**  Country Number of the Origin Country (defaults from Part Country of Origin).  */  
   OrigCountryNum:number,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  Duty Amount portion of the landed cost for this receipt line.  */  
   LCDutyAmt:number,
      /**  Indirect Cost portion of the landed cost for this receipt line.  */  
   LCIndCost:number,
      /**  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   POTransValue:number,
      /**  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  */  
   ExtTransValue:number,
      /**  Flag to indicate that the receipt line has been received.  */  
   Received:boolean,
      /**  Harmonized System (HS) goods classification code.  */  
   CommodityCode:string,
      /**  Identifier of associated PO ('Std', 'CMI', 'SMI')  */  
   POType:string,
      /**  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  */  
   AutoReceipt:boolean,
      /**   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  */  
   VolumeUOM:string,
      /**  The date the shipment detail arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCSpecLineDutyAmt:number,
      /**  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   LCAmt:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   LCMtlBurUnitCost:number,
      /**  PO currency value of this field  */  
   DocVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1VendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2VendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3VendorUnitCost:number,
      /**  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  */  
   NotCompliant:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  */  
   MangCustNum:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  */  
   LegalNumber:string,
      /**  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  */  
   ICPackNum:number,
      /**  Shipment Received  */  
   ShipRcv:string,
      /**  Stores the number of the import document.  Can be different from value on header.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  Can be different from value on header.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  Can be different from Header value.  */  
   ImportedFromDesc:string,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   QtyOption:string,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   ConvOverride:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  */  
   SMITransNum:number,
      /**  PCID  */  
   PCID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  Delivered  */  
   Delivered:boolean,
      /**  DeliveredComments  */  
   DeliveredComments:string,
      /**  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   InOurCost:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocInUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitCost:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  */  
   InVendorUnitCost:number,
      /**  PO currency value of this field  */  
   DocInVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1InVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2InVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3InVendorUnitCost:number,
      /**  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  */  
   SupplierUnInvcReceiptQty:number,
      /**  Value that indicates the un-invoiced quantity of the receipt.  */  
   OurUnInvcReceiptQty:number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  */  
   TaxRegionCode:string,
      /**  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  Indicates if the Receipt line is Taxable  */  
   Taxable:boolean,
      /**  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  */  
   TaxExempt:string,
      /**  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  */  
   NoTaxRecalc:boolean,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCAmt:number,
      /**  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  */  
   InLCDutyAmt:number,
      /**  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  */  
   InLCIndCost:number,
      /**  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  */  
   InLCMtlBurUnitCost:number,
      /**  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCSpecLineDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  */  
   InLCUpliftIndCost:number,
      /**  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  */  
   InPOTransValue:number,
      /**  ProjProcessed  */  
   ProjProcessed:boolean,
      /**  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  */  
   ExtNonRecoverableCost:number,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  AttributeBackoutRequired  */  
   AttributeBackoutRequired:boolean,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
      /**  Flag to indicate if landed cost info can be updated.  */  
   AllowLCUpdate:boolean,
   AsmPartDescription:string,
      /**  Consolidated PO flag.  Used in Consolidated Purchasing.  */  
   ConsolidatedPO:boolean,
      /**  This is the extended cost of the container detail item this RcvDtl entry is tied to.  */  
   ContainerExtCost:number,
      /**  Container Detail Landed Cost Amount  */  
   ContainerLCAmt:number,
   ContractOrder:boolean,
      /**  Interger value of CostPerCode  */  
   CostPerFactor:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Flag to set disable/enable the InspectionReq field.  */  
   DisableInspection:boolean,
      /**  Indicates whether the IUM or DUM field should be displayed/enabled  */  
   DisplayUMField:string,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocScrUnitCost:number,
      /**  PO currency value of this field  */  
   DocScrVendorUnitCost:number,
      /**  DropShipment  */  
   DropShipment:boolean,
      /**  PORel.DueDate  */  
   DueDate:string,
   EnableBin:boolean,
      /**  Indicates whether to enable/disable the dimension fields  */  
   EnableDim:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableInventoryAttributes:boolean,
   EnableLot:boolean,
      /**  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  */  
   EnablePCID:boolean,
      /**  Indicates whether to Enable the Serial Number button  */  
   EnableSN:boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
      /**  Flag to indicate if PO Trans Value can be updated.  */  
   EnableTransValue:boolean,
      /**  Flag to indicate if UpliftPercent can be updated.  */  
   EnableUplift:boolean,
   EnableWhse:boolean,
      /**  Extended receipt detail cost.  */  
   ExtCost:number,
      /**  This is true when using the Receive To PCID option in HH PO Receipt.  */  
   HHReceiveToPCID:boolean,
      /**  OurQty not divided by dimension conversion factor for entry.  */  
   InputOurQty:number,
      /**  Flag used to switch other Received To's to Pur-Ins  */  
   InspectionFlag:boolean,
      /**  Link to the IMRcvDtl table  */  
   IntQueID:number,
   JobIUM:string,
   JobPartNum:string,
   JobRequiredQty:number,
   LegalNumberMessage:string,
   MangCustID:string,
   MangCustName:string,
      /**  Flag to indicate if LCIdCost can be manually updated.  */  
   ManualLC:boolean,
      /**  Indicates if created through Mass Receipts  */  
   MassReceipt:boolean,
   OnTime:string,
   OpenRelease:boolean,
   OrderQty:number,
      /**  Our Remaining Quantity  */  
   OurRemQty:number,
      /**  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  */  
   PCIDOutboundContainer:boolean,
      /**  Package Control Header Status  */  
   PkgControlStatus:string,
      /**  The Plant to which the warehouse belongs to  */  
   Plant:string,
   POComment:string,
      /**  PO Line Due Date  */  
   PODueDate:string,
   POFactor:number,
   POFactorDirection:string,
   POHold:boolean,
   POIUM:string,
   POPUM:string,
      /**  The total quantity that has arrived for this purchase order release.  */  
   PORelArrivedQty:number,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  */  
   PORelStatus:string,
   RcvdSMIQty:number,
      /**  PORel Received Qty for MassReceipts  */  
   ReceivedQty:number,
   RemainingSMIQty:number,
      /**  Reporting currency value of this field  */  
   Rpt1ScrUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1ScrVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ScrUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ScrVendorUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ScrUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ScrVendorUnitCost:number,
      /**  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  */  
   ScrOurUnitCost:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  */  
   ScrVendorUnitCost:number,
   SearchPONum:number,
   Selected:boolean,
      /**  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  */  
   SetToLocation:boolean,
      /**  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  */  
   SkipMaterialQueueCreation:boolean,
   SMIComplete:boolean,
   SNStusChanged:boolean,
      /**  MtlSeq used in PrintTag option  */  
   TagMtlSeq:number,
      /**  Operation Sequence used in PrintTag  */  
   TagOprSeq:number,
   ThisTranQty:number,
   ThisTranUOM:string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   TotalAmt:number,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  */  
   TotDutiesAmt:number,
      /**  Receipt line amount using vendor unit cost.  */  
   TotLineAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   TotTaxAmt:number,
      /**  Total WithHolding Tax amount  */  
   TotWHTaxAmt:number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   TranType:string,
   UsePurchaseCode:boolean,
   VendorCurrSymbol:string,
   VenRemQty:number,
      /**  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  */  
   AllowUpdSuppPrice:boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   AttributeQtyMismatch:boolean,
      /**  Indicates if the status of the PCID has changed since the receipt took place.  */  
   PCIDStatusChanged:boolean,
   CNDeclarationBill:string,
   SerialNoAttributeSetID:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CommodityDescription:string,
   CountryNumDescription:string,
   DimCodeDimCodeDescription:string,
   InspectorIDName:string,
   InvoiceNumDescription:string,
   JobNumPartDescription:string,
   PackSlipInPrice:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumAttrClassID:string,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   POLinePartNum:string,
   PONumConfirmed:boolean,
   PONumApprovalStatus:string,
   PONumShipToConName:string,
   PONumShipName:string,
   PONumApprove:boolean,
   PurchCodePurchDesc:string,
   PurPointZip:string,
   PurPointState:string,
   PurPointCity:string,
   PurPointPrimPCon:number,
   PurPointAddress2:string,
   PurPointAddress3:string,
   PurPointAddress1:string,
   PurPointCountry:string,
   PurPointName:string,
   TaxCatIDDescription:string,
   VendorNumCurrencyCode:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress1:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RcvDtlSearchTableset{
   RcvDtl:Erp_Tablesets_RcvDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRcvDtlSearchTableset{
   RcvDtl:Erp_Tablesets_RcvDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
   */  
export interface GetByID_input{
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RcvDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RcvDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RcvDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_RcvDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param purPoint
      @param packSlip
   */  
export interface GetNewRcvDtl_input{
   ds:Erp_Tablesets_RcvDtlSearchTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewRcvDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RcvDtlSearchTableset[],
}
}

   /** Required : 
      @param whereClauseRcvDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRcvDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RcvDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtRcvDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRcvDtlSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RcvDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RcvDtlSearchTableset[],
}
}

