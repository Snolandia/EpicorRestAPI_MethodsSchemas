import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CCHdrSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/$metadata", {
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
   Description: Get CCHdrSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCHdrSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrRow
   */  
export function get_CCHdrSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCHdrSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CCHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCHdrSearches(requestBody:Erp_Tablesets_CCHdrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches", {
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
   Summary: Calls GetByID to retrieve the CCHdrSearch item
   Description: Calls GetByID to retrieve the CCHdrSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCHdrSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCHdrRow
   */  
export function get_CCHdrSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCHdrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
         resolve(data as Erp_Tablesets_CCHdrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCHdrSearch for the service
   Description: Calls UpdateExt to update CCHdrSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCHdrSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCHdrSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, requestBody:Erp_Tablesets_CCHdrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
   Summary: Call UpdateExt to delete CCHdrSearch item
   Description: Call UpdateExt to delete CCHdrSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCHdrSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCHdrSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow)
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
export function get_GetRows(whereClauseCCHdr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCCHdr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCHdr=" + whereClauseCCHdr
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, warehouseCode:string, ccYear:string, ccMonth:string, fullPhysical:string, cycleSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }
   if(typeof ccYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ccYear=" + ccYear
   }
   if(typeof ccMonth!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ccMonth=" + ccMonth
   }
   if(typeof fullPhysical!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fullPhysical=" + fullPhysical
   }
   if(typeof cycleSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cycleSeq=" + cycleSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewCCHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCHdr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCCHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCHdr(requestBody:GetNewCCHdr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCCHdr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/GetNewCCHdr", {
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
         resolve(data as GetNewCCHdr_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCHdrListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCHdrRow,
}

export interface Erp_Tablesets_CCHdrListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   "CycleDate":string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   "CycleStatus":number,
      /**  This is the date the tags were generated  */  
   "TagGenDate":string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   "SeqStartDate":string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   "TimeSeqStarted":number,
      /**  This is the date the cycle was completed or cancelled.  */  
   "CompleteDate":string,
      /**  This is the time the cycle was completed or cancelled.  */  
   "CompleteTime":number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   "AdjustPosted":boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   "SheetOrTag":number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   "TotalParts":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   "TotalPCIDSelected":number,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   "NumOfBlankTags":number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   "BlankTagsOnly":boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   "TagSortOption":number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   "PostTransDate":string,
      /**  External field used to hold the Post Counts log filename.  */  
   "LogFileName":string,
   "EnablePrintTags":boolean,
   "EnableReprintTags":boolean,
   "EnableVoidTagsByPart":boolean,
   "EnableVoidBlankTags":boolean,
   "EnableStartCountSeq":boolean,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   "RemoveAllParts":boolean,
   "CycleDateString":string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   "CycleStatusDesc":string,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   "CancelPI":boolean,
      /**  Month Name  */  
   "MonthName":string,
      /**  Description.  */  
   "CCHdrWarehseDescription":string,
      /**  Defines the end date of the period  */  
   "CCPeriodDefnPeriodEnd":string,
      /**  Defines the start date of the count period  */  
   "CCPeriodDefnPeriodStart":string,
      /**  Unique period description assigned by the user.  */  
   "CCPeriodDefnPeriodDesc":string,
   "WhseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCHdrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   "Plant":string,
      /**  Calendar year that this cycle count control record is for.  */  
   "CCYear":number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   "CCMonth":number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   "FullPhysical":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   "CycleDate":string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   "CycleStatus":number,
      /**  This is the date the tags were generated  */  
   "TagGenDate":string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   "SeqStartDate":string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   "TimeSeqStarted":number,
      /**  This is the date the cycle was completed or cancelled.  */  
   "CompleteDate":string,
      /**  This is the time the cycle was completed or cancelled.  */  
   "CompleteTime":number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   "AdjustPosted":boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   "SheetOrTag":number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   "TotalParts":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Legal Number of the record.  */  
   "LegalNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IncludeNonNettable  */  
   "IncludeNonNettable":boolean,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   "TotalPCIDSelected":number,
      /**  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  */  
   "NestedPCID":boolean,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   "CancelPI":boolean,
   "CycleDateString":string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   "CycleStatusDesc":string,
   "EnablePrintTags":boolean,
   "EnableReprintTags":boolean,
   "EnableStartCountSeq":boolean,
   "EnableVoidBlankTags":boolean,
   "EnableVoidTagsByPart":boolean,
      /**  External field used to hold the Post Counts log filename.  */  
   "LogFileName":string,
      /**  Month Name  */  
   "MonthName":string,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   "NumOfBlankTags":number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   "PostTransDate":string,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   "RemoveAllParts":boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   "TagSortOption":number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   "BlankTagsOnly":boolean,
      /**  field used by GenerateTags to indicate how many blank PCID tags should be generated  */  
   "NumOfBlankPCIDTags":number,
   "PartPostedExists":boolean,
   "TrackedNumberSerialPart":boolean,
      /**  Indicates that any PartNumTrackSerialNum = true exist in details  */  
   "PartNumTrackSerialNum":boolean,
   "BitFlag":number,
   "CCHdrWarehseDescription":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodEnd":string,
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
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
   */  
export interface DeleteByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CCHdrListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   CycleDate:string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   CycleStatus:number,
      /**  This is the date the tags were generated  */  
   TagGenDate:string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   SeqStartDate:string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   TimeSeqStarted:number,
      /**  This is the date the cycle was completed or cancelled.  */  
   CompleteDate:string,
      /**  This is the time the cycle was completed or cancelled.  */  
   CompleteTime:number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   AdjustPosted:boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   SheetOrTag:number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   TotalParts:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   TotalPCIDSelected:number,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   NumOfBlankTags:number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   BlankTagsOnly:boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   TagSortOption:number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   PostTransDate:string,
      /**  External field used to hold the Post Counts log filename.  */  
   LogFileName:string,
   EnablePrintTags:boolean,
   EnableReprintTags:boolean,
   EnableVoidTagsByPart:boolean,
   EnableVoidBlankTags:boolean,
   EnableStartCountSeq:boolean,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   RemoveAllParts:boolean,
   CycleDateString:string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   CycleStatusDesc:string,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   CancelPI:boolean,
      /**  Month Name  */  
   MonthName:string,
      /**  Description.  */  
   CCHdrWarehseDescription:string,
      /**  Defines the end date of the period  */  
   CCPeriodDefnPeriodEnd:string,
      /**  Defines the start date of the count period  */  
   CCPeriodDefnPeriodStart:string,
      /**  Unique period description assigned by the user.  */  
   CCPeriodDefnPeriodDesc:string,
   WhseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCHdrListTableset{
   CCHdrList:Erp_Tablesets_CCHdrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCHdrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  */  
   Plant:string,
      /**  Calendar year that this cycle count control record is for.  */  
   CCYear:number,
      /**  CCPeriodDefn.CycleSeq that this cycle count control record is for.  */  
   CCMonth:number,
      /**  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  */  
   FullPhysical:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  */  
   CycleDate:string,
      /**   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  */  
   CycleStatus:number,
      /**  This is the date the tags were generated  */  
   TagGenDate:string,
      /**  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  */  
   SeqStartDate:string,
      /**  This is the time the cycle sequence was started and inventory counts were frozen.  */  
   TimeSeqStarted:number,
      /**  This is the date the cycle was completed or cancelled.  */  
   CompleteDate:string,
      /**  This is the time the cycle was completed or cancelled.  */  
   CompleteTime:number,
      /**  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  */  
   AdjustPosted:boolean,
      /**   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  */  
   SheetOrTag:number,
      /**  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  */  
   TotalParts:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Legal Number of the record.  */  
   LegalNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IncludeNonNettable  */  
   IncludeNonNettable:boolean,
      /**  The total number of top level PCIDs selected for this cycle.  */  
   TotalPCIDSelected:number,
      /**  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  */  
   NestedPCID:boolean,
      /**  Used to indicate to the BL that the physical inventory cycle should be cancelled.  */  
   CancelPI:boolean,
   CycleDateString:string,
      /**  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  */  
   CycleStatusDesc:string,
   EnablePrintTags:boolean,
   EnableReprintTags:boolean,
   EnableStartCountSeq:boolean,
   EnableVoidBlankTags:boolean,
   EnableVoidTagsByPart:boolean,
      /**  External field used to hold the Post Counts log filename.  */  
   LogFileName:string,
      /**  Month Name  */  
   MonthName:string,
      /**  field used by GenerateTags to indicate how many blank tags should be generated  */  
   NumOfBlankTags:number,
      /**  External field to be used as the transaction date for the PartTran records created during post adjustments.  */  
   PostTransDate:string,
      /**  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  */  
   RemoveAllParts:boolean,
      /**  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  */  
   TagSortOption:number,
      /**  field used by Generate Tags logic to control when the user is limited to generating blank tags only  */  
   BlankTagsOnly:boolean,
      /**  field used by GenerateTags to indicate how many blank PCID tags should be generated  */  
   NumOfBlankPCIDTags:number,
   PartPostedExists:boolean,
   TrackedNumberSerialPart:boolean,
      /**  Indicates that any PartNumTrackSerialNum = true exist in details  */  
   PartNumTrackSerialNum:boolean,
   BitFlag:number,
   CCHdrWarehseDescription:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodEnd:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCHdrSearchTableset{
   CCHdr:Erp_Tablesets_CCHdrRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCCHdrSearchTableset{
   CCHdr:Erp_Tablesets_CCHdrRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
   */  
export interface GetByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CCHdrSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CCHdrSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CCHdrSearchTableset[],
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
   returnObj:Erp_Tablesets_CCHdrListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
   */  
export interface GetNewCCHdr_input{
   ds:Erp_Tablesets_CCHdrSearchTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
}

export interface GetNewCCHdr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCHdrSearchTableset,
}
}

   /** Required : 
      @param whereClauseCCHdr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCCHdr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CCHdrSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtCCHdrSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCCHdrSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CCHdrSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCHdrSearchTableset,
}
}

