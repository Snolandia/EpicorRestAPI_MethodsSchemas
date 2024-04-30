import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CCDtlSearchSvc
// Description: Special Search to be used by the tracker to fill the CCDtl data
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/$metadata", {
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
   Description: Get CCDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlRow
   */  
export function get_CCDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/CCDtlSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCDtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CCDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCDtlSearches(requestBody:Erp_Tablesets_CCDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/CCDtlSearches", {
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
   Summary: Calls GetByID to retrieve the CCDtlSearch item
   Description: Calls GetByID to retrieve the CCDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CCDtlRow
   */  
export function get_CCDtlSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/CCDtlSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
         resolve(data as Erp_Tablesets_CCDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCDtlSearch for the service
   Description: Calls UpdateExt to update CCDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCDtlSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, requestBody:Erp_Tablesets_CCDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/CCDtlSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
   Summary: Call UpdateExt to delete CCDtlSearch item
   Description: Call UpdateExt to delete CCDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param CCYear Desc: CCYear   Required: True
      @param CCMonth Desc: CCMonth   Required: True
      @param FullPhysical Desc: FullPhysical   Required: True
      @param CycleSeq Desc: CycleSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCDtlSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq_PartNum_AttributeSetID(Company:string, Plant:string, WarehouseCode:string, CCYear:string, CCMonth:string, FullPhysical:string, CycleSeq:string, PartNum:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/CCDtlSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + "," + PartNum + "," + AttributeSetID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlListRow)
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
export function get_GetRows(whereClauseCCDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCCDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCDtl=" + whereClauseCCDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, warehouseCode:string, ccYear:string, ccMonth:string, fullPhysical:string, cycleSeq:string, partNum:string, attributeSetID:string, epicorHeaders?:Headers){
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
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof attributeSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attributeSetID=" + attributeSetID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetCountHistoryData
   Description: Retrieves Count History related to a Part
   OperationID: GetCountHistoryData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCountHistoryData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCountHistoryData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCountHistoryData(requestBody:GetCountHistoryData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCountHistoryData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetCountHistoryData", {
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
         resolve(data as GetCountHistoryData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCCDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCCDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCDtl(requestBody:GetNewCCDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCCDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetNewCCDtl", {
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
         resolve(data as GetNewCCDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CCDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCDtlRow,
}

export interface Erp_Tablesets_CCDtlListRow{
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
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   "AllocationVariance":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  Part Number selected for counting.  */  
   "PartNum":string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   "TotFrozenVal":number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   "TotFrozenQOH":number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   "PostStatus":number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   "CDRCode":string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   "TotCountVal":number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   "TotCountQOH":number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   "DateRemoved":string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   "RemovedBy":string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   "MoveToCycle":string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "PcntTolerance":number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCCode":string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyToleranceUsed":boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   "PcntToleranceUsed":boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   "ValToleranceUsed":boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   "QtyAdjTolerance":number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   "VarToleranceStat":number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   "PostAdjustment":number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyTolerance":number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   "ValueTolerance":number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "BaseUOM":string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   "TotActivityBeforeCount":number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   "TotActivityBeforeVal":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   "AddedByBlankTag":boolean,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCSeq":number,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   "VoidPartTags":boolean,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   "EnableCDRCode":boolean,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   "VarToleranceStatDesc":string,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   "MovePart":boolean,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   "QtyVariance":number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   "ValueVariance":number,
      /**  Moved to Month  */  
   "MovedToMonth":number,
      /**  Moved to Year  */  
   "MovedToYear":number,
      /**  Moved To Cycle Seq  */  
   "MovedToCycleSeq":number,
      /**  Post Status Description  */  
   "PostStatusDesc":string,
      /**  Month name of MonthToMonth field  */  
   "MoveToMonthName":string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   "QtyAdjustmentStatus":string,
      /**  Defines the start date of the count period  */  
   "CCPeriodDefnPeriodStart":string,
      /**  Unique period description assigned by the user.  */  
   "CCPeriodDefnPeriodDesc":string,
      /**  Defines the end date of the period  */  
   "CCPeriodDefnPeriodEnd":string,
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
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**  Description.  */  
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCDtlRow{
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
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   "AllocationVariance":boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   "CycleSeq":number,
      /**  Part Number selected for counting.  */  
   "PartNum":string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   "TotFrozenVal":number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   "TotFrozenQOH":number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   "PostStatus":number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   "CDRCode":string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   "TotCountVal":number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   "TotCountQOH":number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   "DateRemoved":string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   "RemovedBy":string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   "MoveToCycle":string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "PcntTolerance":number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCCode":string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyToleranceUsed":boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   "PcntToleranceUsed":boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   "ValToleranceUsed":boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   "QtyAdjTolerance":number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   "VarToleranceStat":number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   "PostAdjustment":number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   "QtyTolerance":number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   "ValueTolerance":number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "BaseUOM":string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   "TotActivityBeforeCount":number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   "TotActivityBeforeVal":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   "AddedByBlankTag":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   "ABCSeq":number,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   "EnableCDRCode":boolean,
      /**  Moved To Cycle Seq  */  
   "MovedToCycleSeq":number,
      /**  Moved to Month  */  
   "MovedToMonth":number,
      /**  Moved to Year  */  
   "MovedToYear":number,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   "MovePart":boolean,
      /**  Month name of MonthToMonth field  */  
   "MoveToMonthName":string,
      /**  Post Status Description  */  
   "PostStatusDesc":string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   "QtyAdjustmentStatus":string,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   "QtyVariance":number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   "ValueVariance":number,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   "VarToleranceStatDesc":string,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   "VoidPartTags":boolean,
      /**  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  */  
   "AddAllAttributeSets":boolean,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "EnableAttributeSetSearch":boolean,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
   "BitFlag":number,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodStart":string,
   "CCPeriodDefnPeriodEnd":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryByRevision":boolean,
   "ReasonDescription":string,
   "WarehseDescription":string,
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
      @param partNum
      @param attributeSetID
   */  
export interface DeleteByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
   partNum:string,
   attributeSetID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CCDtlListRow{
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
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   AllocationVariance:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   TotFrozenVal:number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   TotFrozenQOH:number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   PostStatus:number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   CDRCode:string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   TotCountVal:number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   TotCountQOH:number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   DateRemoved:string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   RemovedBy:string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   MoveToCycle:string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   PcntTolerance:number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCCode:string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyToleranceUsed:boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   PcntToleranceUsed:boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   ValToleranceUsed:boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   QtyAdjTolerance:number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   VarToleranceStat:number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   PostAdjustment:number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyTolerance:number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   ValueTolerance:number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   BaseUOM:string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   TotActivityBeforeCount:number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   TotActivityBeforeVal:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   AddedByBlankTag:boolean,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCSeq:number,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   VoidPartTags:boolean,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   EnableCDRCode:boolean,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   VarToleranceStatDesc:string,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   MovePart:boolean,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   QtyVariance:number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   ValueVariance:number,
      /**  Moved to Month  */  
   MovedToMonth:number,
      /**  Moved to Year  */  
   MovedToYear:number,
      /**  Moved To Cycle Seq  */  
   MovedToCycleSeq:number,
      /**  Post Status Description  */  
   PostStatusDesc:string,
      /**  Month name of MonthToMonth field  */  
   MoveToMonthName:string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   QtyAdjustmentStatus:string,
      /**  Defines the start date of the count period  */  
   CCPeriodDefnPeriodStart:string,
      /**  Unique period description assigned by the user.  */  
   CCPeriodDefnPeriodDesc:string,
      /**  Defines the end date of the period  */  
   CCPeriodDefnPeriodEnd:string,
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
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**  Description.  */  
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCDtlListTableset{
   CCDtlList:Erp_Tablesets_CCDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCDtlRow{
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
      /**  If the count of this part has a variance, and the part is allocated to a sales order, job or transfer order, this Allocation Variance flag will be set to TRUE.  */  
   AllocationVariance:boolean,
      /**  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  */  
   CycleSeq:number,
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  Total cost of the part at the time the inventory quantity was frozen, based on the frozen bin/lot quantity and the frozen cost of each bin/lot. Updated at the time the counts are posted.  */  
   TotFrozenVal:number,
      /**  Total quantity on hand in the warehouse at the time the inventory was frozen . Updated at the time the counts are posted. This quantity is expressed in the Part base UOM  */  
   TotFrozenQOH:number,
      /**   The posting status of the part. 1 = the count for this part has been processed by the post final counts process, inventory adjustments were made.
2= the count for this part has been processed by the post final counts process and inventory adjustments were not made (no differences between count and frozen, or part was within Quantity Adjustment Tolerance)
 3= part was removed from the cycle after tags were generated, no posting required. 
Code/Desc:
0 ? Not posted
1 ? Adjustment posted
2 = No Adjustment required
3 = Voided  */  
   PostStatus:number,
      /**  If the count/recount of the part is outside of tolerance, this reason code is required before the counts will be posted.  */  
   CDRCode:string,
      /**  Total cost of the part at the time the final count was posted, based on the counted bin/lot quantity and the frozen cost of each bin/lot.  */  
   TotCountVal:number,
      /**  New on hand in the warehouse after the final count was posted This quantity is expressed in the Part base UOM.  */  
   TotCountQOH:number,
      /**  The date the part was removed from  the cycle. (PostStatus=3)  */  
   DateRemoved:string,
      /**  This is the user id of the person that removed the part from the cycle (PostStatus=3)  */  
   RemovedBy:string,
      /**  There will be data here only if PostStatus =3 and the part was moved to another cycle at the time the tags were voided. The format will be YYYY*MM*CycleSeq where CycleSeq is the cycle the part was moved to.  */  
   MoveToCycle:string,
      /**  This is the percent tolerance that was used for this part for this cycle cycle if PcntToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   PcntTolerance:number,
      /**  ABC Code for the part. Used in during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCCode:string,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyToleranceUsed:boolean,
      /**  Indicates whether a PcntTolerance was used by the cycle count variance report.  */  
   PcntToleranceUsed:boolean,
      /**  Indicates whether a ValtTolerance was used by the cycle count variance report.  */  
   ValToleranceUsed:boolean,
      /**  This is the quantity adjustment  tolerance that was used for this part for this cycle. If zero all quantity adjustments will be posted. This data is created by the cycle count variance report process.  */  
   QtyAdjTolerance:number,
      /**   Variance tolerance status. Indicates whether the counted qty for the part is within all variance tolerance parameters. 0 = tolerance has not yet been evaluated by the variance process.
1= the item is in tolerance.
2 =  the item is out of tolerance
This data is created by the cycle count variance report process. It is cleared if the part is selected for recount. The data is used by the posting process to determine if a CDR is required before posting. The posting process will not process this part if the value is zero.
Code/Desc:
0 = Not yet evaluated
1 = In tolerance
2 = Out of tolerance  */  
   VarToleranceStat:number,
      /**   This data is created by the cycle count variance report process.  It is cleared if the part is selected for recount. The data is used by the posting process to determine whether to post adjustments to inventory.
0 = tolerance has not yet been evaluated by the variance process.
1 = the part is within tolerance per the qty adjustment tolerance and no quantity adjustments should be posted.
2 = the part is outside of qty adjustment tolerance and adjustments should be posted

0 = Not yet evaluated
1 = Adjustment will not post
2 = Adjustment will post  */  
   PostAdjustment:number,
      /**  This is the quantity tolerance that was used for this part for this cycle if QtyToleranceUsed = true. This data is created by the cycle count variance report process.  */  
   QtyTolerance:number,
      /**  This is the value tolerance that was used for this part for this cycle if ValToleranceUsed = trueThis data is created by the cycle count variance report process.  */  
   ValueTolerance:number,
      /**  The Base UOM for this part. All qty fields in this record are expressed in this UOM.Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   BaseUOM:string,
      /**  Total ActivityBeforeCount for related CCTag records. Updated at the time the counts are posted. This quantity is expressed in the Part base UOM.  */  
   TotActivityBeforeCount:number,
      /**  Total ActivityBeforeValue for related CCTag records. Updated at the time the counts are posted..  */  
   TotActivityBeforeVal:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  True indicates this part was added to the physical Inventory cycle during count entry using a blank tag. Counts and inventory adjustments for the part will be made based only on the blank tags entered for the part, regardless of what other bins/lots/serial numbers, etc may exist for the part in the warehouse at the time of posting the counts for the part. This is only possible for a physical inventory count.  */  
   AddedByBlankTag:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  External field used during Part Selection for Random method only to help with the ?randomizing? if the number of pats due for cycle count for an ABC code exceeds the CCWhsABC.QtyToSelect for the CCWhsCtrl  */  
   ABCSeq:number,
      /**  Indicates wheter this CCDtl can have a CDR Code entered for it.  */  
   EnableCDRCode:boolean,
      /**  Moved To Cycle Seq  */  
   MovedToCycleSeq:number,
      /**  Moved to Month  */  
   MovedToMonth:number,
      /**  Moved to Year  */  
   MovedToYear:number,
      /**  Indicates whether the CCDtl was selected for move or delete in Cycle Count Part Selection Update  */  
   MovePart:boolean,
      /**  Month name of MonthToMonth field  */  
   MoveToMonthName:string,
      /**  Post Status Description  */  
   PostStatusDesc:string,
      /**  Its value is derived from PostAdjustment field value: 0-Not Yet Evaluated,1-Adjustment Will Not Post,2-Adjustment Will Post"  */  
   QtyAdjustmentStatus:string,
      /**  Qty Variance Value = TotCountQOH - (TotFrozenQOH + TotActivityBeforeCount)  */  
   QtyVariance:number,
      /**  Value Variance = TotCountVal - (TotFrozenVal + TotActivityBeforeVal)  */  
   ValueVariance:number,
      /**  Description of the CCDtl.VarToleranceStat; based on CCDtl.VarToleranceStat code/desc settings  */  
   VarToleranceStatDesc:string,
      /**  External field used to indicate that the VoidTagsByPart processing should be done for this part.  */  
   VoidPartTags:boolean,
      /**  Used in Cycle Count Part Selection update to indicate all attribute sets for an attribute set tracked part should be added to the cycle.  */  
   AddAllAttributeSets:boolean,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   EnableAttributeSetSearch:boolean,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   BitFlag:number,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodStart:string,
   CCPeriodDefnPeriodEnd:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryByRevision:boolean,
   ReasonDescription:string,
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCDtlSearchTableset{
   CCDtl:Erp_Tablesets_CCDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCCDtlSearchTableset{
   CCDtl:Erp_Tablesets_CCDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param ccYear
      @param ccMonth
      @param fullPhysical
      @param cycleSeq
      @param partNum
      @param attributeSetID
   */  
export interface GetByID_input{
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
   partNum:string,
   attributeSetID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CCDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CCDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CCDtlSearchTableset[],
}

   /** Required : 
      @param partNum
   */  
export interface GetCountHistoryData_input{
      /**  Part Number  */  
   partNum:string,
}

export interface GetCountHistoryData_output{
   returnObj:Erp_Tablesets_CCDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_CCDtlListTableset[],
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
      @param cycleSeq
      @param partNum
   */  
export interface GetNewCCDtl_input{
   ds:Erp_Tablesets_CCDtlSearchTableset[],
   plant:string,
   warehouseCode:string,
   ccYear:number,
   ccMonth:number,
   fullPhysical:boolean,
   cycleSeq:number,
   partNum:string,
}

export interface GetNewCCDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCDtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseCCDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCCDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CCDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtCCDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCCDtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CCDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CCDtlSearchTableset,
}
}

