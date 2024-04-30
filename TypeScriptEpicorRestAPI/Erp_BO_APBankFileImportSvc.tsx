import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APBankFileImportSvc
// Description: none
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/$metadata", {
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
   Description: Get APBankFileImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APBankFileImports
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportRow
   */  
export function get_APBankFileImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APBankFileImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APChkGrpImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APBankFileImports(requestBody:Erp_Tablesets_APChkGrpImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports", {
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
   Summary: Calls GetByID to retrieve the APBankFileImport item
   Description: Calls GetByID to retrieve the APBankFileImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APBankFileImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APChkGrpImportRow
   */  
export function get_APBankFileImports_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APChkGrpImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")", {
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
         resolve(data as Erp_Tablesets_APChkGrpImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APBankFileImport for the service
   Description: Calls UpdateExt to update APBankFileImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APBankFileImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APBankFileImports_Company_GroupID(Company:string, GroupID:string, requestBody:Erp_Tablesets_APChkGrpImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete APBankFileImport item
   Description: Call UpdateExt to delete APBankFileImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APBankFileImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APBankFileImports_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")", {
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
   Description: Get CheckHedImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CheckHedImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedImportRow
   */  
export function get_APBankFileImports_Company_GroupID_CheckHedImports(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/CheckHedImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CheckHedImport item
   Description: Calls GetByID to retrieve the CheckHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedImportRow
   */  
export function get_APBankFileImports_Company_GroupID_CheckHedImports_Company_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/CheckHedImports(" + Company + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get APChkGrpImportAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APChkGrpImportAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportAttchRow
   */  
export function get_APBankFileImports_Company_GroupID_APChkGrpImportAttches(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/APChkGrpImportAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APChkGrpImportAttch item
   Description: Calls GetByID to retrieve the APChkGrpImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpImportAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   */  
export function get_APBankFileImports_Company_GroupID_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APChkGrpImportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_APChkGrpImportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CheckHedImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckHedImports
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedImportRow
   */  
export function get_CheckHedImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckHedImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckHedImports(requestBody:Erp_Tablesets_CheckHedImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports", {
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
   Summary: Calls GetByID to retrieve the CheckHedImport item
   Description: Calls GetByID to retrieve the CheckHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedImportRow
   */  
export function get_CheckHedImports_Company_HeadNum(Company:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CheckHedImport for the service
   Description: Calls UpdateExt to update CheckHedImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckHedImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CheckHedImports_Company_HeadNum(Company:string, HeadNum:string, requestBody:Erp_Tablesets_CheckHedImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CheckHedImport item
   Description: Call UpdateExt to delete CheckHedImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckHedImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CheckHedImports_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")", {
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
   Description: Get APTranImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTranImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranImportRow
   */  
export function get_CheckHedImports_Company_HeadNum_APTranImports(Company:string, HeadNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")/APTranImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APTranImport item
   Description: Calls GetByID to retrieve the APTranImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranImportNo Desc: APTranImportNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranImportRow
   */  
export function get_CheckHedImports_Company_HeadNum_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranImportNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")", {
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
         resolve(data as Erp_Tablesets_APTranImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APTranImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTranImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranImportRow
   */  
export function get_APTranImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTranImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APTranImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APTranImports(requestBody:Erp_Tablesets_APTranImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports", {
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
   Summary: Calls GetByID to retrieve the APTranImport item
   Description: Calls GetByID to retrieve the APTranImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranImportNo Desc: APTranImportNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APTranImportRow
   */  
export function get_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranImportNo:string, InvoiceNum:string, Voided:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APTranImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")", {
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
         resolve(data as Erp_Tablesets_APTranImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APTranImport for the service
   Description: Calls UpdateExt to update APTranImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTranImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranImportNo Desc: APTranImportNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranImportNo:string, InvoiceNum:string, Voided:string, requestBody:Erp_Tablesets_APTranImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Summary: Call UpdateExt to delete APTranImport item
   Description: Call UpdateExt to delete APTranImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTranImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTranImportNo Desc: APTranImportNo   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param Voided Desc: Voided   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company:string, HeadNum:string, APTranImportNo:string, InvoiceNum:string, Voided:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")", {
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
   Description: Get APChkGrpImportAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APChkGrpImportAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportAttchRow
   */  
export function get_APChkGrpImportAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APChkGrpImportAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APChkGrpImportAttches(requestBody:Erp_Tablesets_APChkGrpImportAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches", {
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
   Summary: Calls GetByID to retrieve the APChkGrpImportAttch item
   Description: Calls GetByID to retrieve the APChkGrpImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpImportAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   */  
export function get_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APChkGrpImportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_APChkGrpImportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APChkGrpImportAttch for the service
   Description: Calls UpdateExt to update APChkGrpImportAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APChkGrpImportAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, requestBody:Erp_Tablesets_APChkGrpImportAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete APChkGrpImportAttch item
   Description: Call UpdateExt to delete APChkGrpImportAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APChkGrpImportAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
   Description: Get APPmtMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPmtMatches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPmtMatchRow
   */  
export function get_APPmtMatches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPmtMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPmtMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPmtMatches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPmtMatchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPmtMatchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPmtMatches(requestBody:Erp_Tablesets_APPmtMatchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches", {
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
   Summary: Calls GetByID to retrieve the APPmtMatch item
   Description: Calls GetByID to retrieve the APPmtMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPmtMatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTRanNo Desc: APTRanNo   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPmtMatchRow
   */  
export function get_APPmtMatches_Company_HeadNum_APTRanNo(Company:string, HeadNum:string, APTRanNo:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPmtMatchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches(" + Company + "," + HeadNum + "," + APTRanNo + ")", {
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
         resolve(data as Erp_Tablesets_APPmtMatchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPmtMatch for the service
   Description: Calls UpdateExt to update APPmtMatch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPmtMatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTRanNo Desc: APTRanNo   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPmtMatchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPmtMatches_Company_HeadNum_APTRanNo(Company:string, HeadNum:string, APTRanNo:string, requestBody:Erp_Tablesets_APPmtMatchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches(" + Company + "," + HeadNum + "," + APTRanNo + ")", {
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
   Summary: Call UpdateExt to delete APPmtMatch item
   Description: Call UpdateExt to delete APPmtMatch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPmtMatch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param APTRanNo Desc: APTRanNo   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPmtMatches_Company_HeadNum_APTRanNo(Company:string, HeadNum:string, APTRanNo:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches(" + Company + "," + HeadNum + "," + APTRanNo + ")", {
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
   Description: Get CheckHedMatcheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckHedMatcheds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedMatchedRow
   */  
export function get_CheckHedMatcheds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedMatchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedMatchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckHedMatcheds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedMatchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedMatchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckHedMatcheds(requestBody:Erp_Tablesets_CheckHedMatchedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds", {
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
   Summary: Calls GetByID to retrieve the CheckHedMatched item
   Description: Calls GetByID to retrieve the CheckHedMatched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedMatched
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedMatchedRow
   */  
export function get_CheckHedMatcheds_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedMatchedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedMatchedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CheckHedMatched for the service
   Description: Calls UpdateExt to update CheckHedMatched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckHedMatched
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedMatchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CheckHedMatcheds_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_CheckHedMatchedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CheckHedMatched item
   Description: Call UpdateExt to delete CheckHedMatched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckHedMatched
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CheckHedMatcheds_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseAPChkGrpImport:string, whereClauseAPChkGrpImportAttch:string, whereClauseCheckHedImport:string, whereClauseAPTranImport:string, whereClauseAPPmtMatch:string, whereClauseCheckHedMatched:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPChkGrpImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPChkGrpImport=" + whereClauseAPChkGrpImport
   }
   if(typeof whereClauseAPChkGrpImportAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPChkGrpImportAttch=" + whereClauseAPChkGrpImportAttch
   }
   if(typeof whereClauseCheckHedImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCheckHedImport=" + whereClauseCheckHedImport
   }
   if(typeof whereClauseAPTranImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPTranImport=" + whereClauseAPTranImport
   }
   if(typeof whereClauseAPPmtMatch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPmtMatch=" + whereClauseAPPmtMatch
   }
   if(typeof whereClauseCheckHedMatched!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCheckHedMatched=" + whereClauseCheckHedMatched
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetRows" + params, {
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetList" + params, {
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
   Summary: Invoke method ChangeGrpBankAcctID
   Description: Method to call when changing the bank account.
   OperationID: ChangeGrpBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGrpBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGrpBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGrpBankAcctID(requestBody:ChangeGrpBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGrpBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/ChangeGrpBankAcctID", {
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
         resolve(data as ChangeGrpBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMatchFlag
   Description: Validate entered record number - user matches payments
   OperationID: ChangeMatchFlag
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMatchFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMatchFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMatchFlag(requestBody:ChangeMatchFlag_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMatchFlag_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/ChangeMatchFlag", {
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
         resolve(data as ChangeMatchFlag_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRecordNum
   Description: none
   OperationID: ChangeRecordNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRecordNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRecordNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRecordNum(requestBody:ChangeRecordNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRecordNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/ChangeRecordNum", {
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
         resolve(data as ChangeRecordNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBankFileImportParam
   Description: Returns record in BankFileImportParam dataset
   OperationID: GetBankFileImportParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBankFileImportParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFileImportParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankFileImportParam(requestBody:GetBankFileImportParam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBankFileImportParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetBankFileImportParam", {
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
         resolve(data as GetBankFileImportParam_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportBankFile
   Description: none
   OperationID: ImportBankFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportBankFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBankFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportBankFile(requestBody:ImportBankFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportBankFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/ImportBankFile", {
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
         resolve(data as ImportBankFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchPayments
   Description: none
   OperationID: MatchPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchPayments(requestBody:MatchPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/MatchPayments", {
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
         resolve(data as MatchPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchTelepayPayments
   Description: Method Match imported file records to unmatched payments of Proposed Payment Groups
   OperationID: MatchTelepayPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchTelepayPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchTelepayPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchTelepayPayments(requestBody:MatchTelepayPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchTelepayPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/MatchTelepayPayments", {
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
         resolve(data as MatchTelepayPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnEnterGroupID
   Description: Method Match imported file records to unmatched payments of Proposed Payment Groups
   OperationID: OnEnterGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnEnterGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnEnterGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnEnterGroupID(requestBody:OnEnterGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnEnterGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/OnEnterGroupID", {
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
         resolve(data as OnEnterGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessPayments
   Description: Method Match imported file records to unmatched payments of Proposed Payment Groups
   OperationID: ProcessPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPayments(requestBody:ProcessPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/ProcessPayments", {
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
         resolve(data as ProcessPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRejectedPayments
   Description: Delete Rejected Payments from the system
   OperationID: DeleteRejectedPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRejectedPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRejectedPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRejectedPayments(requestBody:DeleteRejectedPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRejectedPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/DeleteRejectedPayments", {
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
         resolve(data as DeleteRejectedPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockGroup
   Description: Should be call before GetByID to lock the Group.
   OperationID: LockGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockGroup(requestBody:LockGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/LockGroup", {
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
         resolve(data as LockGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockGroup
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockGroup(requestBody:UnlockGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/UnlockGroup", {
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
         resolve(data as UnlockGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetStatement
   OperationID: GetStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetStatement(requestBody:GetStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetStatement", {
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
         resolve(data as GetStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPChkGrpImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrpImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPChkGrpImport(requestBody:GetNewAPChkGrpImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPChkGrpImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetNewAPChkGrpImport", {
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
         resolve(data as GetNewAPChkGrpImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPChkGrpImportAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrpImportAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpImportAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpImportAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPChkGrpImportAttch(requestBody:GetNewAPChkGrpImportAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPChkGrpImportAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetNewAPChkGrpImportAttch", {
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
         resolve(data as GetNewAPChkGrpImportAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCheckHedImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHedImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCheckHedImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHedImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCheckHedImport(requestBody:GetNewCheckHedImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCheckHedImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetNewCheckHedImport", {
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
         resolve(data as GetNewCheckHedImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPTranImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTranImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPTranImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTranImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPTranImport(requestBody:GetNewAPTranImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPTranImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetNewAPTranImport", {
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
         resolve(data as GetNewAPTranImport_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APChkGrpImportAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APChkGrpImportListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APChkGrpImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPmtMatchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPmtMatchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APTranImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedMatchedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedMatchedRow,
}

export interface Erp_Tablesets_APChkGrpImportAttchRow{
   "Company":string,
   "GroupID":string,
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

export interface Erp_Tablesets_APChkGrpImportListRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  ActiveUserID  */  
   "ActiveUserID":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  CheckDate  */  
   "CheckDate":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  Cashbook  */  
   "Cashbook":boolean,
      /**  PostErrorLog  */  
   "PostErrorLog":string,
      /**  PostInProcess  */  
   "PostInProcess":boolean,
      /**  RateGrpCode  */  
   "RateGrpCode":string,
      /**  PMUID  */  
   "PMUID":number,
      /**  PromissoryNote  */  
   "PromissoryNote":boolean,
      /**  EIPaymSent  */  
   "EIPaymSent":boolean,
      /**  GrpCreationVia  */  
   "GrpCreationVia":string,
      /**  CompletelyMatched  */  
   "CompletelyMatched":boolean,
      /**  MatchFlag  */  
   "MatchFlag":boolean,
      /**  ImportedFlag  */  
   "ImportedFlag":boolean,
      /**  ProcessedFlag  */  
   "ProcessedFlag":boolean,
      /**  TotalStatementAmt  */  
   "TotalStatementAmt":number,
      /**  MatchedAmt  */  
   "MatchedAmt":number,
      /**  UnMatchedAmt  */  
   "UnMatchedAmt":number,
      /**  ImportBankCode  */  
   "ImportBankCode":string,
      /**  ImportStmtNbr  */  
   "ImportStmtNbr":string,
      /**  ImportBankDate  */  
   "ImportBankDate":string,
      /**  PaymentType  */  
   "PaymentType":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  NOPaymentList  */  
   "NOPaymentList":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  Swift Number or ABA Routing Number  */  
   "BankAcctBankIdentifier":string,
      /**  The Bank's full name.  */  
   "BankAcctBankName":string,
      /**  The account number for the bank account. Used for reference only.  */  
   "BankAcctCheckingAccount":string,
      /**  Currency.CurrencyCode of the currency that the bank account is denominated in.  */  
   "BankAcctCurrencyCode":string,
      /**  Full description of the bank account.  */  
   "BankAcctDescription":string,
      /**  IBAN Code  */  
   "BankAcctIBANCode":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
      /**  The availability of Import File menu item is based on this flag  */  
   "OkToImport":boolean,
      /**  The availability of Import File menu item is based on this flag  */  
   "OkToMatch":boolean,
      /**  The availability of Process Group menu item is based on this flag  */  
   "OkToProcess":boolean,
      /**  The availability of Report menu item is based on this flag  */  
   "OkToReport":boolean,
      /**  Name of the payment method  */  
   "PayMethodName":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  the flag to show if imported records are ready for matching  */  
   "ReadyToMatch":boolean,
      /**  the flag to show if imported records are ready for processing  */  
   "ReadyToProcess":boolean,
      /**  Bank Branch Code  */  
   "BankAcctBankBranchCode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APChkGrpImportRow{
      /**  Company  */  
   "Company":string,
      /**  GroupID  */  
   "GroupID":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  ActiveUserID  */  
   "ActiveUserID":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  CheckDate  */  
   "CheckDate":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  Cashbook  */  
   "Cashbook":boolean,
      /**  PostErrorLog  */  
   "PostErrorLog":string,
      /**  PostInProcess  */  
   "PostInProcess":boolean,
      /**  RateGrpCode  */  
   "RateGrpCode":string,
      /**  PMUID  */  
   "PMUID":number,
      /**  PromissoryNote  */  
   "PromissoryNote":boolean,
      /**  EIPaymSent  */  
   "EIPaymSent":boolean,
      /**  GrpCreationVia  */  
   "GrpCreationVia":string,
      /**  CompletelyMatched  */  
   "CompletelyMatched":boolean,
      /**  MatchFlag  */  
   "MatchFlag":boolean,
      /**  ImportedFlag  */  
   "ImportedFlag":boolean,
      /**  ProcessedFlag  */  
   "ProcessedFlag":boolean,
      /**  TotalStatementAmt  */  
   "TotalStatementAmt":number,
      /**  MatchedAmt  */  
   "MatchedAmt":number,
      /**  UnMatchedAmt  */  
   "UnMatchedAmt":number,
      /**  ImportBankCode  */  
   "ImportBankCode":string,
      /**  ImportStmtNbr  */  
   "ImportStmtNbr":string,
      /**  ImportBankDate  */  
   "ImportBankDate":string,
      /**  PaymentType  */  
   "PaymentType":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  the flag to show if imported records are ready for matching  */  
   "ReadyToMatch":boolean,
      /**  the flag to show if imported records are ready for processing  */  
   "ReadyToProcess":boolean,
   "CurrencyCurrDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
      /**  The availability of Import File menu item is based on this flag  */  
   "OkToImport":boolean,
      /**  The availability of Import File menu item is based on this flag  */  
   "OkToMatch":boolean,
      /**  The availability of Process Group menu item is based on this flag  */  
   "OkToProcess":boolean,
      /**  The availability of Report menu item is based on this flag  */  
   "OkToReport":boolean,
   "BitFlag":number,
   "BankAcctIBANCode":string,
   "BankAcctCurrencyCode":string,
   "BankAcctBankIdentifier":string,
   "BankAcctBankName":string,
   "BankAcctDescription":string,
   "BankAcctBankBranchCode":string,
   "BankAcctCheckingAccount":string,
   "PayMethodOutputFile":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPmtMatchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Check Amount. Document Currency.  */  
   "DocCheckAmt":number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Vendors name.  */  
   "Name":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckAmt":number,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   "InvoiceNum":string,
   "Rpt3CheckAmt":number,
   "CheckAmt":number,
   "VendorID":string,
      /**  The record number of imported file - used for manual match  */  
   "RecordNumber":number,
   "CheckDate":string,
   "APTRanNo":number,
   "CheckNum":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APTranImportRow{
      /**  Company  */  
   "Company":string,
      /**  TranType  */  
   "TranType":string,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  APTranImportNo  */  
   "APTranImportNo":number,
      /**  InvoiceNum  */  
   "InvoiceNum":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  TranAmt  */  
   "TranAmt":number,
      /**  DocTranAmt  */  
   "DocTranAmt":number,
      /**  DiscAmt  */  
   "DiscAmt":number,
      /**  DocDiscAmt  */  
   "DocDiscAmt":number,
      /**  Description  */  
   "Description":string,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  CheckNum  */  
   "CheckNum":number,
      /**  TranDate  */  
   "TranDate":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  GLPosted  */  
   "GLPosted":boolean,
      /**  Voided  */  
   "Voided":boolean,
      /**  EntryPerson  */  
   "EntryPerson":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  Comment  */  
   "Comment":string,
      /**  TaxRegionCode  */  
   "TaxRegionCode":string,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  DocTaxAmt  */  
   "DocTaxAmt":number,
      /**  RefType  */  
   "RefType":string,
      /**  RefCode  */  
   "RefCode":string,
      /**  RefCodeDesc  */  
   "RefCodeDesc":string,
      /**  RoundDiff  */  
   "RoundDiff":number,
      /**  Rpt1DiscAmt  */  
   "Rpt1DiscAmt":number,
      /**  Rpt2DiscAmt  */  
   "Rpt2DiscAmt":number,
      /**  Rpt3DiscAmt  */  
   "Rpt3DiscAmt":number,
      /**  Rpt1TaxAmt  */  
   "Rpt1TaxAmt":number,
      /**  Rpt2TaxAmt  */  
   "Rpt2TaxAmt":number,
      /**  Rpt3TaxAmt  */  
   "Rpt3TaxAmt":number,
      /**  Rpt1TranAmt  */  
   "Rpt1TranAmt":number,
      /**  Rpt2TranAmt  */  
   "Rpt2TranAmt":number,
      /**  Rpt3TranAmt  */  
   "Rpt3TranAmt":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  GetDfltTaxIds  */  
   "GetDfltTaxIds":boolean,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  WithholdAmt  */  
   "WithholdAmt":number,
      /**  DocWithholdAmt  */  
   "DocWithholdAmt":number,
      /**  Rpt1WithholdAmt  */  
   "Rpt1WithholdAmt":number,
      /**  Rpt2WithholdAmt  */  
   "Rpt2WithholdAmt":number,
      /**  Rpt3WithholdAmt  */  
   "Rpt3WithholdAmt":number,
      /**  SelfAssessAmt  */  
   "SelfAssessAmt":number,
      /**  DocSelfAssessAmt  */  
   "DocSelfAssessAmt":number,
      /**  Rpt1SelfAssessAmt  */  
   "Rpt1SelfAssessAmt":number,
      /**  Rpt2SelfAssessAmt  */  
   "Rpt2SelfAssessAmt":number,
      /**  Rpt3SelfAssessAmt  */  
   "Rpt3SelfAssessAmt":number,
      /**  RedStorno  */  
   "RedStorno":boolean,
      /**  PrePayment  */  
   "PrePayment":boolean,
      /**  ContractRef  */  
   "ContractRef":string,
      /**  ContractRefDate  */  
   "ContractRefDate":string,
      /**  RefPONum  */  
   "RefPONum":number,
      /**  TaxReceiptDate  */  
   "TaxReceiptDate":string,
      /**  TaxReceiptNo  */  
   "TaxReceiptNo":string,
      /**  WHTCertificateDate  */  
   "WHTCertificateDate":string,
      /**  WHTCertificateNo  */  
   "WHTCertificateNo":string,
      /**  PCashDeskID  */  
   "PCashDeskID":string,
      /**  GainLossType  */  
   "GainLossType":string,
      /**  PCashRefNum  */  
   "PCashRefNum":number,
      /**  ReverseGL  */  
   "ReverseGL":boolean,
      /**  RevalueDate  */  
   "RevalueDate":string,
      /**  RevalueBal  */  
   "RevalueBal":number,
      /**  DocRevalueBal  */  
   "DocRevalueBal":number,
      /**  Rpt1RevalueBal  */  
   "Rpt1RevalueBal":number,
      /**  Rpt2RevalueBal  */  
   "Rpt2RevalueBal":number,
      /**  Rpt3RevalueBal  */  
   "Rpt3RevalueBal":number,
      /**  BankID  */  
   "BankID":string,
      /**  BankPaidAmt  */  
   "BankPaidAmt":number,
      /**  DocBankPaidAmt  */  
   "DocBankPaidAmt":number,
      /**  Rpt1BankPaidAmt  */  
   "Rpt1BankPaidAmt":number,
      /**  Rpt2BankPaidAmt  */  
   "Rpt2BankPaidAmt":number,
      /**  Rpt3BankPaidAmt  */  
   "Rpt3BankPaidAmt":number,
      /**  AdjLegalNumber  */  
   "AdjLegalNumber":string,
      /**  AdjTranDocTypeID  */  
   "AdjTranDocTypeID":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MainSite  */  
   "MainSite":boolean,
      /**  SiteCode  */  
   "SiteCode":string,
      /**  BranchID  */  
   "BranchID":string,
      /**  InvoiceDate  */  
   "InvoiceDate":string,
      /**  Remarks  */  
   "Remarks":string,
      /**  AssetTypeCode  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  CreditCard  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  CardID  */  
   "CardID":string,
      /**  CardHolderTaxID  */  
   "CardHolderTaxID":string,
      /**  CardMemberName  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  NonDeductAmt  */  
   "NonDeductAmt":number,
      /**  NonDeductDocAmt  */  
   "NonDeductDocAmt":number,
      /**  NonDeductRpt1Amt  */  
   "NonDeductRpt1Amt":number,
      /**  NonDeductRpt2Amt  */  
   "NonDeductRpt2Amt":number,
      /**  NonDeductRpt3Amt  */  
   "NonDeductRpt3Amt":number,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CheckHedImportRow{
      /**  Company  */  
   "Company":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  GroupID  */  
   "GroupID":string,
      /**  HeadNum  */  
   "HeadNum":number,
      /**  BankAcctID  */  
   "BankAcctID":string,
      /**  CheckNum  */  
   "CheckNum":number,
      /**  CheckDate  */  
   "CheckDate":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  Voided  */  
   "Voided":boolean,
      /**  CheckSrc  */  
   "CheckSrc":string,
      /**  ClearedCheck  */  
   "ClearedCheck":boolean,
      /**  ClearedPending  */  
   "ClearedPending":boolean,
      /**  ClearedAmt  */  
   "ClearedAmt":number,
      /**  DocClearedAmt  */  
   "DocClearedAmt":number,
      /**  ClearedPerson  */  
   "ClearedPerson":string,
      /**  ClearedDate  */  
   "ClearedDate":string,
      /**  ClearedTime  */  
   "ClearedTime":string,
      /**  ClearedStmtEndDate  */  
   "ClearedStmtEndDate":string,
      /**  EmployeeNum  */  
   "EmployeeNum":string,
      /**  CheckAmt  */  
   "CheckAmt":number,
      /**  DocCheckAmt  */  
   "DocCheckAmt":number,
      /**  ManualPrint  */  
   "ManualPrint":boolean,
      /**  EntryPerson  */  
   "EntryPerson":string,
      /**  VendorNum  */  
   "VendorNum":number,
      /**  Name  */  
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
      /**  ZIP  */  
   "ZIP":string,
      /**  Country  */  
   "Country":string,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  ExchangeRate  */  
   "ExchangeRate":number,
      /**  CountryNum  */  
   "CountryNum":number,
      /**  BankSlip  */  
   "BankSlip":string,
      /**  ElecPayment  */  
   "ElecPayment":boolean,
      /**  VendorBankID  */  
   "VendorBankID":string,
      /**  VendorBankName  */  
   "VendorBankName":string,
      /**  VendorBankNameOnAccount  */  
   "VendorBankNameOnAccount":string,
      /**  VendorBankAddress1  */  
   "VendorBankAddress1":string,
      /**  VendorBankAddress2  */  
   "VendorBankAddress2":string,
      /**  VendorBankAddress3  */  
   "VendorBankAddress3":string,
      /**  VendorBankCity  */  
   "VendorBankCity":string,
      /**  VendorBankState  */  
   "VendorBankState":string,
      /**  VendorBankPostalCode  */  
   "VendorBankPostalCode":string,
      /**  VendorBankCountryNum  */  
   "VendorBankCountryNum":number,
      /**  VendorBankAcctNumber  */  
   "VendorBankAcctNumber":string,
      /**  VendorBankSwiftNum  */  
   "VendorBankSwiftNum":string,
      /**  CashBookNum  */  
   "CashBookNum":number,
      /**  CashbookLine  */  
   "CashbookLine":number,
      /**  XRefCheckNum  */  
   "XRefCheckNum":string,
      /**  Rpt1CheckAmt  */  
   "Rpt1CheckAmt":number,
      /**  Rpt2CheckAmt  */  
   "Rpt2CheckAmt":number,
      /**  Rpt3CheckAmt  */  
   "Rpt3CheckAmt":number,
      /**  Rpt1ClearedAmt  */  
   "Rpt1ClearedAmt":number,
      /**  Rpt2ClearedAmt  */  
   "Rpt2ClearedAmt":number,
      /**  Rpt3ClearedAmt  */  
   "Rpt3ClearedAmt":number,
      /**  RateGrpCode  */  
   "RateGrpCode":string,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  PaymentTotal  */  
   "PaymentTotal":number,
      /**  DocPaymentTotal  */  
   "DocPaymentTotal":number,
      /**  Rpt1PaymentTotal  */  
   "Rpt1PaymentTotal":number,
      /**  Rpt2PaymentTotal  */  
   "Rpt2PaymentTotal":number,
      /**  Rpt3PaymentTotal  */  
   "Rpt3PaymentTotal":number,
      /**  Variance  */  
   "Variance":number,
      /**  DocVariance  */  
   "DocVariance":number,
      /**  Rpt1Variance  */  
   "Rpt1Variance":number,
      /**  Rpt2Variance  */  
   "Rpt2Variance":number,
      /**  Rpt3Variance  */  
   "Rpt3Variance":number,
      /**  PaymentBankRate  */  
   "PaymentBankRate":number,
      /**  BankTotalAmt  */  
   "BankTotalAmt":number,
      /**  IsEnterTotal  */  
   "IsEnterTotal":boolean,
      /**  LockRate  */  
   "LockRate":number,
      /**  ReadyToCalc  */  
   "ReadyToCalc":boolean,
      /**  RecalcBeforePost  */  
   "RecalcBeforePost":boolean,
      /**  UsePendAcct  */  
   "UsePendAcct":boolean,
      /**  ForceDiscount  */  
   "ForceDiscount":boolean,
      /**  FirstHeadNum  */  
   "FirstHeadNum":number,
      /**  ApplyingPayment  */  
   "ApplyingPayment":boolean,
      /**  Plant  */  
   "Plant":string,
      /**  InvoiceNum  */  
   "InvoiceNum":string,
      /**  PMUID  */  
   "PMUID":number,
      /**  PCashDeskID  */  
   "PCashDeskID":string,
      /**  BankTranID  */  
   "BankTranID":string,
      /**  PCashRefNum  */  
   "PCashRefNum":number,
      /**  BankPaidAmt  */  
   "BankPaidAmt":number,
      /**  DocBankPaidAmt  */  
   "DocBankPaidAmt":number,
      /**  Rpt1BankPaidAmt  */  
   "Rpt1BankPaidAmt":number,
      /**  Rpt2BankPaidAmt  */  
   "Rpt2BankPaidAmt":number,
      /**  Rpt3BankPaidAmt  */  
   "Rpt3BankPaidAmt":number,
      /**  BankTransDate  */  
   "BankTransDate":string,
      /**  VendorID  */  
   "VendorID":string,
      /**  TranType  */  
   "TranType":string,
      /**  StatusDesc  */  
   "StatusDesc":string,
      /**  TransText  */  
   "TransText":string,
      /**  TransDetail  */  
   "TransDetail":string,
      /**  OrigInvoiceNum  */  
   "OrigInvoiceNum":string,
      /**  OrigName  */  
   "OrigName":string,
      /**  OrigVendorID  */  
   "OrigVendorID":string,
      /**  PropGroupID  */  
   "PropGroupID":string,
      /**  NumPayment  */  
   "NumPayment":number,
      /**  CheckHeadNum  */  
   "CheckHeadNum":number,
      /**  OrigVendorNum  */  
   "OrigVendorNum":number,
      /**  Matched  */  
   "Matched":boolean,
      /**  OKToMatch  */  
   "OKToMatch":boolean,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  SavedInvoiceNum  */  
   "SavedInvoiceNum":string,
      /**  SavedVendorName  */  
   "SavedVendorName":string,
      /**  SavedVendorID  */  
   "SavedVendorID":string,
      /**  SavedVendorNum  */  
   "SavedVendorNum":number,
      /**  CheckStatus  */  
   "CheckStatus":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  NOPaymentStatus  */  
   "NOPaymentStatus":number,
      /**  NOPaymentDirection  */  
   "NOPaymentDirection":string,
      /**  NOPaymentType  */  
   "NOPaymentType":string,
      /**  NOTransferFileName  */  
   "NOTransferFileName":string,
      /**  NOBankTransRef  */  
   "NOBankTransRef":string,
      /**  BalanceUpdate  */  
   "BalanceUpdate":number,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  BankRecGainLoss  */  
   "BankRecGainLoss":number,
      /**  BOEInvoiceNum  */  
   "BOEInvoiceNum":string,
      /**  DocBankRecGainLoss  */  
   "DocBankRecGainLoss":number,
      /**  MsgId  */  
   "MsgId":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  PayLegalNumber  */  
   "PayLegalNumber":string,
      /**  PayTranDocTypeID  */  
   "PayTranDocTypeID":string,
      /**  Rpt1BankRecGainLoss  */  
   "Rpt1BankRecGainLoss":number,
      /**  Rpt2BankRecGainLoss  */  
   "Rpt2BankRecGainLoss":number,
      /**  Rpt3BankRecGainLoss  */  
   "Rpt3BankRecGainLoss":number,
      /**  TaxPaymInfo  */  
   "TaxPaymInfo":string,
      /**  VoidLegalNumber  */  
   "VoidLegalNumber":string,
      /**  VoidTranDocTypeID  */  
   "VoidTranDocTypeID":string,
      /**  SEGrpNum  */  
   "SEGrpNum":number,
      /**  SEReference  */  
   "SEReference":string,
      /**  SEISGroupedPO3  */  
   "SEISGroupedPO3":boolean,
      /**  SEISExported  */  
   "SEISExported":boolean,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MXBankAcctNumber  */  
   "MXBankAcctNumber":string,
      /**  MXBankIdentifier  */  
   "MXBankIdentifier":string,
      /**  MXRFC  */  
   "MXRFC":string,
      /**  BankBatchExcluded  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  SEPAPaymentDescription  */  
   "SEPAPaymentDescription":string,
      /**  NOImportErrors  */  
   "NOImportErrors":string,
      /**  THPayerType  */  
   "THPayerType":number,
      /**  THRefInvoiceNum  */  
   "THRefInvoiceNum":string,
      /**  THRefVendorNum  */  
   "THRefVendorNum":number,
      /**  VoidedReason  */  
   "VoidedReason":string,
      /**  RegulatoryReportingCode  */  
   "RegulatoryReportingCode":string,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  TaxPointDate  */  
   "TaxPointDate":string,
      /**  SEC  */  
   "SEC":string,
      /**  ACHTranCode  */  
   "ACHTranCode":number,
      /**  US1099KMerchCatCode  */  
   "US1099KMerchCatCode":string,
      /**  US1099KGen  */  
   "US1099KGen":boolean,
      /**  VendorBankBranchCode  */  
   "VendorBankBranchCode":string,
      /**  NettingID  */  
   "NettingID":number,
      /**  GL Description  */  
   "Description":string,
      /**  GL Description for the Payment Voiding process  */  
   "VoidDescription":string,
      /**  GL Description for AP - Apply Debit Memo/Prepayment  */  
   "DMDescription":string,
      /**  MXDIOTTranType  */  
   "MXDIOTTranType":string,
      /**  Transaction Detail, part 1  */  
   "TransDetail1":string,
      /**  Transactoin Detail part 3  */  
   "TransDetail3":string,
      /**  Transaction Detail part 4  */  
   "TransDetail4":string,
      /**  Indicates if the amount of payment from the imported file is less than amount of  proposed  payment  */  
   "UnderpayFlag":boolean,
      /**  Indicates if the amount of payment from the imported file is more than amount of  proposed  payment  */  
   "OverpayFlag":boolean,
      /**  Transaction Detail, Part2  */  
   "TransDetail2":string,
   "CurrencyCurrSymbol":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CheckHedMatchedRow{
      /**  Company  */  
   "Company":string,
      /**  Supplier Number  */  
   "VendorNum":number,
      /**  Vendor ID  */  
   "VendorID":string,
      /**  Supplier Name  */  
   "Name":string,
      /**  Payment Group ID  */  
   "GroupID":string,
      /**  Group ID of the proposed Payment  */  
   "PrpGroupID":string,
      /**  HeadNum of the CheckHed matched  */  
   "HeadNum":number,
      /**  Invoice Number for the payment matched  */  
   "InvoiceNum":string,
   "APTranNo":number,
   "CheckDate":string,
      /**  Currency Code of the payment  */  
   "CurrencyCode":string,
      /**  Payment amount  */  
   "CheckAmt":number,
      /**  Check Amount in Document currency  */  
   "DocCheckAmt":number,
   "Rpt1CheckAmt":number,
   "Rpt2CheckAmt":number,
   "Rpt3CheckAmt":number,
      /**  Record number of the imported table matched  */  
   "RecordNumber":number,
   "Matched":string,
   "CheckNum":number,
   "SysRowID":string,
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
      @param ProposedBankAcctID
      @param ds
   */  
export interface ChangeGrpBankAcctID_input{
      /**  The proposed bank account id  */  
   ProposedBankAcctID:string,
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface ChangeGrpBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param matchFlag
      @param pcGroupID
      @param ds
   */  
export interface ChangeMatchFlag_input{
      /**  Record number entered/proposed  */  
   matchFlag:boolean,
      /**  Group ID of the payment  */  
   pcGroupID:string,
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface ChangeMatchFlag_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param ds
      @param recordNumber
      @param pcGroupID
   */  
export interface ChangeRecordNum_input{
   ds:Erp_Tablesets_APBankFileImportTableset[],
   recordNumber:number,
   pcGroupID:string,
}

export interface ChangeRecordNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param pcGroupID
   */  
export interface DeleteRejectedPayments_input{
      /**  Group ID of the paymnet  */  
   pcGroupID:string,
}

export interface DeleteRejectedPayments_output{
parameters : {
      /**  output parameters  */  
   opMsg:string,
}
}

export interface Erp_Tablesets_APBankFileImportTableset{
   APChkGrpImport:Erp_Tablesets_APChkGrpImportRow[],
   APChkGrpImportAttch:Erp_Tablesets_APChkGrpImportAttchRow[],
   CheckHedImport:Erp_Tablesets_CheckHedImportRow[],
   APTranImport:Erp_Tablesets_APTranImportRow[],
   APPmtMatch:Erp_Tablesets_APPmtMatchRow[],
   CheckHedMatched:Erp_Tablesets_CheckHedMatchedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APChkGrpImportAttchRow{
   Company:string,
   GroupID:string,
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

export interface Erp_Tablesets_APChkGrpImportListRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  ActiveUserID  */  
   ActiveUserID:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  CheckDate  */  
   CheckDate:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  Cashbook  */  
   Cashbook:boolean,
      /**  PostErrorLog  */  
   PostErrorLog:string,
      /**  PostInProcess  */  
   PostInProcess:boolean,
      /**  RateGrpCode  */  
   RateGrpCode:string,
      /**  PMUID  */  
   PMUID:number,
      /**  PromissoryNote  */  
   PromissoryNote:boolean,
      /**  EIPaymSent  */  
   EIPaymSent:boolean,
      /**  GrpCreationVia  */  
   GrpCreationVia:string,
      /**  CompletelyMatched  */  
   CompletelyMatched:boolean,
      /**  MatchFlag  */  
   MatchFlag:boolean,
      /**  ImportedFlag  */  
   ImportedFlag:boolean,
      /**  ProcessedFlag  */  
   ProcessedFlag:boolean,
      /**  TotalStatementAmt  */  
   TotalStatementAmt:number,
      /**  MatchedAmt  */  
   MatchedAmt:number,
      /**  UnMatchedAmt  */  
   UnMatchedAmt:number,
      /**  ImportBankCode  */  
   ImportBankCode:string,
      /**  ImportStmtNbr  */  
   ImportStmtNbr:string,
      /**  ImportBankDate  */  
   ImportBankDate:string,
      /**  PaymentType  */  
   PaymentType:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  NOPaymentList  */  
   NOPaymentList:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  Swift Number or ABA Routing Number  */  
   BankAcctBankIdentifier:string,
      /**  The Bank's full name.  */  
   BankAcctBankName:string,
      /**  The account number for the bank account. Used for reference only.  */  
   BankAcctCheckingAccount:string,
      /**  Currency.CurrencyCode of the currency that the bank account is denominated in.  */  
   BankAcctCurrencyCode:string,
      /**  Full description of the bank account.  */  
   BankAcctDescription:string,
      /**  IBAN Code  */  
   BankAcctIBANCode:string,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
      /**  The availability of Import File menu item is based on this flag  */  
   OkToImport:boolean,
      /**  The availability of Import File menu item is based on this flag  */  
   OkToMatch:boolean,
      /**  The availability of Process Group menu item is based on this flag  */  
   OkToProcess:boolean,
      /**  The availability of Report menu item is based on this flag  */  
   OkToReport:boolean,
      /**  Name of the payment method  */  
   PayMethodName:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  the flag to show if imported records are ready for matching  */  
   ReadyToMatch:boolean,
      /**  the flag to show if imported records are ready for processing  */  
   ReadyToProcess:boolean,
      /**  Bank Branch Code  */  
   BankAcctBankBranchCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APChkGrpImportListTableset{
   APChkGrpImportList:Erp_Tablesets_APChkGrpImportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APChkGrpImportRow{
      /**  Company  */  
   Company:string,
      /**  GroupID  */  
   GroupID:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  ActiveUserID  */  
   ActiveUserID:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  CheckDate  */  
   CheckDate:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  Cashbook  */  
   Cashbook:boolean,
      /**  PostErrorLog  */  
   PostErrorLog:string,
      /**  PostInProcess  */  
   PostInProcess:boolean,
      /**  RateGrpCode  */  
   RateGrpCode:string,
      /**  PMUID  */  
   PMUID:number,
      /**  PromissoryNote  */  
   PromissoryNote:boolean,
      /**  EIPaymSent  */  
   EIPaymSent:boolean,
      /**  GrpCreationVia  */  
   GrpCreationVia:string,
      /**  CompletelyMatched  */  
   CompletelyMatched:boolean,
      /**  MatchFlag  */  
   MatchFlag:boolean,
      /**  ImportedFlag  */  
   ImportedFlag:boolean,
      /**  ProcessedFlag  */  
   ProcessedFlag:boolean,
      /**  TotalStatementAmt  */  
   TotalStatementAmt:number,
      /**  MatchedAmt  */  
   MatchedAmt:number,
      /**  UnMatchedAmt  */  
   UnMatchedAmt:number,
      /**  ImportBankCode  */  
   ImportBankCode:string,
      /**  ImportStmtNbr  */  
   ImportStmtNbr:string,
      /**  ImportBankDate  */  
   ImportBankDate:string,
      /**  PaymentType  */  
   PaymentType:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  the flag to show if imported records are ready for matching  */  
   ReadyToMatch:boolean,
      /**  the flag to show if imported records are ready for processing  */  
   ReadyToProcess:boolean,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
      /**  The availability of Import File menu item is based on this flag  */  
   OkToImport:boolean,
      /**  The availability of Import File menu item is based on this flag  */  
   OkToMatch:boolean,
      /**  The availability of Process Group menu item is based on this flag  */  
   OkToProcess:boolean,
      /**  The availability of Report menu item is based on this flag  */  
   OkToReport:boolean,
   BitFlag:number,
   BankAcctIBANCode:string,
   BankAcctCurrencyCode:string,
   BankAcctBankIdentifier:string,
   BankAcctBankName:string,
   BankAcctDescription:string,
   BankAcctBankBranchCode:string,
   BankAcctCheckingAccount:string,
   PayMethodOutputFile:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPmtMatchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Check Amount. Document Currency.  */  
   DocCheckAmt:number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Vendors name.  */  
   Name:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Reporting currency value of this field  */  
   Rpt1CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckAmt:number,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   InvoiceNum:string,
   Rpt3CheckAmt:number,
   CheckAmt:number,
   VendorID:string,
      /**  The record number of imported file - used for manual match  */  
   RecordNumber:number,
   CheckDate:string,
   APTRanNo:number,
   CheckNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APTranImportRow{
      /**  Company  */  
   Company:string,
      /**  TranType  */  
   TranType:string,
      /**  HeadNum  */  
   HeadNum:number,
      /**  APTranImportNo  */  
   APTranImportNo:number,
      /**  InvoiceNum  */  
   InvoiceNum:string,
      /**  Posted  */  
   Posted:boolean,
      /**  TranAmt  */  
   TranAmt:number,
      /**  DocTranAmt  */  
   DocTranAmt:number,
      /**  DiscAmt  */  
   DiscAmt:number,
      /**  DocDiscAmt  */  
   DocDiscAmt:number,
      /**  Description  */  
   Description:string,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  CheckNum  */  
   CheckNum:number,
      /**  TranDate  */  
   TranDate:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  GLPosted  */  
   GLPosted:boolean,
      /**  Voided  */  
   Voided:boolean,
      /**  EntryPerson  */  
   EntryPerson:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  Comment  */  
   Comment:string,
      /**  TaxRegionCode  */  
   TaxRegionCode:string,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  DocTaxAmt  */  
   DocTaxAmt:number,
      /**  RefType  */  
   RefType:string,
      /**  RefCode  */  
   RefCode:string,
      /**  RefCodeDesc  */  
   RefCodeDesc:string,
      /**  RoundDiff  */  
   RoundDiff:number,
      /**  Rpt1DiscAmt  */  
   Rpt1DiscAmt:number,
      /**  Rpt2DiscAmt  */  
   Rpt2DiscAmt:number,
      /**  Rpt3DiscAmt  */  
   Rpt3DiscAmt:number,
      /**  Rpt1TaxAmt  */  
   Rpt1TaxAmt:number,
      /**  Rpt2TaxAmt  */  
   Rpt2TaxAmt:number,
      /**  Rpt3TaxAmt  */  
   Rpt3TaxAmt:number,
      /**  Rpt1TranAmt  */  
   Rpt1TranAmt:number,
      /**  Rpt2TranAmt  */  
   Rpt2TranAmt:number,
      /**  Rpt3TranAmt  */  
   Rpt3TranAmt:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  GetDfltTaxIds  */  
   GetDfltTaxIds:boolean,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  WithholdAmt  */  
   WithholdAmt:number,
      /**  DocWithholdAmt  */  
   DocWithholdAmt:number,
      /**  Rpt1WithholdAmt  */  
   Rpt1WithholdAmt:number,
      /**  Rpt2WithholdAmt  */  
   Rpt2WithholdAmt:number,
      /**  Rpt3WithholdAmt  */  
   Rpt3WithholdAmt:number,
      /**  SelfAssessAmt  */  
   SelfAssessAmt:number,
      /**  DocSelfAssessAmt  */  
   DocSelfAssessAmt:number,
      /**  Rpt1SelfAssessAmt  */  
   Rpt1SelfAssessAmt:number,
      /**  Rpt2SelfAssessAmt  */  
   Rpt2SelfAssessAmt:number,
      /**  Rpt3SelfAssessAmt  */  
   Rpt3SelfAssessAmt:number,
      /**  RedStorno  */  
   RedStorno:boolean,
      /**  PrePayment  */  
   PrePayment:boolean,
      /**  ContractRef  */  
   ContractRef:string,
      /**  ContractRefDate  */  
   ContractRefDate:string,
      /**  RefPONum  */  
   RefPONum:number,
      /**  TaxReceiptDate  */  
   TaxReceiptDate:string,
      /**  TaxReceiptNo  */  
   TaxReceiptNo:string,
      /**  WHTCertificateDate  */  
   WHTCertificateDate:string,
      /**  WHTCertificateNo  */  
   WHTCertificateNo:string,
      /**  PCashDeskID  */  
   PCashDeskID:string,
      /**  GainLossType  */  
   GainLossType:string,
      /**  PCashRefNum  */  
   PCashRefNum:number,
      /**  ReverseGL  */  
   ReverseGL:boolean,
      /**  RevalueDate  */  
   RevalueDate:string,
      /**  RevalueBal  */  
   RevalueBal:number,
      /**  DocRevalueBal  */  
   DocRevalueBal:number,
      /**  Rpt1RevalueBal  */  
   Rpt1RevalueBal:number,
      /**  Rpt2RevalueBal  */  
   Rpt2RevalueBal:number,
      /**  Rpt3RevalueBal  */  
   Rpt3RevalueBal:number,
      /**  BankID  */  
   BankID:string,
      /**  BankPaidAmt  */  
   BankPaidAmt:number,
      /**  DocBankPaidAmt  */  
   DocBankPaidAmt:number,
      /**  Rpt1BankPaidAmt  */  
   Rpt1BankPaidAmt:number,
      /**  Rpt2BankPaidAmt  */  
   Rpt2BankPaidAmt:number,
      /**  Rpt3BankPaidAmt  */  
   Rpt3BankPaidAmt:number,
      /**  AdjLegalNumber  */  
   AdjLegalNumber:string,
      /**  AdjTranDocTypeID  */  
   AdjTranDocTypeID:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MainSite  */  
   MainSite:boolean,
      /**  SiteCode  */  
   SiteCode:string,
      /**  BranchID  */  
   BranchID:string,
      /**  InvoiceDate  */  
   InvoiceDate:string,
      /**  Remarks  */  
   Remarks:string,
      /**  AssetTypeCode  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  CreditCard  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  CardID  */  
   CardID:string,
      /**  CardHolderTaxID  */  
   CardHolderTaxID:string,
      /**  CardMemberName  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  NonDeductAmt  */  
   NonDeductAmt:number,
      /**  NonDeductDocAmt  */  
   NonDeductDocAmt:number,
      /**  NonDeductRpt1Amt  */  
   NonDeductRpt1Amt:number,
      /**  NonDeductRpt2Amt  */  
   NonDeductRpt2Amt:number,
      /**  NonDeductRpt3Amt  */  
   NonDeductRpt3Amt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankFileImportParamRow{
   Company:string,
   GroupID:string,
   EFTHeadUID:number,
   EFTHeadName:string,
   ImportFile:string,
   ImportFormat:string,
   ClientImportFileName:string,
   ServerImportFileName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankFileImportParamTableset{
   BankFileImportParam:Erp_Tablesets_BankFileImportParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CheckHedImportRow{
      /**  Company  */  
   Company:string,
      /**  Posted  */  
   Posted:boolean,
      /**  GroupID  */  
   GroupID:string,
      /**  HeadNum  */  
   HeadNum:number,
      /**  BankAcctID  */  
   BankAcctID:string,
      /**  CheckNum  */  
   CheckNum:number,
      /**  CheckDate  */  
   CheckDate:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  Voided  */  
   Voided:boolean,
      /**  CheckSrc  */  
   CheckSrc:string,
      /**  ClearedCheck  */  
   ClearedCheck:boolean,
      /**  ClearedPending  */  
   ClearedPending:boolean,
      /**  ClearedAmt  */  
   ClearedAmt:number,
      /**  DocClearedAmt  */  
   DocClearedAmt:number,
      /**  ClearedPerson  */  
   ClearedPerson:string,
      /**  ClearedDate  */  
   ClearedDate:string,
      /**  ClearedTime  */  
   ClearedTime:string,
      /**  ClearedStmtEndDate  */  
   ClearedStmtEndDate:string,
      /**  EmployeeNum  */  
   EmployeeNum:string,
      /**  CheckAmt  */  
   CheckAmt:number,
      /**  DocCheckAmt  */  
   DocCheckAmt:number,
      /**  ManualPrint  */  
   ManualPrint:boolean,
      /**  EntryPerson  */  
   EntryPerson:string,
      /**  VendorNum  */  
   VendorNum:number,
      /**  Name  */  
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
      /**  ZIP  */  
   ZIP:string,
      /**  Country  */  
   Country:string,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  ExchangeRate  */  
   ExchangeRate:number,
      /**  CountryNum  */  
   CountryNum:number,
      /**  BankSlip  */  
   BankSlip:string,
      /**  ElecPayment  */  
   ElecPayment:boolean,
      /**  VendorBankID  */  
   VendorBankID:string,
      /**  VendorBankName  */  
   VendorBankName:string,
      /**  VendorBankNameOnAccount  */  
   VendorBankNameOnAccount:string,
      /**  VendorBankAddress1  */  
   VendorBankAddress1:string,
      /**  VendorBankAddress2  */  
   VendorBankAddress2:string,
      /**  VendorBankAddress3  */  
   VendorBankAddress3:string,
      /**  VendorBankCity  */  
   VendorBankCity:string,
      /**  VendorBankState  */  
   VendorBankState:string,
      /**  VendorBankPostalCode  */  
   VendorBankPostalCode:string,
      /**  VendorBankCountryNum  */  
   VendorBankCountryNum:number,
      /**  VendorBankAcctNumber  */  
   VendorBankAcctNumber:string,
      /**  VendorBankSwiftNum  */  
   VendorBankSwiftNum:string,
      /**  CashBookNum  */  
   CashBookNum:number,
      /**  CashbookLine  */  
   CashbookLine:number,
      /**  XRefCheckNum  */  
   XRefCheckNum:string,
      /**  Rpt1CheckAmt  */  
   Rpt1CheckAmt:number,
      /**  Rpt2CheckAmt  */  
   Rpt2CheckAmt:number,
      /**  Rpt3CheckAmt  */  
   Rpt3CheckAmt:number,
      /**  Rpt1ClearedAmt  */  
   Rpt1ClearedAmt:number,
      /**  Rpt2ClearedAmt  */  
   Rpt2ClearedAmt:number,
      /**  Rpt3ClearedAmt  */  
   Rpt3ClearedAmt:number,
      /**  RateGrpCode  */  
   RateGrpCode:string,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  PaymentTotal  */  
   PaymentTotal:number,
      /**  DocPaymentTotal  */  
   DocPaymentTotal:number,
      /**  Rpt1PaymentTotal  */  
   Rpt1PaymentTotal:number,
      /**  Rpt2PaymentTotal  */  
   Rpt2PaymentTotal:number,
      /**  Rpt3PaymentTotal  */  
   Rpt3PaymentTotal:number,
      /**  Variance  */  
   Variance:number,
      /**  DocVariance  */  
   DocVariance:number,
      /**  Rpt1Variance  */  
   Rpt1Variance:number,
      /**  Rpt2Variance  */  
   Rpt2Variance:number,
      /**  Rpt3Variance  */  
   Rpt3Variance:number,
      /**  PaymentBankRate  */  
   PaymentBankRate:number,
      /**  BankTotalAmt  */  
   BankTotalAmt:number,
      /**  IsEnterTotal  */  
   IsEnterTotal:boolean,
      /**  LockRate  */  
   LockRate:number,
      /**  ReadyToCalc  */  
   ReadyToCalc:boolean,
      /**  RecalcBeforePost  */  
   RecalcBeforePost:boolean,
      /**  UsePendAcct  */  
   UsePendAcct:boolean,
      /**  ForceDiscount  */  
   ForceDiscount:boolean,
      /**  FirstHeadNum  */  
   FirstHeadNum:number,
      /**  ApplyingPayment  */  
   ApplyingPayment:boolean,
      /**  Plant  */  
   Plant:string,
      /**  InvoiceNum  */  
   InvoiceNum:string,
      /**  PMUID  */  
   PMUID:number,
      /**  PCashDeskID  */  
   PCashDeskID:string,
      /**  BankTranID  */  
   BankTranID:string,
      /**  PCashRefNum  */  
   PCashRefNum:number,
      /**  BankPaidAmt  */  
   BankPaidAmt:number,
      /**  DocBankPaidAmt  */  
   DocBankPaidAmt:number,
      /**  Rpt1BankPaidAmt  */  
   Rpt1BankPaidAmt:number,
      /**  Rpt2BankPaidAmt  */  
   Rpt2BankPaidAmt:number,
      /**  Rpt3BankPaidAmt  */  
   Rpt3BankPaidAmt:number,
      /**  BankTransDate  */  
   BankTransDate:string,
      /**  VendorID  */  
   VendorID:string,
      /**  TranType  */  
   TranType:string,
      /**  StatusDesc  */  
   StatusDesc:string,
      /**  TransText  */  
   TransText:string,
      /**  TransDetail  */  
   TransDetail:string,
      /**  OrigInvoiceNum  */  
   OrigInvoiceNum:string,
      /**  OrigName  */  
   OrigName:string,
      /**  OrigVendorID  */  
   OrigVendorID:string,
      /**  PropGroupID  */  
   PropGroupID:string,
      /**  NumPayment  */  
   NumPayment:number,
      /**  CheckHeadNum  */  
   CheckHeadNum:number,
      /**  OrigVendorNum  */  
   OrigVendorNum:number,
      /**  Matched  */  
   Matched:boolean,
      /**  OKToMatch  */  
   OKToMatch:boolean,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  SavedInvoiceNum  */  
   SavedInvoiceNum:string,
      /**  SavedVendorName  */  
   SavedVendorName:string,
      /**  SavedVendorID  */  
   SavedVendorID:string,
      /**  SavedVendorNum  */  
   SavedVendorNum:number,
      /**  CheckStatus  */  
   CheckStatus:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  NOPaymentStatus  */  
   NOPaymentStatus:number,
      /**  NOPaymentDirection  */  
   NOPaymentDirection:string,
      /**  NOPaymentType  */  
   NOPaymentType:string,
      /**  NOTransferFileName  */  
   NOTransferFileName:string,
      /**  NOBankTransRef  */  
   NOBankTransRef:string,
      /**  BalanceUpdate  */  
   BalanceUpdate:number,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  BankRecGainLoss  */  
   BankRecGainLoss:number,
      /**  BOEInvoiceNum  */  
   BOEInvoiceNum:string,
      /**  DocBankRecGainLoss  */  
   DocBankRecGainLoss:number,
      /**  MsgId  */  
   MsgId:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  PayLegalNumber  */  
   PayLegalNumber:string,
      /**  PayTranDocTypeID  */  
   PayTranDocTypeID:string,
      /**  Rpt1BankRecGainLoss  */  
   Rpt1BankRecGainLoss:number,
      /**  Rpt2BankRecGainLoss  */  
   Rpt2BankRecGainLoss:number,
      /**  Rpt3BankRecGainLoss  */  
   Rpt3BankRecGainLoss:number,
      /**  TaxPaymInfo  */  
   TaxPaymInfo:string,
      /**  VoidLegalNumber  */  
   VoidLegalNumber:string,
      /**  VoidTranDocTypeID  */  
   VoidTranDocTypeID:string,
      /**  SEGrpNum  */  
   SEGrpNum:number,
      /**  SEReference  */  
   SEReference:string,
      /**  SEISGroupedPO3  */  
   SEISGroupedPO3:boolean,
      /**  SEISExported  */  
   SEISExported:boolean,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MXBankAcctNumber  */  
   MXBankAcctNumber:string,
      /**  MXBankIdentifier  */  
   MXBankIdentifier:string,
      /**  MXRFC  */  
   MXRFC:string,
      /**  BankBatchExcluded  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  SEPAPaymentDescription  */  
   SEPAPaymentDescription:string,
      /**  NOImportErrors  */  
   NOImportErrors:string,
      /**  THPayerType  */  
   THPayerType:number,
      /**  THRefInvoiceNum  */  
   THRefInvoiceNum:string,
      /**  THRefVendorNum  */  
   THRefVendorNum:number,
      /**  VoidedReason  */  
   VoidedReason:string,
      /**  RegulatoryReportingCode  */  
   RegulatoryReportingCode:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  TaxPointDate  */  
   TaxPointDate:string,
      /**  SEC  */  
   SEC:string,
      /**  ACHTranCode  */  
   ACHTranCode:number,
      /**  US1099KMerchCatCode  */  
   US1099KMerchCatCode:string,
      /**  US1099KGen  */  
   US1099KGen:boolean,
      /**  VendorBankBranchCode  */  
   VendorBankBranchCode:string,
      /**  NettingID  */  
   NettingID:number,
      /**  GL Description  */  
   Description:string,
      /**  GL Description for the Payment Voiding process  */  
   VoidDescription:string,
      /**  GL Description for AP - Apply Debit Memo/Prepayment  */  
   DMDescription:string,
      /**  MXDIOTTranType  */  
   MXDIOTTranType:string,
      /**  Transaction Detail, part 1  */  
   TransDetail1:string,
      /**  Transactoin Detail part 3  */  
   TransDetail3:string,
      /**  Transaction Detail part 4  */  
   TransDetail4:string,
      /**  Indicates if the amount of payment from the imported file is less than amount of  proposed  payment  */  
   UnderpayFlag:boolean,
      /**  Indicates if the amount of payment from the imported file is more than amount of  proposed  payment  */  
   OverpayFlag:boolean,
      /**  Transaction Detail, Part2  */  
   TransDetail2:string,
   CurrencyCurrSymbol:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CheckHedMatchedRow{
      /**  Company  */  
   Company:string,
      /**  Supplier Number  */  
   VendorNum:number,
      /**  Vendor ID  */  
   VendorID:string,
      /**  Supplier Name  */  
   Name:string,
      /**  Payment Group ID  */  
   GroupID:string,
      /**  Group ID of the proposed Payment  */  
   PrpGroupID:string,
      /**  HeadNum of the CheckHed matched  */  
   HeadNum:number,
      /**  Invoice Number for the payment matched  */  
   InvoiceNum:string,
   APTranNo:number,
   CheckDate:string,
      /**  Currency Code of the payment  */  
   CurrencyCode:string,
      /**  Payment amount  */  
   CheckAmt:number,
      /**  Check Amount in Document currency  */  
   DocCheckAmt:number,
   Rpt1CheckAmt:number,
   Rpt2CheckAmt:number,
   Rpt3CheckAmt:number,
      /**  Record number of the imported table matched  */  
   RecordNumber:number,
   Matched:string,
   CheckNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAPBankFileImportTableset{
   APChkGrpImport:Erp_Tablesets_APChkGrpImportRow[],
   APChkGrpImportAttch:Erp_Tablesets_APChkGrpImportAttchRow[],
   CheckHedImport:Erp_Tablesets_CheckHedImportRow[],
   APTranImport:Erp_Tablesets_APTranImportRow[],
   APPmtMatch:Erp_Tablesets_APPmtMatchRow[],
   CheckHedMatched:Erp_Tablesets_CheckHedMatchedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cGroupID
   */  
export interface GetBankFileImportParam_input{
      /**  The Payment Group ID  */  
   cGroupID:string,
}

export interface GetBankFileImportParam_output{
   returnObj:Erp_Tablesets_BankFileImportParamTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
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
   returnObj:Erp_Tablesets_APChkGrpImportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewAPChkGrpImportAttch_input{
   ds:Erp_Tablesets_APBankFileImportTableset[],
   groupID:string,
}

export interface GetNewAPChkGrpImportAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAPChkGrpImport_input{
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface GetNewAPChkGrpImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param ds
      @param headNum
      @param apTranImportNo
      @param invoiceNum
   */  
export interface GetNewAPTranImport_input{
   ds:Erp_Tablesets_APBankFileImportTableset[],
   headNum:number,
   apTranImportNo:number,
   invoiceNum:string,
}

export interface GetNewAPTranImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCheckHedImport_input{
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface GetNewCheckHedImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param whereClauseAPChkGrpImport
      @param whereClauseAPChkGrpImportAttch
      @param whereClauseCheckHedImport
      @param whereClauseAPTranImport
      @param whereClauseAPPmtMatch
      @param whereClauseCheckHedMatched
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPChkGrpImport:string,
   whereClauseAPChkGrpImportAttch:string,
   whereClauseCheckHedImport:string,
   whereClauseAPTranImport:string,
   whereClauseAPPmtMatch:string,
   whereClauseCheckHedMatched:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param groupID
   */  
export interface GetStatement_input{
      /**  Group ID  */  
   groupID:string,
}

export interface GetStatement_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
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
   */  
export interface ImportBankFile_input{
   ds:Erp_Tablesets_BankFileImportParamTableset[],
}

export interface ImportBankFile_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
}

   /** Required : 
      @param groupID
   */  
export interface LockGroup_input{
      /**  Selected Group ID  */  
   groupID:string,
}

export interface LockGroup_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcGroupID
   */  
export interface MatchPayments_input{
   pcGroupID:string,
}

export interface MatchPayments_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
}

   /** Required : 
      @param pcGroupID
   */  
export interface MatchTelepayPayments_input{
      /**  Group ID of the payment  */  
   pcGroupID:string,
}

export interface MatchTelepayPayments_output{
   returnObj:Erp_Tablesets_APBankFileImportTableset[],
parameters : {
      /**  output parameters  */  
   opMsg:string,
}
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface OnEnterGroupID_input{
      /**  Group ID of the paymnet  */  
   groupID:string,
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface OnEnterGroupID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param pcGroupID
      @param ds
   */  
export interface ProcessPayments_input{
      /**  Group ID of the paymnet  */  
   pcGroupID:string,
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface ProcessPayments_output{
parameters : {
      /**  output parameters  */  
   opMsg:string,
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

   /** Required : 
      @param groupID
   */  
export interface UnlockGroup_input{
      /**  The Group ID selected by the user.  */  
   groupID:string,
}

export interface UnlockGroup_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPBankFileImportTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPBankFileImportTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APBankFileImportTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBankFileImportTableset,
}
}

