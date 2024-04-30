import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.JournalTrackerDetailSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/$metadata", {
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
   Description: Get JournalTrackerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JournalTrackerDetails
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlRow
   */  
export function get_JournalTrackerDetails(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JournalTrackerDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JournalTrackerDetails(requestBody:Erp_Tablesets_GLJrnDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the JournalTrackerDetail item
   Description: Calls GetByID to retrieve the JournalTrackerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JournalTrackerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlRow
   */  
export function get_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JournalTrackerDetail for the service
   Description: Calls UpdateExt to update JournalTrackerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JournalTrackerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, requestBody:Erp_Tablesets_GLJrnDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")", {
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
   Summary: Call UpdateExt to delete JournalTrackerDetail item
   Description: Call UpdateExt to delete JournalTrackerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JournalTrackerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")", {
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
   Description: Get GLJrnDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlAttchRow
   */  
export function get_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_GLJrnDtlAttches(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")/GLJrnDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLJrnDtlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   */  
export function get_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlAttchRow
   */  
export function get_GLJrnDtlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlAttches(requestBody:Erp_Tablesets_GLJrnDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GLJrnDtlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   */  
export function get_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlAttch for the service
   Description: Calls UpdateExt to update GLJrnDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, DrawingSeq:string, requestBody:Erp_Tablesets_GLJrnDtlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlAttch item
   Description: Call UpdateExt to delete GLJrnDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param JournalNum Desc: JournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company:string, BookID:string, FiscalYear:string, FiscalYearSuffix:string, JournalCode:string, JournalNum:string, JournalLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")", {
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
   Description: Get GLJournalTrackers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJournalTrackers
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJournalTrackerRow
   */  
export function get_GLJournalTrackers(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJournalTrackerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJournalTrackerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJournalTrackers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJournalTrackerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJournalTrackerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJournalTrackers(requestBody:Erp_Tablesets_GLJournalTrackerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GLJournalTracker item
   Description: Calls GetByID to retrieve the GLJournalTracker item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJournalTracker
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJournalTrackerRow
   */  
export function get_GLJournalTrackers_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJournalTrackerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_GLJournalTrackerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJournalTracker for the service
   Description: Calls UpdateExt to update GLJournalTracker. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJournalTracker
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJournalTrackerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJournalTrackers_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_GLJournalTrackerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete GLJournalTracker item
   Description: Call UpdateExt to delete GLJournalTracker item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJournalTracker
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJournalTrackers_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers(" + SysRowID + ")", {
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
   Description: Get GLJrnDtlMnlDEASches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlDEASches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlDEASchRow
   */  
export function get_GLJrnDtlMnlDEASches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlDEASches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnDtlMnlDEASches(requestBody:Erp_Tablesets_GLJrnDtlMnlDEASchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlDEASch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   */  
export function get_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, GLBookID:string, JournalCode:string, GLJournalNum:string, JournalLine:string, AmortSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnDtlMnlDEASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLJrnDtlMnlDEASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnDtlMnlDEASch for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlDEASch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlDEASch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, GLBookID:string, JournalCode:string, GLJournalNum:string, JournalLine:string, AmortSeq:string, requestBody:Erp_Tablesets_GLJrnDtlMnlDEASchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
   Summary: Call UpdateExt to delete GLJrnDtlMnlDEASch item
   Description: Call UpdateExt to delete GLJrnDtlMnlDEASch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlDEASch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FiscalCalendarID Desc: FiscalCalendarID   Required: True   Allow empty value : True
      @param FiscalYear Desc: FiscalYear   Required: True
      @param FiscalYearSuffix Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      @param GLBookID Desc: GLBookID   Required: True   Allow empty value : True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param GLJournalNum Desc: GLJournalNum   Required: True
      @param JournalLine Desc: JournalLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company:string, FiscalCalendarID:string, FiscalYear:string, FiscalYearSuffix:string, GLBookID:string, JournalCode:string, GLJournalNum:string, JournalLine:string, AmortSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", {
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
   Description: Get TranGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TranGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranGLCRow
   */  
export function get_TranGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TranGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TranGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TranGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TranGLCs(requestBody:Erp_Tablesets_TranGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TranGLC item
   Description: Calls GetByID to retrieve the TranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TranGLCRow
   */  
export function get_TranGLCs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TranGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_TranGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TranGLC for the service
   Description: Calls UpdateExt to update TranGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TranGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TranGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TranGLCs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_TranGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete TranGLC item
   Description: Call UpdateExt to delete TranGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TranGLC
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TranGLCs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs(" + SysRowID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseGLJrnDtl:string, whereClauseGLJrnDtlAttch:string, whereClauseGLJournalTracker:string, whereClauseGLJrnDtlMnlDEASch:string, whereClauseTranGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLJrnDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtl=" + whereClauseGLJrnDtl
   }
   if(typeof whereClauseGLJrnDtlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlAttch=" + whereClauseGLJrnDtlAttch
   }
   if(typeof whereClauseGLJournalTracker!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJournalTracker=" + whereClauseGLJournalTracker
   }
   if(typeof whereClauseGLJrnDtlMnlDEASch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnDtlMnlDEASch=" + whereClauseGLJrnDtlMnlDEASch
   }
   if(typeof whereClauseTranGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTranGLC=" + whereClauseTranGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(bookID:string, fiscalYear:string, fiscalYearSuffix:string, journalCode:string, journalNum:string, journalLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof bookID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bookID=" + bookID
   }
   if(typeof fiscalYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalYear=" + fiscalYear
   }
   if(typeof fiscalYearSuffix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalYearSuffix=" + fiscalYearSuffix
   }
   if(typeof journalCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "journalCode=" + journalCode
   }
   if(typeof journalNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "journalNum=" + journalNum
   }
   if(typeof journalLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "journalLine=" + journalLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetList" + params, {
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
   Summary: Invoke method LoadGLJournalTracker
   Description: Creates the initial GLTrackerView record
   OperationID: LoadGLJournalTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadGLJournalTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadGLJournalTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadGLJournalTracker(requestBody:LoadGLJournalTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadGLJournalTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/LoadGLJournalTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LoadGLJournalTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJournalDetail
   Description: Filter journals by Journal Code and Journal Number.
   OperationID: GetJournalDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetJournalDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJournalDetail(requestBody:GetJournalDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJournalDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetJournalDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetJournalDetail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJournalDetailByID
   Description: Invokes GetJournalDetail using the values passed in
   OperationID: GetJournalDetailByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetJournalDetailByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalDetailByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJournalDetailByID(requestBody:GetJournalDetailByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJournalDetailByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetJournalDetailByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetJournalDetailByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranGLCHead
   Description: This method replaces the standard GetRows method
   OperationID: GetTranGLCHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTranGLCHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranGLCHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranGLCHead(requestBody:GetTranGLCHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTranGLCHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetTranGLCHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTranGLCHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranGLCHeadSite
   Description: This method replaces the standard GetRows method
   OperationID: GetTranGLCHeadSite
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTranGLCHeadSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranGLCHeadSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranGLCHeadSite(requestBody:GetTranGLCHeadSite_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTranGLCHeadSite_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetTranGLCHeadSite", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTranGLCHeadSite_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtl(requestBody:GetNewGLJrnDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetNewGLJrnDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGLJrnDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlAttch(requestBody:GetNewGLJrnDtlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetNewGLJrnDtlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGLJrnDtlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnDtlMnlDEASch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlDEASch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnDtlMnlDEASch(requestBody:GetNewGLJrnDtlMnlDEASch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnDtlMnlDEASch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetNewGLJrnDtlMnlDEASch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGLJrnDtlMnlDEASch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTranGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTranGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTranGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTranGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTranGLC(requestBody:GetNewTranGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTranGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetNewTranGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTranGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJournalTrackerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJournalTrackerRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlMnlDEASchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TranGLCRow,
}

export interface Erp_Tablesets_GLJournalTrackerRow{
   "Company":string,
   "BookID":string,
   "FiscalYear":number,
   "FiscalYearSuffix":string,
   "JournalCode":string,
   "JournalNum":number,
   "GLBookDesc":string,
   "TotDebit":number,
   "TotCredit":number,
   "JournalCodeDesc":string,
   "CurrencyCode":string,
   "CurrencyCodeDesc":string,
   "Balance":number,
   "FiscalPeriod":number,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  MXRFC  */  
   "MXRFC":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnDtlAttchRow{
   "Company":string,
   "BookID":string,
   "FiscalYear":number,
   "FiscalYearSuffix":string,
   "JournalCode":string,
   "JournalNum":number,
   "JournalLine":number,
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

export interface Erp_Tablesets_GLJrnDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   "Description":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
   "TotCredit":number,
   "TotDebit":number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   "Reverse":boolean,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Legal Number of source document  */  
   "LegalNumber":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  this field equas ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   "BookDebitAmount":number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   "BookCreditAmount":number,
      /**  if has reverse line  */  
   "HasReverseLine":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Journal Sequence Number  */  
   "Sequence":number,
   "BookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnDtlMnlDEASchRow{
      /**  Company  */  
   "Company":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  BookID  */  
   "BookID":string,
      /**  JournalCode  */  
   "JournalCode":string,
      /**  JournalNum  */  
   "JournalNum":number,
      /**  JournalLine  */  
   "JournalLine":number,
      /**  AmortSeq  */  
   "AmortSeq":number,
      /**  SchFiscalCalendarID  */  
   "SchFiscalCalendarID":string,
      /**  SchFiscalYear  */  
   "SchFiscalYear":number,
      /**  SchFiscalYearSuffix  */  
   "SchFiscalYearSuffix":string,
      /**  SchFiscalPeriod  */  
   "SchFiscalPeriod":number,
      /**  AmortDate  */  
   "AmortDate":string,
      /**  AmortPercent  */  
   "AmortPercent":number,
      /**  AmortAmt  */  
   "AmortAmt":number,
      /**  DocAmortAmt  */  
   "DocAmortAmt":number,
      /**  Posted  */  
   "Posted":boolean,
      /**  PostedDate  */  
   "PostedDate":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Rpt1AmortAmt  */  
   "Rpt1AmortAmt":number,
   "GroupID":string,
      /**  Document currency  */  
   "CurrencyCode":string,
      /**  Rpt2AmortAmt  */  
   "Rpt2AmortAmt":number,
      /**  Rpt3AmortAmt  */  
   "Rpt3AmortAmt":number,
      /**  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  */  
   "GLBookID":string,
      /**  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  */  
   "GLJournalNum":number,
      /**  DispAmortAmt  */  
   "DispAmortAmt":number,
      /**  DispDocAmortAmt  */  
   "DispDocAmortAmt":number,
      /**  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  */  
   "HasReverseLines":boolean,
      /**  Account Currency  */  
   "CurrencyCodeAcct":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   "Description":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  User ID that posted this translation.  */  
   "PostedBy":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   "Posted":boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   "SourceModule":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "ARInvoiceNum":number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   "BankAcctID":string,
      /**  Check number.  */  
   "CheckNum":number,
      /**  Cash Receipts reference field.  */  
   "CRHeadNum":number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   "Reverse":boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   "BankTranNum":number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   "BankSlip":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefType":string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefCode":string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalNum":number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalLine":number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   "GlbJournalCode":string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   "GlbVendorNum":number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   "GlbAPInvoiceNum":string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   "MultiCompany":boolean,
      /**  Linked to a Multi-Company Journal.  */  
   "Linked":boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   "CommentText":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "GlbCompanyID":string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   "GlbFiscalYear":number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   "GlbFiscalPeriod":number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   "GlbGroupID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAccount":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "ExtGLAccount":string,
      /**  External Segment Value 1  */  
   "ExtSegValue1":string,
      /**  External Segment Value 2  */  
   "ExtSegValue2":string,
      /**  External Segment Value 3  */  
   "ExtSegValue3":string,
      /**  External Segment Value 4  */  
   "ExtSegValue4":string,
      /**  External Segment Value 5  */  
   "ExtSegValue5":string,
      /**  External Segment Value 6  */  
   "ExtSegValue6":string,
      /**  External Segment Value 7  */  
   "ExtSegValue7":string,
      /**  External Segment Value 8  */  
   "ExtSegValue8":string,
      /**  External Segment Value 9  */  
   "ExtSegValue9":string,
      /**  External Segment Value 10  */  
   "ExtSegValue10":string,
      /**  External Segment Value 11  */  
   "ExtSegValue11":string,
      /**  External Segment Value 12  */  
   "ExtSegValue12":string,
      /**  External Segment Value 13  */  
   "ExtSegValue13":string,
      /**  External Segment Value 14  */  
   "ExtSegValue14":string,
      /**  External Segment Value 15  */  
   "ExtSegValue15":string,
      /**  External Segment Value 16  */  
   "ExtSegValue16":string,
      /**  External Segment Value 17  */  
   "ExtSegValue17":string,
      /**  External Segment Value 18  */  
   "ExtSegValue18":string,
      /**  External Segment Value 19  */  
   "ExtSegValue19":string,
      /**  External Segment Value 20  */  
   "ExtSegValue20":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**  Legal Number of source document  */  
   "LegalNumber":string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "PerBalFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "TBFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "DailyBalFlag":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year suffix.  */  
   "GlbFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "GlbFiscalCalendarID":string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   "IntermediateProc":boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   "SrcCompany":string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SrcBook":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "SrcGLAccount":string,
      /**  Source Journal Code  */  
   "SrcJrnlCode":string,
      /**  Source Journal Number  */  
   "SrcJournalNum":number,
      /**  Source Journal Line  */  
   "SrcJournalLine":number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   "SrcType":string,
      /**  this field equas ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  This field shows Debit value of transaction  */  
   "DebitAmount":number,
      /**  This field shows Credit value of transaction  */  
   "CreditAmount":number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   "BookDebitAmount":number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   "BookCreditAmount":number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   "ParentRUID":string,
      /**  if has reverse line  */  
   "HasReverseLine":boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   "BalanceAcct":string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   "TrialAcct":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   "AllocationStamp":string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   "BatchID":string,
      /**  This is the allocation id that processed this journal entry.  */  
   "AllocID":string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   "RunNbr":number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   "AllocRunNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtSeq":number,
      /**  External COA Code  */  
   "ExtCOACode":string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   "MatchCode":string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   "MatchDate":string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   "Reconciled":boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Journal Sequence Number  */  
   "Sequence":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   "CustNum":number,
      /**  CloseFiscalPeriod  */  
   "CloseFiscalPeriod":number,
      /**  SourcePlant  */  
   "SourcePlant":string,
      /**  Plant  */  
   "Plant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
      /**   Colombia Loc field            
This field is used as external calculated only.  */  
   "COOneTimeDesc":string,
      /**   Colombia Loc field.           
This field is used as external calculated only.  */  
   "COOneTimeID":string,
      /**  DEA Code  */  
   "DEACodeDesc":string,
      /**  DEA End Date  */  
   "DEAEndDate":string,
      /**  DEA Start Date  */  
   "DEAStartDate":string,
      /**  Deferred Expense  */  
   "DeferredExp":boolean,
      /**  DEA Distributed Amount  */  
   "Distributed":number,
      /**  DEA Distributed Amount in Doc Currency  */  
   "DocDistributed":number,
      /**  DEA Expense Amount in Doc Currency  */  
   "DocExpense":number,
      /**  DEA Recognized Amount in Doc Currency  */  
   "DocRecognized":number,
      /**  DEA Remaining Amount in Doc Currency  */  
   "DocRemaining":number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   "DocUnrecognized":number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   "EnableMultiCompany":boolean,
      /**  DEA Expense Amount  */  
   "Expense":number,
   "ExtRefAcctChart":string,
   "ExtRefAcctDept":string,
   "ExtRefAcctDiv":string,
   "ExtRefCodeStatus":string,
   "GLAcctDisp":string,
      /**  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  */  
   "HeaderCommentText":string,
      /**  Manual GL Journal Line Reference.  */  
   "LineReference":string,
      /**  Manual GL Journal Line Reference Holder.  */  
   "LineReferenceHolder":string,
      /**  Manual GL Journal Line Reference Holder Name.  */  
   "LineReferenceHolderName":string,
      /**  Manual GL Journal Line Reference Type.  */  
   "LineReferenceType":string,
   "MovementNum":number,
      /**  Apply Date of the Original Transaction  */  
   "OrigApplyDate":string,
      /**  Journal line of the original transaction that was reversed.  */  
   "OrigJrnlLine":number,
      /**  Journal number of the original transaction that was reversed.  */  
   "OrigJrnlNbr":number,
      /**  Fiscal year of the original transaction that was reversed.  */  
   "OrigJrnlYear":number,
      /**  Fiscal year suffix of the original transaction that was reversed.  */  
   "OrigJrnlYearSuffix":string,
      /**  DEA Recognized Amount  */  
   "Recognized":number,
   "RefAcctChart":string,
   "RefAcctDept":string,
   "RefAcctDiv":string,
   "RefCodeStatus":string,
      /**  DEA Remaining Amount  */  
   "Remaining":number,
      /**  Apply date of the reversing transaction  */  
   "RevApplyDate":string,
      /**  Journal line of the latest journal entry made to reverse a transaction.  */  
   "RevJrnlLine":number,
      /**  Journal number of the latest journal entry made to reverse a transaction.  */  
   "RevJrnlNbr":number,
      /**  Fiscal year of the latest journal entry made to reverse a transaction.  */  
   "RevJrnlYear":number,
      /**  Fiscal year suffix of the latest journal entry made to reverse a transaction.  */  
   "RevJrnlYearSuffix":string,
   "StatAmount":number,
   "TotCredit":number,
   "TotDebit":number,
      /**  DEA Unrecognized Amount  */  
   "Unrecognized":number,
   "BookCurrencyCode":string,
   "BookCurrencySymbol":string,
      /**  Description of the entity the journal detail is for  */  
   "EntityDescription":string,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrName":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrDesc":string,
   "FiscalCalDescription":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAccount":string,
   "JournalCodeJrnlDescription":string,
   "SrcGLAccountGLShortAcct":string,
   "SrcGLAccountAccountDesc":string,
   "SrcGLAccountGLAcctDisp":string,
   "StatUOMStatUOMDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TranGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  AP Tran Number  */  
   "APTranNo":number,
      /**  Indicates if the AP Transaction is voided  */  
   "APTranVoided":boolean,
      /**  Bank Account ID  */  
   "BankAcctID":string,
      /**  Bank Group ID  */  
   "BankGroupID":string,
      /**  Bank Tran Number  */  
   "BankTranNum":number,
      /**  Indicates if the Bank Transaction has been voided  */  
   "BankTranVoided":boolean,
   "BookCurrencyCode":string,
      /**  Cash Head Number  */  
   "CashHeadNum":number,
      /**  Cash Head Group ID  */  
   "CashHedGroup":string,
      /**  Cash Detail Invoice Reference  */  
   "CashInvRef":number,
      /**  Chead Head Number  */  
   "CheckHeadNum":number,
      /**  Indicates if the Check Header has been voided.  */  
   "CheckHedVoided":boolean,
      /**  Container ID  */  
   "ContainerID":number,
   "DocumentText":string,
   "DocumentType":string,
      /**  Used to display a context sensitive label for Key1.  This data is set on the server side and is translateable.  */  
   "Key1Label":string,
      /**  Used to display a context sensitive label for Key2.  This data is set on the server side and is translateable.  */  
   "Key2Label":string,
      /**  Used to display a context sensitive label for Key3.  This data is set on the server side and is translateable.  */  
   "Key3Label":string,
      /**  Used to display a context sensitive label for Key4.  This data is set on the server side and is translateable.  */  
   "Key4Label":string,
      /**  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  */  
   "Key5Label":string,
      /**  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  */  
   "Key6Label":string,
      /**  Purchase order receipt pack slip number  */  
   "Packslip":string,
      /**  Purchase Order Line Number  */  
   "POLine":number,
      /**  Purchase Order Number  */  
   "PONum":number,
      /**  Purchase Order Release Number  */  
   "PORelNum":number,
      /**  Purchase Point  */  
   "PurPoint":string,
   "RateCodeDesc":string,
   "StatAmount":number,
   "SupplierName":string,
      /**  The Taxable Amount if the current TranGLc record is related to the InvcTax or APInvTax tables.  */  
   "TaxableAmt":number,
   "TaxAmt":number,
   "TaxCode":string,
   "TaxCodeDesc":string,
      /**  The percent of the rate if current TranGLC record is related to the InvcTax or APInvTax tables  */  
   "TaxRatePercent":number,
      /**  AP Tran head Number  */  
   "APHeadNum":number,
   "HideKey2":boolean,
   "HideKey3":boolean,
   "HideKey4":boolean,
   "HideKey5":boolean,
   "HideKey6":boolean,
   "BitFlag":number,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrencyID":string,
   "FiscalCalendarDescription":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountGLShortAcct":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
   "InvoiceLineLineDesc":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "JournalCodeJrnlDescription":string,
   "StatUOMStatUOMDesc":string,
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
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param journalLine
   */  
export interface DeleteByID_input{
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLJournalTrackerRow{
   Company:string,
   BookID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   JournalCode:string,
   JournalNum:number,
   GLBookDesc:string,
   TotDebit:number,
   TotCredit:number,
   JournalCodeDesc:string,
   CurrencyCode:string,
   CurrencyCodeDesc:string,
   Balance:number,
   FiscalPeriod:number,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXRFC  */  
   MXRFC:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlAttchRow{
   Company:string,
   BookID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   JournalCode:string,
   JournalNum:number,
   JournalLine:number,
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

export interface Erp_Tablesets_GLJrnDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
   TotCredit:number,
   TotDebit:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
   BookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlListTableset{
   GLJrnDtlList:Erp_Tablesets_GLJrnDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnDtlMnlDEASchRow{
      /**  Company  */  
   Company:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  BookID  */  
   BookID:string,
      /**  JournalCode  */  
   JournalCode:string,
      /**  JournalNum  */  
   JournalNum:number,
      /**  JournalLine  */  
   JournalLine:number,
      /**  AmortSeq  */  
   AmortSeq:number,
      /**  SchFiscalCalendarID  */  
   SchFiscalCalendarID:string,
      /**  SchFiscalYear  */  
   SchFiscalYear:number,
      /**  SchFiscalYearSuffix  */  
   SchFiscalYearSuffix:string,
      /**  SchFiscalPeriod  */  
   SchFiscalPeriod:number,
      /**  AmortDate  */  
   AmortDate:string,
      /**  AmortPercent  */  
   AmortPercent:number,
      /**  AmortAmt  */  
   AmortAmt:number,
      /**  DocAmortAmt  */  
   DocAmortAmt:number,
      /**  Posted  */  
   Posted:boolean,
      /**  PostedDate  */  
   PostedDate:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Rpt1AmortAmt  */  
   Rpt1AmortAmt:number,
   GroupID:string,
      /**  Document currency  */  
   CurrencyCode:string,
      /**  Rpt2AmortAmt  */  
   Rpt2AmortAmt:number,
      /**  Rpt3AmortAmt  */  
   Rpt3AmortAmt:number,
      /**  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  */  
   GLBookID:string,
      /**  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  */  
   GLJournalNum:number,
      /**  DispAmortAmt  */  
   DispAmortAmt:number,
      /**  DispDocAmortAmt  */  
   DispDocAmortAmt:number,
      /**  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  */  
   HasReverseLines:boolean,
      /**  Account Currency  */  
   CurrencyCodeAcct:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   PerBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   TBFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   SrcType:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   BalanceAcct:string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   TrialAcct:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   AllocationStamp:string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   BatchID:string,
      /**  This is the allocation id that processed this journal entry.  */  
   AllocID:string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   RunNbr:number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   AllocRunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  External COA Code  */  
   ExtCOACode:string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   MatchCode:string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   MatchDate:string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   Reconciled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  CloseFiscalPeriod  */  
   CloseFiscalPeriod:number,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Plant  */  
   Plant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**   Colombia Loc field            
This field is used as external calculated only.  */  
   COOneTimeDesc:string,
      /**   Colombia Loc field.           
This field is used as external calculated only.  */  
   COOneTimeID:string,
      /**  DEA Code  */  
   DEACodeDesc:string,
      /**  DEA End Date  */  
   DEAEndDate:string,
      /**  DEA Start Date  */  
   DEAStartDate:string,
      /**  Deferred Expense  */  
   DeferredExp:boolean,
      /**  DEA Distributed Amount  */  
   Distributed:number,
      /**  DEA Distributed Amount in Doc Currency  */  
   DocDistributed:number,
      /**  DEA Expense Amount in Doc Currency  */  
   DocExpense:number,
      /**  DEA Recognized Amount in Doc Currency  */  
   DocRecognized:number,
      /**  DEA Remaining Amount in Doc Currency  */  
   DocRemaining:number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   DocUnrecognized:number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
      /**  DEA Expense Amount  */  
   Expense:number,
   ExtRefAcctChart:string,
   ExtRefAcctDept:string,
   ExtRefAcctDiv:string,
   ExtRefCodeStatus:string,
   GLAcctDisp:string,
      /**  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  */  
   HeaderCommentText:string,
      /**  Manual GL Journal Line Reference.  */  
   LineReference:string,
      /**  Manual GL Journal Line Reference Holder.  */  
   LineReferenceHolder:string,
      /**  Manual GL Journal Line Reference Holder Name.  */  
   LineReferenceHolderName:string,
      /**  Manual GL Journal Line Reference Type.  */  
   LineReferenceType:string,
   MovementNum:number,
      /**  Apply Date of the Original Transaction  */  
   OrigApplyDate:string,
      /**  Journal line of the original transaction that was reversed.  */  
   OrigJrnlLine:number,
      /**  Journal number of the original transaction that was reversed.  */  
   OrigJrnlNbr:number,
      /**  Fiscal year of the original transaction that was reversed.  */  
   OrigJrnlYear:number,
      /**  Fiscal year suffix of the original transaction that was reversed.  */  
   OrigJrnlYearSuffix:string,
      /**  DEA Recognized Amount  */  
   Recognized:number,
   RefAcctChart:string,
   RefAcctDept:string,
   RefAcctDiv:string,
   RefCodeStatus:string,
      /**  DEA Remaining Amount  */  
   Remaining:number,
      /**  Apply date of the reversing transaction  */  
   RevApplyDate:string,
      /**  Journal line of the latest journal entry made to reverse a transaction.  */  
   RevJrnlLine:number,
      /**  Journal number of the latest journal entry made to reverse a transaction.  */  
   RevJrnlNbr:number,
      /**  Fiscal year of the latest journal entry made to reverse a transaction.  */  
   RevJrnlYear:number,
      /**  Fiscal year suffix of the latest journal entry made to reverse a transaction.  */  
   RevJrnlYearSuffix:string,
   StatAmount:number,
   TotCredit:number,
   TotDebit:number,
      /**  DEA Unrecognized Amount  */  
   Unrecognized:number,
   BookCurrencyCode:string,
   BookCurrencySymbol:string,
      /**  Description of the entity the journal detail is for  */  
   EntityDescription:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrName:string,
   CurrencyCurrencyID:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrDesc:string,
   FiscalCalDescription:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLAccountGLAccount:string,
   JournalCodeJrnlDescription:string,
   SrcGLAccountGLShortAcct:string,
   SrcGLAccountAccountDesc:string,
   SrcGLAccountGLAcctDisp:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JournalTrackerDetailTableset{
   GLJrnDtl:Erp_Tablesets_GLJrnDtlRow[],
   GLJrnDtlAttch:Erp_Tablesets_GLJrnDtlAttchRow[],
   GLJournalTracker:Erp_Tablesets_GLJournalTrackerRow[],
   GLJrnDtlMnlDEASch:Erp_Tablesets_GLJrnDtlMnlDEASchRow[],
   TranGLC:Erp_Tablesets_TranGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TranGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  AP Tran Number  */  
   APTranNo:number,
      /**  Indicates if the AP Transaction is voided  */  
   APTranVoided:boolean,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Group ID  */  
   BankGroupID:string,
      /**  Bank Tran Number  */  
   BankTranNum:number,
      /**  Indicates if the Bank Transaction has been voided  */  
   BankTranVoided:boolean,
   BookCurrencyCode:string,
      /**  Cash Head Number  */  
   CashHeadNum:number,
      /**  Cash Head Group ID  */  
   CashHedGroup:string,
      /**  Cash Detail Invoice Reference  */  
   CashInvRef:number,
      /**  Chead Head Number  */  
   CheckHeadNum:number,
      /**  Indicates if the Check Header has been voided.  */  
   CheckHedVoided:boolean,
      /**  Container ID  */  
   ContainerID:number,
   DocumentText:string,
   DocumentType:string,
      /**  Used to display a context sensitive label for Key1.  This data is set on the server side and is translateable.  */  
   Key1Label:string,
      /**  Used to display a context sensitive label for Key2.  This data is set on the server side and is translateable.  */  
   Key2Label:string,
      /**  Used to display a context sensitive label for Key3.  This data is set on the server side and is translateable.  */  
   Key3Label:string,
      /**  Used to display a context sensitive label for Key4.  This data is set on the server side and is translateable.  */  
   Key4Label:string,
      /**  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  */  
   Key5Label:string,
      /**  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  */  
   Key6Label:string,
      /**  Purchase order receipt pack slip number  */  
   Packslip:string,
      /**  Purchase Order Line Number  */  
   POLine:number,
      /**  Purchase Order Number  */  
   PONum:number,
      /**  Purchase Order Release Number  */  
   PORelNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
   RateCodeDesc:string,
   StatAmount:number,
   SupplierName:string,
      /**  The Taxable Amount if the current TranGLc record is related to the InvcTax or APInvTax tables.  */  
   TaxableAmt:number,
   TaxAmt:number,
   TaxCode:string,
   TaxCodeDesc:string,
      /**  The percent of the rate if current TranGLC record is related to the InvcTax or APInvTax tables  */  
   TaxRatePercent:number,
      /**  AP Tran head Number  */  
   APHeadNum:number,
   HideKey2:boolean,
   HideKey3:boolean,
   HideKey4:boolean,
   HideKey5:boolean,
   HideKey6:boolean,
   BitFlag:number,
   CurrencyCurrSymbol:string,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   FiscalCalendarDescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
   InvoiceLineLineDesc:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   JournalCodeJrnlDescription:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtJournalTrackerDetailTableset{
   GLJrnDtl:Erp_Tablesets_GLJrnDtlRow[],
   GLJrnDtlAttch:Erp_Tablesets_GLJrnDtlAttchRow[],
   GLJournalTracker:Erp_Tablesets_GLJournalTrackerRow[],
   GLJrnDtlMnlDEASch:Erp_Tablesets_GLJrnDtlMnlDEASchRow[],
   TranGLC:Erp_Tablesets_TranGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param journalLine
   */  
export interface GetByID_input{
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
}

   /** Required : 
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
   */  
export interface GetJournalDetailByID_input{
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
}

export interface GetJournalDetailByID_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetJournalDetail_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
}

export interface GetJournalDetail_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
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
   returnObj:Erp_Tablesets_GLJrnDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
      @param journalLine
   */  
export interface GetNewGLJrnDtlAttch_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
   journalLine:number,
}

export interface GetNewGLJrnDtlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
}
}

   /** Required : 
      @param ds
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param glBookID
      @param journalCode
      @param glJournalNum
      @param journalLine
   */  
export interface GetNewGLJrnDtlMnlDEASch_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
   fiscalCalendarID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   glBookID:string,
   journalCode:string,
   glJournalNum:number,
   journalLine:number,
}

export interface GetNewGLJrnDtlMnlDEASch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
}
}

   /** Required : 
      @param ds
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param journalCode
      @param journalNum
   */  
export interface GetNewGLJrnDtl_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   journalCode:string,
   journalNum:number,
}

export interface GetNewGLJrnDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTranGLC_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
}

export interface GetNewTranGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
}
}

   /** Required : 
      @param whereClauseGLJrnDtl
      @param whereClauseGLJrnDtlAttch
      @param whereClauseGLJournalTracker
      @param whereClauseGLJrnDtlMnlDEASch
      @param whereClauseTranGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLJrnDtl:string,
   whereClauseGLJrnDtlAttch:string,
   whereClauseGLJournalTracker:string,
   whereClauseGLJrnDtlMnlDEASch:string,
   whereClauseTranGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param vJournalCode
      @param vBookID
      @param vTaxCode
      @param vSiteList
   */  
export interface GetTranGLCHeadSite_input{
      /**  Journal Code  */  
   vJournalCode:string,
      /**  Book ID  */  
   vBookID:string,
      /**  Tax Code  */  
   vTaxCode:string,
      /**  Selected Sites  */  
   vSiteList:string,
}

export interface GetTranGLCHeadSite_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
}

   /** Required : 
      @param vJournalCode
      @param vBookID
      @param vTaxCode
   */  
export interface GetTranGLCHead_input{
      /**  Journal Code  */  
   vJournalCode:string,
      /**  Book ID  */  
   vBookID:string,
      /**  Tax Code  */  
   vTaxCode:string,
}

export interface GetTranGLCHead_output{
   returnObj:Erp_Tablesets_JournalTrackerDetailTableset[],
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
export interface LoadGLJournalTracker_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
}

export interface LoadGLJournalTracker_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtJournalTrackerDetailTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJournalTrackerDetailTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JournalTrackerDetailTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JournalTrackerDetailTableset,
}
}

