import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TransferWorkBenchSvc
// Description: The TransferWorkBench object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/$metadata", {
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
   Description: Get TransferWorkBenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransferWorkBenches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TransferWorkBenches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransferWorkBenches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferWorkBenches(requestBody:Erp_Tablesets_TFOrdDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches", {
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
   Summary: Calls GetByID to retrieve the TransferWorkBench item
   Description: Calls GetByID to retrieve the TransferWorkBench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransferWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TFOrdDtlRow
   */  
export function get_TransferWorkBenches_Company_TFLineNum(Company:string, TFLineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TFOrdDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches(" + Company + "," + TFLineNum + ")", {
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
         resolve(data as Erp_Tablesets_TFOrdDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TransferWorkBench for the service
   Description: Calls UpdateExt to update TransferWorkBench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransferWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TransferWorkBenches_Company_TFLineNum(Company:string, TFLineNum:string, requestBody:Erp_Tablesets_TFOrdDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches(" + Company + "," + TFLineNum + ")", {
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
   Summary: Call UpdateExt to delete TransferWorkBench item
   Description: Call UpdateExt to delete TransferWorkBench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransferWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TFLineNum Desc: TFLineNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TransferWorkBenches_Company_TFLineNum(Company:string, TFLineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches(" + Company + "," + TFLineNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow)
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
export function get_GetRows(whereClauseTFOrdDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTFOrdDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(tfLineNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tfLineNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tfLineNum=" + tfLineNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetList" + params, {
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
   Summary: Invoke method FindPart
   Description: Find part.
   OperationID: FindPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:FindPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/FindPart", {
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
         resolve(data as FindPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetCodeDescList", {
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
   Summary: Invoke method GetPartFromRowID
   Description: Get Part From RowID.
   OperationID: GetPartFromRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:GetPartFromRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartFromRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetPartFromRowID", {
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
         resolve(data as GetPartFromRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForLandingPage
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRowsForLandingPage
      @param inTFLineList Desc: RowType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsForLandingPage(inTFLineList:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof inTFLineList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "inTFLineList=" + inTFLineList
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForLandingPage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetRowsForLandingPage" + params, {
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
         resolve(data as GetRowsForLandingPage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransferShipDate
   Description: Sets the transfer ship date base on fromplant, toplant, and needbydate.
It's calculated using the needby date and subtracting the transfers days
held in the PltTranDef Table.
   OperationID: GetTransferShipDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransferShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransferShipDate(requestBody:GetTransferShipDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransferShipDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetTransferShipDate", {
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
         resolve(data as GetTransferShipDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFirmSuggestion
   Description: This method is called when the Firm checkbox changes
   OperationID: OnChangeFirmSuggestion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFirmSuggestion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFirmSuggestion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFirmSuggestion(requestBody:OnChangeFirmSuggestion_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFirmSuggestion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/OnChangeFirmSuggestion", {
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
         resolve(data as OnChangeFirmSuggestion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: This method is to be called when the Part Number field changes
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQtyValue
   Description: This method is called when the Quantity or Quantity UOM changes to convert quantities.
   OperationID: OnChangeQtyValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQtyValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQtyValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQtyValue(requestBody:OnChangeQtyValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQtyValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/OnChangeQtyValue", {
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
         resolve(data as OnChangeQtyValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingPlant
   Description: Purpose:
Parameters:  none
Notes:
<param name="plantID">PlantID </param><param name="success">Success </param>
   OperationID: OnChangingPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingPlant(requestBody:OnChangingPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/OnChangingPlant", {
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
         resolve(data as OnChangingPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessNewSuggestions
   Description: This method converts unfirm to firm requirements, creates transfer orders .
The suggested where clause:
where TFOrdDtl.Plant  = ipPlant and TFOrdDtl.ToPlant = cur-plant
and TFOrdDtl.NeedByDate less or = horizonDate and TFOrdDtl.TFOrdNum = "":U
and TFOrdDtl.Shipped = no
   OperationID: ProcessNewSuggestions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessNewSuggestions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNewSuggestions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessNewSuggestions(requestBody:ProcessNewSuggestions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessNewSuggestions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/ProcessNewSuggestions", {
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
         resolve(data as ProcessNewSuggestions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetDefaultShipVia
   Description: This method is to be called when the CreateOrder field changes
   OperationID: SetDefaultShipVia
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetDefaultShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetDefaultShipVia(requestBody:SetDefaultShipVia_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetDefaultShipVia_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/SetDefaultShipVia", {
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
         resolve(data as SetDefaultShipVia_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/OnChangingAttributeSet", {
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
         resolve(data as OnChangingAttributeSet_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/OnChangingRevisionNum", {
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
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTFOrdDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTFOrdDtl(requestBody:GetNewTFOrdDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTFOrdDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetNewTFOrdDtl", {
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
         resolve(data as GetNewTFOrdDtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TFOrdDtlRow,
}

export interface Erp_Tablesets_TFOrdDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   "TFOrdNum":string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   "WarehouseCode":string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   "OrderFirm":boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   "NeedByDate":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   "ManualOrder":boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   "SupplyJobNum":string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   "DemandJobNum":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Received Quantity  */  
   "ReceivedQty":number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   "AdditionalQty":number,
      /**  Date transfer suggestion went firm  */  
   "FirmDate":string,
      /**  User who made the transfer suggestion firm  */  
   "FirmUser":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "DemandAsmSeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "DemandMtlSeq":number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "SupplyAsmSeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "SupplyMtlSeq":number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   "StockTrans":boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "OurStockQtyUOM":string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "SellingQtyUOM":string,
      /**  Selling Quantity  */  
   "SellingQty":number,
      /**  Selling Shipped Quantity  */  
   "SellingShippedQty":number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "ToPlantDesc":string,
   "FromPlantDesc":string,
   "Selected":boolean,
   "RequiredQty":number,
   "CreateOrder":boolean,
      /**  Descriptive Text of OpenLine Field  */  
   "LineStatus":string,
   "LotNum":string,
   "DimCode":string,
   "Weight":number,
   "TotNetWeight":number,
   "BinNum":string,
   "PkgClass":string,
   "PkgCode":string,
   "Packages":number,
   "AvailSerialNumbers":boolean,
   "DimConvFactor":number,
   "DUM":string,
      /**  DimCodeDimCodeDescription  */  
   "DimCodeDimCodeDescription":string,
      /**  PkgClassDescription  */  
   "PkgClassDescription":string,
      /**  PkgCodeDescription  */  
   "PkgCodeDescription":string,
      /**  OurStockQty * DimConvFactor  */  
   "DisplayShipQty":number,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   "InvtyUOM":string,
      /**  This order inventory quantity  */  
   "ThisOrderInvtyQty":number,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartDescIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartDescSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartDescTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartDescPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartDescSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartDescTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartDescPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartDescTrackDimension":boolean,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Description.  */  
   "StageWhseCodeDescription":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TFOrdDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   "TFOrdNum":string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "TFOrdLine":number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   "WarehouseCode":string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  Site Identifier. This field cannot be blank.  */  
   "Plant":string,
      /**  Site Identifier.  This field cannot be blank.  */  
   "ToPlant":string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   "OrderFirm":boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   "NeedByDate":string,
      /**  Shipped flag  */  
   "Shipped":boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   "ManualOrder":boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   "SupplyJobNum":string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   "DemandJobNum":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   "TFLineNum":string,
      /**  Received Quantity  */  
   "ReceivedQty":number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   "AdditionalQty":number,
      /**  Date transfer suggestion went firm  */  
   "FirmDate":string,
      /**  User who made the transfer suggestion firm  */  
   "FirmUser":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "DemandAsmSeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "DemandMtlSeq":number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   "SupplyAsmSeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   "SupplyMtlSeq":number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   "StockTrans":boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "OurStockQtyUOM":string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   "SellingQtyUOM":string,
      /**  Selling Quantity  */  
   "SellingQty":number,
      /**  Selling Shipped Quantity  */  
   "SellingShippedQty":number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  */  
   "TransferContractID":string,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  */  
   "TransferLinkToContract":boolean,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Indicates if the transfer order line should be added or removed from the fulfillment queue.  */  
   "PartAllocQueueAction":string,
      /**  This flag indicates if the transfer order line is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
   "AvailSerialNumbers":boolean,
   "BinNum":string,
   "DimCode":string,
      /**  DimCodeDimCodeDescription  */  
   "DimCodeDimCodeDescription":string,
   "DimConvFactor":number,
      /**  OurStockQty * DimConvFactor  */  
   "DisplayShipQty":number,
   "DUM":string,
   "FromPlantDesc":string,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   "InvtyUOM":string,
      /**  Descriptive Text of OpenLine Field  */  
   "LineStatus":string,
   "LotNum":string,
   "Packages":number,
   "PCID":string,
   "PkgClass":string,
      /**  PkgClassDescription  */  
   "PkgClassDescription":string,
   "PkgCode":string,
      /**  PkgCodeDescription  */  
   "PkgCodeDescription":string,
   "RequiredQty":number,
   "Selected":boolean,
   "StagingBinDesc":string,
      /**  This order inventory quantity  */  
   "ThisOrderInvtyQty":number,
   "ToPlantDesc":string,
   "TotNetWeight":number,
   "Weight":number,
   "CreateOrder":boolean,
   "EnableAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
      /**  Error Status Display  */  
   "ErrorStatusDisplay":string,
      /**  True if this release is in the fulfillment queue.  */  
   "InPartAllocQueue":boolean,
      /**  Show Fulfillment Queue Actions  */  
   "ShowFulfillmentQueueActions":boolean,
   "BitFlag":number,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "PartDescTrackInventoryAttributes":boolean,
   "PartDescAttrClassID":string,
   "PartDescPricePerCode":string,
   "PartDescTrackSerialNum":boolean,
   "PartDescPartDescription":string,
   "PartDescTrackDimension":boolean,
   "PartDescSalesUM":string,
   "PartDescIUM":string,
   "PartDescSellingFactor":number,
   "PartDescTrackLots":boolean,
   "PartDescTrackInventoryByRevision":boolean,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "StageWhseCodeDescription":string,
   "WarehouseCodeDescription":string,
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
      @param tfLineNum
   */  
export interface DeleteByID_input{
   tfLineNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TFOrdDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   TFOrdNum:string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   OrderFirm:boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   ManualOrder:boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   SupplyJobNum:string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   DemandJobNum:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Received Quantity  */  
   ReceivedQty:number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   AdditionalQty:number,
      /**  Date transfer suggestion went firm  */  
   FirmDate:string,
      /**  User who made the transfer suggestion firm  */  
   FirmUser:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   DemandAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   DemandMtlSeq:number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   SupplyAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   SupplyMtlSeq:number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   StockTrans:boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   OurStockQtyUOM:string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   SellingQtyUOM:string,
      /**  Selling Quantity  */  
   SellingQty:number,
      /**  Selling Shipped Quantity  */  
   SellingShippedQty:number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   ToPlantDesc:string,
   FromPlantDesc:string,
   Selected:boolean,
   RequiredQty:number,
   CreateOrder:boolean,
      /**  Descriptive Text of OpenLine Field  */  
   LineStatus:string,
   LotNum:string,
   DimCode:string,
   Weight:number,
   TotNetWeight:number,
   BinNum:string,
   PkgClass:string,
   PkgCode:string,
   Packages:number,
   AvailSerialNumbers:boolean,
   DimConvFactor:number,
   DUM:string,
      /**  DimCodeDimCodeDescription  */  
   DimCodeDimCodeDescription:string,
      /**  PkgClassDescription  */  
   PkgClassDescription:string,
      /**  PkgCodeDescription  */  
   PkgCodeDescription:string,
      /**  OurStockQty * DimConvFactor  */  
   DisplayShipQty:number,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   InvtyUOM:string,
      /**  This order inventory quantity  */  
   ThisOrderInvtyQty:number,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartDescIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartDescSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartDescTrackLots:boolean,
      /**  Describes the Part.  */  
   PartDescPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartDescSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartDescTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartDescPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartDescTrackDimension:boolean,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Description.  */  
   StageWhseCodeDescription:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TFOrdDtlListTableset{
   TFOrdDtlList:Erp_Tablesets_TFOrdDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TFOrdDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  */  
   TFOrdNum:string,
      /**  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   TFOrdLine:number,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  Site Identifier.  This field cannot be blank.  */  
   ToPlant:string,
      /**  Indicates an Unfirm Transfer Order.  Similar to JobFirm  */  
   OrderFirm:boolean,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Shipped flag  */  
   Shipped:boolean,
      /**  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  */  
   ManualOrder:boolean,
      /**  Job number of the job supplying the parts for this record (FromSite)  */  
   SupplyJobNum:string,
      /**  Job number of the job demand for the parts on this record (ToSite)  */  
   DemandJobNum:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  */  
   TFLineNum:string,
      /**  Received Quantity  */  
   ReceivedQty:number,
      /**  Additional quantity beyond the initial requirement to be transferred  */  
   AdditionalQty:number,
      /**  Date transfer suggestion went firm  */  
   FirmDate:string,
      /**  User who made the transfer suggestion firm  */  
   FirmUser:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   DemandAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   DemandMtlSeq:number,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   SupplyAsmSeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   SupplyMtlSeq:number,
      /**  Indicates if this requirement/receipt affects stock.  */  
   StockTrans:boolean,
      /**   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   OurStockQtyUOM:string,
      /**   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   SellingQtyUOM:string,
      /**  Selling Quantity  */  
   SellingQty:number,
      /**  Selling Shipped Quantity  */  
   SellingShippedQty:number,
      /**  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ContractID  */  
   ContractID:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  */  
   TransferContractID:string,
      /**  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  */  
   TransferLinkToContract:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Indicates if the transfer order line should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the transfer order line is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   AvailSerialNumbers:boolean,
   BinNum:string,
   DimCode:string,
      /**  DimCodeDimCodeDescription  */  
   DimCodeDimCodeDescription:string,
   DimConvFactor:number,
      /**  OurStockQty * DimConvFactor  */  
   DisplayShipQty:number,
   DUM:string,
   FromPlantDesc:string,
      /**  Inventory UOM that the Transfer Order Detail is allocated against.  */  
   InvtyUOM:string,
      /**  Descriptive Text of OpenLine Field  */  
   LineStatus:string,
   LotNum:string,
   Packages:number,
   PCID:string,
   PkgClass:string,
      /**  PkgClassDescription  */  
   PkgClassDescription:string,
   PkgCode:string,
      /**  PkgCodeDescription  */  
   PkgCodeDescription:string,
   RequiredQty:number,
   Selected:boolean,
   StagingBinDesc:string,
      /**  This order inventory quantity  */  
   ThisOrderInvtyQty:number,
   ToPlantDesc:string,
   TotNetWeight:number,
   Weight:number,
   CreateOrder:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this release is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   PartDescTrackInventoryAttributes:boolean,
   PartDescAttrClassID:string,
   PartDescPricePerCode:string,
   PartDescTrackSerialNum:boolean,
   PartDescPartDescription:string,
   PartDescTrackDimension:boolean,
   PartDescSalesUM:string,
   PartDescIUM:string,
   PartDescSellingFactor:number,
   PartDescTrackLots:boolean,
   PartDescTrackInventoryByRevision:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   StageWhseCodeDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TransferWorkBenchTableset{
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTransferWorkBenchTableset{
   TFOrdDtl:Erp_Tablesets_TFOrdDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  PartNum  */  
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param tfLineNum
   */  
export interface GetByID_input{
   tfLineNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TransferWorkBenchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TransferWorkBenchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TransferWorkBenchTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  TableName  */  
   tableName:string,
      /**  FieldName  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
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
   returnObj:Erp_Tablesets_TFOrdDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTFOrdDtl_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface GetNewTFOrdDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
      /**  RowType  */  
   ipRowType:string,
      /**  RowID  */  
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param inTFLineList
   */  
export interface GetRowsForLandingPage_input{
      /**  RowType  */  
   inTFLineList:string,
}

export interface GetRowsForLandingPage_output{
   returnObj:Erp_Tablesets_TransferWorkBenchTableset[],
}

   /** Required : 
      @param whereClauseTFOrdDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTFOrdDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TransferWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetTransferShipDate_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface GetTransferShipDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
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
      @param ipOrderFirm
      @param ds
   */  
export interface OnChangeFirmSuggestion_input{
      /**  OrderFirm  */  
   ipOrderFirm:boolean,
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface OnChangeFirmSuggestion_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface OnChangePartNum_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
      /**  Part Number  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeQtyValue_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface OnChangeQtyValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param plantID
   */  
export interface OnChangingPlant_input{
   plantID:string,
}

export interface OnChangingPlant_output{
parameters : {
      /**  output parameters  */  
   success:boolean,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessNewSuggestions_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface ProcessNewSuggestions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface SetDefaultShipVia_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface SetDefaultShipVia_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTransferWorkBenchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTransferWorkBenchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TransferWorkBenchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TransferWorkBenchTableset,
}
}

