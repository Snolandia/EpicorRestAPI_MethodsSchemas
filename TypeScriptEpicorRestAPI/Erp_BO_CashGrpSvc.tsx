import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CashGrpSvc
// Description: bo/CashGrp/CashGrp.p
           Cash Group Entry - separated from CashRec.p
           Jennifer Johnson
           03/18/04
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/$metadata", {
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
   Description: Get CashGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashGrps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpRow
   */  
export function get_CashGrps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CashGrps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps", {
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
   Summary: Calls GetByID to retrieve the CashGrp item
   Description: Calls GetByID to retrieve the CashGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashGrpRow
   */  
export function get_CashGrps_Company_GroupID(Company:string, GroupID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CashGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CashGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CashGrp for the service
   Description: Calls UpdateExt to update CashGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CashGrps_Company_GroupID(Company:string, GroupID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete CashGrp item
   Description: Call UpdateExt to delete CashGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CashGrps_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/CashGrps(" + Company + "," + GroupID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpListRow)
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
export function get_GetRows(whereClauseCashGrp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCashGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCashGrp=" + whereClauseCashGrp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetRows" + params, {
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
export function get_GetByID(groupID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: This method returns a code/description list string for the table name and field name passed in
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetCodeDescList", {
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
   Summary: Invoke method BeforeGetByID
   Description: This method checks to see if the selected group is in use before fetching the dataset
if the group is in use, the user must answer yes to continue before the GetByID method is run
   OperationID: BeforeGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BeforeGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BeforeGetByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/BeforeGetByID", {
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
   Summary: Invoke method GetByIDNoLock
   Description: Returns a DataSet given the primary key. Active user locking disabled.
   OperationID: GetByIDNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetByIDNoLock", {
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
   Summary: Invoke method GetNewCashGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewCashGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetNewCashGrpNoLock", {
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
   Summary: Invoke method GetRowsNoLock
   Description: GetRows method with disabled ActiveUser functionality.
   OperationID: GetRowsNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetRowsNoLock", {
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
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since Payments TAx logic calculates tax conditionally only for the first tax line the payment could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteZeroAmtTaxRec(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/DeleteZeroAmtTaxRec", {
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
   Summary: Invoke method GetGrpBankInfo
   Description: This method is called when the Bank Account changes
   OperationID: GetGrpBankInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGrpBankInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrpBankInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGrpBankInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetGrpBankInfo", {
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
   Summary: Invoke method GetGrpFiscal
   Description: This method is run when the Transaction date is changed to update the fiscal period fields
   OperationID: GetGrpFiscal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGrpFiscal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrpFiscal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGrpFiscal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetGrpFiscal", {
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
   Summary: Invoke method GetNewCashGrpForPINoLock
   Description: GetNewCashGrpForPI with active user locking disabled.
   OperationID: GetNewCashGrpForPINoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPINoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPINoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpForPINoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetNewCashGrpForPINoLock", {
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
   Summary: Invoke method GetNewCashGrpForPI
   OperationID: GetNewCashGrpForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpForPI(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetNewCashGrpForPI", {
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
   Summary: Invoke method GetNewCashGrpForPIStatusNoLock
   Description: GetNewCashGrpForPIStatus with active user locking disabled.
   OperationID: GetNewCashGrpForPIStatusNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPIStatusNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPIStatusNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpForPIStatusNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetNewCashGrpForPIStatusNoLock", {
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
   Summary: Invoke method GetNewCashGrpForPIStatus
   OperationID: GetNewCashGrpForPIStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpForPIStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpForPIStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrpForPIStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetNewCashGrpForPIStatus", {
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
   Summary: Invoke method GetPIGroupByID
   OperationID: GetPIGroupByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPIGroupByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPIGroupByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPIGroupByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetPIGroupByID", {
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
   Summary: Invoke method IsPIGroup
   Description: This method verifies a Cash Group exists and returns the different types of group flags for further use.
   OperationID: IsPIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsPIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsPIGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/IsPIGroup", {
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
   Summary: Invoke method LockPIGroup
   Description: Should be call before GetPIGroupByID to lock the Group.
   OperationID: LockPIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockPIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockPIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockPIGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/LockPIGroup", {
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
   Summary: Invoke method LockPIGroupInDS
   Description: Should be call before GetPIGroupByID to lock the Group.
   OperationID: LockPIGroupInDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockPIGroupInDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockPIGroupInDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockPIGroupInDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/LockPIGroupInDS", {
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
   Summary: Invoke method UnlockPIGroup
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockPIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockPIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockPIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockPIGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/UnlockPIGroup", {
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
   Summary: Invoke method UnlockPIGroupInDS
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockPIGroupInDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockPIGroupInDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockPIGroupInDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockPIGroupInDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/UnlockPIGroupInDS", {
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
   Summary: Invoke method GetPIStatusGroupByID
   OperationID: GetPIStatusGroupByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPIStatusGroupByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPIStatusGroupByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPIStatusGroupByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetPIStatusGroupByID", {
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
   Summary: Invoke method LeaveCashGrp
   Description: This method must be run whenever the use is leaving the current CashGrp record
(either by selecting a new Group or by leaving the screen)
   OperationID: LeaveCashGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveCashGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveCashGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveCashGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/LeaveCashGrp", {
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
   Summary: Invoke method PrePostEPGroup
   Description: This method is for Electronically processed group
This method first checks if the Group Receipt/Payment was processed and CashGrp.EIPaymSent field is true
This method checks that the A/R is interfaced to the G/L. If not, then ask the
user if they want to go ahead and post the cash receipts
   OperationID: PrePostEPGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostEPGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostEPGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostEPGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/PrePostEPGroup", {
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
   Summary: Invoke method PrePostGroup
   Description: This method checks that the A/R is interfaced to the G/L.  If not, then ask the
user if they want to go ahead and post the cash receipts
This method also checks if this Group has any related Tax Records with 0 amounts
The user is asked if these records are supposed to be deleted before Post
   OperationID: PrePostGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/PrePostGroup", {
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
   Summary: Invoke method UpdateMaster
   Description: This method is called instead of the standard Update
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/UpdateMaster", {
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
   Summary: Invoke method ReceiptGroupExists
   Description: This method is called to check if group with entered ID exists
   OperationID: ReceiptGroupExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiptGroupExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiptGroupExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiptGroupExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/ReceiptGroupExists", {
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
   Summary: Invoke method GetListDepositSlips
   Description: Returns a List Dataset for DepositSlips
   OperationID: GetListDepositSlips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListDepositSlips_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListDepositSlips_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListDepositSlips(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetListDepositSlips", {
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
   Summary: Invoke method GetRowsUseLockSetting
   Description: Returns the CashGrp dataset using the Auto Lock Group functionality
   OperationID: GetRowsUseLockSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsUseLockSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUseLockSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsUseLockSetting(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetRowsUseLockSetting", {
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
   Summary: Invoke method GroupUnlock
   Description: Clears the lock of a group, only if the user of the current session is the same as the one locking the group.
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupUnlock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupUnlock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupUnlock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupUnlock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GroupUnlock", {
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
   Summary: Invoke method GroupLock
   Description: Locks the groupID for the current user in session only if the group is not locked already
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GroupLock", {
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
   Summary: Invoke method GetNewCashGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCashGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetNewCashGrp", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashGrpSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CashGrpRow[],
}

export interface Erp_Tablesets_CashGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  */  
   "TranDate":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  */  
   "FiscalPeriod":number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**  Related record to a  BankAcct.  */  
   "BankAcctID":string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   "Cashbook":boolean,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  */  
   "DebNoteOnly":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If yes, indicates that the group is for Payment Instrument.  */  
   "PromissoryNote":boolean,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Flag indicating payments were processed  */  
   "EIPaymSent":boolean,
      /**  Payment Instrument Status  */  
   "PIStatus":string,
      /**  Indicates its a PI Status Change group  */  
   "PIStatusGrp":boolean,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "TotalCashReceived":number,
   "TotalApplied":number,
   "UnappliedBalance":number,
   "BankCurrencyCode":string,
   "CurrSymbol":string,
   "TotalDiscount":number,
   "TotalDeposit":number,
   "TotalMisc":number,
   "TotalARAmount":number,
   "TotalWithhold":number,
   "PostErrorLog":string,
   "PostToGL":boolean,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BankCurrencyCodeDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BankCurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BankCurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "BankCurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BankCurrencyCodeCurrSymbol":string,
      /**  Status Description  */  
   "PIStatusStatusDesc":string,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PMType":number,
      /**  Name of the payment method  */  
   "PMName":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PMSummarizePerCustomer":boolean,
   "TotalWriteOff":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CashGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   "GroupID":string,
      /**  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  */  
   "TranDate":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  */  
   "FiscalYear":number,
      /**  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  */  
   "FiscalPeriod":number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**  Related record to a  BankAcct.  */  
   "BankAcctID":string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   "Cashbook":boolean,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  */  
   "DebNoteOnly":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  If yes, indicates that the group is for Payment Instrument.  */  
   "PromissoryNote":boolean,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Flag indicating payments were processed  */  
   "EIPaymSent":boolean,
      /**  Payment Instrument Status  */  
   "PIStatus":string,
      /**  Indicates its a PI Status Change group  */  
   "PIStatusGrp":boolean,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Auto Generated  */  
   "AutoGenerated":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
   "BankCurrencyCodeCurrDesc":string,
   "BankCurrencyCodeCurrencyID":string,
   "BankCurrencyCodeCurrName":string,
   "BankCurrencyCodeCurrSymbol":string,
   "BankCurrencyCodeDocumentDesc":string,
   "CurrSymbol":string,
   "DepSlipGrouping":boolean,
   "DspBankBatchID":string,
   "EIGrouping":boolean,
   "PostErrorLog":string,
   "PostToGL":boolean,
   "TotalApplied":number,
   "TotalARAmount":number,
   "TotalBankFee":number,
   "TotalCashReceived":number,
   "TotalDeposit":number,
   "TotalDiscount":number,
   "TotalMisc":number,
   "TotalWithhold":number,
   "UIGrouping":boolean,
   "UnappliedBalance":number,
   "BankCurrencyCode":string,
   "TotalWriteOff":number,
      /**  Shows that the group contains payments which are in review  */  
   "IsDocumentLocked":boolean,
      /**  Locked means can not be posted: a payment is already in review journal or in posting process.  */  
   "LockStatus":string,
   "RvJrnUID":number,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   "HasDetails":boolean,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "PIStatusPIStage":string,
   "PIStatusStatusDesc":string,
   "PMARIDTiming":number,
   "PMName":string,
   "PMType":number,
   "PMSummarizePerCustomer":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param groupID
      @param ipCheckUserID
      @param ipNeedQuestion
   */  
export interface BeforeGetByID_input{
      /**  Selected Group ID  */  
   groupID:string,
      /**  Check group is in use  */  
   ipCheckUserID:boolean,
      /**  If false, only warning about the group is in use  */  
   ipNeedQuestion:boolean,
}

export interface BeforeGetByID_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
parameters : {
      /**  output parameters  */  
   vQuestion:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param postGroupID
   */  
export interface DeleteZeroAmtTaxRec_input{
      /**  The Group ID of the Group to post  */  
   postGroupID:string,
}

export interface DeleteZeroAmtTaxRec_output{
}

export interface Erp_Tablesets_CashGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  */  
   TranDate:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  */  
   FiscalPeriod:number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**  Related record to a  BankAcct.  */  
   BankAcctID:string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   Cashbook:boolean,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  */  
   DebNoteOnly:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If yes, indicates that the group is for Payment Instrument.  */  
   PromissoryNote:boolean,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Flag indicating payments were processed  */  
   EIPaymSent:boolean,
      /**  Payment Instrument Status  */  
   PIStatus:string,
      /**  Indicates its a PI Status Change group  */  
   PIStatusGrp:boolean,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   TotalCashReceived:number,
   TotalApplied:number,
   UnappliedBalance:number,
   BankCurrencyCode:string,
   CurrSymbol:string,
   TotalDiscount:number,
   TotalDeposit:number,
   TotalMisc:number,
   TotalARAmount:number,
   TotalWithhold:number,
   PostErrorLog:string,
   PostToGL:boolean,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BankCurrencyCodeDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BankCurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BankCurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   BankCurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BankCurrencyCodeCurrSymbol:string,
      /**  Status Description  */  
   PIStatusStatusDesc:string,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PMType:number,
      /**  Name of the payment method  */  
   PMName:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PMSummarizePerCustomer:boolean,
   TotalWriteOff:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashGrpListTableset{
   CashGrpList:Erp_Tablesets_CashGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  Transaction Date.  The user enters the single date that will be used for posting of all the transaction within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which should be displayed for reference.  */  
   TranDate:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding TranDate.  User can override this. This value is then duplicated into the CashHead and CashDtl as part of the Post process. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal period for all  the transactions in this batch. Defaulted based on the Fiscal master which contains the TranDate period. This is then duplicated into the CashHead and CashDtl during posting process.  */  
   FiscalPeriod:number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**  Related record to a  BankAcct.  */  
   BankAcctID:string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   Cashbook:boolean,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available.  */  
   DebNoteOnly:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  If yes, indicates that the group is for Payment Instrument.  */  
   PromissoryNote:boolean,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Flag indicating payments were processed  */  
   EIPaymSent:boolean,
      /**  Payment Instrument Status  */  
   PIStatus:string,
      /**  Indicates its a PI Status Change group  */  
   PIStatusGrp:boolean,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Auto Generated  */  
   AutoGenerated:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
   BankCurrencyCodeCurrDesc:string,
   BankCurrencyCodeCurrencyID:string,
   BankCurrencyCodeCurrName:string,
   BankCurrencyCodeCurrSymbol:string,
   BankCurrencyCodeDocumentDesc:string,
   CurrSymbol:string,
   DepSlipGrouping:boolean,
   DspBankBatchID:string,
   EIGrouping:boolean,
   PostErrorLog:string,
   PostToGL:boolean,
   TotalApplied:number,
   TotalARAmount:number,
   TotalBankFee:number,
   TotalCashReceived:number,
   TotalDeposit:number,
   TotalDiscount:number,
   TotalMisc:number,
   TotalWithhold:number,
   UIGrouping:boolean,
   UnappliedBalance:number,
   BankCurrencyCode:string,
   TotalWriteOff:number,
      /**  Shows that the group contains payments which are in review  */  
   IsDocumentLocked:boolean,
      /**  Locked means can not be posted: a payment is already in review journal or in posting process.  */  
   LockStatus:string,
   RvJrnUID:number,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   HasDetails:boolean,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   PIStatusPIStage:string,
   PIStatusStatusDesc:string,
   PMARIDTiming:number,
   PMName:string,
   PMType:number,
   PMSummarizePerCustomer:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashGrpTableset{
   CashGrp:Erp_Tablesets_CashGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCashGrpTableset{
   CashGrp:Erp_Tablesets_CashGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByIDNoLock_input{
   groupID:string,
}

export interface GetByIDNoLock_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name  */  
   tableName:string,
      /**  The field name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param BankAcctId
      @param ds
   */  
export interface GetGrpBankInfo_input{
      /**  Proposed Bank Account  */  
   BankAcctId:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetGrpBankInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param tranDate
      @param ds
   */  
export interface GetGrpFiscal_input{
      /**  Proposed Transaction Date  */  
   tranDate:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetGrpFiscal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param whereClause
      @param bankAcctID
      @param groupIDs
      @param pageSize
      @param absolutePage
   */  
export interface GetListDepositSlips_input{
      /**  whereClause  */  
   whereClause:string,
   bankAcctID:string,
      /**  list of group IDs  */  
   groupIDs:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListDepositSlips_output{
   returnObj:Erp_Tablesets_CashGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
   returnObj:Erp_Tablesets_CashGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipStage
      @param ds
   */  
export interface GetNewCashGrpForPINoLock_input{
   ipStage:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetNewCashGrpForPINoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashGrpForPIStatusNoLock_input{
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetNewCashGrpForPIStatusNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashGrpForPIStatus_input{
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetNewCashGrpForPIStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param ipStage
      @param ds
   */  
export interface GetNewCashGrpForPI_input{
   ipStage:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetNewCashGrpForPI_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashGrpNoLock_input{
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetNewCashGrpNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCashGrp_input{
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GetNewCashGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param groupID
   */  
export interface GetPIGroupByID_input{
      /**  Selected Group ID  */  
   groupID:string,
}

export interface GetPIGroupByID_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface GetPIStatusGroupByID_input{
      /**  Selected Group ID  */  
   groupID:string,
}

export interface GetPIStatusGroupByID_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
}

   /** Required : 
      @param whereClauseCashGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsNoLock_input{
   whereClauseCashGrp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsNoLock_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCashGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsUseLockSetting_input{
   whereClauseCashGrp:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsUseLockSetting_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCashGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCashGrp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CashGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface GroupLock_input{
      /**  Group ID to lock  */  
   groupID:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GroupLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface GroupUnlock_input{
      /**  Group ID.  */  
   groupID:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface GroupUnlock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
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
      @param groupID
   */  
export interface IsPIGroup_input{
   groupID:string,
}

export interface IsPIGroup_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   promissoryNote:boolean,
   piStatusGrp:boolean,
   cashbook:boolean,
}
}

   /** Required : 
      @param groupID
   */  
export interface LeaveCashGrp_input{
      /**  Cash Group ID to clear  */  
   groupID:string,
}

export interface LeaveCashGrp_output{
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface LockPIGroupInDS_input{
      /**  Selected Group ID  */  
   groupID:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface LockPIGroupInDS_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param groupID
      @param PIStatusGrp
   */  
export interface LockPIGroup_input{
      /**  Selected Group ID  */  
   groupID:string,
      /**  True only if it is PI Status Change Group Type  */  
   PIStatusGrp:boolean,
}

export interface LockPIGroup_output{
   returnObj:boolean,
}

   /** Required : 
      @param groupID
   */  
export interface PrePostEPGroup_input{
      /**  Cash Group ID to check if it was processed  */  
   groupID:string,
}

export interface PrePostEPGroup_output{
parameters : {
      /**  output parameters  */  
   vQuestion:string,
   vTaxQuestion:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface PrePostGroup_input{
      /**  Cash Group ID to check if it was processed  */  
   groupID:string,
}

export interface PrePostGroup_output{
parameters : {
      /**  output parameters  */  
   vQuestion:string,
   vTaxQuestion:string,
   lnMessage:string,
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface ReceiptGroupExists_input{
   ipGroupID:string,
}

export interface ReceiptGroupExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcGroupID
      @param ds
   */  
export interface UnlockPIGroupInDS_input{
      /**  The Group ID selected by the user.  */  
   pcGroupID:string,
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface UnlockPIGroupInDS_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

   /** Required : 
      @param pcGroupID
      @param PIStatusGrp
   */  
export interface UnlockPIGroup_input{
      /**  The Group ID selected by the user.  */  
   pcGroupID:string,
      /**  Is PIStatusGrp  */  
   PIStatusGrp:boolean,
}

export interface UnlockPIGroup_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCashGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCashGrpTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateMaster_input{
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface UpdateMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
   mode:number,
   oldBankBatchSysRowID:string,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CashGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CashGrpTableset[],
}
}

