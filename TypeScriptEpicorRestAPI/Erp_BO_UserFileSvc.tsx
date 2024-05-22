import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.UserFileSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/$metadata", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserFileRow
   */  
export function get_UserFiles(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileRow)
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
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.UserFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserFiles(requestBody:Erp_Tablesets_UserFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.UserFileRow
   */  
export function get_UserFiles_DcdUserID(DcdUserID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UserFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")", {
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
         resolve(data as Erp_Tablesets_UserFileRow)
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserFiles_DcdUserID(DcdUserID:string, requestBody:Erp_Tablesets_UserFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserFiles_DcdUserID(DcdUserID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompRow
   */  
export function get_UserFiles_DcdUserID_UserComps(DcdUserID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")/UserComps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow)
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.UserCompRow
   */  
export function get_UserFiles_DcdUserID_UserComps_DcdUserID_Company(DcdUserID:string, Company:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserFiles(" + DcdUserID + ")/UserComps(" + DcdUserID + "," + Company + ")", {
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
         resolve(data as Erp_Tablesets_UserCompRow)
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompRow
   */  
export function get_UserComps(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow)
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
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.UserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserComps(requestBody:Erp_Tablesets_UserCompRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.UserCompRow
   */  
export function get_UserComps_DcdUserID_Company(DcdUserID:string, Company:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")", {
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
         resolve(data as Erp_Tablesets_UserCompRow)
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserComps_DcdUserID_Company(DcdUserID:string, Company:string, requestBody:Erp_Tablesets_UserCompRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserComps_DcdUserID_Company(DcdUserID:string, Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompExtRow
   */  
export function get_UserComps_DcdUserID_Company_UserCompExts(DcdUserID:string, Company:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")/UserCompExts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompExtRow)
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.UserCompExtRow
   */  
export function get_UserComps_DcdUserID_Company_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID:string, Company:string, ExtCompID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserComps(" + DcdUserID + "," + Company + ")/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")", {
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
         resolve(data as Erp_Tablesets_UserCompExtRow)
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompExtRow
   */  
export function get_UserCompExts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompExtRow)
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
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.UserCompExtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserCompExts(requestBody:Erp_Tablesets_UserCompExtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.UserCompExtRow
   */  
export function get_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID:string, Company:string, ExtCompID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UserCompExtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")", {
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
         resolve(data as Erp_Tablesets_UserCompExtRow)
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserCompExtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID:string, Company:string, ExtCompID:string, requestBody:Erp_Tablesets_UserCompExtRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")", {
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
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompID Desc: ExtCompID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserCompExts_DcdUserID_Company_ExtCompID(DcdUserID:string, Company:string, ExtCompID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UserCompExts(" + DcdUserID + "," + Company + "," + ExtCompID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserFileListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileListRow)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetRows" + params, {
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
export function get_GetByID(dcdUserID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof dcdUserID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dcdUserID=" + dcdUserID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetByID" + params, {
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
   Summary: Invoke method GetRowsFromList
   Description: Get rows from list dataset
   OperationID: GetRowsFromList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromList(requestBody:GetRowsFromList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsFromList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetRowsFromList", {
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
         resolve(data as GetRowsFromList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPayrollRights
   Description: Method to call to determine if the user has payroll manager rights
   OperationID: CheckPayrollRights
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPayrollRights_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPayrollRights(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPayrollRights_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/CheckPayrollRights", {
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
         resolve(data as CheckPayrollRights_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAdvancedConfiguratorUser
   Description: Method to call to determine if the user has Advanced Configurator User Rights
   OperationID: CheckAdvancedConfiguratorUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAdvancedConfiguratorUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAdvancedConfiguratorUser(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAdvancedConfiguratorUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/CheckAdvancedConfiguratorUser", {
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
         resolve(data as CheckAdvancedConfiguratorUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUserTimeExpenseRetrieveOptions
   Description: Returns the Time/Expense retrieve options for the current user
   OperationID: GetUserTimeExpenseRetrieveOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserTimeExpenseRetrieveOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserTimeExpenseRetrieveOptions(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUserTimeExpenseRetrieveOptions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetUserTimeExpenseRetrieveOptions", {
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
         resolve(data as GetUserTimeExpenseRetrieveOptions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUserTimeExpenseRetrieveOptions
   Description: Sets the Time/Expense retrieve options for the current user
   OperationID: SetUserTimeExpenseRetrieveOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetUserTimeExpenseRetrieveOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUserTimeExpenseRetrieveOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUserTimeExpenseRetrieveOptions(requestBody:SetUserTimeExpenseRetrieveOptions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetUserTimeExpenseRetrieveOptions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/SetUserTimeExpenseRetrieveOptions", {
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
         resolve(data as SetUserTimeExpenseRetrieveOptions_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetNewUserFile", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetNewUserComp", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetNewUserCompExt", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserFileSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompExtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UserCompExtRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UserCompRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UserFileListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserFileRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UserFileRow,
}

export interface Erp_Tablesets_UserCompExtRow{
      /**  User ID  */  
   "DcdUserID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company ID  */  
   "ExtCompID":string,
      /**  Site Identifier.  */  
   "CurPlant":string,
      /**  List of Sites the user has access to.  */  
   "PlantList":string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   "PrimBuyerID":string,
      /**  Initial height of the Overload Informer in pixels.  */  
   "OverloadInfHeight":number,
      /**  Initial overload informer sort option.  */  
   "OverloadInfSort":string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   "PrimSalesRepID":string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   "StartTaskSaleRepWB":boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   "StartTaskOppEnt":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   "StartOppSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   "StartOrdSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   "StartRMASaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   "StartSCallSaleRepWB":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_UserCompRow{
      /**  User ID  */  
   "DcdUserID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "CurPlant":string,
      /**  List of Sites the user has access to.  */  
   "PlantList":string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   "PrimBuyerID":string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   "Name":string,
      /**  Initial height of the Overload Informer in pixels.  */  
   "OverloadInfHeight":number,
      /**  Initial overload informer sort option.  */  
   "OverloadInfSort":string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   "PrimSalesRepID":string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   "StartTaskSaleRepWB":boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   "StartTaskOppEnt":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   "StartOppSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   "StartOrdSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   "StartRMASaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   "StartSCallSaleRepWB":boolean,
      /**  Unique identifier of the Workstations  */  
   "WorkstationID":string,
      /**  Employee ID  */  
   "EmpID":string,
      /**  Indicates if the user can update expense entries (EmpExpense) for any employee.  */  
   "CanUpdateExpense":boolean,
      /**  Indicates if the user can update time entries (LaborDtl) for any employee.  */  
   "CanUpdateTime":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  FWBLimitedRefresh  */  
   "FWBLimitedRefresh":boolean,
      /**  FWBUseDemandWhseOnly  */  
   "FWBUseDemandWhseOnly":boolean,
      /**  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  */  
   "SharedSupValidation":boolean,
      /**  TransactionRetrievalDays  */  
   "TransactionRetrievalDays":number,
   "BitFlag":number,
   "CompanyName":string,
   "DCDUserIDName":string,
   "EmpIDName":string,
   "WorkstationIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_UserFileListRow{
      /**  User ID  */  
   "DcdUserID":string,
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
      /**  Date the user last logged into the system.  */  
   "LastDate":string,
      /**  Time the user last logged into the system.  */  
   "LastTime":number,
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
      /**  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  */  
   "DspPayrollMgr":boolean,
      /**   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  */  
   "PayrollMgr":string,
      /**  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  */  
   "ShpTrackerIntMinute":number,
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
      /**  Whether the user can be referenced as the requestor on a PO Requisition.  */  
   "AllowReq":boolean,
      /**  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  */  
   "JCDept":string,
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
      /**  Whether the user can suspend his session.  */  
   "CanSuspend":boolean,
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
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the user has payroll manager rights for the current company  */  
   "DspPayrollMgrComp":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_UserFileRow{
      /**  User ID  */  
   "DcdUserID":string,
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
      /**  Date the user last logged into the system.  */  
   "LastDate":string,
      /**  Time the user last logged into the system.  */  
   "LastTime":number,
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
      /**  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  */  
   "DspPayrollMgr":boolean,
      /**   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  */  
   "PayrollMgr":string,
      /**  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  */  
   "ShpTrackerIntMinute":number,
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
      /**  Whether the user can be referenced as the requestor on a PO Requisition.  */  
   "AllowReq":boolean,
      /**  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  */  
   "JCDept":string,
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
      /**  Whether the user can suspend his session.  */  
   "CanSuspend":boolean,
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
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Epicor. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Epicor using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Epicor icon; they will be taken directly to the application main menu.  */  
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
      /**  User is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  */  
   "CanOverrideAllocations":boolean,
      /**   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  */  
   "GlbCompSM":boolean,
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
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  */  
   "TERetrieveApproved":boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  */  
   "TERetrieveEntered":boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  */  
   "TERetrieveRejected":boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  */  
   "TERetrieveSubmitted":boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  */  
   "TERetrievePartiallyApproved":boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  */  
   "TEAprRetrieveApproved":boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  */  
   "TEAprRetrieveEntered":boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  */  
   "TEAprRetrieveRejected":boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  */  
   "TEAprRetrieveSubmitted":boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  */  
   "TEAprRetrievePartiallyApproved":boolean,
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
      /**  MobilePassword  */  
   "MobilePassword":string,
      /**  ShopTrackerReuseLast  */  
   "ShopTrackerReuseLast":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AdvancedConfiguratorUser  */  
   "AdvancedConfiguratorUser":boolean,
      /**  TERetrieveByDay  */  
   "TERetrieveByDay":boolean,
      /**  TERetrieveByWeek  */  
   "TERetrieveByWeek":boolean,
      /**  TERetrieveByMonth  */  
   "TERetrieveByMonth":boolean,
      /**  If yes, the user will be able to enter a blank password and still get the prompt for new password.  */  
   "ClearPassword":boolean,
      /**  Indicates if the user has payroll manager rights for the current company  */  
   "DspPayrollMgrComp":boolean,
      /**  Indicates if DspPayrollMgr is enabled  */  
   "EnableDspPayrollMgr":boolean,
      /**  Indicates if DspPayrollMgrComp is enabled  */  
   "EnableDspPayrollMgrComp":boolean,
      /**  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  */  
   "ExpirePassword":boolean,
   "IsCurCompPayrollMgr":boolean,
   "UseCompression":boolean,
      /**  Indicates a user can run BAQ accross multiple companies  */  
   "BAQXCompany":boolean,
   "LangNameIDDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
   "Character01":string,
   "UD_SysRevID":string,
   "EpicUpgrade_c":boolean,
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
export interface CheckAdvancedConfiguratorUser_output{
   returnObj:boolean,
}

export interface CheckPayrollRights_output{
   returnObj:boolean,
}

   /** Required : 
      @param dcdUserID
   */  
export interface DeleteByID_input{
   dcdUserID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtUserFileTableset{
   UserFile:Erp_Tablesets_UserFileRow[],
   UserComp:Erp_Tablesets_UserCompRow[],
   UserCompExt:Erp_Tablesets_UserCompExtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UserCompExtRow{
      /**  User ID  */  
   DcdUserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company ID  */  
   ExtCompID:string,
      /**  Site Identifier.  */  
   CurPlant:string,
      /**  List of Sites the user has access to.  */  
   PlantList:string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   PrimBuyerID:string,
      /**  Initial height of the Overload Informer in pixels.  */  
   OverloadInfHeight:number,
      /**  Initial overload informer sort option.  */  
   OverloadInfSort:string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   PrimSalesRepID:string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   StartTaskSaleRepWB:boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   StartTaskOppEnt:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   StartOppSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   StartOrdSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   StartRMASaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   StartSCallSaleRepWB:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UserCompRow{
      /**  User ID  */  
   DcdUserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   CurPlant:string,
      /**  List of Sites the user has access to.  */  
   PlantList:string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   PrimBuyerID:string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   Name:string,
      /**  Initial height of the Overload Informer in pixels.  */  
   OverloadInfHeight:number,
      /**  Initial overload informer sort option.  */  
   OverloadInfSort:string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   PrimSalesRepID:string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   StartTaskSaleRepWB:boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   StartTaskOppEnt:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   StartOppSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   StartOrdSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   StartRMASaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   StartSCallSaleRepWB:boolean,
      /**  Unique identifier of the Workstations  */  
   WorkstationID:string,
      /**  Employee ID  */  
   EmpID:string,
      /**  Indicates if the user can update expense entries (EmpExpense) for any employee.  */  
   CanUpdateExpense:boolean,
      /**  Indicates if the user can update time entries (LaborDtl) for any employee.  */  
   CanUpdateTime:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  FWBLimitedRefresh  */  
   FWBLimitedRefresh:boolean,
      /**  FWBUseDemandWhseOnly  */  
   FWBUseDemandWhseOnly:boolean,
      /**  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  */  
   SharedSupValidation:boolean,
      /**  TransactionRetrievalDays  */  
   TransactionRetrievalDays:number,
   BitFlag:number,
   CompanyName:string,
   DCDUserIDName:string,
   EmpIDName:string,
   WorkstationIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UserFileListRow{
      /**  User ID  */  
   DcdUserID:string,
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
      /**  Date the user last logged into the system.  */  
   LastDate:string,
      /**  Time the user last logged into the system.  */  
   LastTime:number,
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
      /**  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  */  
   DspPayrollMgr:boolean,
      /**   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  */  
   PayrollMgr:string,
      /**  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  */  
   ShpTrackerIntMinute:number,
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
      /**  Whether the user can be referenced as the requestor on a PO Requisition.  */  
   AllowReq:boolean,
      /**  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  */  
   JCDept:string,
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
      /**  Whether the user can suspend his session.  */  
   CanSuspend:boolean,
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
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the user has payroll manager rights for the current company  */  
   DspPayrollMgrComp:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UserFileListTableset{
   UserFileList:Erp_Tablesets_UserFileListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UserFileRow{
      /**  User ID  */  
   DcdUserID:string,
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
      /**  Date the user last logged into the system.  */  
   LastDate:string,
      /**  Time the user last logged into the system.  */  
   LastTime:number,
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
      /**  Payroll Manager field used for display purposes only. See UserFile.PayrollMgr for additional information.  */  
   DspPayrollMgr:boolean,
      /**   Encoded field which indicates if the user is a Payroll Manager.
Only payroll managers can access the Payroll Class and Payroll Manager master files to assign rights to users in regards to viewing or processing payroll information.  */  
   PayrollMgr:string,
      /**  How often (in minutes) the user wants their shop tracker displays will be automatically refreshed.  */  
   ShpTrackerIntMinute:number,
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
      /**  Whether the user can be referenced as the requestor on a PO Requisition.  */  
   AllowReq:boolean,
      /**  Default JC Department for PO Requisitions (ReqDetail.JCDept) created by this user.  This can be left blank or must be valid in the JCDept table.  */  
   JCDept:string,
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
      /**  Whether the user can suspend his session.  */  
   CanSuspend:boolean,
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
Select this check box to indicate that this user has to use his/her operating system (Windows, Unix, and so on) logon information as the logon for Epicor. 
Single Sign-On (SSO) is functionality that allows users to sign on (log in) to Epicor using the Login IDs and Passwords they use to log into their computer's operating system (for example Windows, Unix, Linux and so on). In other words, if SSO is enabled, users will not be presented with a Logon window when they click their Epicor icon; they will be taken directly to the application main menu.  */  
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
      /**  User is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  */  
   CanOverrideAllocations:boolean,
      /**   Global Company Security Manager
Allows a user on a Isolated-Company system to behave like a user on a regular system. Can be allowed to login to multiple companies and can apply changes that affect all companies. Used to maintain menus and global customizations or security.  */  
   GlbCompSM:boolean,
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
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  */  
   TERetrieveApproved:boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  */  
   TERetrieveEntered:boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  */  
   TERetrieveRejected:boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  */  
   TERetrieveSubmitted:boolean,
      /**  When retrieving records in Time and Expense Entry, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  */  
   TERetrievePartiallyApproved:boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Approved status.  */  
   TEAprRetrieveApproved:boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Entered status.  */  
   TEAprRetrieveEntered:boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Rejected status.  */  
   TEAprRetrieveRejected:boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records currently in the Submitted status.  */  
   TEAprRetrieveSubmitted:boolean,
      /**  When retrieving records in Time and Expense Approval, this indicates whether this user wants to retrieve time and expense records that have been Partially Approved.  */  
   TEAprRetrievePartiallyApproved:boolean,
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
      /**  MobilePassword  */  
   MobilePassword:string,
      /**  ShopTrackerReuseLast  */  
   ShopTrackerReuseLast:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AdvancedConfiguratorUser  */  
   AdvancedConfiguratorUser:boolean,
      /**  TERetrieveByDay  */  
   TERetrieveByDay:boolean,
      /**  TERetrieveByWeek  */  
   TERetrieveByWeek:boolean,
      /**  TERetrieveByMonth  */  
   TERetrieveByMonth:boolean,
      /**  If yes, the user will be able to enter a blank password and still get the prompt for new password.  */  
   ClearPassword:boolean,
      /**  Indicates if the user has payroll manager rights for the current company  */  
   DspPayrollMgrComp:boolean,
      /**  Indicates if DspPayrollMgr is enabled  */  
   EnableDspPayrollMgr:boolean,
      /**  Indicates if DspPayrollMgrComp is enabled  */  
   EnableDspPayrollMgrComp:boolean,
      /**  If yes, the user will be forced to enter his or her current password before he or she will be prompted for the new password.  */  
   ExpirePassword:boolean,
   IsCurCompPayrollMgr:boolean,
   UseCompression:boolean,
      /**  Indicates a user can run BAQ accross multiple companies  */  
   BAQXCompany:boolean,
   LangNameIDDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
   Character01:string,
   UD_SysRevID:string,
   EpicUpgrade_c:boolean,
}

export interface Erp_Tablesets_UserFileTableset{
   UserFile:Erp_Tablesets_UserFileRow[],
   UserComp:Erp_Tablesets_UserCompRow[],
   UserCompExt:Erp_Tablesets_UserCompExtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param dcdUserID
   */  
export interface GetByID_input{
   dcdUserID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_UserFileTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_UserFileTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_UserFileTableset[],
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
   returnObj:Erp_Tablesets_UserFileListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param dcdUserID
      @param company
   */  
export interface GetNewUserCompExt_input{
   ds:Erp_Tablesets_UserFileTableset[],
   dcdUserID:string,
   company:string,
}

export interface GetNewUserCompExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param ds
      @param dcdUserID
   */  
export interface GetNewUserComp_input{
   ds:Erp_Tablesets_UserFileTableset[],
   dcdUserID:string,
}

export interface GetNewUserComp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewUserFile_input{
   ds:Erp_Tablesets_UserFileTableset[],
}

export interface GetNewUserFile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserFileTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetRowsFromList_input{
   ds:Erp_Tablesets_UserFileListTableset[],
}

export interface GetRowsFromList_output{
   returnObj:Erp_Tablesets_UserFileTableset[],
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
   returnObj:Erp_Tablesets_UserFileTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetUserTimeExpenseRetrieveOptions_output{
parameters : {
      /**  output parameters  */  
   retrieveApproved:boolean,
   retrieveEntered:boolean,
   retrievePartiallyApproved:boolean,
   retrieveRejected:boolean,
   retrieveSubmitted:boolean,
   retrieveByDay:boolean,
   retrieveByMonth:boolean,
   retrieveByWeek:boolean,
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
      @param retrieveApproved
      @param retrieveEntered
      @param retrievePartiallyApproved
      @param retrieveRejected
      @param retrieveSubmitted
      @param retrieveByDay
      @param retrieveByMonth
      @param retrieveByWeek
   */  
export interface SetUserTimeExpenseRetrieveOptions_input{
      /**  Retrieve approved  */  
   retrieveApproved:boolean,
      /**  Retrieve entered  */  
   retrieveEntered:boolean,
      /**  Retrieve partially approved  */  
   retrievePartiallyApproved:boolean,
      /**  Retrieve rejected  */  
   retrieveRejected:boolean,
      /**  Retrieve submitted  */  
   retrieveSubmitted:boolean,
      /**  Retrieve by date  */  
   retrieveByDay:boolean,
      /**  Retrieve by month  */  
   retrieveByMonth:boolean,
      /**  Retrieve by week  */  
   retrieveByWeek:boolean,
}

export interface SetUserTimeExpenseRetrieveOptions_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtUserFileTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtUserFileTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_UserFileTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserFileTableset,
}
}

