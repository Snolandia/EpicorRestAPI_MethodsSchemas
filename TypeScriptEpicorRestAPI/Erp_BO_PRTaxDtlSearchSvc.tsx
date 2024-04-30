import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PRTaxDtlSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/$metadata", {
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
   Description: Get PRTaxDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlRow
   */  
export function get_PRTaxDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxDtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRTaxDtlSearches(requestBody:Erp_Tablesets_PRTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches", {
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
   Summary: Calls GetByID to retrieve the PRTaxDtlSearch item
   Description: Calls GetByID to retrieve the PRTaxDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRTaxDtlRow
   */  
export function get_PRTaxDtlSearches_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRTaxDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
         resolve(data as Erp_Tablesets_PRTaxDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRTaxDtlSearch for the service
   Description: Calls UpdateExt to update PRTaxDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRTaxDtlSearches_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, requestBody:Erp_Tablesets_PRTaxDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
   Summary: Call UpdateExt to delete PRTaxDtlSearch item
   Description: Call UpdateExt to delete PRTaxDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param FileStatus Desc: FileStatus   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRTaxDtlSearches_Company_TaxTblID_FileStatus_TaxYear(Company:string, TaxTblID:string, FileStatus:string, TaxYear:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/PRTaxDtlSearches(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlListRow)
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
export function get_GetRows(whereClausePRTaxDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePRTaxDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRTaxDtl=" + whereClausePRTaxDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(taxTblID:string, fileStatus:string, taxYear:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taxTblID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taxTblID=" + taxTblID
   }
   if(typeof fileStatus!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fileStatus=" + fileStatus
   }
   if(typeof taxYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taxYear=" + taxYear
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListCustom
   Description: Returns a list of rows that satisfy the where clause and removes duplicate rows.
   OperationID: GetListCustom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:GetListCustom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListCustom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetListCustom", {
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
         resolve(data as GetListCustom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPRTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRTaxDtl(requestBody:GetNewPRTaxDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRTaxDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetNewPRTaxDtl", {
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
         resolve(data as GetNewPRTaxDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRTaxDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRTaxDtlRow,
}

export interface Erp_Tablesets_PRTaxDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  */  
   "TaxYear":number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  Description of this tax filing status master.  Ex: Married, Single.  */  
   "FileStatusDesc":string,
      /**   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  */  
   "TaxBasis":string,
      /**  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  */  
   "TaxableWageLimit":number,
      /**  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  */  
   "TaxPercent":number,
      /**  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  */  
   "StdDeductionMin":number,
      /**  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  */  
   "StdDeductionMax":number,
      /**  Standard deduction percentage.  (See also StdDeductionMin, Max)  */  
   "StdDeductionPct":number,
      /**  An annual deduction amount which some states use when personal exemptions = 0.  */  
   "StdDeduction0":number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   "StdDeduction1":number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   "StdDeduction2":number,
      /**  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  */  
   "PersonalExAmt":number,
      /**  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  */  
   "DependentExAmt":number,
      /**  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   "PersonalCrAmt":number,
      /**  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   "DependentCrAmt":number,
      /**  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  */  
   "FITExPct":number,
      /**  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  */  
   "FITExMax":number,
      /**  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  */  
   "FICAExPct":number,
      /**   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  */  
   "FICAExMax":number,
      /**  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  */  
   "WeeklyLimit":number,
      /**   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  */  
   "SupplementalPercent":number,
      /**  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  */  
   "AddTaxPercent":number,
      /**  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  */  
   "AddTaxAmount":number,
      /**  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  */  
   "AddDeductionPercent":number,
      /**  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  */  
   "AddDeductionAmt1":number,
      /**  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  */  
   "AddDeductionAmt2":number,
      /**  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  */  
   "TaxableThreshold":number,
      /**  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  */  
   "AboveThresholdPercent":number,
      /**  Added for OK payroll.  Additional tax amount for wages above threshold.  */  
   "AboveThresholdAdditionalAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description  */  
   "TaxTblIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRTaxDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Tax Table ID  */  
   "TaxTblID":string,
      /**  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  */  
   "TaxYear":number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  Description of this tax filing status master.  Ex: Married, Single.  */  
   "FileStatusDesc":string,
      /**   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  */  
   "TaxBasis":string,
      /**  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  */  
   "TaxableWageLimit":number,
      /**  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  */  
   "TaxPercent":number,
      /**  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  */  
   "StdDeductionMin":number,
      /**  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  */  
   "StdDeductionMax":number,
      /**  Standard deduction percentage.  (See also StdDeductionMin, Max)  */  
   "StdDeductionPct":number,
      /**  An annual deduction amount which some states use when personal exemptions = 0.  */  
   "StdDeduction0":number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   "StdDeduction1":number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   "StdDeduction2":number,
      /**  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  */  
   "PersonalExAmt":number,
      /**  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  */  
   "DependentExAmt":number,
      /**  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   "PersonalCrAmt":number,
      /**  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   "DependentCrAmt":number,
      /**  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  */  
   "FITExPct":number,
      /**  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  */  
   "FITExMax":number,
      /**  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  */  
   "FICAExPct":number,
      /**   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  */  
   "FICAExMax":number,
      /**  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  */  
   "WeeklyLimit":number,
      /**   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  */  
   "SupplementalPercent":number,
      /**  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  */  
   "AddTaxPercent":number,
      /**  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  */  
   "AddTaxAmount":number,
      /**  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  */  
   "AddDeductionPercent":number,
      /**  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  */  
   "AddDeductionAmt1":number,
      /**  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  */  
   "AddDeductionAmt2":number,
      /**  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  */  
   "TaxableThreshold":number,
      /**  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  */  
   "AboveThresholdPercent":number,
      /**  Added for OK payroll.  Additional tax amount for wages above threshold.  */  
   "AboveThresholdAdditionalAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "TaxTblIDDescription":string,
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
      @param taxTblID
      @param fileStatus
      @param taxYear
   */  
export interface DeleteByID_input{
   taxTblID:string,
   fileStatus:string,
   taxYear:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PRTaxDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  */  
   TaxYear:number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  Description of this tax filing status master.  Ex: Married, Single.  */  
   FileStatusDesc:string,
      /**   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  */  
   TaxBasis:string,
      /**  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  */  
   TaxableWageLimit:number,
      /**  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  */  
   TaxPercent:number,
      /**  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  */  
   StdDeductionMin:number,
      /**  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  */  
   StdDeductionMax:number,
      /**  Standard deduction percentage.  (See also StdDeductionMin, Max)  */  
   StdDeductionPct:number,
      /**  An annual deduction amount which some states use when personal exemptions = 0.  */  
   StdDeduction0:number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   StdDeduction1:number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   StdDeduction2:number,
      /**  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  */  
   PersonalExAmt:number,
      /**  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  */  
   DependentExAmt:number,
      /**  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   PersonalCrAmt:number,
      /**  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   DependentCrAmt:number,
      /**  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  */  
   FITExPct:number,
      /**  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  */  
   FITExMax:number,
      /**  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  */  
   FICAExPct:number,
      /**   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  */  
   FICAExMax:number,
      /**  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  */  
   WeeklyLimit:number,
      /**   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  */  
   SupplementalPercent:number,
      /**  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  */  
   AddTaxPercent:number,
      /**  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  */  
   AddTaxAmount:number,
      /**  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  */  
   AddDeductionPercent:number,
      /**  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  */  
   AddDeductionAmt1:number,
      /**  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  */  
   AddDeductionAmt2:number,
      /**  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  */  
   TaxableThreshold:number,
      /**  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  */  
   AboveThresholdPercent:number,
      /**  Added for OK payroll.  Additional tax amount for wages above threshold.  */  
   AboveThresholdAdditionalAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description  */  
   TaxTblIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxDtlListTableset{
   PRTaxDtlList:Erp_Tablesets_PRTaxDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRTaxDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Tax Table ID  */  
   TaxTblID:string,
      /**  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  */  
   TaxYear:number,
      /**  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  Description of this tax filing status master.  Ex: Married, Single.  */  
   FileStatusDesc:string,
      /**   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  */  
   TaxBasis:string,
      /**  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  */  
   TaxableWageLimit:number,
      /**  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  */  
   TaxPercent:number,
      /**  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  */  
   StdDeductionMin:number,
      /**  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  */  
   StdDeductionMax:number,
      /**  Standard deduction percentage.  (See also StdDeductionMin, Max)  */  
   StdDeductionPct:number,
      /**  An annual deduction amount which some states use when personal exemptions = 0.  */  
   StdDeduction0:number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   StdDeduction1:number,
      /**  An annual deduction amount which some states use when personal exemptions = 1.  */  
   StdDeduction2:number,
      /**  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  */  
   PersonalExAmt:number,
      /**  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  */  
   DependentExAmt:number,
      /**  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   PersonalCrAmt:number,
      /**  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  */  
   DependentCrAmt:number,
      /**  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  */  
   FITExPct:number,
      /**  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  */  
   FITExMax:number,
      /**  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  */  
   FICAExPct:number,
      /**   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  */  
   FICAExMax:number,
      /**  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  */  
   WeeklyLimit:number,
      /**   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  */  
   SupplementalPercent:number,
      /**  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  */  
   AddTaxPercent:number,
      /**  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  */  
   AddTaxAmount:number,
      /**  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  */  
   AddDeductionPercent:number,
      /**  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  */  
   AddDeductionAmt1:number,
      /**  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  */  
   AddDeductionAmt2:number,
      /**  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  */  
   TaxableThreshold:number,
      /**  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  */  
   AboveThresholdPercent:number,
      /**  Added for OK payroll.  Additional tax amount for wages above threshold.  */  
   AboveThresholdAdditionalAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   TaxTblIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRTaxDtlSearchTableset{
   PRTaxDtl:Erp_Tablesets_PRTaxDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPRTaxDtlSearchTableset{
   PRTaxDtl:Erp_Tablesets_PRTaxDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param taxTblID
      @param fileStatus
      @param taxYear
   */  
export interface GetByID_input{
   taxTblID:string,
   fileStatus:string,
   taxYear:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PRTaxDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PRTaxDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PRTaxDtlSearchTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_PRTaxDtlListTableset[],
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
   returnObj:Erp_Tablesets_PRTaxDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param taxTblID
      @param fileStatus
   */  
export interface GetNewPRTaxDtl_input{
   ds:Erp_Tablesets_PRTaxDtlSearchTableset[],
   taxTblID:string,
   fileStatus:string,
}

export interface GetNewPRTaxDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRTaxDtlSearchTableset,
}
}

   /** Required : 
      @param whereClausePRTaxDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePRTaxDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PRTaxDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPRTaxDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPRTaxDtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PRTaxDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRTaxDtlSearchTableset,
}
}

