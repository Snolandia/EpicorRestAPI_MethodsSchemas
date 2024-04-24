import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PRChkGrpSvc
// Description: Payroll Check Group.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/$metadata", {
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
   Description: Get PRChkGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkGrps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkGrpRow
   */  
export function get_PRChkGrps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRChkGrps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps", {
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
   Summary: Calls GetByID to retrieve the PRChkGrp item
   Description: Calls GetByID to retrieve the PRChkGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
   */  
export function get_PRChkGrps_Company_GroupID(Company:string, GroupID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRChkGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRChkGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRChkGrp for the service
   Description: Calls UpdateExt to update PRChkGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRChkGrps_Company_GroupID(Company:string, GroupID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete PRChkGrp item
   Description: Call UpdateExt to delete PRChkGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRChkGrps_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps(" + Company + "," + GroupID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpListRow)
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
export function get_GetRows(whereClausePRChkGrp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePRChkGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRChkGrp=" + whereClausePRChkGrp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetList" + params, {
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
   Summary: Invoke method ChangeBankAcctID
   Description: Method to call when changing the bank account.
   OperationID: ChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBankAcctID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/ChangeBankAcctID", {
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
   Summary: Invoke method ChangeCheckDate
   Description: Method to call to update the fiscal period fields for the new check date.
   OperationID: ChangeCheckDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCheckDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCheckDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCheckDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/ChangeCheckDate", {
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
   Summary: Invoke method PostGroup
   Description: Method to call when posting checks for a specific group.  Posting of a group causes
the PRChkGrp record to be deleted from the database if all checks in the group posted correctly.
   OperationID: PostGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PostGroup", {
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
   Description: Method to call before posting checks for a specific group.  It will check
to see if the register has printed or not.  The text for this question is returned
in RegisterText.  It will also check to see if payroll is interfaced with
G/L.  The text for this question is returned in InterfacedText.
For both questions, if the answer is yes, posting can continue,
otherwise posting is canceled.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PrePostGroup", {
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
   Summary: Invoke method PreUpdateCheck
   Description: Method to call to perform pre-validations on the update of a check group record.
The pre-validations involve asking the user various questions about
the changes being made and if the changes will be ok.
The validations are:
1) The check date is less than today or more than 14 days out
2) The check date changed, which will require taxes and deductions to be
recalculated.
3) The Deduction period value is zero.
If the user answers yes to all questions, the save can continue.  If
the user answers no to any question, the update is canceled.
This method should be called prior to the Update method.
   OperationID: PreUpdateCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdateCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdateCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdateCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PreUpdateCheck", {
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
   Summary: Invoke method UnlockGroup
   Description: Method to call to unlock a group record.  This method should be called whenever
the group no longer needs to be locked.  The group no longer needs to be locked
when the payroll entry object is closed, or when a different group is selected.
   OperationID: UnlockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/UnlockGroup", {
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
   Description: The wrapper method for GetRows. Retrieve groups ignoring Active User lock
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetRowsNoLock", {
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
   Summary: Invoke method UpdateNoLock
   Description: The wrapper method for GetRows. Update the group ignoring Active User lock
   OperationID: UpdateNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/UpdateNoLock", {
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
   Summary: Invoke method CheckGroupAccess
   Description: The method validates that the user has access rights to the the group and payroll classes which are used in the group
   OperationID: CheckGroupAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGroupAccess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/CheckGroupAccess", {
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
   Summary: Invoke method GetNewPRChkGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRChkGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetNewPRChkGrp", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRChkGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRChkGrpRow[],
}

export interface Erp_Tablesets_PRChkGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  */  
   "GroupID":string,
      /**  The user id that created this batch.  */  
   "CreatedBy":string,
      /**  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  */  
   "BankAcctID":string,
      /**  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  */  
   "CheckDate":string,
      /**  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  */  
   "PEDate":string,
      /**  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  */  
   "PayWeekly":boolean,
      /**  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  */  
   "PayBiWeekly":boolean,
      /**  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  */  
   "PaySemiMonthly":boolean,
      /**  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  */  
   "PayMonthly":boolean,
      /**  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  */  
   "PayClasses":string,
      /**   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  */  
   "DeductionPeriod":number,
      /**   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  */  
   "TaxesNeeded":boolean,
      /**  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  */  
   "ChecksPrinted":boolean,
      /**  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  */  
   "RegisterPrinted":boolean,
      /**  Contains posting error messages. Possible messages are;  */  
   "PostErrorLog":string,
      /**  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  */  
   "UpdateAccrual":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "IncludedPayFrequencies":string,
   "ChecksInGroup":number,
   "BaseHours":number,
   "PremiumHours":number,
   "TotalGross":number,
   "TotalTaxes":number,
   "TotalDeductions":number,
   "NetAmount":number,
   "PayClassesDescriptions":string,
   "NonPaidPayClasses":string,
   "NonPaidPayClassesDesc":string,
   "FiscalYear":number,
   "FiscalPeriod":number,
   "PRChecksExist":boolean,
   "DispPostErrors":string,
   "EnablePrintChecks":boolean,
   "FiscalCalendarID":string,
   "FiscalYearSuffix":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRChkGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  */  
   "GroupID":string,
      /**  The user id that created this batch.  */  
   "CreatedBy":string,
      /**  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  */  
   "BankAcctID":string,
      /**  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  */  
   "CheckDate":string,
      /**  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  */  
   "PEDate":string,
      /**  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  */  
   "PayWeekly":boolean,
      /**  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  */  
   "PayBiWeekly":boolean,
      /**  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  */  
   "PaySemiMonthly":boolean,
      /**  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  */  
   "PayMonthly":boolean,
      /**  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  */  
   "PayClasses":string,
      /**   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  */  
   "DeductionPeriod":number,
      /**   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  */  
   "TaxesNeeded":boolean,
      /**  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  */  
   "ChecksPrinted":boolean,
      /**  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  */  
   "RegisterPrinted":boolean,
      /**  Contains posting error messages. Possible messages are;  */  
   "PostErrorLog":string,
      /**  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  */  
   "UpdateAccrual":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  FilePath  */  
   "FilePath":string,
      /**  DownloadStatus  */  
   "DownloadStatus":number,
      /**  IncludeOutdatedLabor  */  
   "IncludeOutdatedLabor":boolean,
   "DispPostErrors":string,
   "EnablePrintChecks":boolean,
   "FiscalCalendarID":string,
   "FiscalPeriod":number,
   "FiscalYear":number,
   "FiscalYearSuffix":string,
   "IncludedPayFrequencies":string,
   "NetAmount":number,
   "NonPaidPayClasses":string,
   "NonPaidPayClassesDesc":string,
   "PayClassesDescriptions":string,
   "PRChecksExist":boolean,
   "PremiumHours":number,
   "TotalDeductions":number,
   "TotalGross":number,
   "TotalTaxes":number,
   "BaseHours":number,
   "ChecksInGroup":number,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ProposedBankAcctID
      @param ds
   */  
export interface ChangeBankAcctID_input{
      /**  The proposed bank account id  */  
   ProposedBankAcctID:string,
   ds:Erp_Tablesets_PRChkGrpTableset[],
}

export interface ChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRChkGrpTableset[],
}
}

   /** Required : 
      @param ProposedCheckDate
      @param ds
   */  
export interface ChangeCheckDate_input{
      /**  The proposed check date  */  
   ProposedCheckDate:string,
   ds:Erp_Tablesets_PRChkGrpTableset[],
}

export interface ChangeCheckDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRChkGrpTableset[],
}
}

   /** Required : 
      @param groupID
   */  
export interface CheckGroupAccess_input{
      /**  The code group  */  
   groupID:string,
}

export interface CheckGroupAccess_output{
      /**  true - the user has access to the group, false - the user doesn't have access to the group  */  
   returnObj:boolean,
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PRChkGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  */  
   GroupID:string,
      /**  The user id that created this batch.  */  
   CreatedBy:string,
      /**  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  */  
   BankAcctID:string,
      /**  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  */  
   CheckDate:string,
      /**  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  */  
   PEDate:string,
      /**  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  */  
   PayWeekly:boolean,
      /**  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  */  
   PayBiWeekly:boolean,
      /**  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  */  
   PaySemiMonthly:boolean,
      /**  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  */  
   PayMonthly:boolean,
      /**  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  */  
   PayClasses:string,
      /**   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  */  
   DeductionPeriod:number,
      /**   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  */  
   TaxesNeeded:boolean,
      /**  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  */  
   ChecksPrinted:boolean,
      /**  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  */  
   RegisterPrinted:boolean,
      /**  Contains posting error messages. Possible messages are;  */  
   PostErrorLog:string,
      /**  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  */  
   UpdateAccrual:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   IncludedPayFrequencies:string,
   ChecksInGroup:number,
   BaseHours:number,
   PremiumHours:number,
   TotalGross:number,
   TotalTaxes:number,
   TotalDeductions:number,
   NetAmount:number,
   PayClassesDescriptions:string,
   NonPaidPayClasses:string,
   NonPaidPayClassesDesc:string,
   FiscalYear:number,
   FiscalPeriod:number,
   PRChecksExist:boolean,
   DispPostErrors:string,
   EnablePrintChecks:boolean,
   FiscalCalendarID:string,
   FiscalYearSuffix:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRChkGrpListTableset{
   PRChkGrpList:Erp_Tablesets_PRChkGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRChkGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  */  
   GroupID:string,
      /**  The user id that created this batch.  */  
   CreatedBy:string,
      /**  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  */  
   BankAcctID:string,
      /**  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  */  
   CheckDate:string,
      /**  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  */  
   PEDate:string,
      /**  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  */  
   PayWeekly:boolean,
      /**  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  */  
   PayBiWeekly:boolean,
      /**  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  */  
   PaySemiMonthly:boolean,
      /**  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  */  
   PayMonthly:boolean,
      /**  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  */  
   PayClasses:string,
      /**   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  */  
   DeductionPeriod:number,
      /**   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  */  
   TaxesNeeded:boolean,
      /**  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  */  
   ChecksPrinted:boolean,
      /**  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  */  
   RegisterPrinted:boolean,
      /**  Contains posting error messages. Possible messages are;  */  
   PostErrorLog:string,
      /**  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  */  
   UpdateAccrual:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  FilePath  */  
   FilePath:string,
      /**  DownloadStatus  */  
   DownloadStatus:number,
      /**  IncludeOutdatedLabor  */  
   IncludeOutdatedLabor:boolean,
   DispPostErrors:string,
   EnablePrintChecks:boolean,
   FiscalCalendarID:string,
   FiscalPeriod:number,
   FiscalYear:number,
   FiscalYearSuffix:string,
   IncludedPayFrequencies:string,
   NetAmount:number,
   NonPaidPayClasses:string,
   NonPaidPayClassesDesc:string,
   PayClassesDescriptions:string,
   PRChecksExist:boolean,
   PremiumHours:number,
   TotalDeductions:number,
   TotalGross:number,
   TotalTaxes:number,
   BaseHours:number,
   ChecksInGroup:number,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRChkGrpTableset{
   PRChkGrp:Erp_Tablesets_PRChkGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPRChkGrpTableset{
   PRChkGrp:Erp_Tablesets_PRChkGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PRChkGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PRChkGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PRChkGrpTableset[],
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
   returnObj:Erp_Tablesets_PRChkGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPRChkGrp_input{
   ds:Erp_Tablesets_PRChkGrpTableset[],
}

export interface GetNewPRChkGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRChkGrpTableset[],
}
}

   /** Required : 
      @param whereClausePRChkGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsNoLock_input{
   whereClausePRChkGrp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsNoLock_output{
   returnObj:Erp_Tablesets_PRChkGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePRChkGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePRChkGrp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PRChkGrpTableset[],
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
      @param PostGroupID
   */  
export interface PostGroup_input{
      /**  The group id of the group of checks to be posted  */  
   PostGroupID:string,
}

export interface PostGroup_output{
parameters : {
      /**  output parameters  */  
   PostErrors:string,
}
}

   /** Required : 
      @param PostGroupID
   */  
export interface PrePostGroup_input{
      /**  The Group ID of the Group to post  */  
   PostGroupID:string,
}

export interface PrePostGroup_output{
parameters : {
      /**  output parameters  */  
   RegisterText:string,
   InterfacedText:string,
}
}

   /** Required : 
      @param GroupID
      @param CheckDate
      @param DeductionPeriod
      @param ds
   */  
export interface PreUpdateCheck_input{
      /**  The group id  */  
   GroupID:string,
      /**  The check date  */  
   CheckDate:string,
      /**  The deduction period to validate  */  
   DeductionPeriod:number,
   ds:Erp_Tablesets_PRChkGrpTableset[],
}

export interface PreUpdateCheck_output{
parameters : {
      /**  output parameters  */  
   DateRangeText:string,
   RecalcTaxAndDedText:string,
   DeductionPeriodText:string,
   ds:Erp_Tablesets_PRChkGrpTableset[],
}
}

   /** Required : 
      @param InGroupID
   */  
export interface UnlockGroup_input{
      /**  The group id of the group record to unlock  */  
   InGroupID:string,
}

export interface UnlockGroup_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPRChkGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPRChkGrpTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateNoLock_input{
   ds:Erp_Tablesets_PRChkGrpTableset[],
}

export interface UpdateNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRChkGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PRChkGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRChkGrpTableset[],
}
}

