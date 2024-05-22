import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.InventoryAdvisorSvc
// Description: InventoryAdvisorSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/$metadata", {
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
   Description: Get InventoryAdvisors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InventoryAdvisors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartQtyAttrRow
   */  
export function get_InventoryAdvisors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InventoryAdvisors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartQtyAttrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartQtyAttrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InventoryAdvisors(requestBody:Erp_Tablesets_PartQtyAttrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors", {
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
   Summary: Calls GetByID to retrieve the InventoryAdvisor item
   Description: Calls GetByID to retrieve the InventoryAdvisor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InventoryAdvisor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartQtyAttrRow
   */  
export function get_InventoryAdvisors_Company_PartNum_WarehouseCode_DimCode_AttributeSetID(Company:string, PartNum:string, WarehouseCode:string, DimCode:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartQtyAttrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors(" + Company + "," + PartNum + "," + WarehouseCode + "," + DimCode + "," + AttributeSetID + ")", {
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
         resolve(data as Erp_Tablesets_PartQtyAttrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InventoryAdvisor for the service
   Description: Calls UpdateExt to update InventoryAdvisor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InventoryAdvisor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartQtyAttrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InventoryAdvisors_Company_PartNum_WarehouseCode_DimCode_AttributeSetID(Company:string, PartNum:string, WarehouseCode:string, DimCode:string, AttributeSetID:string, requestBody:Erp_Tablesets_PartQtyAttrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors(" + Company + "," + PartNum + "," + WarehouseCode + "," + DimCode + "," + AttributeSetID + ")", {
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
   Summary: Call UpdateExt to delete InventoryAdvisor item
   Description: Call UpdateExt to delete InventoryAdvisor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InventoryAdvisor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InventoryAdvisors_Company_PartNum_WarehouseCode_DimCode_AttributeSetID(Company:string, PartNum:string, WarehouseCode:string, DimCode:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/InventoryAdvisors(" + Company + "," + PartNum + "," + WarehouseCode + "," + DimCode + "," + AttributeSetID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartQtyAttrListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrListRow)
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
export function get_GetRows(whereClausePartQtyAttr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartQtyAttr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartQtyAttr=" + whereClausePartQtyAttr
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, warehouseCode:string, dimCode:string, attributeSetID:string, epicorHeaders?:Headers){
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
   if(typeof dimCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dimCode=" + dimCode
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetList" + params, {
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
   Summary: Invoke method AddToQuote
   Description: Updates existing Quote with search results from the InventoryAdvisor BO
   OperationID: AddToQuote
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddToQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddToQuote(requestBody:AddToQuote_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddToQuote_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/AddToQuote", {
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
         resolve(data as AddToQuote_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddToQuoteInventoryDynAttrValues
   Description: Updates existing Quote with search results from the InventoryAdvisor BO
   OperationID: AddToQuoteInventoryDynAttrValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddToQuoteInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToQuoteInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddToQuoteInventoryDynAttrValues(requestBody:AddToQuoteInventoryDynAttrValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddToQuoteInventoryDynAttrValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/AddToQuoteInventoryDynAttrValues", {
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
         resolve(data as AddToQuoteInventoryDynAttrValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateQuote
   Description: Creates a new Quote and adds lines based on the search results from the InventoryAdvisor BO
   OperationID: CreateQuote
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateQuote(requestBody:CreateQuote_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateQuote_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/CreateQuote", {
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
         resolve(data as CreateQuote_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateQuoteInventoryDynAttrValues
   OperationID: CreateQuoteInventoryDynAttrValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateQuoteInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateQuoteInventoryDynAttrValues(requestBody:CreateQuoteInventoryDynAttrValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateQuoteInventoryDynAttrValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/CreateQuoteInventoryDynAttrValues", {
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
         resolve(data as CreateQuoteInventoryDynAttrValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddToSalesOrder
   Description: Updates existing Sales Order with search results from the InventoryAdvisor BO
   OperationID: AddToSalesOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddToSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddToSalesOrder(requestBody:AddToSalesOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddToSalesOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/AddToSalesOrder", {
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
         resolve(data as AddToSalesOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddToSalesOrderInventoryDynAttrValues
   OperationID: AddToSalesOrderInventoryDynAttrValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddToSalesOrderInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddToSalesOrderInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddToSalesOrderInventoryDynAttrValues(requestBody:AddToSalesOrderInventoryDynAttrValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddToSalesOrderInventoryDynAttrValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/AddToSalesOrderInventoryDynAttrValues", {
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
         resolve(data as AddToSalesOrderInventoryDynAttrValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSalesOrder
   Description: Creates a new Sales Order and adds lines based on the search results from the InventoryAdvisor BO
   OperationID: CreateSalesOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSalesOrder(requestBody:CreateSalesOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSalesOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/CreateSalesOrder", {
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
         resolve(data as CreateSalesOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSalesOrderInventoryDynAttrValues
   Description: Creates a new Sales Order and adds lines based on the search results from the InventoryAdvisor BO
   OperationID: CreateSalesOrderInventoryDynAttrValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSalesOrderInventoryDynAttrValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSalesOrderInventoryDynAttrValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSalesOrderInventoryDynAttrValues(requestBody:CreateSalesOrderInventoryDynAttrValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSalesOrderInventoryDynAttrValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/CreateSalesOrderInventoryDynAttrValues", {
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
         resolve(data as CreateSalesOrderInventoryDynAttrValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Number Of Pieces changes to calculate a new Action Quantity
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingSelectedForActionQty
   Description: Call this method when the Action Quantity changes to calculate a new Number Of Pieces
   OperationID: OnChangingSelectedForActionQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingSelectedForActionQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSelectedForActionQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSelectedForActionQty(requestBody:OnChangingSelectedForActionQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingSelectedForActionQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/OnChangingSelectedForActionQty", {
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
         resolve(data as OnChangingSelectedForActionQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsAdvanced
   Description: Get rows using additional search criteria and incorporate with Enterprise Search results
   OperationID: GetRowsAdvanced
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsAdvanced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsAdvanced_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsAdvanced(requestBody:GetRowsAdvanced_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsAdvanced_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetRowsAdvanced", {
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
         resolve(data as GetRowsAdvanced_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsInventoryAdvisor
   Description: Get rows using additional search criteria and incorporate with Enterprise Search results
   OperationID: GetRowsInventoryAdvisor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsInventoryAdvisor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsInventoryAdvisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsInventoryAdvisor(requestBody:GetRowsInventoryAdvisor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsInventoryAdvisor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetRowsInventoryAdvisor", {
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
         resolve(data as GetRowsInventoryAdvisor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsUsingSearchParams
   Description: Get rows using static Part Attributes and Dynamic Attributes and incorporate with Enterprise Search results
   OperationID: GetRowsUsingSearchParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsUsingSearchParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUsingSearchParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsUsingSearchParams(requestBody:GetRowsUsingSearchParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsUsingSearchParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetRowsUsingSearchParams", {
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
         resolve(data as GetRowsUsingSearchParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTableStructure
   Description: Builds dynamic DataTable structure based on class selected
   OperationID: GetTableStructure
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTableStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableStructure(requestBody:GetTableStructure_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTableStructure_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetTableStructure", {
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
         resolve(data as GetTableStructure_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByInventoryAdvisorSysRowIDs
   Description: Return result in dynamic DataTable based on InventoryAdvisor dataset
   OperationID: GetByInventoryAdvisorSysRowIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByInventoryAdvisorSysRowIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByInventoryAdvisorSysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByInventoryAdvisorSysRowIDs(requestBody:GetByInventoryAdvisorSysRowIDs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByInventoryAdvisorSysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetByInventoryAdvisorSysRowIDs", {
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
         resolve(data as GetByInventoryAdvisorSysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshInventoryAdvisor
   Description: Refresh Inventory Advisor using a list PartQtyAttr and Part SysRowIDs
   OperationID: RefreshInventoryAdvisor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshInventoryAdvisor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshInventoryAdvisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshInventoryAdvisor(requestBody:RefreshInventoryAdvisor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshInventoryAdvisor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/RefreshInventoryAdvisor", {
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
         resolve(data as RefreshInventoryAdvisor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshInventoryAdvisorFromDataset
   Description: Refresh Inventory Advisor using rows in the dataset
   OperationID: RefreshInventoryAdvisorFromDataset
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshInventoryAdvisorFromDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshInventoryAdvisorFromDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshInventoryAdvisorFromDataset(requestBody:RefreshInventoryAdvisorFromDataset_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshInventoryAdvisorFromDataset_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/RefreshInventoryAdvisorFromDataset", {
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
         resolve(data as RefreshInventoryAdvisorFromDataset_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAdvisorSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartQtyAttrListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartQtyAttrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartQtyAttrRow,
}

export interface Erp_Tablesets_PartQtyAttrListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Warehouse  */  
   "WarehouseCode":string,
      /**  UOM  */  
   "DimCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  */  
   "DemandQty":number,
      /**  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  */  
   "ReservedQty":number,
      /**  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  */  
   "AllocatedQty":number,
      /**  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  */  
   "PickingQty":number,
      /**  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  */  
   "PickedQty":number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   "OnHandQty":number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   "NonNettableQty":number,
      /**  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  */  
   "BuyToOrderQty":number,
      /**  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   "SalesDemandQty":number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesReservedQty":number,
      /**  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  */  
   "SalesAllocatedQty":number,
      /**  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickingQty":number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickedQty":number,
      /**  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  */  
   "JobDemandQty":number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   "JobReservedQty":number,
      /**  New in 9.00.  Summary of stock allocated for jobs.  */  
   "JobAllocatedQty":number,
      /**  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  */  
   "JobPickingQty":number,
      /**  Stock Quantity picked for jobs.  */  
   "JobPickedQty":number,
      /**  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  */  
   "UnfirmJobDemandQty":number,
      /**  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   "TFOrdDemandQty":number,
      /**  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  */  
   "TFOrdReservedQty":number,
      /**  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  */  
   "TFOrdAllocatedQty":number,
      /**  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  */  
   "TFOrdPickingQty":number,
      /**  Stock Quantity picked for transfer orders.  */  
   "TFOrdPickedQty":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Attribute Class that was selected in the Search.  */  
   "SearchParamAttrClassID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartQtyAttrRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number  */  
   "PartNum":string,
      /**  Warehouse  */  
   "WarehouseCode":string,
      /**  UOM  */  
   "DimCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  */  
   "DemandQty":number,
      /**  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  */  
   "ReservedQty":number,
      /**  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  */  
   "AllocatedQty":number,
      /**  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  */  
   "PickingQty":number,
      /**  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  */  
   "PickedQty":number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   "OnHandQty":number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   "NonNettableQty":number,
      /**  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  */  
   "BuyToOrderQty":number,
      /**  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   "SalesDemandQty":number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesReservedQty":number,
      /**  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  */  
   "SalesAllocatedQty":number,
      /**  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickingQty":number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickedQty":number,
      /**  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  */  
   "JobDemandQty":number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   "JobReservedQty":number,
      /**  New in 9.00.  Summary of stock allocated for jobs.  */  
   "JobAllocatedQty":number,
      /**  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  */  
   "JobPickingQty":number,
      /**  Stock Quantity picked for jobs.  */  
   "JobPickedQty":number,
      /**  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  */  
   "UnfirmJobDemandQty":number,
      /**  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   "TFOrdDemandQty":number,
      /**  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  */  
   "TFOrdReservedQty":number,
      /**  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  */  
   "TFOrdAllocatedQty":number,
      /**  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  */  
   "TFOrdPickingQty":number,
      /**  Stock Quantity picked for transfer orders.  */  
   "TFOrdPickedQty":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "ProdCodeDescription":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "ClassIDDescription":string,
   "SelectedForAction":boolean,
   "SelectedForActionQty":number,
   "PlantVendorID":string,
   "PlantVendorName":string,
   "PlantLeadTime":number,
      /**  Number of pieces for inventory attribute tracked parts as relates to On Hand Quantity.  */  
   "DispNumberOfPieces":number,
   "AvailableQty":number,
   "PlantName":string,
   "AttributeSetShortDescription":string,
   "AttrClassIDDescription":string,
      /**  Attribute Class that was selected in the Search.  */  
   "SearchParamAttrClassID":string,
      /**  Number of pieces for inventory attribute tracked parts as relates to Available Quantity.  */  
   "AvailableNbrPcs":number,
   "BitFlag":number,
   "AttributeSetIDRevisionNum":string,
   "AttributeSetIDDescription":string,
   "AttributeSetIDShortDescription":string,
   "PartNumIsSafetyItem":boolean,
   "PartNumUnitPrice":number,
   "PartNumIsGiftCard":boolean,
   "PartNumDiameterInside":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumAttrClassID":string,
   "PartNumDurometer":string,
   "PartNumSysRowID":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumProdCode":string,
   "PartNumCommercialColor":string,
   "PartNumPricePerCode":string,
   "PartNumDiameterUM":string,
   "PartNumPartHeight":number,
   "PartNumCondition":string,
   "PartNumDualUOMClassID":string,
   "PartNumCommercialBrand":string,
   "PartNumCommercialSubBrand":string,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumCommercialCategory":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumClassID":string,
   "PartNumPartLength":number,
   "PartNumIsRestricted":boolean,
   "PartNumCommentText":string,
   "PartNumCommercialSize1":string,
   "PartNumEngineeringAlert":string,
   "PartNumPartWidth":number,
   "PartNumTrackDimension":boolean,
   "PartNumCommercialSize2":string,
   "PartNumPartLengthWidthHeightUM":string,
   "PartNumCommercialSubCategory":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumDiameterOutside":number,
   "PartNumCommercialStyle":string,
   "PartNumSpecification":string,
   "PartNumThicknessUM":string,
   "PartNumIsCompliant":boolean,
   "PartNumThickness":number,
   "PartNumThicknessMax":number,
   "WarehouseCodeDescription":string,
   "WarehouseCodePlant":string,
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
      @param quoteNum
      @param ds
   */  
export interface AddToQuoteInventoryDynAttrValues_input{
   attrClassID:string,
   quoteNum:number,
   ds:any,      //schema had no properties on an object.
}

export interface AddToQuoteInventoryDynAttrValues_output{
}

   /** Required : 
      @param quoteNum
      @param ds
   */  
export interface AddToQuote_input{
   quoteNum:number,
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface AddToQuote_output{
}

   /** Required : 
      @param attrClassID
      @param orderNum
      @param ds
   */  
export interface AddToSalesOrderInventoryDynAttrValues_input{
   attrClassID:string,
   orderNum:number,
   ds:any,      //schema had no properties on an object.
}

export interface AddToSalesOrderInventoryDynAttrValues_output{
}

   /** Required : 
      @param orderNum
      @param ds
   */  
export interface AddToSalesOrder_input{
   orderNum:number,
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface AddToSalesOrder_output{
}

   /** Required : 
      @param attrClassID
      @param custID
      @param ds
   */  
export interface CreateQuoteInventoryDynAttrValues_input{
   attrClassID:string,
   custID:string,
   ds:any,      //schema had no properties on an object.
}

export interface CreateQuoteInventoryDynAttrValues_output{
}

   /** Required : 
      @param custID
      @param ds
   */  
export interface CreateQuote_input{
   custID:string,
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface CreateQuote_output{
}

   /** Required : 
      @param attrClassID
      @param custID
      @param ds
   */  
export interface CreateSalesOrderInventoryDynAttrValues_input{
   attrClassID:string,
   custID:string,
   ds:any,      //schema had no properties on an object.
}

export interface CreateSalesOrderInventoryDynAttrValues_output{
}

   /** Required : 
      @param custID
      @param ds
   */  
export interface CreateSalesOrder_input{
   custID:string,
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface CreateSalesOrder_output{
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
      /**  The actual generic table name used by the BL  */  
   DataTableID:string,
      /**  Unique identifier for the virtual schema  */  
   UniqueTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InventoryAdvisorListTableset{
   PartQtyAttrList:Erp_Tablesets_PartQtyAttrListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InventoryAdvisorTableset{
   PartQtyAttr:Erp_Tablesets_PartQtyAttrRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartQtyAttrListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Warehouse  */  
   WarehouseCode:string,
      /**  UOM  */  
   DimCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  */  
   DemandQty:number,
      /**  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  */  
   ReservedQty:number,
      /**  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  */  
   AllocatedQty:number,
      /**  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  */  
   PickingQty:number,
      /**  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  */  
   PickedQty:number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   OnHandQty:number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   NonNettableQty:number,
      /**  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  */  
   BuyToOrderQty:number,
      /**  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   SalesDemandQty:number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesReservedQty:number,
      /**  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  */  
   SalesAllocatedQty:number,
      /**  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickingQty:number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickedQty:number,
      /**  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  */  
   JobDemandQty:number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   JobReservedQty:number,
      /**  New in 9.00.  Summary of stock allocated for jobs.  */  
   JobAllocatedQty:number,
      /**  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  */  
   JobPickingQty:number,
      /**  Stock Quantity picked for jobs.  */  
   JobPickedQty:number,
      /**  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  */  
   UnfirmJobDemandQty:number,
      /**  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   TFOrdDemandQty:number,
      /**  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  */  
   TFOrdReservedQty:number,
      /**  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  */  
   TFOrdAllocatedQty:number,
      /**  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  */  
   TFOrdPickingQty:number,
      /**  Stock Quantity picked for transfer orders.  */  
   TFOrdPickedQty:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Attribute Class that was selected in the Search.  */  
   SearchParamAttrClassID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartQtyAttrRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Warehouse  */  
   WarehouseCode:string,
      /**  UOM  */  
   DimCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  A summary of demand.The system calculates Available Inventory as OnHandQty - DemandQty + BuyToOrderQty.  */  
   DemandQty:number,
      /**  A summary of the reserved quantities for order open sales releases, job materials, or transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of reservations in PartAlloc.  */  
   ReservedQty:number,
      /**  A summary of the allocated quantities for order open sales releases, job materials, and transfer orders for this Part within a specific warehouse. NOTE: This value is the TOTAL of allocation in PartAlloc.  */  
   AllocatedQty:number,
      /**  Quantity that is in the picking process for sales orders, job materials or transfer orders. A summary of PartAlloc.PickingQty for all demand.  */  
   PickingQty:number,
      /**  Stock Quantity picked for sales orders, job materials, and transfer orders.  A summary of PartAlloc.PickedQty for all demand.  */  
   PickedQty:number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  */  
   OnHandQty:number,
      /**  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  */  
   NonNettableQty:number,
      /**  A summary of Demand that is Buy To Order to be used in the calculations of the summary of Available Inventory.  */  
   BuyToOrderQty:number,
      /**  A summary of the outstanding quantities for order open sales releases that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   SalesDemandQty:number,
      /**  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesReservedQty:number,
      /**  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled from stock and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  */  
   SalesAllocatedQty:number,
      /**  Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0. A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickingQty:number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickedQty:number,
      /**  A summary of the outstanding quantities for job material requirements that are being filled from stock for this Part within a specific warehouse.  */  
   JobDemandQty:number,
      /**  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  */  
   JobReservedQty:number,
      /**  New in 9.00.  Summary of stock allocated for jobs.  */  
   JobAllocatedQty:number,
      /**  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  */  
   JobPickingQty:number,
      /**  Stock Quantity picked for jobs.  */  
   JobPickedQty:number,
      /**  New in 9.00.  Summary of mfg demand requirements on unfirm jobs. That is, a summary of outstanding JobMtl.RequiredQty and JobAsmbl.PullQty where JobHead.JobFirm = No.  */  
   UnfirmJobDemandQty:number,
      /**  A summary of the outstanding quantities for transfer order requirements that are being filled from stock for this Part within a specific warehouse. The system calculates Available as OnhandQty - AllocatedQty.  */  
   TFOrdDemandQty:number,
      /**  Summary of Transfer Order Reserved Qty for this Part in this Warehouse.  */  
   TFOrdReservedQty:number,
      /**  Summary of Transfer Order Allocated Qty for this Part in this Warehouse.  */  
   TFOrdAllocatedQty:number,
      /**  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  */  
   TFOrdPickingQty:number,
      /**  Stock Quantity picked for transfer orders.  */  
   TFOrdPickedQty:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   ProdCodeDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   ClassIDDescription:string,
   SelectedForAction:boolean,
   SelectedForActionQty:number,
   PlantVendorID:string,
   PlantVendorName:string,
   PlantLeadTime:number,
      /**  Number of pieces for inventory attribute tracked parts as relates to On Hand Quantity.  */  
   DispNumberOfPieces:number,
   AvailableQty:number,
   PlantName:string,
   AttributeSetShortDescription:string,
   AttrClassIDDescription:string,
      /**  Attribute Class that was selected in the Search.  */  
   SearchParamAttrClassID:string,
      /**  Number of pieces for inventory attribute tracked parts as relates to Available Quantity.  */  
   AvailableNbrPcs:number,
   BitFlag:number,
   AttributeSetIDRevisionNum:string,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   PartNumIsSafetyItem:boolean,
   PartNumUnitPrice:number,
   PartNumIsGiftCard:boolean,
   PartNumDiameterInside:number,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
   PartNumDurometer:string,
   PartNumSysRowID:string,
   PartNumTrackLots:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumProdCode:string,
   PartNumCommercialColor:string,
   PartNumPricePerCode:string,
   PartNumDiameterUM:string,
   PartNumPartHeight:number,
   PartNumCondition:string,
   PartNumDualUOMClassID:string,
   PartNumCommercialBrand:string,
   PartNumCommercialSubBrand:string,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumCommercialCategory:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumClassID:string,
   PartNumPartLength:number,
   PartNumIsRestricted:boolean,
   PartNumCommentText:string,
   PartNumCommercialSize1:string,
   PartNumEngineeringAlert:string,
   PartNumPartWidth:number,
   PartNumTrackDimension:boolean,
   PartNumCommercialSize2:string,
   PartNumPartLengthWidthHeightUM:string,
   PartNumCommercialSubCategory:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumDiameterOutside:number,
   PartNumCommercialStyle:string,
   PartNumSpecification:string,
   PartNumThicknessUM:string,
   PartNumIsCompliant:boolean,
   PartNumThickness:number,
   PartNumThicknessMax:number,
   WarehouseCodeDescription:string,
   WarehouseCodePlant:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtInventoryAdvisorTableset{
   PartQtyAttr:Erp_Tablesets_PartQtyAttrRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param warehouseCode
      @param dimCode
      @param attributeSetID
   */  
export interface GetByID_input{
   partNum:string,
   warehouseCode:string,
   dimCode:string,
   attributeSetID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
}

   /** Required : 
      @param attrClassID
      @param ds
      @param dynamicMetadataDS
   */  
export interface GetByInventoryAdvisorSysRowIDs_input{
   attrClassID:string,
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface GetByInventoryAdvisorSysRowIDs_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset,
}
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
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
   returnObj:Erp_Tablesets_InventoryAdvisorListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param startsWith
      @param partNum
      @param classID
      @param prodCode
      @param attrClassID
      @param attributeSetIDList
      @param searchText
      @param inStockOnly
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsAdvanced_input{
   startsWith:string,
   partNum:string,
   classID:string,
   prodCode:string,
   attrClassID:string,
   attributeSetIDList:number,
   searchText:string,
   inStockOnly:boolean,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsAdvanced_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param startsWith
      @param partNum
      @param classID
      @param prodCode
      @param attrClassID
      @param attributeSetIDList
      @param searchText
      @param inStockOnly
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsInventoryAdvisor_input{
   startsWith:string,
   partNum:string,
   classID:string,
   prodCode:string,
   attrClassID:string,
   attributeSetIDList:string,
   searchText:string,
   inStockOnly:boolean,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsInventoryAdvisor_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param partNum
      @param classID
      @param prodCode
      @param attrClassID
      @param partAttrListString
      @param dynAttrListString
      @param startsWith
      @param enterpriseSearchText
      @param inStockOnly
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsUsingSearchParams_input{
   partNum:string,
   classID:string,
   prodCode:string,
   attrClassID:string,
   partAttrListString:string,
   dynAttrListString:string,
   startsWith:string,
   enterpriseSearchText:string,
   inStockOnly:boolean,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsUsingSearchParams_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePartQtyAttr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartQtyAttr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param attrClassID
      @param dynamicMetadataDS
   */  
export interface GetTableStructure_input{
   attrClassID:string,
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface GetTableStructure_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   dynamicMetadataDS:Erp_Tablesets_DynamicMetadataTableset,
   displayAttrClassID:string,
   displayAttrClassIDDescription:string,
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
      @param attrClassID
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   attrClassID:string,
   numberOfPieces:number,
   ds:any,      //schema had no properties on an object.
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:any // UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param attrClassID
      @param selectedForActionQty
      @param ds
   */  
export interface OnChangingSelectedForActionQty_input{
   attrClassID:string,
   selectedForActionQty:number,
   ds:any,      //schema had no properties on an object.
}

export interface OnChangingSelectedForActionQty_output{
parameters : {
      /**  output parameters  */  
   ds:any // UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshInventoryAdvisorFromDataset_input{
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface RefreshInventoryAdvisorFromDataset_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
}

   /** Required : 
      @param partQtyAttrSysRowIDList
      @param partSysRowIDList
      @param ds
   */  
export interface RefreshInventoryAdvisor_input{
      /**  The list of rows with an associated PartQtyAttr record  */  
   partQtyAttrSysRowIDList:string,
      /**  The list of rows without an associated PartQtyAttr record  */  
   partSysRowIDList:string,
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface RefreshInventoryAdvisor_output{
   returnObj:Erp_Tablesets_InventoryAdvisorTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtInventoryAdvisorTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtInventoryAdvisorTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_InventoryAdvisorTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryAdvisorTableset,
}
}

