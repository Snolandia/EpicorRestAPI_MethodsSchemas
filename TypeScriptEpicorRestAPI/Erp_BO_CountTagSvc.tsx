import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CountTagSvc
// Description: Count Tag
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/$metadata", {
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
   Description: Get CountTags items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CountTags
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCTagRow
   */  
export function get_CountTags(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CountTags", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CountTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCTagRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCTagRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountTags(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CountTags", {
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
   Summary: Calls GetByID to retrieve the CountTag item
   Description: Calls GetByID to retrieve the CountTag item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CountTag
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param TagNum Desc: TagNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCTagRow
   */  
export function get_CountTags_Company_Plant_WarehouseCode_TagNum(Company:string, Plant:string, WarehouseCode:string, TagNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCTagRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CountTags(" + Company + "," + Plant + "," + WarehouseCode + "," + TagNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCTagRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CountTag for the service
   Description: Calls UpdateExt to update CountTag. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CountTag
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param TagNum Desc: TagNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCTagRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CountTags_Company_Plant_WarehouseCode_TagNum(Company:string, Plant:string, WarehouseCode:string, TagNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CountTags(" + Company + "," + Plant + "," + WarehouseCode + "," + TagNum + ")", {
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
   Summary: Call UpdateExt to delete CountTag item
   Description: Call UpdateExt to delete CountTag item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CountTag
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param TagNum Desc: TagNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CountTags_Company_Plant_WarehouseCode_TagNum(Company:string, Plant:string, WarehouseCode:string, TagNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CountTags(" + Company + "," + Plant + "," + WarehouseCode + "," + TagNum + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get CCTagWrkShts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCTagWrkShts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCTagWrkShtRow
   */  
export function get_CCTagWrkShts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagWrkShtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CCTagWrkShts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagWrkShtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCTagWrkShts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCTagWrkShtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCTagWrkShtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CCTagWrkShts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CCTagWrkShts", {
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
   Summary: Calls GetByID to retrieve the CCTagWrkSht item
   Description: Calls GetByID to retrieve the CCTagWrkSht item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCTagWrkSht
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCTagWrkShtRow
   */  
export function get_CCTagWrkShts_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CCTagWrkShtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CCTagWrkShts(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CCTagWrkShtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CCTagWrkSht for the service
   Description: Calls UpdateExt to update CCTagWrkSht. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCTagWrkSht
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCTagWrkShtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CCTagWrkShts_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CCTagWrkShts(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CCTagWrkSht item
   Description: Call UpdateExt to delete CCTagWrkSht item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCTagWrkSht
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CCTagWrkShts_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CCTagWrkShts(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCTagListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCCTag:string, whereClauseCCTagWrkSht:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCCTag!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCTag=" + whereClauseCCTag
   }
   if(typeof whereClauseCCTagWrkSht!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCCTagWrkSht=" + whereClauseCCTagWrkSht
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, warehouseCode:string, tagNum:string, epicorHeaders?:Headers){
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
   if(typeof tagNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tagNum=" + tagNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetList" + params, {
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
   Summary: Invoke method CalcCountedQty
   Description: Purpose:
Parameters:  none
Notes:
<param name="pQty">CCTag.CountedQty</param><param name="ds">The CountTag data set</param>
   OperationID: CalcCountedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcCountedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcCountedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcCountedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CalcCountedQty", {
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
   Summary: Invoke method CustomGetByID
   Description: This is a custome GetByID to be used when the user manually enters a tag number in count Tag Entry. It will ensure
that the tag belongs to the specific cycle that is selected in Count Tag Entry.
   OperationID: CustomGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomGetByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CustomGetByID", {
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
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetPartXRefInfo", {
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
   Summary: Invoke method GetUOMData
   Description: Purpose:     CCTagWrkSht
Parameters:  none
Notes:
<param name="ipPartNum">Proposed PartNum</param><param name="ds">The CountTag data set</param>
   OperationID: GetUOMData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUOMData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUOMData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUOMData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetUOMData", {
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
   Summary: Invoke method OnChangePCIDTagType
   Description: Call this method when user changes the PCID Tag Type.
   OperationID: OnChangePCIDTagType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDTagType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDTagType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDTagType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangePCIDTagType", {
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
   Summary: Invoke method OnChangeMoveToBinNum
   Description: Procedure that validates the Move To Bin Num
   OperationID: OnChangeMoveToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMoveToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMoveToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMoveToBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeMoveToBinNum", {
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
   Summary: Invoke method OnChangeBinNum
   Description: Procedure that validates the Bin Num
   OperationID: OnChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeBinNum", {
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
   Summary: Invoke method OnChangeCountedQty
   Description: Recalculate the CountedQty field.
   OperationID: OnChangeCountedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCountedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCountedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCountedQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeCountedQty", {
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
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangePartNum
   Description: CountTag - Call this method when the user changes the PartNum.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangePCID
   Description: Method that validates the PCID.
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangePCID", {
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
   Summary: Invoke method OnChangeItemPCID
   Description: Method that validates the Item PCID.
   OperationID: OnChangeItemPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeItemPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeItemPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeItemPCID", {
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
   Summary: Invoke method OnChangeUOM
   Description: CountTag - Call this method when the user changes the PartNum.
   OperationID: OnChangeUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeUOM", {
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
   Summary: Invoke method OnChangeAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangeAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeAttributeSet", {
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
   Summary: Invoke method OnChangeNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangeNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/OnChangeNumberOfPieces", {
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
   Summary: Invoke method ValidatePlant
   Description: Purpose:
Parameters:  none
Notes:
///
///
   OperationID: ValidatePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePlant(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/ValidatePlant", {
          method: 'post',
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
   Summary: Invoke method GenerateNestedTags
   Description: Purpose:
Parameters:  none
Notes:
///
///
   OperationID: GenerateNestedTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateNestedTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNestedTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateNestedTags(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GenerateNestedTags", {
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
   Summary: Invoke method GenerateTags
   Description: Purpose:
Parameters:  none
Notes:
///
///
   OperationID: GenerateTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateTags(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GenerateTags", {
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
   Summary: Invoke method getRelatedTagsWhereClause
   Description: Purpose:     get RelatedTags WhereClause
Parameters:  none
Notes:
<param name="ds">The CountTag data set</param>
   OperationID: getRelatedTagsWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getRelatedTagsWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getRelatedTagsWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getRelatedTagsWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/getRelatedTagsWhereClause", {
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
   Summary: Invoke method GetActivityWhereClause
   Description: Purpose:     Get Activity WhereClause
Parameters:  none
Notes:
<param name="seqStartDate" /><param name="seqTimeSeqStarted" /><param name="ds">The CountTag data set</param>
   OperationID: GetActivityWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActivityWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActivityWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActivityWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetActivityWhereClause", {
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
   Summary: Invoke method CalculateActivityBeforeCount
   Description: CalculateActivityBeforeCount
   OperationID: CalculateActivityBeforeCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateActivityBeforeCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateActivityBeforeCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateActivityBeforeCount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/CalculateActivityBeforeCount", {
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
   Summary: Invoke method GetSNTransWhereClause
   Description: GetSNTransWhereClause
   OperationID: GetSNTransWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSNTransWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSNTransWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSNTransWhereClause(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetSNTransWhereClause", {
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
   Summary: Invoke method GetNewCCTag
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCTag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCTag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCTag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCCTag(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetNewCCTag", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CountTagSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCTagListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCTagRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagWrkShtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CCTagWrkShtRow[],
}

export interface Erp_Tablesets_CCTagListRow{
      /**  Company Identifier.  */  
   "Company":string,
   "Bindesc":string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   "WarehouseCode":string,
      /**  Part Number selected for counting.  */  
   "PartNum":string,
      /**  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  */  
   "TagNum":string,
   "TagSelForVoid":boolean,
      /**  Bin number for the tag  */  
   "BinNum":string,
      /**  Person that counted the parts on the Count Tag.  */  
   "CountedBy":string,
   "WrehouseCode":string,
      /**  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  */  
   "CountedQty":number,
   "WarehseDesc":string,
      /**  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  */  
   "CountedTime":string,
      /**  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  */  
   "TagReturned":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The outermost PCID that contains this CCPDICTag.PCID  */  
   "TopLevelPCID":string,
      /**  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  */  
   "PCID":string,
      /**  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  */  
   "ItemPCID":string,
      /**  Tag Status Description  */  
   "TagStatusDesc":string,
      /**  Tag Type for PCID tag  */  
   "CCTagCharacter02":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "AttributeSetIDDescription":string,
   "AttributeSetIDShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCTagRow{
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
      /**  Part Number selected for counting.  */  
   "PartNum":string,
      /**  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  */  
   "TagNum":string,
      /**  Bin number for the tag  */  
   "BinNum":string,
      /**  Person that counted the parts on the Count Tag.  */  
   "CountedBy":string,
      /**  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  */  
   "CountedQty":number,
      /**  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  */  
   "CountedTime":string,
      /**  Tag Note  */  
   "TagNote":string,
      /**  This field is set equal to the Login ID variable.  System Set when a user enters a counted amount for the tag or voids the tag.  */  
   "EntryPerson":string,
      /**  Indicates that the Count Tag has been printed.  Manually entered tags are set to "Printed" when they are entered.  System Set.  */  
   "TagPrinted":boolean,
      /**  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  */  
   "TagReturned":boolean,
      /**  Date the count was performed.  */  
   "CountedDate":string,
      /**   Tag status.
Code/Desc:
0 = open
1 = posted
2 = voided 3=Closed/Recount.  */  
   "TagStatus":number,
      /**  True = this tag was generated as a blank tag. This will control whether bin/lot/serial data can be changed on the tag and whether the tag can be voided independent of other tags generated for an part.  */  
   "BlankTag":boolean,
      /**  LotNum for the tag  */  
   "LotNum":string,
      /**  Serial number.  */  
   "SerialNumber":string,
      /**  The PartBin Unit of measure for this tag.  */  
   "UOM":string,
      /**  QOH in PartBin at the time the inventory was frozen. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM. For blank tags this will be zero.  */  
   "FrozenQOH":number,
      /**  The per unit part cost at the time the quantity was frozen, based on the costing method for the part/Site. This is the unit cost based on the part base UOM, which might not be the CCTag.UOM so to get total frozen cost for this tag, the CCTag quantities wi  */  
   "FrozenCost":number,
      /**  The date the count was entered or tag was voided  */  
   "EntryDate":string,
      /**  The time the count was entered or tag was voided  */  
   "EntryTime":number,
      /**  The sheet number the tag is assigned to. If the sheet is being accessed by enter count by sheet, tags tied to that sheet cannot be accessed individually until the sheet record is unlocked.  */  
   "SheetNum":number,
      /**  The PartTran.SysDate for the last PartTran for this part when  the quantity was frozen, used with FrozentTranNum and FrozenTranTime to determine what activity has taken place after the freeze.  */  
   "FrozenTranDate":string,
      /**  The PartTran.SysTime for the last PartTran for this part when  the quantity was frozen, used with FrozentTranDate and FrozenTranNum to determine what activity has taken place after the freeze.  */  
   "FrozenTranTime":number,
      /**  Manually entered by the user to account for ongoing activity that took place during the count.  Inventory activity that took place AFTER the start of the count FrozenQOH), but BEFORE the actual count.  This number is used to adjust the "FrozenQOH" when determining the variance between the Frozen Quantity and the Actual Counted Quantity.  Example:  At 1:00 the count is started and the computer has 250 units on hand for part XYZ.  At 1:30 75 units are issued to a job.  At 2:30 John counts 175 units.  The variance report would report a variance of 75 units and show the issue as activity.  The user could then decide that the issue took place before the count took place and enter 75 units into the Activity Before Count field in Tag Maintenance.  The variance report would then "expect" 175 units and have a count of 175 units for a variance of zero(0).  */  
   "ActivityBeforeCount":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  True indicates this tag is associated with a PCID, false indicates this tag is associated to loose inventory (non-PCID)  */  
   "PCIDTag":boolean,
      /**  The outermost PCID that contains this CCPDICTag.PCID  */  
   "TopLevelPCID":string,
      /**  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  */  
   "PCID":string,
      /**  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  */  
   "ItemPCID":string,
      /**  Only applies if ItemPCID has data. True = indicates in Count Entry that all of the related CCPCIDTag records for this CCPCIDTag.ItemPCID and all lower level nested child PCIDs/Parts should be set to TagReturned = true and  for ItemPartNum records set CountedQty = FrozenQty as if the user had accessed each of the tags and manually entered.  */  
   "ReturnNestedPCID":boolean,
      /**  CCTagBoolean01  */  
   "CCTagBoolean01":boolean,
      /**  CCTagBoolean02  */  
   "CCTagBoolean02":boolean,
      /**  Move To Bin for the tag  */  
   "CCTagCharacter01":string,
      /**  Tag Type for PCID tag  */  
   "CCTagCharacter02":string,
      /**  CCTagCharacter03  */  
   "CCTagCharacter03":string,
      /**  CCTagCharacter04  */  
   "CCTagCharacter04":string,
      /**  Source data used to generate the default serial tag when no standard tag is generated from SerialNo, PartBinQOH or  PrimaryBin  */  
   "CCTagCharacter05":string,
      /**  CCTagDate01  */  
   "CCTagDate01":string,
      /**  CCTagDate02  */  
   "CCTagDate02":string,
      /**  CCTagDecimal01  */  
   "CCTagDecimal01":number,
      /**  CCTagDecimal02  */  
   "CCTagDecimal02":number,
      /**  CCTagInteger01  */  
   "CCTagInteger01":number,
      /**  CCTagInteger02  */  
   "CCTagInteger02":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "CountedQtyWarn":string,
   "EnableLotNo":boolean,
   "EnableSerialNo":boolean,
      /**  True when UOM Worksheet must be enabled  */  
   "EnableUOMWorksheet":boolean,
      /**  This field is to indicate there is data in the activity grid to cue the user to consult the detail sheet before entering counts.  */  
   "HasActivity":string,
   "SavedBlankTag":boolean,
      /**  External field. Used by the Void Blank Tags processing to indicate the tag was selected for void.  */  
   "SelectedForVoid":boolean,
      /**  Tag Status Description  */  
   "TagStatusDesc":string,
      /**  Display Only Unit Of Measure.  */  
   "UOMDO":string,
   "WarehouseCodeDescription":string,
   "EnablePCID":boolean,
   "EnableItemPCID":boolean,
   "IsNestedPCID":boolean,
   "IsItemQty":boolean,
   "MoveToBinDescription":string,
      /**  Used for Code Desc list to allow changing this list by manually setting in code logic.  */  
   "TagTypeDescList":string,
      /**  Tag Type Description  */  
   "TagTypeDescription":string,
   "EnableTagType":boolean,
   "EnableGenLowerNestedPCID":boolean,
      /**  This field used by GenerateTags to indicate how many blank PCID tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  */  
   "HHNumOfBlankPCIDTags":number,
      /**  This field used by GenerateTags to indicate how many blank tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  */  
   "HHNumOfBlankTags":number,
      /**  Flag to set row rule to know if CCTag.BinNum should be enabled in UI  */  
   "EnableBinNum":boolean,
   "EnableReturnNestedPCID":boolean,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
   "EnableAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "DisableRevisionNum":boolean,
   "BitFlag":number,
   "BinNumDescription":string,
   "CCPeriodDefnPeriodEnd":string,
   "CCPeriodDefnPeriodDesc":string,
   "CCPeriodDefnPeriodStart":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumSalesUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryAttributes":boolean,
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CCTagWrkShtRow{
   "UOMCode":string,
   "Description":string,
   "ConvFactor":number,
   "BaseUOMCode":string,
   "CountedQty":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param pQty
      @param ds
   */  
export interface CalcCountedQty_input{
   pQty:number,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface CalcCountedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param seqStartDate
      @param seqTimeSeqStarted
      @param snTranListCount
      @param ds
   */  
export interface CalculateActivityBeforeCount_input{
   seqStartDate:string,
   seqTimeSeqStarted:string,
      /**  snTranListView.dataView.Count  */  
   snTranListCount:number,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface CalculateActivityBeforeCount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param iTagNum
      @param iWarehouseCode
      @param iMonth
      @param iYear
      @param iCycleSeq
      @param iFullPhysical
   */  
export interface CustomGetByID_input{
      /**  The Tag Number  */  
   iTagNum:string,
      /**  The Warehouse Code  */  
   iWarehouseCode:string,
      /**  The TFOrdLine code  */  
   iMonth:number,
      /**  The Year  */  
   iYear:number,
      /**  The Cycle Number  */  
   iCycleSeq:number,
      /**  Full Physical Inventory flag  */  
   iFullPhysical:boolean,
}

export interface CustomGetByID_output{
   returnObj:Erp_Tablesets_CountTagTableset[],
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param tagNum
   */  
export interface DeleteByID_input{
   plant:string,
   warehouseCode:string,
   tagNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CCTagListRow{
      /**  Company Identifier.  */  
   Company:string,
   Bindesc:string,
      /**  Unique identifier for this warehouse assigned by the user.  */  
   WarehouseCode:string,
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  */  
   TagNum:string,
   TagSelForVoid:boolean,
      /**  Bin number for the tag  */  
   BinNum:string,
      /**  Person that counted the parts on the Count Tag.  */  
   CountedBy:string,
   WrehouseCode:string,
      /**  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  */  
   CountedQty:number,
   WarehseDesc:string,
      /**  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  */  
   CountedTime:string,
      /**  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  */  
   TagReturned:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The outermost PCID that contains this CCPDICTag.PCID  */  
   TopLevelPCID:string,
      /**  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  */  
   PCID:string,
      /**  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  */  
   ItemPCID:string,
      /**  Tag Status Description  */  
   TagStatusDesc:string,
      /**  Tag Type for PCID tag  */  
   CCTagCharacter02:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCTagListTableset{
   CCTagList:Erp_Tablesets_CCTagListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CCTagRow{
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
      /**  Part Number selected for counting.  */  
   PartNum:string,
      /**  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  */  
   TagNum:string,
      /**  Bin number for the tag  */  
   BinNum:string,
      /**  Person that counted the parts on the Count Tag.  */  
   CountedBy:string,
      /**  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  */  
   CountedQty:number,
      /**  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  */  
   CountedTime:string,
      /**  Tag Note  */  
   TagNote:string,
      /**  This field is set equal to the Login ID variable.  System Set when a user enters a counted amount for the tag or voids the tag.  */  
   EntryPerson:string,
      /**  Indicates that the Count Tag has been printed.  Manually entered tags are set to "Printed" when they are entered.  System Set.  */  
   TagPrinted:boolean,
      /**  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  */  
   TagReturned:boolean,
      /**  Date the count was performed.  */  
   CountedDate:string,
      /**   Tag status.
Code/Desc:
0 = open
1 = posted
2 = voided 3=Closed/Recount.  */  
   TagStatus:number,
      /**  True = this tag was generated as a blank tag. This will control whether bin/lot/serial data can be changed on the tag and whether the tag can be voided independent of other tags generated for an part.  */  
   BlankTag:boolean,
      /**  LotNum for the tag  */  
   LotNum:string,
      /**  Serial number.  */  
   SerialNumber:string,
      /**  The PartBin Unit of measure for this tag.  */  
   UOM:string,
      /**  QOH in PartBin at the time the inventory was frozen. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM. For blank tags this will be zero.  */  
   FrozenQOH:number,
      /**  The per unit part cost at the time the quantity was frozen, based on the costing method for the part/Site. This is the unit cost based on the part base UOM, which might not be the CCTag.UOM so to get total frozen cost for this tag, the CCTag quantities wi  */  
   FrozenCost:number,
      /**  The date the count was entered or tag was voided  */  
   EntryDate:string,
      /**  The time the count was entered or tag was voided  */  
   EntryTime:number,
      /**  The sheet number the tag is assigned to. If the sheet is being accessed by enter count by sheet, tags tied to that sheet cannot be accessed individually until the sheet record is unlocked.  */  
   SheetNum:number,
      /**  The PartTran.SysDate for the last PartTran for this part when  the quantity was frozen, used with FrozentTranNum and FrozenTranTime to determine what activity has taken place after the freeze.  */  
   FrozenTranDate:string,
      /**  The PartTran.SysTime for the last PartTran for this part when  the quantity was frozen, used with FrozentTranDate and FrozenTranNum to determine what activity has taken place after the freeze.  */  
   FrozenTranTime:number,
      /**  Manually entered by the user to account for ongoing activity that took place during the count.  Inventory activity that took place AFTER the start of the count FrozenQOH), but BEFORE the actual count.  This number is used to adjust the "FrozenQOH" when determining the variance between the Frozen Quantity and the Actual Counted Quantity.  Example:  At 1:00 the count is started and the computer has 250 units on hand for part XYZ.  At 1:30 75 units are issued to a job.  At 2:30 John counts 175 units.  The variance report would report a variance of 75 units and show the issue as activity.  The user could then decide that the issue took place before the count took place and enter 75 units into the Activity Before Count field in Tag Maintenance.  The variance report would then "expect" 175 units and have a count of 175 units for a variance of zero(0).  */  
   ActivityBeforeCount:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  True indicates this tag is associated with a PCID, false indicates this tag is associated to loose inventory (non-PCID)  */  
   PCIDTag:boolean,
      /**  The outermost PCID that contains this CCPDICTag.PCID  */  
   TopLevelPCID:string,
      /**  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  */  
   PCID:string,
      /**  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  */  
   ItemPCID:string,
      /**  Only applies if ItemPCID has data. True = indicates in Count Entry that all of the related CCPCIDTag records for this CCPCIDTag.ItemPCID and all lower level nested child PCIDs/Parts should be set to TagReturned = true and  for ItemPartNum records set CountedQty = FrozenQty as if the user had accessed each of the tags and manually entered.  */  
   ReturnNestedPCID:boolean,
      /**  CCTagBoolean01  */  
   CCTagBoolean01:boolean,
      /**  CCTagBoolean02  */  
   CCTagBoolean02:boolean,
      /**  Move To Bin for the tag  */  
   CCTagCharacter01:string,
      /**  Tag Type for PCID tag  */  
   CCTagCharacter02:string,
      /**  CCTagCharacter03  */  
   CCTagCharacter03:string,
      /**  CCTagCharacter04  */  
   CCTagCharacter04:string,
      /**  Source data used to generate the default serial tag when no standard tag is generated from SerialNo, PartBinQOH or  PrimaryBin  */  
   CCTagCharacter05:string,
      /**  CCTagDate01  */  
   CCTagDate01:string,
      /**  CCTagDate02  */  
   CCTagDate02:string,
      /**  CCTagDecimal01  */  
   CCTagDecimal01:number,
      /**  CCTagDecimal02  */  
   CCTagDecimal02:number,
      /**  CCTagInteger01  */  
   CCTagInteger01:number,
      /**  CCTagInteger02  */  
   CCTagInteger02:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   CountedQtyWarn:string,
   EnableLotNo:boolean,
   EnableSerialNo:boolean,
      /**  True when UOM Worksheet must be enabled  */  
   EnableUOMWorksheet:boolean,
      /**  This field is to indicate there is data in the activity grid to cue the user to consult the detail sheet before entering counts.  */  
   HasActivity:string,
   SavedBlankTag:boolean,
      /**  External field. Used by the Void Blank Tags processing to indicate the tag was selected for void.  */  
   SelectedForVoid:boolean,
      /**  Tag Status Description  */  
   TagStatusDesc:string,
      /**  Display Only Unit Of Measure.  */  
   UOMDO:string,
   WarehouseCodeDescription:string,
   EnablePCID:boolean,
   EnableItemPCID:boolean,
   IsNestedPCID:boolean,
   IsItemQty:boolean,
   MoveToBinDescription:string,
      /**  Used for Code Desc list to allow changing this list by manually setting in code logic.  */  
   TagTypeDescList:string,
      /**  Tag Type Description  */  
   TagTypeDescription:string,
   EnableTagType:boolean,
   EnableGenLowerNestedPCID:boolean,
      /**  This field used by GenerateTags to indicate how many blank PCID tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  */  
   HHNumOfBlankPCIDTags:number,
      /**  This field used by GenerateTags to indicate how many blank tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  */  
   HHNumOfBlankTags:number,
      /**  Flag to set row rule to know if CCTag.BinNum should be enabled in UI  */  
   EnableBinNum:boolean,
   EnableReturnNestedPCID:boolean,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   DisableRevisionNum:boolean,
   BitFlag:number,
   BinNumDescription:string,
   CCPeriodDefnPeriodEnd:string,
   CCPeriodDefnPeriodDesc:string,
   CCPeriodDefnPeriodStart:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackInventoryAttributes:boolean,
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CCTagWrkShtRow{
   UOMCode:string,
   Description:string,
   ConvFactor:number,
   BaseUOMCode:string,
   CountedQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CountTagTableset{
   CCTag:Erp_Tablesets_CCTagRow[],
   CCTagWrkSht:Erp_Tablesets_CCTagWrkShtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCountTagTableset{
   CCTag:Erp_Tablesets_CCTagRow[],
   CCTagWrkSht:Erp_Tablesets_CCTagWrkShtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipTopLevelPCID
      @param company
      @param plant
      @param whseCode
      @param ccYear
      @param ccMonth
      @param cycleSeq
      @param fullPhysical
   */  
export interface GenerateNestedTags_input{
   ipTopLevelPCID:string,
   company:string,
   plant:string,
   whseCode:string,
   ccYear:number,
   ccMonth:number,
   cycleSeq:number,
   fullPhysical:boolean,
}

export interface GenerateNestedTags_output{
parameters : {
      /**  output parameters  */  
   vFirstTag:number,
   vLastTag:number,
}
}

   /** Required : 
      @param numBlankTags
      @param numBlankPCIDTags
      @param company
      @param plant
      @param whseCode
      @param ccYear
      @param ccMonth
      @param cycleSeq
      @param fullPhysical
   */  
export interface GenerateTags_input{
   numBlankTags:number,
   numBlankPCIDTags:number,
   company:string,
   plant:string,
   whseCode:string,
   ccYear:number,
   ccMonth:number,
   cycleSeq:number,
   fullPhysical:boolean,
}

export interface GenerateTags_output{
parameters : {
      /**  output parameters  */  
   vFirstTag:number,
   vLastTag:number,
}
}

   /** Required : 
      @param seqStartDate
      @param seqTimeSeqStarted
      @param ds
   */  
export interface GetActivityWhereClause_input{
   seqStartDate:string,
   seqTimeSeqStarted:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface GetActivityWhereClause_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param plant
      @param warehouseCode
      @param tagNum
   */  
export interface GetByID_input{
   plant:string,
   warehouseCode:string,
   tagNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CountTagTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CountTagTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CountTagTableset[],
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
   returnObj:Erp_Tablesets_CCTagListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param warehouseCode
   */  
export interface GetNewCCTag_input{
   ds:Erp_Tablesets_CountTagTableset[],
   plant:string,
   warehouseCode:string,
}

export interface GetNewCCTag_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param partNum
      @param uomCode
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param whereClauseCCTag
      @param whereClauseCCTagWrkSht
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCCTag:string,
   whereClauseCCTagWrkSht:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CountTagTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param seqStartDate
      @param seqTimeSeqStarted
      @param ds
   */  
export interface GetSNTransWhereClause_input{
   seqStartDate:string,
   seqTimeSeqStarted:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface GetSNTransWhereClause_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface GetUOMData_input{
   ipPartNum:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface GetUOMData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
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
      @param attributeSetID
      @param ds
   */  
export interface OnChangeAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param inBinNum
      @param ds
   */  
export interface OnChangeBinNum_input{
      /**  Proposed BinNum  */  
   inBinNum:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param pQty
      @param ds
   */  
export interface OnChangeCountedQty_input{
      /**  Proposed DimCode  */  
   pQty:number,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeCountedQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param ipItemPCID
      @param ds
   */  
export interface OnChangeItemPCID_input{
      /**  Package Control Item PCID  */  
   ipItemPCID:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeItemPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param inBinNum
      @param ds
   */  
export interface OnChangeMoveToBinNum_input{
      /**  Proposed Move to BinNum  */  
   inBinNum:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeMoveToBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangeNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param ipPCIDTagType
      @param ds
   */  
export interface OnChangePCIDTagType_input{
      /**  Proposed PCID Tag type  */  
   ipPCIDTagType:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangePCIDTagType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param ipPCID
      @param ds
   */  
export interface OnChangePCID_input{
      /**  Package Control ID  */  
   ipPCID:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param pcPartNum
      @param uomCode
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  Proposed PartNum  */  
   pcPartNum:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param ipCCUOM
      @param ds
   */  
export interface OnChangeUOM_input{
      /**  Proposed UOM  */  
   ipCCUOM:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCountTagTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCountTagTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

export interface ValidatePlant_output{
}

   /** Required : 
      @param ds
   */  
export interface getRelatedTagsWhereClause_input{
   ds:Erp_Tablesets_CountTagTableset[],
}

export interface getRelatedTagsWhereClause_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CountTagTableset[],
}
}

