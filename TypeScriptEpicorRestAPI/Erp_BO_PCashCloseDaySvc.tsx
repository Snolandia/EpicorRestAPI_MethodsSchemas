import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PCashCloseDaySvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/$metadata", {
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
   Description: Get PCashCloseDays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashCloseDays
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashBalRow
   */  
export function get_PCashCloseDays(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashCloseDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashBalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashBalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashCloseDays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays", {
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
   Summary: Calls GetByID to retrieve the PCashCloseDay item
   Description: Calls GetByID to retrieve the PCashCloseDay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashCloseDay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param Date Desc: Date   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashBalRow
   */  
export function get_PCashCloseDays_Company_CashDeskID_Date(Company:string, CashDeskID:string, Date:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashBalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays(" + Company + "," + CashDeskID + "," + Date + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashBalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashCloseDay for the service
   Description: Calls UpdateExt to update PCashCloseDay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashCloseDay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param Date Desc: Date   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashBalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashCloseDays_Company_CashDeskID_Date(Company:string, CashDeskID:string, Date:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays(" + Company + "," + CashDeskID + "," + Date + ")", {
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
   Summary: Call UpdateExt to delete PCashCloseDay item
   Description: Call UpdateExt to delete PCashCloseDay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashCloseDay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param Date Desc: Date   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashCloseDays_Company_CashDeskID_Date(Company:string, CashDeskID:string, Date:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/PCashCloseDays(" + Company + "," + CashDeskID + "," + Date + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashBalListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalListRow)
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
export function get_GetRows(whereClausePCashBal:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePCashBal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashBal=" + whereClausePCashBal
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(cashDeskID:string, date:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof cashDeskID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cashDeskID=" + cashDeskID
   }
   if(typeof date!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "date=" + date
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/GetList" + params, {
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
   Summary: Invoke method ClosePettyCashDay
   Description: Close a day for a petty cash desk.
   OperationID: ClosePettyCashDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePettyCashDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePettyCashDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClosePettyCashDay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/ClosePettyCashDay", {
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
   Summary: Invoke method GetNewPCashBal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/GetNewPCashBal", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashCloseDaySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashBalListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashBalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashBalRow[],
}

export interface Erp_Tablesets_PCashBalListRow{
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashBalRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**  A unique value. Date for which calculated Cash Desk Balances.  */  
   "Date":string,
      /**  Number of Cash Issue Documents per day  */  
   "CashIssueCount":number,
      /**  Number of Cash Receipt Documents per day  */  
   "CashRcptCount":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Day is Closed  */  
   "DayIsClosed":boolean,
      /**  Total cash amount received per day  */  
   "DocRcvCashAmt":number,
      /**  Total cash amount received per day  */  
   "RcvCashAmt":number,
      /**  Total cash amount received per day in reporting Currency  */  
   "Rpt1RcvCashAmt":number,
      /**  Total cash amount received per day in reporting Currency  */  
   "Rpt2RcvCashAmt":number,
      /**  Total cash amount received per day in reporting Currency  */  
   "Rpt3RcvCashAmt":number,
      /**  Total cash amount received per day by payroll operations only  */  
   "DocRcvPayrollAmt":number,
      /**  Total cash amount received per day by payroll operations only  */  
   "RcvPayrollAmt":number,
      /**  Received Payroll Amount in reporting Currency  */  
   "Rpt1RcvPayrollAmt":number,
      /**  Received Payroll Amount in reporting Currency  */  
   "Rpt2RcvPayrollAmt":number,
      /**  Received Payroll Amount in reporting Currency  */  
   "Rpt3RcvPayrollAmt":number,
      /**  Total cash amount received per day with draft document amounts  */  
   "DocTotalRcvAmt":number,
      /**  Total cash amount received per day with draft document amounts  */  
   "RcvTotalAmt":number,
      /**  Total cash amount received per day with draft document amounts in reporting Currency  */  
   "Rpt1RcvTotalAmt":number,
      /**  Total cash amount received per day with draft document amounts in reporting Currency  */  
   "Rpt2RcvTotalAmt":number,
      /**  Total cash amount received per day with draft document amounts in reporting Currency.  */  
   "Rpt3RcvTotalAmt":number,
      /**  Total cash amount Issued per day.  */  
   "DocIssCashAmt":number,
      /**  Total cash amount Issued per day  */  
   "IssCashAmt":number,
      /**  Total cash amount Issued per day in reporting Currency  */  
   "Rpt1IssCashAmt":number,
      /**  Total cash amount Issued per day in reporting Currency  */  
   "Rpt2IssCashAmt":number,
      /**  Total cash amount Issued per day in reporting Currency  */  
   "Rpt3IssCashAmt":number,
      /**  Total cash amount Issued per day by payroll operations only  */  
   "DocIssPayrollAmt":number,
      /**  Total cash amount Issued per day by payroll operations only  */  
   "IssPayrollAmt":number,
      /**  Issued Payroll Amount in reporting Currency  */  
   "Rpt1IssPayrollAmt":number,
      /**  Issued Payroll Amount in reporting Currency  */  
   "Rpt2IssPayrollAmt":number,
      /**  Issued Payroll Amount in reporting Currency  */  
   "Rpt3IssPayrollAmt":number,
      /**  Total cash amount Issued per day with draft document amounts  */  
   "DocIssTotalAmt":number,
      /**  Total cash amount Issued per day with draft document amounts  */  
   "IssTotalAmt":number,
      /**  Total cash amount Issued per day with draft document amounts in reporting Currency  */  
   "Rpt1IssTotalAmt":number,
      /**  Total cash amount Issued per day with draft document amounts in reporting Currency  */  
   "Rpt2IssTotalAmt":number,
      /**  Total cash amount Issued per day with draft document amounts in reporting Currency  */  
   "Rpt3IssTotalAmt":number,
      /**  Cash Desk Day Closing Balance  */  
   "DocDayBal":number,
      /**  Cash Desk Day Closing Balance  */  
   "DayBal":number,
      /**  Cash Desk Day Closing Balance in reporting Currency  */  
   "Rpt1DayBal":number,
      /**  Cash Desk Day Closing Balance in reporting Currency  */  
   "Rpt2DayBal":number,
      /**  Cash Desk Day Closing Balance in reporting Currency  */  
   "Rpt3DayBal":number,
      /**  Cash Desk Day Closing Payroll Balance  */  
   "DocPayrollDayBal":number,
      /**  Cash Desk Day Closing Payroll Balance  */  
   "PayrollDayBal":number,
      /**  Cash Desk Day Closing Payroll Balance in reporting Currency  */  
   "Rpt1PayrollDayBal":number,
      /**  Cash Desk Day Closing Payroll Balance in reporting Currency  */  
   "Rpt2PayrollDayBal":number,
      /**  Cash Desk Day Closing Payroll Balance in reporting Currency  */  
   "Rpt3PayrollDayBal":number,
      /**  Cash Desk Day Closing Balance with draft document amounts  */  
   "DocDayBalWithDraft":number,
      /**  Cash Desk Day Closing Balance with draft document amounts  */  
   "DayBalWithDraft":number,
      /**  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  */  
   "Rpt1DayBalWithDraft":number,
      /**  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  */  
   "Rpt2DayBalWithDraft":number,
      /**  Cash Desk Day Closing Balance with draft document amounts in reporting Currency  */  
   "Rpt3DayBalWithDraft":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  GainLossBal  */  
   "GainLossBal":number,
      /**  DocGainLossBal  */  
   "DocGainLossBal":number,
      /**  Rpt1GainLossBal  */  
   "Rpt1GainLossBal":number,
      /**  Rpt2GainLossBal  */  
   "Rpt2GainLossBal":number,
      /**  Rpt3GainLossBal  */  
   "Rpt3GainLossBal":number,
      /**  PrintedOfficial  */  
   "PrintedOfficial":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param cashDeskID
      @param dteUpto
      @param dtePrgDraftsBefore
   */  
export interface ClosePettyCashDay_input{
      /**  Cash Desk ID.  */  
   cashDeskID:string,
      /**  Close Up to Date.  */  
   dteUpto:string,
      /**  Purge Drafts Before date.  */  
   dtePrgDraftsBefore:string,
}

export interface ClosePettyCashDay_output{
}

   /** Required : 
      @param cashDeskID
      @param date
   */  
export interface DeleteByID_input{
   cashDeskID:string,
   date:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PCashBalListRow{
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashBalRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  A unique value. Date for which calculated Cash Desk Balances.  */  
   Date:string,
      /**  Number of Cash Issue Documents per day  */  
   CashIssueCount:number,
      /**  Number of Cash Receipt Documents per day  */  
   CashRcptCount:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Day is Closed  */  
   DayIsClosed:boolean,
      /**  Total cash amount received per day  */  
   DocRcvCashAmt:number,
      /**  Total cash amount received per day  */  
   RcvCashAmt:number,
      /**  Total cash amount received per day in reporting Currency  */  
   Rpt1RcvCashAmt:number,
      /**  Total cash amount received per day in reporting Currency  */  
   Rpt2RcvCashAmt:number,
      /**  Total cash amount received per day in reporting Currency  */  
   Rpt3RcvCashAmt:number,
      /**  Total cash amount received per day by payroll operations only  */  
   DocRcvPayrollAmt:number,
      /**  Total cash amount received per day by payroll operations only  */  
   RcvPayrollAmt:number,
      /**  Received Payroll Amount in reporting Currency  */  
   Rpt1RcvPayrollAmt:number,
      /**  Received Payroll Amount in reporting Currency  */  
   Rpt2RcvPayrollAmt:number,
      /**  Received Payroll Amount in reporting Currency  */  
   Rpt3RcvPayrollAmt:number,
      /**  Total cash amount received per day with draft document amounts  */  
   DocTotalRcvAmt:number,
      /**  Total cash amount received per day with draft document amounts  */  
   RcvTotalAmt:number,
      /**  Total cash amount received per day with draft document amounts in reporting Currency  */  
   Rpt1RcvTotalAmt:number,
      /**  Total cash amount received per day with draft document amounts in reporting Currency  */  
   Rpt2RcvTotalAmt:number,
      /**  Total cash amount received per day with draft document amounts in reporting Currency.  */  
   Rpt3RcvTotalAmt:number,
      /**  Total cash amount Issued per day.  */  
   DocIssCashAmt:number,
      /**  Total cash amount Issued per day  */  
   IssCashAmt:number,
      /**  Total cash amount Issued per day in reporting Currency  */  
   Rpt1IssCashAmt:number,
      /**  Total cash amount Issued per day in reporting Currency  */  
   Rpt2IssCashAmt:number,
      /**  Total cash amount Issued per day in reporting Currency  */  
   Rpt3IssCashAmt:number,
      /**  Total cash amount Issued per day by payroll operations only  */  
   DocIssPayrollAmt:number,
      /**  Total cash amount Issued per day by payroll operations only  */  
   IssPayrollAmt:number,
      /**  Issued Payroll Amount in reporting Currency  */  
   Rpt1IssPayrollAmt:number,
      /**  Issued Payroll Amount in reporting Currency  */  
   Rpt2IssPayrollAmt:number,
      /**  Issued Payroll Amount in reporting Currency  */  
   Rpt3IssPayrollAmt:number,
      /**  Total cash amount Issued per day with draft document amounts  */  
   DocIssTotalAmt:number,
      /**  Total cash amount Issued per day with draft document amounts  */  
   IssTotalAmt:number,
      /**  Total cash amount Issued per day with draft document amounts in reporting Currency  */  
   Rpt1IssTotalAmt:number,
      /**  Total cash amount Issued per day with draft document amounts in reporting Currency  */  
   Rpt2IssTotalAmt:number,
      /**  Total cash amount Issued per day with draft document amounts in reporting Currency  */  
   Rpt3IssTotalAmt:number,
      /**  Cash Desk Day Closing Balance  */  
   DocDayBal:number,
      /**  Cash Desk Day Closing Balance  */  
   DayBal:number,
      /**  Cash Desk Day Closing Balance in reporting Currency  */  
   Rpt1DayBal:number,
      /**  Cash Desk Day Closing Balance in reporting Currency  */  
   Rpt2DayBal:number,
      /**  Cash Desk Day Closing Balance in reporting Currency  */  
   Rpt3DayBal:number,
      /**  Cash Desk Day Closing Payroll Balance  */  
   DocPayrollDayBal:number,
      /**  Cash Desk Day Closing Payroll Balance  */  
   PayrollDayBal:number,
      /**  Cash Desk Day Closing Payroll Balance in reporting Currency  */  
   Rpt1PayrollDayBal:number,
      /**  Cash Desk Day Closing Payroll Balance in reporting Currency  */  
   Rpt2PayrollDayBal:number,
      /**  Cash Desk Day Closing Payroll Balance in reporting Currency  */  
   Rpt3PayrollDayBal:number,
      /**  Cash Desk Day Closing Balance with draft document amounts  */  
   DocDayBalWithDraft:number,
      /**  Cash Desk Day Closing Balance with draft document amounts  */  
   DayBalWithDraft:number,
      /**  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  */  
   Rpt1DayBalWithDraft:number,
      /**  Cash Desk Day Closing Balance with draft document amounts  in reporting Currency  */  
   Rpt2DayBalWithDraft:number,
      /**  Cash Desk Day Closing Balance with draft document amounts in reporting Currency  */  
   Rpt3DayBalWithDraft:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  GainLossBal  */  
   GainLossBal:number,
      /**  DocGainLossBal  */  
   DocGainLossBal:number,
      /**  Rpt1GainLossBal  */  
   Rpt1GainLossBal:number,
      /**  Rpt2GainLossBal  */  
   Rpt2GainLossBal:number,
      /**  Rpt3GainLossBal  */  
   Rpt3GainLossBal:number,
      /**  PrintedOfficial  */  
   PrintedOfficial:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashCloseDayListTableset{
   PCashBalList:Erp_Tablesets_PCashBalListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCashCloseDayTableset{
   PCashBal:Erp_Tablesets_PCashBalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPCashCloseDayTableset{
   PCashBal:Erp_Tablesets_PCashBalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cashDeskID
      @param date
   */  
export interface GetByID_input{
   cashDeskID:string,
   date:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PCashCloseDayTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PCashCloseDayTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PCashCloseDayTableset[],
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
   returnObj:Erp_Tablesets_PCashCloseDayListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param cashDeskID
   */  
export interface GetNewPCashBal_input{
   ds:Erp_Tablesets_PCashCloseDayTableset[],
   cashDeskID:string,
}

export interface GetNewPCashBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashCloseDayTableset[],
}
}

   /** Required : 
      @param whereClausePCashBal
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePCashBal:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PCashCloseDayTableset[],
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
   ds:Erp_Tablesets_UpdExtPCashCloseDayTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPCashCloseDayTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PCashCloseDayTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashCloseDayTableset[],
}
}

