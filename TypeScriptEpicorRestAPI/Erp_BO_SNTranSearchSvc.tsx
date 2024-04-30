import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SNTranSearchSvc
// Description: Serial Number Transaction Search Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/$metadata", {
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
   Description: Get SNTranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNTranSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNTranRow
   */  
export function get_SNTranSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNTranSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SNTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SNTranSearches(requestBody:Erp_Tablesets_SNTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches", {
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
   Summary: Calls GetByID to retrieve the SNTranSearch item
   Description: Calls GetByID to retrieve the SNTranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SNTranRow
   */  
export function get_SNTranSearches_Company_PartNum_SerialNumber_TranNum(Company:string, PartNum:string, SerialNumber:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SNTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches(" + Company + "," + PartNum + "," + SerialNumber + "," + TranNum + ")", {
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
         resolve(data as Erp_Tablesets_SNTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SNTranSearch for the service
   Description: Calls UpdateExt to update SNTranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SNTranSearches_Company_PartNum_SerialNumber_TranNum(Company:string, PartNum:string, SerialNumber:string, TranNum:string, requestBody:Erp_Tablesets_SNTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches(" + Company + "," + PartNum + "," + SerialNumber + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete SNTranSearch item
   Description: Call UpdateExt to delete SNTranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNTranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param TranNum Desc: TranNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SNTranSearches_Company_PartNum_SerialNumber_TranNum(Company:string, PartNum:string, SerialNumber:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches(" + Company + "," + PartNum + "," + SerialNumber + "," + TranNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranListRow)
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
export function get_GetRows(whereClauseSNTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSNTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSNTran=" + whereClauseSNTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetRows" + params, {
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
export function get_GetByID(partNum:string, serialNumber:string, tranNum:string, epicorHeaders?:Headers){
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
   if(typeof serialNumber!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serialNumber=" + serialNumber
   }
   if(typeof tranNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranNum=" + tranNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetSNTran
   Description: Purpose:     Get all rows from the SNTran that has a TranType = 'RMA-INS'";
Parameters:  int rmaNum, int rmaLine, int rmaReceiptNum
Notes:       If a SN has more than one row in SNTran with TranType = 'RMA-INS', selects the row with the most recent TranNum.
   OperationID: GetSNTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSNTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSNTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSNTran(requestBody:GetSNTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSNTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetSNTran", {
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
         resolve(data as GetSNTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSNTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSNTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSNTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSNTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSNTran(requestBody:GetNewSNTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSNTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetNewSNTran", {
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
         resolve(data as GetNewSNTran_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNTranListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SNTranRow,
}

export interface Erp_Tablesets_SNTranListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part.  */  
   "PartNum":string,
      /**  The serial number of the part that this transaction is for.  */  
   "SerialNumber":string,
      /**  A number which is used to allow for a unique key for the file.  */  
   "TranNum":number,
      /**  Field that indicates the type of transaction  */  
   "TranType":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  Packing slip line that this record is associated with.  */  
   "PackLine":number,
      /**  The Service Call that this record is accociated with.  */  
   "CallNum":number,
      /**  The Service Call line that this record is accociated with.  */  
   "CallLine":number,
      /**  The RMA that this record is accociated with.  */  
   "RMANum":number,
      /**  The RMA detail that this record is accociated with.  */  
   "RMALine":number,
      /**  Entry Person  */  
   "EntryPerson":string,
      /**  The date of the tranaction  */  
   "TranDate":string,
      /**  Job number.  The job number that this item is linked to.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Seq # of specific material or subcontract operation record.  */  
   "MtlSeq":number,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackSlipLine":number,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   "SNPrefix":string,
      /**  Format of the Base number.  */  
   "SNFormat":string,
      /**  Information about serail number formatting.  */  
   "SNBaseStructure":string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   "SNBaseNumber":string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   "ScrapReasonCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   "SNReference":string,
      /**  RMA receipt  */  
   "RMAReceipt":number,
      /**  DMR Number to identify the DMR record.  */  
   "DMRNum":number,
      /**  System Date  */  
   "SysDate":string,
      /**  System time  */  
   "SysTime":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  */  
   "OprSeq":number,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "WarrExpiration":string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfNum":number,
      /**  Transfer Order packing slip.  */  
   "TFPackNum":number,
      /**  Transfer Order packing slip line.  */  
   "TFPackLine":number,
      /**  Related (OrderHed) Sales Order number  */  
   "OrderNum":number,
      /**  Related (OrderDtl) sales order line number  */  
   "OrderLine":number,
      /**  related (OrderRel) order release number  */  
   "OrderRelNum":number,
      /**  The status of this serial numbered item prior to its current status.  */  
   "PrevSNStatus":string,
      /**  Used to tie back to the related RMADisp record.  */  
   "RMADisp":number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   "ShippedFrom":string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   "SNStatus":string,
      /**  Indicates that this serial number has been voided.  */  
   "Voided":boolean,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   "FullyMatched":boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   "SNMask":string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   "AddedByMatching":boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   "Scrapped":boolean,
      /**  DMR action number.  */  
   "DMRActionNum":number,
      /**  Indicates that this item has failed inspection.  */  
   "FailSelect":boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   "LineDetailNum":number,
      /**  Added at shipment  */  
   "TranAdd":boolean,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   "SubConOprSeq":number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborHedSeq":number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborDtlSeq":number,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   "LastLbrOprSeq":number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   "LotNum":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Next Labor Operation Sequence  */  
   "NextLbrOprSeq":number,
      /**  Next Labor Assembly Sequence  */  
   "NextLbrAssySeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  TFOrdNum  */  
   "TFOrdNum":string,
      /**  TFOrdLine  */  
   "TFOrdLine":number,
   "DispSysTime":string,
   "ShpLegalNum":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "CallLineLineDesc":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "DMRNumPartDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Line description.  */  
   "PackLineLineDesc":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "PackNumName":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
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
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "RMALineLineDesc":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Description.  */  
   "WareHouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SNTranRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part.  */  
   "PartNum":string,
      /**  The serial number of the part that this transaction is for.  */  
   "SerialNumber":string,
      /**  A number which is used to allow for a unique key for the file.  */  
   "TranNum":number,
      /**  Field that indicates the type of transaction  */  
   "TranType":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  Packing slip line that this record is associated with.  */  
   "PackLine":number,
      /**  The Service Call that this record is accociated with.  */  
   "CallNum":number,
      /**  The Service Call line that this record is accociated with.  */  
   "CallLine":number,
      /**  The RMA that this record is accociated with.  */  
   "RMANum":number,
      /**  The RMA detail that this record is accociated with.  */  
   "RMALine":number,
      /**  Entry Person  */  
   "EntryPerson":string,
      /**  The date of the tranaction  */  
   "TranDate":string,
      /**  Job number.  The job number that this item is linked to.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Seq # of specific material or subcontract operation record.  */  
   "MtlSeq":number,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackSlipLine":number,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   "SNPrefix":string,
      /**  Format of the Base number.  */  
   "SNFormat":string,
      /**  Information about serail number formatting.  */  
   "SNBaseStructure":string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   "SNBaseNumber":string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   "ScrapReasonCode":string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   "SNReference":string,
      /**  RMA receipt  */  
   "RMAReceipt":number,
      /**  DMR Number to identify the DMR record.  */  
   "DMRNum":number,
      /**  System Date  */  
   "SysDate":string,
      /**  System time  */  
   "SysTime":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  */  
   "OprSeq":number,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "WarrExpiration":string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfNum":number,
      /**  Transfer Order packing slip.  */  
   "TFPackNum":number,
      /**  Transfer Order packing slip line.  */  
   "TFPackLine":number,
      /**  Related (OrderHed) Sales Order number  */  
   "OrderNum":number,
      /**  Related (OrderDtl) sales order line number  */  
   "OrderLine":number,
      /**  related (OrderRel) order release number  */  
   "OrderRelNum":number,
      /**  The status of this serial numbered item prior to its current status.  */  
   "PrevSNStatus":string,
      /**  Used to tie back to the related RMADisp record.  */  
   "RMADisp":number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   "ShippedFrom":string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   "SNStatus":string,
      /**  Indicates that this serial number has been voided.  */  
   "Voided":boolean,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   "FullyMatched":boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   "RawSerialNum":string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   "SNMask":string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   "AddedByMatching":boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   "SNMaskPrefix":string,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   "Scrapped":boolean,
      /**  DMR action number.  */  
   "DMRActionNum":number,
      /**  Indicates that this item has failed inspection.  */  
   "FailSelect":boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   "LineDetailNum":number,
      /**  Added at shipment  */  
   "TranAdd":boolean,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   "SubConOprSeq":number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborHedSeq":number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   "ScrapLaborDtlSeq":number,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   "LastLbrOprSeq":number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   "LotNum":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Next Labor Operation Sequence  */  
   "NextLbrOprSeq":number,
      /**  Next Labor Assembly Sequence  */  
   "NextLbrAssySeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ShipToCustNum  */  
   "ShipToCustNum":number,
      /**  Latitude  */  
   "Latitude":number,
      /**  Longitude  */  
   "Longitude":number,
      /**  Altitude  */  
   "Altitude":number,
      /**  FSAssetClassCode  */  
   "FSAssetClassCode":string,
      /**  FSServiceLevelAgreement  */  
   "FSServiceLevelAgreement":string,
      /**  Accuracy  */  
   "Accuracy":number,
      /**  MeterReading  */  
   "MeterReading":number,
      /**  One time shipto flag  */  
   "OTS":boolean,
      /**  OTS Address 1  */  
   "OTSAddress1":string,
      /**  OTS Address 2  */  
   "OTSAddress2":string,
      /**  OTS Address 3  */  
   "OTSAddress3":string,
      /**  OTS City  */  
   "OTSCity":string,
      /**  OTS Contact  */  
   "OTSContact":string,
      /**  OTS Country Number  */  
   "OTSCountryNum":number,
      /**  OTS Country Number  */  
   "OTSCustSaved":boolean,
      /**  One Time fax number  */  
   "OTSFaxNum":string,
      /**  OTS Name  */  
   "OTSName":string,
      /**  OTS Phone Number  */  
   "OTSPhoneNum":string,
      /**  OTS Resale ID  */  
   "OTSResaleID":string,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  OTS Ship To Num  */  
   "OTSShipToNum":string,
      /**  OTS State  */  
   "OTSState":string,
      /**  OTS Tax Region Code  */  
   "OTSTaxRegionCode":string,
      /**  OTS Zip  */  
   "OTSZip":string,
      /**  PriorJobNum  */  
   "PriorJobNum":string,
      /**  PriorAssemblySeq  */  
   "PriorAssemblySeq":number,
      /**  PriorMtlSeq  */  
   "PriorMtlSeq":number,
      /**  PriorPartNum  */  
   "PriorPartNum":string,
      /**  PCID  */  
   "PCID":string,
      /**  MscPackNum  */  
   "MscPackNum":number,
      /**  MscPackLine  */  
   "MscPackLine":number,
      /**  Identifier of the asset this Serial Number is associated to. When the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   "AssetNum":string,
      /**  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   "AdditionNum":number,
      /**  DisposalNum  */  
   "DisposalNum":number,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  TFOrdNum  */  
   "TFOrdNum":string,
      /**  TFOrdLine  */  
   "TFOrdLine":number,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "DispSysTime":string,
   "ShpLegalNum":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CallLineLineDesc":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "DMRNumPartDescription":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "JobNumPartDescription":string,
   "PackLineLineDesc":string,
   "PackNumName":string,
   "PartNumTrackDimension":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "RMALineLineDesc":string,
   "SerialNumberSNStatus":string,
   "ShipToCustName":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCountry":string,
   "VendorNumZIP":string,
   "VendorNumCity":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumName":string,
   "WareHouseCodeDescription":string,
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
      @param serialNumber
      @param tranNum
   */  
export interface DeleteByID_input{
   partNum:string,
   serialNumber:string,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_SNTranListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  The serial number of the part that this transaction is for.  */  
   SerialNumber:string,
      /**  A number which is used to allow for a unique key for the file.  */  
   TranNum:number,
      /**  Field that indicates the type of transaction  */  
   TranType:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  Packing slip line that this record is associated with.  */  
   PackLine:number,
      /**  The Service Call that this record is accociated with.  */  
   CallNum:number,
      /**  The Service Call line that this record is accociated with.  */  
   CallLine:number,
      /**  The RMA that this record is accociated with.  */  
   RMANum:number,
      /**  The RMA detail that this record is accociated with.  */  
   RMALine:number,
      /**  Entry Person  */  
   EntryPerson:string,
      /**  The date of the tranaction  */  
   TranDate:string,
      /**  Job number.  The job number that this item is linked to.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Seq # of specific material or subcontract operation record.  */  
   MtlSeq:number,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackSlipLine:number,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   SNPrefix:string,
      /**  Format of the Base number.  */  
   SNFormat:string,
      /**  Information about serail number formatting.  */  
   SNBaseStructure:string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   SNBaseNumber:string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   ScrapReasonCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   SNReference:string,
      /**  RMA receipt  */  
   RMAReceipt:number,
      /**  DMR Number to identify the DMR record.  */  
   DMRNum:number,
      /**  System Date  */  
   SysDate:string,
      /**  System time  */  
   SysTime:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  */  
   OprSeq:number,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The latest of the 3 warranty expiration dates  */  
   WarrExpiration:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfNum:number,
      /**  Transfer Order packing slip.  */  
   TFPackNum:number,
      /**  Transfer Order packing slip line.  */  
   TFPackLine:number,
      /**  Related (OrderHed) Sales Order number  */  
   OrderNum:number,
      /**  Related (OrderDtl) sales order line number  */  
   OrderLine:number,
      /**  related (OrderRel) order release number  */  
   OrderRelNum:number,
      /**  The status of this serial numbered item prior to its current status.  */  
   PrevSNStatus:string,
      /**  Used to tie back to the related RMADisp record.  */  
   RMADisp:number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   ShippedFrom:string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   SNStatus:string,
      /**  Indicates that this serial number has been voided.  */  
   Voided:boolean,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   FullyMatched:boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   SNMask:string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   AddedByMatching:boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   Scrapped:boolean,
      /**  DMR action number.  */  
   DMRActionNum:number,
      /**  Indicates that this item has failed inspection.  */  
   FailSelect:boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   LineDetailNum:number,
      /**  Added at shipment  */  
   TranAdd:boolean,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   SubConOprSeq:number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborHedSeq:number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborDtlSeq:number,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   LastLbrOprSeq:number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   LotNum:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Next Labor Operation Sequence  */  
   NextLbrOprSeq:number,
      /**  Next Labor Assembly Sequence  */  
   NextLbrAssySeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  TFOrdNum  */  
   TFOrdNum:string,
      /**  TFOrdLine  */  
   TFOrdLine:number,
   DispSysTime:string,
   ShpLegalNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   CallLineLineDesc:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   DMRNumPartDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Line description.  */  
   PackLineLineDesc:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   PackNumName:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
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
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   RMALineLineDesc:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Description.  */  
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNTranListTableset{
   SNTranList:Erp_Tablesets_SNTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SNTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  The serial number of the part that this transaction is for.  */  
   SerialNumber:string,
      /**  A number which is used to allow for a unique key for the file.  */  
   TranNum:number,
      /**  Field that indicates the type of transaction  */  
   TranType:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  Packing slip line that this record is associated with.  */  
   PackLine:number,
      /**  The Service Call that this record is accociated with.  */  
   CallNum:number,
      /**  The Service Call line that this record is accociated with.  */  
   CallLine:number,
      /**  The RMA that this record is accociated with.  */  
   RMANum:number,
      /**  The RMA detail that this record is accociated with.  */  
   RMALine:number,
      /**  Entry Person  */  
   EntryPerson:string,
      /**  The date of the tranaction  */  
   TranDate:string,
      /**  Job number.  The job number that this item is linked to.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Seq # of specific material or subcontract operation record.  */  
   MtlSeq:number,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackSlipLine:number,
      /**  A Standard prefix that will be attached to all Serial Numbers for a particular part.  */  
   SNPrefix:string,
      /**  Format of the Base number.  */  
   SNFormat:string,
      /**  Information about serail number formatting.  */  
   SNBaseStructure:string,
      /**  Base number of Serial Number, needed mainly for adding ranges of numbers.  */  
   SNBaseNumber:string,
      /**  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  */  
   ScrapReasonCode:string,
      /**  A generic fill-in field that could be used to allow the user to enter data.  */  
   SNReference:string,
      /**  RMA receipt  */  
   RMAReceipt:number,
      /**  DMR Number to identify the DMR record.  */  
   DMRNum:number,
      /**  System Date  */  
   SysDate:string,
      /**  System time  */  
   SysTime:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  */  
   OprSeq:number,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  The latest of the 3 warranty expiration dates  */  
   WarrExpiration:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfNum:number,
      /**  Transfer Order packing slip.  */  
   TFPackNum:number,
      /**  Transfer Order packing slip line.  */  
   TFPackLine:number,
      /**  Related (OrderHed) Sales Order number  */  
   OrderNum:number,
      /**  Related (OrderDtl) sales order line number  */  
   OrderLine:number,
      /**  related (OrderRel) order release number  */  
   OrderRelNum:number,
      /**  The status of this serial numbered item prior to its current status.  */  
   PrevSNStatus:string,
      /**  Used to tie back to the related RMADisp record.  */  
   RMADisp:number,
      /**  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  */  
   ShippedFrom:string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   SNStatus:string,
      /**  Indicates that this serial number has been voided.  */  
   Voided:boolean,
      /**  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  */  
   FullyMatched:boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  The Serial Mask ID that was used when a serial number was created.  */  
   SNMask:string,
      /**  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  */  
   AddedByMatching:boolean,
      /**  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  Indicates that this serial numbered item has been scrapped.  */  
   Scrapped:boolean,
      /**  DMR action number.  */  
   DMRActionNum:number,
      /**  Indicates that this item has failed inspection.  */  
   FailSelect:boolean,
      /**  Identifies the contract record along with Company, contractNum, ContractLine.  */  
   LineDetailNum:number,
      /**  Added at shipment  */  
   TranAdd:boolean,
      /**  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  */  
   SubConOprSeq:number,
      /**  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborHedSeq:number,
      /**  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  */  
   ScrapLaborDtlSeq:number,
      /**  The last OperSeq in Labor entry where this serial number was flagged as completed.  */  
   LastLbrOprSeq:number,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   LotNum:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Next Labor Operation Sequence  */  
   NextLbrOprSeq:number,
      /**  Next Labor Assembly Sequence  */  
   NextLbrAssySeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ShipToCustNum  */  
   ShipToCustNum:number,
      /**  Latitude  */  
   Latitude:number,
      /**  Longitude  */  
   Longitude:number,
      /**  Altitude  */  
   Altitude:number,
      /**  FSAssetClassCode  */  
   FSAssetClassCode:string,
      /**  FSServiceLevelAgreement  */  
   FSServiceLevelAgreement:string,
      /**  Accuracy  */  
   Accuracy:number,
      /**  MeterReading  */  
   MeterReading:number,
      /**  One time shipto flag  */  
   OTS:boolean,
      /**  OTS Address 1  */  
   OTSAddress1:string,
      /**  OTS Address 2  */  
   OTSAddress2:string,
      /**  OTS Address 3  */  
   OTSAddress3:string,
      /**  OTS City  */  
   OTSCity:string,
      /**  OTS Contact  */  
   OTSContact:string,
      /**  OTS Country Number  */  
   OTSCountryNum:number,
      /**  OTS Country Number  */  
   OTSCustSaved:boolean,
      /**  One Time fax number  */  
   OTSFaxNum:string,
      /**  OTS Name  */  
   OTSName:string,
      /**  OTS Phone Number  */  
   OTSPhoneNum:string,
      /**  OTS Resale ID  */  
   OTSResaleID:string,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  OTS Ship To Num  */  
   OTSShipToNum:string,
      /**  OTS State  */  
   OTSState:string,
      /**  OTS Tax Region Code  */  
   OTSTaxRegionCode:string,
      /**  OTS Zip  */  
   OTSZip:string,
      /**  PriorJobNum  */  
   PriorJobNum:string,
      /**  PriorAssemblySeq  */  
   PriorAssemblySeq:number,
      /**  PriorMtlSeq  */  
   PriorMtlSeq:number,
      /**  PriorPartNum  */  
   PriorPartNum:string,
      /**  PCID  */  
   PCID:string,
      /**  MscPackNum  */  
   MscPackNum:number,
      /**  MscPackLine  */  
   MscPackLine:number,
      /**  Identifier of the asset this Serial Number is associated to. When the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AssetNum:string,
      /**  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AdditionNum:number,
      /**  DisposalNum  */  
   DisposalNum:number,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  TFOrdNum  */  
   TFOrdNum:string,
      /**  TFOrdLine  */  
   TFOrdLine:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   DispSysTime:string,
   ShpLegalNum:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CallLineLineDesc:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   DMRNumPartDescription:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   JobNumPartDescription:string,
   PackLineLineDesc:string,
   PackNumName:string,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumSalesUM:string,
   RMALineLineDesc:string,
   SerialNumberSNStatus:string,
   ShipToCustName:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumCountry:string,
   VendorNumZIP:string,
   VendorNumCity:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumName:string,
   WareHouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNTranSearchTableset{
   SNTran:Erp_Tablesets_SNTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtSNTranSearchTableset{
   SNTran:Erp_Tablesets_SNTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param serialNumber
      @param tranNum
   */  
export interface GetByID_input{
   partNum:string,
   serialNumber:string,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_SNTranSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_SNTranSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_SNTranSearchTableset[],
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
   returnObj:Erp_Tablesets_SNTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param serialNumber
   */  
export interface GetNewSNTran_input{
   ds:Erp_Tablesets_SNTranSearchTableset[],
   partNum:string,
   serialNumber:string,
}

export interface GetNewSNTran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SNTranSearchTableset,
}
}

   /** Required : 
      @param whereClauseSNTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSNTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_SNTranSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param rmaNum
      @param rmaLine
      @param rmaReceiptNum
   */  
export interface GetSNTran_input{
   rmaNum:number,
   rmaLine:number,
   rmaReceiptNum:number,
}

export interface GetSNTran_output{
   returnObj:Erp_Tablesets_SNTranSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtSNTranSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtSNTranSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_SNTranSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SNTranSearchTableset,
}
}

