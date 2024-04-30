import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.NamedSearchSvc
// Description: Stores user-defined search parameters, along with two child tables, ControlSettings and WhereClauses.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/$metadata", {
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
   Description: Get NamedSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NamedSearches
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NamedSearchRow
   */  
export function get_NamedSearches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NamedSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.NamedSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.NamedSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NamedSearches(requestBody:Ice_Tablesets_NamedSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches", {
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
   Summary: Calls GetByID to retrieve the NamedSearch item
   Description: Calls GetByID to retrieve the NamedSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NamedSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.NamedSearchRow
   */  
export function get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_NamedSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")", {
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
         resolve(data as Ice_Tablesets_NamedSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NamedSearch for the service
   Description: Calls UpdateExt to update NamedSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NamedSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.NamedSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, requestBody:Ice_Tablesets_NamedSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")", {
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
   Summary: Call UpdateExt to delete NamedSearch item
   Description: Call UpdateExt to delete NamedSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NamedSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get ControlSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ControlSettings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ControlSettingRow
   */  
export function get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_ControlSettings(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ControlSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/ControlSettings", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ControlSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ControlSetting item
   Description: Calls GetByID to retrieve the ControlSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlSetting1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param ControlGuid Desc: ControlGuid   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ControlSettingRow
   */  
export function get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, ControlGuid:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ControlSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")", {
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
         resolve(data as Ice_Tablesets_ControlSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get WhereClauses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhereClauses1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseRow
   */  
export function get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_WhereClauses(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/WhereClauses", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WhereClause item
   Description: Calls GetByID to retrieve the WhereClause item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClause1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.WhereClauseRow
   */  
export function get_NamedSearches_Company_SearchForm_NSId_UserID_CalledFrom_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, TableName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_WhereClauseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/NamedSearches(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + ")/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")", {
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
         resolve(data as Ice_Tablesets_WhereClauseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ControlSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlSettings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ControlSettingRow
   */  
export function get_ControlSettings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ControlSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ControlSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ControlSettingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ControlSettings(requestBody:Ice_Tablesets_ControlSettingRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings", {
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
   Summary: Calls GetByID to retrieve the ControlSetting item
   Description: Calls GetByID to retrieve the ControlSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlSetting
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param ControlGuid Desc: ControlGuid   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ControlSettingRow
   */  
export function get_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, ControlGuid:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ControlSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")", {
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
         resolve(data as Ice_Tablesets_ControlSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ControlSetting for the service
   Description: Calls UpdateExt to update ControlSetting. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlSetting
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param ControlGuid Desc: ControlGuid   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ControlSettingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, ControlGuid:string, requestBody:Ice_Tablesets_ControlSettingRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")", {
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
   Summary: Call UpdateExt to delete ControlSetting item
   Description: Call UpdateExt to delete ControlSetting item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlSetting
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param ControlGuid Desc: ControlGuid   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ControlSettings_Company_SearchForm_NSId_UserID_CalledFrom_ControlGuid(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, ControlGuid:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/ControlSettings(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + ControlGuid + ")", {
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
   Description: Get WhereClauses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhereClauses
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseRow
   */  
export function get_WhereClauses(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhereClauses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.WhereClauseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhereClauses(requestBody:Ice_Tablesets_WhereClauseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses", {
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
   Summary: Calls GetByID to retrieve the WhereClause item
   Description: Calls GetByID to retrieve the WhereClause item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClause
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.WhereClauseRow
   */  
export function get_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, TableName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_WhereClauseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")", {
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
         resolve(data as Ice_Tablesets_WhereClauseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WhereClause for the service
   Description: Calls UpdateExt to update WhereClause. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhereClause
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.WhereClauseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, TableName:string, requestBody:Ice_Tablesets_WhereClauseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")", {
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
   Summary: Call UpdateExt to delete WhereClause item
   Description: Call UpdateExt to delete WhereClause item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhereClause
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SearchForm Desc: SearchForm   Required: True   Allow empty value : True
      @param NSId Desc: NSId   Required: True   Allow empty value : True
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param CalledFrom Desc: CalledFrom   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WhereClauses_Company_SearchForm_NSId_UserID_CalledFrom_TableName(Company:string, SearchForm:string, NSId:string, UserID:string, CalledFrom:string, TableName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/WhereClauses(" + Company + "," + SearchForm + "," + NSId + "," + UserID + "," + CalledFrom + "," + TableName + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NamedSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseNamedSearch:string, whereClauseControlSetting:string, whereClauseWhereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseNamedSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNamedSearch=" + whereClauseNamedSearch
   }
   if(typeof whereClauseControlSetting!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseControlSetting=" + whereClauseControlSetting
   }
   if(typeof whereClauseWhereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWhereClause=" + whereClauseWhereClause
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(searchForm:string, nsId:string, userID:string, calledFrom:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof searchForm!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "searchForm=" + searchForm
   }
   if(typeof nsId!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "nsId=" + nsId
   }
   if(typeof userID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "userID=" + userID
   }
   if(typeof calledFrom!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "calledFrom=" + calledFrom
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewNamedSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNamedSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewNamedSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNamedSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewNamedSearch(requestBody:GetNewNamedSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewNamedSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetNewNamedSearch", {
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
         resolve(data as GetNewNamedSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewControlSetting
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlSetting
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewControlSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewControlSetting(requestBody:GetNewControlSetting_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewControlSetting_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetNewControlSetting", {
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
         resolve(data as GetNewControlSetting_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewWhereClause
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhereClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWhereClause(requestBody:GetNewWhereClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewWhereClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetNewWhereClause", {
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
         resolve(data as GetNewWhereClause_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NamedSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ControlSettingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ControlSettingRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_NamedSearchListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NamedSearchRow{
   "odatametadata":string,
   "value":Ice_Tablesets_NamedSearchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseRow{
   "odatametadata":string,
   "value":Ice_Tablesets_WhereClauseRow,
}

export interface Ice_Tablesets_ControlSettingRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Search Form  */  
   "SearchForm":string,
      /**  Namespace ID  */  
   "NSId":string,
      /**  User ID  */  
   "UserID":string,
      /**  Called From  */  
   "CalledFrom":string,
      /**  Control GUID  */  
   "ControlGuid":string,
      /**  Control Value  */  
   "ControlValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  EpBinding  */  
   "EpBinding":string,
      /**  ComponentID  */  
   "ComponentID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_NamedSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Name of base search form  */  
   "SearchForm":string,
      /**  Named Search ID  */  
   "NSId":string,
      /**  User ID  */  
   "UserID":string,
      /**  UI from which the search is called from  */  
   "CalledFrom":string,
      /**  Default named search flag  */  
   "IsDefault":boolean,
      /**  Auto Execute flag  */  
   "AutoExecute":boolean,
      /**  Can unpin Criteria  */  
   "UnpinCrit":boolean,
      /**  Can be shared flag  */  
   "IsShared":boolean,
      /**  Share Type  */  
   "ShareType":string,
      /**  Return all rows flag.  */  
   "ReturnAll":boolean,
      /**  Maximum number search rows.  */  
   "MaxRows":number,
      /**  Auto select flag  */  
   "AutoSelect":boolean,
      /**  Value will be one of: "RowsDataSet" or "ListDataSet"  */  
   "DataSetMode":string,
      /**  Description  */  
   "Description":string,
      /**  "VN" = Vantage; "VS" = Vista  */  
   "ProductID":string,
      /**  Active panel  */  
   "ActiveTab":string,
      /**  Can use Group By flag  */  
   "GroupOn":boolean,
      /**  Group by column  */  
   "GroupBy":string,
      /**  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  */  
   "SearchType":string,
      /**  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  */  
   "SearchUsing":string,
      /**  Column to sort by  */  
   "SortByColumn":string,
      /**  A for Ascending or D for Descending  */  
   "SortOrder":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_NamedSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Name of base search form  */  
   "SearchForm":string,
      /**  Named Search ID  */  
   "NSId":string,
      /**  User ID  */  
   "UserID":string,
      /**  UI from which the search is called from  */  
   "CalledFrom":string,
      /**  Default named search flag  */  
   "IsDefault":boolean,
      /**  Auto Execute flag  */  
   "AutoExecute":boolean,
      /**  Can unpin Criteria  */  
   "UnpinCrit":boolean,
      /**  Can be shared flag  */  
   "IsShared":boolean,
      /**  Share Type  */  
   "ShareType":string,
      /**  Return all rows flag.  */  
   "ReturnAll":boolean,
      /**  Maximum number search rows.  */  
   "MaxRows":number,
      /**  Auto select flag  */  
   "AutoSelect":boolean,
      /**  Value will be one of: "RowsDataSet" or "ListDataSet"  */  
   "DataSetMode":string,
      /**  Description  */  
   "Description":string,
      /**  "VN" = Vantage; "VS" = Vista  */  
   "ProductID":string,
      /**  Active panel  */  
   "ActiveTab":string,
      /**  Can use Group By flag  */  
   "GroupOn":boolean,
      /**  Group by column  */  
   "GroupBy":string,
      /**  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  */  
   "SearchType":string,
      /**  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  */  
   "SearchUsing":string,
      /**  Column to sort by  */  
   "SortByColumn":string,
      /**  A for Ascending or D for Descending  */  
   "SortOrder":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_WhereClauseRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Search Form  */  
   "SearchForm":string,
      /**  Namespace ID  */  
   "NSId":string,
      /**  User ID  */  
   "UserID":string,
      /**  Called From  */  
   "CalledFrom":string,
      /**  Table Name  */  
   "TableName":string,
   "WhereClause1":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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
      @param searchForm
      @param nsId
      @param userID
      @param calledFrom
   */  
export interface DeleteByID_input{
   searchForm:string,
   nsId:string,
   userID:string,
   calledFrom:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param searchForm
      @param nsId
      @param userID
      @param calledFrom
   */  
export interface GetByID_input{
   searchForm:string,
   nsId:string,
   userID:string,
   calledFrom:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_NamedSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_NamedSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_NamedSearchTableset[],
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
   returnObj:Ice_Tablesets_NamedSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param searchForm
      @param nsId
      @param userID
      @param calledFrom
   */  
export interface GetNewControlSetting_input{
   ds:Ice_Tablesets_NamedSearchTableset[],
   searchForm:string,
   nsId:string,
   userID:string,
   calledFrom:string,
}

export interface GetNewControlSetting_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_NamedSearchTableset,
}
}

   /** Required : 
      @param ds
      @param searchForm
      @param nsId
      @param userID
   */  
export interface GetNewNamedSearch_input{
   ds:Ice_Tablesets_NamedSearchTableset[],
   searchForm:string,
   nsId:string,
   userID:string,
}

export interface GetNewNamedSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_NamedSearchTableset,
}
}

   /** Required : 
      @param ds
      @param searchForm
      @param nsId
      @param userID
      @param calledFrom
   */  
export interface GetNewWhereClause_input{
   ds:Ice_Tablesets_NamedSearchTableset[],
   searchForm:string,
   nsId:string,
   userID:string,
   calledFrom:string,
}

export interface GetNewWhereClause_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_NamedSearchTableset,
}
}

   /** Required : 
      @param whereClauseNamedSearch
      @param whereClauseControlSetting
      @param whereClauseWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseNamedSearch:string,
   whereClauseControlSetting:string,
   whereClauseWhereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_NamedSearchTableset[],
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

export interface Ice_Tablesets_ControlSettingRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Search Form  */  
   SearchForm:string,
      /**  Namespace ID  */  
   NSId:string,
      /**  User ID  */  
   UserID:string,
      /**  Called From  */  
   CalledFrom:string,
      /**  Control GUID  */  
   ControlGuid:string,
      /**  Control Value  */  
   ControlValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EpBinding  */  
   EpBinding:string,
      /**  ComponentID  */  
   ComponentID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_NamedSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Name of base search form  */  
   SearchForm:string,
      /**  Named Search ID  */  
   NSId:string,
      /**  User ID  */  
   UserID:string,
      /**  UI from which the search is called from  */  
   CalledFrom:string,
      /**  Default named search flag  */  
   IsDefault:boolean,
      /**  Auto Execute flag  */  
   AutoExecute:boolean,
      /**  Can unpin Criteria  */  
   UnpinCrit:boolean,
      /**  Can be shared flag  */  
   IsShared:boolean,
      /**  Share Type  */  
   ShareType:string,
      /**  Return all rows flag.  */  
   ReturnAll:boolean,
      /**  Maximum number search rows.  */  
   MaxRows:number,
      /**  Auto select flag  */  
   AutoSelect:boolean,
      /**  Value will be one of: "RowsDataSet" or "ListDataSet"  */  
   DataSetMode:string,
      /**  Description  */  
   Description:string,
      /**  "VN" = Vantage; "VS" = Vista  */  
   ProductID:string,
      /**  Active panel  */  
   ActiveTab:string,
      /**  Can use Group By flag  */  
   GroupOn:boolean,
      /**  Group by column  */  
   GroupBy:string,
      /**  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  */  
   SearchType:string,
      /**  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  */  
   SearchUsing:string,
      /**  Column to sort by  */  
   SortByColumn:string,
      /**  A for Ascending or D for Descending  */  
   SortOrder:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_NamedSearchListTableset{
   NamedSearchList:Ice_Tablesets_NamedSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_NamedSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Name of base search form  */  
   SearchForm:string,
      /**  Named Search ID  */  
   NSId:string,
      /**  User ID  */  
   UserID:string,
      /**  UI from which the search is called from  */  
   CalledFrom:string,
      /**  Default named search flag  */  
   IsDefault:boolean,
      /**  Auto Execute flag  */  
   AutoExecute:boolean,
      /**  Can unpin Criteria  */  
   UnpinCrit:boolean,
      /**  Can be shared flag  */  
   IsShared:boolean,
      /**  Share Type  */  
   ShareType:string,
      /**  Return all rows flag.  */  
   ReturnAll:boolean,
      /**  Maximum number search rows.  */  
   MaxRows:number,
      /**  Auto select flag  */  
   AutoSelect:boolean,
      /**  Value will be one of: "RowsDataSet" or "ListDataSet"  */  
   DataSetMode:string,
      /**  Description  */  
   Description:string,
      /**  "VN" = Vantage; "VS" = Vista  */  
   ProductID:string,
      /**  Active panel  */  
   ActiveTab:string,
      /**  Can use Group By flag  */  
   GroupOn:boolean,
      /**  Group by column  */  
   GroupBy:string,
      /**  SearchType will hold one of two values initially but will be expanded in the future to offer other values.  This field is mandatory. Current values are Basic or BAQ.  */  
   SearchType:string,
      /**  SearchUsing will hold either null or the name of an existing BAQ.  In the future it may hold the name of an existing Dashboard.  */  
   SearchUsing:string,
      /**  Column to sort by  */  
   SortByColumn:string,
      /**  A for Ascending or D for Descending  */  
   SortOrder:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_NamedSearchTableset{
   NamedSearch:Ice_Tablesets_NamedSearchRow[],
   ControlSetting:Ice_Tablesets_ControlSettingRow[],
   WhereClause:Ice_Tablesets_WhereClauseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtNamedSearchTableset{
   NamedSearch:Ice_Tablesets_NamedSearchRow[],
   ControlSetting:Ice_Tablesets_ControlSettingRow[],
   WhereClause:Ice_Tablesets_WhereClauseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_WhereClauseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Search Form  */  
   SearchForm:string,
      /**  Namespace ID  */  
   NSId:string,
      /**  User ID  */  
   UserID:string,
      /**  Called From  */  
   CalledFrom:string,
      /**  Table Name  */  
   TableName:string,
      /**  Where Clause  */  
   WhereClause:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtNamedSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtNamedSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_NamedSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_NamedSearchTableset,
}
}

