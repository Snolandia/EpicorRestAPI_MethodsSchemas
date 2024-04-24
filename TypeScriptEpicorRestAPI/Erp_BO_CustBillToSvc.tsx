import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CustBillToSvc
// Description: Used as a search object for CustBillTo.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/$metadata", {
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
   Description: Get CustBillToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustBillToes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustBillToRow
   */  
export function get_CustBillToes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustBillToes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustBillToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustBillToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustBillToes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes", {
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
   Summary: Calls GetByID to retrieve the CustBillTo item
   Description: Calls GetByID to retrieve the CustBillTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustBillTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param BTCustNum Desc: BTCustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustBillToRow
   */  
export function get_CustBillToes_Company_CustNum_BTCustNum(Company:string, CustNum:string, BTCustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustBillToRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes(" + Company + "," + CustNum + "," + BTCustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CustBillToRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustBillTo for the service
   Description: Calls UpdateExt to update CustBillTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustBillTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param BTCustNum Desc: BTCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustBillToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustBillToes_Company_CustNum_BTCustNum(Company:string, CustNum:string, BTCustNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes(" + Company + "," + CustNum + "," + BTCustNum + ")", {
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
   Summary: Call UpdateExt to delete CustBillTo item
   Description: Call UpdateExt to delete CustBillTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustBillTo
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param BTCustNum Desc: BTCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustBillToes_Company_CustNum_BTCustNum(Company:string, CustNum:string, BTCustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes(" + Company + "," + CustNum + "," + BTCustNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustBillToListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToListRow)
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
export function get_GetRows(whereClauseCustBillTo:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCustBillTo!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustBillTo=" + whereClauseCustBillTo
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(custNum:string, btCustNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }
   if(typeof btCustNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "btCustNum=" + btCustNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetList" + params, {
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
   Summary: Invoke method GetListByBTCustID
   Description: Calls the normal GetList but returns the list dataset with the starting at.
   OperationID: GetListByBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByBTCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetListByBTCustID", {
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
   Summary: Invoke method GetListForReportFilter
   Description: Retrieves the List Data Set containing CustBillTo records filtered by BTCustNum.
   OperationID: GetListForReportFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForReportFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForReportFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForReportFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetListForReportFilter", {
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
   Summary: Invoke method GetNewCustBillTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustBillTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustBillTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustBillTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCustBillTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetNewCustBillTo", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustBillToListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustBillToRow[],
}

export interface Erp_Tablesets_CustBillToListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   "CustNum":number,
      /**  Indicates the CustNum of the alternate Bill To Customer.  */  
   "BTCustNum":number,
      /**  Indicates whether this Alt Bill To is the default record or not.  */  
   "DefaultBillTo":boolean,
      /**  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  */  
   "InvoiceAddress":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Our Bank Code  */  
   "OurBankCode":string,
      /**  Full Legal name  */  
   "BTLegalName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BTAddress one from the Cusomer table for this AltBTCustNum.  */  
   "BTAddress1":string,
      /**  BTAddress two from the Customer table for this AltBTCustNum.  */  
   "BTAddress2":string,
      /**  BTAddress three from the Customer table for this AltBTCustNum.  */  
   "BTAddress3":string,
      /**  The BTAddrList from the Customer table for this AltBTCustNum.  */  
   "BTAddrList":string,
      /**  The BTcity from the Customer table for this AltBTCustNum.  */  
   "BTCity":string,
      /**  Primary billing contact.  */  
   "BTConPrc":number,
      /**  Contact name.  */  
   "BTContactName":string,
      /**  The BTCountry from the Customer table for this AltBTCustNum.  */  
   "BTCountry":string,
      /**  The BT Customer ID from the Customer table for this AltBTCustNum.  */  
   "BTCustID":string,
      /**  The BT Customer Name from the Customer table for this AltBTCustNum.  */  
   "BTCustomerName":string,
      /**  The BTFaxNum from the Customer table for this AltBTCustNum.  */  
   "BTFaxNum":string,
      /**  The BTPhoneNum from the Customer table for this AltBTCustNum.  */  
   "BTPhoneNum":string,
      /**  The BTState from the Customer Table for this AltBTCustNum.  */  
   "BTState":string,
      /**  The BTZip from the Customer table for this AltBTCustNum.  */  
   "BTZip":string,
      /**  Customer ID from the Customer table for this AltBTCustNum.  */  
   "CustID":string,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  */  
   "GlbLink":string,
      /**  Indicates if CustBillTo is Global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  Bill to credit hold flag.  */  
   "BTCreditHold":boolean,
      /**  The Customer Name from the Customer table for this AltBTCustNum.  */  
   "CustomerName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CustBillToRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   "CustNum":number,
      /**  Indicates the CustNum of the alternate Bill To Customer.  */  
   "BTCustNum":number,
      /**  Indicates whether this Alt Bill To is the default record or not.  */  
   "DefaultBillTo":boolean,
      /**  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  */  
   "InvoiceAddress":boolean,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Our Bank Code  */  
   "OurBankCode":string,
      /**  Full Legal name  */  
   "BTLegalName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  If this value is true, the Customer that is designated as the Alternate Bill To has not been sent to FSA.  */  
   "FSACustomerNotSent":boolean,
      /**  BTAddress one from the Cusomer table for this AltBTCustNum.  */  
   "BTAddress1":string,
      /**  BTAddress two from the Customer table for this AltBTCustNum.  */  
   "BTAddress2":string,
      /**  BTAddress three from the Customer table for this AltBTCustNum.  */  
   "BTAddress3":string,
      /**  The BTAddrList from the Customer table for this AltBTCustNum.  */  
   "BTAddrList":string,
      /**  The BTcity from the Customer table for this AltBTCustNum.  */  
   "BTCity":string,
      /**  Primary billing contact.  */  
   "BTConPrc":number,
      /**  Contact name.  */  
   "BTContactName":string,
      /**  The BTCountry from the Customer table for this AltBTCustNum.  */  
   "BTCountry":string,
      /**  Bill to credit hold flag.  */  
   "BTCreditHold":boolean,
      /**  The BT Customer ID from the Customer table for this AltBTCustNum.  */  
   "BTCustID":string,
      /**  The BT Customer Name from the Customer table for this AltBTCustNum.  */  
   "BTCustomerName":string,
      /**  The BTFaxNum from the Customer table for this AltBTCustNum.  */  
   "BTFaxNum":string,
      /**  The BTPhoneNum from the Customer table for this AltBTCustNum.  */  
   "BTPhoneNum":string,
      /**  The BTState from the Customer Table for this AltBTCustNum.  */  
   "BTState":string,
      /**  The BTZip from the Customer table for this AltBTCustNum.  */  
   "BTZip":string,
      /**  Customer ID from the Customer table for this AltBTCustNum.  */  
   "CustID":string,
      /**  The Customer Name from the Customer table for this AltBTCustNum.  */  
   "CustomerName":string,
      /**  Indicates if CustBillTo is Global (Master or Linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  */  
   "GlbLink":string,
      /**  The full formatted address from the Customer table for this AltBTCustNum.  */  
   "BTAddress":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param custNum
      @param btCustNum
   */  
export interface DeleteByID_input{
   custNum:number,
   btCustNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CustBillToListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Indicates the CustNum of the alternate Bill To Customer.  */  
   BTCustNum:number,
      /**  Indicates whether this Alt Bill To is the default record or not.  */  
   DefaultBillTo:boolean,
      /**  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  */  
   InvoiceAddress:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Our Bank Code  */  
   OurBankCode:string,
      /**  Full Legal name  */  
   BTLegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BTAddress one from the Cusomer table for this AltBTCustNum.  */  
   BTAddress1:string,
      /**  BTAddress two from the Customer table for this AltBTCustNum.  */  
   BTAddress2:string,
      /**  BTAddress three from the Customer table for this AltBTCustNum.  */  
   BTAddress3:string,
      /**  The BTAddrList from the Customer table for this AltBTCustNum.  */  
   BTAddrList:string,
      /**  The BTcity from the Customer table for this AltBTCustNum.  */  
   BTCity:string,
      /**  Primary billing contact.  */  
   BTConPrc:number,
      /**  Contact name.  */  
   BTContactName:string,
      /**  The BTCountry from the Customer table for this AltBTCustNum.  */  
   BTCountry:string,
      /**  The BT Customer ID from the Customer table for this AltBTCustNum.  */  
   BTCustID:string,
      /**  The BT Customer Name from the Customer table for this AltBTCustNum.  */  
   BTCustomerName:string,
      /**  The BTFaxNum from the Customer table for this AltBTCustNum.  */  
   BTFaxNum:string,
      /**  The BTPhoneNum from the Customer table for this AltBTCustNum.  */  
   BTPhoneNum:string,
      /**  The BTState from the Customer Table for this AltBTCustNum.  */  
   BTState:string,
      /**  The BTZip from the Customer table for this AltBTCustNum.  */  
   BTZip:string,
      /**  Customer ID from the Customer table for this AltBTCustNum.  */  
   CustID:string,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  */  
   GlbLink:string,
      /**  Indicates if CustBillTo is Global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  Bill to credit hold flag.  */  
   BTCreditHold:boolean,
      /**  The Customer Name from the Customer table for this AltBTCustNum.  */  
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustBillToListTableset{
   CustBillToList:Erp_Tablesets_CustBillToListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustBillToRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Indicates the CustNum of the alternate Bill To Customer.  */  
   BTCustNum:number,
      /**  Indicates whether this Alt Bill To is the default record or not.  */  
   DefaultBillTo:boolean,
      /**  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  */  
   InvoiceAddress:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Our Bank Code  */  
   OurBankCode:string,
      /**  Full Legal name  */  
   BTLegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If this value is true, the Customer that is designated as the Alternate Bill To has not been sent to FSA.  */  
   FSACustomerNotSent:boolean,
      /**  BTAddress one from the Cusomer table for this AltBTCustNum.  */  
   BTAddress1:string,
      /**  BTAddress two from the Customer table for this AltBTCustNum.  */  
   BTAddress2:string,
      /**  BTAddress three from the Customer table for this AltBTCustNum.  */  
   BTAddress3:string,
      /**  The BTAddrList from the Customer table for this AltBTCustNum.  */  
   BTAddrList:string,
      /**  The BTcity from the Customer table for this AltBTCustNum.  */  
   BTCity:string,
      /**  Primary billing contact.  */  
   BTConPrc:number,
      /**  Contact name.  */  
   BTContactName:string,
      /**  The BTCountry from the Customer table for this AltBTCustNum.  */  
   BTCountry:string,
      /**  Bill to credit hold flag.  */  
   BTCreditHold:boolean,
      /**  The BT Customer ID from the Customer table for this AltBTCustNum.  */  
   BTCustID:string,
      /**  The BT Customer Name from the Customer table for this AltBTCustNum.  */  
   BTCustomerName:string,
      /**  The BTFaxNum from the Customer table for this AltBTCustNum.  */  
   BTFaxNum:string,
      /**  The BTPhoneNum from the Customer table for this AltBTCustNum.  */  
   BTPhoneNum:string,
      /**  The BTState from the Customer Table for this AltBTCustNum.  */  
   BTState:string,
      /**  The BTZip from the Customer table for this AltBTCustNum.  */  
   BTZip:string,
      /**  Customer ID from the Customer table for this AltBTCustNum.  */  
   CustID:string,
      /**  The Customer Name from the Customer table for this AltBTCustNum.  */  
   CustomerName:string,
      /**  Indicates if CustBillTo is Global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  */  
   GlbLink:string,
      /**  The full formatted address from the Customer table for this AltBTCustNum.  */  
   BTAddress:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustBillToTableset{
   CustBillTo:Erp_Tablesets_CustBillToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCustBillToTableset{
   CustBillTo:Erp_Tablesets_CustBillToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param custNum
      @param btCustNum
   */  
export interface GetByID_input{
   custNum:number,
   btCustNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CustBillToTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CustBillToTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CustBillToTableset[],
}

   /** Required : 
      @param custNum
      @param btCustID
      @param pageSize
      @param absolutePage
   */  
export interface GetListByBTCustID_input{
      /**  Sold to customer number.  */  
   custNum:number,
      /**  BTCustID to start at and sort by.  */  
   btCustID:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListByBTCustID_output{
   returnObj:Erp_Tablesets_CustBillToListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param customers
   */  
export interface GetListForReportFilter_input{
      /**  List of customers separated by '~'.  */  
   customers:string,
}

export interface GetListForReportFilter_output{
   returnObj:Erp_Tablesets_CustBillToListTableset[],
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
   returnObj:Erp_Tablesets_CustBillToListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param custNum
   */  
export interface GetNewCustBillTo_input{
   ds:Erp_Tablesets_CustBillToTableset[],
   custNum:number,
}

export interface GetNewCustBillTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustBillToTableset[],
}
}

   /** Required : 
      @param whereClauseCustBillTo
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCustBillTo:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CustBillToTableset[],
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
   ds:Erp_Tablesets_UpdExtCustBillToTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCustBillToTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CustBillToTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CustBillToTableset[],
}
}

