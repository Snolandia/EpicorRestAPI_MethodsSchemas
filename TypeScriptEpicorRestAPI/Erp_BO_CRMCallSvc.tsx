import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CRMCallSvc
// Description: CRMCall Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/$metadata", {
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
   Description: Get CRMCalls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCalls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallRow
   */  
export function get_CRMCalls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCalls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CRMCallRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CRMCalls(requestBody:Erp_Tablesets_CRMCallRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls", {
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
   Summary: Calls GetByID to retrieve the CRMCall item
   Description: Calls GetByID to retrieve the CRMCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCall
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CRMCall for the service
   Description: Calls UpdateExt to update CRMCall. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCall
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, requestBody:Erp_Tablesets_CRMCallRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
   Summary: Call UpdateExt to delete CRMCall item
   Description: Call UpdateExt to delete CRMCall item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCall
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
   Description: Get CRMCallCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRMCallCnts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallCntRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallCnts(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallCnts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CRMCallCnt item
   Description: Calls GetByID to retrieve the CRMCallCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallCnt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallCntRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, PerConLnkRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CRMCallHistories items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRMCallHistories1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallHistoryRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallHistories(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallHistories", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CRMCallHistory item
   Description: Calls GetByID to retrieve the CRMCallHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallHistory1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CRMCallAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRMCallAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallAttchRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallAttches(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CRMCallAttch item
   Description: Calls GetByID to retrieve the CRMCallAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallAttchRow
   */  
export function get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CRMCallCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCallCnts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallCntRow
   */  
export function get_CRMCallCnts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCallCnts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CRMCallCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CRMCallCnts(requestBody:Erp_Tablesets_CRMCallCntRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts", {
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
   Summary: Calls GetByID to retrieve the CRMCallCnt item
   Description: Calls GetByID to retrieve the CRMCallCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallCntRow
   */  
export function get_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, PerConLnkRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallCntRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallCntRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CRMCallCnt for the service
   Description: Calls UpdateExt to update CRMCallCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCallCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, PerConLnkRowID:string, requestBody:Erp_Tablesets_CRMCallCntRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")", {
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
   Summary: Call UpdateExt to delete CRMCallCnt item
   Description: Call UpdateExt to delete CRMCallCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCallCnt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param PerConLnkRowID Desc: PerConLnkRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, PerConLnkRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")", {
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
   Description: Get CRMCallHistories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCallHistories
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallHistoryRow
   */  
export function get_CRMCallHistories(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCallHistories
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CRMCallHistoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CRMCallHistories(requestBody:Erp_Tablesets_CRMCallHistoryRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories", {
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
   Summary: Calls GetByID to retrieve the CRMCallHistory item
   Description: Calls GetByID to retrieve the CRMCallHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   */  
export function get_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallHistoryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallHistoryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CRMCallHistory for the service
   Description: Calls UpdateExt to update CRMCallHistory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCallHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, requestBody:Erp_Tablesets_CRMCallHistoryRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
   Summary: Call UpdateExt to delete CRMCallHistory item
   Description: Call UpdateExt to delete CRMCallHistory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCallHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", {
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
   Description: Get CRMCallAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCallAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallAttchRow
   */  
export function get_CRMCallAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCallAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CRMCallAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CRMCallAttches(requestBody:Erp_Tablesets_CRMCallAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches", {
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
   Summary: Calls GetByID to retrieve the CRMCallAttch item
   Description: Calls GetByID to retrieve the CRMCallAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRMCallAttchRow
   */  
export function get_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRMCallAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CRMCallAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CRMCallAttch for the service
   Description: Calls UpdateExt to update CRMCallAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCallAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_CRMCallAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CRMCallAttch item
   Description: Call UpdateExt to delete CRMCallAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCallAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param CallSeqNum Desc: CallSeqNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, CallSeqNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCRMCall:string, whereClauseCRMCallAttch:string, whereClauseCRMCallCnt:string, whereClauseCRMCallHistory:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCRMCall!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCRMCall=" + whereClauseCRMCall
   }
   if(typeof whereClauseCRMCallAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCRMCallAttch=" + whereClauseCRMCallAttch
   }
   if(typeof whereClauseCRMCallCnt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCRMCallCnt=" + whereClauseCRMCallCnt
   }
   if(typeof whereClauseCRMCallHistory!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCRMCallHistory=" + whereClauseCRMCallHistory
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(relatedToFile:string, key1:string, key2:string, key3:string, callSeqNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof relatedToFile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "relatedToFile=" + relatedToFile
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof callSeqNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "callSeqNum=" + callSeqNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetList" + params, {
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
   Summary: Invoke method ChangeConName
   Description: Update CRMCallCnt information when the contact Name is changed.
   OperationID: ChangeConName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeConName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConName(requestBody:ChangeConName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeConName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeConName", {
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
         resolve(data as ChangeConName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeConPerConLnkRowID
   Description: Update CRMCallCnt information when the contact PerConLnkRowID is changed.
   OperationID: ChangeConPerConLnkRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeConPerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConPerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConPerConLnkRowID(requestBody:ChangeConPerConLnkRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeConPerConLnkRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeConPerConLnkRowID", {
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
         resolve(data as ChangeConPerConLnkRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCustomerID
   Description: Update CRMCall information when the CustomerId is changed.
   OperationID: ChangeCustomerID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCustomerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomerID(requestBody:ChangeCustomerID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCustomerID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeCustomerID", {
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
         resolve(data as ChangeCustomerID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFSCallNum
   Description: Update CRMCall information when the FSCall Number is changed.
   OperationID: ChangeFSCallNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFSCallNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSCallNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFSCallNum(requestBody:ChangeFSCallNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFSCallNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeFSCallNum", {
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
         resolve(data as ChangeFSCallNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeHDCaseNum
   Description: Update CRMCall information when the Case Number is changed.
   OperationID: ChangeHDCaseNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeHDCaseNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHDCaseNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHDCaseNum(requestBody:ChangeHDCaseNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeHDCaseNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeHDCaseNum", {
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
         resolve(data as ChangeHDCaseNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceNum
   Description: Update CRMCall information when the AR Invoice Number is changed.
   OperationID: ChangeInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceNum(requestBody:ChangeInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeInvoiceNum", {
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
         resolve(data as ChangeInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderNum
   Description: Update CRMCall information when the Order Number is changed.
   OperationID: ChangeOrderNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderNum(requestBody:ChangeOrderNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeOrderNum", {
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
         resolve(data as ChangeOrderNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePurPoint
   Description: Update CRMCall information when the Purchase Point is changed.
   OperationID: ChangePurPoint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePurPoint(requestBody:ChangePurPoint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePurPoint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangePurPoint", {
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
         resolve(data as ChangePurPoint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuoteNum
   Description: Update CRMCall information when the Quote Number is changed.
   OperationID: ChangeQuoteNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuoteNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuoteNum(requestBody:ChangeQuoteNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuoteNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeQuoteNum", {
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
         resolve(data as ChangeQuoteNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProjectID
   Description: Update CRMCall information when the Project ID is changed.
   OperationID: ChangeProjectID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProjectID(requestBody:ChangeProjectID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProjectID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeProjectID", {
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
         resolve(data as ChangeProjectID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRMANum
   Description: Update CRMCall information when the RMA Number is changed.
   OperationID: ChangeRMANum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRMANum(requestBody:ChangeRMANum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRMANum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeRMANum", {
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
         resolve(data as ChangeRMANum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipToNum
   Description: Update CRMCall information when the ShipToNum is changed.
   OperationID: ChangeShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToNum(requestBody:ChangeShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeShipToNum", {
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
         resolve(data as ChangeShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTaskID
   Description: Update CRMCall information when the Task ID is changed.
   OperationID: ChangeTaskID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTaskID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaskID(requestBody:ChangeTaskID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTaskID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeTaskID", {
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
         resolve(data as ChangeTaskID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendorID
   Description: Update CRMCall information when the VendorID (Supplier ID) is changed.
   OperationID: ChangeVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendorID(requestBody:ChangeVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/ChangeVendorID", {
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
         resolve(data as ChangeVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCRMCallBySysRowID
   Description: Get CRMCall by SysRowID after refresh.
   OperationID: GetCRMCallBySysRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCRMCallBySysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMCallBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCRMCallBySysRowID(requestBody:GetCRMCallBySysRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCRMCallBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetCRMCallBySysRowID", {
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
         resolve(data as GetCRMCallBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultContactFields
   Description: Update CRMCall information when the contact is changed.
   OperationID: DefaultContactFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultContactFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultContactFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultContactFields(requestBody:DefaultContactFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultContactFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/DefaultContactFields", {
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
         resolve(data as DefaultContactFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultSupplierCntFields
   Description: Update CRMCall information when the supplier contact is changed.
   OperationID: DefaultSupplierCntFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultSupplierCntFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultSupplierCntFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultSupplierCntFields(requestBody:DefaultSupplierCntFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultSupplierCntFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/DefaultSupplierCntFields", {
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
         resolve(data as DefaultSupplierCntFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCRMCallsToShow
   Description: Gets the number of CRM Calls to show at startup according to the Company settings.
   OperationID: GetCRMCallsToShow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMCallsToShow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCRMCallsToShow(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCRMCallsToShow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetCRMCallsToShow", {
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
         resolve(data as GetCRMCallsToShow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker for better performance.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetRowsContactTracker", {
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
   Summary: Invoke method GetRowsCustomerTracker
   Description: Called from Customer tracker for better performance.
   OperationID: GetRowsCustomerTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:GetRowsCustomerTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCustomerTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetRowsCustomerTracker", {
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
         resolve(data as GetRowsCustomerTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsForPerson
   Description: Gets the list of calls where the DcdUserID is an authorized user for the Workforce specified in the call.
   OperationID: GetRowsForPerson
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsForPerson_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPerson_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForPerson(requestBody:GetRowsForPerson_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsForPerson_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetRowsForPerson", {
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
         resolve(data as GetRowsForPerson_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFilteredRowsForPerson
   Description: Gets the list of calls where the DcdUserID is an authorized user for the Workforce specified in the call.
   OperationID: GetFilteredRowsForPerson
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFilteredRowsForPerson_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFilteredRowsForPerson_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFilteredRowsForPerson(requestBody:GetFilteredRowsForPerson_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFilteredRowsForPerson_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetFilteredRowsForPerson", {
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
         resolve(data as GetFilteredRowsForPerson_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SortByData
   Description: Return a list of the sort by options based on the data passed in.
   OperationID: SortByData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SortByData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SortByData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SortByData(requestBody:SortByData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SortByData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/SortByData", {
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
         resolve(data as SortByData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UserIsAuthorized
   Description: Checks if user is authorized
   OperationID: UserIsAuthorized
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UserIsAuthorized_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UserIsAuthorized_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserIsAuthorized(requestBody:UserIsAuthorized_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UserIsAuthorized_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/UserIsAuthorized", {
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
         resolve(data as UserIsAuthorized_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCRMSummarize
   Description: Summarizes CRM call text/description for the rows in the input dataset
   OperationID: GetCRMSummarize
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCRMSummarize_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMSummarize_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCRMSummarize(requestBody:GetCRMSummarize_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCRMSummarize_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetCRMSummarize", {
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
         resolve(data as GetCRMSummarize_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCRMCall
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCall
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCRMCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCRMCall(requestBody:GetNewCRMCall_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCRMCall_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetNewCRMCall", {
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
         resolve(data as GetNewCRMCall_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCRMCallAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCallAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCRMCallAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCallAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCRMCallAttch(requestBody:GetNewCRMCallAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCRMCallAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetNewCRMCallAttch", {
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
         resolve(data as GetNewCRMCallAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCRMCallCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCallCnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCRMCallCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCallCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCRMCallCnt(requestBody:GetNewCRMCallCnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCRMCallCnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetNewCRMCallCnt", {
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
         resolve(data as GetNewCRMCallCnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCRMCallHistory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCallHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCRMCallHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCallHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCRMCallHistory(requestBody:GetNewCRMCallHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCRMCallHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetNewCRMCallHistory", {
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
         resolve(data as GetNewCRMCallHistory_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CRMCallAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallCntRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CRMCallCntRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallHistoryRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CRMCallHistoryRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CRMCallListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CRMCallRow,
}

export interface Erp_Tablesets_CRMCallAttchRow{
   "Company":string,
   "RelatedToFile":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "CallSeqNum":number,
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

export interface Erp_Tablesets_CRMCallCntRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The master file to which the PCE is related to. This field is used to properly isolate PCE's to the master table they are related to.
records.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   "Key3":string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "CallSeqNum":number,
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
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "BuyerID":string,
   "BuyerName":string,
   "City":string,
   "ContextLink":string,
   "CustID":string,
   "CustName":string,
   "EmpID":string,
   "EmpName":string,
   "Name":string,
   "PurPoint":string,
   "PurPointName":string,
   "SalesRepCode":string,
   "SalesRepName":string,
   "ShipToName":string,
   "ShipToNum":string,
   "State":string,
   "VendorID":string,
   "VendorName":string,
   "Zip":string,
   "PerConID":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CRMCallHistoryRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   "Key3":string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "CallSeqNum":number,
      /**  An abbreviated description of what the Call is about.  */  
   "CallDesc":string,
      /**  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  */  
   "CallText":string,
      /**  The Salesperson that owns this PCE  */  
   "SalesRepCode":string,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   "CallTypeCode":string,
      /**   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  */  
   "CallContactType":string,
      /**  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  */  
   "CallCustNum":number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  */  
   "CallShipToNum":string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to.  */  
   "CallConNum":number,
      /**  This key links the record to the Vendor file.  */  
   "CallVendorNum":number,
      /**  Purchase point of linked Vendor  */  
   "CallPurPoint":string,
      /**  Used to uniquely identify the contact record for the related vendor or purchase point.  */  
   "CallVConNum":number,
      /**  The DCD user ID that created the record  */  
   "OrigDcdUserID":string,
      /**  The DCD user ID that last updated the record  */  
   "LastDcdUserID":string,
      /**  The date the PCE was created.  */  
   "OrigDate":string,
      /**  The time the PCE was created.  */  
   "OrigTime":number,
      /**  The date the PCE was last modified.  */  
   "LastDate":string,
      /**  The time the PCE was last modified.  */  
   "LastTime":number,
      /**  The Quote that this call is related to.  */  
   "CallQuoteNum":number,
      /**  The Quote line that this Call is related to.  */  
   "CallQuoteLine":number,
   "CallTypeDescription":string,
   "SalesRepName":string,
   "ContactName":string,
   "ContactEmail":string,
   "ContactPhone":string,
   "ContactFax":string,
   "TaskDescription":string,
   "HistorySeqNum":number,
   "HistoryCallSeqNum":number,
   "HistoryRelatedToFile":string,
   "DispOrigTime":string,
   "DispLastTime":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CallCustNumName":string,
   "CallCustNumCustID":string,
   "CallCustNumBTName":string,
   "CallTypeCodeCallTypeDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CRMCallListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   "RelatedToFile":string,
   "DisplayOrigTime":string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   "Key3":string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "CallSeqNum":number,
      /**  An abbreviated description of what the Call is about.  */  
   "CallDesc":string,
      /**  The Salesperson that owns this PCE  */  
   "SalesRepCode":string,
   "SalesRepName":string,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   "CallTypeCode":string,
   "TaskDescription":string,
      /**  The DCD user ID that created the record  */  
   "OrigDcdUserID":string,
      /**  The DCD user ID that last updated the record  */  
   "LastDcdUserID":string,
      /**  The date the PCE was created.  */  
   "OrigDate":string,
      /**  The time the PCE was created.  */  
   "OrigTime":number,
      /**  The date the PCE was last modified.  */  
   "LastDate":string,
      /**  The Quote that this call is related to.  */  
   "CallQuoteNum":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CallTypeCodeCallTypeDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CRMCallRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   "Key3":string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   "CallSeqNum":number,
      /**  An abbreviated description of what the Call is about.  */  
   "CallDesc":string,
      /**  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  */  
   "CallText":string,
      /**  The Salesperson that owns this PCE  */  
   "SalesRepCode":string,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   "CallTypeCode":string,
      /**   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  */  
   "CallContactType":string,
      /**  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  */  
   "CallCustNum":number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  */  
   "CallShipToNum":string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to.  */  
   "CallConNum":number,
      /**  This key links the record to the Vendor file.  */  
   "CallVendorNum":number,
      /**  Purchase point of linked Vendor  */  
   "CallPurPoint":string,
      /**  Used to uniquely identify the contact record for the related vendor or purchase point.  */  
   "CallVConNum":number,
      /**  The DCD user ID that created the record  */  
   "OrigDcdUserID":string,
      /**  The DCD user ID that last updated the record  */  
   "LastDcdUserID":string,
      /**  The date the PCE was created.  */  
   "OrigDate":string,
      /**  The time the PCE was created.  */  
   "OrigTime":number,
      /**  The date the PCE was last modified.  */  
   "LastDate":string,
      /**  The time the PCE was last modified.  */  
   "LastTime":number,
      /**  The Quote that this call is related to.  */  
   "CallQuoteNum":number,
      /**  The Quote line that this Call is related to.  */  
   "CallQuoteLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unique identifier of the primary Employee contact.  */  
   "CallEmpID":string,
      /**  Unique identifier of the primary Buyer contact.  */  
   "CallBuyerID":string,
      /**  The sales order the call is related to.  */  
   "CallOrderNum":number,
      /**  The invoice the call is related to.  */  
   "CallInvoiceNum":number,
      /**  The RMA this call is related to.  */  
   "CallRMANum":number,
      /**  The field service call this CRM call is related to.  */  
   "CallFSCallNum":number,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  CallHDCaseNum  */  
   "CallHDCaseNum":number,
      /**  CallTaskID  */  
   "CallTaskID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CallPerConID  */  
   "CallPerConID":number,
      /**  RelatedToSysRowID  */  
   "RelatedToSysRowID":string,
      /**  CallProjectID  */  
   "CallProjectID":string,
      /**  Name of the purchase point.  */  
   "CallPurPointName":string,
      /**  The name for the ship to location.  */  
   "CallShipToName":string,
   "CallTaskDescription":string,
   "CallTypeDescription":string,
   "ContactEmail":string,
   "ContactFax":string,
      /**  The contact's name.  */  
   "ContactName":string,
   "ContactPhone":string,
   "DispLastTime":string,
   "DispOrigTime":string,
   "NextRelatedTo":string,
      /**  Name of the sales representative.  */  
   "SalesRepName":string,
   "TaskDescription":string,
   "VContactEmail":string,
   "VContactFax":string,
   "VContactName":string,
   "VContactPhone":string,
   "CallKeys":string,
   "BitFlag":number,
   "CallCustNumInactive":boolean,
   "CallCustNumBTName":string,
   "CallCustNumName":string,
   "CallCustNumCustID":string,
   "CallShipToNumInactive":boolean,
   "CallTypeCodeCallTypeDesc":string,
   "CallVendorNumDefaultFOB":string,
   "CallVendorNumVendorID":string,
   "CallVendorNumAddress1":string,
   "CallVendorNumZIP":string,
   "CallVendorNumState":string,
   "CallVendorNumCurrencyCode":string,
   "CallVendorNumTermsCode":string,
   "CallVendorNumAddress3":string,
   "CallVendorNumCity":string,
   "CallVendorNumAddress2":string,
   "CallVendorNumName":string,
   "CallVendorNumCountry":string,
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
      @param pName
      @param ds
   */  
export interface ChangeConName_input{
      /**  Proposed Name  */  
   pName:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeConName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pPerConLnkRowID
      @param ds
   */  
export interface ChangeConPerConLnkRowID_input{
      /**  Proposed PerConLnkRowID  */  
   pPerConLnkRowID:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeConPerConLnkRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pCustomerId
      @param ds
   */  
export interface ChangeCustomerID_input{
      /**  Proposed Customer ID  */  
   pCustomerId:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeCustomerID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pFSCallNum
      @param ds
   */  
export interface ChangeFSCallNum_input{
      /**  Proposed FSCall Number  */  
   pFSCallNum:number,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeFSCallNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pHDCaseNum
      @param ds
   */  
export interface ChangeHDCaseNum_input{
      /**  Proposed Case Number  */  
   pHDCaseNum:number,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeHDCaseNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pInvoiceNum
      @param ds
   */  
export interface ChangeInvoiceNum_input{
      /**  Proposed Invoice Number  */  
   pInvoiceNum:number,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pOrderNum
      @param ds
   */  
export interface ChangeOrderNum_input{
      /**  Proposed Order Number  */  
   pOrderNum:number,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param projectID
      @param ds
   */  
export interface ChangeProjectID_input{
      /**  Proposed Project ID  */  
   projectID:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pVendorNum
      @param pPurPoint
      @param ds
   */  
export interface ChangePurPoint_input{
      /**  Proposed Supplier number.  */  
   pVendorNum:number,
      /**  Proposed purchase point..  */  
   pPurPoint:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pQuoteNum
      @param ds
   */  
export interface ChangeQuoteNum_input{
      /**  Proposed Quote Number  */  
   pQuoteNum:number,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeQuoteNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pRMANum
      @param ds
   */  
export interface ChangeRMANum_input{
      /**  Proposed RMA Number  */  
   pRMANum:number,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeRMANum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pCustNum
      @param pShipToNum
      @param ds
   */  
export interface ChangeShipToNum_input{
      /**  Proposed Customer number.  */  
   pCustNum:number,
      /**  Proposed Ship To number.  */  
   pShipToNum:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pTaskID
      @param ds
   */  
export interface ChangeTaskID_input{
      /**  Proposed Task ID  */  
   pTaskID:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeTaskID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param pVendorID
      @param ds
   */  
export interface ChangeVendorID_input{
      /**  Proposed Supplier ID  */  
   pVendorID:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface ChangeVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultContactFields_input{
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface DefaultContactFields_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DefaultSupplierCntFields_input{
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface DefaultSupplierCntFields_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param callSeqNum
   */  
export interface DeleteByID_input{
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   callSeqNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CRMCallAttchRow{
   Company:string,
   RelatedToFile:string,
   Key1:string,
   Key2:string,
   Key3:string,
   CallSeqNum:number,
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

export interface Erp_Tablesets_CRMCallCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The master file to which the PCE is related to. This field is used to properly isolate PCE's to the master table they are related to.
records.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   Key3:string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   CallSeqNum:number,
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
   Address1:string,
   Address2:string,
   Address3:string,
   BuyerID:string,
   BuyerName:string,
   City:string,
   ContextLink:string,
   CustID:string,
   CustName:string,
   EmpID:string,
   EmpName:string,
   Name:string,
   PurPoint:string,
   PurPointName:string,
   SalesRepCode:string,
   SalesRepName:string,
   ShipToName:string,
   ShipToNum:string,
   State:string,
   VendorID:string,
   VendorName:string,
   Zip:string,
   PerConID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CRMCallHistoryRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   Key3:string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   CallSeqNum:number,
      /**  An abbreviated description of what the Call is about.  */  
   CallDesc:string,
      /**  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  */  
   CallText:string,
      /**  The Salesperson that owns this PCE  */  
   SalesRepCode:string,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   CallTypeCode:string,
      /**   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  */  
   CallContactType:string,
      /**  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  */  
   CallCustNum:number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  */  
   CallShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to.  */  
   CallConNum:number,
      /**  This key links the record to the Vendor file.  */  
   CallVendorNum:number,
      /**  Purchase point of linked Vendor  */  
   CallPurPoint:string,
      /**  Used to uniquely identify the contact record for the related vendor or purchase point.  */  
   CallVConNum:number,
      /**  The DCD user ID that created the record  */  
   OrigDcdUserID:string,
      /**  The DCD user ID that last updated the record  */  
   LastDcdUserID:string,
      /**  The date the PCE was created.  */  
   OrigDate:string,
      /**  The time the PCE was created.  */  
   OrigTime:number,
      /**  The date the PCE was last modified.  */  
   LastDate:string,
      /**  The time the PCE was last modified.  */  
   LastTime:number,
      /**  The Quote that this call is related to.  */  
   CallQuoteNum:number,
      /**  The Quote line that this Call is related to.  */  
   CallQuoteLine:number,
   CallTypeDescription:string,
   SalesRepName:string,
   ContactName:string,
   ContactEmail:string,
   ContactPhone:string,
   ContactFax:string,
   TaskDescription:string,
   HistorySeqNum:number,
   HistoryCallSeqNum:number,
   HistoryRelatedToFile:string,
   DispOrigTime:string,
   DispLastTime:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CallCustNumName:string,
   CallCustNumCustID:string,
   CallCustNumBTName:string,
   CallTypeCodeCallTypeDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CRMCallListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   RelatedToFile:string,
   DisplayOrigTime:string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   Key3:string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   CallSeqNum:number,
      /**  An abbreviated description of what the Call is about.  */  
   CallDesc:string,
      /**  The Salesperson that owns this PCE  */  
   SalesRepCode:string,
   SalesRepName:string,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   CallTypeCode:string,
   TaskDescription:string,
      /**  The DCD user ID that created the record  */  
   OrigDcdUserID:string,
      /**  The DCD user ID that last updated the record  */  
   LastDcdUserID:string,
      /**  The date the PCE was created.  */  
   OrigDate:string,
      /**  The time the PCE was created.  */  
   OrigTime:number,
      /**  The date the PCE was last modified.  */  
   LastDate:string,
      /**  The Quote that this call is related to.  */  
   CallQuoteNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CallTypeCodeCallTypeDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CRMCallListTableset{
   CRMCallList:Erp_Tablesets_CRMCallListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CRMCallRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   Key3:string,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   CallSeqNum:number,
      /**  An abbreviated description of what the Call is about.  */  
   CallDesc:string,
      /**  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  */  
   CallText:string,
      /**  The Salesperson that owns this PCE  */  
   SalesRepCode:string,
      /**  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  */  
   CallTypeCode:string,
      /**   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  */  
   CallContactType:string,
      /**  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  */  
   CallCustNum:number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  */  
   CallShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to.  */  
   CallConNum:number,
      /**  This key links the record to the Vendor file.  */  
   CallVendorNum:number,
      /**  Purchase point of linked Vendor  */  
   CallPurPoint:string,
      /**  Used to uniquely identify the contact record for the related vendor or purchase point.  */  
   CallVConNum:number,
      /**  The DCD user ID that created the record  */  
   OrigDcdUserID:string,
      /**  The DCD user ID that last updated the record  */  
   LastDcdUserID:string,
      /**  The date the PCE was created.  */  
   OrigDate:string,
      /**  The time the PCE was created.  */  
   OrigTime:number,
      /**  The date the PCE was last modified.  */  
   LastDate:string,
      /**  The time the PCE was last modified.  */  
   LastTime:number,
      /**  The Quote that this call is related to.  */  
   CallQuoteNum:number,
      /**  The Quote line that this Call is related to.  */  
   CallQuoteLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unique identifier of the primary Employee contact.  */  
   CallEmpID:string,
      /**  Unique identifier of the primary Buyer contact.  */  
   CallBuyerID:string,
      /**  The sales order the call is related to.  */  
   CallOrderNum:number,
      /**  The invoice the call is related to.  */  
   CallInvoiceNum:number,
      /**  The RMA this call is related to.  */  
   CallRMANum:number,
      /**  The field service call this CRM call is related to.  */  
   CallFSCallNum:number,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  CallHDCaseNum  */  
   CallHDCaseNum:number,
      /**  CallTaskID  */  
   CallTaskID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CallPerConID  */  
   CallPerConID:number,
      /**  RelatedToSysRowID  */  
   RelatedToSysRowID:string,
      /**  CallProjectID  */  
   CallProjectID:string,
      /**  Name of the purchase point.  */  
   CallPurPointName:string,
      /**  The name for the ship to location.  */  
   CallShipToName:string,
   CallTaskDescription:string,
   CallTypeDescription:string,
   ContactEmail:string,
   ContactFax:string,
      /**  The contact's name.  */  
   ContactName:string,
   ContactPhone:string,
   DispLastTime:string,
   DispOrigTime:string,
   NextRelatedTo:string,
      /**  Name of the sales representative.  */  
   SalesRepName:string,
   TaskDescription:string,
   VContactEmail:string,
   VContactFax:string,
   VContactName:string,
   VContactPhone:string,
   CallKeys:string,
   BitFlag:number,
   CallCustNumInactive:boolean,
   CallCustNumBTName:string,
   CallCustNumName:string,
   CallCustNumCustID:string,
   CallShipToNumInactive:boolean,
   CallTypeCodeCallTypeDesc:string,
   CallVendorNumDefaultFOB:string,
   CallVendorNumVendorID:string,
   CallVendorNumAddress1:string,
   CallVendorNumZIP:string,
   CallVendorNumState:string,
   CallVendorNumCurrencyCode:string,
   CallVendorNumTermsCode:string,
   CallVendorNumAddress3:string,
   CallVendorNumCity:string,
   CallVendorNumAddress2:string,
   CallVendorNumName:string,
   CallVendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CRMCallTableset{
   CRMCall:Erp_Tablesets_CRMCallRow[],
   CRMCallAttch:Erp_Tablesets_CRMCallAttchRow[],
   CRMCallCnt:Erp_Tablesets_CRMCallCntRow[],
   CRMCallHistory:Erp_Tablesets_CRMCallHistoryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCRMCallTableset{
   CRMCall:Erp_Tablesets_CRMCallRow[],
   CRMCallAttch:Erp_Tablesets_CRMCallAttchRow[],
   CRMCallCnt:Erp_Tablesets_CRMCallCntRow[],
   CRMCallHistory:Erp_Tablesets_CRMCallHistoryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param callSeqNum
   */  
export interface GetByID_input{
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   callSeqNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
}

   /** Required : 
      @param sysRowID
      @param ds
   */  
export interface GetCRMCallBySysRowID_input{
      /**  SysRowID  */  
   sysRowID:string,
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface GetCRMCallBySysRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

export interface GetCRMCallsToShow_output{
parameters : {
      /**  output parameters  */  
   crmCallsToShow:number,
}
}

   /** Required : 
      @param ds
   */  
export interface GetCRMSummarize_input{
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface GetCRMSummarize_output{
parameters : {
      /**  output parameters  */  
   summarizedString:string,
}
}

   /** Required : 
      @param whereClause
      @param startingAt
      @param pageSize
      @param absolutePage
   */  
export interface GetFilteredRowsForPerson_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   startingAt:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetFilteredRowsForPerson_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
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
   returnObj:Erp_Tablesets_CRMCallListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param callSeqNum
   */  
export interface GetNewCRMCallAttch_input{
   ds:Erp_Tablesets_CRMCallTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   callSeqNum:number,
}

export interface GetNewCRMCallAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param callSeqNum
   */  
export interface GetNewCRMCallCnt_input{
   ds:Erp_Tablesets_CRMCallTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   callSeqNum:number,
}

export interface GetNewCRMCallCnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
   */  
export interface GetNewCRMCallHistory_input{
   ds:Erp_Tablesets_CRMCallTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetNewCRMCallHistory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
   */  
export interface GetNewCRMCall_input{
   ds:Erp_Tablesets_CRMCallTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetNewCRMCall_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param whereClauseCRMCall
      @param whereClauseCRMCallHistory
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for CRMCall table.  */  
   whereClauseCRMCall:string,
      /**  Whereclause for CRMCallHistory table.  */  
   whereClauseCRMCallHistory:string,
      /**  The contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCRMCall
      @param whereClauseCRMCallHistory
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for CRMCall table.  */  
   whereClauseCRMCall:string,
      /**  Whereclause for CRMCallHistory table.  */  
   whereClauseCRMCallHistory:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param startingAt
      @param hDCaseNum
      @param pageSize
      @param absolutePage
      @param orderBy
   */  
export interface GetRowsForPerson_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   startingAt:string,
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   hDCaseNum:number,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
   orderBy:string,
}

export interface GetRowsForPerson_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseCRMCall
      @param whereClauseCRMCallAttch
      @param whereClauseCRMCallCnt
      @param whereClauseCRMCallHistory
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCRMCall:string,
   whereClauseCRMCallAttch:string,
   whereClauseCRMCallCnt:string,
   whereClauseCRMCallHistory:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CRMCallTableset[],
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
      @param cTableName
      @param iCustNum
      @param iQuoteNum
      @param iVendorNum
   */  
export interface SortByData_input{
      /**  The table name to base the sort by on.  Valid values are:
            Customer, QuoteHed, Task  */  
   cTableName:string,
      /**  The Customer ID if available.  Can be blank.  */  
   iCustNum:number,
      /**  The Quote Number if available.  Can be zero.  */  
   iQuoteNum:number,
      /**  The Vendor ID if available.  Can be blank.  */  
   iVendorNum:number,
}

export interface SortByData_output{
parameters : {
      /**  output parameters  */  
   cSortByList:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCRMCallTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCRMCallTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CRMCallTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CRMCallTableset,
}
}

   /** Required : 
      @param cSalesRepCode
   */  
export interface UserIsAuthorized_input{
      /**  The SalesRep code  */  
   cSalesRepCode:string,
}

export interface UserIsAuthorized_output{
   returnObj:boolean,
}

