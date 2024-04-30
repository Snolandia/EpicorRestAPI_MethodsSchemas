import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.HelpDeskSvc
// Description: This is the Help Desk main business object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/$metadata", {
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
   Description: Get HelpDesks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HelpDesks
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseRow
   */  
export function get_HelpDesks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HelpDesks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HelpDesks(requestBody:Erp_Tablesets_HDCaseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks", {
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
   Summary: Calls GetByID to retrieve the HelpDesk item
   Description: Calls GetByID to retrieve the HelpDesk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HelpDesk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseRow
   */  
export function get_HelpDesks_Company_HDCaseNum(Company:string, HDCaseNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HelpDesk for the service
   Description: Calls UpdateExt to update HelpDesk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HelpDesk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HelpDesks_Company_HDCaseNum(Company:string, HDCaseNum:string, requestBody:Erp_Tablesets_HDCaseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")", {
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
   Summary: Call UpdateExt to delete HelpDesk item
   Description: Call UpdateExt to delete HelpDesk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HelpDesk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HelpDesks_Company_HDCaseNum(Company:string, HDCaseNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")", {
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
   Description: Get HDCaseFSCalls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseFSCalls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseFSCallRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseFSCalls(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseFSCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseFSCalls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseFSCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseFSCall item
   Description: Calls GetByID to retrieve the HDCaseFSCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseFSCall1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseFSCalls_SysRowID(Company:string, HDCaseNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseFSCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseFSCalls(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseFSCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseJobs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseJobs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseJobRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseJobs(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseJobRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseJobs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseJobRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseJob item
   Description: Calls GetByID to retrieve the HDCaseJob item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseJob1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseJobRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseJobs_SysRowID(Company:string, HDCaseNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseJobRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseJobs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseJobRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseLinks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseLinkRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseLinks(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseLinks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseLink item
   Description: Calls GetByID to retrieve the HDCaseLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseLink1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param ExternalLink Desc: ExternalLink   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseLinkRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company:string, HDCaseNum:string, ExternalLink:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseOrders items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseOrders1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseOrderRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseOrders(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseOrderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseOrders", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseOrderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseOrder item
   Description: Calls GetByID to retrieve the HDCaseOrder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseOrder1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseOrderRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseOrders_SysRowID(Company:string, HDCaseNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseOrderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseOrders(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseOrderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseQuotes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseQuotes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseQuoteRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseQuotes(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseQuoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseQuotes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseQuoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseQuote item
   Description: Calls GetByID to retrieve the HDCaseQuote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseQuote1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseQuotes_SysRowID(Company:string, HDCaseNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseQuoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseQuotes(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseQuoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseRMAs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseRMAs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseRMARow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseRMAs(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRMARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseRMAs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRMARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseRMA item
   Description: Calls GetByID to retrieve the HDCaseRMA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseRMA1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseRMARow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseRMAs_SysRowID(Company:string, HDCaseNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseRMARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseRMAs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseRMARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDChildCases items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDChildCases1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDChildCasesRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDChildCases(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDChildCasesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDChildCases", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDChildCasesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDChildCas item
   Description: Calls GetByID to retrieve the HDChildCas item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDChildCas1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDChildCasesRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDChildCases_Company_HDCaseNum(Company:string, HDCaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDChildCasesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDChildCases(" + Company + "," + HDCaseNum + ")", {
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
         resolve(data as Erp_Tablesets_HDChildCasesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDContacts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDContacts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDContactRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDContacts(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDContactRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDContacts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDContactRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDContact item
   Description: Calls GetByID to retrieve the HDContact item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDContact1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDContactRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company:string, HDCaseNum:string, PerConLnkRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDContactRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDContactRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseMaintReqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseMaintReqs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseMaintReqRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseMaintReqs(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseMaintReqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseMaintReqs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseMaintReqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseMaintReq item
   Description: Calls GetByID to retrieve the HDCaseMaintReq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseMaintReq1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseMaintReqs_SysRowID(Company:string, HDCaseNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseMaintReqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseMaintReqs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseMaintReqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get HDCaseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseAttchRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseAttches(Company:string, HDCaseNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the HDCaseAttch item
   Description: Calls GetByID to retrieve the HDCaseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseAttchRow
   */  
export function get_HelpDesks_Company_HDCaseNum_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company:string, HDCaseNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get HDCaseFSCalls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseFSCalls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseFSCallRow
   */  
export function get_HDCaseFSCalls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseFSCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseFSCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseFSCalls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseFSCallRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseFSCalls(requestBody:Erp_Tablesets_HDCaseFSCallRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls", {
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
   Summary: Calls GetByID to retrieve the HDCaseFSCall item
   Description: Calls GetByID to retrieve the HDCaseFSCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseFSCall
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   */  
export function get_HDCaseFSCalls_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseFSCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseFSCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseFSCall for the service
   Description: Calls UpdateExt to update HDCaseFSCall. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseFSCall
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseFSCalls_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_HDCaseFSCallRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete HDCaseFSCall item
   Description: Call UpdateExt to delete HDCaseFSCall item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseFSCall
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseFSCalls_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls(" + SysRowID + ")", {
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
   Description: Get HDCaseJobs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseJobs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseJobRow
   */  
export function get_HDCaseJobs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseJobRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseJobRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseJobs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseJobRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseJobs(requestBody:Erp_Tablesets_HDCaseJobRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs", {
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
   Summary: Calls GetByID to retrieve the HDCaseJob item
   Description: Calls GetByID to retrieve the HDCaseJob item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseJob
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseJobRow
   */  
export function get_HDCaseJobs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseJobRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseJobRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseJob for the service
   Description: Calls UpdateExt to update HDCaseJob. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseJob
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseJobs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_HDCaseJobRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete HDCaseJob item
   Description: Call UpdateExt to delete HDCaseJob item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseJob
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseJobs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs(" + SysRowID + ")", {
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
   Description: Get HDCaseLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseLinks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseLinkRow
   */  
export function get_HDCaseLinks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseLinks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseLinks(requestBody:Erp_Tablesets_HDCaseLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks", {
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
   Summary: Calls GetByID to retrieve the HDCaseLink item
   Description: Calls GetByID to retrieve the HDCaseLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param ExternalLink Desc: ExternalLink   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseLinkRow
   */  
export function get_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company:string, HDCaseNum:string, ExternalLink:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseLink for the service
   Description: Calls UpdateExt to update HDCaseLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param ExternalLink Desc: ExternalLink   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company:string, HDCaseNum:string, ExternalLink:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, requestBody:Erp_Tablesets_HDCaseLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Summary: Call UpdateExt to delete HDCaseLink item
   Description: Call UpdateExt to delete HDCaseLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param ExternalLink Desc: ExternalLink   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company:string, HDCaseNum:string, ExternalLink:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Description: Get HDCaseOrders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseOrders
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseOrderRow
   */  
export function get_HDCaseOrders(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseOrderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseOrderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseOrders
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseOrderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseOrders(requestBody:Erp_Tablesets_HDCaseOrderRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders", {
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
   Summary: Calls GetByID to retrieve the HDCaseOrder item
   Description: Calls GetByID to retrieve the HDCaseOrder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseOrder
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseOrderRow
   */  
export function get_HDCaseOrders_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseOrderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseOrderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseOrder for the service
   Description: Calls UpdateExt to update HDCaseOrder. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseOrder
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseOrders_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_HDCaseOrderRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete HDCaseOrder item
   Description: Call UpdateExt to delete HDCaseOrder item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseOrder
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseOrders_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders(" + SysRowID + ")", {
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
   Description: Get HDCaseQuotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseQuotes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseQuoteRow
   */  
export function get_HDCaseQuotes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseQuoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseQuoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseQuotes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseQuoteRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseQuotes(requestBody:Erp_Tablesets_HDCaseQuoteRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes", {
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
   Summary: Calls GetByID to retrieve the HDCaseQuote item
   Description: Calls GetByID to retrieve the HDCaseQuote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseQuote
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   */  
export function get_HDCaseQuotes_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseQuoteRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseQuoteRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseQuote for the service
   Description: Calls UpdateExt to update HDCaseQuote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseQuote
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseQuotes_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_HDCaseQuoteRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete HDCaseQuote item
   Description: Call UpdateExt to delete HDCaseQuote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseQuote
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseQuotes_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes(" + SysRowID + ")", {
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
   Description: Get HDCaseRMAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseRMAs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseRMARow
   */  
export function get_HDCaseRMAs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRMARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRMARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseRMAs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseRMARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseRMAs(requestBody:Erp_Tablesets_HDCaseRMARow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs", {
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
   Summary: Calls GetByID to retrieve the HDCaseRMA item
   Description: Calls GetByID to retrieve the HDCaseRMA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseRMA
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseRMARow
   */  
export function get_HDCaseRMAs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseRMARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseRMARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseRMA for the service
   Description: Calls UpdateExt to update HDCaseRMA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseRMA
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseRMAs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_HDCaseRMARow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete HDCaseRMA item
   Description: Call UpdateExt to delete HDCaseRMA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseRMA
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseRMAs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs(" + SysRowID + ")", {
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
   Description: Get HDChildCases items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDChildCases
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDChildCasesRow
   */  
export function get_HDChildCases(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDChildCasesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDChildCasesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDChildCases
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDChildCasesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDChildCases(requestBody:Erp_Tablesets_HDChildCasesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases", {
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
   Summary: Calls GetByID to retrieve the HDChildCas item
   Description: Calls GetByID to retrieve the HDChildCas item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDChildCas
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDChildCasesRow
   */  
export function get_HDChildCases_Company_HDCaseNum(Company:string, HDCaseNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDChildCasesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases(" + Company + "," + HDCaseNum + ")", {
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
         resolve(data as Erp_Tablesets_HDChildCasesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDChildCas for the service
   Description: Calls UpdateExt to update HDChildCas. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDChildCas
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDChildCases_Company_HDCaseNum(Company:string, HDCaseNum:string, requestBody:Erp_Tablesets_HDChildCasesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases(" + Company + "," + HDCaseNum + ")", {
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
   Summary: Call UpdateExt to delete HDChildCas item
   Description: Call UpdateExt to delete HDChildCas item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDChildCas
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDChildCases_Company_HDCaseNum(Company:string, HDCaseNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases(" + Company + "," + HDCaseNum + ")", {
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
   Description: Get HDContacts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDContacts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDContactRow
   */  
export function get_HDContacts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDContactRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDContactRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDContacts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDContactRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDContactRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDContacts(requestBody:Erp_Tablesets_HDContactRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts", {
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
   Summary: Calls GetByID to retrieve the HDContact item
   Description: Calls GetByID to retrieve the HDContact item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDContact
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDContactRow
   */  
export function get_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company:string, HDCaseNum:string, PerConLnkRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDContactRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDContactRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDContact for the service
   Description: Calls UpdateExt to update HDContact. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDContact
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDContactRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company:string, HDCaseNum:string, PerConLnkRowID:string, requestBody:Erp_Tablesets_HDContactRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")", {
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
   Summary: Call UpdateExt to delete HDContact item
   Description: Call UpdateExt to delete HDContact item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDContact
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company:string, HDCaseNum:string, PerConLnkRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")", {
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
   Description: Get HDCaseMaintReqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseMaintReqs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseMaintReqRow
   */  
export function get_HDCaseMaintReqs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseMaintReqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseMaintReqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseMaintReqs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseMaintReqs(requestBody:Erp_Tablesets_HDCaseMaintReqRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs", {
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
   Summary: Calls GetByID to retrieve the HDCaseMaintReq item
   Description: Calls GetByID to retrieve the HDCaseMaintReq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseMaintReq
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   */  
export function get_HDCaseMaintReqs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseMaintReqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseMaintReqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseMaintReq for the service
   Description: Calls UpdateExt to update HDCaseMaintReq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseMaintReq
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseMaintReqs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_HDCaseMaintReqRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete HDCaseMaintReq item
   Description: Call UpdateExt to delete HDCaseMaintReq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseMaintReq
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseMaintReqs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs(" + SysRowID + ")", {
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
   Description: Get HDCaseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseAttchRow
   */  
export function get_HDCaseAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HDCaseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HDCaseAttches(requestBody:Erp_Tablesets_HDCaseAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches", {
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
   Summary: Calls GetByID to retrieve the HDCaseAttch item
   Description: Calls GetByID to retrieve the HDCaseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HDCaseAttchRow
   */  
export function get_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company:string, HDCaseNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HDCaseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_HDCaseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HDCaseAttch for the service
   Description: Calls UpdateExt to update HDCaseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company:string, HDCaseNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_HDCaseAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete HDCaseAttch item
   Description: Call UpdateExt to delete HDCaseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HDCaseNum Desc: HDCaseNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company:string, HDCaseNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseHDCase:string, whereClauseHDCaseAttch:string, whereClauseHDCaseFSCall:string, whereClauseHDCaseJob:string, whereClauseHDCaseLink:string, whereClauseHDCaseOrder:string, whereClauseHDCaseQuote:string, whereClauseHDCaseRMA:string, whereClauseHDChildCases:string, whereClauseHDContact:string, whereClauseHDCaseMaintReq:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseHDCase!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCase=" + whereClauseHDCase
   }
   if(typeof whereClauseHDCaseAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseAttch=" + whereClauseHDCaseAttch
   }
   if(typeof whereClauseHDCaseFSCall!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseFSCall=" + whereClauseHDCaseFSCall
   }
   if(typeof whereClauseHDCaseJob!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseJob=" + whereClauseHDCaseJob
   }
   if(typeof whereClauseHDCaseLink!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseLink=" + whereClauseHDCaseLink
   }
   if(typeof whereClauseHDCaseOrder!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseOrder=" + whereClauseHDCaseOrder
   }
   if(typeof whereClauseHDCaseQuote!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseQuote=" + whereClauseHDCaseQuote
   }
   if(typeof whereClauseHDCaseRMA!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseRMA=" + whereClauseHDCaseRMA
   }
   if(typeof whereClauseHDChildCases!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDChildCases=" + whereClauseHDChildCases
   }
   if(typeof whereClauseHDContact!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDContact=" + whereClauseHDContact
   }
   if(typeof whereClauseHDCaseMaintReq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHDCaseMaintReq=" + whereClauseHDCaseMaintReq
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(hdCaseNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof hdCaseNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "hdCaseNum=" + hdCaseNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetList" + params, {
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
   Summary: Invoke method CheckPrePartInfo
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, a part number and if any substitutes exist.  Call this method
first before calling the ChangeDtlPartNum method when the field HDCase.PartNum changes.
   OperationID: CheckPrePartInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPrePartInfo(requestBody:CheckPrePartInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPrePartInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CheckPrePartInfo", {
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
         resolve(data as CheckPrePartInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateFSCall
   Description: Create a Field Service call from this Help Desk Case.
   OperationID: CreateFSCall
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateFSCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateFSCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateFSCall(requestBody:CreateFSCall_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateFSCall_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateFSCall", {
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
         resolve(data as CreateFSCall_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateFSCallLine
   Description: Create a Field Service call with 1 line , for this Help Desk Case.
   OperationID: CreateFSCallLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateFSCallLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateFSCallLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateFSCallLine(requestBody:CreateFSCallLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateFSCallLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateFSCallLine", {
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
         resolve(data as CreateFSCallLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateJob
   Description: Create a Job from this Help Desk Case.
PartNum must be populated before calling this method, as it is required on a Job
The HDCase in the database will be used for this call.
   OperationID: CreateJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateJob(requestBody:CreateJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateJob", {
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
         resolve(data as CreateJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckProjectID
   Description: Validate the Project ID for Quotes, Orders and Jobs.
   OperationID: CheckProjectID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckProjectID(requestBody:CheckProjectID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckProjectID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CheckProjectID", {
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
         resolve(data as CheckProjectID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMaintReq
   Description: Create a Request from this Help Desk Case.
   OperationID: CreateMaintReq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMaintReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMaintReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMaintReq(requestBody:CreateMaintReq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMaintReq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateMaintReq", {
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
         resolve(data as CreateMaintReq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateOrder
   Description: Create a quote from this Help Desk Case.
CustNum must be populated before calling this method, as it is required on a quote
The HDCase in the database will be used for this call.
   OperationID: CreateOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateOrder(requestBody:CreateOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateOrder", {
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
         resolve(data as CreateOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateQuote
   Description: Create a quote from this Help Desk Case.
CustNum must be populated before calling this method, as it is required on a quote
The HDCase in the database will be used for this call.
   OperationID: CreateQuote
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateQuote(requestBody:CreateQuote_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateQuote_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateQuote", {
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
         resolve(data as CreateQuote_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateQuoteWithLine
   Description: Create a quote with 1 line for this Help Desk Case.
CustNum and PartNum must be populated before calling this method, as it is required on a quote
The HDCase in the database will be used for this call.
   OperationID: CreateQuoteWithLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateQuoteWithLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteWithLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateQuoteWithLine(requestBody:CreateQuoteWithLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateQuoteWithLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateQuoteWithLine", {
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
         resolve(data as CreateQuoteWithLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateOrderWithLine
   OperationID: CreateOrderWithLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateOrderWithLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderWithLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateOrderWithLine(requestBody:CreateOrderWithLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateOrderWithLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateOrderWithLine", {
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
         resolve(data as CreateOrderWithLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateRMAUpdConNum
   Description: Create an RMA from this Help Desk Case.
CustNum and PrcConNum (customer contact) must be populated before calling this method, as it is required on an RMA
The HDCase in the database will be used for this call.
   OperationID: CreateRMAUpdConNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateRMAUpdConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRMAUpdConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateRMAUpdConNum(requestBody:CreateRMAUpdConNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateRMAUpdConNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateRMAUpdConNum", {
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
         resolve(data as CreateRMAUpdConNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateRMALine
   Description: Create an RMA with 1 line for this Help Desk Case.
CustNum and PrcConNum (customer contact) must be populated before calling this method, as it is required on an RMA
The HDCase in the database will be used for this call.
   OperationID: CreateRMALine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateRMALine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRMALine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateRMALine(requestBody:CreateRMALine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateRMALine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateRMALine", {
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
         resolve(data as CreateRMALine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateRMA
   Description: Create an RMA from this Help Desk Case.
CustNum must be populated before calling this method, as it is required on an RMA
The HDCase in the database will be used for this call.
   OperationID: CreateRMA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateRMA(requestBody:CreateRMA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateRMA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/CreateRMA", {
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
         resolve(data as CreateRMA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangedTaskSet
   Description: Change a Task from this Help Desk Case when changing the Task Set.
   OperationID: ChangedTaskSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangedTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedTaskSet(requestBody:ChangedTaskSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangedTaskSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/ChangedTaskSet", {
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
         resolve(data as ChangedTaskSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRMAHeadLink
   Description: Update RMAHead.HDCaseNum  = 0  to delete the link from the current HDCase.
RMAHead is populated with the record filter by the current Company, HDCaseNum and RMANum
it is modified to remove the HDCaseNum
   OperationID: DeleteRMAHeadLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRMAHeadLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRMAHeadLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRMAHeadLink(requestBody:DeleteRMAHeadLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRMAHeadLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteRMAHeadLink", {
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
         resolve(data as DeleteRMAHeadLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteQuoteHedLink
   Description: Update QuoteHed.HDCaseNum  = 0  to delete the link from the current HDCase.
QuoteHead is populated with the record filter by the current Company, HDCaseNum and QuoteNum
it is modified to remove the HDCaseNum
   OperationID: DeleteQuoteHedLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteQuoteHedLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQuoteHedLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteQuoteHedLink(requestBody:DeleteQuoteHedLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteQuoteHedLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteQuoteHedLink", {
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
         resolve(data as DeleteQuoteHedLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteOrderHedLink
   Description: Update OrderHed.HDCaseNum  = 0  to delete the link from the current HDCase.
OrderHed is populated with the record filter by the current Company, HDCaseNum and OrderNum
it is modified to remove the HDCaseNum
   OperationID: DeleteOrderHedLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteOrderHedLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOrderHedLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteOrderHedLink(requestBody:DeleteOrderHedLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteOrderHedLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteOrderHedLink", {
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
         resolve(data as DeleteOrderHedLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteJobHeadLink
   Description: Update JobHead.HDCaseNum  = 0  to delete the link from the current HDCase.
JobHead is populated with the record filter by the current Company, HDCaseNum and jobNum
it is modified to remove the HDCaseNum
   OperationID: DeleteJobHeadLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteJobHeadLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteJobHeadLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteJobHeadLink(requestBody:DeleteJobHeadLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteJobHeadLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteJobHeadLink", {
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
         resolve(data as DeleteJobHeadLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteFSCallhdLink
   Description: Update FSCallhd.HDCaseNum  = 0  to delete the link from the current HDCase.
FSCallhd is populated with the record filter by the current Company, HDCaseNum and callNum
it is modified to remove the HDCaseNum
   OperationID: DeleteFSCallhdLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteFSCallhdLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFSCallhdLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFSCallhdLink(requestBody:DeleteFSCallhdLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteFSCallhdLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteFSCallhdLink", {
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
         resolve(data as DeleteFSCallhdLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteMaintReqLink
   Description: Update MaintReq.HDCaseNum  = 0  to delete the link from the current HDCase.
MaintReq is populated with the record filter by the current Company, HDCaseNum and ReqID
it is modified to remove the HDCaseNum
   OperationID: DeleteMaintReqLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteMaintReqLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMaintReqLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteMaintReqLink(requestBody:DeleteMaintReqLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteMaintReqLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteMaintReqLink", {
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
         resolve(data as DeleteMaintReqLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteHDCaseExternalLink
   Description: Delete HDCaseLink records associated with the current HDCase.
   OperationID: DeleteHDCaseExternalLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteHDCaseExternalLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteHDCaseExternalLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteHDCaseExternalLink(requestBody:DeleteHDCaseExternalLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteHDCaseExternalLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteHDCaseExternalLink", {
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
         resolve(data as DeleteHDCaseExternalLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteHDChildCaseLink
   Description: Delete HDChildCase records associated with the current HDCase.
   OperationID: DeleteHDChildCaseLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteHDChildCaseLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteHDChildCaseLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteHDChildCaseLink(requestBody:DeleteHDChildCaseLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteHDChildCaseLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteHDChildCaseLink", {
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
         resolve(data as DeleteHDChildCaseLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTaskSets
   Description: Get the topics to make available as children to a given topic.
For top level topics, pass in  a blank parentTopicID
For all topics pass in "ReturnFullTopicList"
   OperationID: GetAvailTaskSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailTaskSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTaskSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTaskSets(requestBody:GetAvailTaskSets_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTaskSets_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetAvailTaskSets", {
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
         resolve(data as GetAvailTaskSets_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetChildTopics
   Description: Get the topics to make available as children to a given topic.
           For top level topics, pass in  a blank parentTopicID
           For all topics pass in "ReturnFullTopicList"
   OperationID: GetChildTopics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetChildTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChildTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetChildTopics(requestBody:GetChildTopics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetChildTopics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetChildTopics", {
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
         resolve(data as GetChildTopics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetChildTopicsDS
   Description: Populate HDCaseSearch ds with child topics.
   OperationID: GetChildTopicsDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetChildTopicsDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChildTopicsDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetChildTopicsDS(requestBody:GetChildTopicsDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetChildTopicsDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetChildTopicsDS", {
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
         resolve(data as GetChildTopicsDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseSearchDS
   Description: Get new HDCaseSearch data and populate the dataset with child topics.
   OperationID: GetNewHDCaseSearchDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseSearchDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseSearchDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseSearchDS(requestBody:GetNewHDCaseSearchDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseSearchDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseSearchDS", {
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
         resolve(data as GetNewHDCaseSearchDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSearchTopicID
   Description: Validate change of search topics and populate the next available combo box.
   OperationID: OnChangeSearchTopicID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSearchTopicID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSearchTopicID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSearchTopicID(requestBody:OnChangeSearchTopicID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSearchTopicID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeSearchTopicID", {
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
         resolve(data as OnChangeSearchTopicID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseSearch
   Description: Get a blank set of search parameters
   OperationID: GetNewHDCaseSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseSearch(requestBody:GetNewHDCaseSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseSearch", {
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
         resolve(data as GetNewHDCaseSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method createAvailableMilestonesList
   Description: Return a delimited list of the available Milestone for the selected Help Desk Case number.
   OperationID: createAvailableMilestonesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/createAvailableMilestonesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createAvailableMilestonesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_createAvailableMilestonesList(requestBody:createAvailableMilestonesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<createAvailableMilestonesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/createAvailableMilestonesList", {
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
         resolve(data as createAvailableMilestonesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method createAvailableTaskSetsList
   Description: Return a list of Available TaskSets
   OperationID: createAvailableTaskSetsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/createAvailableTaskSetsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createAvailableTaskSetsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_createAvailableTaskSetsList(requestBody:createAvailableTaskSetsList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<createAvailableTaskSetsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/createAvailableTaskSetsList", {
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
         resolve(data as createAvailableTaskSetsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:GetRowsContactTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsContactTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetRowsContactTracker", {
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
         resolve(data as GetRowsContactTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HelpDeskSearch
   Description: Perform a search of the helpdesk and/or knowledgebase cases
   OperationID: HelpDeskSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HelpDeskSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HelpDeskSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HelpDeskSearch(requestBody:HelpDeskSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HelpDeskSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDeskSearch", {
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
         resolve(data as HelpDeskSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAttrCodeList
   Description: Get the defaults from the AttrCodeList field on the HDCase record.
   OperationID: OnChangeAttrCodeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAttrCodeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttrCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttrCodeList(requestBody:OnChangeAttrCodeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAttrCodeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeAttrCodeList", {
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
         resolve(data as OnChangeAttrCodeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBuyerID
   Description: This method should be called when BuyerID change.
   OperationID: OnChangeBuyerID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBuyerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBuyerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBuyerID(requestBody:OnChangeBuyerID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBuyerID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeBuyerID", {
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
         resolve(data as OnChangeBuyerID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCallLine
   Description: Get the defaults from the CallLine field on the HDCase
record.
   OperationID: OnChangeCallLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCallLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCallLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCallLine(requestBody:OnChangeCallLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCallLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeCallLine", {
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
         resolve(data as OnChangeCallLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCallNum
   Description: Get the defaults from the CallNum field on the HDCase
record.
   OperationID: OnChangeCallNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCallNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCallNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCallNum(requestBody:OnChangeCallNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCallNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeCallNum", {
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
         resolve(data as OnChangeCallNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCaseOwner
   Description: Get the defaults from the CaseOwner field on the HDCase
record.
   OperationID: OnChangeCaseOwner
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCaseOwner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCaseOwner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCaseOwner(requestBody:OnChangeCaseOwner_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCaseOwner_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeCaseOwner", {
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
         resolve(data as OnChangeCaseOwner_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCaseTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeCaseTopics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCaseTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCaseTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCaseTopics(requestBody:OnChangeCaseTopics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCaseTopics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeCaseTopics", {
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
         resolve(data as OnChangeCaseTopics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCaseTypeID
   Description: Get the defaults for the Case Type on HDCase.
   OperationID: OnChangeCaseTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCaseTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCaseTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCaseTypeID(requestBody:OnChangeCaseTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCaseTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeCaseTypeID", {
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
         resolve(data as OnChangeCaseTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeContractNum
   Description: Get the defaults from the ContractNum field on the HDCase record.
   OperationID: OnChangeContractNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeContractNum(requestBody:OnChangeContractNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeContractNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeContractNum", {
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
         resolve(data as OnChangeContractNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeContractLine
   OperationID: OnChangeContractLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeContractLine(requestBody:OnChangeContractLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeContractLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeContractLine", {
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
         resolve(data as OnChangeContractLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ContractHasLines
   Description: Get the ContractLines from the ContractNum field on the HDCase record.
   OperationID: ContractHasLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ContractHasLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContractHasLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContractHasLines(requestBody:ContractHasLines_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ContractHasLines_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/ContractHasLines", {
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
         resolve(data as ContractHasLines_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateContractStatus
   Description: Validate the ContractNum field on the HDCase record.
   OperationID: ValidateContractStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateContractStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateContractStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateContractStatus(requestBody:ValidateContractStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateContractStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/ValidateContractStatus", {
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
         resolve(data as ValidateContractStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateContractPart
   Description: Validate the ContractNum field on the HDCase record.
   OperationID: ValidateContractPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateContractPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateContractPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateContractPart(requestBody:ValidateContractPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateContractPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/ValidateContractPart", {
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
         resolve(data as ValidateContractPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   Description: Find part.
   OperationID: FindPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:FindPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/FindPart", {
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
         resolve(data as FindPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID.
   OperationID: GetPartFromRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:GetPartFromRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartFromRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetPartFromRowID", {
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
         resolve(data as GetPartFromRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCustID
   Description: Get the defaults from the CustID field on the HDCase
           record.
           This will set:
           The Customer Contact
   OperationID: OnChangeCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCustID(requestBody:OnChangeCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeCustID", {
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
         resolve(data as OnChangeCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEmpID
   Description: This method should be called when EmpID change.
   OperationID: OnChangeEmpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEmpID(requestBody:OnChangeEmpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEmpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeEmpID", {
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
         resolve(data as OnChangeEmpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEquipID
   Description: This method should be called when EquipID change.
   OperationID: OnChangeEquipID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEquipID(requestBody:OnChangeEquipID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEquipID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeEquipID", {
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
         resolve(data as OnChangeEquipID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeHDCaseSearch
   Description: Validates the search fields
   OperationID: OnChangeHDCaseSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeHDCaseSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHDCaseSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeHDCaseSearch(requestBody:OnChangeHDCaseSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeHDCaseSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeHDCaseSearch", {
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
         resolve(data as OnChangeHDCaseSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeInvoiceLine
   Description: Get the defaults from the InvoiceLine field on the HDCase
record.
   OperationID: OnChangeInvoiceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInvoiceLine(requestBody:OnChangeInvoiceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeInvoiceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeInvoiceLine", {
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
         resolve(data as OnChangeInvoiceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeInvoiceNum
   Description: Get the defaults from the InvoiceNum field on the HDCase
           record.
   OperationID: OnChangeInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInvoiceNum(requestBody:OnChangeInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeInvoiceNum", {
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
         resolve(data as OnChangeInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMktgCampaignID
   Description: Get the defaults from the MktgCampaignID field on the HDCase
record.
   OperationID: OnChangeMktgCampaignID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMktgCampaignID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgCampaignID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMktgCampaignID(requestBody:OnChangeMktgCampaignID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMktgCampaignID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeMktgCampaignID", {
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
         resolve(data as OnChangeMktgCampaignID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMktgEvntSeq
   Description: Get the defaults from the MktgEvntSeq field on the HDCase
record.
   OperationID: OnChangeMktgEvntSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMktgEvntSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgEvntSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMktgEvntSeq(requestBody:OnChangeMktgEvntSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMktgEvntSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeMktgEvntSeq", {
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
         resolve(data as OnChangeMktgEvntSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeName
   Description: This method should be called when Name change.
   OperationID: OnChangeName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeName(requestBody:OnChangeName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeName", {
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
         resolve(data as OnChangeName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOrderLine
   Description: Get the defaults from the OrderLine field on the HDCase
record.
   OperationID: OnChangeOrderLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOrderLine(requestBody:OnChangeOrderLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOrderLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeOrderLine", {
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
         resolve(data as OnChangeOrderLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOrderNum
   Description: Get the defaults from the OrderNum field on the HDCase
record.
   OperationID: OnChangeOrderNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOrderNum(requestBody:OnChangeOrderNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOrderNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeOrderNum", {
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
         resolve(data as OnChangeOrderNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOrderRelNum
   Description: Get the defaults from the OrderRelNum field on the HDCase
record.
   OperationID: OnChangeOrderRelNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOrderRelNum(requestBody:OnChangeOrderRelNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOrderRelNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeOrderRelNum", {
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
         resolve(data as OnChangeOrderRelNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Get the defaults from the PartNum field on the HDCase
record.
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePerConLnkRowID
   Description: This method should be called when PerConLnkRowID change.
   OperationID: OnChangePerConLnkRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePerConLnkRowID(requestBody:OnChangePerConLnkRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePerConLnkRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangePerConLnkRowID", {
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
         resolve(data as OnChangePerConLnkRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePrcConNum
   Description: Get the defaults from the PrcConNum field on the HDCase
record.
   OperationID: OnChangePrcConNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePrcConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrcConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePrcConNum(requestBody:OnChangePrcConNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePrcConNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangePrcConNum", {
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
         resolve(data as OnChangePrcConNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeProjectID
   Description: Validate the ProjectID record.
   OperationID: OnChangeProjectID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeProjectID(requestBody:OnChangeProjectID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeProjectID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeProjectID", {
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
         resolve(data as OnChangeProjectID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePurPoint
   Description: Get the defaults from the PurPoint field on the HDCase record.
   OperationID: OnChangePurPoint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePurPoint(requestBody:OnChangePurPoint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePurPoint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangePurPoint", {
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
         resolve(data as OnChangePurPoint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePurPointConNum
   Description: Get the defaults from the PurPointConNum field on the HDCase record.
   OperationID: OnChangePurPointConNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePurPointConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPointConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePurPointConNum(requestBody:OnChangePurPointConNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePurPointConNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangePurPointConNum", {
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
         resolve(data as OnChangePurPointConNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuantity
   Description: Calculate de Ext Price when Quantity Change
   OperationID: OnChangeQuantity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuantity(requestBody:OnChangeQuantity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuantity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeQuantity", {
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
         resolve(data as OnChangeQuantity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuantityUOM
   Description: Calculate de Unit Price when change
   OperationID: OnChangeQuantityUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuantityUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantityUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuantityUOM(requestBody:OnChangeQuantityUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuantityUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeQuantityUOM", {
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
         resolve(data as OnChangeQuantityUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuoteLine
   Description: Get the defaults from the QuoteLine field on the HDCase record.
   OperationID: OnChangeQuoteLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuoteLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuoteLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuoteLine(requestBody:OnChangeQuoteLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuoteLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeQuoteLine", {
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
         resolve(data as OnChangeQuoteLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuoteNum
   Description: Get the defaults from the QuoteNum field on the HDCase record.
   OperationID: OnChangeQuoteNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuoteNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuoteNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuoteNum(requestBody:OnChangeQuoteNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuoteNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeQuoteNum", {
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
         resolve(data as OnChangeQuoteNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeReqPerConID
   Description: Get the defaults from the ReqPerConID field on the HDCase record.
   OperationID: OnChangeReqPerConID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeReqPerConID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReqPerConID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeReqPerConID(requestBody:OnChangeReqPerConID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeReqPerConID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeReqPerConID", {
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
         resolve(data as OnChangeReqPerConID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeReqPerConLnkRowID
   Description: Get the defaults from the ReqPerConLnkRowID field on the HDCase record.
   OperationID: OnChangeReqPerConLnkRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeReqPerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReqPerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeReqPerConLnkRowID(requestBody:OnChangeReqPerConLnkRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeReqPerConLnkRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeReqPerConLnkRowID", {
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
         resolve(data as OnChangeReqPerConLnkRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRevisionNum
   Description: Get the defaults from the RevisionNum field on the HDCase record.
   OperationID: OnChangeRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRevisionNum(requestBody:OnChangeRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeRevisionNum", {
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
         resolve(data as OnChangeRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRMALine
   Description: Get the defaults from the RMALine field on the HDCase record.
   OperationID: OnChangeRMALine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRMALine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRMALine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRMALine(requestBody:OnChangeRMALine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRMALine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeRMALine", {
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
         resolve(data as OnChangeRMALine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRMANum
   Description: Get the defaults from the RMANum field on the HDCase record.
   OperationID: OnChangeRMANum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRMANum(requestBody:OnChangeRMANum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRMANum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeRMANum", {
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
         resolve(data as OnChangeRMANum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSearchCaseTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeSearchCaseTopics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSearchCaseTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSearchCaseTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSearchCaseTopics(requestBody:OnChangeSearchCaseTopics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSearchCaseTopics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeSearchCaseTopics", {
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
         resolve(data as OnChangeSearchCaseTopics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSearchTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeSearchTopics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSearchTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSearchTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSearchTopics(requestBody:OnChangeSearchTopics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSearchTopics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeSearchTopics", {
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
         resolve(data as OnChangeSearchTopics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSerialNoPartNum
   Description: Get the PartNum from the SerialNumber field on the HDCase record.
   OperationID: GetSerialNoPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSerialNoPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNoPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNoPartNum(requestBody:GetSerialNoPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSerialNoPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetSerialNoPartNum", {
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
         resolve(data as GetSerialNoPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSerialNumber
   Description: Get the defaults from the SerialNumber field on the HDCase record.
   OperationID: OnChangeSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSerialNumber(requestBody:OnChangeSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeSerialNumber", {
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
         resolve(data as OnChangeSerialNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShipToCustID
   Description: Get the defaults from the ShipToCustID field on the HDCase record.
   OperationID: OnChangeShipToCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipToCustID(requestBody:OnChangeShipToCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShipToCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeShipToCustID", {
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
         resolve(data as OnChangeShipToCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTaskSetID
   Description: Check for related task with mandatory milestones related to be completed
   OperationID: OnChangeTaskSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTaskSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaskSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTaskSetID(requestBody:OnChangeTaskSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTaskSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeTaskSetID", {
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
         resolve(data as OnChangeTaskSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShipToNum
   Description: Get the defaults from the ShipToNum field on the HDCase record.
   OperationID: OnChangeShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShipToNum(requestBody:OnChangeShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeShipToNum", {
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
         resolve(data as OnChangeShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeShpConNum
   Description: Get the defaults from the ShpConNum field on the HDCase record.
   OperationID: OnChangeShpConNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeShpConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShpConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeShpConNum(requestBody:OnChangeShpConNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeShpConNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeShpConNum", {
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
         resolve(data as OnChangeShpConNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeTopics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTopics(requestBody:OnChangeTopics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTopics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeTopics", {
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
         resolve(data as OnChangeTopics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUnitPrice
   Description: Calculate de Ext Price
   OperationID: OnChangeUnitPrice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUnitPrice(requestBody:OnChangeUnitPrice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUnitPrice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeUnitPrice", {
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
         resolve(data as OnChangeUnitPrice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVenConNum
   Description: Get the defaults from the PrcConNum field on the HDCase record.
   OperationID: OnChangeVenConNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVenConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVenConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVenConNum(requestBody:OnChangeVenConNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVenConNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeVenConNum", {
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
         resolve(data as OnChangeVenConNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeVendorID
   Description: Get the defaults from the VendorID field on the HDCase record.
   OperationID: OnChangeVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeVendorID(requestBody:OnChangeVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeVendorID", {
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
         resolve(data as OnChangeVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWarrantyCode
   Description: Get the defaults from the WarrantyCode field on the HDCase record.
   OperationID: OnChangeWarrantyCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWarrantyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWarrantyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWarrantyCode(requestBody:OnChangeWarrantyCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWarrantyCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeWarrantyCode", {
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
         resolve(data as OnChangeWarrantyCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWFGroupID
   Description: Get the defaults from the WFGroupID field on the HDCase record.
   OperationID: OnChangeWFGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWFGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWFGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWFGroupID(requestBody:OnChangeWFGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWFGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OnChangeWFGroupID", {
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
         resolve(data as OnChangeWFGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OpenCloseCase
   Description: This method either opens or closes a Case and returns the updated object
   OperationID: OpenCloseCase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OpenCloseCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCloseCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenCloseCase(requestBody:OpenCloseCase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OpenCloseCase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/OpenCloseCase", {
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
         resolve(data as OpenCloseCase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreOpenCloseCase
   Description: This method is to be run before the OpenCloseCase method so that any questions
that need to be asked before the OpenCloseCase method can run can be asked
   OperationID: PreOpenCloseCase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreOpenCloseCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreOpenCloseCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreOpenCloseCase(requestBody:PreOpenCloseCase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreOpenCloseCase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/PreOpenCloseCase", {
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
         resolve(data as PreOpenCloseCase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFSCallRequirements
   Description: Validates if we have all the required data to create a FSCallLine.
   OperationID: ValidateFSCallRequirements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFSCallRequirements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFSCallRequirements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFSCallRequirements(requestBody:ValidateFSCallRequirements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFSCallRequirements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/ValidateFSCallRequirements", {
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
         resolve(data as ValidateFSCallRequirements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCase
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCase(requestBody:GetNewHDCase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCase", {
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
         resolve(data as GetNewHDCase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseAttch(requestBody:GetNewHDCaseAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseAttch", {
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
         resolve(data as GetNewHDCaseAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseFSCall
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseFSCall
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseFSCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseFSCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseFSCall(requestBody:GetNewHDCaseFSCall_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseFSCall_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseFSCall", {
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
         resolve(data as GetNewHDCaseFSCall_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseJob
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseJob(requestBody:GetNewHDCaseJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseJob", {
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
         resolve(data as GetNewHDCaseJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseLink(requestBody:GetNewHDCaseLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseLink", {
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
         resolve(data as GetNewHDCaseLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseOrder
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseOrder(requestBody:GetNewHDCaseOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseOrder", {
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
         resolve(data as GetNewHDCaseOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseQuote
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseQuote
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseQuote(requestBody:GetNewHDCaseQuote_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseQuote_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseQuote", {
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
         resolve(data as GetNewHDCaseQuote_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseRMA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseRMA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseRMA(requestBody:GetNewHDCaseRMA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseRMA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseRMA", {
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
         resolve(data as GetNewHDCaseRMA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDChildCases
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDChildCases
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDChildCases_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDChildCases_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDChildCases(requestBody:GetNewHDChildCases_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDChildCases_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDChildCases", {
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
         resolve(data as GetNewHDChildCases_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDContact
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDContact
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDContact(requestBody:GetNewHDContact_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDContact_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDContact", {
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
         resolve(data as GetNewHDContact_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewHDCaseMaintReq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseMaintReq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseMaintReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseMaintReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHDCaseMaintReq(requestBody:GetNewHDCaseMaintReq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHDCaseMaintReq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetNewHDCaseMaintReq", {
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
         resolve(data as GetNewHDCaseMaintReq_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseFSCallRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseFSCallRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseJobRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseJobRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseLinkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseLinkRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseMaintReqRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseMaintReqRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseOrderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseOrderRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseQuoteRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseQuoteRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRMARow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseRMARow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDCaseRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDChildCasesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDChildCasesRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDContactRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HDContactRow,
}

export interface Erp_Tablesets_HDCaseAttchRow{
   "Company":string,
   "HDCaseNum":number,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseFSCallRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   "CallNum":number,
      /**  The help desk case that created this service call.  */  
   "HDCaseNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseJobRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseLinkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  If true this is an external link that was manually entered.  Internal links will refer to other database records.  */  
   "ExternalLink":boolean,
      /**  Identifies the master file to which the link is related.  If an external link this will be blank.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record.  */  
   "Key1":string,
      /**  2nd component of the foreign key to the related master record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  */  
   "Key3":string,
      /**  4th component of the foreign key to the related master record.  */  
   "Key4":string,
      /**  5th component of the foreign key to the related master record.  */  
   "Key5":string,
      /**  Description of the link contents.  */  
   "Description":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  The customer associated with this case.  */  
   "CustNum":number,
      /**  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  */  
   "ShipToNum":string,
      /**  The parent Help Desk case number of this case.  */  
   "ParentCase":number,
      /**  The description of the case issue.  */  
   "Description":string,
      /**  A description if the resolution for the case.  */  
   "ResolutionText":string,
      /**  Publishable text of the issue and resolution of the case.  */  
   "PublishedText":string,
      /**  A summary of the issue/resolution of the help desk case.  */  
   "PublishedSummary":string,
      /**  If true this is a Knowledge Base entry.  */  
   "KBEntry":boolean,
      /**  If true this item can be published.  If false this item is for internal use only.  */  
   "PublishedItem":boolean,
      /**  The part that is associated with this Help Desk case.  The part is in the Part table.  */  
   "PartNum":string,
      /**  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  */  
   "SerialNumber":string,
      /**  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  */  
   "QuoteNum":number,
      /**  The order associated with the Help Desk case.  The order is in the OrderHed table.  */  
   "OrderNum":number,
      /**  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  */  
   "CaseOwner":string,
      /**  Date which this Help Desk case was created.  Not maintainable by the user.  */  
   "CreatedDate":string,
      /**  UserID who created the Help Desk case.  Not maintainable by the user.  */  
   "CreatedBy":string,
      /**  The time (in milliseconds) that the Help Desk case was created.  */  
   "CreatedTime":number,
      /**  UserID who last updated the Help Desk case.  Not maintainable by the user.  */  
   "LastUpdatedBy":string,
      /**  Date which this Help Desk case was last updated.  Not maintainable by the user.  */  
   "LastUpdatedDate":string,
      /**  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  */  
   "LastUpdatedTime":number,
      /**  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  */  
   "TopicID1":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  */  
   "TopicID2":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  */  
   "TopicID3":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  */  
   "TopicID4":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  */  
   "TopicID5":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  */  
   "TopicID6":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  */  
   "TopicID7":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  */  
   "TopicID8":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  */  
   "TopicID9":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  */  
   "TopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "CaseTopics":string,
      /**  Revision number  */  
   "RevisionNum":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  A general quantity field.  */  
   "Quantity":number,
      /**   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  */  
   "QuantityUOM":string,
      /**  The quote line number  */  
   "QuoteLine":number,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  The invoice line.  */  
   "InvoiceLine":number,
      /**  Customer Name  */  
   "CustomerName":string,
      /**  Packing slip number that this Service call is linked with.  */  
   "PackNum":number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   "PackLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Case Completed By  */  
   "CompletedBy":string,
      /**  Case Completion Date  */  
   "CompletionDate":string,
      /**  Case Completion Time  */  
   "CompletionTime":number,
      /**  Unit price for the PartNum.  */  
   "UnitPrice":number,
      /**  Same as UnitPrice except that this field contains the unit price in the case currency.  */  
   "DocUnitPrice":number,
      /**  Extended Price in Report currency 1.  */  
   "Rp1ExtPrice":number,
      /**  Extended Price in Report currency 2.  */  
   "Rp2ExtPrice":number,
      /**  Unique identifier of the case type.  */  
   "CaseTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Case attribute code list  */  
   "AttrCodeList":string,
      /**  Short summary if the issue  */  
   "IssueSummary":string,
      /**  Long issue description  */  
   "IssueText":string,
      /**  String version of the creation time  */  
   "DispCreateTime":string,
      /**  String version of the last update time  */  
   "DispLastUpdateTime":string,
      /**  Name  */  
   "CaseOwnerName":string,
   "CaseCode":string,
   "NextReviewDate":string,
   "EvaluationStatus":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumBTName":string,
   "ShipToNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseMaintReqRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  */  
   "ReqID":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseOrderRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "OrderNum":number,
      /**  The help desk case that created this order.  */  
   "HDCaseNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Project_c":string,
   "OriginalOrderNo_c":number,
   "MASFlag_c":boolean,
   "Estimate_c":boolean,
   "ShipOrderComplete_c":boolean,
   "ProjectID_c":string,
   "PhaseID_c":string,
   "SalesCatID__c":string,
   "TaxCatID_c":string,
   "MfgOrder_c":boolean,
}

export interface Erp_Tablesets_HDCaseQuoteRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   "QuoteNum":number,
      /**  The help desk case that created this quote.  */  
   "HDCaseNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseRMARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   "RMANum":number,
      /**  The help desk case that created this RMA.  */  
   "HDCaseNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDCaseRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  The customer associated with this case.  */  
   "CustNum":number,
      /**  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  */  
   "ShipToNum":string,
      /**  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  */  
   "ShpConNum":number,
      /**  The parent Help Desk case number of this case.  */  
   "ParentCase":number,
      /**  The description of the case issue.  */  
   "Description":string,
      /**  A description if the resolution for the case.  */  
   "ResolutionText":string,
      /**  Publishable text of the issue and resolution of the case.  */  
   "PublishedText":string,
      /**  A summary of the issue/resolution of the help desk case.  */  
   "PublishedSummary":string,
      /**  If true this is a Knowledge Base entry.  */  
   "KBEntry":boolean,
      /**  If true this item can be published.  If false this item is for internal use only.  */  
   "PublishedItem":boolean,
      /**  The part that is associated with this Help Desk case.  The part is in the Part table.  */  
   "PartNum":string,
      /**  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  */  
   "SerialNumber":string,
      /**  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  */  
   "QuoteNum":number,
      /**  The order associated with the Help Desk case.  The order is in the OrderHed table.  */  
   "OrderNum":number,
      /**  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  */  
   "CallNum":number,
      /**  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  */  
   "ContractNum":number,
      /**  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  */  
   "WarrantyCode":string,
      /**  The priority of the Help Desk case  */  
   "Priority":number,
      /**  Unique identifier of the task set.  */  
   "TaskSetID":string,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The Currently active milestone task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  */  
   "CaseOwner":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this case is complete.  */  
   "WFComplete":boolean,
      /**  Date which this Help Desk case was created.  Not maintainable by the user.  */  
   "CreatedDate":string,
      /**  UserID who created the Help Desk case.  Not maintainable by the user.  */  
   "CreatedBy":string,
      /**  The time (in milliseconds) that the Help Desk case was created.  */  
   "CreatedTime":number,
      /**  UserID who last updated the Help Desk case.  Not maintainable by the user.  */  
   "LastUpdatedBy":string,
      /**  Date which this Help Desk case was last updated.  Not maintainable by the user.  */  
   "LastUpdatedDate":string,
      /**  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  */  
   "LastUpdatedTime":number,
      /**  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  */  
   "TopicID1":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  */  
   "TopicID2":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  */  
   "TopicID3":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  */  
   "TopicID4":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  */  
   "TopicID5":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  */  
   "TopicID6":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  */  
   "TopicID7":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  */  
   "TopicID8":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  */  
   "TopicID9":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  */  
   "TopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "CaseTopics":string,
      /**  Link to the Marketing Campaign related to this Help Desk case.  */  
   "MktgCampaignID":string,
      /**  Link to the marketing event associated with this Help Desk case.  */  
   "MktgEvntSeq":number,
      /**  Revision number  */  
   "RevisionNum":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  A general quantity field.  */  
   "Quantity":number,
      /**   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  */  
   "QuantityUOM":string,
      /**  Order line number.  */  
   "OrderLine":number,
      /**  The order release number.  */  
   "OrderRelNum":number,
      /**  The quote line number  */  
   "QuoteLine":number,
      /**  Field service call line number  */  
   "CallLine":number,
      /**  The RMA Number.  */  
   "RMANum":number,
      /**  The RMA line number.  */  
   "RMALine":number,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  The invoice line.  */  
   "InvoiceLine":number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Customer Name  */  
   "CustomerName":string,
      /**  Packing slip number that this Service call is linked with.  */  
   "PackNum":number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   "PackLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Case Completed By  */  
   "CompletedBy":string,
      /**  Case Completion Date  */  
   "CompletionDate":string,
      /**  Case Completion Time  */  
   "CompletionTime":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   "DropShipPackSlip":string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   "DropShipPackLine":number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   "VendorNum":number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   "PurPoint":string,
      /**  Related Equip.EquipID.  */  
   "EquipID":string,
      /**  Unique identifier of the primary Employee contact.  */  
   "EmpID":string,
      /**  Unique identifier of the primary Buyer contact.  */  
   "BuyerID":string,
      /**  Unique identifier of the Primary Vendor contact.  */  
   "VendorNumCon":number,
      /**  Unique identifier of the Primary Vendor PP contact.  */  
   "PurPointCon":string,
      /**  Unique identifier of the Primary Vendor contact num.  */  
   "VenConNum":number,
      /**  Contact number.  Unique identifier for the Primary Purchase Point contact record.  */  
   "PurPointConNum":number,
      /**  Unit price for the PartNum.  */  
   "UnitPrice":number,
      /**  Same as UnitPrice except that this field contains the unit price in the case currency.  */  
   "DocUnitPrice":number,
      /**  Unit Price in Report currency 1.  */  
   "Rpt1UnitPrice":number,
      /**  Unit Price in Report currency 2.  */  
   "Rpt2UnitPrice":number,
      /**  Unit Price in Report currency 3.  */  
   "Rpt3UnitPrice":number,
      /**  Extended price. Calculated as Quantity * (UnitPrice / PFactor).  */  
   "ExtPrice":number,
      /**  Same as ExtPrice except that this field contains the extended price in the case currency.  */  
   "DocExtPrice":number,
      /**  Extended Price in Report currency 1.  */  
   "Rp1ExtPrice":number,
      /**  Extended Price in Report currency 2.  */  
   "Rp2ExtPrice":number,
      /**  Extended Price in Report currency 3.  */  
   "Rp3ExtPrice":number,
      /**  Currency Code  */  
   "CurrencyCode":string,
      /**  Rate Type Code  */  
   "RateGrpCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Exchange rate that will be used for this role code entry.  */  
   "ExchangeRate":number,
      /**  Unique identifier of the case type.  */  
   "CaseTypeID":string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   "PONum":number,
      /**  Link to the territory ID.  */  
   "TerritoryID":string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   "POLine":number,
      /**  The type of workflow.  */  
   "WorkflowType":string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   "POPackSlip":string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   "POPackLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  HDCaseStatus  */  
   "HDCaseStatus":string,
      /**  ReqPerConID  */  
   "ReqPerConID":number,
      /**  PerConID  */  
   "PerConID":number,
      /**  Case was initiated from the web  */  
   "WebCase":boolean,
      /**  Comment used for discussion through web  */  
   "WebComment":string,
      /**  Identification Number of related Location Inventory record.  */  
   "IDNum":string,
      /**  Unique ID Num of related Location Inventory record.  */  
   "LocationNum":number,
      /**  Field service contract line number. The service contract line is in the FSContDt table.  */  
   "ContractLine":number,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMCurrentStatus  */  
   "FSMCurrentStatus":string,
      /**  FSMServiceReportID  */  
   "FSMServiceReportID":string,
      /**  FSMNumberOfFollowups  */  
   "FSMNumberOfFollowups":number,
      /**  FSMReceivedBy  */  
   "FSMReceivedBy":string,
      /**  FSMOriginalScheduleDate  */  
   "FSMOriginalScheduleDate":string,
      /**  FSMCompletedDate  */  
   "FSMCompletedDate":string,
      /**  If true the MilestoneSeq field can be modified  */  
   "AllowMilestoneUpdate":boolean,
      /**  Case attribute code list  */  
   "AttrCodeList":string,
      /**  Available PrcConNum values  */  
   "AvailablePrcConNum":string,
      /**  Available AvailablePurPointConNum values  */  
   "AvailablePurPointConNum":string,
      /**  Available ShpConNum values  */  
   "AvailableShpConNum":string,
      /**  a delimited list of Task Sets that can be selected in the TaskSetId field  */  
   "AvailableTaskSets":string,
      /**  Available AvailableVenConNum values  */  
   "AvailableVenConNum":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
      /**  Code of the event. Selected from predefined list of codes.  */  
   "CaseCode":string,
      /**  Indicates the current status of the case.  */  
   "CaseStatus":string,
      /**  List of children linked to the case. Case numbers are separated by commas.  */  
   "ChildCases":string,
      /**  The current milestone in tasks  */  
   "CurrentMilestone":number,
      /**  Description of current milestone.  */  
   "CurrentMilestoneDesc":string,
   "CustCntCorpName":string,
   "CustCntEMail":string,
   "CustCntFaxNum":string,
   "CustCntFirstName":string,
   "CustCntLastName":string,
   "CustCntMiddleName":string,
   "CustCntName":string,
   "CustCntPhoneNum":string,
      /**  If true the customer requires a unique PO on Sales Orders  */  
   "CustomerRequiresPO":boolean,
      /**  String version of the creation time  */  
   "DispCreateTime":string,
      /**  String version of the last update time  */  
   "DispLastUpdateTime":string,
   "DropShip":boolean,
      /**  Evaluation status of the event. Possible values are user defined.  */  
   "EvaluationStatus":string,
      /**  Description of Evaluation Status  */  
   "EvaluationStatusDesc":string,
      /**  String version of HDCaseNum (used for relationships)  */  
   "HDCaseNumString":string,
   "Inactive":boolean,
      /**  Short summary if the issue  */  
   "IssueSummary":string,
      /**  Long issue description  */  
   "IssueText":string,
      /**  Date of the next review.  */  
   "NextReviewDate":string,
      /**  The SalesUM of the part  */  
   "PartSalesUM":string,
   "PPCntEmailAddress":string,
   "PPCntFaxNum":string,
   "PPCntName":string,
   "PPCntPhoneNum":string,
   "PricePerCode":string,
   "PurPointConName":string,
      /**  Requestor Context Link  */  
   "ReqContextLink":string,
      /**  Holds the first ID for the linked record.  */  
   "ReqPerConLnkID1":string,
      /**  Holds the second ID for the linked record. Used with compound key records like ShipTo or PurPoint.  */  
   "ReqPerConLnkID2":string,
      /**  The display name for the link.  */  
   "ReqPerConLnkName":string,
      /**  The SysRowId of the linked PerConLnk.  */  
   "ReqPerConLnkRowID":string,
      /**  Requestor PerCon Name  */  
   "ReqPerConName":string,
      /**  Requestor is primary contact.  */  
   "ReqPrimary":boolean,
      /**  Extended Price in Report currency 1.  */  
   "Rpt1ExtPrice":number,
      /**  Extended Price in Report currency 2.  */  
   "Rpt2ExtPrice":number,
      /**  Extended Price in Report currency 3.  */  
   "Rpt3ExtPrice":number,
   "ShipCntCorpName":string,
   "ShipCntEMail":string,
   "ShipCntFaxNum":string,
   "ShipCntFirstName":string,
   "ShipCntLastName":string,
   "ShipCntMiddleName":string,
   "ShipCntName":string,
   "ShipCntPhoneNum":string,
      /**  Customer Id of the third-party Ship To  */  
   "ShipToCustID":string,
   "ShipToNumName":string,
      /**  TargetUOM  */  
   "TargetUOM":string,
      /**  A flag to indicate the user password was validated  */  
   "TaskCompletePasswordIsValid":boolean,
      /**  Indicates if a the user password should be validated to complete a task  */  
   "TaskCompletePasswordRequired":boolean,
   "VendCntEmailAddress":string,
   "VendCntFaxNum":string,
   "VendCntName":string,
   "VendCntPhoneNum":string,
      /**  The Quote Num that created a case number from the web  */  
   "WebQuoteNum":number,
      /**  The available next milestones for the MilestoneSeq.  */  
   "AvailableMilestones":string,
      /**  Translated description of current FSM status for FSM related cases  */  
   "FSMCurrentStatusDesc":string,
   "BitFlag":number,
   "ActiveTaskIDTaskDescription":string,
   "BuyerIDName":string,
   "CaseOwnerName":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumAllowShipTo3":boolean,
   "DropShipDtlLineDesc":string,
   "EmpIDName":string,
   "EquipIDDescription":string,
   "LastTaskIDTaskDescription":string,
   "LocationInventoryLotNum":string,
   "LocationInventorySerialNumber":string,
   "LocationInventoryIDNum":string,
   "MktgCampaignIDCampDescription":string,
   "MktgEventEvntDescription":string,
   "PackLineLineDesc":string,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "ProjectIDDescription":string,
   "ShipToCustNumName":string,
   "ShipToCustNumCustID":string,
   "TaskSetIDWorkflowType":string,
   "TaskSetIDTaskSetDescription":string,
   "TerritoryIDTerritoryDesc":string,
   "VendorNumConVendorID":string,
   "VendorNumConName":string,
   "WarrantyCodeWarrDescription":string,
   "WFGroupIDDescription":string,
   "WFStageIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDChildCasesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   "HDCaseNum":number,
      /**  The customer associated with this case.  */  
   "CustNum":number,
      /**  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  */  
   "ShipToNum":string,
      /**  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  */  
   "ShpConNum":number,
      /**  The parent Help Desk case number of this case.  */  
   "ParentCase":number,
      /**  The description of the case issue.  */  
   "Description":string,
      /**  A description if the resolution for the case.  */  
   "ResolutionText":string,
      /**  Publishable text of the issue and resolution of the case.  */  
   "PublishedText":string,
      /**  A summary of the issue/resolution of the help desk case.  */  
   "PublishedSummary":string,
      /**  If true this is a Knowledge Base entry.  */  
   "KBEntry":boolean,
      /**  If true this item can be published.  If false this item is for internal use only.  */  
   "PublishedItem":boolean,
      /**  The part that is associated with this Help Desk case.  The part is in the Part table.  */  
   "PartNum":string,
      /**  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  */  
   "SerialNumber":string,
      /**  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  */  
   "QuoteNum":number,
      /**  The order associated with the Help Desk case.  The order is in the OrderHed table.  */  
   "OrderNum":number,
      /**  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  */  
   "CallNum":number,
      /**  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  */  
   "ContractNum":number,
      /**  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  */  
   "WarrantyCode":string,
      /**  The priority of the Help Desk case  */  
   "Priority":number,
      /**  Unique identifier of the task set.  */  
   "TaskSetID":string,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The Currently active milestone task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  */  
   "CaseOwner":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this case is complete.  */  
   "WFComplete":boolean,
      /**  Date which this Help Desk case was created.  Not maintainable by the user.  */  
   "CreatedDate":string,
      /**  UserID who created the Help Desk case.  Not maintainable by the user.  */  
   "CreatedBy":string,
      /**  The time (in milliseconds) that the Help Desk case was created.  */  
   "CreatedTime":number,
      /**  UserID who last updated the Help Desk case.  Not maintainable by the user.  */  
   "LastUpdatedBy":string,
      /**  Date which this Help Desk case was last updated.  Not maintainable by the user.  */  
   "LastUpdatedDate":string,
      /**  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  */  
   "LastUpdatedTime":number,
      /**  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  */  
   "TopicID1":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  */  
   "TopicID2":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  */  
   "TopicID3":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  */  
   "TopicID4":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  */  
   "TopicID5":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  */  
   "TopicID6":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  */  
   "TopicID7":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  */  
   "TopicID8":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  */  
   "TopicID9":string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  */  
   "TopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "CaseTopics":string,
      /**  Link to the Marketing Campaign related to this Help Desk case.  */  
   "MktgCampaignID":string,
      /**  Link to the marketing event associated with this Help Desk case.  */  
   "MktgEvntSeq":number,
      /**  Revision number  */  
   "RevisionNum":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  A general quantity field.  */  
   "Quantity":number,
      /**  Order line number.  */  
   "OrderLine":number,
      /**  The order release number.  */  
   "OrderRelNum":number,
      /**  The quote line number  */  
   "QuoteLine":number,
      /**  Field service call line number  */  
   "CallLine":number,
      /**  The RMA Number.  */  
   "RMANum":number,
      /**  The RMA line number.  */  
   "RMALine":number,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  The invoice line.  */  
   "InvoiceLine":number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Customer Name  */  
   "CustomerName":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CustCntEMail":string,
   "ShipCntEMail":string,
   "BitFlag":number,
   "CaseOwnerName":string,
   "CustomerCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HDContactRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique help desk case number.  */  
   "HDCaseNum":number,
      /**  The SysRowId of the linked PerConLnk.  */  
   "PerConLnkRowID":string,
      /**  Primary contact for each Context type. Only one allowed per context type.  The primary contact for each context type is shown on the detail sheet.  */  
   "Primary":boolean,
      /**  User entered comments.  */  
   "Comment":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Specifies the identifier for the contact who requested the case entry.  */  
   "Requestor":boolean,
   "Name":string,
   "City":string,
   "State":string,
   "Zip":string,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "ContextLink":string,
   "BuyerID":string,
   "BuyerName":string,
   "CustID":string,
   "CustName":string,
   "EmpID":string,
   "EmpName":string,
   "PurPoint":string,
   "PurPointName":string,
   "SalesRepCode":string,
   "SalesRepName":string,
   "ShipToName":string,
   "ShipToNum":string,
   "VendorID":string,
   "VendorName":string,
   "Selected":boolean,
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
      @param retainTask
      @param ds
   */  
export interface ChangedTaskSet_input{
      /**  Retain Task  */  
   retainTask:boolean,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface ChangedTaskSet_output{
parameters : {
      /**  output parameters  */  
   currTaskSeqNum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param vPartNum
   */  
export interface CheckPrePartInfo_input{
      /**  The input-output part number to validate and it gets returned  */  
   vPartNum:string,
}

export interface CheckPrePartInfo_output{
parameters : {
      /**  output parameters  */  
   vPartNum:string,
   vSubPartMsg:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param projectID
      @param relatedTo
      @param jobNum
   */  
export interface CheckProjectID_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  ProjectID to be validated  */  
   projectID:string,
      /**  Entity that will be used to validate the ProjectID  */  
   relatedTo:string,
      /**  Job to be updated with the new ProjectID and ContractID  */  
   jobNum:string,
}

export interface CheckProjectID_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   contractID:string,
   errorMsg:string,
}
}

   /** Required : 
      @param ds
      @param proposedContractNum
   */  
export interface ContractHasLines_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed ContractNum  */  
   proposedContractNum:number,
}

export interface ContractHasLines_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param callCode
      @param ds
   */  
export interface CreateFSCallLine_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The call code to be used for the Field Service call  */  
   callCode:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateFSCallLine_output{
parameters : {
      /**  output parameters  */  
   newCallNum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param callCode
      @param ds
   */  
export interface CreateFSCall_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The call code to be used for the Field Service call  */  
   callCode:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateFSCall_output{
parameters : {
      /**  output parameters  */  
   newCallNum:number,
   validPackingSlip:boolean,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param optionTool
      @param ds
   */  
export interface CreateJob_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  Action Menu Option  */  
   optionTool:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateJob_output{
parameters : {
      /**  output parameters  */  
   newJobNum:string,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param ds
   */  
export interface CreateMaintReq_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateMaintReq_output{
parameters : {
      /**  output parameters  */  
   newReqID:string,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param orderPONum
      @param contractID
      @param ds
   */  
export interface CreateOrderWithLine_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
   orderPONum:string,
      /**  Fill if we want to set any Contract in the Line  */  
   contractID:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateOrderWithLine_output{
parameters : {
      /**  output parameters  */  
   newOrderNum:number,
   errorType:number,
   errorMsg:string,
   orderDtlSysRowID:string,
   smartString:string,
   smartStringProcessed:boolean,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param orderPONum
      @param ds
   */  
export interface CreateOrder_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The PO number to use on the order. (This may be required by the customer)  */  
   orderPONum:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateOrder_output{
parameters : {
      /**  output parameters  */  
   newOrderNum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param contractID
      @param ds
   */  
export interface CreateQuoteWithLine_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  Fill if we want to set any Contract in the Line  */  
   contractID:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateQuoteWithLine_output{
parameters : {
      /**  output parameters  */  
   newQuoteNum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param ds
   */  
export interface CreateQuote_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateQuote_output{
parameters : {
      /**  output parameters  */  
   newQuoteNum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param reasonCode
      @param serialNumber
      @param ds
   */  
export interface CreateRMALine_input{
   helpDeskCaseNum:number,
   reasonCode:string,
   serialNumber:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateRMALine_output{
parameters : {
      /**  output parameters  */  
   newRMANum:number,
   SNErrorMsg:string,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param ds
   */  
export interface CreateRMAUpdConNum_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateRMAUpdConNum_output{
parameters : {
      /**  output parameters  */  
   newRMANum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param ds
   */  
export interface CreateRMA_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface CreateRMA_output{
parameters : {
      /**  output parameters  */  
   newRMANum:number,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param hdCaseNum
   */  
export interface DeleteByID_input{
   hdCaseNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param helpDeskCaseNum
      @param callNum
   */  
export interface DeleteFSCallhdLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The linked fscall number  */  
   callNum:number,
}

export interface DeleteFSCallhdLink_output{
}

   /** Required : 
      @param helpDeskCaseNum
   */  
export interface DeleteHDCaseExternalLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
}

export interface DeleteHDCaseExternalLink_output{
}

   /** Required : 
      @param hdChildCaseNum
   */  
export interface DeleteHDChildCaseLink_input{
      /**  The Help Desk case number to use as a source  */  
   hdChildCaseNum:number,
}

export interface DeleteHDChildCaseLink_output{
}

   /** Required : 
      @param helpDeskCaseNum
      @param jobNum
   */  
export interface DeleteJobHeadLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The linked job number  */  
   jobNum:string,
}

export interface DeleteJobHeadLink_output{
}

   /** Required : 
      @param helpDeskCaseNum
      @param reqID
   */  
export interface DeleteMaintReqLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The linked maint req number  */  
   reqID:string,
}

export interface DeleteMaintReqLink_output{
}

   /** Required : 
      @param helpDeskCaseNum
      @param orderNum
   */  
export interface DeleteOrderHedLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The linked quote number  */  
   orderNum:number,
}

export interface DeleteOrderHedLink_output{
}

   /** Required : 
      @param helpDeskCaseNum
      @param quoteNum
   */  
export interface DeleteQuoteHedLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The linked quote number  */  
   quoteNum:number,
}

export interface DeleteQuoteHedLink_output{
}

   /** Required : 
      @param helpDeskCaseNum
      @param rmaNum
   */  
export interface DeleteRMAHeadLink_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
      /**  The linked RMA number  */  
   rmaNum:number,
}

export interface DeleteRMAHeadLink_output{
}

export interface Erp_Tablesets_HDCaseAttchRow{
   Company:string,
   HDCaseNum:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseFSCallRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  The help desk case that created this service call.  */  
   HDCaseNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseJobRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseLinkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  If true this is an external link that was manually entered.  Internal links will refer to other database records.  */  
   ExternalLink:boolean,
      /**  Identifies the master file to which the link is related.  If an external link this will be blank.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record.  */  
   Key1:string,
      /**  2nd component of the foreign key to the related master record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  */  
   Key3:string,
      /**  4th component of the foreign key to the related master record.  */  
   Key4:string,
      /**  5th component of the foreign key to the related master record.  */  
   Key5:string,
      /**  Description of the link contents.  */  
   Description:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  The customer associated with this case.  */  
   CustNum:number,
      /**  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  */  
   ShipToNum:string,
      /**  The parent Help Desk case number of this case.  */  
   ParentCase:number,
      /**  The description of the case issue.  */  
   Description:string,
      /**  A description if the resolution for the case.  */  
   ResolutionText:string,
      /**  Publishable text of the issue and resolution of the case.  */  
   PublishedText:string,
      /**  A summary of the issue/resolution of the help desk case.  */  
   PublishedSummary:string,
      /**  If true this is a Knowledge Base entry.  */  
   KBEntry:boolean,
      /**  If true this item can be published.  If false this item is for internal use only.  */  
   PublishedItem:boolean,
      /**  The part that is associated with this Help Desk case.  The part is in the Part table.  */  
   PartNum:string,
      /**  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  */  
   SerialNumber:string,
      /**  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  */  
   QuoteNum:number,
      /**  The order associated with the Help Desk case.  The order is in the OrderHed table.  */  
   OrderNum:number,
      /**  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  */  
   CaseOwner:string,
      /**  Date which this Help Desk case was created.  Not maintainable by the user.  */  
   CreatedDate:string,
      /**  UserID who created the Help Desk case.  Not maintainable by the user.  */  
   CreatedBy:string,
      /**  The time (in milliseconds) that the Help Desk case was created.  */  
   CreatedTime:number,
      /**  UserID who last updated the Help Desk case.  Not maintainable by the user.  */  
   LastUpdatedBy:string,
      /**  Date which this Help Desk case was last updated.  Not maintainable by the user.  */  
   LastUpdatedDate:string,
      /**  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  */  
   LastUpdatedTime:number,
      /**  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  */  
   TopicID1:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  */  
   TopicID2:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  */  
   TopicID3:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  */  
   TopicID4:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  */  
   TopicID5:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  */  
   TopicID6:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  */  
   TopicID7:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  */  
   TopicID8:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  */  
   TopicID9:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  */  
   TopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   CaseTopics:string,
      /**  Revision number  */  
   RevisionNum:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  A general quantity field.  */  
   Quantity:number,
      /**   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  */  
   QuantityUOM:string,
      /**  The quote line number  */  
   QuoteLine:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  The invoice line.  */  
   InvoiceLine:number,
      /**  Customer Name  */  
   CustomerName:string,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Case Completed By  */  
   CompletedBy:string,
      /**  Case Completion Date  */  
   CompletionDate:string,
      /**  Case Completion Time  */  
   CompletionTime:number,
      /**  Unit price for the PartNum.  */  
   UnitPrice:number,
      /**  Same as UnitPrice except that this field contains the unit price in the case currency.  */  
   DocUnitPrice:number,
      /**  Extended Price in Report currency 1.  */  
   Rp1ExtPrice:number,
      /**  Extended Price in Report currency 2.  */  
   Rp2ExtPrice:number,
      /**  Unique identifier of the case type.  */  
   CaseTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Case attribute code list  */  
   AttrCodeList:string,
      /**  Short summary if the issue  */  
   IssueSummary:string,
      /**  Long issue description  */  
   IssueText:string,
      /**  String version of the creation time  */  
   DispCreateTime:string,
      /**  String version of the last update time  */  
   DispLastUpdateTime:string,
      /**  Name  */  
   CaseOwnerName:string,
   CaseCode:string,
   NextReviewDate:string,
   EvaluationStatus:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   ShipToNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseListTableset{
   HDCaseList:Erp_Tablesets_HDCaseListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_HDCaseMaintReqRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  */  
   ReqID:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseOrderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   OrderNum:number,
      /**  The help desk case that created this order.  */  
   HDCaseNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Project_c:string,
   OriginalOrderNo_c:number,
   MASFlag_c:boolean,
   Estimate_c:boolean,
   ShipOrderComplete_c:boolean,
   ProjectID_c:string,
   PhaseID_c:string,
   SalesCatID__c:string,
   TaxCatID_c:string,
   MfgOrder_c:boolean,
}

export interface Erp_Tablesets_HDCaseQuoteRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  */  
   QuoteNum:number,
      /**  The help desk case that created this quote.  */  
   HDCaseNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseRMARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   RMANum:number,
      /**  The help desk case that created this RMA.  */  
   HDCaseNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  The customer associated with this case.  */  
   CustNum:number,
      /**  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  */  
   ShipToNum:string,
      /**  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  */  
   ShpConNum:number,
      /**  The parent Help Desk case number of this case.  */  
   ParentCase:number,
      /**  The description of the case issue.  */  
   Description:string,
      /**  A description if the resolution for the case.  */  
   ResolutionText:string,
      /**  Publishable text of the issue and resolution of the case.  */  
   PublishedText:string,
      /**  A summary of the issue/resolution of the help desk case.  */  
   PublishedSummary:string,
      /**  If true this is a Knowledge Base entry.  */  
   KBEntry:boolean,
      /**  If true this item can be published.  If false this item is for internal use only.  */  
   PublishedItem:boolean,
      /**  The part that is associated with this Help Desk case.  The part is in the Part table.  */  
   PartNum:string,
      /**  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  */  
   SerialNumber:string,
      /**  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  */  
   QuoteNum:number,
      /**  The order associated with the Help Desk case.  The order is in the OrderHed table.  */  
   OrderNum:number,
      /**  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  */  
   CallNum:number,
      /**  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  */  
   ContractNum:number,
      /**  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  */  
   WarrantyCode:string,
      /**  The priority of the Help Desk case  */  
   Priority:number,
      /**  Unique identifier of the task set.  */  
   TaskSetID:string,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The Currently active milestone task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  */  
   CaseOwner:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this case is complete.  */  
   WFComplete:boolean,
      /**  Date which this Help Desk case was created.  Not maintainable by the user.  */  
   CreatedDate:string,
      /**  UserID who created the Help Desk case.  Not maintainable by the user.  */  
   CreatedBy:string,
      /**  The time (in milliseconds) that the Help Desk case was created.  */  
   CreatedTime:number,
      /**  UserID who last updated the Help Desk case.  Not maintainable by the user.  */  
   LastUpdatedBy:string,
      /**  Date which this Help Desk case was last updated.  Not maintainable by the user.  */  
   LastUpdatedDate:string,
      /**  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  */  
   LastUpdatedTime:number,
      /**  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  */  
   TopicID1:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  */  
   TopicID2:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  */  
   TopicID3:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  */  
   TopicID4:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  */  
   TopicID5:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  */  
   TopicID6:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  */  
   TopicID7:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  */  
   TopicID8:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  */  
   TopicID9:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  */  
   TopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   CaseTopics:string,
      /**  Link to the Marketing Campaign related to this Help Desk case.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this Help Desk case.  */  
   MktgEvntSeq:number,
      /**  Revision number  */  
   RevisionNum:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  A general quantity field.  */  
   Quantity:number,
      /**   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  */  
   QuantityUOM:string,
      /**  Order line number.  */  
   OrderLine:number,
      /**  The order release number.  */  
   OrderRelNum:number,
      /**  The quote line number  */  
   QuoteLine:number,
      /**  Field service call line number  */  
   CallLine:number,
      /**  The RMA Number.  */  
   RMANum:number,
      /**  The RMA line number.  */  
   RMALine:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  The invoice line.  */  
   InvoiceLine:number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Customer Name  */  
   CustomerName:string,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Case Completed By  */  
   CompletedBy:string,
      /**  Case Completion Date  */  
   CompletionDate:string,
      /**  Case Completion Time  */  
   CompletionTime:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   DropShipPackSlip:string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   DropShipPackLine:number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   VendorNum:number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   PurPoint:string,
      /**  Related Equip.EquipID.  */  
   EquipID:string,
      /**  Unique identifier of the primary Employee contact.  */  
   EmpID:string,
      /**  Unique identifier of the primary Buyer contact.  */  
   BuyerID:string,
      /**  Unique identifier of the Primary Vendor contact.  */  
   VendorNumCon:number,
      /**  Unique identifier of the Primary Vendor PP contact.  */  
   PurPointCon:string,
      /**  Unique identifier of the Primary Vendor contact num.  */  
   VenConNum:number,
      /**  Contact number.  Unique identifier for the Primary Purchase Point contact record.  */  
   PurPointConNum:number,
      /**  Unit price for the PartNum.  */  
   UnitPrice:number,
      /**  Same as UnitPrice except that this field contains the unit price in the case currency.  */  
   DocUnitPrice:number,
      /**  Unit Price in Report currency 1.  */  
   Rpt1UnitPrice:number,
      /**  Unit Price in Report currency 2.  */  
   Rpt2UnitPrice:number,
      /**  Unit Price in Report currency 3.  */  
   Rpt3UnitPrice:number,
      /**  Extended price. Calculated as Quantity * (UnitPrice / PFactor).  */  
   ExtPrice:number,
      /**  Same as ExtPrice except that this field contains the extended price in the case currency.  */  
   DocExtPrice:number,
      /**  Extended Price in Report currency 1.  */  
   Rp1ExtPrice:number,
      /**  Extended Price in Report currency 2.  */  
   Rp2ExtPrice:number,
      /**  Extended Price in Report currency 3.  */  
   Rp3ExtPrice:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Rate Type Code  */  
   RateGrpCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Exchange rate that will be used for this role code entry.  */  
   ExchangeRate:number,
      /**  Unique identifier of the case type.  */  
   CaseTypeID:string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   PONum:number,
      /**  Link to the territory ID.  */  
   TerritoryID:string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   POLine:number,
      /**  The type of workflow.  */  
   WorkflowType:string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   POPackSlip:string,
      /**  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  */  
   POPackLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  HDCaseStatus  */  
   HDCaseStatus:string,
      /**  ReqPerConID  */  
   ReqPerConID:number,
      /**  PerConID  */  
   PerConID:number,
      /**  Case was initiated from the web  */  
   WebCase:boolean,
      /**  Comment used for discussion through web  */  
   WebComment:string,
      /**  Identification Number of related Location Inventory record.  */  
   IDNum:string,
      /**  Unique ID Num of related Location Inventory record.  */  
   LocationNum:number,
      /**  Field service contract line number. The service contract line is in the FSContDt table.  */  
   ContractLine:number,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMCurrentStatus  */  
   FSMCurrentStatus:string,
      /**  FSMServiceReportID  */  
   FSMServiceReportID:string,
      /**  FSMNumberOfFollowups  */  
   FSMNumberOfFollowups:number,
      /**  FSMReceivedBy  */  
   FSMReceivedBy:string,
      /**  FSMOriginalScheduleDate  */  
   FSMOriginalScheduleDate:string,
      /**  FSMCompletedDate  */  
   FSMCompletedDate:string,
      /**  If true the MilestoneSeq field can be modified  */  
   AllowMilestoneUpdate:boolean,
      /**  Case attribute code list  */  
   AttrCodeList:string,
      /**  Available PrcConNum values  */  
   AvailablePrcConNum:string,
      /**  Available AvailablePurPointConNum values  */  
   AvailablePurPointConNum:string,
      /**  Available ShpConNum values  */  
   AvailableShpConNum:string,
      /**  a delimited list of Task Sets that can be selected in the TaskSetId field  */  
   AvailableTaskSets:string,
      /**  Available AvailableVenConNum values  */  
   AvailableVenConNum:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Code of the event. Selected from predefined list of codes.  */  
   CaseCode:string,
      /**  Indicates the current status of the case.  */  
   CaseStatus:string,
      /**  List of children linked to the case. Case numbers are separated by commas.  */  
   ChildCases:string,
      /**  The current milestone in tasks  */  
   CurrentMilestone:number,
      /**  Description of current milestone.  */  
   CurrentMilestoneDesc:string,
   CustCntCorpName:string,
   CustCntEMail:string,
   CustCntFaxNum:string,
   CustCntFirstName:string,
   CustCntLastName:string,
   CustCntMiddleName:string,
   CustCntName:string,
   CustCntPhoneNum:string,
      /**  If true the customer requires a unique PO on Sales Orders  */  
   CustomerRequiresPO:boolean,
      /**  String version of the creation time  */  
   DispCreateTime:string,
      /**  String version of the last update time  */  
   DispLastUpdateTime:string,
   DropShip:boolean,
      /**  Evaluation status of the event. Possible values are user defined.  */  
   EvaluationStatus:string,
      /**  Description of Evaluation Status  */  
   EvaluationStatusDesc:string,
      /**  String version of HDCaseNum (used for relationships)  */  
   HDCaseNumString:string,
   Inactive:boolean,
      /**  Short summary if the issue  */  
   IssueSummary:string,
      /**  Long issue description  */  
   IssueText:string,
      /**  Date of the next review.  */  
   NextReviewDate:string,
      /**  The SalesUM of the part  */  
   PartSalesUM:string,
   PPCntEmailAddress:string,
   PPCntFaxNum:string,
   PPCntName:string,
   PPCntPhoneNum:string,
   PricePerCode:string,
   PurPointConName:string,
      /**  Requestor Context Link  */  
   ReqContextLink:string,
      /**  Holds the first ID for the linked record.  */  
   ReqPerConLnkID1:string,
      /**  Holds the second ID for the linked record. Used with compound key records like ShipTo or PurPoint.  */  
   ReqPerConLnkID2:string,
      /**  The display name for the link.  */  
   ReqPerConLnkName:string,
      /**  The SysRowId of the linked PerConLnk.  */  
   ReqPerConLnkRowID:string,
      /**  Requestor PerCon Name  */  
   ReqPerConName:string,
      /**  Requestor is primary contact.  */  
   ReqPrimary:boolean,
      /**  Extended Price in Report currency 1.  */  
   Rpt1ExtPrice:number,
      /**  Extended Price in Report currency 2.  */  
   Rpt2ExtPrice:number,
      /**  Extended Price in Report currency 3.  */  
   Rpt3ExtPrice:number,
   ShipCntCorpName:string,
   ShipCntEMail:string,
   ShipCntFaxNum:string,
   ShipCntFirstName:string,
   ShipCntLastName:string,
   ShipCntMiddleName:string,
   ShipCntName:string,
   ShipCntPhoneNum:string,
      /**  Customer Id of the third-party Ship To  */  
   ShipToCustID:string,
   ShipToNumName:string,
      /**  TargetUOM  */  
   TargetUOM:string,
      /**  A flag to indicate the user password was validated  */  
   TaskCompletePasswordIsValid:boolean,
      /**  Indicates if a the user password should be validated to complete a task  */  
   TaskCompletePasswordRequired:boolean,
   VendCntEmailAddress:string,
   VendCntFaxNum:string,
   VendCntName:string,
   VendCntPhoneNum:string,
      /**  The Quote Num that created a case number from the web  */  
   WebQuoteNum:number,
      /**  The available next milestones for the MilestoneSeq.  */  
   AvailableMilestones:string,
      /**  Translated description of current FSM status for FSM related cases  */  
   FSMCurrentStatusDesc:string,
   BitFlag:number,
   ActiveTaskIDTaskDescription:string,
   BuyerIDName:string,
   CaseOwnerName:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumAllowShipTo3:boolean,
   DropShipDtlLineDesc:string,
   EmpIDName:string,
   EquipIDDescription:string,
   LastTaskIDTaskDescription:string,
   LocationInventoryLotNum:string,
   LocationInventorySerialNumber:string,
   LocationInventoryIDNum:string,
   MktgCampaignIDCampDescription:string,
   MktgEventEvntDescription:string,
   PackLineLineDesc:string,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   ProjectIDDescription:string,
   ShipToCustNumName:string,
   ShipToCustNumCustID:string,
   TaskSetIDWorkflowType:string,
   TaskSetIDTaskSetDescription:string,
   TerritoryIDTerritoryDesc:string,
   VendorNumConVendorID:string,
   VendorNumConName:string,
   WarrantyCodeWarrDescription:string,
   WFGroupIDDescription:string,
   WFStageIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseSearchRow{
      /**  The mode to use for searching  */  
   SearchMode:string,
      /**  Search only published items  */  
   SearchPublishedItemsOnly:boolean,
      /**  The completion status of the workflow  */  
   WorkflowCompletionStatus:string,
      /**  The Customer ID  */  
   CustID:string,
      /**  Customer Name  */  
   CustomerName:string,
      /**  Ship to Number  */  
   ShipToNum:string,
      /**  Ship To Contact Number  */  
   ShpConNum:number,
      /**  Bill To Contact Number  */  
   PrcConNum:number,
      /**  Keywords to use in text searching  */  
   TextKeywords:string,
      /**  Use TextKeywords to search issue text  */  
   SearchIssueText:boolean,
      /**  Use TextKeywords to search resolution text  */  
   SearchResolutionText:boolean,
      /**  Use TextKeywords to search published text  */  
   SearchPublishedText:boolean,
      /**  The part number  */  
   PartNum:string,
      /**  The part revision number  */  
   RevisionNum:string,
      /**  Part description.  If blank this will be ignored.  */  
   PartDescription:string,
      /**  The serial number.   If blank this will be ignored.  */  
   SerialNumber:string,
      /**  The quote number.   If 0 this will be ignored.  */  
   QuoteNum:number,
      /**  The quote line.   If 0 this will be ignored.  */  
   QuoteLine:number,
      /**  The order number.   If 0 this will be ignored.  */  
   OrderNum:number,
      /**  The order line number.   If 0 this will be ignored.  */  
   OrderLine:number,
      /**  The order release number.   If 0 this will be ignored.  */  
   OrderRelNum:number,
      /**  Field service call number  */  
   CallNum:number,
      /**  Field service call line number.   If 0 this will be ignored.  */  
   CallLine:number,
      /**  The RMA number.   If 0 this will be ignored.  */  
   RMANum:number,
      /**  The RMA line number.   If 0 this will be ignored.  */  
   RMALine:number,
      /**  The invoice number.   If 0 this will be ignored.  */  
   InvoiceNum:number,
      /**  The invoice line number.   If 0 this will be ignored.  */  
   InvoiceLine:number,
      /**  The contract number.   If 0 this will be ignored.  */  
   ContractNum:number,
      /**  The warrancy code. If blank this will be ignored.  */  
   WarrantyCode:string,
      /**  The help desk priority. If 0 this will be ignored.  */  
   Priority:number,
      /**  Case topics. If blank this will be ignored.  */  
   CaseTopics:string,
      /**  The marketing campaign Id. If blank this will be ignored.  */  
   MktgCampaignID:string,
      /**  The marketing event sequence. If 0 this will be ignored.  */  
   MktgEvntSeq:number,
      /**  The project Id. If blank this will be ignored.  */  
   ProjectID:string,
      /**  The case owner. If blank this will be ignored.  */  
   CaseOwner:string,
      /**  The help desk workflow group Id. If blank this will be ignored.  */  
   WFGroupID:string,
      /**  The current workflow stage. If blank this will be ignored.  */  
   CurrentWFStageID:string,
      /**  Active task Id. If blank this will be ignored.  */  
   ActiveTaskID:string,
      /**  The starting date for a range used to search created date. If null this will be ignored.  */  
   CreatedDateFrom:string,
      /**  The ending date for a range used to search created date. If null this will be ignored.  */  
   CreatedDateTo:string,
      /**  The user that created the case. If blank this will be ignored.  */  
   CreatedBy:string,
      /**  The starting date for a range used to search last updated date. If null this will be ignored.  */  
   LastUpdatedFrom:string,
      /**  The ending date for a range used to search last updated date. If null this will be ignored.  */  
   LastUpdatedTo:string,
      /**  The user that last updated the case. If blank this will be ignored.  */  
   LastUpdatedBy:string,
   Company:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Available ShpConNum values  */  
   AvailableShpConNum:string,
      /**  Available PrcConNum values  */  
   AvailablePrcConNum:string,
   TopicID1:string,
   TopicID2:string,
   TopicID3:string,
   TopicID4:string,
   TopicID5:string,
   TopicID6:string,
   TopicID7:string,
   TopicID8:string,
   TopicID9:string,
   TopicID10:string,
   ShipToName:string,
   EquipID:string,
   EquipIDDescription:string,
   BuyerID:string,
   EmpID:string,
   PurPointCon:string,
   VendorNumCon:number,
   VenConNum:number,
   VendorName:string,
   BuyerIDName:string,
   EmpIDName:string,
   PurPointConNum:number,
      /**  Available VenConNum values  */  
   AvailableVenConNum:string,
      /**  Available PurPointConNum values  */  
   AvailablePurPointConNum:string,
   PurPointConName:string,
   VendorNumConVendorID:string,
   VendorNumConName:string,
   WorkflowType:string,
   RelatedTo:boolean,
   LinkedTo:boolean,
   JobNum:string,
   ReqID:string,
      /**  Delimited list with valid topics.  */  
   TopicID10List:string,
      /**  Delimited list with valid topics.  */  
   TopicID2List:string,
      /**  Delimited list with valid topics.  */  
   TopicID3List:string,
      /**  Delimited list with valid topics.  */  
   TopicID4List:string,
      /**  Delimited list with valid topics.  */  
   TopicID5List:string,
      /**  Delimited list with valid topics.  */  
   TopicID6List:string,
      /**  Delimited list with valid topics.  */  
   TopicID7List:string,
      /**  Delimited list with valid topics.  */  
   TopicID8List:string,
      /**  Delimited list with valid topics.  */  
   TopicID9List:string,
      /**  Delimited list with valid topics.  */  
   TopicID1List:string,
      /**  Field service contract line number. If 0 this will be ignored.  */  
   ContractLine:number,
   SysRowID:string,
   ActiveTaskIDTaskDescription:string,
   CaseOwnerName:string,
   CustIDCustID:string,
   CustIDBTName:string,
   CustIDName:string,
   MktgCampCampDescription:string,
   MktgEvntEvntDescription:string,
   ProjectIDDescription:string,
   WarrantyCodeWarrDescription:string,
   WFGroupDescription:string,
   WFStageDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDCaseSearchTableset{
   HDCaseSearch:Erp_Tablesets_HDCaseSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_HDChildCasesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique help desk case number.  This number is system generated when the help desk case is created.  */  
   HDCaseNum:number,
      /**  The customer associated with this case.  */  
   CustNum:number,
      /**  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  */  
   ShipToNum:string,
      /**  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  */  
   ShpConNum:number,
      /**  The parent Help Desk case number of this case.  */  
   ParentCase:number,
      /**  The description of the case issue.  */  
   Description:string,
      /**  A description if the resolution for the case.  */  
   ResolutionText:string,
      /**  Publishable text of the issue and resolution of the case.  */  
   PublishedText:string,
      /**  A summary of the issue/resolution of the help desk case.  */  
   PublishedSummary:string,
      /**  If true this is a Knowledge Base entry.  */  
   KBEntry:boolean,
      /**  If true this item can be published.  If false this item is for internal use only.  */  
   PublishedItem:boolean,
      /**  The part that is associated with this Help Desk case.  The part is in the Part table.  */  
   PartNum:string,
      /**  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  */  
   SerialNumber:string,
      /**  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  */  
   QuoteNum:number,
      /**  The order associated with the Help Desk case.  The order is in the OrderHed table.  */  
   OrderNum:number,
      /**  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  */  
   CallNum:number,
      /**  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  */  
   ContractNum:number,
      /**  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  */  
   WarrantyCode:string,
      /**  The priority of the Help Desk case  */  
   Priority:number,
      /**  Unique identifier of the task set.  */  
   TaskSetID:string,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The Currently active milestone task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  */  
   CaseOwner:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this case is complete.  */  
   WFComplete:boolean,
      /**  Date which this Help Desk case was created.  Not maintainable by the user.  */  
   CreatedDate:string,
      /**  UserID who created the Help Desk case.  Not maintainable by the user.  */  
   CreatedBy:string,
      /**  The time (in milliseconds) that the Help Desk case was created.  */  
   CreatedTime:number,
      /**  UserID who last updated the Help Desk case.  Not maintainable by the user.  */  
   LastUpdatedBy:string,
      /**  Date which this Help Desk case was last updated.  Not maintainable by the user.  */  
   LastUpdatedDate:string,
      /**  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  */  
   LastUpdatedTime:number,
      /**  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  */  
   TopicID1:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  */  
   TopicID2:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  */  
   TopicID3:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  */  
   TopicID4:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  */  
   TopicID5:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  */  
   TopicID6:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  */  
   TopicID7:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  */  
   TopicID8:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  */  
   TopicID9:string,
      /**  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  */  
   TopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   CaseTopics:string,
      /**  Link to the Marketing Campaign related to this Help Desk case.  */  
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this Help Desk case.  */  
   MktgEvntSeq:number,
      /**  Revision number  */  
   RevisionNum:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  A general quantity field.  */  
   Quantity:number,
      /**  Order line number.  */  
   OrderLine:number,
      /**  The order release number.  */  
   OrderRelNum:number,
      /**  The quote line number  */  
   QuoteLine:number,
      /**  Field service call line number  */  
   CallLine:number,
      /**  The RMA Number.  */  
   RMANum:number,
      /**  The RMA line number.  */  
   RMALine:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  The invoice line.  */  
   InvoiceLine:number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Customer Name  */  
   CustomerName:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustCntEMail:string,
   ShipCntEMail:string,
   BitFlag:number,
   CaseOwnerName:string,
   CustomerCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HDContactRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique help desk case number.  */  
   HDCaseNum:number,
      /**  The SysRowId of the linked PerConLnk.  */  
   PerConLnkRowID:string,
      /**  Primary contact for each Context type. Only one allowed per context type.  The primary contact for each context type is shown on the detail sheet.  */  
   Primary:boolean,
      /**  User entered comments.  */  
   Comment:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Specifies the identifier for the contact who requested the case entry.  */  
   Requestor:boolean,
   Name:string,
   City:string,
   State:string,
   Zip:string,
   Address1:string,
   Address2:string,
   Address3:string,
   ContextLink:string,
   BuyerID:string,
   BuyerName:string,
   CustID:string,
   CustName:string,
   EmpID:string,
   EmpName:string,
   PurPoint:string,
   PurPointName:string,
   SalesRepCode:string,
   SalesRepName:string,
   ShipToName:string,
   ShipToNum:string,
   VendorID:string,
   VendorName:string,
   Selected:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HelpDeskContTrkRow{
      /**  The name of the current company.  */  
   Company:string,
   CustNum:number,
      /**  The customer ID.  */  
   CustID:string,
      /**  The full name for customer.  */  
   CustomerName:string,
   ShipToNum:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
      /**  Specifies the unique case number.  */  
   HDCaseNum:number,
      /**  Specifies the case owner.  */  
   CaseOwner:string,
      /**  Specifies the current milestone.  */  
   CurrentMilestone:number,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Specifies an unique number of the call.  */  
   CallNum:number,
      /**  Specifies an unique number of Contract.  */  
   ContractNum:number,
      /**  Specifies the description of a Part selected.  */  
   PartDescription:string,
      /**  Specifies the Part revision number.  */  
   RevisionNum:string,
      /**  Long issue description.  */  
   IssueText:string,
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HelpDeskContTrkTableset{
   HelpDeskContTrk:Erp_Tablesets_HelpDeskContTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_HelpDeskTableset{
   HDCase:Erp_Tablesets_HDCaseRow[],
   HDCaseAttch:Erp_Tablesets_HDCaseAttchRow[],
   HDCaseFSCall:Erp_Tablesets_HDCaseFSCallRow[],
   HDCaseJob:Erp_Tablesets_HDCaseJobRow[],
   HDCaseLink:Erp_Tablesets_HDCaseLinkRow[],
   HDCaseOrder:Erp_Tablesets_HDCaseOrderRow[],
   HDCaseQuote:Erp_Tablesets_HDCaseQuoteRow[],
   HDCaseRMA:Erp_Tablesets_HDCaseRMARow[],
   HDChildCases:Erp_Tablesets_HDChildCasesRow[],
   HDContact:Erp_Tablesets_HDContactRow[],
   HDCaseMaintReq:Erp_Tablesets_HDCaseMaintReqRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtHelpDeskTableset{
   HDCase:Erp_Tablesets_HDCaseRow[],
   HDCaseAttch:Erp_Tablesets_HDCaseAttchRow[],
   HDCaseFSCall:Erp_Tablesets_HDCaseFSCallRow[],
   HDCaseJob:Erp_Tablesets_HDCaseJobRow[],
   HDCaseLink:Erp_Tablesets_HDCaseLinkRow[],
   HDCaseOrder:Erp_Tablesets_HDCaseOrderRow[],
   HDCaseQuote:Erp_Tablesets_HDCaseQuoteRow[],
   HDCaseRMA:Erp_Tablesets_HDCaseRMARow[],
   HDChildCases:Erp_Tablesets_HDChildCasesRow[],
   HDContact:Erp_Tablesets_HDContactRow[],
   HDCaseMaintReq:Erp_Tablesets_HDCaseMaintReqRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  PartNum  */  
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetAvailTaskSets_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetAvailTaskSets_output{
parameters : {
      /**  output parameters  */  
   whereClause:string,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param hdCaseNum
   */  
export interface GetByID_input{
   hdCaseNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_HelpDeskTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_HelpDeskTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_HelpDeskTableset[],
}

   /** Required : 
      @param topicID
      @param ds
   */  
export interface GetChildTopicsDS_input{
      /**  The Topic ID to be populated.  */  
   topicID:string,
   ds:Erp_Tablesets_HDCaseSearchTableset[],
}

export interface GetChildTopicsDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param parentTopicID
   */  
export interface GetChildTopics_input{
      /**  The parent topic or string.Empty for top level topics.  */  
   parentTopicID:string,
}

export interface GetChildTopics_output{
parameters : {
      /**  output parameters  */  
   childList:string,
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
   returnObj:Erp_Tablesets_HDCaseListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param hdCaseNum
   */  
export interface GetNewHDCaseAttch_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
   hdCaseNum:number,
}

export interface GetNewHDCaseAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseFSCall_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCaseFSCall_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseJob_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCaseJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param hdCaseNum
      @param externalLink
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
   */  
export interface GetNewHDCaseLink_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
   hdCaseNum:number,
   externalLink:boolean,
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
}

export interface GetNewHDCaseLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseMaintReq_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCaseMaintReq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseOrder_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCaseOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseQuote_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCaseQuote_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseRMA_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCaseRMA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseSearchDS_input{
   ds:Erp_Tablesets_HDCaseSearchTableset[],
}

export interface GetNewHDCaseSearchDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCaseSearch_input{
   ds:Erp_Tablesets_HDCaseSearchTableset[],
}

export interface GetNewHDCaseSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDCase_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDCase_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewHDChildCases_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface GetNewHDChildCases_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param hdCaseNum
   */  
export interface GetNewHDContact_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
   hdCaseNum:number,
}

export interface GetNewHDContact_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
      /**  Row Type  */  
   ipRowType:string,
      /**  Row ID  */  
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param whereClauseHDCase
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Where clause for HDCase table.  */  
   whereClauseHDCase:string,
      /**  The contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_HelpDeskContTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseHDCase
      @param whereClauseHDCaseAttch
      @param whereClauseHDCaseFSCall
      @param whereClauseHDCaseJob
      @param whereClauseHDCaseLink
      @param whereClauseHDCaseOrder
      @param whereClauseHDCaseQuote
      @param whereClauseHDCaseRMA
      @param whereClauseHDChildCases
      @param whereClauseHDContact
      @param whereClauseHDCaseMaintReq
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseHDCase:string,
   whereClauseHDCaseAttch:string,
   whereClauseHDCaseFSCall:string,
   whereClauseHDCaseJob:string,
   whereClauseHDCaseLink:string,
   whereClauseHDCaseOrder:string,
   whereClauseHDCaseQuote:string,
   whereClauseHDCaseRMA:string,
   whereClauseHDChildCases:string,
   whereClauseHDContact:string,
   whereClauseHDCaseMaintReq:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_HelpDeskTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param proposedSerialNumber
   */  
export interface GetSerialNoPartNum_input{
      /**  The proposed SerialNumber  */  
   proposedSerialNumber:string,
}

export interface GetSerialNoPartNum_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   PartNumFromSerial:string,
}
}

   /** Required : 
      @param ds
   */  
export interface HelpDeskSearch_input{
   ds:Erp_Tablesets_HDCaseSearchTableset[],
}

export interface HelpDeskSearch_output{
   returnObj:Erp_Tablesets_HDCaseListTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
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
      @param proposedAttrCodeList
   */  
export interface OnChangeAttrCodeList_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed AttrCodeList  */  
   proposedAttrCodeList:string,
}

export interface OnChangeAttrCodeList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param buyerID
      @param ds
   */  
export interface OnChangeBuyerID_input{
      /**  BuyerID  */  
   buyerID:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeBuyerID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCallLine
      @param getDefaults
   */  
export interface OnChangeCallLine_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed CallLine  */  
   proposedCallLine:number,
      /**  Assign any fields related to CallLine  */  
   getDefaults:boolean,
}

export interface OnChangeCallLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCallNum
      @param getDefaults
   */  
export interface OnChangeCallNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed CallNum  */  
   proposedCallNum:number,
      /**  Assign any fields related to CallNum  */  
   getDefaults:boolean,
}

export interface OnChangeCallNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCaseOwner
   */  
export interface OnChangeCaseOwner_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed CaseOwner  */  
   proposedCaseOwner:string,
}

export interface OnChangeCaseOwner_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCaseTopics
   */  
export interface OnChangeCaseTopics_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed case topics delimited with spaces  */  
   proposedCaseTopics:string,
}

export interface OnChangeCaseTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCaseTypeID
   */  
export interface OnChangeCaseTypeID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed CaseTypeID  */  
   proposedCaseTypeID:string,
}

export interface OnChangeCaseTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedContractLine
      @param getDefaults
   */  
export interface OnChangeContractLine_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
   proposedContractLine:number,
   getDefaults:boolean,
}

export interface OnChangeContractLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedContractNum
      @param getDefaults
   */  
export interface OnChangeContractNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed ContractNum  */  
   proposedContractNum:number,
      /**  Assign any fields related to ContractNum  */  
   getDefaults:boolean,
}

export interface OnChangeContractNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCustID
      @param getDefaults
   */  
export interface OnChangeCustID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed Customer ID  */  
   proposedCustID:string,
      /**  Assign any fields related to CustID  */  
   getDefaults:boolean,
}

export interface OnChangeCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param empID
      @param ds
   */  
export interface OnChangeEmpID_input{
      /**  EmpID  */  
   empID:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeEmpID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param equipID
      @param ds
   */  
export interface OnChangeEquipID_input{
      /**  equipID  */  
   equipID:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeEquipID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeHDCaseSearch_input{
   ds:Erp_Tablesets_HDCaseSearchTableset[],
}

export interface OnChangeHDCaseSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param ds
      @param proposedInvoiceLine
      @param getDefaults
   */  
export interface OnChangeInvoiceLine_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed InvoiceLine  */  
   proposedInvoiceLine:number,
      /**  Assign any fields related to InvoiceLine  */  
   getDefaults:boolean,
}

export interface OnChangeInvoiceLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedInvoiceNum
      @param getDefaults
   */  
export interface OnChangeInvoiceNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed InvoiceNum  */  
   proposedInvoiceNum:number,
      /**  Assign any fields related to InvoiceNum  */  
   getDefaults:boolean,
}

export interface OnChangeInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedMktgCampaignID
   */  
export interface OnChangeMktgCampaignID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed MktgCampaignID  */  
   proposedMktgCampaignID:string,
}

export interface OnChangeMktgCampaignID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedMktgEvntSeq
   */  
export interface OnChangeMktgEvntSeq_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed MktgEvntSeq  */  
   proposedMktgEvntSeq:number,
}

export interface OnChangeMktgEvntSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ipName
      @param ds
   */  
export interface OnChangeName_input{
      /**  Name  */  
   ipName:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedOrderLine
      @param getDefaults
   */  
export interface OnChangeOrderLine_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed OrderLine  */  
   proposedOrderLine:number,
      /**  Assign any fields related to OrderLine  */  
   getDefaults:boolean,
}

export interface OnChangeOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedOrderNum
      @param getDefaults
   */  
export interface OnChangeOrderNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed OrderNum  */  
   proposedOrderNum:number,
      /**  Assign any fields related to OrderNum  */  
   getDefaults:boolean,
}

export interface OnChangeOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedOrderRelNum
   */  
export interface OnChangeOrderRelNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed OrderRelNum  */  
   proposedOrderRelNum:number,
}

export interface OnChangeOrderRelNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedPartNum
      @param getDefaults
      @param SysRowID
      @param rowType
   */  
export interface OnChangePartNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed PartNum  */  
   proposedPartNum:string,
      /**  Assign any fields related to PartNum  */  
   getDefaults:boolean,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
   proposedPartNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ipPerConLnkRowID
      @param ds
   */  
export interface OnChangePerConLnkRowID_input{
      /**  PerConLnkRowID  */  
   ipPerConLnkRowID:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangePerConLnkRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedPrcConNum
      @param proposedPrcCustNum
      @param proposedPrcShipToNum
   */  
export interface OnChangePrcConNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed PrcConNum  */  
   proposedPrcConNum:number,
      /**  The proposed PrcCustNum  */  
   proposedPrcCustNum:number,
      /**  The proposed PrcShipToNum  */  
   proposedPrcShipToNum:string,
}

export interface OnChangePrcConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedProjectID
   */  
export interface OnChangeProjectID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed ProjectID  */  
   proposedProjectID:string,
}

export interface OnChangeProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedPurPointConNum
      @param proposedPurPoint
      @param proposedVendorNum
   */  
export interface OnChangePurPointConNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed PurPointConNum  */  
   proposedPurPointConNum:number,
      /**  The proposed PurPoint  */  
   proposedPurPoint:string,
      /**  The proposed VendorNum  */  
   proposedVendorNum:number,
}

export interface OnChangePurPointConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedPurPoint
   */  
export interface OnChangePurPoint_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed PurPoint  */  
   proposedPurPoint:string,
}

export interface OnChangePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param proposedQuantityUOM
      @param ds
   */  
export interface OnChangeQuantityUOM_input{
      /**  The proposed QuantityUOM  */  
   proposedQuantityUOM:string,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeQuantityUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param proposedQuantity
      @param ds
   */  
export interface OnChangeQuantity_input{
      /**  The proposed UnitPrice  */  
   proposedQuantity:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeQuantity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedQuoteLine
      @param getDefaults
   */  
export interface OnChangeQuoteLine_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed QuoteLine  */  
   proposedQuoteLine:number,
      /**  Assign any fields related to QuoteLine  */  
   getDefaults:boolean,
}

export interface OnChangeQuoteLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedQuoteNum
      @param getDefaults
   */  
export interface OnChangeQuoteNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed QuoteNum  */  
   proposedQuoteNum:number,
      /**  Assign any fields related to QuoteNum  */  
   getDefaults:boolean,
}

export interface OnChangeQuoteNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedRMALine
      @param getDefaults
   */  
export interface OnChangeRMALine_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed RMALine  */  
   proposedRMALine:number,
      /**  Defaults  */  
   getDefaults:boolean,
}

export interface OnChangeRMALine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedRMANum
      @param getDefaults
   */  
export interface OnChangeRMANum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed RMANum  */  
   proposedRMANum:number,
      /**  Defaults  */  
   getDefaults:boolean,
}

export interface OnChangeRMANum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedReqPerConID
   */  
export interface OnChangeReqPerConID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed Person Contact ID  */  
   proposedReqPerConID:number,
}

export interface OnChangeReqPerConID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedReqPerConLnkRowID
   */  
export interface OnChangeReqPerConLnkRowID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed Person Contact Link ID  */  
   proposedReqPerConLnkRowID:string,
}

export interface OnChangeReqPerConLnkRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedRevisionNum
   */  
export interface OnChangeRevisionNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed RevisionNum  */  
   proposedRevisionNum:string,
}

export interface OnChangeRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedCaseTopics
   */  
export interface OnChangeSearchCaseTopics_input{
   ds:Erp_Tablesets_HDCaseSearchTableset[],
      /**  The proposed case topics delimited with spaces  */  
   proposedCaseTopics:string,
}

export interface OnChangeSearchCaseTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param changedTopicIDInt
      @param ds
      @param proposedTopicID1
      @param proposedTopicID2
      @param proposedTopicID3
      @param proposedTopicID4
      @param proposedTopicID5
      @param proposedTopicID6
      @param proposedTopicID7
      @param proposedTopicID8
      @param proposedTopicID9
      @param proposedTopicID10
   */  
export interface OnChangeSearchTopicID_input{
   changedTopicIDInt:number,
   ds:Erp_Tablesets_HDCaseSearchTableset[],
   proposedTopicID1:string,
   proposedTopicID2:string,
   proposedTopicID3:string,
   proposedTopicID4:string,
   proposedTopicID5:string,
   proposedTopicID6:string,
   proposedTopicID7:string,
   proposedTopicID8:string,
   proposedTopicID9:string,
   proposedTopicID10:string,
}

export interface OnChangeSearchTopicID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param ds
      @param proposedTopicID1
      @param proposedTopicID2
      @param proposedTopicID3
      @param proposedTopicID4
      @param proposedTopicID5
      @param proposedTopicID6
      @param proposedTopicID7
      @param proposedTopicID8
      @param proposedTopicID9
      @param proposedTopicID10
   */  
export interface OnChangeSearchTopics_input{
   ds:Erp_Tablesets_HDCaseSearchTableset[],
      /**  The proposed TopicID1  */  
   proposedTopicID1:string,
      /**  The proposed TopicID2  */  
   proposedTopicID2:string,
      /**  The proposed TopicID3  */  
   proposedTopicID3:string,
      /**  The proposed TopicID4  */  
   proposedTopicID4:string,
      /**  The proposed TopicID5  */  
   proposedTopicID5:string,
      /**  The proposed TopicID6  */  
   proposedTopicID6:string,
      /**  The proposed TopicID7  */  
   proposedTopicID7:string,
      /**  The proposed TopicID8  */  
   proposedTopicID8:string,
      /**  The proposed TopicID9  */  
   proposedTopicID9:string,
      /**  The proposed TopicID10  */  
   proposedTopicID10:string,
}

export interface OnChangeSearchTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HDCaseSearchTableset,
}
}

   /** Required : 
      @param ds
      @param proposedSerialNumber
      @param getDefaults
      @param proposedPartNum
   */  
export interface OnChangeSerialNumber_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed SerialNumber  */  
   proposedSerialNumber:string,
      /**  Assign any fields related to SerialNumber  */  
   getDefaults:boolean,
      /**  The proposed PartNum  */  
   proposedPartNum:string,
}

export interface OnChangeSerialNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param proposedShipToCustID
   */  
export interface OnChangeShipToCustID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  Proposed Third-Party Ship To  */  
   proposedShipToCustID:string,
}

export interface OnChangeShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedShipToNum
   */  
export interface OnChangeShipToNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed ShipToNum  */  
   proposedShipToNum:string,
}

export interface OnChangeShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedShpConNum
      @param proposedShipToNum
      @param proposedShpCustNum
   */  
export interface OnChangeShpConNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed ShpConNum  */  
   proposedShpConNum:number,
      /**  The proposed ShipToNum  */  
   proposedShipToNum:string,
      /**  The proposed ShpCustNum  */  
   proposedShpCustNum:number,
}

export interface OnChangeShpConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedTaskSetID
   */  
export interface OnChangeTaskSetID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  Proposed Third-Party Ship To  */  
   proposedTaskSetID:string,
}

export interface OnChangeTaskSetID_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedTopicID1
      @param proposedTopicID2
      @param proposedTopicID3
      @param proposedTopicID4
      @param proposedTopicID5
      @param proposedTopicID6
      @param proposedTopicID7
      @param proposedTopicID8
      @param proposedTopicID9
      @param proposedTopicID10
   */  
export interface OnChangeTopics_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed TopicID1  */  
   proposedTopicID1:string,
      /**  The proposed TopicID2  */  
   proposedTopicID2:string,
      /**  The proposed TopicID3  */  
   proposedTopicID3:string,
      /**  The proposed TopicID4  */  
   proposedTopicID4:string,
      /**  The proposed TopicID5  */  
   proposedTopicID5:string,
      /**  The proposed TopicID6  */  
   proposedTopicID6:string,
      /**  The proposed TopicID7  */  
   proposedTopicID7:string,
      /**  The proposed TopicID8  */  
   proposedTopicID8:string,
      /**  The proposed TopicID9  */  
   proposedTopicID9:string,
      /**  The proposed TopicID10  */  
   proposedTopicID10:string,
}

export interface OnChangeTopics_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param proposedUnitPrice
      @param ds
   */  
export interface OnChangeUnitPrice_input{
      /**  The proposed UnitPrice  */  
   proposedUnitPrice:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface OnChangeUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedVenConNum
      @param proposedVendorNum
      @param proposedPurPoint
   */  
export interface OnChangeVenConNum_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed VenConNum  */  
   proposedVenConNum:number,
      /**  The proposed CustNum  */  
   proposedVendorNum:number,
      /**  The proposed PurPoint  */  
   proposedPurPoint:string,
}

export interface OnChangeVenConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedVendorID
      @param getDefaults
   */  
export interface OnChangeVendorID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed VendorID  */  
   proposedVendorID:string,
      /**  Assign any fields related to VendorID  */  
   getDefaults:boolean,
}

export interface OnChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedWFGroupID
   */  
export interface OnChangeWFGroupID_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed WFGroupID  */  
   proposedWFGroupID:string,
}

export interface OnChangeWFGroupID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param helpDeskCaseNum
      @param proposedPackNum
      @param proposedPackLine
      @param proposedDropShipPackSlip
      @param proposedDropShipPackLine
      @param getDefaults
   */  
export interface OnChangeWarrantyCode_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  Current Help Desk Case Number  */  
   helpDeskCaseNum:number,
      /**  The proposed PackNum  */  
   proposedPackNum:number,
      /**  The proposed PackLine  */  
   proposedPackLine:number,
      /**  The proposed Drop Shipment Pack Slip  */  
   proposedDropShipPackSlip:string,
      /**  The proposed Drop Shipment Pack Line  */  
   proposedDropShipPackLine:number,
      /**  Assign any fields related to Packing Slip  */  
   getDefaults:boolean,
}

export interface OnChangeWarrantyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param hdCaseNum
      @param closeCase
   */  
export interface OpenCloseCase_input{
      /**  HDCaseNum to be opened or closed  */  
   hdCaseNum:number,
      /**  Yes to close Case, no to open Case  */  
   closeCase:boolean,
}

export interface OpenCloseCase_output{
   returnObj:Erp_Tablesets_HelpDeskTableset[],
}

   /** Required : 
      @param hdCaseNum
      @param closeCase
   */  
export interface PreOpenCloseCase_input{
      /**  The current HDCase.HDCaseNum field  */  
   hdCaseNum:number,
      /**  Yes to close Case, no to open Case  */  
   closeCase:boolean,
}

export interface PreOpenCloseCase_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtHelpDeskTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtHelpDeskTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param ds
      @param proposedContractNum
      @param contractLine
      @param partNum
   */  
export interface ValidateContractPart_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed service contract number  */  
   proposedContractNum:number,
      /**  Contract line of the contract.  */  
   contractLine:number,
      /**  partNum of the HdCase  */  
   partNum:string,
}

export interface ValidateContractPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
   WarningMsg:string,
}
}

   /** Required : 
      @param ds
      @param proposedContractNum
   */  
export interface ValidateContractStatus_input{
   ds:Erp_Tablesets_HelpDeskTableset[],
      /**  The proposed service contract number  */  
   proposedContractNum:number,
}

export interface ValidateContractStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HelpDeskTableset,
   WarningMsg:string,
}
}

   /** Required : 
      @param helpDeskCaseNum
      @param ds
   */  
export interface ValidateFSCallRequirements_input{
      /**  The Help Desk case number to use as a source  */  
   helpDeskCaseNum:number,
   ds:Erp_Tablesets_HelpDeskTableset[],
}

export interface ValidateFSCallRequirements_output{
parameters : {
      /**  output parameters  */  
   WarningMsg:string,
   ds:Erp_Tablesets_HelpDeskTableset,
}
}

   /** Required : 
      @param hDCaseNum
      @param wFComplete
      @param taskSetID
   */  
export interface createAvailableMilestonesList_input{
      /**  Help Desk Case Number  */  
   hDCaseNum:number,
      /**  Current status of the Workflow for this case. HDCase.WFComplete  */  
   wFComplete:boolean,
      /**  Task set ID, currently assigned to this Case. (HDCase.TaskSetiID)  */  
   taskSetID:string,
}

export interface createAvailableMilestonesList_output{
parameters : {
      /**  output parameters  */  
   availableMilestonesList:string,
}
}

   /** Required : 
      @param taskSetID
      @param wFComplete
   */  
export interface createAvailableTaskSetsList_input{
      /**  Task set ID, currently assigned to this Case. (HDCase.TaskSetiID)  */  
   taskSetID:string,
      /**  Current status of the Workflow for this case. HDCase.WFComplete  */  
   wFComplete:boolean,
}

export interface createAvailableTaskSetsList_output{
parameters : {
      /**  output parameters  */  
   availableTaskSetsList:string,
}
}

