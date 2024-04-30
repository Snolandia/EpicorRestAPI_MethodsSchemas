import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CrossDockSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/$metadata", {
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
   Description: Get CrossDocks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CrossDocks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CrossDockRow
   */  
export function get_CrossDocks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CrossDocks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CrossDockRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CrossDockRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CrossDocks(requestBody:Erp_Tablesets_CrossDockRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks", {
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
   Summary: Calls GetByID to retrieve the CrossDock item
   Description: Calls GetByID to retrieve the CrossDock item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CrossDock
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param TFOrdLine Desc: TFOrdLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CrossDockRow
   */  
export function get_CrossDocks_Company_PartNum_WarehouseCode_BinNum_SupplyJobNum_OrderNum_OrderLine_OrderRelNum_JobNum_AssemblySeq_MtlSeq_TFOrdNum_TFOrdLine(Company:string, PartNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, OrderNum:string, OrderLine:string, OrderRelNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, TFOrdNum:string, TFOrdLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CrossDockRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + "," + TFOrdNum + "," + TFOrdLine + ")", {
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
         resolve(data as Erp_Tablesets_CrossDockRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CrossDock for the service
   Description: Calls UpdateExt to update CrossDock. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CrossDock
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param TFOrdLine Desc: TFOrdLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CrossDockRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CrossDocks_Company_PartNum_WarehouseCode_BinNum_SupplyJobNum_OrderNum_OrderLine_OrderRelNum_JobNum_AssemblySeq_MtlSeq_TFOrdNum_TFOrdLine(Company:string, PartNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, OrderNum:string, OrderLine:string, OrderRelNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, TFOrdNum:string, TFOrdLine:string, requestBody:Erp_Tablesets_CrossDockRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + "," + TFOrdNum + "," + TFOrdLine + ")", {
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
   Summary: Call UpdateExt to delete CrossDock item
   Description: Call UpdateExt to delete CrossDock item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CrossDock
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param SupplyJobNum Desc: SupplyJobNum   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param TFOrdNum Desc: TFOrdNum   Required: True   Allow empty value : True
      @param TFOrdLine Desc: TFOrdLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CrossDocks_Company_PartNum_WarehouseCode_BinNum_SupplyJobNum_OrderNum_OrderLine_OrderRelNum_JobNum_AssemblySeq_MtlSeq_TFOrdNum_TFOrdLine(Company:string, PartNum:string, WarehouseCode:string, BinNum:string, SupplyJobNum:string, OrderNum:string, OrderLine:string, OrderRelNum:string, JobNum:string, AssemblySeq:string, MtlSeq:string, TFOrdNum:string, TFOrdLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + "," + TFOrdNum + "," + TFOrdLine + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CrossDockListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockListRow)
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
export function get_GetRows(whereClauseCrossDock:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCrossDock!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCrossDock=" + whereClauseCrossDock
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, warehouseCode:string, binNum:string, supplyJobNum:string, orderNum:string, orderLine:string, orderRelNum:string, jobNum:string, assemblySeq:string, mtlSeq:string, tfOrdNum:string, tfOrdLine:string, epicorHeaders?:Headers){
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
   if(typeof warehouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "warehouseCode=" + warehouseCode
   }
   if(typeof binNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "binNum=" + binNum
   }
   if(typeof supplyJobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "supplyJobNum=" + supplyJobNum
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
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof assemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assemblySeq=" + assemblySeq
   }
   if(typeof mtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mtlSeq=" + mtlSeq
   }
   if(typeof tfOrdNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tfOrdNum=" + tfOrdNum
   }
   if(typeof tfOrdLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tfOrdLine=" + tfOrdLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCrossDock
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCrossDock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCrossDock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCrossDock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCrossDock(requestBody:GetNewCrossDock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCrossDock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetNewCrossDock", {
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
         resolve(data as GetNewCrossDock_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CrossDockListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CrossDockRow,
}

export interface Erp_Tablesets_CrossDockListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part number that the cross dock is for.  */  
   "PartNum":string,
      /**  Warehouse that is quantity cross docked is being supplied from.  */  
   "WarehouseCode":string,
      /**  Warehouse Bin number  */  
   "BinNum":string,
      /**  Job that is supplying the cross docked quantity  */  
   "SupplyJobNum":string,
      /**  Order number of the order release that is cross docked.  */  
   "OrderNum":number,
      /**  Order line number of the order release that is cross docked.  */  
   "OrderLine":number,
      /**  Order release number of the order release that is cross docked.  */  
   "OrderRelNum":number,
      /**  Job number of the JobMtl/JobAsmbl that is cross docked.  */  
   "JobNum":string,
      /**  Assembly number of the JobMtl/JobAsmbl that is cross docked.  */  
   "AssemblySeq":number,
      /**  Material sequence number of the JobMtl that is cross docked.  */  
   "MtlSeq":number,
      /**  Transfer Order that is cross docked.  */  
   "TFOrdNum":string,
      /**  Transfer Order Line that is cross docked.  */  
   "TFOrdLine":number,
      /**  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  */  
   "CrossDockedQty":number,
      /**  Unit of measure (how it is cross docked).  */  
   "CrossDockedUM":string,
      /**  The To Site for a Transfer Order Cross Dock.  */  
   "ToPlant":string,
      /**  The From Site for a Transfer Order Cross Dock.  */  
   "FromPlant":string,
      /**  Creation date  */  
   "CreateDate":string,
      /**  Is this Cross Dock transaction a result of a Buy To Order transaction?  */  
   "BuyToOrder":boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   "CustID":string,
      /**  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  */  
   "Priority":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   "AssignEmpID":string,
      /**  Warehouse Group Identifier.  */  
   "WhseGroupCode":string,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   "OnHold":boolean,
      /**  The allocated demand is ready to be Released to Picking.  */  
   "ReleaseToPicking":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CrossDockedAttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "CrossDockedRevisionNum":string,
   "CommitedQty":number,
      /**  valid values: Order, Job or Transfer.  */  
   "DemandType":string,
      /**  Description of Demand Type code.  */  
   "DemandTypeDesc":string,
      /**  HH:MM:SS Format of System Time.  */  
   "DispSysTime":string,
   "TFOrdNumTFOrdLine":number,
   "TranType":string,
   "SalesOrderLineRelease":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CrossDockRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part number that the cross dock is for.  */  
   "PartNum":string,
      /**  Warehouse that is quantity cross docked is being supplied from.  */  
   "WarehouseCode":string,
      /**  Warehouse Bin number  */  
   "BinNum":string,
      /**  Job that is supplying the cross docked quantity  */  
   "SupplyJobNum":string,
      /**  Order number of the order release that is cross docked.  */  
   "OrderNum":number,
      /**  Order line number of the order release that is cross docked.  */  
   "OrderLine":number,
      /**  Order release number of the order release that is cross docked.  */  
   "OrderRelNum":number,
      /**  Job number of the JobMtl/JobAsmbl that is cross docked.  */  
   "JobNum":string,
      /**  Assembly number of the JobMtl/JobAsmbl that is cross docked.  */  
   "AssemblySeq":number,
      /**  Material sequence number of the JobMtl that is cross docked.  */  
   "MtlSeq":number,
      /**  Transfer Order that is cross docked.  */  
   "TFOrdNum":string,
      /**  Transfer Order Line that is cross docked.  */  
   "TFOrdLine":number,
      /**  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  */  
   "CrossDockedQty":number,
      /**  Unit of measure (how it is cross docked).  */  
   "CrossDockedUM":string,
      /**  The To Site for a Transfer Order Cross Dock.  */  
   "ToPlant":string,
      /**  The From Site for a Transfer Order Cross Dock.  */  
   "FromPlant":string,
      /**  Creation date  */  
   "CreateDate":string,
      /**  Creation Time  */  
   "CreateTime":number,
      /**  Is this Cross Dock transaction a result of a Buy To Order transaction?  */  
   "BuyToOrder":boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   "CustID":string,
      /**  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  */  
   "Priority":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   "DistributionType":string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   "AssignEmpID":string,
      /**  Warehouse Group Identifier.  */  
   "WhseGroupCode":string,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   "OnHold":boolean,
      /**  The allocated demand is ready to be Released to Picking.  */  
   "ReleaseToPicking":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "CrossDockedAttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "CrossDockedRevisionNum":string,
   "CommittedQty":number,
      /**  valid values: Order, Job or Transfer  */  
   "DemandType":string,
      /**  Description of Demand Type Code.  */  
   "DemandTypeDesc":string,
      /**  HH:MM:SS format of system time.  */  
   "DispSysTime":string,
   "TFOrdNumTFOrdLine":number,
      /**  Transaction Type  */  
   "TranType":string,
   "SalesOrderLineRelease":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "PartPartDescription":string,
   "PartAttrClassID":string,
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
      @param partNum
      @param warehouseCode
      @param binNum
      @param supplyJobNum
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param jobNum
      @param assemblySeq
      @param mtlSeq
      @param tfOrdNum
      @param tfOrdLine
   */  
export interface DeleteByID_input{
   partNum:string,
   warehouseCode:string,
   binNum:string,
   supplyJobNum:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   jobNum:string,
   assemblySeq:number,
   mtlSeq:number,
   tfOrdNum:string,
   tfOrdLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CrossDockListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part number that the cross dock is for.  */  
   PartNum:string,
      /**  Warehouse that is quantity cross docked is being supplied from.  */  
   WarehouseCode:string,
      /**  Warehouse Bin number  */  
   BinNum:string,
      /**  Job that is supplying the cross docked quantity  */  
   SupplyJobNum:string,
      /**  Order number of the order release that is cross docked.  */  
   OrderNum:number,
      /**  Order line number of the order release that is cross docked.  */  
   OrderLine:number,
      /**  Order release number of the order release that is cross docked.  */  
   OrderRelNum:number,
      /**  Job number of the JobMtl/JobAsmbl that is cross docked.  */  
   JobNum:string,
      /**  Assembly number of the JobMtl/JobAsmbl that is cross docked.  */  
   AssemblySeq:number,
      /**  Material sequence number of the JobMtl that is cross docked.  */  
   MtlSeq:number,
      /**  Transfer Order that is cross docked.  */  
   TFOrdNum:string,
      /**  Transfer Order Line that is cross docked.  */  
   TFOrdLine:number,
      /**  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  */  
   CrossDockedQty:number,
      /**  Unit of measure (how it is cross docked).  */  
   CrossDockedUM:string,
      /**  The To Site for a Transfer Order Cross Dock.  */  
   ToPlant:string,
      /**  The From Site for a Transfer Order Cross Dock.  */  
   FromPlant:string,
      /**  Creation date  */  
   CreateDate:string,
      /**  Is this Cross Dock transaction a result of a Buy To Order transaction?  */  
   BuyToOrder:boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  */  
   Priority:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   AssignEmpID:string,
      /**  Warehouse Group Identifier.  */  
   WhseGroupCode:string,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   OnHold:boolean,
      /**  The allocated demand is ready to be Released to Picking.  */  
   ReleaseToPicking:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CrossDockedAttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   CrossDockedRevisionNum:string,
   CommitedQty:number,
      /**  valid values: Order, Job or Transfer.  */  
   DemandType:string,
      /**  Description of Demand Type code.  */  
   DemandTypeDesc:string,
      /**  HH:MM:SS Format of System Time.  */  
   DispSysTime:string,
   TFOrdNumTFOrdLine:number,
   TranType:string,
   SalesOrderLineRelease:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CrossDockListTableset{
   CrossDockList:Erp_Tablesets_CrossDockListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CrossDockRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part number that the cross dock is for.  */  
   PartNum:string,
      /**  Warehouse that is quantity cross docked is being supplied from.  */  
   WarehouseCode:string,
      /**  Warehouse Bin number  */  
   BinNum:string,
      /**  Job that is supplying the cross docked quantity  */  
   SupplyJobNum:string,
      /**  Order number of the order release that is cross docked.  */  
   OrderNum:number,
      /**  Order line number of the order release that is cross docked.  */  
   OrderLine:number,
      /**  Order release number of the order release that is cross docked.  */  
   OrderRelNum:number,
      /**  Job number of the JobMtl/JobAsmbl that is cross docked.  */  
   JobNum:string,
      /**  Assembly number of the JobMtl/JobAsmbl that is cross docked.  */  
   AssemblySeq:number,
      /**  Material sequence number of the JobMtl that is cross docked.  */  
   MtlSeq:number,
      /**  Transfer Order that is cross docked.  */  
   TFOrdNum:string,
      /**  Transfer Order Line that is cross docked.  */  
   TFOrdLine:number,
      /**  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  */  
   CrossDockedQty:number,
      /**  Unit of measure (how it is cross docked).  */  
   CrossDockedUM:string,
      /**  The To Site for a Transfer Order Cross Dock.  */  
   ToPlant:string,
      /**  The From Site for a Transfer Order Cross Dock.  */  
   FromPlant:string,
      /**  Creation date  */  
   CreateDate:string,
      /**  Creation Time  */  
   CreateTime:number,
      /**  Is this Cross Dock transaction a result of a Buy To Order transaction?  */  
   BuyToOrder:boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  */  
   Priority:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   AssignEmpID:string,
      /**  Warehouse Group Identifier.  */  
   WhseGroupCode:string,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   OnHold:boolean,
      /**  The allocated demand is ready to be Released to Picking.  */  
   ReleaseToPicking:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CrossDockedAttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   CrossDockedRevisionNum:string,
   CommittedQty:number,
      /**  valid values: Order, Job or Transfer  */  
   DemandType:string,
      /**  Description of Demand Type Code.  */  
   DemandTypeDesc:string,
      /**  HH:MM:SS format of system time.  */  
   DispSysTime:string,
   TFOrdNumTFOrdLine:number,
      /**  Transaction Type  */  
   TranType:string,
   SalesOrderLineRelease:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartPartDescription:string,
   PartAttrClassID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CrossDockTableset{
   CrossDock:Erp_Tablesets_CrossDockRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCrossDockTableset{
   CrossDock:Erp_Tablesets_CrossDockRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param warehouseCode
      @param binNum
      @param supplyJobNum
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param jobNum
      @param assemblySeq
      @param mtlSeq
      @param tfOrdNum
      @param tfOrdLine
   */  
export interface GetByID_input{
   partNum:string,
   warehouseCode:string,
   binNum:string,
   supplyJobNum:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   jobNum:string,
   assemblySeq:number,
   mtlSeq:number,
   tfOrdNum:string,
   tfOrdLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CrossDockTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CrossDockTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CrossDockTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
      /**  Description List  */  
   returnObj:string,
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
   returnObj:Erp_Tablesets_CrossDockListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param warehouseCode
      @param binNum
      @param supplyJobNum
      @param orderNum
      @param orderLine
      @param orderRelNum
      @param jobNum
      @param assemblySeq
      @param mtlSeq
      @param tfOrdNum
   */  
export interface GetNewCrossDock_input{
   ds:Erp_Tablesets_CrossDockTableset[],
   partNum:string,
   warehouseCode:string,
   binNum:string,
   supplyJobNum:string,
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
   jobNum:string,
   assemblySeq:number,
   mtlSeq:number,
   tfOrdNum:string,
}

export interface GetNewCrossDock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CrossDockTableset,
}
}

   /** Required : 
      @param whereClauseCrossDock
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCrossDock:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CrossDockTableset[],
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
   ds:Erp_Tablesets_UpdExtCrossDockTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCrossDockTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CrossDockTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CrossDockTableset,
}
}

