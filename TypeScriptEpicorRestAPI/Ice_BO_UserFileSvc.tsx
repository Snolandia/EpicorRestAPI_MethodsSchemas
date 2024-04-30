import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.UserFileSvc
// Description: User File Definition
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/$metadata", {
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
   Description: Get UserFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserFiles
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserFileRow
   */  
export function get_UserFiles(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserFiles
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UserFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.UserFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserFiles(requestBody:Ice_Tablesets_UserFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles", {
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
   Summary: Calls GetByID to retrieve the UserFile item
   Description: Calls GetByID to retrieve the UserFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserFile
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.UserFileRow
   */  
export function get_UserFiles_UserID(UserID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UserFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")", {
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
         resolve(data as Ice_Tablesets_UserFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UserFile for the service
   Description: Calls UpdateExt to update UserFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserFile
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.UserFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserFiles_UserID(UserID:string, requestBody:Ice_Tablesets_UserFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")", {
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
   Summary: Call UpdateExt to delete UserFile item
   Description: Call UpdateExt to delete UserFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserFile
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserFiles_UserID(UserID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")", {
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
   Description: Get UserComps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UserComps1
      @param UserID Desc: UserID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompRow
   */  
export function get_UserFiles_UserID_UserComps(UserID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")/UserComps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the UserComp item
   Description: Calls GetByID to retrieve the UserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserComp1
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.UserCompRow
   */  
export function get_UserFiles_UserID_UserComps_UserID_Company(UserID:string, Company:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserFiles(" + UserID + ")/UserComps(" + UserID + "," + Company + ")", {
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
         resolve(data as Ice_Tablesets_UserCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get UserComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserComps
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompRow
   */  
export function get_UserComps(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserComps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.UserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserComps(requestBody:Ice_Tablesets_UserCompRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps", {
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
   Summary: Calls GetByID to retrieve the UserComp item
   Description: Calls GetByID to retrieve the UserComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserComp
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.UserCompRow
   */  
export function get_UserComps_UserID_Company(UserID:string, Company:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")", {
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
         resolve(data as Ice_Tablesets_UserCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UserComp for the service
   Description: Calls UpdateExt to update UserComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserComp
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.UserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserComps_UserID_Company(UserID:string, Company:string, requestBody:Ice_Tablesets_UserCompRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")", {
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
   Summary: Call UpdateExt to delete UserComp item
   Description: Call UpdateExt to delete UserComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserComp
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserComps_UserID_Company(UserID:string, Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")", {
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
   Description: Get UserCompExts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UserCompExts1
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompExtRow
   */  
export function get_UserComps_UserID_Company_UserCompExts(UserID:string, Company:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")/UserCompExts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompExtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the UserCompExt item
   Description: Calls GetByID to retrieve the UserCompExt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompExt1
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.UserCompExtRow
   */  
export function get_UserComps_UserID_Company_UserCompExts_UserID_Company_ExtCompID(UserID:string, Company:string, ExtCompID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserComps(" + UserID + "," + Company + ")/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")", {
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
         resolve(data as Ice_Tablesets_UserCompExtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get UserCompExts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserCompExts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserCompExtRow
   */  
export function get_UserCompExts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompExtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserCompExts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.UserCompExtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserCompExts(requestBody:Ice_Tablesets_UserCompExtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts", {
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
   Summary: Calls GetByID to retrieve the UserCompExt item
   Description: Calls GetByID to retrieve the UserCompExt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompExt
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.UserCompExtRow
   */  
export function get_UserCompExts_UserID_Company_ExtCompID(UserID:string, Company:string, ExtCompID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")", {
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
         resolve(data as Ice_Tablesets_UserCompExtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UserCompExt for the service
   Description: Calls UpdateExt to update UserCompExt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserCompExt
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.UserCompExtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserCompExts_UserID_Company_ExtCompID(UserID:string, Company:string, ExtCompID:string, requestBody:Ice_Tablesets_UserCompExtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")", {
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
   Summary: Call UpdateExt to delete UserCompExt item
   Description: Call UpdateExt to delete UserCompExt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserCompExt
      @param UserID Desc: UserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserCompExts_UserID_Company_ExtCompID(UserID:string, Company:string, ExtCompID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UserCompExts(" + UserID + "," + Company + "," + ExtCompID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UserFileListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileListRow)
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
export function get_GetRows(whereClauseUserFile:string, whereClauseUserComp:string, whereClauseUserCompExt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseUserFile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUserFile=" + whereClauseUserFile
   }
   if(typeof whereClauseUserComp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUserComp=" + whereClauseUserComp
   }
   if(typeof whereClauseUserCompExt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUserCompExt=" + whereClauseUserCompExt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetRows" + params, {
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
export function get_GetByID(userID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof userID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "userID=" + userID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetList" + params, {
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
   Summary: Invoke method AddUserCompany
   Description: This method will create a new row in the UserComp data table related to the given UserID.
   OperationID: AddUserCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddUserCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddUserCompany(requestBody:AddUserCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddUserCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/AddUserCompany", {
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
         resolve(data as AddUserCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePassword
   Description: Changes the specified user's password.
   OperationID: ChangePassword
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePassword(requestBody:ChangePassword_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePassword_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/ChangePassword", {
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
         resolve(data as ChangePassword_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckForCompany
   Description: This method is to be run when the user leaves the UserFile record. It will check to see that at least one
UserComp record exists. If not the user must add one before continuing on.
   OperationID: CheckForCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForCompany(requestBody:CheckForCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckForCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/CheckForCompany", {
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
         resolve(data as CheckForCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DetermineAccessibleInstallationsForUser
   Description: Determines the accessible installations for user.
   OperationID: DetermineAccessibleInstallationsForUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DetermineAccessibleInstallationsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetermineAccessibleInstallationsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DetermineAccessibleInstallationsForUser(requestBody:DetermineAccessibleInstallationsForUser_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DetermineAccessibleInstallationsForUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/DetermineAccessibleInstallationsForUser", {
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
         resolve(data as DetermineAccessibleInstallationsForUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUserFile
   Description: Uses the security credentials to retrieve the UserFile record
   OperationID: GetUserFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserFile(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUserFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetUserFile", {
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
         resolve(data as GetUserFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrentUserId
   Description: Uses the security credentials to retrieve the current ERP user Id
   OperationID: GetCurrentUserId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentUserId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentUserId(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrentUserId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetCurrentUserId", {
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
         resolve(data as GetCurrentUserId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExtCompanyList
   Description: Builds a list of the external companies for the specified company.
   OperationID: GetExtCompanyList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExtCompanyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExtCompanyList(requestBody:GetExtCompanyList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExtCompanyList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetExtCompanyList", {
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
         resolve(data as GetExtCompanyList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveSettings
   Description: Save user settings.
Unlike the Update method, there is no optimistic locking performed.
So the settings are saved in a last in wins basis.
   OperationID: SaveSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveSettings(requestBody:SaveSettings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/SaveSettings", {
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
         resolve(data as SaveSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsPasswordExpired
   Description: Check if password is expired.
   OperationID: IsPasswordExpired
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsPasswordExpired_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPasswordExpired_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsPasswordExpired(requestBody:IsPasswordExpired_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsPasswordExpired_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/IsPasswordExpired", {
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
         resolve(data as IsPasswordExpired_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePassword
   Description: Check if password is valid.
   OperationID: ValidatePassword
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePassword(requestBody:ValidatePassword_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePassword_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/ValidatePassword", {
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
         resolve(data as ValidatePassword_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsUserIDAvailable
   Description: Check if user can be created with this UserID. Available for security managers
   OperationID: IsUserIDAvailable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsUserIDAvailable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsUserIDAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsUserIDAvailable(requestBody:IsUserIDAvailable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsUserIDAvailable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/IsUserIDAvailable", {
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
         resolve(data as IsUserIDAvailable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExpireAllPasswords
   Description: Expire the passwords for all the users within the current tenant.
   OperationID: ExpireAllPasswords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExpireAllPasswords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireAllPasswords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpireAllPasswords(requestBody:ExpireAllPasswords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExpireAllPasswords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/ExpireAllPasswords", {
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
         resolve(data as ExpireAllPasswords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockAccount
   Description: Unlocks the account for the user
   OperationID: UnlockAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockAccount(requestBody:UnlockAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UnlockAccount", {
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
         resolve(data as UnlockAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AllowBlankPassword
   Description: Is a blank Password Allowed
   OperationID: AllowBlankPassword
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowBlankPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowBlankPassword(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AllowBlankPassword_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/AllowBlankPassword", {
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
         resolve(data as AllowBlankPassword_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AccountDisabled
   Description: Is a blank Password Allowed
   OperationID: AccountDisabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AccountDisabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AccountDisabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AccountDisabled(requestBody:AccountDisabled_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AccountDisabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/AccountDisabled", {
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
         resolve(data as AccountDisabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResetPassword
   Description: Allows a temp password to be set.
   OperationID: ResetPassword
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResetPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetPassword(requestBody:ResetPassword_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResetPassword_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/ResetPassword", {
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
         resolve(data as ResetPassword_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportUserToIdentityProvider
   Description: Sends user information to Identity Provider
   OperationID: ExportUserToIdentityProvider
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportUserToIdentityProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportUserToIdentityProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportUserToIdentityProvider(requestBody:ExportUserToIdentityProvider_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportUserToIdentityProvider_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/ExportUserToIdentityProvider", {
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
         resolve(data as ExportUserToIdentityProvider_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BulkUserExportToIdentityProvider
   Description: Bulk user export to Identity Provider
   OperationID: BulkUserExportToIdentityProvider
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BulkUserExportToIdentityProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkUserExportToIdentityProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BulkUserExportToIdentityProvider(requestBody:BulkUserExportToIdentityProvider_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BulkUserExportToIdentityProvider_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/BulkUserExportToIdentityProvider", {
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
         resolve(data as BulkUserExportToIdentityProvider_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListCompanyFilter
   Description: Returns a list of user filtered by Company
   OperationID: GetListCompanyFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListCompanyFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCompanyFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCompanyFilter(requestBody:GetListCompanyFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListCompanyFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetListCompanyFilter", {
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
         resolve(data as GetListCompanyFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompanyListForUser
   Description: Returns a list of the "visible" companies by the user (i.e. the companies in the same tenancy), or all if the user is a GSM.
   OperationID: GetCompanyListForUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCompanyListForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyListForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanyListForUser(requestBody:GetCompanyListForUser_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCompanyListForUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetCompanyListForUser", {
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
         resolve(data as GetCompanyListForUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailableCompanyListForUser
   Description: Returns a list of the "available" companies by the user (i.e. the companies in the same tenancy), or all if the user is a GSM.
   OperationID: GetAvailableCompanyListForUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailableCompanyListForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCompanyListForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableCompanyListForUser(requestBody:GetAvailableCompanyListForUser_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableCompanyListForUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetAvailableCompanyListForUser", {
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
         resolve(data as GetAvailableCompanyListForUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BackupIdentities
   Description: Backup user identity information to user data folder.
   OperationID: BackupIdentities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BackupIdentities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BackupIdentities(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BackupIdentities_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/BackupIdentities", {
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
         resolve(data as BackupIdentities_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RestoreIdentities
   Description: Restore user identity information from user data folder and update user files.
   OperationID: RestoreIdentities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreIdentities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RestoreIdentities(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RestoreIdentities_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/RestoreIdentities", {
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
         resolve(data as RestoreIdentities_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteTemporaryFile
   Description: Deletes temporary file after downloading
   OperationID: DeleteTemporaryFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTemporaryFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteTemporaryFile(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteTemporaryFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/DeleteTemporaryFile", {
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
         resolve(data as DeleteTemporaryFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrentInstallationId
   Description: Returns the InstallationId from SysCompany using the user's CurComp
   OperationID: GetCurrentInstallationId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCurrentInstallationId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentInstallationId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentInstallationId(requestBody:GetCurrentInstallationId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrentInstallationId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetCurrentInstallationId", {
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
         resolve(data as GetCurrentInstallationId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewUserFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewUserFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUserFile(requestBody:GetNewUserFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewUserFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetNewUserFile", {
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
         resolve(data as GetNewUserFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewUserComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserComp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewUserComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUserComp(requestBody:GetNewUserComp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewUserComp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetNewUserComp", {
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
         resolve(data as GetNewUserComp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewUserCompExt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserCompExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewUserCompExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserCompExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUserCompExt(requestBody:GetNewUserCompExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewUserCompExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetNewUserCompExt", {
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
         resolve(data as GetNewUserCompExt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.UserFileSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompExtRow{
   "odatametadata":string,
   "value":Ice_Tablesets_UserCompExtRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserCompRow{
   "odatametadata":string,
   "value":Ice_Tablesets_UserCompRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_UserFileListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UserFileRow{
   "odatametadata":string,
   "value":Ice_Tablesets_UserFileRow,
}

export interface Ice_Tablesets_UserCompExtRow{
      /**  UserID  */  
   "UserID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company ID  */  
   "ExtCompID":string,
      /**  Site Identifier.  */  
   "CurPlant":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_UserCompRow{
      /**  UserID  */  
   "UserID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   "Name":string,
      /**  Site Identifier.  */  
   "CurPlant":string,
      /**  List of Sites the user has access to.  */  
   "PlantList":string,
      /**  SolutionID  */  
   "SolutionID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the user can update expense entries (EmpExpense) for any employee.  */  
   "CanUpdateExpense":boolean,
      /**  Indicates if the user can update time entries (LaborDtl) for any employee.  */  
   "CanUpdateTime":boolean,
      /**  Employee ID  */  
   "EmpID":string,
      /**  Unique identifier of the Workstations  */  
   "WorkstationID":string,
   "BitFlag":number,
   "CompanyName":string,
   "UserIDName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_UserFileListRow{
      /**  User ID  */  
   "UserID":string,
      /**  User Name  */  
   "Name":string,
      /**  First address line  */  
   "Address1":string,
      /**  Second address line  */  
   "Address2":string,
      /**  City portion of the address  */  
   "City":string,
      /**  State portion of the address  */  
   "State":string,
      /**  Postal code or zip code portion of the address  */  
   "ZIP":string,
      /**  Country portion of the address  */  
   "Country":string,
      /**  Office phone number  */  
   "OfficePhone":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  User's email address.  */  
   "EMailAddress":string,
      /**  Indicates if the user account has been disabled (turned off).  */  
   "UserDisabled":boolean,
      /**  Indicates that the user account has security maintenance privileges.  */  
   "SecurityMgr":boolean,
      /**  Allow user to change save settings  */  
   "CanChangeSaveSettings":boolean,
      /**  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  */  
   "CurComp":string,
      /**  Date that the password was last changed.  */  
   "PwdLastChanged":string,
      /**  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  */  
   "PwdExpiresDays":number,
      /**  The date that the user account password expires.  */  
   "PwdExpires":string,
      /**  The number of remaining grace logins.  */  
   "PwdGrace":number,
      /**  List of security groups the user belongs to.  */  
   "GroupList":string,
      /**  List of companies the user has access to.  */  
   "CompList":string,
      /**  Enable Favorite Bar  */  
   "ViewFavoriteBar":boolean,
      /**  Enable Status Bar  */  
   "ViewStatusBar":boolean,
      /**  Sequence number of the folder in focus  */  
   "CurFolderSeq":number,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   "CurMenuID":string,
      /**  Indicates if the user wants tips to be displayed during logon.  */  
   "DispTips":boolean,
      /**  Whether the user can change their password.  */  
   "CanChangePassword":boolean,
      /**  Language ID  */  
   "LangNameID":string,
      /**  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  */  
   "LastGraphType":string,
      /**  Indicates that the internal web browser should be used instead of using the OS registered browser.  */  
   "UseInternalWebBrowser":boolean,
      /**  Allow user to start multiple sessions at the same time.  */  
   "AllowMultipleSessions":boolean,
      /**  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  */  
   "WebUser":boolean,
      /**  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  */  
   "ListViewMode":number,
      /**  Whether the user can add/maintain Dashboard Queries on the favorites bar.  */  
   "CanMaintainFavQueries":boolean,
      /**  Whether the user can add/maintain Dashboard URLs on the favorites bar.  */  
   "CanMaintainFavURLs":boolean,
      /**  Whether the user can add/maintain Windows Programs on the favorites bar.  */  
   "CanMaintainFavPrograms":boolean,
      /**  Whether the user can access customization screens.  */  
   "CanCustomize":boolean,
      /**  Whether to display the TreeView alone.  */  
   "ViewTreeOnly":number,
      /**  Time Out  */  
   "Timeout":number,
      /**  Whether the user can personalize.  */  
   "CanPersonalize":boolean,
      /**  Whether the user can translate.  */  
   "CanTranslate":boolean,
      /**  Can this user edit Company level Help Annotations  */  
   "CanEditCompAnnotations":boolean,
      /**  Can this user edit user level Help Annotations  */  
   "CanEditUserAnnotations":boolean,
      /**  Does this user get access to the HelpLink Editor  */  
   "CanEditHelpLinks":string,
      /**  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  */  
   "AutoStartMonitor":boolean,
      /**  How frequently (expressed as secounds) the Monitor will poll for results  */  
   "MonitorPollingInterval":number,
      /**  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  */  
   "FormOpenMode":string,
      /**  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  */  
   "EntConType":string,
      /**  Allow user to open dashboards in developer mode  */  
   "DashboardDeveloper":boolean,
      /**   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  */  
   "GlbCompSM":boolean,
      /**  LastLogOnAttempt  */  
   "LastLogOnAttempt":string,
      /**  ThemeID  */  
   "ThemeID":string,
      /**  DisableTheming  */  
   "DisableTheming":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ExternalIdentity  */  
   "ExternalIdentity":string,
      /**  SSRSReportDesigner  */  
   "SSRSReportDesigner":boolean,
      /**  RestrictIP  */  
   "RestrictIP":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_UserFileRow{
      /**  User ID  */  
   "UserID":string,
      /**  User Name  */  
   "Name":string,
      /**  First address line  */  
   "Address1":string,
      /**  Second address line  */  
   "Address2":string,
      /**  City portion of the address  */  
   "City":string,
      /**  State portion of the address  */  
   "State":string,
      /**  Postal code or zip code portion of the address  */  
   "ZIP":string,
      /**  Country portion of the address  */  
   "Country":string,
      /**  Office phone number  */  
   "OfficePhone":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  User's email address.  */  
   "EMailAddress":string,
      /**  Indicates if the user account has been disabled (turned off).  */  
   "UserDisabled":boolean,
      /**  Indicates that the user account has security maintenance privileges.  */  
   "SecurityMgr":boolean,
      /**  Allow user to change save settings  */  
   "CanChangeSaveSettings":boolean,
      /**  Save settings  */  
   "SaveSettings":boolean,
      /**  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  */  
   "CurComp":string,
      /**  Date that the password was last changed.  */  
   "PwdLastChanged":string,
      /**  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  */  
   "PwdExpiresDays":number,
      /**  The date that the user account password expires.  */  
   "PwdExpires":string,
      /**  The number of remaining grace logins.  */  
   "PwdGrace":number,
      /**  List of security groups the user belongs to.  */  
   "GroupList":string,
      /**  List of companies the user has access to.  */  
   "CompList":string,
      /**  Enable Favorite Bar  */  
   "ViewFavoriteBar":boolean,
      /**  Enable Status Bar  */  
   "ViewStatusBar":boolean,
      /**  Main menu X-position  */  
   "WinX":number,
      /**  Main menu Y-position  */  
   "WinY":number,
      /**  Sequence number of the folder in focus  */  
   "CurFolderSeq":number,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   "CurMenuID":string,
      /**  Main menu width  */  
   "WinWidth":number,
      /**  Main menu height  */  
   "WinHeight":number,
      /**  Indicates if the user wants tips to be displayed during logon.  */  
   "DispTips":boolean,
      /**  Whether the user can change their password.  */  
   "CanChangePassword":boolean,
      /**  Language ID  */  
   "LangNameID":string,
      /**  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  */  
   "LastGraphType":string,
      /**  Indicates that the internal web browser should be used instead of using the OS registered browser.  */  
   "UseInternalWebBrowser":boolean,
      /**  Allow user to start multiple sessions at the same time.  */  
   "AllowMultipleSessions":boolean,
      /**  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  */  
   "WebUser":boolean,
      /**  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  */  
   "ListViewMode":number,
      /**  Whether the user can add/maintain Dashboard Queries on the favorites bar.  */  
   "CanMaintainFavQueries":boolean,
      /**  Whether the user can add/maintain Dashboard URLs on the favorites bar.  */  
   "CanMaintainFavURLs":boolean,
      /**  Whether the user can add/maintain Windows Programs on the favorites bar.  */  
   "CanMaintainFavPrograms":boolean,
      /**  Whether the user can access customization screens.  */  
   "CanCustomize":boolean,
      /**  Whether to display the TreeView alone.  */  
   "ViewTreeOnly":number,
      /**  Time Out  */  
   "Timeout":number,
      /**  Whether the user can personalize.  */  
   "CanPersonalize":boolean,
      /**  Whether the user can translate.  */  
   "CanTranslate":boolean,
      /**  Can this user edit Company level Help Annotations  */  
   "CanEditCompAnnotations":boolean,
      /**  Can this user edit user level Help Annotations  */  
   "CanEditUserAnnotations":boolean,
      /**  Does this user get access to the HelpLink Editor  */  
   "CanEditHelpLinks":string,
      /**  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  */  
   "AutoStartMonitor":boolean,
      /**  How frequently (expressed as secounds) the Monitor will poll for results  */  
   "MonitorPollingInterval":number,
      /**  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  */  
   "FormOpenMode":string,
      /**  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  */  
   "EntConType":string,
      /**  Allow user to open dashboards in developer mode  */  
   "DashboardDeveloper":boolean,
      /**  Allow user to design quick searches  */  
   "CanDesignQSearch":boolean,
      /**   Whether single sign-on (SSO) is required to log on.
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Vantage. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Vantage using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Vantage icon; they will be taken directly to the application's main menu.  */  
   "RequireSso":boolean,
      /**  Show User ID in status panel  */  
   "ViewStatusPanelUserID":boolean,
      /**  Show language in status panel  */  
   "ViewStatusPanelLanguage":boolean,
      /**  Show current company in status panel  */  
   "ViewStatusPanelCompany":boolean,
      /**  Show current Site in status panel  */  
   "ViewStatusPanelPlant":boolean,
      /**  Show server name in status panel  */  
   "ViewStatusPanelServer":boolean,
      /**  Show workstation in status panel  */  
   "ViewStatusPanelWorkstationID":boolean,
      /**  Name of the operating system domain into which this users logs in.  Used when Require Single Sign on is enabled.  */  
   "DomainName":string,
      /**  Determines whether the user is allowed to use advanced development features of Business Process Management.  The freeform editor requires knowledge of Progress 4GL programming and specific method operational working.  Typically freeform options are used by Epicor custom programming or experienced programmers for advanced techniques not available through the wizard-like interface.  */  
   "BPMAdvancedUser":boolean,
      /**  Maximum number of favorite bar groups  */  
   "MaxGroupsFavorites":number,
      /**  Maximum number of system menus  */  
   "MaxGroupsSystemMenu":number,
      /**  Operating system user ID.  */  
   "OSUserID":string,
      /**  Allow user to create themes  */  
   "CanTheme":boolean,
      /**  Culture format  */  
   "FormatCulture":string,
      /**  yes = the user can use enterprise searches  */  
   "CanUseEntSearch":boolean,
      /**  Allow access to EWA  */  
   "CanAccEpiEverywhere":boolean,
      /**  Allow Acess to Mobile Office  */  
   "CanAcessMobile":boolean,
      /**  Initial start Menu for the Client  */  
   "StartMenuClient":string,
      /**  Initial Start Menu ID for EWA  */  
   "StartMenuEWA":string,
      /**  Initial Start Menu ID for Mobile  */  
   "StartMenuMobile":string,
      /**  Allow advanced BAQ designer rights  */  
   "AdvBAQRights":boolean,
      /**  Defines isthe uesr has Security Access Only  */  
   "SecurityAccessOnly":boolean,
      /**  Defines if is user can create a Solution using the Solution Manager  */  
   "SolutionMgrCreate":boolean,
      /**  Defines if a user can install Solutions using the Solution Manager  */  
   "SolutionMgrInstall":boolean,
      /**  Enterprise Search URL  */  
   "EntSearchURL":string,
      /**  Whether the user can add/maintain Quick Searches.  */  
   "CanMaintQuickSearch":boolean,
      /**  Use Default Enterprise Search  */  
   "UseDefaultEntSearch":boolean,
      /**  UserAccessOnly  */  
   "UserAccessOnly":boolean,
      /**   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  */  
   "GlbCompSM":boolean,
      /**  BAQXCompany  */  
   "BAQXCompany":boolean,
      /**  LastLogOnAttempt  */  
   "LastLogOnAttempt":string,
      /**  CanImpersonate  */  
   "CanImpersonate":boolean,
      /**  ViewStatusPanelSolutionID  */  
   "ViewStatusPanelSolutionID":boolean,
      /**  CanMaintPredictiveSearch  */  
   "CanMaintPredictiveSearch":boolean,
      /**  ThemeID  */  
   "ThemeID":string,
      /**  DisableTheming  */  
   "DisableTheming":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CanPublishLayout  */  
   "CanPublishLayout":boolean,
      /**  DefaultLayoutID  */  
   "DefaultLayoutID":string,
      /**  CanViewDocStar  */  
   "CanViewDocStar":boolean,
      /**  PwdChangeRequestOn  */  
   "PwdChangeRequestOn":string,
      /**  ExternalIdentity  */  
   "ExternalIdentity":string,
      /**  SSRSReportDesigner  */  
   "SSRSReportDesigner":boolean,
      /**  DefaultHomepageLayoutID  */  
   "DefaultHomepageLayoutID":string,
      /**  AccessScopeID  */  
   "AccessScopeID":string,
      /**  IoTUser  */  
   "IoTUser":boolean,
      /**  IoTAdministrator  */  
   "IoTAdministrator":boolean,
      /**  DMTUser  */  
   "DMTUser":boolean,
      /**  EVAUser  */  
   "EVAUser":boolean,
      /**  DefaultFormType  */  
   "DefaultFormType":string,
      /**  HideKineticToast  */  
   "HideKineticToast":boolean,
      /**  RestrictIP  */  
   "RestrictIP":boolean,
      /**  flag to indicate Advanced Configurator User  */  
   "AdvancedConfiguratorUser":boolean,
   "CanOverrideAllocPart":boolean,
      /**  If yes, the user will be able to enter a blank password and still get the prompt for new password.  */  
   "ClearPassword":boolean,
      /**  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  */  
   "ExpirePassword":boolean,
   "FailedAttempts":number,
   "IntegrationAccount":boolean,
   "LockedOut":boolean,
   "LockedOutUntil":string,
      /**  set passwrod to blank  */  
   "PasswordBlank":boolean,
      /**  Email to send new password to  */  
   "PasswordEmail":string,
      /**  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  */  
   "ShpTrackerIntMinute":number,
      /**  Update Warning Message  */  
   "UpdateWarning":string,
   "UseCompression":boolean,
      /**  Whether the user can be referenced as the requestor on a PO Requisition.  */  
   "AllowReq":boolean,
   "LangNameIDDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
   "Character01":string,
   "UD_SysRevID":string,
   "SendSaaSAlert_c":boolean,
   "TempEpiSupportUser_c":boolean,
   "EpicUpgrade_c":boolean,
   "DisableDate_c":string,
   "DisabledDate_c":string,
   "Checkbox20":boolean,
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
      @param userID
   */  
export interface AccountDisabled_input{
   userID:string,
}

export interface AccountDisabled_output{
      /**  `true` if blank password allowed.  */  
   returnObj:boolean,
}

   /** Required : 
      @param userID
      @param data
   */  
export interface AddUserCompany_input{
      /**  The user ID for which a company will be added.  */  
   userID:string,
   data:Ice_Tablesets_UserFileTableset[],
}

export interface AddUserCompany_output{
parameters : {
      /**  output parameters  */  
   data:Ice_Tablesets_UserFileTableset,
}
}

export interface AllowBlankPassword_output{
      /**  `true` if blank password allowed.  */  
   returnObj:boolean,
}

export interface BackupIdentities_output{
}

   /** Required : 
      @param users
   */  
export interface BulkUserExportToIdentityProvider_input{
      /**  List of User ID  */  
   users:string,
}

export interface BulkUserExportToIdentityProvider_output{
      /**  Dictionary of errors during export. Key - userID, value - error message  */  
   returnObj:System_Collections_Generic_KeyValuePair_System_String_System_String[],
}

   /** Required : 
      @param userID
      @param currentPassword
      @param newPassword
   */  
export interface ChangePassword_input{
      /**  The user identifier.  */  
   userID:string,
      /**  The current password.  */  
   currentPassword:string,
      /**  The new password.  */  
   newPassword:string,
}

export interface ChangePassword_output{
}

   /** Required : 
      @param userID
   */  
export interface CheckForCompany_input{
      /**  The user identifier.  */  
   userID:string,
}

export interface CheckForCompany_output{
}

   /** Required : 
      @param userID
   */  
export interface DeleteByID_input{
   userID:string,
}

export interface DeleteByID_output{
}

export interface DeleteTemporaryFile_output{
}

   /** Required : 
      @param userID
   */  
export interface DetermineAccessibleInstallationsForUser_input{
      /**  The user identifier.  */  
   userID:string,
}

export interface DetermineAccessibleInstallationsForUser_output{
      /**  The list of installations that the user has access to.  */  
   returnObj:string,
}

   /** Required : 
      @param blankPasswordsOnly
      @param disableAccount
   */  
export interface ExpireAllPasswords_input{
   blankPasswordsOnly:boolean,
   disableAccount:boolean,
}

export interface ExpireAllPasswords_output{
}

   /** Required : 
      @param userID
   */  
export interface ExportUserToIdentityProvider_input{
      /**  User ID to export  */  
   userID:string,
}

export interface ExportUserToIdentityProvider_output{
}

   /** Required : 
      @param userID
   */  
export interface GetAvailableCompanyListForUser_input{
   userID:string,
}

export interface GetAvailableCompanyListForUser_output{
   returnObj:Ice_Tablesets_CompanyListTableset[],
}

   /** Required : 
      @param userID
   */  
export interface GetByID_input{
   userID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_UserFileTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_UserFileTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_UserFileTableset[],
}

   /** Required : 
      @param userID
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetCompanyListForUser_input{
      /**  User ID.  */  
   userID:string,
      /**  where clause to apply.  */  
   whereClause:string,
      /**  page size.  */  
   pageSize:number,
      /**  absolute page.  */  
   absolutePage:number,
}

export interface GetCompanyListForUser_output{
   returnObj:Ice_Tablesets_CompanyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param userID
   */  
export interface GetCurrentInstallationId_input{
   userID:string,
}

export interface GetCurrentInstallationId_output{
   returnObj:string,
}

export interface GetCurrentUserId_output{
      /**  User Id record of the logged in user  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
   */  
export interface GetExtCompanyList_input{
      /**  Authorized Company  */  
   companyID:string,
}

export interface GetExtCompanyList_output{
parameters : {
      /**  output parameters  */  
   externalCompanyList:string,
}
}

   /** Required : 
      @param whereClause
      @param CompList
      @param pageSize
      @param absolutePage
   */  
export interface GetListCompanyFilter_input{
   whereClause:string,
      /**  company to filter on  */  
   CompList:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListCompanyFilter_output{
   returnObj:Ice_Tablesets_UserFileListTableset[],
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
   returnObj:Ice_Tablesets_UserFileListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param userID
      @param company
   */  
export interface GetNewUserCompExt_input{
   ds:Ice_Tablesets_UserFileTableset[],
   userID:string,
   company:string,
}

export interface GetNewUserCompExt_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param ds
      @param userID
   */  
export interface GetNewUserComp_input{
   ds:Ice_Tablesets_UserFileTableset[],
   userID:string,
}

export interface GetNewUserComp_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewUserFile_input{
   ds:Ice_Tablesets_UserFileTableset[],
}

export interface GetNewUserFile_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param whereClauseUserFile
      @param whereClauseUserComp
      @param whereClauseUserCompExt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseUserFile:string,
   whereClauseUserComp:string,
   whereClauseUserCompExt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_UserFileTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetUserFile_output{
   returnObj:Ice_Tablesets_UserFileTableset[],
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
   Company:string,
   Name:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_Tablesets_CompanyListTableset{
   CompanyList:Ice_Tablesets_CompanyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtUserFileTableset{
   UserFile:Ice_Tablesets_UserFileRow[],
   UserComp:Ice_Tablesets_UserCompRow[],
   UserCompExt:Ice_Tablesets_UserCompExtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UserCompExtRow{
      /**  UserID  */  
   UserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company ID  */  
   ExtCompID:string,
      /**  Site Identifier.  */  
   CurPlant:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UserCompRow{
      /**  UserID  */  
   UserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   Name:string,
      /**  Site Identifier.  */  
   CurPlant:string,
      /**  List of Sites the user has access to.  */  
   PlantList:string,
      /**  SolutionID  */  
   SolutionID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the user can update expense entries (EmpExpense) for any employee.  */  
   CanUpdateExpense:boolean,
      /**  Indicates if the user can update time entries (LaborDtl) for any employee.  */  
   CanUpdateTime:boolean,
      /**  Employee ID  */  
   EmpID:string,
      /**  Unique identifier of the Workstations  */  
   WorkstationID:string,
   BitFlag:number,
   CompanyName:string,
   UserIDName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UserFileListRow{
      /**  User ID  */  
   UserID:string,
      /**  User Name  */  
   Name:string,
      /**  First address line  */  
   Address1:string,
      /**  Second address line  */  
   Address2:string,
      /**  City portion of the address  */  
   City:string,
      /**  State portion of the address  */  
   State:string,
      /**  Postal code or zip code portion of the address  */  
   ZIP:string,
      /**  Country portion of the address  */  
   Country:string,
      /**  Office phone number  */  
   OfficePhone:string,
      /**  Home phone number  */  
   Phone:string,
      /**  User's email address.  */  
   EMailAddress:string,
      /**  Indicates if the user account has been disabled (turned off).  */  
   UserDisabled:boolean,
      /**  Indicates that the user account has security maintenance privileges.  */  
   SecurityMgr:boolean,
      /**  Allow user to change save settings  */  
   CanChangeSaveSettings:boolean,
      /**  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  */  
   CurComp:string,
      /**  Date that the password was last changed.  */  
   PwdLastChanged:string,
      /**  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  */  
   PwdExpiresDays:number,
      /**  The date that the user account password expires.  */  
   PwdExpires:string,
      /**  The number of remaining grace logins.  */  
   PwdGrace:number,
      /**  List of security groups the user belongs to.  */  
   GroupList:string,
      /**  List of companies the user has access to.  */  
   CompList:string,
      /**  Enable Favorite Bar  */  
   ViewFavoriteBar:boolean,
      /**  Enable Status Bar  */  
   ViewStatusBar:boolean,
      /**  Sequence number of the folder in focus  */  
   CurFolderSeq:number,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   CurMenuID:string,
      /**  Indicates if the user wants tips to be displayed during logon.  */  
   DispTips:boolean,
      /**  Whether the user can change their password.  */  
   CanChangePassword:boolean,
      /**  Language ID  */  
   LangNameID:string,
      /**  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  */  
   LastGraphType:string,
      /**  Indicates that the internal web browser should be used instead of using the OS registered browser.  */  
   UseInternalWebBrowser:boolean,
      /**  Allow user to start multiple sessions at the same time.  */  
   AllowMultipleSessions:boolean,
      /**  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  */  
   WebUser:boolean,
      /**  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  */  
   ListViewMode:number,
      /**  Whether the user can add/maintain Dashboard Queries on the favorites bar.  */  
   CanMaintainFavQueries:boolean,
      /**  Whether the user can add/maintain Dashboard URLs on the favorites bar.  */  
   CanMaintainFavURLs:boolean,
      /**  Whether the user can add/maintain Windows Programs on the favorites bar.  */  
   CanMaintainFavPrograms:boolean,
      /**  Whether the user can access customization screens.  */  
   CanCustomize:boolean,
      /**  Whether to display the TreeView alone.  */  
   ViewTreeOnly:number,
      /**  Time Out  */  
   Timeout:number,
      /**  Whether the user can personalize.  */  
   CanPersonalize:boolean,
      /**  Whether the user can translate.  */  
   CanTranslate:boolean,
      /**  Can this user edit Company level Help Annotations  */  
   CanEditCompAnnotations:boolean,
      /**  Can this user edit user level Help Annotations  */  
   CanEditUserAnnotations:boolean,
      /**  Does this user get access to the HelpLink Editor  */  
   CanEditHelpLinks:string,
      /**  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  */  
   AutoStartMonitor:boolean,
      /**  How frequently (expressed as secounds) the Monitor will poll for results  */  
   MonitorPollingInterval:number,
      /**  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  */  
   FormOpenMode:string,
      /**  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  */  
   EntConType:string,
      /**  Allow user to open dashboards in developer mode  */  
   DashboardDeveloper:boolean,
      /**   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  */  
   GlbCompSM:boolean,
      /**  LastLogOnAttempt  */  
   LastLogOnAttempt:string,
      /**  ThemeID  */  
   ThemeID:string,
      /**  DisableTheming  */  
   DisableTheming:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExternalIdentity  */  
   ExternalIdentity:string,
      /**  SSRSReportDesigner  */  
   SSRSReportDesigner:boolean,
      /**  RestrictIP  */  
   RestrictIP:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UserFileListTableset{
   UserFileList:Ice_Tablesets_UserFileListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UserFileRow{
      /**  User ID  */  
   UserID:string,
      /**  User Name  */  
   Name:string,
      /**  First address line  */  
   Address1:string,
      /**  Second address line  */  
   Address2:string,
      /**  City portion of the address  */  
   City:string,
      /**  State portion of the address  */  
   State:string,
      /**  Postal code or zip code portion of the address  */  
   ZIP:string,
      /**  Country portion of the address  */  
   Country:string,
      /**  Office phone number  */  
   OfficePhone:string,
      /**  Home phone number  */  
   Phone:string,
      /**  User's email address.  */  
   EMailAddress:string,
      /**  Indicates if the user account has been disabled (turned off).  */  
   UserDisabled:boolean,
      /**  Indicates that the user account has security maintenance privileges.  */  
   SecurityMgr:boolean,
      /**  Allow user to change save settings  */  
   CanChangeSaveSettings:boolean,
      /**  Save settings  */  
   SaveSettings:boolean,
      /**  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  */  
   CurComp:string,
      /**  Date that the password was last changed.  */  
   PwdLastChanged:string,
      /**  Password expires x days after the password has been changed.  Zero means the password does not automatically expire.  */  
   PwdExpiresDays:number,
      /**  The date that the user account password expires.  */  
   PwdExpires:string,
      /**  The number of remaining grace logins.  */  
   PwdGrace:number,
      /**  List of security groups the user belongs to.  */  
   GroupList:string,
      /**  List of companies the user has access to.  */  
   CompList:string,
      /**  Enable Favorite Bar  */  
   ViewFavoriteBar:boolean,
      /**  Enable Status Bar  */  
   ViewStatusBar:boolean,
      /**  Main menu X-position  */  
   WinX:number,
      /**  Main menu Y-position  */  
   WinY:number,
      /**  Sequence number of the folder in focus  */  
   CurFolderSeq:number,
      /**  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  */  
   CurMenuID:string,
      /**  Main menu width  */  
   WinWidth:number,
      /**  Main menu height  */  
   WinHeight:number,
      /**  Indicates if the user wants tips to be displayed during logon.  */  
   DispTips:boolean,
      /**  Whether the user can change their password.  */  
   CanChangePassword:boolean,
      /**  Language ID  */  
   LangNameID:string,
      /**  The last type of Graph (Bar, 3D Bar, Line, etc.) used in the Schedule Load Graph program.  */  
   LastGraphType:string,
      /**  Indicates that the internal web browser should be used instead of using the OS registered browser.  */  
   UseInternalWebBrowser:boolean,
      /**  Allow user to start multiple sessions at the same time.  */  
   AllowMultipleSessions:boolean,
      /**  Indicates that the user has Web interface privileges.  When this is turned on, the write trigger maintains certain fields in the WebUser table.  If this is never turned on, a corresponding WebUser doesn't exist.  If this has been on, and is now turned off, the WebUser record is set to disabled, but not deleted.  */  
   WebUser:boolean,
      /**  This property determines the viewing mode of the ListView object. The ListView object supports viewing items in four different modes: Icon(0),SmallIcon(1), List(2) and Report(3). Only 0 1 and 3 are used  */  
   ListViewMode:number,
      /**  Whether the user can add/maintain Dashboard Queries on the favorites bar.  */  
   CanMaintainFavQueries:boolean,
      /**  Whether the user can add/maintain Dashboard URLs on the favorites bar.  */  
   CanMaintainFavURLs:boolean,
      /**  Whether the user can add/maintain Windows Programs on the favorites bar.  */  
   CanMaintainFavPrograms:boolean,
      /**  Whether the user can access customization screens.  */  
   CanCustomize:boolean,
      /**  Whether to display the TreeView alone.  */  
   ViewTreeOnly:number,
      /**  Time Out  */  
   Timeout:number,
      /**  Whether the user can personalize.  */  
   CanPersonalize:boolean,
      /**  Whether the user can translate.  */  
   CanTranslate:boolean,
      /**  Can this user edit Company level Help Annotations  */  
   CanEditCompAnnotations:boolean,
      /**  Can this user edit user level Help Annotations  */  
   CanEditUserAnnotations:boolean,
      /**  Does this user get access to the HelpLink Editor  */  
   CanEditHelpLinks:string,
      /**  Does this user want the Monitor to Started when they log in. (replaces Config Setting)  */  
   AutoStartMonitor:boolean,
      /**  How frequently (expressed as secounds) the Monitor will poll for results  */  
   MonitorPollingInterval:number,
      /**  Default form open behavior (Nil, Auto'S'earch, Auto'P'opulate) -  (Replaces Config Setting)  */  
   FormOpenMode:string,
      /**  Enterprise Connection Type, Determines how the UI Behaves when Session information is changed and UI forms are already present (Nil, 'S'ingleSession, 'M'ultiSession) (Replaces Config Setting)  */  
   EntConType:string,
      /**  Allow user to open dashboards in developer mode  */  
   DashboardDeveloper:boolean,
      /**  Allow user to design quick searches  */  
   CanDesignQSearch:boolean,
      /**   Whether single sign-on (SSO) is required to log on.
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Vantage. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Vantage using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Vantage icon; they will be taken directly to the application's main menu.  */  
   RequireSso:boolean,
      /**  Show User ID in status panel  */  
   ViewStatusPanelUserID:boolean,
      /**  Show language in status panel  */  
   ViewStatusPanelLanguage:boolean,
      /**  Show current company in status panel  */  
   ViewStatusPanelCompany:boolean,
      /**  Show current Site in status panel  */  
   ViewStatusPanelPlant:boolean,
      /**  Show server name in status panel  */  
   ViewStatusPanelServer:boolean,
      /**  Show workstation in status panel  */  
   ViewStatusPanelWorkstationID:boolean,
      /**  Name of the operating system domain into which this users logs in.  Used when Require Single Sign on is enabled.  */  
   DomainName:string,
      /**  Determines whether the user is allowed to use advanced development features of Business Process Management.  The freeform editor requires knowledge of Progress 4GL programming and specific method operational working.  Typically freeform options are used by Epicor custom programming or experienced programmers for advanced techniques not available through the wizard-like interface.  */  
   BPMAdvancedUser:boolean,
      /**  Maximum number of favorite bar groups  */  
   MaxGroupsFavorites:number,
      /**  Maximum number of system menus  */  
   MaxGroupsSystemMenu:number,
      /**  Operating system user ID.  */  
   OSUserID:string,
      /**  Allow user to create themes  */  
   CanTheme:boolean,
      /**  Culture format  */  
   FormatCulture:string,
      /**  yes = the user can use enterprise searches  */  
   CanUseEntSearch:boolean,
      /**  Allow access to EWA  */  
   CanAccEpiEverywhere:boolean,
      /**  Allow Acess to Mobile Office  */  
   CanAcessMobile:boolean,
      /**  Initial start Menu for the Client  */  
   StartMenuClient:string,
      /**  Initial Start Menu ID for EWA  */  
   StartMenuEWA:string,
      /**  Initial Start Menu ID for Mobile  */  
   StartMenuMobile:string,
      /**  Allow advanced BAQ designer rights  */  
   AdvBAQRights:boolean,
      /**  Defines isthe uesr has Security Access Only  */  
   SecurityAccessOnly:boolean,
      /**  Defines if is user can create a Solution using the Solution Manager  */  
   SolutionMgrCreate:boolean,
      /**  Defines if a user can install Solutions using the Solution Manager  */  
   SolutionMgrInstall:boolean,
      /**  Enterprise Search URL  */  
   EntSearchURL:string,
      /**  Whether the user can add/maintain Quick Searches.  */  
   CanMaintQuickSearch:boolean,
      /**  Use Default Enterprise Search  */  
   UseDefaultEntSearch:boolean,
      /**  UserAccessOnly  */  
   UserAccessOnly:boolean,
      /**   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  */  
   GlbCompSM:boolean,
      /**  BAQXCompany  */  
   BAQXCompany:boolean,
      /**  LastLogOnAttempt  */  
   LastLogOnAttempt:string,
      /**  CanImpersonate  */  
   CanImpersonate:boolean,
      /**  ViewStatusPanelSolutionID  */  
   ViewStatusPanelSolutionID:boolean,
      /**  CanMaintPredictiveSearch  */  
   CanMaintPredictiveSearch:boolean,
      /**  ThemeID  */  
   ThemeID:string,
      /**  DisableTheming  */  
   DisableTheming:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CanPublishLayout  */  
   CanPublishLayout:boolean,
      /**  DefaultLayoutID  */  
   DefaultLayoutID:string,
      /**  CanViewDocStar  */  
   CanViewDocStar:boolean,
      /**  PwdChangeRequestOn  */  
   PwdChangeRequestOn:string,
      /**  ExternalIdentity  */  
   ExternalIdentity:string,
      /**  SSRSReportDesigner  */  
   SSRSReportDesigner:boolean,
      /**  DefaultHomepageLayoutID  */  
   DefaultHomepageLayoutID:string,
      /**  AccessScopeID  */  
   AccessScopeID:string,
      /**  IoTUser  */  
   IoTUser:boolean,
      /**  IoTAdministrator  */  
   IoTAdministrator:boolean,
      /**  DMTUser  */  
   DMTUser:boolean,
      /**  EVAUser  */  
   EVAUser:boolean,
      /**  DefaultFormType  */  
   DefaultFormType:string,
      /**  HideKineticToast  */  
   HideKineticToast:boolean,
      /**  RestrictIP  */  
   RestrictIP:boolean,
      /**  flag to indicate Advanced Configurator User  */  
   AdvancedConfiguratorUser:boolean,
   CanOverrideAllocPart:boolean,
      /**  If yes, the user will be able to enter a blank password and still get the prompt for new password.  */  
   ClearPassword:boolean,
      /**  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  */  
   ExpirePassword:boolean,
   FailedAttempts:number,
   IntegrationAccount:boolean,
   LockedOut:boolean,
   LockedOutUntil:string,
      /**  set passwrod to blank  */  
   PasswordBlank:boolean,
      /**  Email to send new password to  */  
   PasswordEmail:string,
      /**  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  */  
   ShpTrackerIntMinute:number,
      /**  Update Warning Message  */  
   UpdateWarning:string,
   UseCompression:boolean,
      /**  Whether the user can be referenced as the requestor on a PO Requisition.  */  
   AllowReq:boolean,
   LangNameIDDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
   Character01:string,
   UD_SysRevID:string,
   SendSaaSAlert_c:boolean,
   TempEpiSupportUser_c:boolean,
   EpicUpgrade_c:boolean,
   DisableDate_c:string,
   DisabledDate_c:string,
   Checkbox20:boolean,
}

export interface Ice_Tablesets_UserFileTableset{
   UserFile:Ice_Tablesets_UserFileRow[],
   UserComp:Ice_Tablesets_UserCompRow[],
   UserCompExt:Ice_Tablesets_UserCompExtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param userID
   */  
export interface IsPasswordExpired_input{
      /**  The user identifier.  */  
   userID:string,
}

export interface IsPasswordExpired_output{
      /**  `true` if the password has expired or not set.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   graceCount:number,
}
}

   /** Required : 
      @param userID
   */  
export interface IsUserIDAvailable_input{
   userID:string,
}

export interface IsUserIDAvailable_output{
   returnObj:boolean,
}

   /** Required : 
      @param userID
      @param setToBlank
      @param email
   */  
export interface ResetPassword_input{
      /**  UserID to change password on.  */  
   userID:string,
      /**  Set to a blank password.  */  
   setToBlank:boolean,
      /**  Email to send new password to.  */  
   email:string,
}

export interface ResetPassword_output{
}

export interface RestoreIdentities_output{
      /**  The results of the process.  */  
   returnObj:string,
}

   /** Required : 
      @param userID
      @param saveSettings
      @param currentCompany
      @param viewFavoriteBar
      @param viewFullTree
      @param viewStatusBar
      @param viewStatusPanelCompany
      @param viewStatusPanelLanguage
      @param viewStatusPanelPlant
      @param viewStatusPanelServer
      @param viewStatusPanelUserID
      @param viewStatusPanelWorkstationID
      @param viewStatusPanelSolutionID
      @param winX
      @param winY
      @param winWidth
      @param winHeight
      @param listViewMode
      @param currentMenuID
      @param plantID
      @param workstationID
      @param currentFolderSequence
      @param maxGroupsFavorites
      @param maxGroupsSystemMenu
      @param themeID
      @param disableTheming
      @param defaultFormType
   */  
export interface SaveSettings_input{
      /**  The user identifier.  */  
   userID:string,
      /**  If set to `true` settings are saved.  */  
   saveSettings:boolean,
      /**  The current company.  */  
   currentCompany:string,
      /**  If set to `true` then favorite bar is visible.  */  
   viewFavoriteBar:boolean,
      /**  If set to `true` then the full tree is visible.  */  
   viewFullTree:boolean,
      /**  If set to `true` then the status bar is visible.  */  
   viewStatusBar:boolean,
      /**  If set to `true` then the status panel company is visible.  */  
   viewStatusPanelCompany:boolean,
      /**  If set to `true` then the status panel language is visible.  */  
   viewStatusPanelLanguage:boolean,
      /**  If set to `true` then the status panel plant is visible.  */  
   viewStatusPanelPlant:boolean,
      /**  If set to `true` then the status panel server is visible.  */  
   viewStatusPanelServer:boolean,
      /**  If set to `true` then the status panel user identifier is visible.  */  
   viewStatusPanelUserID:boolean,
      /**  If set to `true` then the status panel workstation identifier is visible.  */  
   viewStatusPanelWorkstationID:boolean,
      /**  If set to `true` then the status panel workstation identifier is visible.  */  
   viewStatusPanelSolutionID:boolean,
      /**  The main window X co-ordinate.  */  
   winX:number,
      /**  The main window Y co-ordinate.  */  
   winY:number,
      /**  Width of the main window.  */  
   winWidth:number,
      /**  Height of the main window.  */  
   winHeight:number,
      /**  The list view mode.  */  
   listViewMode:number,
      /**  The current menu identifier.  */  
   currentMenuID:string,
      /**  The plant identifier.  */  
   plantID:string,
      /**  The workstation identifier.  */  
   workstationID:string,
      /**  The current folder sequence.  */  
   currentFolderSequence:number,
      /**  The max groups favorites.  */  
   maxGroupsFavorites:number,
      /**  The max groups system menu.  */  
   maxGroupsSystemMenu:number,
      /**  Theme to be used for this user  */  
   themeID:string,
      /**  Disable theming for this user  */  
   disableTheming:boolean,
      /**  The default form type the user prefers - WinForm or WebBridge.  */  
   defaultFormType:string,
}

export interface SaveSettings_output{
}

export interface System_Collections_Generic_KeyValuePair_System_String_System_String{
   Key:string,
   Value:string,
}

   /** Required : 
      @param userID
   */  
export interface UnlockAccount_input{
   userID:string,
}

export interface UnlockAccount_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtUserFileTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtUserFileTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_UserFileTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param userID
      @param password
   */  
export interface ValidatePassword_input{
      /**  The user identifier.  */  
   userID:string,
      /**  The user's password.  */  
   password:string,
}

export interface ValidatePassword_output{
      /**  `true` if the password is valid.  */  
   returnObj:boolean,
}

