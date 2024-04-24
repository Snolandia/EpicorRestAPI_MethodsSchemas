import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.VoidPRCheckSvc
// Description: VoidPRCheckSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/$metadata", {
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
   Description: Get VoidPRChecks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VoidPRChecks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckRow
   */  
export function get_VoidPRChecks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VoidPRChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidPRChecks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks", {
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
   Summary: Calls GetByID to retrieve the VoidPRCheck item
   Description: Calls GetByID to retrieve the VoidPRCheck item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VoidPRCheck
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   */  
export function get_VoidPRChecks_Company_HeadNum(Company:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRCheckRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks(" + Company + "," + HeadNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRCheckRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update VoidPRCheck for the service
   Description: Calls UpdateExt to update VoidPRCheck. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VoidPRCheck
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_VoidPRChecks_Company_HeadNum(Company:string, HeadNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete VoidPRCheck item
   Description: Call UpdateExt to delete VoidPRCheck item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VoidPRCheck
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_VoidPRChecks_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks(" + Company + "," + HeadNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow)
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
export function get_GetRows(whereClausePRCheck:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePRCheck!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRCheck=" + whereClausePRCheck
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/GetList" + params, {
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
   Summary: Invoke method getClientFileName
   OperationID: getClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getClientFileName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/getClientFileName", {
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
   Summary: Invoke method ValidateEmpID
   Description: Call this method from Kinetic before calling OnChangeEmployeeID as that method acts more like the GetByID and
we need to validate if the EmpID is valid first.
   OperationID: ValidateEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEmpID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/ValidateEmpID", {
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
   Summary: Invoke method OnChangeEmployeeID
   Description: Call this method after user enters the Employee ID.
   OperationID: OnChangeEmployeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEmployeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEmployeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEmployeeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/OnChangeEmployeeID", {
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
   Summary: Invoke method PreVoidCheck
   Description: check if interface
   OperationID: PreVoidCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreVoidCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreVoidCheck(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/PreVoidCheck", {
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
   Summary: Invoke method VoidPayrollCheck
   OperationID: VoidPayrollCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidPayrollCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidPayrollCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidPayrollCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPayrollCheck", {
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
   Summary: Invoke method GetNewPRCheck
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRCheck(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/GetNewPRCheck", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRCheckListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRCheckRow[],
}

export interface Erp_Tablesets_PRCheckListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   "Posted":boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PSDate":string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PEDate":string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   "FiscalYear":number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   "TotalBasePay":number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalPremiumPay":number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalShiftPay":number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   "TotalTaxes":number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   "TotalDeductions":number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   "TotalBaseHours":number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   "TotalPremiumHours":number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   "CheckAmt":number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   "StartupCheck":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   "WorkCompCode":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  A short note which is printed on the check.  */  
   "Note":string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   "PayFrequency":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  VoidedDate  */  
   "VoidedDate":string,
   "SocSecNum":string,
   "EmpID":string,
   "AddressList":string,
   "EmpFirstName":string,
   "EmpMiddleInit":string,
   "EmpLastName":string,
   "PhotoFile":string,
   "ImageFile":string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   "PRInterfacedContinue":boolean,
   "EmpLinkFirstName":string,
   "EmpLinkLastName":string,
   "EmpLinkName":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the payroll class.  */  
   "ClassIDDescription":string,
      /**  Description of the workers' compensation code.  */  
   "WorkCompCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRCheckRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   "Posted":boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PSDate":string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   "PEDate":string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   "FiscalYear":number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   "TotalBasePay":number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalPremiumPay":number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   "TotalShiftPay":number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   "TotalTaxes":number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   "TotalDeductions":number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   "TotalBaseHours":number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   "TotalPremiumHours":number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   "CheckAmt":number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   "StartupCheck":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   "WorkCompCode":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  A short note which is printed on the check.  */  
   "Note":string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   "PayFrequency":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ActiveToPrint  */  
   "ActiveToPrint":boolean,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  VoidedDate  */  
   "VoidedDate":string,
   "EmpFirstName":string,
   "EmpID":string,
   "EmpLastName":string,
   "EmpLinkFirstName":string,
   "EmpLinkLastName":string,
   "EmpLinkName":string,
   "EmpMiddleInit":string,
   "ImageFile":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PhotoFile":string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   "PRInterfacedContinue":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SocSecNum":string,
   "AddressList":string,
      /**  The columns is the formatted by new line separator version of the AddressList column  */  
   "AddressListFormatted":string,
      /**  Display CheckAmt for kinetic  */  
   "DspCheckAmt":number,
      /**  Display CheckDate for kinetic  */  
   "DspCheckDate":string,
      /**  Display CheckNum for kinetic  */  
   "DspCheckNum":number,
   "BitFlag":number,
   "BankAcctIDBankName":string,
   "BankAcctIDDescription":string,
   "ClassIDDescription":string,
   "WorkCompCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param headNum
   */  
export interface DeleteByID_input{
   headNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PRCheckListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   Posted:boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PSDate:string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PEDate:string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   FiscalYear:number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   TotalBasePay:number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalPremiumPay:number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalShiftPay:number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   TotalTaxes:number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   TotalDeductions:number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   TotalBaseHours:number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   TotalPremiumHours:number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   CheckAmt:number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   StartupCheck:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   WorkCompCode:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  A short note which is printed on the check.  */  
   Note:string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   PayFrequency:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  VoidedDate  */  
   VoidedDate:string,
   SocSecNum:string,
   EmpID:string,
   AddressList:string,
   EmpFirstName:string,
   EmpMiddleInit:string,
   EmpLastName:string,
   PhotoFile:string,
   ImageFile:string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   PRInterfacedContinue:boolean,
   EmpLinkFirstName:string,
   EmpLinkLastName:string,
   EmpLinkName:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the payroll class.  */  
   ClassIDDescription:string,
      /**  Description of the workers' compensation code.  */  
   WorkCompCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRCheckListTableset{
   PRCheckList:Erp_Tablesets_PRCheckListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRCheckRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  */  
   Posted:boolean,
      /**  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PSDate:string,
      /**  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  */  
   PEDate:string,
      /**  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  */  
   FiscalYear:number,
      /**  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  */  
   TotalBasePay:number,
      /**  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalPremiumPay:number,
      /**  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  */  
   TotalShiftPay:number,
      /**  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  */  
   TotalTaxes:number,
      /**  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  */  
   TotalDeductions:number,
      /**  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  */  
   TotalBaseHours:number,
      /**  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  */  
   TotalPremiumHours:number,
      /**  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  */  
   CheckAmt:number,
      /**  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  */  
   StartupCheck:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  */  
   WorkCompCode:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  A short note which is printed on the check.  */  
   Note:string,
      /**  Copied from PREmpMas at the time the PRCheck record is created.  */  
   PayFrequency:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ActiveToPrint  */  
   ActiveToPrint:boolean,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  VoidedDate  */  
   VoidedDate:string,
   EmpFirstName:string,
   EmpID:string,
   EmpLastName:string,
   EmpLinkFirstName:string,
   EmpLinkLastName:string,
   EmpLinkName:string,
   EmpMiddleInit:string,
   ImageFile:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PhotoFile:string,
      /**  Used in VoidPRCheck - User response to a question when GL is not interfaced.  */  
   PRInterfacedContinue:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SocSecNum:string,
   AddressList:string,
      /**  The columns is the formatted by new line separator version of the AddressList column  */  
   AddressListFormatted:string,
      /**  Display CheckAmt for kinetic  */  
   DspCheckAmt:number,
      /**  Display CheckDate for kinetic  */  
   DspCheckDate:string,
      /**  Display CheckNum for kinetic  */  
   DspCheckNum:number,
   BitFlag:number,
   BankAcctIDBankName:string,
   BankAcctIDDescription:string,
   ClassIDDescription:string,
   WorkCompCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtVoidPRCheckTableset{
   PRCheck:Erp_Tablesets_PRCheckRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VoidPRCheckPREmpMasRow{
   Company:string,
      /**  Name and address combined in one field.  */  
   DisplayAddress:string,
   SupervisorName:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
   EmpID:string,
   PRInterfaced:boolean,
      /**  Path of photo id  */  
   ImageFile:string,
      /**  ImageID  */  
   ImageID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_VoidPRCheckPREmpMasTableset{
   VoidPRCheckPREmpMas:Erp_Tablesets_VoidPRCheckPREmpMasRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_VoidPRCheckTableset{
   PRCheck:Erp_Tablesets_PRCheckRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param headNum
   */  
export interface GetByID_input{
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_VoidPRCheckTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_VoidPRCheckTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_VoidPRCheckTableset[],
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
   returnObj:Erp_Tablesets_PRCheckListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPRCheck_input{
   ds:Erp_Tablesets_VoidPRCheckTableset[],
}

export interface GetNewPRCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VoidPRCheckTableset[],
}
}

   /** Required : 
      @param whereClausePRCheck
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePRCheck:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_VoidPRCheckTableset[],
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
      @param pcEmployeeID
   */  
export interface OnChangeEmployeeID_input{
   ds:Erp_Tablesets_VoidPRCheckPREmpMasTableset[],
      /**  Employee ID  */  
   pcEmployeeID:string,
}

export interface OnChangeEmployeeID_output{
   returnObj:Erp_Tablesets_VoidPRCheckTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VoidPRCheckPREmpMasTableset[],
}
}

export interface PreVoidCheck_output{
parameters : {
      /**  output parameters  */  
   InterfacedText:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtVoidPRCheckTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtVoidPRCheckTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_VoidPRCheckTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_VoidPRCheckTableset[],
}
}

   /** Required : 
      @param pcEmployeeID
   */  
export interface ValidateEmpID_input{
      /**  Employee ID  */  
   pcEmployeeID:string,
}

export interface ValidateEmpID_output{
}

   /** Required : 
      @param ipCheckNum
      @param ipVoidDate
      @param ipEmployeeId
      @param ipPRInterfacedContinue
   */  
export interface VoidPayrollCheck_input{
   ipCheckNum:number,
   ipVoidDate:string,
   ipEmployeeId:string,
   ipPRInterfacedContinue:boolean,
}

export interface VoidPayrollCheck_output{
parameters : {
      /**  output parameters  */  
   oErrMessage:string,
}
}

   /** Required : 
      @param IP_ServerFileName
   */  
export interface getClientFileName_input{
   IP_ServerFileName:string,
}

export interface getClientFileName_output{
   returnObj:string,
}

