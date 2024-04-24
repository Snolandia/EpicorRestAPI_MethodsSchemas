import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.RebateTransSvc
// Description: This is the maintenance program for RebateTrans records
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/$metadata", {
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
   Description: Get RebateTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateTransRow
   */  
export function get_RebateTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateTransRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateTransRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RebateTrans(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans", {
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
   Summary: Calls GetByID to retrieve the RebateTran item
   Description: Calls GetByID to retrieve the RebateTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateTransRow
   */  
export function get_RebateTrans_Company_RebateID_LineNum_CustNum_TranNum(Company:string, RebateID:string, LineNum:string, CustNum:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RebateTransRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_RebateTransRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RebateTran for the service
   Description: Calls UpdateExt to update RebateTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateTransRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RebateTrans_Company_RebateID_LineNum_CustNum_TranNum(Company:string, RebateID:string, LineNum:string, CustNum:string, TranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete RebateTran item
   Description: Call UpdateExt to delete RebateTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RebateID Desc: RebateID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param CustNum Desc: CustNum   Required: True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RebateTrans_Company_RebateID_LineNum_CustNum_TranNum(Company:string, RebateID:string, LineNum:string, CustNum:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + "," + TranNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateTransListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransListRow)
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
export function get_GetRows(whereClauseRebateTrans:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRebateTrans!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRebateTrans=" + whereClauseRebateTrans
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/GetRows" + params, {
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
   Required: True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(rebateID:string, lineNum:string, custNum:string, tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rebateID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rebateID=" + rebateID
   }
   if(typeof lineNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lineNum=" + lineNum
   }
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/GetList" + params, {
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
   Summary: Invoke method DeleteAll
   Description: This method deletes all the selected rebate transactions.
   OperationID: DeleteAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/DeleteAll", {
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
   Summary: Invoke method ImportRebateTrans
   Description: Call this method to import rebate transactions into the database.
This method expects an input data table ttImportRebateTrans with data coming
from an external comma delimited file.
   OperationID: ImportRebateTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportRebateTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportRebateTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportRebateTrans(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/ImportRebateTrans", {
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
   Summary: Invoke method ImportFile
   OperationID: ImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/ImportFile", {
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
   Summary: Invoke method GetNewRebateTrans
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRebateTrans(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/GetNewRebateTrans", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateTransListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RebateTransRow[],
}

export interface Erp_Tablesets_RebateTransListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Internal unique identifier for the RebateDtl table  */  
   "LineNum":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  Transaction Number  */  
   "TranNum":number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  Date Created  */  
   "TranDate":string,
      /**  Date of the source transaction  */  
   "InvoiceDate":string,
      /**  Invoiced Quantity  */  
   "Quantity":number,
      /**  Quantity Unit of Measure  */  
   "QuantityUOM":string,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   "RebateAmount":number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   "DocRebateAmount":number,
      /**  Adjustments to the calculated Rebate Amount  */  
   "Adjustments":number,
      /**  Adjustments to the calculated Rebate Amount  */  
   "DocAdjustments":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  */  
   "Void":boolean,
      /**  Indicates that this transaction has been applied against a rebate payment  */  
   "Applied":boolean,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  */  
   "SalesDept":string,
      /**   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  */  
   "SalesDiv":string,
      /**  AP Invoice transaction is associated with (Payment)  */  
   "APInvoiceNum":string,
      /**  AR Invoice transaction is associated with (Credit Memo)  */  
   "ARInvoiceNum":number,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   "ProdCode":string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   "APInvoiceLine":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "ARInvoiceLine":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Adjustments":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Adjustments":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Adjustments":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1RebateAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2RebateAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3RebateAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "NetRebateAmt":number,
      /**  Part UOM  */  
   "PartUOM":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartPricePerCode":string,
      /**  Full description of Product Group.  */  
   "ProdGrupDescription":string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   "RebateDtlProdCode":string,
      /**  Unit of Measure  */  
   "RebateDtlUOMCode":string,
      /**  A unique part number that identifies this part.  */  
   "RebateDtlPartNum":string,
      /**  Rebate Description  */  
   "RebateHdrRebateDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RebateTransRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Identifier for the Rebate  */  
   "RebateID":string,
      /**  Internal unique identifier for the RebateDtl table  */  
   "LineNum":number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  Transaction Number  */  
   "TranNum":number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  Date Created  */  
   "TranDate":string,
      /**  Date of the source transaction  */  
   "InvoiceDate":string,
      /**  Invoiced Quantity  */  
   "Quantity":number,
      /**  Quantity Unit of Measure  */  
   "QuantityUOM":string,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   "RebateAmount":number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   "DocRebateAmount":number,
      /**  Adjustments to the calculated Rebate Amount  */  
   "Adjustments":number,
      /**  Adjustments to the calculated Rebate Amount  */  
   "DocAdjustments":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  */  
   "Void":boolean,
      /**  Indicates that this transaction has been applied against a rebate payment  */  
   "Applied":boolean,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  */  
   "SalesDept":string,
      /**   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  */  
   "SalesDiv":string,
      /**  AP Invoice transaction is associated with (Payment)  */  
   "APInvoiceNum":string,
      /**  AR Invoice transaction is associated with (Credit Memo)  */  
   "ARInvoiceNum":number,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   "ProdCode":string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   "APInvoiceLine":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "ARInvoiceLine":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Adjustments":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Adjustments":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Adjustments":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1RebateAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2RebateAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3RebateAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "NetRebateAmt":number,
      /**  Part UOM  */  
   "PartUOM":string,
   "BitFlag":number,
   "CustomerName":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartTrackDimension":boolean,
   "PartPricePerCode":string,
   "PartSalesUM":string,
   "PartTrackSerialNum":boolean,
   "PartPartDescription":string,
   "PartTrackLots":boolean,
   "ProdGrupDescription":string,
   "RebateDtlPartNum":string,
   "RebateDtlProdCode":string,
   "RebateDtlUOMCode":string,
   "RebateHdrRebateDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface DeleteAll_input{
   ds:Erp_Tablesets_RebateTransTableset[],
}

export interface DeleteAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTransTableset[],
}
}

   /** Required : 
      @param rebateID
      @param lineNum
      @param custNum
      @param tranNum
   */  
export interface DeleteByID_input{
   rebateID:string,
   lineNum:number,
   custNum:number,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ImportRebateTransRow{
   Company:string,
   RebateID:string,
   LineNum:number,
   CustID:string,
   InvoiceNum:number,
   Quantity:number,
   UnitPrice:number,
   ExtPrice:number,
   Discount:number,
   RebateAmount:number,
   Adjustments:number,
   InvoiceLine:number,
   TotalMiscChrg:number,
   Void:boolean,
      /**  Has been applied to a payment or credit memo  */  
   Applied:boolean,
   DocUnitPrice:number,
   DocExtPrice:number,
   DocDiscount:number,
   DocTotalMiscChrg:number,
   DocRebateAmount:number,
   DocAdjustments:number,
   CurrencyCode:string,
   ExchangeRate:number,
   RefCode:string,
   DocToRef:boolean,
   RefToBase:boolean,
   RefToBaseRate:number,
   SalesDept:string,
   SalesDiv:string,
   APInvoiceNum:string,
   ARInvoiceNum:number,
   PartNum:string,
   ProdCode:string,
   InvoiceDate:string,
   APInvoiceLine:number,
   ARInvoiceLine:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportRebateTransTableset{
   ImportRebateTrans:Erp_Tablesets_ImportRebateTransRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RebateTransListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Internal unique identifier for the RebateDtl table  */  
   LineNum:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  Transaction Number  */  
   TranNum:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  Date Created  */  
   TranDate:string,
      /**  Date of the source transaction  */  
   InvoiceDate:string,
      /**  Invoiced Quantity  */  
   Quantity:number,
      /**  Quantity Unit of Measure  */  
   QuantityUOM:string,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   RebateAmount:number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   DocRebateAmount:number,
      /**  Adjustments to the calculated Rebate Amount  */  
   Adjustments:number,
      /**  Adjustments to the calculated Rebate Amount  */  
   DocAdjustments:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  */  
   Void:boolean,
      /**  Indicates that this transaction has been applied against a rebate payment  */  
   Applied:boolean,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  */  
   SalesDept:string,
      /**   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  */  
   SalesDiv:string,
      /**  AP Invoice transaction is associated with (Payment)  */  
   APInvoiceNum:string,
      /**  AR Invoice transaction is associated with (Credit Memo)  */  
   ARInvoiceNum:number,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   ProdCode:string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   APInvoiceLine:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   ARInvoiceLine:number,
      /**  Reporting currency value of this field  */  
   Rpt1Adjustments:number,
      /**  Reporting currency value of this field  */  
   Rpt2Adjustments:number,
      /**  Reporting currency value of this field  */  
   Rpt3Adjustments:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1RebateAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2RebateAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3RebateAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   NetRebateAmt:number,
      /**  Part UOM  */  
   PartUOM:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartTrackLots:boolean,
      /**  Describes the Part.  */  
   PartPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartPricePerCode:string,
      /**  Full description of Product Group.  */  
   ProdGrupDescription:string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   RebateDtlProdCode:string,
      /**  Unit of Measure  */  
   RebateDtlUOMCode:string,
      /**  A unique part number that identifies this part.  */  
   RebateDtlPartNum:string,
      /**  Rebate Description  */  
   RebateHdrRebateDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateTransListTableset{
   RebateTransList:Erp_Tablesets_RebateTransListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RebateTransRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Identifier for the Rebate  */  
   RebateID:string,
      /**  Internal unique identifier for the RebateDtl table  */  
   LineNum:number,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  Transaction Number  */  
   TranNum:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  Date Created  */  
   TranDate:string,
      /**  Date of the source transaction  */  
   InvoiceDate:string,
      /**  Invoiced Quantity  */  
   Quantity:number,
      /**  Quantity Unit of Measure  */  
   QuantityUOM:string,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   RebateAmount:number,
      /**  Amount of Rebate Earned for this transaction (calculated)  */  
   DocRebateAmount:number,
      /**  Adjustments to the calculated Rebate Amount  */  
   Adjustments:number,
      /**  Adjustments to the calculated Rebate Amount  */  
   DocAdjustments:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  */  
   Void:boolean,
      /**  Indicates that this transaction has been applied against a rebate payment  */  
   Applied:boolean,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  */  
   SalesDept:string,
      /**   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  */  
   SalesDiv:string,
      /**  AP Invoice transaction is associated with (Payment)  */  
   APInvoiceNum:string,
      /**  AR Invoice transaction is associated with (Credit Memo)  */  
   ARInvoiceNum:number,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  */  
   ProdCode:string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   APInvoiceLine:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   ARInvoiceLine:number,
      /**  Reporting currency value of this field  */  
   Rpt1Adjustments:number,
      /**  Reporting currency value of this field  */  
   Rpt2Adjustments:number,
      /**  Reporting currency value of this field  */  
   Rpt3Adjustments:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1RebateAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2RebateAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3RebateAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   NetRebateAmt:number,
      /**  Part UOM  */  
   PartUOM:string,
   BitFlag:number,
   CustomerName:string,
   CustomerCustID:string,
   CustomerBTName:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartSalesUM:string,
   PartTrackSerialNum:boolean,
   PartPartDescription:string,
   PartTrackLots:boolean,
   ProdGrupDescription:string,
   RebateDtlPartNum:string,
   RebateDtlProdCode:string,
   RebateDtlUOMCode:string,
   RebateHdrRebateDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RebateTransTableset{
   RebateTrans:Erp_Tablesets_RebateTransRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRebateTransTableset{
   RebateTrans:Erp_Tablesets_RebateTransRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rebateID
      @param lineNum
      @param custNum
      @param tranNum
   */  
export interface GetByID_input{
   rebateID:string,
   lineNum:number,
   custNum:number,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RebateTransTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RebateTransTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RebateTransTableset[],
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
   returnObj:Erp_Tablesets_RebateTransListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rebateID
      @param lineNum
      @param custNum
   */  
export interface GetNewRebateTrans_input{
   ds:Erp_Tablesets_RebateTransTableset[],
   rebateID:string,
   lineNum:number,
   custNum:number,
}

export interface GetNewRebateTrans_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTransTableset[],
}
}

   /** Required : 
      @param whereClauseRebateTrans
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRebateTrans:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RebateTransTableset[],
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
      @param fileName
      @param ds
   */  
export interface ImportFile_input{
   fileName:string,
   ds:Erp_Tablesets_RebateTransTableset[],
}

export interface ImportFile_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_RebateTransTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ImportRebateTrans_input{
   ds:Erp_Tablesets_ImportRebateTransTableset[],
}

export interface ImportRebateTrans_output{
   returnObj:Erp_Tablesets_RebateTransTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportRebateTransTableset[],
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtRebateTransTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRebateTransTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RebateTransTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RebateTransTableset[],
}
}

