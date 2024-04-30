import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CoaSegAcctSearchSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/$metadata", {
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
   Description: Get CoaSegAcctSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CoaSegAcctSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegAcctRow
   */  
export function get_CoaSegAcctSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/CoaSegAcctSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CoaSegAcctSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.COASegAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CoaSegAcctSearches(requestBody:Erp_Tablesets_COASegAcctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/CoaSegAcctSearches", {
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
   Summary: Calls GetByID to retrieve the CoaSegAcctSearch item
   Description: Calls GetByID to retrieve the CoaSegAcctSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CoaSegAcctSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.COASegAcctRow
   */  
export function get_CoaSegAcctSearches_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COASegAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/CoaSegAcctSearches(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
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
         resolve(data as Erp_Tablesets_COASegAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CoaSegAcctSearch for the service
   Description: Calls UpdateExt to update CoaSegAcctSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CoaSegAcctSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CoaSegAcctSearches_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, requestBody:Erp_Tablesets_COASegAcctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/CoaSegAcctSearches(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
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
   Summary: Call UpdateExt to delete CoaSegAcctSearch item
   Description: Call UpdateExt to delete CoaSegAcctSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CoaSegAcctSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CoaSegAcctSearches_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company:string, COACode:string, SegmentNbr:string, SegmentCode:string, CurrencyCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/CoaSegAcctSearches(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegAcctListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctListRow)
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
export function get_GetRows(whereClauseCOASegAcct:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCOASegAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOASegAcct=" + whereClauseCOASegAcct
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(coACode:string, segmentNbr:string, segmentCode:string, currencyCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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
   if(typeof segmentCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "segmentCode=" + segmentCode
   }
   if(typeof currencyCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "currencyCode=" + currencyCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewCOASegAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegAcct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCOASegAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOASegAcct(requestBody:GetNewCOASegAcct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCOASegAcct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/GetNewCOASegAcct", {
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
         resolve(data as GetNewCOASegAcct_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CoaSegAcctSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegAcctListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COASegAcctRow,
}

export interface Erp_Tablesets_COASegAcctListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   "CurrencyCode":string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   "Allowed":boolean,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   "Revalue":number,
      /**  The natural account used for booking currency gains.  */  
   "GainAccount":string,
      /**  The natural account used for booking currency losses.  */  
   "LossAccount":string,
      /**  The natural account used as the accrual account.  */  
   "AccrualAccount":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COASegAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   "CurrencyCode":string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   "Allowed":boolean,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   "Revalue":number,
      /**  The natural account used for booking currency gains.  */  
   "GainAccount":string,
      /**  The natural account used for booking currency losses.  */  
   "LossAccount":string,
      /**  The natural account used as the accrual account.  */  
   "AccrualAccount":string,
      /**  GainSegVal1  */  
   "GainSegVal1":string,
      /**  GainSegVal2  */  
   "GainSegVal2":string,
      /**  GainSegVal3  */  
   "GainSegVal3":string,
      /**  GainSegVal4  */  
   "GainSegVal4":string,
      /**  GainSegVal5  */  
   "GainSegVal5":string,
      /**  GainSegVal6  */  
   "GainSegVal6":string,
      /**  GainSegVal7  */  
   "GainSegVal7":string,
      /**  GainSegVal8  */  
   "GainSegVal8":string,
      /**  GainSegVal9  */  
   "GainSegVal9":string,
      /**  GainSegVal10  */  
   "GainSegVal10":string,
      /**  GainSegVal11  */  
   "GainSegVal11":string,
      /**  GainSegVal12  */  
   "GainSegVal12":string,
      /**  GainSegVal13  */  
   "GainSegVal13":string,
      /**  GainSegVal14  */  
   "GainSegVal14":string,
      /**  GainSegVal15  */  
   "GainSegVal15":string,
      /**  GainSegVal16  */  
   "GainSegVal16":string,
      /**  GainSegVal17  */  
   "GainSegVal17":string,
      /**  GainSegVal18  */  
   "GainSegVal18":string,
      /**  GainSegVal19  */  
   "GainSegVal19":string,
      /**  GainSegVal20  */  
   "GainSegVal20":string,
      /**  LossSegVal1  */  
   "LossSegVal1":string,
      /**  LossSegVal2  */  
   "LossSegVal2":string,
      /**  LossSegVal3  */  
   "LossSegVal3":string,
      /**  LossSegVal4  */  
   "LossSegVal4":string,
      /**  LossSegVal5  */  
   "LossSegVal5":string,
      /**  LossSegVal6  */  
   "LossSegVal6":string,
      /**  LossSegVal7  */  
   "LossSegVal7":string,
      /**  LossSegVal8  */  
   "LossSegVal8":string,
      /**  LossSegVal9  */  
   "LossSegVal9":string,
      /**  LossSegVal10  */  
   "LossSegVal10":string,
      /**  LossSegVal11  */  
   "LossSegVal11":string,
      /**  LossSegVal12  */  
   "LossSegVal12":string,
      /**  LossSegVal13  */  
   "LossSegVal13":string,
      /**  LossSegVal14  */  
   "LossSegVal14":string,
      /**  LossSegVal15  */  
   "LossSegVal15":string,
      /**  LossSegVal16  */  
   "LossSegVal16":string,
      /**  LossSegVal17  */  
   "LossSegVal17":string,
      /**  LossSegVal18  */  
   "LossSegVal18":string,
      /**  LossSegVal19  */  
   "LossSegVal19":string,
      /**  LossSegVal20  */  
   "LossSegVal20":string,
      /**  AccrualSegVal1  */  
   "AccrualSegVal1":string,
      /**  AccrualSegVal2  */  
   "AccrualSegVal2":string,
      /**  AccrualSegVal3  */  
   "AccrualSegVal3":string,
      /**  AccrualSegVal4  */  
   "AccrualSegVal4":string,
      /**  AccrualSegVal5  */  
   "AccrualSegVal5":string,
      /**  AccrualSegVal6  */  
   "AccrualSegVal6":string,
      /**  AccrualSegVal7  */  
   "AccrualSegVal7":string,
      /**  AccrualSegVal8  */  
   "AccrualSegVal8":string,
      /**  AccrualSegVal9  */  
   "AccrualSegVal9":string,
      /**  AccrualSegVal10  */  
   "AccrualSegVal10":string,
      /**  AccrualSegVal11  */  
   "AccrualSegVal11":string,
      /**  AccrualSegVal12  */  
   "AccrualSegVal12":string,
      /**  AccrualSegVal13  */  
   "AccrualSegVal13":string,
      /**  AccrualSegVal14  */  
   "AccrualSegVal14":string,
      /**  AccrualSegVal15  */  
   "AccrualSegVal15":string,
      /**  AccrualSegVal16  */  
   "AccrualSegVal16":string,
      /**  AccrualSegVal17  */  
   "AccrualSegVal17":string,
      /**  AccrualSegVal18  */  
   "AccrualSegVal18":string,
      /**  AccrualSegVal19  */  
   "AccrualSegVal19":string,
      /**  AccrualSegVal20  */  
   "AccrualSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Accrual GL Account description  */  
   "AccrualGLDesc":string,
      /**  Gain GL Account Description  */  
   "GainGLDesc":string,
      /**  Loss GL Account Description  */  
   "LossGLDesc":string,
   "BitFlag":number,
   "CurrencyCurrencyID":string,
   "CurrencyCurrDesc":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
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
      @param coACode
      @param segmentNbr
      @param segmentCode
      @param currencyCode
   */  
export interface DeleteByID_input{
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
   currencyCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_COASegAcctListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   CurrencyCode:string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   Allowed:boolean,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   Revalue:number,
      /**  The natural account used for booking currency gains.  */  
   GainAccount:string,
      /**  The natural account used for booking currency losses.  */  
   LossAccount:string,
      /**  The natural account used as the accrual account.  */  
   AccrualAccount:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COASegAcctListTableset{
   COASegAcctList:Erp_Tablesets_COASegAcctListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_COASegAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  */  
   CurrencyCode:string,
      /**  Indicates the currency can be used as a transactional currency.  */  
   Allowed:boolean,
      /**   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  */  
   Revalue:number,
      /**  The natural account used for booking currency gains.  */  
   GainAccount:string,
      /**  The natural account used for booking currency losses.  */  
   LossAccount:string,
      /**  The natural account used as the accrual account.  */  
   AccrualAccount:string,
      /**  GainSegVal1  */  
   GainSegVal1:string,
      /**  GainSegVal2  */  
   GainSegVal2:string,
      /**  GainSegVal3  */  
   GainSegVal3:string,
      /**  GainSegVal4  */  
   GainSegVal4:string,
      /**  GainSegVal5  */  
   GainSegVal5:string,
      /**  GainSegVal6  */  
   GainSegVal6:string,
      /**  GainSegVal7  */  
   GainSegVal7:string,
      /**  GainSegVal8  */  
   GainSegVal8:string,
      /**  GainSegVal9  */  
   GainSegVal9:string,
      /**  GainSegVal10  */  
   GainSegVal10:string,
      /**  GainSegVal11  */  
   GainSegVal11:string,
      /**  GainSegVal12  */  
   GainSegVal12:string,
      /**  GainSegVal13  */  
   GainSegVal13:string,
      /**  GainSegVal14  */  
   GainSegVal14:string,
      /**  GainSegVal15  */  
   GainSegVal15:string,
      /**  GainSegVal16  */  
   GainSegVal16:string,
      /**  GainSegVal17  */  
   GainSegVal17:string,
      /**  GainSegVal18  */  
   GainSegVal18:string,
      /**  GainSegVal19  */  
   GainSegVal19:string,
      /**  GainSegVal20  */  
   GainSegVal20:string,
      /**  LossSegVal1  */  
   LossSegVal1:string,
      /**  LossSegVal2  */  
   LossSegVal2:string,
      /**  LossSegVal3  */  
   LossSegVal3:string,
      /**  LossSegVal4  */  
   LossSegVal4:string,
      /**  LossSegVal5  */  
   LossSegVal5:string,
      /**  LossSegVal6  */  
   LossSegVal6:string,
      /**  LossSegVal7  */  
   LossSegVal7:string,
      /**  LossSegVal8  */  
   LossSegVal8:string,
      /**  LossSegVal9  */  
   LossSegVal9:string,
      /**  LossSegVal10  */  
   LossSegVal10:string,
      /**  LossSegVal11  */  
   LossSegVal11:string,
      /**  LossSegVal12  */  
   LossSegVal12:string,
      /**  LossSegVal13  */  
   LossSegVal13:string,
      /**  LossSegVal14  */  
   LossSegVal14:string,
      /**  LossSegVal15  */  
   LossSegVal15:string,
      /**  LossSegVal16  */  
   LossSegVal16:string,
      /**  LossSegVal17  */  
   LossSegVal17:string,
      /**  LossSegVal18  */  
   LossSegVal18:string,
      /**  LossSegVal19  */  
   LossSegVal19:string,
      /**  LossSegVal20  */  
   LossSegVal20:string,
      /**  AccrualSegVal1  */  
   AccrualSegVal1:string,
      /**  AccrualSegVal2  */  
   AccrualSegVal2:string,
      /**  AccrualSegVal3  */  
   AccrualSegVal3:string,
      /**  AccrualSegVal4  */  
   AccrualSegVal4:string,
      /**  AccrualSegVal5  */  
   AccrualSegVal5:string,
      /**  AccrualSegVal6  */  
   AccrualSegVal6:string,
      /**  AccrualSegVal7  */  
   AccrualSegVal7:string,
      /**  AccrualSegVal8  */  
   AccrualSegVal8:string,
      /**  AccrualSegVal9  */  
   AccrualSegVal9:string,
      /**  AccrualSegVal10  */  
   AccrualSegVal10:string,
      /**  AccrualSegVal11  */  
   AccrualSegVal11:string,
      /**  AccrualSegVal12  */  
   AccrualSegVal12:string,
      /**  AccrualSegVal13  */  
   AccrualSegVal13:string,
      /**  AccrualSegVal14  */  
   AccrualSegVal14:string,
      /**  AccrualSegVal15  */  
   AccrualSegVal15:string,
      /**  AccrualSegVal16  */  
   AccrualSegVal16:string,
      /**  AccrualSegVal17  */  
   AccrualSegVal17:string,
      /**  AccrualSegVal18  */  
   AccrualSegVal18:string,
      /**  AccrualSegVal19  */  
   AccrualSegVal19:string,
      /**  AccrualSegVal20  */  
   AccrualSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Accrual GL Account description  */  
   AccrualGLDesc:string,
      /**  Gain GL Account Description  */  
   GainGLDesc:string,
      /**  Loss GL Account Description  */  
   LossGLDesc:string,
   BitFlag:number,
   CurrencyCurrencyID:string,
   CurrencyCurrDesc:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CoaSegAcctSearchTableset{
   COASegAcct:Erp_Tablesets_COASegAcctRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCoaSegAcctSearchTableset{
   COASegAcct:Erp_Tablesets_COASegAcctRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param coACode
      @param segmentNbr
      @param segmentCode
      @param currencyCode
   */  
export interface GetByID_input{
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
   currencyCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CoaSegAcctSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CoaSegAcctSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CoaSegAcctSearchTableset[],
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
   returnObj:Erp_Tablesets_COASegAcctListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetNewCOASegAcct_input{
   ds:Erp_Tablesets_CoaSegAcctSearchTableset[],
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetNewCOASegAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CoaSegAcctSearchTableset,
}
}

   /** Required : 
      @param whereClauseCOASegAcct
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCOASegAcct:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CoaSegAcctSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtCoaSegAcctSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCoaSegAcctSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CoaSegAcctSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CoaSegAcctSearchTableset,
}
}

