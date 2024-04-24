import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.AdminCompanySvc
// Description: Company maintenance business object for use by Admin Console
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/$metadata", {
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
   Description: Get AdminCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AdminCompanies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AdminCompanyRow
   */  
export function get_AdminCompanies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AdminCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AdminCompanies(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies", {
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
   Summary: Calls GetByID to retrieve the AdminCompany item
   Description: Calls GetByID to retrieve the AdminCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AdminCompany
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
   */  
export function get_AdminCompanies_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AdminCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies(" + Company + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AdminCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AdminCompany for the service
   Description: Calls UpdateExt to update AdminCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AdminCompany
      @param Company Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AdminCompanies_Company(Company:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies(" + Company + ")", {
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
   Summary: Call UpdateExt to delete AdminCompany item
   Description: Call UpdateExt to delete AdminCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AdminCompany
      @param Company Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AdminCompanies_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies(" + Company + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AdminCompanyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyListRow)
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
export function get_GetRows(whereClauseAdminCompany:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAdminCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAdminCompany=" + whereClauseAdminCompany
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetRows" + params, {
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetList" + params, {
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
   Summary: Invoke method AddCompany
   Description: This method adds a new company.
   OperationID: AddCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AddCompany", {
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
   Summary: Invoke method SetProductionInstance
   Description: Update the global licensing portal and mark the production instance as true / false.
   OperationID: SetProductionInstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetProductionInstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetProductionInstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetProductionInstance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/SetProductionInstance", {
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
   Summary: Invoke method AssignLicense
   Description: This method updates the installation id of a license for a Company.
   OperationID: AssignLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLicense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AssignLicense", {
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
   Summary: Invoke method ChangeCountryCodeID
   Description: This method updates the CGC codes for a Company.
   OperationID: ChangeCountryCodeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCountryCodeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCountryCodeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCountryCodeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/ChangeCountryCodeID", {
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
   Summary: Invoke method ChangeCountryCode
   Description: This method updates the CGC codes for a Company.
   OperationID: ChangeCountryCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCountryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCountryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCountryCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/ChangeCountryCode", {
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
   Summary: Invoke method ChangeCompanyName
   Description: This method updates the name for a Company.
   OperationID: ChangeCompanyName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompanyName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompanyName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCompanyName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/ChangeCompanyName", {
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
   Summary: Invoke method DeleteByCompanyId
   Description: This method deletes the Company with the specified id and
and all of the associated data for the company.
   OperationID: DeleteByCompanyId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByCompanyId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByCompanyId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByCompanyId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/DeleteByCompanyId", {
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
   Summary: Invoke method DeleteBySysRowId
   Description: This method deletes the Company with the specified id and
and all of the associated data for the company.
   OperationID: DeleteBySysRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteBySysRowId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/DeleteBySysRowId", {
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
   Summary: Invoke method GetByCompanyId
   Description: This method retrieves details of the Company with the specified id.
   OperationID: GetByCompanyId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByCompanyId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCompanyId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByCompanyId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetByCompanyId", {
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
   Summary: Invoke method GetListBySysRowId
   Description: This method retrieves details of the Company with the specified id.
   OperationID: GetListBySysRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListBySysRowId(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetListBySysRowId", {
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
   Summary: Invoke method GetCompanyList
   Description: Returns a list of all companies. regardless visibility.
   OperationID: GetCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetCompanyList", {
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
   Summary: Invoke method ExposeCurrencyData
   Description: Determines whether or not admin console should expose currency functionality.
   OperationID: ExposeCurrencyData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExposeCurrencyData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExposeCurrencyData(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/ExposeCurrencyData", {
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
   Summary: Invoke method GetServerLogTraceSettings
   Description: Returns a dataset with the current trace settings for use at the administration console.
   OperationID: GetServerLogTraceSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServerLogTraceSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetServerLogTraceSettings(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetServerLogTraceSettings", {
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
   Summary: Invoke method SetServerLogTraceSettings
   Description: Sets the trace section configuration depending on the dataset sent to it.
   OperationID: SetServerLogTraceSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetServerLogTraceSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetServerLogTraceSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetServerLogTraceSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/SetServerLogTraceSettings", {
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
   Summary: Invoke method ChangeCompaniesTelemetryOptStatus
   Description: Changes the opt out status of multiple companies
   OperationID: ChangeCompaniesTelemetryOptStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompaniesTelemetryOptStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompaniesTelemetryOptStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCompaniesTelemetryOptStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/ChangeCompaniesTelemetryOptStatus", {
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
   Summary: Invoke method GetCompaniesTelemetryOptStatus
   Description: Gets the Opt status of multiple companies
   OperationID: GetCompaniesTelemetryOptStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompaniesTelemetryOptStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompaniesTelemetryOptStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompaniesTelemetryOptStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetCompaniesTelemetryOptStatus", {
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
   Summary: Invoke method GetGlobalSetting
   Description: Get configuration strings from Ice.GlobalSetting and Ice.GlobalSettingAttribute table
   OperationID: GetGlobalSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlobalSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlobalSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlobalSetting(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetGlobalSetting", {
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
   Summary: Invoke method GetCgcCode
   Description: This method get the CGC Code given the guid of the country.
   OperationID: GetCgcCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCgcCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCgcCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCgcCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetCgcCode", {
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
   Summary: Invoke method GetLicenseInfoViewerAppUrl
   Description: Gets the license viewer URL.
   OperationID: GetLicenseInfoViewerAppUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicenseInfoViewerAppUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLicenseInfoViewerAppUrl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetLicenseInfoViewerAppUrl", {
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
   Summary: Invoke method UpdateIsLiveFlag
   Description: Updates the IsLive flag in Cosmos DB.
   OperationID: UpdateIsLiveFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateIsLiveFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIsLiveFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateIsLiveFlag(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/UpdateIsLiveFlag", {
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
   Summary: Invoke method GetNewAdminCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAdminCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAdminCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAdminCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAdminCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetNewAdminCompany", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AdminCompanyListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AdminCompanyRow[],
}

export interface Ice_Tablesets_AdminCompanyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company Name  */  
   "Name":string,
      /**  MfgSys  */  
   "MfgSys":string,
      /**  Web Access URL for this company  */  
   "WinWebURL":string,
      /**  InstallationID  */  
   "InstallationID":string,
      /**  CountryGroupCode  */  
   "CountryGroupCode":string,
      /**  CountryCode  */  
   "CountryCode":string,
      /**  CountryCodeID  */  
   "CountryCodeID":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Product":string,
   "BaseCurrencyCode":string,
   "DecimalsGeneral":number,
   "DecimalsCost":number,
   "DecimalsPrice":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_AdminCompanyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company Name  */  
   "Name":string,
      /**  MfgSys  */  
   "MfgSys":string,
      /**  Web Access URL for this company  */  
   "WinWebURL":string,
      /**  InstallationID  */  
   "InstallationID":string,
      /**  CountryGroupCode  */  
   "CountryGroupCode":string,
      /**  CountryCode  */  
   "CountryCode":string,
      /**  CountryCodeID  */  
   "CountryCodeID":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Product":string,
   "BaseCurrencyCode":string,
   "DecimalsGeneral":number,
   "DecimalsCost":number,
   "DecimalsPrice":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param companyID
      @param companyName
      @param installationID
      @param currencyCode
      @param decimalsGeneral
      @param decimalsCost
      @param decimalsPrice
      @param countryCode
      @param countryGroupCode
   */  
export interface AddCompany_input{
      /**  Id for the new Company  */  
   companyID:string,
      /**  Name for the new Company  */  
   companyName:string,
      /**  Installation id for license to be assigned for the new Company  */  
   installationID:string,
      /**  The base currency code for the new Company  */  
   currencyCode:string,
      /**  General Decimals for the base currency code for the new Company  */  
   decimalsGeneral:number,
      /**  Unit Cost Decimals for the base currency code for the new Company  */  
   decimalsCost:number,
      /**  Unit Prices Decimals for the base currency code for the new Company  */  
   decimalsPrice:number,
      /**  The Country code to use for Country Specific Functionality.  */  
   countryCode:string,
      /**  The Country Group code to use for Country Specific Functionality.  */  
   countryGroupCode:string,
}

export interface AddCompany_output{
}

   /** Required : 
      @param companyID
      @param installationID
   */  
export interface AssignLicense_input{
      /**  Id for the Company  */  
   companyID:string,
      /**  Installation Id of license to be assigned to the Company  */  
   installationID:string,
}

export interface AssignLicense_output{
}

   /** Required : 
      @param action
      @param companies
   */  
export interface ChangeCompaniesTelemetryOptStatus_input{
      /**  available options are OptOut, OptIn  */  
   action:string,
      /**  if no entries are sent all companies are changed  */  
   companies:string,
}

export interface ChangeCompaniesTelemetryOptStatus_output{
}

   /** Required : 
      @param companyID
      @param companyName
   */  
export interface ChangeCompanyName_input{
      /**  Id for the Company  */  
   companyID:string,
      /**  New name for the Company  */  
   companyName:string,
}

export interface ChangeCompanyName_output{
}

   /** Required : 
      @param companyID
      @param countryCodeID
   */  
export interface ChangeCountryCodeID_input{
      /**  Id for the Company  */  
   companyID:string,
      /**  The country code ID.  */  
   countryCodeID:string,
}

export interface ChangeCountryCodeID_output{
}

   /** Required : 
      @param companyID
      @param countryCode
   */  
export interface ChangeCountryCode_input{
      /**  Id for the Company  */  
   companyID:string,
      /**  The country code ID.  */  
   countryCode:string,
}

export interface ChangeCountryCode_output{
}

   /** Required : 
      @param companyID
   */  
export interface DeleteByCompanyId_input{
      /**  Id for Company to be deleted  */  
   companyID:string,
}

export interface DeleteByCompanyId_output{
}

   /** Required : 
      @param company
   */  
export interface DeleteByID_input{
   company:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param sysRowID
   */  
export interface DeleteBySysRowId_input{
      /**  SysRowID for Company to be deleted  */  
   sysRowID:string,
}

export interface DeleteBySysRowId_output{
}

export interface ExposeCurrencyData_output{
   returnObj:boolean,
}

   /** Required : 
      @param companyID
   */  
export interface GetByCompanyId_input{
      /**  CompanyId for Company to be retrieved  */  
   companyID:string,
}

export interface GetByCompanyId_output{
   returnObj:Ice_Tablesets_AdminCompanyListTableset[],
}

   /** Required : 
      @param company
   */  
export interface GetByID_input{
   company:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_AdminCompanyTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_AdminCompanyTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_AdminCompanyTableset[],
}

   /** Required : 
      @param csfCountry
   */  
export interface GetCgcCode_input{
      /**  Guid of the country  */  
   csfCountry:string,
}

export interface GetCgcCode_output{
   returnObj:string,
}

   /** Required : 
      @param companies
   */  
export interface GetCompaniesTelemetryOptStatus_input{
      /**  if no entries are sent all companies are sent back  */  
   companies:string,
}

export interface GetCompaniesTelemetryOptStatus_output{
      /**  A dictionary of company, and telemetry either on or off  */  
   returnObj:any,      //schema had no properties on an object.
}

export interface GetCompanyList_output{
   returnObj:Ice_Tablesets_AdminCompanyListTableset[],
}

   /** Required : 
      @param settingType
      @param settingName
   */  
export interface GetGlobalSetting_input{
      /**  SettingType corresponding to the configuration.  */  
   settingType:string,
      /**  SettingName is the key for the configuration.  */  
   settingName:string,
}

export interface GetGlobalSetting_output{
      /**  A string if the setting was found in either of the tables, else null.  */  
   returnObj:string,
}

export interface GetLicenseInfoViewerAppUrl_output{
      /**  License Viewer App URL  */  
   returnObj:string,
}

   /** Required : 
      @param sysRowID
   */  
export interface GetListBySysRowId_input{
      /**  SysRowID for Company to be retrieved  */  
   sysRowID:string,
}

export interface GetListBySysRowId_output{
   returnObj:Ice_Tablesets_AdminCompanyListTableset[],
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
   returnObj:Ice_Tablesets_AdminCompanyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAdminCompany_input{
   ds:Ice_Tablesets_AdminCompanyTableset[],
}

export interface GetNewAdminCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AdminCompanyTableset[],
}
}

   /** Required : 
      @param whereClauseAdminCompany
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAdminCompany:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_AdminCompanyTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetServerLogTraceSettings_output{
      /**  A Ice.BO.AdminCompany.ServerLogTraceDS containing the trace settings.  */  
   returnObj:any,      //schema had no properties on an object.
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

export interface Ice_Tablesets_AdminCompanyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  MfgSys  */  
   MfgSys:string,
      /**  Web Access URL for this company  */  
   WinWebURL:string,
      /**  InstallationID  */  
   InstallationID:string,
      /**  CountryGroupCode  */  
   CountryGroupCode:string,
      /**  CountryCode  */  
   CountryCode:string,
      /**  CountryCodeID  */  
   CountryCodeID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Product:string,
   BaseCurrencyCode:string,
   DecimalsGeneral:number,
   DecimalsCost:number,
   DecimalsPrice:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AdminCompanyListTableset{
   AdminCompanyList:Ice_Tablesets_AdminCompanyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AdminCompanyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  MfgSys  */  
   MfgSys:string,
      /**  Web Access URL for this company  */  
   WinWebURL:string,
      /**  InstallationID  */  
   InstallationID:string,
      /**  CountryGroupCode  */  
   CountryGroupCode:string,
      /**  CountryCode  */  
   CountryCode:string,
      /**  CountryCodeID  */  
   CountryCodeID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Product:string,
   BaseCurrencyCode:string,
   DecimalsGeneral:number,
   DecimalsCost:number,
   DecimalsPrice:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AdminCompanyTableset{
   AdminCompany:Ice_Tablesets_AdminCompanyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtAdminCompanyTableset{
   AdminCompany:Ice_Tablesets_AdminCompanyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param licenseId
      @param companyId
      @param dbHash
      @param isSetAsProductionInstance
   */  
export interface SetProductionInstance_input{
      /**  LicenseId of the ERP10 instance  */  
   licenseId:string,
      /**  Id for the Company  */  
   companyId:string,
      /**  DBHash of the ERP10 instance  */  
   dbHash:string,
   isSetAsProductionInstance:boolean,
}

export interface SetProductionInstance_output{
   returnObj:boolean,
}

   /** Required : 
      @param traceDS
   */  
export interface SetServerLogTraceSettings_input{
   traceDS:any,      //schema had no properties on an object.
}

export interface SetServerLogTraceSettings_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtAdminCompanyTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtAdminCompanyTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param companyID
   */  
export interface UpdateIsLiveFlag_input{
      /**  company ID.  */  
   companyID:string,
}

export interface UpdateIsLiveFlag_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_AdminCompanyTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AdminCompanyTableset[],
}
}

