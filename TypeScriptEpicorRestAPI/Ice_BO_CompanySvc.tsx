import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.CompanySvc
// Description: Company service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/$metadata", {
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
   Description: Get Companies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Companies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CompanyRow
   */  
export function get_Companies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Companies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.CompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.CompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Companies(requestBody:Ice_Tablesets_CompanyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies", {
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
   Summary: Calls GetByID to retrieve the Company item
   Description: Calls GetByID to retrieve the Company item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Company
      @param Company1 Desc: Company1   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.CompanyRow
   */  
export function get_Companies_Company1(Company1:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_CompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies(" + Company1 + ")", {
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
         resolve(data as Ice_Tablesets_CompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Company for the service
   Description: Calls UpdateExt to update Company. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Company
      @param Company1 Desc: Company1   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.CompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Companies_Company1(Company1:string, requestBody:Ice_Tablesets_CompanyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies(" + Company1 + ")", {
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
   Summary: Call UpdateExt to delete Company item
   Description: Call UpdateExt to delete Company item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Company
      @param Company1 Desc: Company1   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Companies_Company1(Company1:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies(" + Company1 + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CompanyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyListRow)
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
export function get_GetRows(whereClauseCompany:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCompany=" + whereClauseCompany
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetRows" + params, {
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
export function get_GetByID(company:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetByID" + params, {
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
   Summary: Invoke method VerifySSRSConnection
   Description: Verify SQL connections for SSRS DB
   OperationID: VerifySSRSConnection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifySSRSConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifySSRSConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifySSRSConnection(requestBody:VerifySSRSConnection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifySSRSConnection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/VerifySSRSConnection", {
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
         resolve(data as VerifySSRSConnection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDBNameList
   Description: Gets a list of SSRS DB
   OperationID: GetDBNameList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDBNameList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDBNameList(requestBody:GetDBNameList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDBNameList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetDBNameList", {
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
         resolve(data as GetDBNameList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSystemTimeZoneList
   Description: This method returns a list of Microsoft Time Zone Index Values and their corresponding display name
   OperationID: GetSystemTimeZoneList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemTimeZoneList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSystemTimeZoneList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSystemTimeZoneList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetSystemTimeZoneList", {
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
         resolve(data as GetSystemTimeZoneList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackageProcessList
   Description: Gets the package process list from Service Connect.
   OperationID: GetPackageProcessList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackageProcessList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageProcessList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackageProcessList(requestBody:GetPackageProcessList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackageProcessList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetPackageProcessList", {
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
         resolve(data as GetPackageProcessList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateLogoImage
   Description: Updates the current company logo image (returned as Base-64 encoded string in LogoImageContent but not saved in database)
and deletes the file in the user import folder.
   OperationID: UpdateLogoImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateLogoImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLogoImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLogoImage(requestBody:UpdateLogoImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateLogoImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/UpdateLogoImage", {
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
         resolve(data as UpdateLogoImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCompany(requestBody:GetNewCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetNewCompany", {
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
         resolve(data as GetNewCompany_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_CompanyListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyRow{
   "odatametadata":string,
   "value":Ice_Tablesets_CompanyRow,
}

export interface Ice_Tablesets_CompanyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company Name  */  
   "Name":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_CompanyRow{
   "Company1":string,
      /**  Company Name  */  
   "Name":string,
      /**  Address1  */  
   "Address1":string,
      /**  Address2  */  
   "Address2":string,
      /**  Address3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State  */  
   "State":string,
      /**  Zip  */  
   "Zip":string,
      /**  Country  */  
   "Country":string,
      /**  PhoneNum  */  
   "PhoneNum":string,
      /**  FaxNum  */  
   "FaxNum":string,
      /**  MfgSys  */  
   "MfgSys":string,
      /**  Defines the directory location used by this company to receive metadata.  */  
   "MetadataPath":string,
      /**  Web Access URL for this company  */  
   "WinWebURL":string,
      /**  Track System Activity flag  */  
   "TrackSysActivity":boolean,
      /**  Track Personalization changes flag  */  
   "TrackPersonalizationChg":boolean,
      /**  Type of report  */  
   "ReportTypePref":string,
      /**  URL for Mobile client  */  
   "MobileURL":string,
      /**  Metadatapath for Mobile Client  */  
   "MobileMetaPath":string,
      /**  Workstation Method  */  
   "WorkstationMethod":string,
      /**  Enterprise Search URL  */  
   "EntSearchURL":string,
      /**  GlobalEntSearch  */  
   "GlobalEntSearch":boolean,
      /**  SCServer  */  
   "SCServer":string,
      /**  SCUserID  */  
   "SCUserID":string,
      /**  SCPassword  */  
   "SCPassword":string,
      /**  UBAQWFPackage  */  
   "UBAQWFPackage":string,
      /**  InstallationID  */  
   "InstallationID":string,
      /**  CountryGroupCode  */  
   "CountryGroupCode":string,
      /**  CountryCode  */  
   "CountryCode":string,
      /**  CountryCodeID  */  
   "CountryCodeID":string,
      /**  DefaultLabelsPrinter  */  
   "DefaultLabelsPrinter":string,
      /**  DefaultReportsPrinter  */  
   "DefaultReportsPrinter":string,
      /**  HelpURI  */  
   "HelpURI":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SSRSBaseURL  */  
   "SSRSBaseURL":string,
      /**  SSRSDatabaseServerName  */  
   "SSRSDatabaseServerName":string,
      /**  SSRSAuthenticationType  */  
   "SSRSAuthenticationType":string,
      /**  SSRSDatabaseUser  */  
   "SSRSDatabaseUser":string,
      /**  SSRSDatabaseUserPassword  */  
   "SSRSDatabaseUserPassword":string,
      /**  SSRSDatabaseName  */  
   "SSRSDatabaseName":string,
      /**  SSRSOverrideDefaults  */  
   "SSRSOverrideDefaults":boolean,
      /**  SSRSPrintOptions  */  
   "SSRSPrintOptions":string,
      /**  TimeZoneID  */  
   "TimeZoneID":string,
      /**  DefaultLayoutID  */  
   "DefaultLayoutID":string,
      /**  ODBCUserID  */  
   "ODBCUserID":string,
      /**  ODBCPassword  */  
   "ODBCPassword":string,
      /**  EpicorEducationURL  */  
   "EpicorEducationURL":string,
      /**  EpicorHelpURL  */  
   "EpicorHelpURL":string,
      /**  TenantID  */  
   "TenantID":string,
      /**  GridsUseBaseCurrencyInfo  */  
   "GridsUseBaseCurrencyInfo":boolean,
      /**  EDDURL  */  
   "EDDURL":string,
      /**  EdiProcessing  */  
   "EdiProcessing":string,
      /**  ReportLoggingLevel  */  
   "ReportLoggingLevel":string,
      /**  ImportAPIMaxDOP  */  
   "ImportAPIMaxDOP":number,
      /**  TelemetryOptIn  */  
   "TelemetryOptIn":boolean,
      /**  TelemetryOptOutReason  */  
   "TelemetryOptOutReason":string,
      /**  ImportPurgeInterval  */  
   "ImportPurgeInterval":number,
      /**  ImportMaxFileSize  */  
   "ImportMaxFileSize":number,
      /**  TelemetryKey  */  
   "TelemetryKey":string,
      /**  DefaultHomepageLayoutID  */  
   "DefaultHomepageLayoutID":string,
      /**  IsLive  */  
   "IsLive":boolean,
      /**  KineticColor  */  
   "KineticColor":string,
      /**  DefaultPaperSize  */  
   "DefaultPaperSize":string,
      /**  NomenclatureID  */  
   "NomenclatureID":string,
   "GlobalEducationURL":boolean,
      /**  Indicates whether or not the education courses URL is global or just for this specific company.  */  
   "GlobalHelpURL":boolean,
   "ODBCPasswordMasked":string,
      /**  Indicates if the end user can download the Edge Agent installer via the Kinetic client.  */  
   "AllowEdgeAgentUserInstall":boolean,
      /**  The company logo file name, stored in a server shared folder.  */  
   "LogoFileName":string,
      /**  The logo image content as Base-64 string.  */  
   "LogoImageContent":string,
      /**  Kinetic color - in CSS format, i.e: rgba(255, 255, 255, 0)  */  
   "KineticCssColor":string,
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
      @param company
   */  
export interface DeleteByID_input{
   company:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param company
   */  
export interface GetByID_input{
   company:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_CompanyTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_CompanyTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_CompanyTableset[],
}

   /** Required : 
      @param SQLAuthtype
      @param SQLServer
      @param DBUser
      @param DBPassword
   */  
export interface GetDBNameList_input{
   SQLAuthtype:string,
   SQLServer:string,
   DBUser:string,
   DBPassword:string,
}

export interface GetDBNameList_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
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
   returnObj:Ice_Tablesets_CompanyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCompany_input{
   ds:Ice_Tablesets_CompanyTableset[],
}

export interface GetNewCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param server
      @param userName
      @param password
   */  
export interface GetPackageProcessList_input{
      /**  the Epicor Service Connect server  */  
   server:string,
      /**  the Epicor Service Connect username  */  
   userName:string,
      /**  the Epicor Service Connect password  */  
   password:string,
}

export interface GetPackageProcessList_output{
   returnObj:Ice_BO_Company_Contracts_PackageInfo[],
}

   /** Required : 
      @param whereClauseCompany
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCompany:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_CompanyTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSystemTimeZoneList_output{
   returnObj:string,
}

export interface Ice_BO_Company_Contracts_PackageInfo{
   Name:string,
   Processes:string,
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

export interface Ice_Tablesets_CompanyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CompanyListTableset{
   CompanyList:Ice_Tablesets_CompanyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_CompanyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  Address1  */  
   Address1:string,
      /**  Address2  */  
   Address2:string,
      /**  Address3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State  */  
   State:string,
      /**  Zip  */  
   Zip:string,
      /**  Country  */  
   Country:string,
      /**  PhoneNum  */  
   PhoneNum:string,
      /**  FaxNum  */  
   FaxNum:string,
      /**  MfgSys  */  
   MfgSys:string,
      /**  Defines the directory location used by this company to receive metadata.  */  
   MetadataPath:string,
      /**  Web Access URL for this company  */  
   WinWebURL:string,
      /**  Track System Activity flag  */  
   TrackSysActivity:boolean,
      /**  Track Personalization changes flag  */  
   TrackPersonalizationChg:boolean,
      /**  Type of report  */  
   ReportTypePref:string,
      /**  URL for Mobile client  */  
   MobileURL:string,
      /**  Metadatapath for Mobile Client  */  
   MobileMetaPath:string,
      /**  Workstation Method  */  
   WorkstationMethod:string,
      /**  Enterprise Search URL  */  
   EntSearchURL:string,
      /**  GlobalEntSearch  */  
   GlobalEntSearch:boolean,
      /**  SCServer  */  
   SCServer:string,
      /**  SCUserID  */  
   SCUserID:string,
      /**  SCPassword  */  
   SCPassword:string,
      /**  UBAQWFPackage  */  
   UBAQWFPackage:string,
      /**  InstallationID  */  
   InstallationID:string,
      /**  CountryGroupCode  */  
   CountryGroupCode:string,
      /**  CountryCode  */  
   CountryCode:string,
      /**  CountryCodeID  */  
   CountryCodeID:string,
      /**  DefaultLabelsPrinter  */  
   DefaultLabelsPrinter:string,
      /**  DefaultReportsPrinter  */  
   DefaultReportsPrinter:string,
      /**  HelpURI  */  
   HelpURI:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SSRSBaseURL  */  
   SSRSBaseURL:string,
      /**  SSRSDatabaseServerName  */  
   SSRSDatabaseServerName:string,
      /**  SSRSAuthenticationType  */  
   SSRSAuthenticationType:string,
      /**  SSRSDatabaseUser  */  
   SSRSDatabaseUser:string,
      /**  SSRSDatabaseUserPassword  */  
   SSRSDatabaseUserPassword:string,
      /**  SSRSDatabaseName  */  
   SSRSDatabaseName:string,
      /**  SSRSOverrideDefaults  */  
   SSRSOverrideDefaults:boolean,
      /**  SSRSPrintOptions  */  
   SSRSPrintOptions:string,
      /**  TimeZoneID  */  
   TimeZoneID:string,
      /**  DefaultLayoutID  */  
   DefaultLayoutID:string,
      /**  ODBCUserID  */  
   ODBCUserID:string,
      /**  ODBCPassword  */  
   ODBCPassword:string,
      /**  EpicorEducationURL  */  
   EpicorEducationURL:string,
      /**  EpicorHelpURL  */  
   EpicorHelpURL:string,
      /**  TenantID  */  
   TenantID:string,
      /**  GridsUseBaseCurrencyInfo  */  
   GridsUseBaseCurrencyInfo:boolean,
      /**  EDDURL  */  
   EDDURL:string,
      /**  EdiProcessing  */  
   EdiProcessing:string,
      /**  ReportLoggingLevel  */  
   ReportLoggingLevel:string,
      /**  ImportAPIMaxDOP  */  
   ImportAPIMaxDOP:number,
      /**  TelemetryOptIn  */  
   TelemetryOptIn:boolean,
      /**  TelemetryOptOutReason  */  
   TelemetryOptOutReason:string,
      /**  ImportPurgeInterval  */  
   ImportPurgeInterval:number,
      /**  ImportMaxFileSize  */  
   ImportMaxFileSize:number,
      /**  TelemetryKey  */  
   TelemetryKey:string,
      /**  DefaultHomepageLayoutID  */  
   DefaultHomepageLayoutID:string,
      /**  IsLive  */  
   IsLive:boolean,
      /**  KineticColor  */  
   KineticColor:string,
      /**  DefaultPaperSize  */  
   DefaultPaperSize:string,
      /**  NomenclatureID  */  
   NomenclatureID:string,
   GlobalEducationURL:boolean,
      /**  Indicates whether or not the education courses URL is global or just for this specific company.  */  
   GlobalHelpURL:boolean,
   ODBCPasswordMasked:string,
      /**  Indicates if the end user can download the Edge Agent installer via the Kinetic client.  */  
   AllowEdgeAgentUserInstall:boolean,
      /**  The company logo file name, stored in a server shared folder.  */  
   LogoFileName:string,
      /**  The logo image content as Base-64 string.  */  
   LogoImageContent:string,
      /**  Kinetic color - in CSS format, i.e: rgba(255, 255, 255, 0)  */  
   KineticCssColor:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CompanyTableset{
   Company:Ice_Tablesets_CompanyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtCompanyTableset{
   Company:Ice_Tablesets_CompanyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtCompanyTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtCompanyTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateLogoImage_input{
   ds:Ice_Tablesets_CompanyTableset[],
}

export interface UpdateLogoImage_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_CompanyTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param SQLAuthtype
      @param SQLServer
      @param SQLDBName
      @param DBUser
      @param DBPassword
   */  
export interface VerifySSRSConnection_input{
   SQLAuthtype:string,
   SQLServer:string,
   SQLDBName:string,
   DBUser:string,
   DBPassword:string,
}

export interface VerifySSRSConnection_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMessage:string,
}
}

