import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DropShipDtlSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/$metadata", {
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
   Description: Get DropShipDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlRow
   */  
export function get_DropShipDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipDtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DropShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DropShipDtlSearches(requestBody:Erp_Tablesets_DropShipDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches", {
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
   Summary: Calls GetByID to retrieve the DropShipDtlSearch item
   Description: Calls GetByID to retrieve the DropShipDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DropShipDtlRow
   */  
export function get_DropShipDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DropShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
         resolve(data as Erp_Tablesets_DropShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DropShipDtlSearch for the service
   Description: Calls UpdateExt to update DropShipDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DropShipDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, requestBody:Erp_Tablesets_DropShipDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete DropShipDtlSearch item
   Description: Call UpdateExt to delete DropShipDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param PackSlip Desc: PackSlip   Required: True   Allow empty value : True
      @param PackLine Desc: PackLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DropShipDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company:string, VendorNum:string, PurPoint:string, PackSlip:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlListRow)
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
export function get_GetRows(whereClauseDropShipDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDropShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDropShipDtl=" + whereClauseDropShipDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewDropShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDropShipDtl(requestBody:GetNewDropShipDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDropShipDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/GetNewDropShipDtl", {
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
         resolve(data as GetNewDropShipDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DropShipDtlRow,
}

export interface Erp_Tablesets_DropShipDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for the drop shipment.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  */  
   "PackLine":number,
      /**  Purchase order being drop shipped.  */  
   "PONum":number,
      /**  The line number of the purchase order being drop shipped.  */  
   "POLine":number,
      /**  The release number of the purchase order being drop shipped.  */  
   "PORelNum":number,
      /**  Part Num defaulted from the PO release.  */  
   "PartNum":string,
      /**  Part revision number.  */  
   "RevisionNum":string,
      /**  Supplier's part num. Defaulted from the PO release.  */  
   "VenPartNum":string,
      /**  Defaulted from the PO release.  */  
   "OrderNum":number,
      /**  Defaulted from the PO release.  */  
   "OrderLine":number,
      /**  Defaulted from the PO release.  */  
   "OrderRelNum":number,
      /**  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  */  
   "XPartNum":string,
      /**  Field that contains the customer's revision.  */  
   "XRevisionNum":string,
      /**  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  */  
   "OurQty":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  These comments will be copied into the Invoice detail.  */  
   "InvoiceComment":string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   "HeaderShipComment":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  */  
   "Complete":boolean,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
      /**  Defaults from PODetail LineDesc.  */  
   "LineDesc":string,
      /**  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  */  
   "OurUnitCost":number,
      /**  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  */  
   "DocUnitCost":number,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "VendorQty":number,
      /**  Vendor's selling Unit of Measure.  */  
   "PUM":string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  */  
   "VendorUnitCost":number,
      /**  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  */  
   "ReceiptDate":string,
      /**  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  */  
   "APInvoiced":boolean,
      /**  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  */  
   "ARInvoiced":boolean,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "APInvoiceNum":string,
      /**  Invoice Number Line from corresponding APInvDtl record.  */  
   "APInvoiceLine":number,
      /**  Invoice Number from corresponding InvcHead record.  */  
   "ARInvoiceNum":number,
      /**  Invoice Number Line from corresponding InvcDtl record.  */  
   "ARInvoiceLine":number,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   "CostPerCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Identifies a drop shipment line that is complete and ready to be invoiced.  */  
   "ReceivedShipped":boolean,
      /**  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "LaborExpiration":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "LastExpiration":string,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MaterialExpiration":string,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   "MaterialMod":string,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MiscExpiration":string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   "MiscMod":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Warranty comments.  */  
   "WarrantyComment":string,
      /**  Duplicated from DropShipHead.CustNum.  */  
   "CustNum":number,
      /**  Duplicated from DropShipHead.ShipTotNum.  */  
   "ShipToNum":string,
      /**  Duplicated from DropShipHead.ShipToCustNum  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RequestedQty":number,
   "ShippedToDateQty":number,
   "ThisShipmentQty":number,
   "RemainingQty":number,
   "RequestedQtyUOM":string,
   "ShippedToDateQtyUOM":string,
   "ThisShipmentQtyUOM":string,
   "RemainingQtyUOM":string,
   "CurrencyCode":string,
   "POComment":string,
      /**  Interger value of CostPerCode  */  
   "CostPerFactor":number,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
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
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Second address line  */  
   "PurPointAddress2":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "PurPointCountry":string,
      /**  State portion of the address  */  
   "PurPointState":string,
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
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustNumCustID":string,
      /**  The full name of the customer.  */  
   "ShipToCustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustNumBTName":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
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
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DropShipDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for the drop shipment.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  */  
   "PackLine":number,
      /**  Purchase order being drop shipped.  */  
   "PONum":number,
      /**  The line number of the purchase order being drop shipped.  */  
   "POLine":number,
      /**  The release number of the purchase order being drop shipped.  */  
   "PORelNum":number,
      /**  Part Num defaulted from the PO release.  */  
   "PartNum":string,
      /**  Part revision number.  */  
   "RevisionNum":string,
      /**  Supplier's part num. Defaulted from the PO release.  */  
   "VenPartNum":string,
      /**  Defaulted from the PO release.  */  
   "OrderNum":number,
      /**  Defaulted from the PO release.  */  
   "OrderLine":number,
      /**  Defaulted from the PO release.  */  
   "OrderRelNum":number,
      /**  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  */  
   "XPartNum":string,
      /**  Field that contains the customer's revision.  */  
   "XRevisionNum":string,
      /**  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  */  
   "OurQty":number,
      /**  Unit of Measure.  */  
   "IUM":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  These comments will be copied into the Invoice detail.  */  
   "InvoiceComment":string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   "HeaderShipComment":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  */  
   "Complete":boolean,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
      /**  Defaults from PODetail LineDesc.  */  
   "LineDesc":string,
      /**  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  */  
   "OurUnitCost":number,
      /**  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  */  
   "DocUnitCost":number,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   "VendorQty":number,
      /**  Vendor's selling Unit of Measure.  */  
   "PUM":string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  */  
   "VendorUnitCost":number,
      /**  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  */  
   "ReceiptDate":string,
      /**  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  */  
   "APInvoiced":boolean,
      /**  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  */  
   "ARInvoiced":boolean,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "APInvoiceNum":string,
      /**  Invoice Number Line from corresponding APInvDtl record.  */  
   "APInvoiceLine":number,
      /**  Invoice Number from corresponding InvcHead record.  */  
   "ARInvoiceNum":number,
      /**  Invoice Number Line from corresponding InvcDtl record.  */  
   "ARInvoiceLine":number,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   "CostPerCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   "TranReference":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Identifies a drop shipment line that is complete and ready to be invoiced.  */  
   "ReceivedShipped":boolean,
      /**  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "LaborExpiration":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "LastExpiration":string,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MaterialExpiration":string,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   "MaterialMod":string,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MiscExpiration":string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   "MiscMod":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Warranty comments.  */  
   "WarrantyComment":string,
      /**  Duplicated from DropShipHead.CustNum.  */  
   "CustNum":number,
      /**  Duplicated from DropShipHead.ShipTotNum.  */  
   "ShipToNum":string,
      /**  Duplicated from DropShipHead.ShipToCustNum  */  
   "ShipToCustNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ProjProcessed  */  
   "ProjProcessed":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Estimated Value  */  
   "MXEstValue":number,
      /**  Estimated Value Currency  */  
   "MXEstValueCurrencyCode":string,
      /**  Total Net Weight in kilograms  */  
   "MXTotalNetWeightKGM":number,
      /**  Hazardous Shipment  */  
   "MXHazardousShipment":boolean,
      /**  Hazardous Type  */  
   "MXHazardousType":string,
      /**  Package Type  */  
   "MXPackageType":string,
   "CurrencyCode":string,
   "POComment":string,
   "RemainingQty":number,
   "RemainingQtyUOM":string,
   "RequestedQty":number,
   "RequestedQtyUOM":string,
   "ShippedToDateQty":number,
   "ShippedToDateQtyUOM":string,
   "ThisShipmentQty":number,
   "ThisShipmentQtyUOM":string,
   "VendorCurrencyCode":string,
      /**  Interger value of CostPerCode  */  
   "CostPerFactor":number,
      /**  The formatted bill to address  */  
   "BillToAddrFormatted":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "AttributeSetIDDescription":string,
   "AttributeSetIDShortDescription":string,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PurPointCity":string,
   "PurPointCountry":string,
   "PurPointAddress1":string,
   "PurPointZip":string,
   "PurPointAddress3":string,
   "PurPointState":string,
   "PurPointName":string,
   "PurPointAddress2":string,
   "PurPointPrimPCon":number,
   "ShipToCustNumName":string,
   "ShipToCustNumCustID":string,
   "ShipToCustNumBTName":string,
   "ShipToNumInactive":boolean,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "VendorNumState":string,
   "VendorNumName":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress2":string,
   "VendorNumVendorID":string,
   "VendorNumCountry":string,
   "VendorNumAddress3":string,
   "VendorNumCity":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
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

export interface Erp_Tablesets_DropShipDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for the drop shipment.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  */  
   PackLine:number,
      /**  Purchase order being drop shipped.  */  
   PONum:number,
      /**  The line number of the purchase order being drop shipped.  */  
   POLine:number,
      /**  The release number of the purchase order being drop shipped.  */  
   PORelNum:number,
      /**  Part Num defaulted from the PO release.  */  
   PartNum:string,
      /**  Part revision number.  */  
   RevisionNum:string,
      /**  Supplier's part num. Defaulted from the PO release.  */  
   VenPartNum:string,
      /**  Defaulted from the PO release.  */  
   OrderNum:number,
      /**  Defaulted from the PO release.  */  
   OrderLine:number,
      /**  Defaulted from the PO release.  */  
   OrderRelNum:number,
      /**  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  */  
   XPartNum:string,
      /**  Field that contains the customer's revision.  */  
   XRevisionNum:string,
      /**  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  These comments will be copied into the Invoice detail.  */  
   InvoiceComment:string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   HeaderShipComment:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  */  
   Complete:boolean,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
      /**  Defaults from PODetail LineDesc.  */  
   LineDesc:string,
      /**  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  */  
   OurUnitCost:number,
      /**  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  */  
   DocUnitCost:number,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  */  
   VendorUnitCost:number,
      /**  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  */  
   ReceiptDate:string,
      /**  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  */  
   APInvoiced:boolean,
      /**  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  */  
   ARInvoiced:boolean,
      /**  Invoice Number from corresponding APInvHed record.  */  
   APInvoiceNum:string,
      /**  Invoice Number Line from corresponding APInvDtl record.  */  
   APInvoiceLine:number,
      /**  Invoice Number from corresponding InvcHead record.  */  
   ARInvoiceNum:number,
      /**  Invoice Number Line from corresponding InvcDtl record.  */  
   ARInvoiceLine:number,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Identifies a drop shipment line that is complete and ready to be invoiced.  */  
   ReceivedShipped:boolean,
      /**  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   MaterialMod:string,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   MiscMod:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Warranty comments.  */  
   WarrantyComment:string,
      /**  Duplicated from DropShipHead.CustNum.  */  
   CustNum:number,
      /**  Duplicated from DropShipHead.ShipTotNum.  */  
   ShipToNum:string,
      /**  Duplicated from DropShipHead.ShipToCustNum  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RequestedQty:number,
   ShippedToDateQty:number,
   ThisShipmentQty:number,
   RemainingQty:number,
   RequestedQtyUOM:string,
   ShippedToDateQtyUOM:string,
   ThisShipmentQtyUOM:string,
   RemainingQtyUOM:string,
   CurrencyCode:string,
   POComment:string,
      /**  Interger value of CostPerCode  */  
   CostPerFactor:number,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
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
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Second address line  */  
   PurPointAddress2:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   PurPointCountry:string,
      /**  State portion of the address  */  
   PurPointState:string,
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
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustNumCustID:string,
      /**  The full name of the customer.  */  
   ShipToCustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustNumBTName:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
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
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DropShipDtlListTableset{
   DropShipDtlList:Erp_Tablesets_DropShipDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DropShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for the drop shipment.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  */  
   PackLine:number,
      /**  Purchase order being drop shipped.  */  
   PONum:number,
      /**  The line number of the purchase order being drop shipped.  */  
   POLine:number,
      /**  The release number of the purchase order being drop shipped.  */  
   PORelNum:number,
      /**  Part Num defaulted from the PO release.  */  
   PartNum:string,
      /**  Part revision number.  */  
   RevisionNum:string,
      /**  Supplier's part num. Defaulted from the PO release.  */  
   VenPartNum:string,
      /**  Defaulted from the PO release.  */  
   OrderNum:number,
      /**  Defaulted from the PO release.  */  
   OrderLine:number,
      /**  Defaulted from the PO release.  */  
   OrderRelNum:number,
      /**  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  */  
   XPartNum:string,
      /**  Field that contains the customer's revision.  */  
   XRevisionNum:string,
      /**  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  */  
   OurQty:number,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  These comments will be copied into the Invoice detail.  */  
   InvoiceComment:string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   HeaderShipComment:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  */  
   Complete:boolean,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
      /**  Defaults from PODetail LineDesc.  */  
   LineDesc:string,
      /**  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  */  
   OurUnitCost:number,
      /**  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  */  
   DocUnitCost:number,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   VendorQty:number,
      /**  Vendor's selling Unit of Measure.  */  
   PUM:string,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  */  
   VendorUnitCost:number,
      /**  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  */  
   ReceiptDate:string,
      /**  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  */  
   APInvoiced:boolean,
      /**  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  */  
   ARInvoiced:boolean,
      /**  Invoice Number from corresponding APInvHed record.  */  
   APInvoiceNum:string,
      /**  Invoice Number Line from corresponding APInvDtl record.  */  
   APInvoiceLine:number,
      /**  Invoice Number from corresponding InvcHead record.  */  
   ARInvoiceNum:number,
      /**  Invoice Number Line from corresponding InvcDtl record.  */  
   ARInvoiceLine:number,
      /**  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  */  
   CostPerCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  */  
   TranReference:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Identifies a drop shipment line that is complete and ready to be invoiced.  */  
   ReceivedShipped:boolean,
      /**  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   MaterialMod:string,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   MiscMod:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Warranty comments.  */  
   WarrantyComment:string,
      /**  Duplicated from DropShipHead.CustNum.  */  
   CustNum:number,
      /**  Duplicated from DropShipHead.ShipTotNum.  */  
   ShipToNum:string,
      /**  Duplicated from DropShipHead.ShipToCustNum  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProjProcessed  */  
   ProjProcessed:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Estimated Value  */  
   MXEstValue:number,
      /**  Estimated Value Currency  */  
   MXEstValueCurrencyCode:string,
      /**  Total Net Weight in kilograms  */  
   MXTotalNetWeightKGM:number,
      /**  Hazardous Shipment  */  
   MXHazardousShipment:boolean,
      /**  Hazardous Type  */  
   MXHazardousType:string,
      /**  Package Type  */  
   MXPackageType:string,
   CurrencyCode:string,
   POComment:string,
   RemainingQty:number,
   RemainingQtyUOM:string,
   RequestedQty:number,
   RequestedQtyUOM:string,
   ShippedToDateQty:number,
   ShippedToDateQtyUOM:string,
   ThisShipmentQty:number,
   ThisShipmentQtyUOM:string,
   VendorCurrencyCode:string,
      /**  Interger value of CostPerCode  */  
   CostPerFactor:number,
      /**  The formatted bill to address  */  
   BillToAddrFormatted:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PurPointCity:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointZip:string,
   PurPointAddress3:string,
   PurPointState:string,
   PurPointName:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   ShipToCustNumName:string,
   ShipToCustNumCustID:string,
   ShipToCustNumBTName:string,
   ShipToNumInactive:boolean,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   VendorNumState:string,
   VendorNumName:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
   VendorNumAddress3:string,
   VendorNumCity:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DropShipDtlSearchTableset{
   DropShipDtl:Erp_Tablesets_DropShipDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDropShipDtlSearchTableset{
   DropShipDtl:Erp_Tablesets_DropShipDtlRow[],
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
   returnObj:Erp_Tablesets_DropShipDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DropShipDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DropShipDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_DropShipDtlListTableset[],
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
export interface GetNewDropShipDtl_input{
   ds:Erp_Tablesets_DropShipDtlSearchTableset[],
   vendorNum:number,
   purPoint:string,
   packSlip:string,
}

export interface GetNewDropShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipDtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseDropShipDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDropShipDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DropShipDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtDropShipDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDropShipDtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DropShipDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DropShipDtlSearchTableset,
}
}

