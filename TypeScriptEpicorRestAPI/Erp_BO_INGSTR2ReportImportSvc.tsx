import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.INGSTR2ReportImportSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/$metadata", {
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
   Description: Get INGSTR2ReportImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2ReportImports
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportRow
   */  
export function get_INGSTR2ReportImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2ReportImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.INGSTR2ReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_INGSTR2ReportImports(requestBody:Erp_Tablesets_INGSTR2ReportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the INGSTR2ReportImport item
   Description: Calls GetByID to retrieve the INGSTR2ReportImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR2ReportRow
   */  
export function get_INGSTR2ReportImports_Company_ReportID(Company:string, ReportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR2ReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR2ReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update INGSTR2ReportImport for the service
   Description: Calls UpdateExt to update INGSTR2ReportImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2ReportImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_INGSTR2ReportImports_Company_ReportID(Company:string, ReportID:string, requestBody:Erp_Tablesets_INGSTR2ReportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")", {
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
   Summary: Call UpdateExt to delete INGSTR2ReportImport item
   Description: Call UpdateExt to delete INGSTR2ReportImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2ReportImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_INGSTR2ReportImports_Company_ReportID(Company:string, ReportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")", {
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
   Description: Get INGSTR2MatchedLines items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_INGSTR2MatchedLines1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2MatchedLineRow
   */  
export function get_INGSTR2ReportImports_Company_ReportID_INGSTR2MatchedLines(Company:string, ReportID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2MatchedLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2MatchedLines", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2MatchedLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the INGSTR2MatchedLine item
   Description: Calls GetByID to retrieve the INGSTR2MatchedLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2MatchedLine1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param Section Desc: Section   Required: True   Allow empty value : True
      @param TransactionType Desc: TransactionType   Required: True
      @param ExternalSysRowID Desc: ExternalSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   */  
export function get_INGSTR2ReportImports_Company_ReportID_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company:string, ReportID:string, Section:string, TransactionType:string, ExternalSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR2MatchedLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR2MatchedLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get INGSTR2ReportAttchs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_INGSTR2ReportAttchs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportAttchRow
   */  
export function get_INGSTR2ReportImports_Company_ReportID_INGSTR2ReportAttchs(Company:string, ReportID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2ReportAttchs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the INGSTR2ReportAttch item
   Description: Calls GetByID to retrieve the INGSTR2ReportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   */  
export function get_INGSTR2ReportImports_Company_ReportID_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company:string, ReportID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR2ReportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportImports(" + Company + "," + ReportID + ")/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR2ReportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2MatchedLines items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2MatchedLines
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2MatchedLineRow
   */  
export function get_INGSTR2MatchedLines(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2MatchedLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2MatchedLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2MatchedLines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_INGSTR2MatchedLines(requestBody:Erp_Tablesets_INGSTR2MatchedLineRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the INGSTR2MatchedLine item
   Description: Calls GetByID to retrieve the INGSTR2MatchedLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2MatchedLine
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param Section Desc: Section   Required: True   Allow empty value : True
      @param TransactionType Desc: TransactionType   Required: True
      @param ExternalSysRowID Desc: ExternalSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   */  
export function get_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company:string, ReportID:string, Section:string, TransactionType:string, ExternalSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR2MatchedLineRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR2MatchedLineRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update INGSTR2MatchedLine for the service
   Description: Calls UpdateExt to update INGSTR2MatchedLine. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2MatchedLine
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param Section Desc: Section   Required: True   Allow empty value : True
      @param TransactionType Desc: TransactionType   Required: True
      @param ExternalSysRowID Desc: ExternalSysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2MatchedLineRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company:string, ReportID:string, Section:string, TransactionType:string, ExternalSysRowID:string, requestBody:Erp_Tablesets_INGSTR2MatchedLineRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")", {
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
   Summary: Call UpdateExt to delete INGSTR2MatchedLine item
   Description: Call UpdateExt to delete INGSTR2MatchedLine item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2MatchedLine
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param Section Desc: Section   Required: True   Allow empty value : True
      @param TransactionType Desc: TransactionType   Required: True
      @param ExternalSysRowID Desc: ExternalSysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_INGSTR2MatchedLines_Company_ReportID_Section_TransactionType_ExternalSysRowID(Company:string, ReportID:string, Section:string, TransactionType:string, ExternalSysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2MatchedLines(" + Company + "," + ReportID + "," + Section + "," + TransactionType + "," + ExternalSysRowID + ")", {
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
   Description: Get INGSTR2ReportAttchs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2ReportAttchs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportAttchRow
   */  
export function get_INGSTR2ReportAttchs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2ReportAttchs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_INGSTR2ReportAttchs(requestBody:Erp_Tablesets_INGSTR2ReportAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the INGSTR2ReportAttch item
   Description: Calls GetByID to retrieve the INGSTR2ReportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   */  
export function get_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company:string, ReportID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR2ReportAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR2ReportAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update INGSTR2ReportAttch for the service
   Description: Calls UpdateExt to update INGSTR2ReportAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2ReportAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company:string, ReportID:string, DrawingSeq:string, requestBody:Erp_Tablesets_INGSTR2ReportAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete INGSTR2ReportAttch item
   Description: Call UpdateExt to delete INGSTR2ReportAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2ReportAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_INGSTR2ReportAttchs_Company_ReportID_DrawingSeq(Company:string, ReportID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2ReportAttchs(" + Company + "," + ReportID + "," + DrawingSeq + ")", {
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
   Description: Get INGSTR23s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR23s
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR23Row
   */  
export function get_INGSTR23s(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR23Row>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR23Row)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR23s
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR23Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.INGSTR23Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_INGSTR23s(requestBody:Erp_Tablesets_INGSTR23Row, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the INGSTR23 item
   Description: Calls GetByID to retrieve the INGSTR23 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR23
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR23Row
   */  
export function get_INGSTR23s_Company_LocalName_Key1_Key2_Key3_Key4(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR23Row>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR23Row)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update INGSTR23 for the service
   Description: Calls UpdateExt to update INGSTR23. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR23
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR23Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_INGSTR23s_Company_LocalName_Key1_Key2_Key3_Key4(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, requestBody:Erp_Tablesets_INGSTR23Row, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete INGSTR23 item
   Description: Call UpdateExt to delete INGSTR23 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR23
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_INGSTR23s_Company_LocalName_Key1_Key2_Key3_Key4(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR23s(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Description: Get INGSTR26Cs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR26Cs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR26CRow
   */  
export function get_INGSTR26Cs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR26CRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR26CRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR26Cs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR26CRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.INGSTR26CRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_INGSTR26Cs(requestBody:Erp_Tablesets_INGSTR26CRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the INGSTR26C item
   Description: Calls GetByID to retrieve the INGSTR26C item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR26C
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR26CRow
   */  
export function get_INGSTR26Cs_Company_LocalName_Key1_Key2_Key3_Key4(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR26CRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR26CRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update INGSTR26C for the service
   Description: Calls UpdateExt to update INGSTR26C. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR26C
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR26CRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_INGSTR26Cs_Company_LocalName_Key1_Key2_Key3_Key4(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, requestBody:Erp_Tablesets_INGSTR26CRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Summary: Call UpdateExt to delete INGSTR26C item
   Description: Call UpdateExt to delete INGSTR26C item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR26C
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_INGSTR26Cs_Company_LocalName_Key1_Key2_Key3_Key4(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR26Cs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + ")", {
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
   Description: Get INGSTR2Transactions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2Transactions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2TransactionRow
   */  
export function get_INGSTR2Transactions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2TransactionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2TransactionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2Transactions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_INGSTR2Transactions(requestBody:Erp_Tablesets_INGSTR2TransactionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the INGSTR2Transaction item
   Description: Calls GetByID to retrieve the INGSTR2Transaction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2Transaction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param IntKey1 Desc: IntKey1   Required: True
      @param IntKey2 Desc: IntKey2   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param IntKey3 Desc: IntKey3   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
   */  
export function get_INGSTR2Transactions_Company_LocalName_Key1_IntKey1_IntKey2_Key2_IntKey3(Company:string, LocalName:string, Key1:string, IntKey1:string, IntKey2:string, Key2:string, IntKey3:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_INGSTR2TransactionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions(" + Company + "," + LocalName + "," + Key1 + "," + IntKey1 + "," + IntKey2 + "," + Key2 + "," + IntKey3 + ")", {
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
         resolve(data as Erp_Tablesets_INGSTR2TransactionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update INGSTR2Transaction for the service
   Description: Calls UpdateExt to update INGSTR2Transaction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2Transaction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param IntKey1 Desc: IntKey1   Required: True
      @param IntKey2 Desc: IntKey2   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param IntKey3 Desc: IntKey3   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2TransactionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_INGSTR2Transactions_Company_LocalName_Key1_IntKey1_IntKey2_Key2_IntKey3(Company:string, LocalName:string, Key1:string, IntKey1:string, IntKey2:string, Key2:string, IntKey3:string, requestBody:Erp_Tablesets_INGSTR2TransactionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions(" + Company + "," + LocalName + "," + Key1 + "," + IntKey1 + "," + IntKey2 + "," + Key2 + "," + IntKey3 + ")", {
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
   Summary: Call UpdateExt to delete INGSTR2Transaction item
   Description: Call UpdateExt to delete INGSTR2Transaction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2Transaction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param IntKey1 Desc: IntKey1   Required: True
      @param IntKey2 Desc: IntKey2   Required: True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param IntKey3 Desc: IntKey3   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_INGSTR2Transactions_Company_LocalName_Key1_IntKey1_IntKey2_Key2_IntKey3(Company:string, LocalName:string, Key1:string, IntKey1:string, IntKey2:string, Key2:string, IntKey3:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/INGSTR2Transactions(" + Company + "," + LocalName + "," + Key1 + "," + IntKey1 + "," + IntKey2 + "," + Key2 + "," + IntKey3 + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportListRow)
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
export function get_GetRows(whereClauseINGSTR2Report:string, whereClauseINGSTR2ReportAttch:string, whereClauseINGSTR23:string, whereClauseINGSTR26C:string, whereClauseINGSTR2MatchedLine:string, whereClauseINGSTR2Transaction:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseINGSTR2Report!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseINGSTR2Report=" + whereClauseINGSTR2Report
   }
   if(typeof whereClauseINGSTR2ReportAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseINGSTR2ReportAttch=" + whereClauseINGSTR2ReportAttch
   }
   if(typeof whereClauseINGSTR23!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseINGSTR23=" + whereClauseINGSTR23
   }
   if(typeof whereClauseINGSTR26C!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseINGSTR26C=" + whereClauseINGSTR26C
   }
   if(typeof whereClauseINGSTR2MatchedLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseINGSTR2MatchedLine=" + whereClauseINGSTR2MatchedLine
   }
   if(typeof whereClauseINGSTR2Transaction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseINGSTR2Transaction=" + whereClauseINGSTR2Transaction
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetRows" + params, {
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
export function get_GetByID(reportID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reportID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reportID=" + reportID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetList" + params, {
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
   Summary: Invoke method ImportStatement
   Description: Import Statement file
   OperationID: ImportStatement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportStatement(requestBody:ImportStatement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportStatement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/ImportStatement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportStatement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteImportData
   Description: Deletes lines imported for the current section of the current report and removes links from the previous reports
   OperationID: DeleteImportData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteImportData(requestBody:DeleteImportData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteImportData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/DeleteImportData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteImportData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsImportData
   Description: Checks existence of imported data
   OperationID: ExistsImportData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsImportData(requestBody:ExistsImportData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsImportData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/ExistsImportData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExistsImportData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsImportDataSection
   Description: Checks for existence of imported data in specific section of the report.
   OperationID: ExistsImportDataSection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsImportDataSection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsImportDataSection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsImportDataSection(requestBody:ExistsImportDataSection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsImportDataSection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/ExistsImportDataSection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExistsImportDataSection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsApproveAllowed
   Description: Check if report can be approved
   OperationID: IsApproveAllowed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsApproveAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsApproveAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsApproveAllowed(requestBody:IsApproveAllowed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsApproveAllowed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/IsApproveAllowed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsApproveAllowed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrieveTransactions
   Description: Retrieve Transactions
   OperationID: RetrieveTransactions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RetrieveTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveTransactions(requestBody:RetrieveTransactions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveTransactions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/RetrieveTransactions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RetrieveTransactions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchTransaction2Line
   OperationID: MatchTransaction2Line
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchTransaction2Line_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchTransaction2Line_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchTransaction2Line(requestBody:MatchTransaction2Line_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchTransaction2Line_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/MatchTransaction2Line", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MatchTransaction2Line_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnmatchFromLine
   OperationID: UnmatchFromLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnmatchFromLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchFromLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnmatchFromLine(requestBody:UnmatchFromLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnmatchFromLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/UnmatchFromLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnmatchFromLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchSection
   OperationID: MatchSection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchSection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchSection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchSection(requestBody:MatchSection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchSection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/MatchSection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as MatchSection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewINGSTR2Report
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2Report
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2Report_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2Report_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewINGSTR2Report(requestBody:GetNewINGSTR2Report_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewINGSTR2Report_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetNewINGSTR2Report", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewINGSTR2Report_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewINGSTR2ReportAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2ReportAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2ReportAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2ReportAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewINGSTR2ReportAttch(requestBody:GetNewINGSTR2ReportAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewINGSTR2ReportAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetNewINGSTR2ReportAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewINGSTR2ReportAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewINGSTR23
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR23
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR23_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR23_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewINGSTR23(requestBody:GetNewINGSTR23_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewINGSTR23_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetNewINGSTR23", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewINGSTR23_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewINGSTR26C
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR26C
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR26C_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR26C_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewINGSTR26C(requestBody:GetNewINGSTR26C_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewINGSTR26C_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetNewINGSTR26C", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewINGSTR26C_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewINGSTR2MatchedLine
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2MatchedLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2MatchedLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2MatchedLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewINGSTR2MatchedLine(requestBody:GetNewINGSTR2MatchedLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewINGSTR2MatchedLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetNewINGSTR2MatchedLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewINGSTR2MatchedLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewINGSTR2Transaction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2Transaction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2Transaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2Transaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewINGSTR2Transaction(requestBody:GetNewINGSTR2Transaction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewINGSTR2Transaction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetNewINGSTR2Transaction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewINGSTR2Transaction_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportImportSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR23Row{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR23Row,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR26CRow{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR26CRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2MatchedLineRow{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR2MatchedLineRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR2ReportAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR2ReportListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR2ReportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2TransactionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_INGSTR2TransactionRow,
}

export interface Erp_Tablesets_INGSTR23Row{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "CheckBox01":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "ShortChar01":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "APInvoiceAmt":number,
   "APInvoiceDate":string,
   "APInvoiceLegalNumber":string,
   "APInvoiceNum":string,
      /**  CESS Amount  */  
   "CESSAmt":number,
      /**  CGST Amount  */  
   "CGSTAmt":number,
      /**  Changed On  */  
   "ChangedOn":string,
      /**  Created On  */  
   "CreatedOn":string,
      /**  Eligibility  */  
   "Eligibility":string,
      /**  GST ID  */  
   "GSTID":string,
      /**  IGST Amount  */  
   "IGSTAmt":number,
   "ImportCounter":number,
      /**  Matched AP Invoice CESS Amount  */  
   "INGSTR2TransactionCESSAmt":number,
      /**  Matched AP Invoice CGST Amount  */  
   "INGSTR2TransactionCGSTAmt":number,
      /**  Matched AP Invoice IGST Amoun  */  
   "INGSTR2TransactionIGSTAmt":number,
      /**  Matched AP Invoice ITC CESS Amoun  */  
   "INGSTR2TransactionITCCESSAmt":number,
      /**  Matched AP Invoice ITC CGST Amoun  */  
   "INGSTR2TransactionITCCGSTAmt":number,
      /**  Matched AP Invoice ITC IGST Amoun  */  
   "INGSTR2TransactionITCIGSTAmt":number,
      /**  Matched AP Invoice ITC SGST Amoun  */  
   "INGSTR2TransactionITCSGSTAmt":number,
      /**  Matched AP Invoice Rate  */  
   "INGSTR2TransactionRate":number,
      /**  Matched AP Invoice SGST Amoun  */  
   "INGSTR2TransactionSGSTAmt":number,
      /**  Matched AP Invoice Taxable Amoun  */  
   "INGSTR2TransactionTaxableAmt":number,
      /**  Invoice Amount  */  
   "InvoiceAmt":number,
      /**  Invoice Date  */  
   "InvoiceDate":string,
      /**  Invoice Number  */  
   "InvoiceNum":string,
      /**  Invoice Type  */  
   "InvoiceType":string,
      /**  ITC CESS Amount  */  
   "ITCCESSAmt":number,
      /**  ITC CGST Amount  */  
   "ITCCGSTAmt":number,
      /**  ITC IGST Amount  */  
   "ITCIGSTAmt":number,
      /**  ITC SGST Amount  */  
   "ITCSGSTAmt":number,
      /**  Latest Import  */  
   "LatestImport":number,
      /**  Line Status  */  
   "LineStatus":number,
      /**  Matched  */  
   "Matched":boolean,
      /**  Message  */  
   "Message":string,
      /**  Notes  */  
   "Notes":string,
      /**  Place of Supply  */  
   "PlaceSupply":string,
      /**  Rate  */  
   "Rate":number,
      /**  Report ID  */  
   "ReportID":string,
      /**  Row Number  */  
   "RowNum":number,
      /**  SGST Amount  */  
   "SGSTAmt":number,
      /**  Taxable Amount  */  
   "TaxableAmt":number,
   "APVendorNum":number,
   "Manual":boolean,
   "VendorName":string,
   "VendorVendorID":string,
   "ChangedBy":string,
   "CreatedBy":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_INGSTR26CRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "CheckBox01":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "ShortChar01":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "APInvoiceAmt":number,
   "APInvoiceDate":string,
   "APInvoiceLegalNumber":string,
   "APInvoiceNum":string,
      /**  CESS Amount  */  
   "CESSAmt":number,
      /**  CGST Amount  */  
   "CGSTAmt":number,
      /**  Changed On  */  
   "ChangedOn":string,
      /**  Created On  */  
   "CreatedOn":string,
      /**  Eligibility  */  
   "Eligibility":string,
      /**  GST ID  */  
   "GSTID":string,
      /**  IGST Amount  */  
   "IGSTAmt":number,
   "ImportCounter":number,
      /**  Matched AP Invoice CESS Amount  */  
   "INGSTR2TransactionCESSAmt":number,
      /**  Matched AP Invoice CGST Amount  */  
   "INGSTR2TransactionCGSTAmt":number,
      /**  Matched AP Invoice IGST Amoun  */  
   "INGSTR2TransactionIGSTAmt":number,
      /**  Matched AP Invoice ITC CESS Amoun  */  
   "INGSTR2TransactionITCCESSAmt":number,
      /**  Matched AP Invoice ITC CGST Amoun  */  
   "INGSTR2TransactionITCCGSTAmt":number,
      /**  Matched AP Invoice ITC IGST Amoun  */  
   "INGSTR2TransactionITCIGSTAmt":number,
      /**  Matched AP Invoice ITC SGST Amoun  */  
   "INGSTR2TransactionITCSGSTAmt":number,
      /**  Matched AP Invoice Rate  */  
   "INGSTR2TransactionRate":number,
      /**  Matched AP Invoice SGST Amoun  */  
   "INGSTR2TransactionSGSTAmt":number,
      /**  Matched AP Invoice Taxable Amoun  */  
   "INGSTR2TransactionTaxableAmt":number,
      /**  Note Amount  */  
   "NoteAmt":number,
      /**  Note Date  */  
   "NoteDate":string,
      /**  Note Number  */  
   "NoteNum":string,
      /**  Note Type  */  
   "NoteType":string,
      /**  ITC CESS Amount  */  
   "ITCCESSAmt":number,
      /**  ITC CGST Amount  */  
   "ITCCGSTAmt":number,
      /**  ITC IGST Amount  */  
   "ITCIGSTAmt":number,
      /**  ITC SGST Amount  */  
   "ITCSGSTAmt":number,
      /**  Latest Import  */  
   "LatestImport":number,
      /**  Line Status  */  
   "LineStatus":number,
      /**  Matched  */  
   "Matched":boolean,
      /**  Message  */  
   "Message":string,
      /**  Notes  */  
   "Notes":string,
      /**  Rate  */  
   "Rate":number,
      /**  Report ID  */  
   "ReportID":string,
      /**  Row Number  */  
   "RowNum":number,
      /**  SGST Amount  */  
   "SGSTAmt":number,
      /**  Taxable Amount  */  
   "TaxableAmt":number,
      /**  Reason  */  
   "Reason":string,
   "APVendorNum":number,
   "VendorVendorID":string,
   "VendorName":string,
   "Manual":boolean,
   "ChangedBy":string,
   "CreatedBy":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_INGSTR2MatchedLineRow{
      /**  Company  */  
   "Company":string,
      /**  ReportID  */  
   "ReportID":string,
      /**  Section  */  
   "Section":string,
      /**  TransactionType  */  
   "TransactionType":number,
      /**  ExternalSysRowID  */  
   "ExternalSysRowID":string,
      /**  Key1  */  
   "Key1":string,
      /**  Key2  */  
   "Key2":string,
      /**  IntKey1  */  
   "IntKey1":number,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_INGSTR2ReportAttchRow{
   "Company":string,
   "ReportID":string,
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

export interface Erp_Tablesets_INGSTR2ReportListRow{
      /**  ReportID  */  
   "ReportID":string,
      /**  FinancialPeriod  */  
   "FinancialPeriod":string,
      /**  Description  */  
   "Description":string,
      /**  Status  */  
   "Status":number,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  ConfirmedBy  */  
   "ConfirmedBy":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_INGSTR2ReportRow{
      /**  Company  */  
   "Company":string,
      /**  ReportID  */  
   "ReportID":string,
      /**  FinancialPeriod  */  
   "FinancialPeriod":string,
      /**  Description  */  
   "Description":string,
      /**  FromDate  */  
   "FromDate":string,
      /**  ToDate  */  
   "ToDate":string,
      /**  Status  */  
   "Status":number,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  ConfirmedBy  */  
   "ConfirmedBy":string,
      /**  ConfirmDate  */  
   "ConfirmDate":string,
      /**  SkipInvoices  */  
   "SkipInvoices":boolean,
      /**  ReportNotes  */  
   "ReportNotes":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "Imported":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_INGSTR2TransactionRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Integer Key field 1  */  
   "IntKey1":number,
      /**  Integer Key field 2  */  
   "IntKey2":number,
      /**  Integer Key field 3  */  
   "IntKey3":number,
      /**  Character Key field 1  */  
   "Key1":string,
      /**  Character Key field 2  */  
   "Key2":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ReportID":string,
   "TransactionType":number,
   "RowNum":number,
   "Rate":number,
   "TaxableAmt":number,
   "IGSTAmt":number,
   "CGSTAmt":number,
   "SGSTAmt":number,
   "CESSAmt":number,
   "ITCIGSTAmt":number,
   "ITCCGSTAmt":number,
   "ITCSGSTAmt":number,
   "ITCCESSAmt":number,
   "InvoiceNum":string,
   "VendorNum":number,
   "Matched":boolean,
   "Selected":boolean,
   "InvoiceAmt":number,
   "BitFlag":number,
   "APInvHedInvoiceAmt":number,
   "APInvHedInvoiceDate":string,
   "APInvHedLegalNumber":string,
   "VendorName":string,
   "VendorCountry":string,
   "VendorVendorID":string,
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
      @param reportID
   */  
export interface DeleteByID_input{
   reportID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param reportID
      @param section
      @param ds
   */  
export interface DeleteImportData_input{
      /**  Report ID  */  
   reportID:string,
      /**  Section  */  
   section:string,
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface DeleteImportData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

export interface Erp_Tablesets_INGSTR23Row{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   CheckBox01:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   ShortChar01:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   APInvoiceAmt:number,
   APInvoiceDate:string,
   APInvoiceLegalNumber:string,
   APInvoiceNum:string,
      /**  CESS Amount  */  
   CESSAmt:number,
      /**  CGST Amount  */  
   CGSTAmt:number,
      /**  Changed On  */  
   ChangedOn:string,
      /**  Created On  */  
   CreatedOn:string,
      /**  Eligibility  */  
   Eligibility:string,
      /**  GST ID  */  
   GSTID:string,
      /**  IGST Amount  */  
   IGSTAmt:number,
   ImportCounter:number,
      /**  Matched AP Invoice CESS Amount  */  
   INGSTR2TransactionCESSAmt:number,
      /**  Matched AP Invoice CGST Amount  */  
   INGSTR2TransactionCGSTAmt:number,
      /**  Matched AP Invoice IGST Amoun  */  
   INGSTR2TransactionIGSTAmt:number,
      /**  Matched AP Invoice ITC CESS Amoun  */  
   INGSTR2TransactionITCCESSAmt:number,
      /**  Matched AP Invoice ITC CGST Amoun  */  
   INGSTR2TransactionITCCGSTAmt:number,
      /**  Matched AP Invoice ITC IGST Amoun  */  
   INGSTR2TransactionITCIGSTAmt:number,
      /**  Matched AP Invoice ITC SGST Amoun  */  
   INGSTR2TransactionITCSGSTAmt:number,
      /**  Matched AP Invoice Rate  */  
   INGSTR2TransactionRate:number,
      /**  Matched AP Invoice SGST Amoun  */  
   INGSTR2TransactionSGSTAmt:number,
      /**  Matched AP Invoice Taxable Amoun  */  
   INGSTR2TransactionTaxableAmt:number,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Invoice Number  */  
   InvoiceNum:string,
      /**  Invoice Type  */  
   InvoiceType:string,
      /**  ITC CESS Amount  */  
   ITCCESSAmt:number,
      /**  ITC CGST Amount  */  
   ITCCGSTAmt:number,
      /**  ITC IGST Amount  */  
   ITCIGSTAmt:number,
      /**  ITC SGST Amount  */  
   ITCSGSTAmt:number,
      /**  Latest Import  */  
   LatestImport:number,
      /**  Line Status  */  
   LineStatus:number,
      /**  Matched  */  
   Matched:boolean,
      /**  Message  */  
   Message:string,
      /**  Notes  */  
   Notes:string,
      /**  Place of Supply  */  
   PlaceSupply:string,
      /**  Rate  */  
   Rate:number,
      /**  Report ID  */  
   ReportID:string,
      /**  Row Number  */  
   RowNum:number,
      /**  SGST Amount  */  
   SGSTAmt:number,
      /**  Taxable Amount  */  
   TaxableAmt:number,
   APVendorNum:number,
   Manual:boolean,
   VendorName:string,
   VendorVendorID:string,
   ChangedBy:string,
   CreatedBy:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_INGSTR26CRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   CheckBox01:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   ShortChar01:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   APInvoiceAmt:number,
   APInvoiceDate:string,
   APInvoiceLegalNumber:string,
   APInvoiceNum:string,
      /**  CESS Amount  */  
   CESSAmt:number,
      /**  CGST Amount  */  
   CGSTAmt:number,
      /**  Changed On  */  
   ChangedOn:string,
      /**  Created On  */  
   CreatedOn:string,
      /**  Eligibility  */  
   Eligibility:string,
      /**  GST ID  */  
   GSTID:string,
      /**  IGST Amount  */  
   IGSTAmt:number,
   ImportCounter:number,
      /**  Matched AP Invoice CESS Amount  */  
   INGSTR2TransactionCESSAmt:number,
      /**  Matched AP Invoice CGST Amount  */  
   INGSTR2TransactionCGSTAmt:number,
      /**  Matched AP Invoice IGST Amoun  */  
   INGSTR2TransactionIGSTAmt:number,
      /**  Matched AP Invoice ITC CESS Amoun  */  
   INGSTR2TransactionITCCESSAmt:number,
      /**  Matched AP Invoice ITC CGST Amoun  */  
   INGSTR2TransactionITCCGSTAmt:number,
      /**  Matched AP Invoice ITC IGST Amoun  */  
   INGSTR2TransactionITCIGSTAmt:number,
      /**  Matched AP Invoice ITC SGST Amoun  */  
   INGSTR2TransactionITCSGSTAmt:number,
      /**  Matched AP Invoice Rate  */  
   INGSTR2TransactionRate:number,
      /**  Matched AP Invoice SGST Amoun  */  
   INGSTR2TransactionSGSTAmt:number,
      /**  Matched AP Invoice Taxable Amoun  */  
   INGSTR2TransactionTaxableAmt:number,
      /**  Note Amount  */  
   NoteAmt:number,
      /**  Note Date  */  
   NoteDate:string,
      /**  Note Number  */  
   NoteNum:string,
      /**  Note Type  */  
   NoteType:string,
      /**  ITC CESS Amount  */  
   ITCCESSAmt:number,
      /**  ITC CGST Amount  */  
   ITCCGSTAmt:number,
      /**  ITC IGST Amount  */  
   ITCIGSTAmt:number,
      /**  ITC SGST Amount  */  
   ITCSGSTAmt:number,
      /**  Latest Import  */  
   LatestImport:number,
      /**  Line Status  */  
   LineStatus:number,
      /**  Matched  */  
   Matched:boolean,
      /**  Message  */  
   Message:string,
      /**  Notes  */  
   Notes:string,
      /**  Rate  */  
   Rate:number,
      /**  Report ID  */  
   ReportID:string,
      /**  Row Number  */  
   RowNum:number,
      /**  SGST Amount  */  
   SGSTAmt:number,
      /**  Taxable Amount  */  
   TaxableAmt:number,
      /**  Reason  */  
   Reason:string,
   APVendorNum:number,
   VendorVendorID:string,
   VendorName:string,
   Manual:boolean,
   ChangedBy:string,
   CreatedBy:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_INGSTR2MatchedLineRow{
      /**  Company  */  
   Company:string,
      /**  ReportID  */  
   ReportID:string,
      /**  Section  */  
   Section:string,
      /**  TransactionType  */  
   TransactionType:number,
      /**  ExternalSysRowID  */  
   ExternalSysRowID:string,
      /**  Key1  */  
   Key1:string,
      /**  Key2  */  
   Key2:string,
      /**  IntKey1  */  
   IntKey1:number,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_INGSTR2ReportAttchRow{
   Company:string,
   ReportID:string,
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

export interface Erp_Tablesets_INGSTR2ReportImportTableset{
   INGSTR2Report:Erp_Tablesets_INGSTR2ReportRow[],
   INGSTR2ReportAttch:Erp_Tablesets_INGSTR2ReportAttchRow[],
   INGSTR23:Erp_Tablesets_INGSTR23Row[],
   INGSTR26C:Erp_Tablesets_INGSTR26CRow[],
   INGSTR2MatchedLine:Erp_Tablesets_INGSTR2MatchedLineRow[],
   INGSTR2Transaction:Erp_Tablesets_INGSTR2TransactionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_INGSTR2ReportListRow{
      /**  ReportID  */  
   ReportID:string,
      /**  FinancialPeriod  */  
   FinancialPeriod:string,
      /**  Description  */  
   Description:string,
      /**  Status  */  
   Status:number,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  ConfirmedBy  */  
   ConfirmedBy:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_INGSTR2ReportListTableset{
   INGSTR2ReportList:Erp_Tablesets_INGSTR2ReportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_INGSTR2ReportRow{
      /**  Company  */  
   Company:string,
      /**  ReportID  */  
   ReportID:string,
      /**  FinancialPeriod  */  
   FinancialPeriod:string,
      /**  Description  */  
   Description:string,
      /**  FromDate  */  
   FromDate:string,
      /**  ToDate  */  
   ToDate:string,
      /**  Status  */  
   Status:number,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  ConfirmedBy  */  
   ConfirmedBy:string,
      /**  ConfirmDate  */  
   ConfirmDate:string,
      /**  SkipInvoices  */  
   SkipInvoices:boolean,
      /**  ReportNotes  */  
   ReportNotes:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   Imported:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_INGSTR2TransactionRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Integer Key field 1  */  
   IntKey1:number,
      /**  Integer Key field 2  */  
   IntKey2:number,
      /**  Integer Key field 3  */  
   IntKey3:number,
      /**  Character Key field 1  */  
   Key1:string,
      /**  Character Key field 2  */  
   Key2:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ReportID:string,
   TransactionType:number,
   RowNum:number,
   Rate:number,
   TaxableAmt:number,
   IGSTAmt:number,
   CGSTAmt:number,
   SGSTAmt:number,
   CESSAmt:number,
   ITCIGSTAmt:number,
   ITCCGSTAmt:number,
   ITCSGSTAmt:number,
   ITCCESSAmt:number,
   InvoiceNum:string,
   VendorNum:number,
   Matched:boolean,
   Selected:boolean,
   InvoiceAmt:number,
   BitFlag:number,
   APInvHedInvoiceAmt:number,
   APInvHedInvoiceDate:string,
   APInvHedLegalNumber:string,
   VendorName:string,
   VendorCountry:string,
   VendorVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtINGSTR2ReportImportTableset{
   INGSTR2Report:Erp_Tablesets_INGSTR2ReportRow[],
   INGSTR2ReportAttch:Erp_Tablesets_INGSTR2ReportAttchRow[],
   INGSTR23:Erp_Tablesets_INGSTR23Row[],
   INGSTR26C:Erp_Tablesets_INGSTR26CRow[],
   INGSTR2MatchedLine:Erp_Tablesets_INGSTR2MatchedLineRow[],
   INGSTR2Transaction:Erp_Tablesets_INGSTR2TransactionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reportID
      @param section
   */  
export interface ExistsImportDataSection_input{
      /**  Report ID  */  
   reportID:string,
      /**  Section key  */  
   section:string,
}

export interface ExistsImportDataSection_output{
   returnObj:boolean,
}

   /** Required : 
      @param reportID
   */  
export interface ExistsImportData_input{
      /**  Report ID  */  
   reportID:string,
}

export interface ExistsImportData_output{
   returnObj:boolean,
}

   /** Required : 
      @param reportID
   */  
export interface GetByID_input{
   reportID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_INGSTR2ReportImportTableset[],
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
   returnObj:Erp_Tablesets_INGSTR2ReportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param localName
      @param key1
      @param key2
      @param key3
   */  
export interface GetNewINGSTR23_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
   localName:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetNewINGSTR23_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ds
      @param localName
      @param key1
      @param key2
      @param key3
   */  
export interface GetNewINGSTR26C_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
   localName:string,
   key1:string,
   key2:string,
   key3:string,
}

export interface GetNewINGSTR26C_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ds
      @param reportID
      @param section
      @param transactionType
   */  
export interface GetNewINGSTR2MatchedLine_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
   reportID:string,
   section:string,
   transactionType:number,
}

export interface GetNewINGSTR2MatchedLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ds
      @param reportID
   */  
export interface GetNewINGSTR2ReportAttch_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
   reportID:string,
}

export interface GetNewINGSTR2ReportAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewINGSTR2Report_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface GetNewINGSTR2Report_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ds
      @param localName
      @param key1
      @param intKey1
      @param intKey2
      @param key2
   */  
export interface GetNewINGSTR2Transaction_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
   localName:string,
   key1:string,
   intKey1:number,
   intKey2:number,
   key2:string,
}

export interface GetNewINGSTR2Transaction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param whereClauseINGSTR2Report
      @param whereClauseINGSTR2ReportAttch
      @param whereClauseINGSTR23
      @param whereClauseINGSTR26C
      @param whereClauseINGSTR2MatchedLine
      @param whereClauseINGSTR2Transaction
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseINGSTR2Report:string,
   whereClauseINGSTR2ReportAttch:string,
   whereClauseINGSTR23:string,
   whereClauseINGSTR26C:string,
   whereClauseINGSTR2MatchedLine:string,
   whereClauseINGSTR2Transaction:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_INGSTR2ReportImportTableset[],
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
      @param eftHeadUID
      @param section
      @param importFile
      @param reportID
   */  
export interface ImportStatement_input{
      /**  EFTHeadUID  */  
   eftHeadUID:number,
      /**  Section  */  
   section:string,
      /**  Import file name  */  
   importFile:string,
      /**  Report ID  */  
   reportID:string,
}

export interface ImportStatement_output{
}

   /** Required : 
      @param reportID
   */  
export interface IsApproveAllowed_input{
      /**  Report ID  */  
   reportID:string,
}

export interface IsApproveAllowed_output{
parameters : {
      /**  output parameters  */  
   result:number,
}
}

   /** Required : 
      @param ipReportID
      @param ipSectionName
      @param ipRematch
      @param ds
   */  
export interface MatchSection_input{
   ipReportID:string,
   ipSectionName:string,
   ipRematch:boolean,
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface MatchSection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ipReportID
      @param ipSectionName
      @param ipGSTR2XSysRowID
      @param ds
   */  
export interface MatchTransaction2Line_input{
   ipReportID:string,
   ipSectionName:string,
   ipGSTR2XSysRowID:string,
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface MatchTransaction2Line_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ipReportID
      @param ipSection
      @param ds
   */  
export interface RetrieveTransactions_input{
      /**  From date  */  
   ipReportID:string,
      /**  To date  */  
   ipSection:string,
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface RetrieveTransactions_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ipReportID
      @param ipSectionName
      @param ipINGSTR2XSysRowID
      @param ds
   */  
export interface UnmatchFromLine_input{
   ipReportID:string,
   ipSectionName:string,
   ipINGSTR2XSysRowID:string,
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface UnmatchFromLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtINGSTR2ReportImportTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtINGSTR2ReportImportTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_INGSTR2ReportImportTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_INGSTR2ReportImportTableset,
}
}

