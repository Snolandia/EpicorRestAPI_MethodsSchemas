import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.ObjectSecuritySvc
// Description: Service level security.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/$metadata", {
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
   Description: Get ObjectSecurities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ObjectSecurities
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
export function get_ObjectSecurities(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities", {
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
   OperationID: NewUpdateExt_ObjectSecurities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SecurityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.SecurityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ObjectSecurities(requestBody:Ice_Tablesets_SecurityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities", {
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
   Summary: Calls GetByID to retrieve the ObjectSecurity item
   Description: Calls GetByID to retrieve the ObjectSecurity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ObjectSecurity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.SecurityRow
   */  
export function get_ObjectSecurities_Company_SecCode(Company:string, SecCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SecurityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities(" + Company + "," + SecCode + ")", {
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
   Summary: Calls UpdateExt to update ObjectSecurity for the service
   Description: Calls UpdateExt to update ObjectSecurity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ObjectSecurity
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
export function patch_ObjectSecurities_Company_SecCode(Company:string, SecCode:string, requestBody:Ice_Tablesets_SecurityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities(" + Company + "," + SecCode + ")", {
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
   Summary: Call UpdateExt to delete ObjectSecurity item
   Description: Call UpdateExt to delete ObjectSecurity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ObjectSecurity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ObjectSecurities_Company_SecCode(Company:string, SecCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities(" + Company + "," + SecCode + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get ObjectSecurityMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ObjectSecurityMethods
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ObjectSecurityMethodRow
   */  
export function get_ObjectSecurityMethods(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ObjectSecurityMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ObjectSecurityMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ObjectSecurityMethods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ObjectSecurityMethods(requestBody:Ice_Tablesets_ObjectSecurityMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods", {
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
   Summary: Calls GetByID to retrieve the ObjectSecurityMethod item
   Description: Calls GetByID to retrieve the ObjectSecurityMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ObjectSecurityMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
   */  
export function get_ObjectSecurityMethods_Company_SecCode(Company:string, SecCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ObjectSecurityMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods(" + Company + "," + SecCode + ")", {
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
         resolve(data as Ice_Tablesets_ObjectSecurityMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ObjectSecurityMethod for the service
   Description: Calls UpdateExt to update ObjectSecurityMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ObjectSecurityMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ObjectSecurityMethods_Company_SecCode(Company:string, SecCode:string, requestBody:Ice_Tablesets_ObjectSecurityMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods(" + Company + "," + SecCode + ")", {
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
   Summary: Call UpdateExt to delete ObjectSecurityMethod item
   Description: Call UpdateExt to delete ObjectSecurityMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ObjectSecurityMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SecCode Desc: SecCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ObjectSecurityMethods_Company_SecCode(Company:string, SecCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods(" + Company + "," + SecCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", {
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseSecurity:string, whereClauseObjectSecurityMethod:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
   if(typeof whereClauseObjectSecurityMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseObjectSecurityMethod=" + whereClauseObjectSecurityMethod
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetRows" + params, {
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
export function get_GetByID(secCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetList" + params, {
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
   Summary: Invoke method CheckCompanyInfo
   Description: This method is run before Update method to warn
           the user if the same record exists, the old record will be deleted during
           saving.
   OperationID: CheckCompanyInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCompanyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCompanyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCompanyInfo(requestBody:CheckCompanyInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCompanyInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/CheckCompanyInfo", {
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
         resolve(data as CheckCompanyInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDEx
   Description: This method returns a dataset representing a Security with CompanyID,
which is allowable for the current company.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetByIDEx", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetListEx", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetMethodList", {
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
   Summary: Invoke method GetServiceMethodList
   Description: This method returns a list of the public methods for the given
service.
   OperationID: GetServiceMethodList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetServiceMethodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServiceMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetServiceMethodList(requestBody:GetServiceMethodList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetServiceMethodList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetServiceMethodList", {
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
         resolve(data as GetServiceMethodList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUserGroupList
   Description: Get combined list of user and groups to use in MetaFx.
   OperationID: GetUserGroupList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserGroupList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserGroupList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUserGroupList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetUserGroupList", {
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
         resolve(data as GetUserGroupList_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetNewSubSecurity", {
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
   Summary: Invoke method ValidateNewSecCode
   Description: This method don't allow create new record, if there are records
           with the same code for all companies and for the current company.
           If there is only record for all companies, this method retuns the current
           company ID to allow create new record only for the current company.
   OperationID: ValidateNewSecCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNewSecCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNewSecCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNewSecCode(requestBody:ValidateNewSecCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNewSecCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ValidateNewSecCode", {
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
         resolve(data as ValidateNewSecCode_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GlobalRecordFound", {
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
   Summary: Invoke method AddServices
   Description: This method will add new service to the ice.security table
   OperationID: AddServices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddServices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddServices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddServices(requestBody:AddServices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddServices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/AddServices", {
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
         resolve(data as AddServices_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetNewSecurity", {
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
   Summary: Invoke method GetNewObjectSecurityMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewObjectSecurityMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewObjectSecurityMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewObjectSecurityMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewObjectSecurityMethod(requestBody:GetNewObjectSecurityMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewObjectSecurityMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetNewObjectSecurityMethod", {
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
         resolve(data as GetNewObjectSecurityMethod_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ObjectSecurityMethodRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ObjectSecurityMethodRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SecurityListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SecurityRow,
}

export interface Ice_Tablesets_ObjectSecurityMethodRow{
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
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "AllowAll":boolean,
   "AllowAccess":string,
   "DisallowAll":boolean,
   "DisallowAccess":string,
   "AllCompanies":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
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
      @param directroyName
      @param password
   */  
export interface AddServices_input{
      /**  Dirextory name to serch for services: C:\_projects\ERP10CC\Current\Deployment\Server\Assemblies  */  
   directroyName:string,
      /**  System Password to run method  */  
   password:string,
}

export interface AddServices_output{
}

   /** Required : 
      @param secCode
      @param pcCurCompOnly
   */  
export interface CheckCompanyInfo_input{
      /**  The current security code  */  
   secCode:string,
      /**  The flag CurrentCompanyOnly  */  
   pcCurCompOnly:boolean,
}

export interface CheckCompanyInfo_output{
parameters : {
      /**  output parameters  */  
   rowExists:boolean,
}
}

   /** Required : 
      @param secCode
   */  
export interface DeleteByID_input{
   secCode:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param secCode
      @param pcComp
      @param strictPrimKey
   */  
export interface GetByIDEx_input{
      /**  The security code  */  
   secCode:string,
      /**  The company  */  
   pcComp:string,
      /**  If it is false, look for all recordes allowed for the current company  */  
   strictPrimKey:boolean,
}

export interface GetByIDEx_output{
   returnObj:Ice_Tablesets_ObjectSecurityTableset[],
}

   /** Required : 
      @param secCode
   */  
export interface GetByID_input{
   secCode:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ObjectSecurityTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ObjectSecurityTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ObjectSecurityTableset[],
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
   */  
export interface GetNewObjectSecurityMethod_input{
   ds:Ice_Tablesets_ObjectSecurityTableset[],
}

export interface GetNewObjectSecurityMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ObjectSecurityTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSecurity_input{
   ds:Ice_Tablesets_ObjectSecurityTableset[],
}

export interface GetNewSecurity_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ObjectSecurityTableset,
}
}

   /** Required : 
      @param ds
      @param parentSecCode
      @param secCode
   */  
export interface GetNewSubSecurity_input{
   ds:Ice_Tablesets_ObjectSecurityTableset[],
      /**  The parent security code  */  
   parentSecCode:string,
      /**  The security code  */  
   secCode:string,
}

export interface GetNewSubSecurity_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ObjectSecurityTableset,
}
}

   /** Required : 
      @param whereClauseSecurity
      @param whereClauseObjectSecurityMethod
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSecurity:string,
   whereClauseObjectSecurityMethod:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ObjectSecurityTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param secCode
   */  
export interface GetServiceMethodList_input{
      /**  Service security code.  */  
   secCode:string,
}

export interface GetServiceMethodList_output{
   returnObj:Ice_Tablesets_ServiceMethodListTableset[],
}

export interface GetUserGroupList_output{
   returnObj:Ice_Tablesets_UserGroupListTableset[],
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

export interface Ice_Tablesets_ObjectSecurityMethodRow{
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
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   AllowAll:boolean,
   AllowAccess:string,
   DisallowAll:boolean,
   DisallowAccess:string,
   AllCompanies:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ObjectSecurityTableset{
   Security:Ice_Tablesets_SecurityRow[],
   ObjectSecurityMethod:Ice_Tablesets_ObjectSecurityMethodRow[],
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

export interface Ice_Tablesets_ServiceMethodListRow{
      /**  Method Name  */  
   Name:string,
      /**  Method description  */  
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ServiceMethodListTableset{
   ServiceMethodList:Ice_Tablesets_ServiceMethodListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtObjectSecurityTableset{
   Security:Ice_Tablesets_SecurityRow[],
   ObjectSecurityMethod:Ice_Tablesets_ObjectSecurityMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UserGroupListRow{
      /**  User ID or Group Code  */  
   ID:string,
      /**  User or group name  */  
   Name:string,
      /**  Record type: 0 - User, 1-Group  */  
   Type:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UserGroupListTableset{
   UserGroupList:Ice_Tablesets_UserGroupListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtObjectSecurityTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtObjectSecurityTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ObjectSecurityTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ObjectSecurityTableset,
}
}

   /** Required : 
      @param newSecCode
   */  
export interface ValidateNewSecCode_input{
      /**  The new security code  */  
   newSecCode:string,
}

export interface ValidateNewSecCode_output{
parameters : {
      /**  output parameters  */  
   curComp:string,
}
}

