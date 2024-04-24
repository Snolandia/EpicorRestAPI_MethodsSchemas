import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PcECCSvc
// Description: Pc ECC main object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/$metadata", {
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
   Description: Get PcECCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcECCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcECCOrderDtlRow
   */  
export function get_PcECCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcECCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcECCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs", {
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
   Summary: Calls GetByID to retrieve the PcECC item
   Description: Calls GetByID to retrieve the PcECC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcECC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ECCBSVID Desc: ECCBSVID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
   */  
export function get_PcECCs_Company_ECCBSVID(Company:string, ECCBSVID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcECCOrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs(" + Company + "," + ECCBSVID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcECCOrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcECC for the service
   Description: Calls UpdateExt to update PcECC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcECC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ECCBSVID Desc: ECCBSVID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcECCOrderDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcECCs_Company_ECCBSVID(Company:string, ECCBSVID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs(" + Company + "," + ECCBSVID + ")", {
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
   Summary: Call UpdateExt to delete PcECC item
   Description: Call UpdateExt to delete PcECC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcECC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ECCBSVID Desc: ECCBSVID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcECCs_Company_ECCBSVID(Company:string, ECCBSVID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/PcECCs(" + Company + "," + ECCBSVID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcECCOrderDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlListRow)
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
export function get_GetRows(whereClausePcECCOrderDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcECCOrderDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcECCOrderDtl=" + whereClausePcECCOrderDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(ecCBSVID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ecCBSVID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ecCBSVID=" + ecCBSVID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetList" + params, {
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
   Summary: Invoke method SubmitCIMRequest
   Description: Creates/updates PcECCOrderDtl record to be used later by EWA
   OperationID: SubmitCIMRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitCIMRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitCIMRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitCIMRequest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/SubmitCIMRequest", {
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
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartForConfig(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetBasePartForConfig", {
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
   Summary: Invoke method SetKBMaxConfigProdID
   Description: Set the CPQ Quote Product ID on the Web Basket Line.
   OperationID: SetKBMaxConfigProdID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetKBMaxConfigProdID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetKBMaxConfigProdID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetKBMaxConfigProdID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/SetKBMaxConfigProdID", {
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
   Summary: Invoke method GetNewPcECCOrderDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcECCOrderDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcECCOrderDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcECCOrderDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcECCOrderDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetNewPcECCOrderDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcECCSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcECCOrderDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcECCOrderDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcECCOrderDtlRow[],
}

export interface Erp_Tablesets_PcECCOrderDtlListRow{
      /**  Company  */  
   "Company":string,
      /**  ECCBSVID  */  
   "ECCBSVID":string,
      /**  CustNum  */  
   "CustNum":number,
      /**  PartNum  */  
   "PartNum":string,
      /**  BasePartNum  */  
   "BasePartNum":string,
      /**  BaseRevisionNum  */  
   "BaseRevisionNum":string,
      /**  Plant  */  
   "Plant":string,
      /**  LineDesc  */  
   "LineDesc":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  BreakListCode  */  
   "BreakListCode":string,
      /**  Commissionable  */  
   "Commissionable":boolean,
      /**  DiscBreakListCode  */  
   "DiscBreakListCode":string,
      /**  UnitPrice  */  
   "UnitPrice":number,
      /**  LockPrice  */  
   "LockPrice":boolean,
      /**  LockQty  */  
   "LockQty":boolean,
      /**  NeedByDate  */  
   "NeedByDate":string,
      /**  OrderComment  */  
   "OrderComment":string,
      /**  OverrideDiscPriceList  */  
   "OverrideDiscPriceList":boolean,
      /**  OverridePriceList  */  
   "OverridePriceList":boolean,
      /**  PickListComment  */  
   "PickListComment":string,
      /**  POLine  */  
   "POLine":string,
      /**  PricePerCode  */  
   "PricePerCode":string,
      /**  ProdCode  */  
   "ProdCode":string,
      /**  ProjectID  */  
   "ProjectID":string,
      /**  Reference  */  
   "Reference":string,
      /**  RequestDate  */  
   "RequestDate":string,
      /**  Rework  */  
   "Rework":boolean,
      /**  RMALine  */  
   "RMALine":number,
      /**  RMANum  */  
   "RMANum":number,
      /**  SalesCatID  */  
   "SalesCatID":string,
      /**  SalesUM  */  
   "SalesUM":string,
      /**  SellingQuantity  */  
   "SellingQuantity":number,
      /**  ShipComment  */  
   "ShipComment":string,
      /**  ShipLineComplete  */  
   "ShipLineComplete":boolean,
      /**  TaxCatID  */  
   "TaxCatID":string,
      /**  TMBilling  */  
   "TMBilling":boolean,
      /**  XPartNum  */  
   "XPartNum":string,
      /**  XRevisionNum  */  
   "XRevisionNum":string,
      /**  DocUnitPrice  */  
   "DocUnitPrice":number,
      /**  ConfigBaseUnitPrice  */  
   "ConfigBaseUnitPrice":number,
      /**  ConfigUnitPrice  */  
   "ConfigUnitPrice":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcECCOrderDtlRow{
      /**  Company  */  
   "Company":string,
      /**  ECCBSVID  */  
   "ECCBSVID":string,
      /**  CustNum  */  
   "CustNum":number,
      /**  PartNum  */  
   "PartNum":string,
      /**  BasePartNum  */  
   "BasePartNum":string,
      /**  BaseRevisionNum  */  
   "BaseRevisionNum":string,
      /**  Plant  */  
   "Plant":string,
      /**  LineDesc  */  
   "LineDesc":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  BreakListCode  */  
   "BreakListCode":string,
      /**  Commissionable  */  
   "Commissionable":boolean,
      /**  DiscBreakListCode  */  
   "DiscBreakListCode":string,
      /**  UnitPrice  */  
   "UnitPrice":number,
      /**  LockPrice  */  
   "LockPrice":boolean,
      /**  LockQty  */  
   "LockQty":boolean,
      /**  NeedByDate  */  
   "NeedByDate":string,
      /**  OrderComment  */  
   "OrderComment":string,
      /**  OverrideDiscPriceList  */  
   "OverrideDiscPriceList":boolean,
      /**  OverridePriceList  */  
   "OverridePriceList":boolean,
      /**  PickListComment  */  
   "PickListComment":string,
      /**  POLine  */  
   "POLine":string,
      /**  PricePerCode  */  
   "PricePerCode":string,
      /**  ProdCode  */  
   "ProdCode":string,
      /**  ProjectID  */  
   "ProjectID":string,
      /**  Reference  */  
   "Reference":string,
      /**  RequestDate  */  
   "RequestDate":string,
      /**  Rework  */  
   "Rework":boolean,
      /**  RMALine  */  
   "RMALine":number,
      /**  RMANum  */  
   "RMANum":number,
      /**  SalesCatID  */  
   "SalesCatID":string,
      /**  SalesUM  */  
   "SalesUM":string,
      /**  SellingQuantity  */  
   "SellingQuantity":number,
      /**  ShipComment  */  
   "ShipComment":string,
      /**  ShipLineComplete  */  
   "ShipLineComplete":boolean,
      /**  TaxCatID  */  
   "TaxCatID":string,
      /**  TMBilling  */  
   "TMBilling":boolean,
      /**  XPartNum  */  
   "XPartNum":string,
      /**  XRevisionNum  */  
   "XRevisionNum":string,
      /**  DocUnitPrice  */  
   "DocUnitPrice":number,
      /**  ConfigBaseUnitPrice  */  
   "ConfigBaseUnitPrice":number,
      /**  ConfigUnitPrice  */  
   "ConfigUnitPrice":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ECCQuoteNum  */  
   "ECCQuoteNum":string,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  ShipToNum  */  
   "ShipToNum":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  CreateDate  */  
   "CreateDate":string,
      /**  AnalysisCode  */  
   "AnalysisCode":string,
      /**  BestCsPct  */  
   "BestCsPct":number,
      /**  Discount  */  
   "Discount":number,
      /**  DiscountPercent  */  
   "DiscountPercent":number,
      /**  DocDiscount  */  
   "DocDiscount":number,
      /**  Engineer  */  
   "Engineer":boolean,
      /**  JobComment  */  
   "JobComment":string,
      /**  KitQtyPer  */  
   "KitQtyPer":number,
      /**  LeadTime  */  
   "LeadTime":string,
      /**  MultiRel  */  
   "MultiRel":boolean,
      /**  PhaseID  */  
   "PhaseID":string,
      /**  QuoteComment  */  
   "QuoteComment":string,
      /**  ReqShipDate  */  
   "ReqShipDate":string,
      /**  SellingExpectedQty  */  
   "SellingExpectedQty":number,
      /**  SellingExpectedUM  */  
   "SellingExpectedUM":string,
      /**  Template  */  
   "Template":boolean,
      /**  WorstCsPct  */  
   "WorstCsPct":number,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  MSRP  */  
   "MSRP":number,
      /**  EndCustomerPrice  */  
   "EndCustomerPrice":number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   "PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate.  */  
   "DocPromotionalPrice":number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate.  */  
   "DocEndCustomerPrice":number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate.  */  
   "DocMSRP":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
   "ConfigID":string,
   "ConfigVersion":number,
   "BitFlag":number,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "PartNumTrackLots":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "SalesCatIDDescription":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ecCBSVID
   */  
export interface DeleteByID_input{
   ecCBSVID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PcECCListTableset{
   PcECCOrderDtlList:Erp_Tablesets_PcECCOrderDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcECCOrderDtlListRow{
      /**  Company  */  
   Company:string,
      /**  ECCBSVID  */  
   ECCBSVID:string,
      /**  CustNum  */  
   CustNum:number,
      /**  PartNum  */  
   PartNum:string,
      /**  BasePartNum  */  
   BasePartNum:string,
      /**  BaseRevisionNum  */  
   BaseRevisionNum:string,
      /**  Plant  */  
   Plant:string,
      /**  LineDesc  */  
   LineDesc:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  BreakListCode  */  
   BreakListCode:string,
      /**  Commissionable  */  
   Commissionable:boolean,
      /**  DiscBreakListCode  */  
   DiscBreakListCode:string,
      /**  UnitPrice  */  
   UnitPrice:number,
      /**  LockPrice  */  
   LockPrice:boolean,
      /**  LockQty  */  
   LockQty:boolean,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  OrderComment  */  
   OrderComment:string,
      /**  OverrideDiscPriceList  */  
   OverrideDiscPriceList:boolean,
      /**  OverridePriceList  */  
   OverridePriceList:boolean,
      /**  PickListComment  */  
   PickListComment:string,
      /**  POLine  */  
   POLine:string,
      /**  PricePerCode  */  
   PricePerCode:string,
      /**  ProdCode  */  
   ProdCode:string,
      /**  ProjectID  */  
   ProjectID:string,
      /**  Reference  */  
   Reference:string,
      /**  RequestDate  */  
   RequestDate:string,
      /**  Rework  */  
   Rework:boolean,
      /**  RMALine  */  
   RMALine:number,
      /**  RMANum  */  
   RMANum:number,
      /**  SalesCatID  */  
   SalesCatID:string,
      /**  SalesUM  */  
   SalesUM:string,
      /**  SellingQuantity  */  
   SellingQuantity:number,
      /**  ShipComment  */  
   ShipComment:string,
      /**  ShipLineComplete  */  
   ShipLineComplete:boolean,
      /**  TaxCatID  */  
   TaxCatID:string,
      /**  TMBilling  */  
   TMBilling:boolean,
      /**  XPartNum  */  
   XPartNum:string,
      /**  XRevisionNum  */  
   XRevisionNum:string,
      /**  DocUnitPrice  */  
   DocUnitPrice:number,
      /**  ConfigBaseUnitPrice  */  
   ConfigBaseUnitPrice:number,
      /**  ConfigUnitPrice  */  
   ConfigUnitPrice:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcECCOrderDtlRow{
      /**  Company  */  
   Company:string,
      /**  ECCBSVID  */  
   ECCBSVID:string,
      /**  CustNum  */  
   CustNum:number,
      /**  PartNum  */  
   PartNum:string,
      /**  BasePartNum  */  
   BasePartNum:string,
      /**  BaseRevisionNum  */  
   BaseRevisionNum:string,
      /**  Plant  */  
   Plant:string,
      /**  LineDesc  */  
   LineDesc:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  BreakListCode  */  
   BreakListCode:string,
      /**  Commissionable  */  
   Commissionable:boolean,
      /**  DiscBreakListCode  */  
   DiscBreakListCode:string,
      /**  UnitPrice  */  
   UnitPrice:number,
      /**  LockPrice  */  
   LockPrice:boolean,
      /**  LockQty  */  
   LockQty:boolean,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  OrderComment  */  
   OrderComment:string,
      /**  OverrideDiscPriceList  */  
   OverrideDiscPriceList:boolean,
      /**  OverridePriceList  */  
   OverridePriceList:boolean,
      /**  PickListComment  */  
   PickListComment:string,
      /**  POLine  */  
   POLine:string,
      /**  PricePerCode  */  
   PricePerCode:string,
      /**  ProdCode  */  
   ProdCode:string,
      /**  ProjectID  */  
   ProjectID:string,
      /**  Reference  */  
   Reference:string,
      /**  RequestDate  */  
   RequestDate:string,
      /**  Rework  */  
   Rework:boolean,
      /**  RMALine  */  
   RMALine:number,
      /**  RMANum  */  
   RMANum:number,
      /**  SalesCatID  */  
   SalesCatID:string,
      /**  SalesUM  */  
   SalesUM:string,
      /**  SellingQuantity  */  
   SellingQuantity:number,
      /**  ShipComment  */  
   ShipComment:string,
      /**  ShipLineComplete  */  
   ShipLineComplete:boolean,
      /**  TaxCatID  */  
   TaxCatID:string,
      /**  TMBilling  */  
   TMBilling:boolean,
      /**  XPartNum  */  
   XPartNum:string,
      /**  XRevisionNum  */  
   XRevisionNum:string,
      /**  DocUnitPrice  */  
   DocUnitPrice:number,
      /**  ConfigBaseUnitPrice  */  
   ConfigBaseUnitPrice:number,
      /**  ConfigUnitPrice  */  
   ConfigUnitPrice:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ECCQuoteNum  */  
   ECCQuoteNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  CreateDate  */  
   CreateDate:string,
      /**  AnalysisCode  */  
   AnalysisCode:string,
      /**  BestCsPct  */  
   BestCsPct:number,
      /**  Discount  */  
   Discount:number,
      /**  DiscountPercent  */  
   DiscountPercent:number,
      /**  DocDiscount  */  
   DocDiscount:number,
      /**  Engineer  */  
   Engineer:boolean,
      /**  JobComment  */  
   JobComment:string,
      /**  KitQtyPer  */  
   KitQtyPer:number,
      /**  LeadTime  */  
   LeadTime:string,
      /**  MultiRel  */  
   MultiRel:boolean,
      /**  PhaseID  */  
   PhaseID:string,
      /**  QuoteComment  */  
   QuoteComment:string,
      /**  ReqShipDate  */  
   ReqShipDate:string,
      /**  SellingExpectedQty  */  
   SellingExpectedQty:number,
      /**  SellingExpectedUM  */  
   SellingExpectedUM:string,
      /**  Template  */  
   Template:boolean,
      /**  WorstCsPct  */  
   WorstCsPct:number,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  MSRP  */  
   MSRP:number,
      /**  EndCustomerPrice  */  
   EndCustomerPrice:number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate.  */  
   DocPromotionalPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate.  */  
   DocEndCustomerPrice:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate.  */  
   DocMSRP:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
   ConfigID:string,
   ConfigVersion:number,
   BitFlag:number,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   SalesCatIDDescription:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcECCTableset{
   PcECCOrderDtl:Erp_Tablesets_PcECCOrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPcECCTableset{
   PcECCOrderDtl:Erp_Tablesets_PcECCOrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartForConfig_input{
      /**  Order Number of the target Assembly  */  
   sourceSysRowID:string,
}

export interface GetBasePartForConfig_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
}
}

   /** Required : 
      @param ecCBSVID
   */  
export interface GetByID_input{
   ecCBSVID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PcECCTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PcECCTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PcECCTableset[],
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
   returnObj:Erp_Tablesets_PcECCListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPcECCOrderDtl_input{
   ds:Erp_Tablesets_PcECCTableset[],
}

export interface GetNewPcECCOrderDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcECCTableset[],
}
}

   /** Required : 
      @param whereClausePcECCOrderDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcECCOrderDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PcECCTableset[],
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
      @param eccBsvID
      @param kbConfigProdID
   */  
export interface SetKBMaxConfigProdID_input{
      /**  Web Basket ID  */  
   eccBsvID:string,
      /**  CPQ Quote Product ID  */  
   kbConfigProdID:number,
}

export interface SetKBMaxConfigProdID_output{
}

   /** Required : 
      @param ds
   */  
export interface SubmitCIMRequest_input{
   ds:Erp_Tablesets_PcECCTableset[],
}

export interface SubmitCIMRequest_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcECCTableset[],
   errCode:string,
   errMsg:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPcECCTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPcECCTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PcECCTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcECCTableset[],
}
}

