import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.SecuritySvc
// Description: Security business object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/$metadata", {
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
   Description: Get Securities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Securities
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SecurityRow
   */  
export function get_Securities(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Securities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SecurityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.SecurityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Securities(requestBody:Ice_Tablesets_SecurityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities", {
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
   Summary: Calls GetByID to retrieve the Security item
   Description: Calls GetByID to retrieve the Security item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Security
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.SecurityRow
   */  
export function get_Securities_Company_SecCode(Company:string, SecCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SecurityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities(" + Company + "," + SecCode + ")", {
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
         resolve(data as Ice_Tablesets_SecurityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Security for the service
   Description: Calls UpdateExt to update Security. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Security
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.SecurityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Securities_Company_SecCode(Company:string, SecCode:string, requestBody:Ice_Tablesets_SecurityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities(" + Company + "," + SecCode + ")", {
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
   Summary: Call UpdateExt to delete Security item
   Description: Call UpdateExt to delete Security item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Security
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Securities_Company_SecCode(Company:string, SecCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities(" + Company + "," + SecCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SecurityListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityListRow)
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
export function get_GetRows(whereClauseSecurity:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSecurity!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSecurity=" + whereClauseSecurity
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, secCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof secCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "secCode=" + secCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetList" + params, {
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
   Summary: Invoke method GetByIDEx
   Description: This method returns a dataset representing a Security with a blank CompanyID
   OperationID: GetByIDEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDEx(requestBody:GetByIDEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetByIDEx", {
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
         resolve(data as GetByIDEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupUserList
   Description: This method returns a double-delimited list of value-name pairs of all
Users and Groups.  This could be used to provide a "picker list" as a
starting point
when adding a new Security record related to a method.  These would look the
same as a Security record for an object, but with a SecCode field that has
been appended with "." + MethodName.
For example, a security record for the
   OperationID: GetGroupUserList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupUserList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupUserList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetGroupUserList", {
          method: 'post',
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
         resolve(data as GetGroupUserList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListEx
   Description: This method returns a list of Security, including those with blank Company ID
   OperationID: GetListEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListEx(requestBody:GetListEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetListEx", {
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
         resolve(data as GetListEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMethodList
   Description: This method returns a delimited list of the public methods for the given
object.  This could be used to provide a "picker list" as a starting point
when adding a new Security record related to a method.  These would look the
same as a Security record for an object, but with a SecCode field that has
been appended with "." + MethodName.
For example, a security record for the
   OperationID: GetMethodList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMethodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMethodList(requestBody:GetMethodList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMethodList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetMethodList", {
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
         resolve(data as GetMethodList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSubSecurity
   Description: This method creates a new sub security row
   OperationID: GetNewSubSecurity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSubSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSubSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSubSecurity(requestBody:GetNewSubSecurity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSubSecurity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetNewSubSecurity", {
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
         resolve(data as GetNewSubSecurity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopySecurityRow
   Description: Copies an existing security row to a new row.
   OperationID: CopySecurityRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopySecurityRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopySecurityRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopySecurityRow(requestBody:CopySecurityRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopySecurityRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/CopySecurityRow", {
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
         resolve(data as CopySecurityRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsEx
   Description: This method returns a list of Security, including those with blank Company ID
   OperationID: GetRowsEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsEx(requestBody:GetRowsEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetRowsEx", {
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
         resolve(data as GetRowsEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GlobalRecordFound
   OperationID: GlobalRecordFound
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GlobalRecordFound_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlobalRecordFound_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlobalRecordFound(requestBody:GlobalRecordFound_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GlobalRecordFound_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GlobalRecordFound", {
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
         resolve(data as GlobalRecordFound_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSecurity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSecurity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSecurity(requestBody:GetNewSecurity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSecurity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetNewSecurity", {
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
         resolve(data as GetNewSecurity_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/UpdateExt", {
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

   /**  
   Summary: Invoke method SecurityGetByID
   Description: Retrieve correct record based on tenancy.
   OperationID: SecurityGetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SecurityGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SecurityGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SecurityGetByID(requestBody:SecurityGetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SecurityGetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/SecurityGetByID", {
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
         resolve(data as SecurityGetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SecCodeChanging
   Description: Find seccode if company was not supplied.
   OperationID: SecCodeChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SecCodeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SecCodeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SecCodeChanging(requestBody:SecCodeChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SecCodeChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/SecCodeChanging", {
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
         resolve(data as SecCodeChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: Set field values prior to calling update method. Moved client code to the server.
   OperationID: PreUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:PreUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/PreUpdate", {
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
         resolve(data as PreUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetSelectedAccess
   Description: Update select rows with new access type.
   OperationID: SetSelectedAccess
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetSelectedAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSelectedAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetSelectedAccess(requestBody:SetSelectedAccess_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetSelectedAccess_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/SetSelectedAccess", {
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
         resolve(data as SetSelectedAccess_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddUserRows
   Description: Add user and groups to Access table
   OperationID: AddUserRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserRows(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddUserRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/AddUserRows", {
          method: 'post',
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
         resolve(data as AddUserRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddSecurityInfo
   Description: Populate access tables with access code.
   OperationID: AddSecurityInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddSecurityInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSecurityInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddSecurityInfo(requestBody:AddSecurityInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddSecurityInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/AddSecurityInfo", {
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
         resolve(data as AddSecurityInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyExistingSecCode
   Description: Copies an existing security row to a new row.
   OperationID: CopyExistingSecCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyExistingSecCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyExistingSecCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyExistingSecCode(requestBody:CopyExistingSecCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyExistingSecCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/CopyExistingSecCode", {
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
         resolve(data as CopyExistingSecCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CGCCodeList
   Description: Build cgccode list.
   OperationID: CGCCodeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CGCCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CGCCodeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CGCCodeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/CGCCodeList", {
          method: 'post',
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
         resolve(data as CGCCodeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AllCompaniesChanging
   Description: Verify if all company can be set
   OperationID: AllCompaniesChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AllCompaniesChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllCompaniesChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllCompaniesChanging(requestBody:AllCompaniesChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AllCompaniesChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/AllCompaniesChanging", {
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
         resolve(data as AllCompaniesChanging_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SecurityListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SecurityRow,
}

export interface Ice_Tablesets_SecurityListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  */  
   "SecCode":string,
      /**  Indicates that the user account must have Security Manager privileges to access the options.  */  
   "SecurityMgr":boolean,
      /**  Description  */  
   "Description":string,
      /**  Sub-Security Code Sequence.  */  
   "ParentSeqNum":number,
      /**  Should this security code be available to a disconnect user?  If so, the value should be YES.  */  
   "Disconnected":boolean,
      /**  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  */  
   "ShipRecv":boolean,
      /**  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  */  
   "ShopSupervisor":boolean,
      /**  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  */  
   "ProductionWorker":boolean,
      /**   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  */  
   "CustWebAvailable":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CompanyVisibility  */  
   "CompanyVisibility":number,
   "AllowAll":boolean,
   "AllowAccess":string,
   "AllCompanies":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SecurityRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  */  
   "SecCode":string,
      /**  List of security groups the user belongs to.  */  
   "EntryList":string,
      /**  List of security groups the user belongs to.  */  
   "NoEntryList":string,
      /**  Indicates that the user account must have Security Manager privileges to access the options.  */  
   "SecurityMgr":boolean,
      /**  Description  */  
   "Description":string,
      /**  Parent Security ID for a Sub-Security Code.  Only Set for Security Codes that are subcomponents of a regular security code.  For example: Costing information in Job Tracker.  */  
   "ParentSecCode":string,
      /**  Sub-Security Code Sequence.  */  
   "ParentSeqNum":number,
      /**  Should this security code be available to a disconnect user?  If so, the value should be YES.  */  
   "Disconnected":boolean,
      /**  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  */  
   "ShipRecv":boolean,
      /**  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  */  
   "ShopSupervisor":boolean,
      /**  Indicates if the menu item associated to this security code requires the employee to be a material handler.  */  
   "MaterialHandler":boolean,
      /**  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  */  
   "ProductionWorker":boolean,
      /**  Indicates if the menu item associated with this security code requires the employee goes out on service calls.  */  
   "ServTech":boolean,
      /**   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  */  
   "CustWebAvailable":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  GlobalSecurityMgr  */  
   "GlobalSecurityMgr":boolean,
      /**  CompanyVisibility  */  
   "CompanyVisibility":number,
   "AllowAll":boolean,
   "AvailableUsers":string,
   "DisallowAccess":string,
   "DisallowAll":boolean,
   "MenuOptions":string,
   "AllowAccess":string,
   "AllCompanies":boolean,
   "Access":string,
   "CanModify":boolean,
   "Preupdated":boolean,
   "BitFlag":number,
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
      @param ds
      @param dsSecurityList
   */  
export interface AddSecurityInfo_input{
   ds:Ice_Tablesets_SecurityTableset[],
   dsSecurityList:Ice_Tablesets_SecurityAccessTableset[],
}

export interface AddSecurityInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SecurityTableset,
   dsSecurityList:Ice_Tablesets_SecurityAccessTableset,
}
}

export interface AddUserRows_output{
   returnObj:Ice_Tablesets_SecurityAccessTableset[],
}

   /** Required : 
      @param secCode
      @param currentCompany
   */  
export interface AllCompaniesChanging_input{
   secCode:string,
   currentCompany:string,
}

export interface AllCompaniesChanging_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   company:string,
   companyVisibility:number,
}
}

export interface CGCCodeList_output{
   returnObj:string,
}

   /** Required : 
      @param sourceCompany
      @param sourceSecurityCode
      @param targetCompany
      @param targetSecurityCode
   */  
export interface CopyExistingSecCode_input{
      /**  The source company ID  */  
   sourceCompany:string,
      /**  The source security code.  */  
   sourceSecurityCode:string,
      /**  Target company.  */  
   targetCompany:string,
      /**  Target security code.  */  
   targetSecurityCode:string,
}

export interface CopyExistingSecCode_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
}

   /** Required : 
      @param ds
      @param sourceCompany
      @param sourceSecurityCode
      @param targetCompany
      @param targetSecurityCode
   */  
export interface CopySecurityRow_input{
   ds:Ice_Tablesets_SecurityTableset[],
      /**  The source company ID  */  
   sourceCompany:string,
      /**  The source security code.  */  
   sourceSecurityCode:string,
      /**  Target company.  */  
   targetCompany:string,
      /**  Target security code.  */  
   targetSecurityCode:string,
}

export interface CopySecurityRow_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SecurityTableset,
}
}

   /** Required : 
      @param company
      @param secCode
   */  
export interface DeleteByID_input{
   company:string,
   secCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param secCode
   */  
export interface GetByIDEx_input{
      /**  The security code  */  
   secCode:string,
}

export interface GetByIDEx_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
}

   /** Required : 
      @param company
      @param secCode
   */  
export interface GetByID_input{
   company:string,
   secCode:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
}

export interface GetGroupUserList_output{
parameters : {
      /**  output parameters  */  
   groupUserList:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListEx_input{
      /**  The criteria  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetListEx_output{
   returnObj:Ice_Tablesets_SecurityListTableset[],
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
   returnObj:Ice_Tablesets_SecurityListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param secCode
   */  
export interface GetMethodList_input{
      /**  The security code for which you want the list of methods.  */  
   secCode:string,
}

export interface GetMethodList_output{
parameters : {
      /**  output parameters  */  
   methodList:string,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewSecurity_input{
   ds:Ice_Tablesets_SecurityTableset[],
   company:string,
}

export interface GetNewSecurity_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SecurityTableset,
}
}

   /** Required : 
      @param ds
      @param parentSecCode
      @param secCode
   */  
export interface GetNewSubSecurity_input{
   ds:Ice_Tablesets_SecurityTableset[],
      /**  The parent security code  */  
   parentSecCode:string,
      /**  The security code  */  
   secCode:string,
}

export interface GetNewSubSecurity_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SecurityTableset,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsEx_input{
      /**  The criteria  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetRowsEx_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSecurity
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSecurity:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param SecCode
   */  
export interface GlobalRecordFound_input{
   SecCode:string,
}

export interface GlobalRecordFound_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   Company:string,
   CompanyVisibility:number,
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

export interface Ice_Tablesets_GroupAccessRow{
   Access:string,
   SecGroupCode:string,
   SecGroupDesc:string,
   Select:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SecurityAccessTableset{
   GroupAccess:Ice_Tablesets_GroupAccessRow[],
   UserAccess:Ice_Tablesets_UserAccessRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SecurityListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  */  
   SecCode:string,
      /**  Indicates that the user account must have Security Manager privileges to access the options.  */  
   SecurityMgr:boolean,
      /**  Description  */  
   Description:string,
      /**  Sub-Security Code Sequence.  */  
   ParentSeqNum:number,
      /**  Should this security code be available to a disconnect user?  If so, the value should be YES.  */  
   Disconnected:boolean,
      /**  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  */  
   ShipRecv:boolean,
      /**  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  */  
   ShopSupervisor:boolean,
      /**  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  */  
   ProductionWorker:boolean,
      /**   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  */  
   CustWebAvailable:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CompanyVisibility  */  
   CompanyVisibility:number,
   AllowAll:boolean,
   AllowAccess:string,
   AllCompanies:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SecurityListTableset{
   SecurityList:Ice_Tablesets_SecurityListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SecurityRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  */  
   SecCode:string,
      /**  List of security groups the user belongs to.  */  
   EntryList:string,
      /**  List of security groups the user belongs to.  */  
   NoEntryList:string,
      /**  Indicates that the user account must have Security Manager privileges to access the options.  */  
   SecurityMgr:boolean,
      /**  Description  */  
   Description:string,
      /**  Parent Security ID for a Sub-Security Code.  Only Set for Security Codes that are subcomponents of a regular security code.  For example: Costing information in Job Tracker.  */  
   ParentSecCode:string,
      /**  Sub-Security Code Sequence.  */  
   ParentSeqNum:number,
      /**  Should this security code be available to a disconnect user?  If so, the value should be YES.  */  
   Disconnected:boolean,
      /**  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  */  
   ShipRecv:boolean,
      /**  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  */  
   ShopSupervisor:boolean,
      /**  Indicates if the menu item associated to this security code requires the employee to be a material handler.  */  
   MaterialHandler:boolean,
      /**  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  */  
   ProductionWorker:boolean,
      /**  Indicates if the menu item associated with this security code requires the employee goes out on service calls.  */  
   ServTech:boolean,
      /**   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  */  
   CustWebAvailable:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  GlobalSecurityMgr  */  
   GlobalSecurityMgr:boolean,
      /**  CompanyVisibility  */  
   CompanyVisibility:number,
   AllowAll:boolean,
   AvailableUsers:string,
   DisallowAccess:string,
   DisallowAll:boolean,
   MenuOptions:string,
   AllowAccess:string,
   AllCompanies:boolean,
   Access:string,
   CanModify:boolean,
   Preupdated:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SecurityTableset{
   Security:Ice_Tablesets_SecurityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtSecurityTableset{
   Security:Ice_Tablesets_SecurityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UserAccessRow{
   Access:string,
   Name:string,
   SecurityMgr:boolean,
   UserID:string,
   Select:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
      @param dsSecurityList
   */  
export interface PreUpdate_input{
   ds:Ice_Tablesets_SecurityTableset[],
   dsSecurityList:Ice_Tablesets_SecurityAccessTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SecurityTableset,
   dsSecurityList:Ice_Tablesets_SecurityAccessTableset,
}
}

   /** Required : 
      @param secCode
   */  
export interface SecCodeChanging_input{
   secCode:string,
}

export interface SecCodeChanging_output{
parameters : {
      /**  output parameters  */  
   company:string,
}
}

   /** Required : 
      @param company
      @param secCode
   */  
export interface SecurityGetByID_input{
   company:string,
   secCode:string,
}

export interface SecurityGetByID_output{
   returnObj:Ice_Tablesets_SecurityTableset[],
}

   /** Required : 
      @param dsSecurityList
      @param table
      @param newAccess
   */  
export interface SetSelectedAccess_input{
   dsSecurityList:Ice_Tablesets_SecurityAccessTableset[],
   table:string,
   newAccess:string,
}

export interface SetSelectedAccess_output{
parameters : {
      /**  output parameters  */  
   dsSecurityList:Ice_Tablesets_SecurityAccessTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtSecurityTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtSecurityTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_SecurityTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SecurityTableset,
}
}

