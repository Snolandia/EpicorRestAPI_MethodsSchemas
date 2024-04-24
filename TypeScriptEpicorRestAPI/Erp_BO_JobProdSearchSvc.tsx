import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobProdSearchSvc
// Description: Search object for JobProd records
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/$metadata", {
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
   Description: Get JobProdSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobProdSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobProdRow
   */  
export function get_JobProdSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/JobProdSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobProdSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobProdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobProdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobProdSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/JobProdSearches", {
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
   Summary: Calls GetByID to retrieve the JobProdSearch item
   Description: Calls GetByID to retrieve the JobProdSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobProdSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param TargetJobNum Desc: TargetJobNum   Required: True   Allow empty value : True
      @param TargetAssemblySeq Desc: TargetAssemblySeq   Required: True
      @param TargetMtlSeq Desc: TargetMtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobProdRow
   */  
export function get_JobProdSearches_Company_JobNum_PartNum_OrderNum_OrderLine_OrderRelNum_WarehouseCode_TargetJobNum_TargetAssemblySeq_TargetMtlSeq(Company:string, JobNum:string, PartNum:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, TargetJobNum:string, TargetAssemblySeq:string, TargetMtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobProdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/JobProdSearches(" + Company + "," + JobNum + "," + PartNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + TargetJobNum + "," + TargetAssemblySeq + "," + TargetMtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JobProdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobProdSearch for the service
   Description: Calls UpdateExt to update JobProdSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobProdSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param TargetJobNum Desc: TargetJobNum   Required: True   Allow empty value : True
      @param TargetAssemblySeq Desc: TargetAssemblySeq   Required: True
      @param TargetMtlSeq Desc: TargetMtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobProdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobProdSearches_Company_JobNum_PartNum_OrderNum_OrderLine_OrderRelNum_WarehouseCode_TargetJobNum_TargetAssemblySeq_TargetMtlSeq(Company:string, JobNum:string, PartNum:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, TargetJobNum:string, TargetAssemblySeq:string, TargetMtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/JobProdSearches(" + Company + "," + JobNum + "," + PartNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + TargetJobNum + "," + TargetAssemblySeq + "," + TargetMtlSeq + ")", {
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
   Summary: Call UpdateExt to delete JobProdSearch item
   Description: Call UpdateExt to delete JobProdSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobProdSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param TargetJobNum Desc: TargetJobNum   Required: True   Allow empty value : True
      @param TargetAssemblySeq Desc: TargetAssemblySeq   Required: True
      @param TargetMtlSeq Desc: TargetMtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobProdSearches_Company_JobNum_PartNum_OrderNum_OrderLine_OrderRelNum_WarehouseCode_TargetJobNum_TargetAssemblySeq_TargetMtlSeq(Company:string, JobNum:string, PartNum:string, OrderNum:string, OrderLine:string, OrderRelNum:string, WarehouseCode:string, TargetJobNum:string, TargetAssemblySeq:string, TargetMtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/JobProdSearches(" + Company + "," + JobNum + "," + PartNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + WarehouseCode + "," + TargetJobNum + "," + TargetAssemblySeq + "," + TargetMtlSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobProdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdListRow)
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
export function get_GetRows(whereClauseJobProd:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobProd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobProd=" + whereClauseJobProd
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, partNum:string, orderNum:string, orderLine:string, orderRelNum:string, warehouseCode:string, targetJobNum:string, targetAssemblySeq:string, targetMtlSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof orderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderNum=" + orderNum
   }
   if(typeof orderLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderLine=" + orderLine
   }
   if(typeof orderRelNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderRelNum=" + orderRelNum
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
   if(typeof targetJobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "targetJobNum=" + targetJobNum
   }
   if(typeof targetAssemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "targetAssemblySeq=" + targetAssemblySeq
   }
   if(typeof targetMtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "targetMtlSeq=" + targetMtlSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewJobProd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobProd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobProd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobProd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobProd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/GetNewJobProd", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobProdSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobProdListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobProdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobProdRow[],
}

export interface Erp_Tablesets_JobProdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   "JobNum":string,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  */  
   "ProdQty":number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   "WarehouseCode":string,
      /**  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  */  
   "TargetJobNum":string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetAssemblySeq":number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetMtlSeq":number,
      /**   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  */  
   "ShippedQty":number,
      /**   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  */  
   "ReceivedQty":number,
      /**   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  */  
   "WIPQty":number,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The demand contract this demand schedule is for.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   "DemandHeadSeq":number,
      /**  The sequence from the DemandDetail record this DemandSchedule is related to.  */  
   "DemandDtlSeq":number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  */  
   "DemandScheduleSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The Demand Link Due Date - Ship By  */  
   "ShipBy":string,
      /**  The demand link status  */  
   "DemandLinkStatus":string,
      /**  The demand linke source  */  
   "DemandLinkSource":string,
      /**  The Make to type (i.e. Stock, Job, Order)  */  
   "MakeToType":string,
      /**  The customer ID  */  
   "CustID":string,
      /**  The customer name.  */  
   "CustName":string,
      /**  The stock WIP quantity  */  
   "StkWIPQty":number,
      /**  The order WIP quantity  */  
   "OrdWIPQty":number,
      /**  The jobhead part number  */  
   "JHPartNum":string,
      /**  The jobasmbl part number.  */  
   "AsmPartNum":string,
      /**  The jobmtl part number.  */  
   "MtlPartNum":string,
      /**  The jobhead part description  */  
   "JHPartDesc":string,
      /**  The jobasmbl part description.  */  
   "AsmPartDesc":string,
      /**  The jobmtl part description.  */  
   "MtlPartDesc":string,
      /**  Calculated field OurStockQty, will update OrderRel.OurStockQty  */  
   "OurStockQty":number,
      /**  The make to stock quantity  */  
   "MakeToStockQty":number,
      /**  The make to job quantity  */  
   "MakeToJobQty":number,
      /**  Pull from Stock warehouse code (orderrel.warehousecode  */  
   "PullFromStockWarehouseCode":string,
      /**  The pull from stock warehouse description  */  
   "PullFromStockWarehouseDesc":string,
      /**  The split quantity for the demand.  */  
   "SplitQty":number,
      /**  Calculated quantity that could come from allocatedqty or accumulation from parttran.  */  
   "MaxAllowedQty":number,
      /**  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  */  
   "TotalSplitQuantity":number,
      /**  This is a field used in Split Job to determine if record has been validated.  */  
   "Valid":boolean,
   "TFOrdLine":number,
   "TFOrdNum":string,
      /**  IUM  */  
   "IUM":string,
   "TrackSerialNumbers":boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "CallLineLineDesc":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartTrackLots":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "PartTrackSerialNum":boolean,
      /**  Describes the Part.  */  
   "PartPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartSellingFactor":number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartTrackDimension":boolean,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobProdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   "JobNum":string,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   "OrderNum":number,
      /**  Related Sales order line number.  */  
   "OrderLine":number,
      /**  Related sales order release number.  */  
   "OrderRelNum":number,
      /**   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  */  
   "ProdQty":number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   "WarehouseCode":string,
      /**  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  */  
   "TargetJobNum":string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetAssemblySeq":number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   "TargetMtlSeq":number,
      /**   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  */  
   "ShippedQty":number,
      /**   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  */  
   "ReceivedQty":number,
      /**   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  */  
   "WIPQty":number,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The demand contract this demand schedule is for.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   "DemandHeadSeq":number,
      /**  The sequence from the DemandDetail record this DemandSchedule is related to.  */  
   "DemandDtlSeq":number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  */  
   "DemandScheduleSeq":number,
      /**  PlanUserID  */  
   "PlanUserID":string,
      /**  PlanID  */  
   "PlanID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Job will be shipped through a Misc Shipment directly from WIP when job is closed.  */  
   "WIPToMiscShipment":boolean,
      /**  RMA Num linked from RMA Disposition.  */  
   "RMANum":number,
      /**  RMA Line linked from RMA Disposition.  */  
   "RMALine":number,
      /**  RMA Receipt linked from RMA Disposition.  */  
   "RMAReceipt":number,
      /**  RMA Disposition linked from RMA Disposition.  */  
   "RMADisp":number,
      /**  DMRNum  */  
   "DMRNum":number,
      /**  DMRActionNum  */  
   "DMRActionNum":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  The customer ID  */  
   "CustID":string,
      /**  The customer name.  */  
   "CustName":string,
      /**  The demand linke source  */  
   "DemandLinkSource":string,
      /**  The demand link status  */  
   "DemandLinkStatus":string,
      /**  IUM  */  
   "IUM":string,
      /**  The jobhead part description  */  
   "JHPartDesc":string,
      /**  The jobhead part number  */  
   "JHPartNum":string,
      /**  The make to job quantity  */  
   "MakeToJobQty":number,
      /**  The make to stock quantity  */  
   "MakeToStockQty":number,
      /**  The Make to type (i.e. Stock, Job, Order)  */  
   "MakeToType":string,
      /**  Calculated quantity that could come from allocatedqty or accumulation from parttran.  */  
   "MaxAllowedQty":number,
      /**  The jobmtl part description.  */  
   "MtlPartDesc":string,
      /**  The jobmtl part number.  */  
   "MtlPartNum":string,
      /**  The order WIP quantity  */  
   "OrdWIPQty":number,
      /**  Calculated field OurStockQty, will update OrderRel.OurStockQty  */  
   "OurStockQty":number,
      /**  Pull from Stock warehouse code (orderrel.warehousecode  */  
   "PullFromStockWarehouseCode":string,
      /**  The pull from stock warehouse description  */  
   "PullFromStockWarehouseDesc":string,
      /**  The Demand Link Due Date - Ship By  */  
   "ShipBy":string,
      /**  The split quantity for the demand.  */  
   "SplitQty":number,
      /**  The stock WIP quantity  */  
   "StkWIPQty":number,
   "TFOrdLine":number,
   "TFOrdNum":string,
      /**  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  */  
   "TotalSplitQuantity":number,
   "TrackSerialNumbers":boolean,
      /**  This is a field used in Split Job to determine if record has been validated.  */  
   "Valid":boolean,
      /**  The jobasmbl part description.  */  
   "AsmPartDesc":string,
      /**  The jobasmbl part number.  */  
   "AsmPartNum":string,
   "EnableAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
      /**  Indicates a customer referenced on the record is inactive.  */  
   "CustInactive":boolean,
      /**  Indicates if a ShipTo referenced on the record is inactive.  */  
   "ShipToNumInactive":boolean,
   "BitFlag":number,
   "CallLineLineDesc":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobNumPartDescription":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartAttrClassID":string,
   "PartTrackInventoryByRevision":boolean,
   "PartSalesUM":string,
   "PartTrackSerialNum":boolean,
   "PartSellingFactor":number,
   "PartTrackLots":boolean,
   "PartIUM":string,
   "PartTrackDimension":boolean,
   "PartPricePerCode":string,
   "PartPartDescription":string,
   "PartTrackInventoryAttributes":boolean,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param jobNum
      @param partNum
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param warehouseCode
      @param targetJobNum
      @param targetAssemblySeq
      @param targetMtlSeq
   */  
export interface DeleteByID_input{
   jobNum:string,
   partNum:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   warehouseCode:string,
   targetJobNum:string,
   targetAssemblySeq:number,
   targetMtlSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobProdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   JobNum:string,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  */  
   ProdQty:number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   WarehouseCode:string,
      /**  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  */  
   TargetJobNum:string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetAssemblySeq:number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetMtlSeq:number,
      /**   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  */  
   ShippedQty:number,
      /**   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  */  
   ReceivedQty:number,
      /**   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  */  
   WIPQty:number,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The demand contract this demand schedule is for.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   DemandHeadSeq:number,
      /**  The sequence from the DemandDetail record this DemandSchedule is related to.  */  
   DemandDtlSeq:number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  */  
   DemandScheduleSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The Demand Link Due Date - Ship By  */  
   ShipBy:string,
      /**  The demand link status  */  
   DemandLinkStatus:string,
      /**  The demand linke source  */  
   DemandLinkSource:string,
      /**  The Make to type (i.e. Stock, Job, Order)  */  
   MakeToType:string,
      /**  The customer ID  */  
   CustID:string,
      /**  The customer name.  */  
   CustName:string,
      /**  The stock WIP quantity  */  
   StkWIPQty:number,
      /**  The order WIP quantity  */  
   OrdWIPQty:number,
      /**  The jobhead part number  */  
   JHPartNum:string,
      /**  The jobasmbl part number.  */  
   AsmPartNum:string,
      /**  The jobmtl part number.  */  
   MtlPartNum:string,
      /**  The jobhead part description  */  
   JHPartDesc:string,
      /**  The jobasmbl part description.  */  
   AsmPartDesc:string,
      /**  The jobmtl part description.  */  
   MtlPartDesc:string,
      /**  Calculated field OurStockQty, will update OrderRel.OurStockQty  */  
   OurStockQty:number,
      /**  The make to stock quantity  */  
   MakeToStockQty:number,
      /**  The make to job quantity  */  
   MakeToJobQty:number,
      /**  Pull from Stock warehouse code (orderrel.warehousecode  */  
   PullFromStockWarehouseCode:string,
      /**  The pull from stock warehouse description  */  
   PullFromStockWarehouseDesc:string,
      /**  The split quantity for the demand.  */  
   SplitQty:number,
      /**  Calculated quantity that could come from allocatedqty or accumulation from parttran.  */  
   MaxAllowedQty:number,
      /**  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  */  
   TotalSplitQuantity:number,
      /**  This is a field used in Split Job to determine if record has been validated.  */  
   Valid:boolean,
   TFOrdLine:number,
   TFOrdNum:string,
      /**  IUM  */  
   IUM:string,
   TrackSerialNumbers:boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   CallLineLineDesc:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartTrackLots:boolean,
      /**  Indicates if this part is serial number tracked  */  
   PartTrackSerialNum:boolean,
      /**  Describes the Part.  */  
   PartPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartSellingFactor:number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartTrackDimension:boolean,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobProdListTableset{
   JobProdList:Erp_Tablesets_JobProdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobProdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   JobNum:string,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  */  
   ProdQty:number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   WarehouseCode:string,
      /**  Production Demands can be from other jobs.  That is, one job can be building parts that are required by another job. The demand is defined by a JobMtl record on some other job.  "TargetJobNum" is the job that this job is making parts for.  */  
   TargetJobNum:string,
      /**  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetAssemblySeq:number,
      /**  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  */  
   TargetMtlSeq:number,
      /**   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  */  
   ShippedQty:number,
      /**   Total quantity received to stock for this production allocation.
Updated via the Manufacturing Receipts process  */  
   ReceivedQty:number,
      /**   Represents the "outstanding" WIP production quantity.
WIPQty = JobProd.Quantity - (ShippedQty +ReceivedQty) if negative then it is set to zero. If related Order Release is closed then reservation is zero.
Updated via the JobProd, OrderRel triggers.  */  
   WIPQty:number,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The demand contract this demand schedule is for.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   DemandHeadSeq:number,
      /**  The sequence from the DemandDetail record this DemandSchedule is related to.  */  
   DemandDtlSeq:number,
      /**  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDetailSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandSchedulel record for the DemandDetail and the adding 1 to it.  */  
   DemandScheduleSeq:number,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  PlanID  */  
   PlanID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Job will be shipped through a Misc Shipment directly from WIP when job is closed.  */  
   WIPToMiscShipment:boolean,
      /**  RMA Num linked from RMA Disposition.  */  
   RMANum:number,
      /**  RMA Line linked from RMA Disposition.  */  
   RMALine:number,
      /**  RMA Receipt linked from RMA Disposition.  */  
   RMAReceipt:number,
      /**  RMA Disposition linked from RMA Disposition.  */  
   RMADisp:number,
      /**  DMRNum  */  
   DMRNum:number,
      /**  DMRActionNum  */  
   DMRActionNum:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The customer ID  */  
   CustID:string,
      /**  The customer name.  */  
   CustName:string,
      /**  The demand linke source  */  
   DemandLinkSource:string,
      /**  The demand link status  */  
   DemandLinkStatus:string,
      /**  IUM  */  
   IUM:string,
      /**  The jobhead part description  */  
   JHPartDesc:string,
      /**  The jobhead part number  */  
   JHPartNum:string,
      /**  The make to job quantity  */  
   MakeToJobQty:number,
      /**  The make to stock quantity  */  
   MakeToStockQty:number,
      /**  The Make to type (i.e. Stock, Job, Order)  */  
   MakeToType:string,
      /**  Calculated quantity that could come from allocatedqty or accumulation from parttran.  */  
   MaxAllowedQty:number,
      /**  The jobmtl part description.  */  
   MtlPartDesc:string,
      /**  The jobmtl part number.  */  
   MtlPartNum:string,
      /**  The order WIP quantity  */  
   OrdWIPQty:number,
      /**  Calculated field OurStockQty, will update OrderRel.OurStockQty  */  
   OurStockQty:number,
      /**  Pull from Stock warehouse code (orderrel.warehousecode  */  
   PullFromStockWarehouseCode:string,
      /**  The pull from stock warehouse description  */  
   PullFromStockWarehouseDesc:string,
      /**  The Demand Link Due Date - Ship By  */  
   ShipBy:string,
      /**  The split quantity for the demand.  */  
   SplitQty:number,
      /**  The stock WIP quantity  */  
   StkWIPQty:number,
   TFOrdLine:number,
   TFOrdNum:string,
      /**  Temp field so UI has a column to bind to for calculation of Total Split Quantity.  */  
   TotalSplitQuantity:number,
   TrackSerialNumbers:boolean,
      /**  This is a field used in Split Job to determine if record has been validated.  */  
   Valid:boolean,
      /**  The jobasmbl part description.  */  
   AsmPartDesc:string,
      /**  The jobasmbl part number.  */  
   AsmPartNum:string,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Indicates a customer referenced on the record is inactive.  */  
   CustInactive:boolean,
      /**  Indicates if a ShipTo referenced on the record is inactive.  */  
   ShipToNumInactive:boolean,
   BitFlag:number,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartAttrClassID:string,
   PartTrackInventoryByRevision:boolean,
   PartSalesUM:string,
   PartTrackSerialNum:boolean,
   PartSellingFactor:number,
   PartTrackLots:boolean,
   PartIUM:string,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartPartDescription:string,
   PartTrackInventoryAttributes:boolean,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobProdSearchTableset{
   JobProd:Erp_Tablesets_JobProdRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJobProdSearchTableset{
   JobProd:Erp_Tablesets_JobProdRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param partNum
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param warehouseCode
      @param targetJobNum
      @param targetAssemblySeq
      @param targetMtlSeq
   */  
export interface GetByID_input{
   jobNum:string,
   partNum:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   warehouseCode:string,
   targetJobNum:string,
   targetAssemblySeq:number,
   targetMtlSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobProdSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobProdSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobProdSearchTableset[],
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
   returnObj:Erp_Tablesets_JobProdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
      @param partNum
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param warehouseCode
      @param targetJobNum
      @param targetAssemblySeq
   */  
export interface GetNewJobProd_input{
   ds:Erp_Tablesets_JobProdSearchTableset[],
   jobNum:string,
   partNum:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   warehouseCode:string,
   targetJobNum:string,
   targetAssemblySeq:number,
}

export interface GetNewJobProd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobProdSearchTableset[],
}
}

   /** Required : 
      @param whereClauseJobProd
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobProd:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobProdSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtJobProdSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobProdSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobProdSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobProdSearchTableset[],
}
}

