import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DemandImportEntrySvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/$metadata", {
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
   Description: Get DemandImportEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandImportEntries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpRow
   */  
export function get_DemandImportEntries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandImportEntries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ImportGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandImportEntries(requestBody:Erp_Tablesets_ImportGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DemandImportEntry item
   Description: Calls GetByID to retrieve the DemandImportEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandImportEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ImportGrpRow
   */  
export function get_DemandImportEntries_Company_ImportID(Company:string, ImportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ImportGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")", {
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
         resolve(data as Erp_Tablesets_ImportGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandImportEntry for the service
   Description: Calls UpdateExt to update DemandImportEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandImportEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandImportEntries_Company_ImportID(Company:string, ImportID:string, requestBody:Erp_Tablesets_ImportGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")", {
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
   Summary: Call UpdateExt to delete DemandImportEntry item
   Description: Call UpdateExt to delete DemandImportEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandImportEntry
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandImportEntries_Company_ImportID(Company:string, ImportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")", {
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
   Description: Get DemandHeadImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandHeadImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadImportRow
   */  
export function get_DemandImportEntries_Company_ImportID_DemandHeadImports(Company:string, ImportID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")/DemandHeadImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandHeadImport item
   Description: Calls GetByID to retrieve the DemandHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandHeadImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandHeadImportRow
   */  
export function get_DemandImportEntries_Company_ImportID_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
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
         resolve(data as Erp_Tablesets_DemandHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DemandHeadImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandHeadImports
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadImportRow
   */  
export function get_DemandHeadImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandHeadImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DemandHeadImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandHeadImports(requestBody:Erp_Tablesets_DemandHeadImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DemandHeadImport item
   Description: Calls GetByID to retrieve the DemandHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandHeadImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandHeadImportRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandHeadImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
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
         resolve(data as Erp_Tablesets_DemandHeadImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandHeadImport for the service
   Description: Calls UpdateExt to update DemandHeadImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandHeadImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, requestBody:Erp_Tablesets_DemandHeadImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
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
   Summary: Call UpdateExt to delete DemandHeadImport item
   Description: Call UpdateExt to delete DemandHeadImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandHeadImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")", {
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
   Description: Get PkgControlLabelValueImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlLabelValueImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelValueImportRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_PkgControlLabelValueImports(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/PkgControlLabelValueImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PkgControlLabelValueImport item
   Description: Calls GetByID to retrieve the PkgControlLabelValueImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelValueImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ShipToCustID Desc: ShipToCustID   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, Plant:string, ShipToCustID:string, ShipToNum:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlLabelValueImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")", {
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
         resolve(data as Erp_Tablesets_PkgControlLabelValueImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DemandDetailImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandDetailImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailImportRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDetailImports(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetailImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandDetailImport item
   Description: Calls GetByID to retrieve the DemandDetailImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetailImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandDetailImportRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandDetailImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_DemandDetailImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DemandMiscChgImportDHs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgImportDHs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportDHRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandMiscChgImportDHs(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgImportDHs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandMiscChgImportDH item
   Description: Calls GetByID to retrieve the DemandMiscChgImportDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImportDH1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   */  
export function get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgImportDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_DemandMiscChgImportDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PkgControlLabelValueImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlLabelValueImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelValueImportRow
   */  
export function get_PkgControlLabelValueImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlLabelValueImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlLabelValueImports(requestBody:Erp_Tablesets_PkgControlLabelValueImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PkgControlLabelValueImport item
   Description: Calls GetByID to retrieve the PkgControlLabelValueImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelValueImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ShipToCustID Desc: ShipToCustID   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   */  
export function get_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company:string, Plant:string, ShipToCustID:string, ShipToNum:string, PartNum:string, DemandContractNum:string, DemandHeadSeq:string, ImportID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PkgControlLabelValueImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")", {
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
         resolve(data as Erp_Tablesets_PkgControlLabelValueImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PkgControlLabelValueImport for the service
   Description: Calls UpdateExt to update PkgControlLabelValueImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlLabelValueImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ShipToCustID Desc: ShipToCustID   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company:string, Plant:string, ShipToCustID:string, ShipToNum:string, PartNum:string, DemandContractNum:string, DemandHeadSeq:string, ImportID:string, requestBody:Erp_Tablesets_PkgControlLabelValueImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")", {
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
   Summary: Call UpdateExt to delete PkgControlLabelValueImport item
   Description: Call UpdateExt to delete PkgControlLabelValueImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlLabelValueImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ShipToCustID Desc: ShipToCustID   Required: True   Allow empty value : True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company:string, Plant:string, ShipToCustID:string, ShipToNum:string, PartNum:string, DemandContractNum:string, DemandHeadSeq:string, ImportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")", {
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
   Description: Get DemandDetailImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandDetailImports
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailImportRow
   */  
export function get_DemandDetailImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandDetailImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DemandDetailImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandDetailImports(requestBody:Erp_Tablesets_DemandDetailImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DemandDetailImport item
   Description: Calls GetByID to retrieve the DemandDetailImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetailImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandDetailImportRow
   */  
export function get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandDetailImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_DemandDetailImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandDetailImport for the service
   Description: Calls UpdateExt to update DemandDetailImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandDetailImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, requestBody:Erp_Tablesets_DemandDetailImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete DemandDetailImport item
   Description: Call UpdateExt to delete DemandDetailImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandDetailImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", {
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
   Description: Get DemandMiscChgImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportRow
   */  
export function get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgImports(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandMiscChgImport item
   Description: Calls GetByID to retrieve the DemandMiscChgImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   */  
export function get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_DemandMiscChgImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DemandScheduleImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandScheduleImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleImportRow
   */  
export function get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleImports(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandScheduleImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DemandScheduleImport item
   Description: Calls GetByID to retrieve the DemandScheduleImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandScheduleImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   */  
export function get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandScheduleImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
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
         resolve(data as Erp_Tablesets_DemandScheduleImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DemandMiscChgImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportRow
   */  
export function get_DemandMiscChgImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandMiscChgImports(requestBody:Erp_Tablesets_DemandMiscChgImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DemandMiscChgImport item
   Description: Calls GetByID to retrieve the DemandMiscChgImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   */  
export function get_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_DemandMiscChgImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandMiscChgImport for the service
   Description: Calls UpdateExt to update DemandMiscChgImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChgImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, requestBody:Erp_Tablesets_DemandMiscChgImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete DemandMiscChgImport item
   Description: Call UpdateExt to delete DemandMiscChgImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChgImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
   Description: Get DemandScheduleImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandScheduleImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleImportRow
   */  
export function get_DemandScheduleImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandScheduleImports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DemandScheduleImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandScheduleImports(requestBody:Erp_Tablesets_DemandScheduleImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DemandScheduleImport item
   Description: Calls GetByID to retrieve the DemandScheduleImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandScheduleImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   */  
export function get_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandScheduleImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
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
         resolve(data as Erp_Tablesets_DemandScheduleImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandScheduleImport for the service
   Description: Calls UpdateExt to update DemandScheduleImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandScheduleImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, requestBody:Erp_Tablesets_DemandScheduleImportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
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
   Summary: Call UpdateExt to delete DemandScheduleImport item
   Description: Call UpdateExt to delete DemandScheduleImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandScheduleImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param DemandScheduleSeq Desc: DemandScheduleSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, DemandScheduleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", {
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
   Description: Get DemandMiscChgImportDHs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgImportDHs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportDHRow
   */  
export function get_DemandMiscChgImportDHs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgImportDHs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemandMiscChgImportDHs(requestBody:Erp_Tablesets_DemandMiscChgImportDHRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the DemandMiscChgImportDH item
   Description: Calls GetByID to retrieve the DemandMiscChgImportDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImportDH
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   */  
export function get_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DemandMiscChgImportDHRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_DemandMiscChgImportDHRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DemandMiscChgImportDH for the service
   Description: Calls UpdateExt to update DemandMiscChgImportDH. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChgImportDH
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, requestBody:Erp_Tablesets_DemandMiscChgImportDHRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete DemandMiscChgImportDH item
   Description: Call UpdateExt to delete DemandMiscChgImportDH item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChgImportDH
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param DemandContractNum Desc: DemandContractNum   Required: True
      @param DemandHeadSeq Desc: DemandHeadSeq   Required: True
      @param DemandDtlSeq Desc: DemandDtlSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company:string, ImportID:string, DemandContractNum:string, DemandHeadSeq:string, DemandDtlSeq:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseImportGrp:string, whereClauseDemandHeadImport:string, whereClausePkgControlLabelValueImport:string, whereClauseDemandDetailImport:string, whereClauseDemandMiscChgImport:string, whereClauseDemandScheduleImport:string, whereClauseDemandMiscChgImportDH:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseImportGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportGrp=" + whereClauseImportGrp
   }
   if(typeof whereClauseDemandHeadImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandHeadImport=" + whereClauseDemandHeadImport
   }
   if(typeof whereClausePkgControlLabelValueImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePkgControlLabelValueImport=" + whereClausePkgControlLabelValueImport
   }
   if(typeof whereClauseDemandDetailImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandDetailImport=" + whereClauseDemandDetailImport
   }
   if(typeof whereClauseDemandMiscChgImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandMiscChgImport=" + whereClauseDemandMiscChgImport
   }
   if(typeof whereClauseDemandScheduleImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandScheduleImport=" + whereClauseDemandScheduleImport
   }
   if(typeof whereClauseDemandMiscChgImportDH!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDemandMiscChgImportDH=" + whereClauseDemandMiscChgImportDH
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, importID:string, epicorHeaders?:Headers){
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
   if(typeof importID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "importID=" + importID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetList" + params, {
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
   Summary: Invoke method ChangeDemandDetailDemandContractLine
   Description: Update Demand Detail information when the Demand Contract Line is changed.
   OperationID: ChangeDemandDetailDemandContractLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailDemandContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailDemandContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailDemandContractLine(requestBody:ChangeDemandDetailDemandContractLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandDetailDemandContractLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandDetailDemandContractLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandDetailDemandContractLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandDetailMktgCamp
   Description: Update MktgCampaign on the DmdCntDtl.
   OperationID: ChangeDemandDetailMktgCamp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailMktgCamp(requestBody:ChangeDemandDetailMktgCamp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandDetailMktgCamp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandDetailMktgCamp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandDetailMktgCamp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandDetailPartNum
   Description: Update partnum on the DmdCntDtl.
   OperationID: ChangeDemandDetailPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailPartNum(requestBody:ChangeDemandDetailPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandDetailPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandDetailPartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandDetailPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandDetailRevisionNum
   Description: Update Demand Detail information when the Part Revision Number is changed.
   OperationID: ChangeDemandDetailRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandDetailRevisionNum(requestBody:ChangeDemandDetailRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandDetailRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandDetailRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandDetailRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandHeadCustID
   Description: Method to call when changing the Customer ID on the DemandHead record.
Validates the Customer ID and ressets the ShipTo to the Customer default.
   OperationID: ChangeDemandHeadCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadCustID(requestBody:ChangeDemandHeadCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandHeadCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandHeadCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandHeadCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandHeadDemandContract
   Description: Update Demand Header information when the Demand Contract is changed.
   OperationID: ChangeDemandHeadDemandContract
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadDemandContract(requestBody:ChangeDemandHeadDemandContract_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandHeadDemandContract_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandHeadDemandContract", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandHeadDemandContract_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandHeadERSOrder
   Description: Update Demand Header information when the ERS Order changes.
   OperationID: ChangeDemandHeadERSOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadERSOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadERSOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadERSOrder(requestBody:ChangeDemandHeadERSOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandHeadERSOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandHeadERSOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandHeadERSOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandHeadShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandHead record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandHeadShipToCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadShipToCustID(requestBody:ChangeDemandHeadShipToCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandHeadShipToCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandHeadShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandHeadShipToCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandHeadShipToNum
   Description: Update Demand Header information when the Ship To Num changes.
   OperationID: ChangeDemandHeadShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadShipToNum(requestBody:ChangeDemandHeadShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandHeadShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandHeadShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandHeadShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandHeadUseOTS
   Description: Method to call when changing the UseOTS field the DemandHead record.
Refreshes the address list and contact info
   OperationID: ChangeDemandHeadUseOTS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandHeadUseOTS(requestBody:ChangeDemandHeadUseOTS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandHeadUseOTS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandHeadUseOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandHeadUseOTS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleMarkForNum
   Description: Update DemandSchedule information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeDemandScheduleMarkForNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMarkForNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMarkForNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleMarkForNum(requestBody:ChangeDemandScheduleMarkForNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleMarkForNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleMarkForNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleMarkForNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleMFCustID
   Description: Method to call when changing the Mark For Customer ID on the DemandSchedule record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleMFCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleMFCustID(requestBody:ChangeDemandScheduleMFCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleMFCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleMFCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleMFCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleOTSDetails
   Description: Method to call when changing the OTS fields the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleOTSDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleOTSDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleOTSDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleOTSDetails(requestBody:ChangeDemandScheduleOTSDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleOTSDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleOTSDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleOTSDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandSchedulePlant
   Description: Update DemandSchedule information with values from the Plant when the Plant is changed.
   OperationID: ChangeDemandSchedulePlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandSchedulePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandSchedulePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandSchedulePlant(requestBody:ChangeDemandSchedulePlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandSchedulePlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandSchedulePlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandSchedulePlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleSellingReqQty
   Description: Update Demand Schedule information when the Selling Req Qty is changed.
   OperationID: ChangeDemandScheduleSellingReqQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleSellingReqQty(requestBody:ChangeDemandScheduleSellingReqQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleSellingReqQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleSellingReqQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleSellingReqQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandSchedule record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleShipToCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleShipToCustID(requestBody:ChangeDemandScheduleShipToCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleShipToCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleShipToCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleShipToNum
   Description: Update DemandSchedule information with values from the Ship To when the Ship To is changed.
   OperationID: ChangeDemandScheduleShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleShipToNum(requestBody:ChangeDemandScheduleShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleShipToNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleUseOTMF
   Description: Method to call when changing the UseOTMF field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTMF
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleUseOTMF(requestBody:ChangeDemandScheduleUseOTMF_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleUseOTMF_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleUseOTMF", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleUseOTMF_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDemandScheduleUseOTS
   Description: Method to call when changing the UseOTS field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDemandScheduleUseOTS(requestBody:ChangeDemandScheduleUseOTS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDemandScheduleUseOTS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeDemandScheduleUseOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDemandScheduleUseOTS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMiscCode
   Description: This method returns default information for the MiscChrg.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field.
Also allows IMDemandMiscChgDH and IMDemandMiscChg to use the same code
   OperationID: ChangeMiscCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscCode(requestBody:ChangeMiscCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMiscCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ChangeMiscCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeMiscCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPartRevisionChange
   Description: The method is to be run on leave of the PartNum and Revision fields
before the ChangePart, ChangeRevision, or Update methods are run.
When run before CreateOrderFromQuote, the Part Number expected is the part number
from the quote.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartRevisionChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPartRevisionChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartRevisionChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartRevisionChange(requestBody:CheckPartRevisionChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPartRevisionChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/CheckPartRevisionChange", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckPartRevisionChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPriceDiscrepancy
   Description: Check if the differente between the UnitPrice and EDIUnitPrice is less than the value defd in
the PriceTolerance field of the ShipTo or Customer tables.
   OperationID: GetPriceDiscrepancy
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPriceDiscrepancy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceDiscrepancy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceDiscrepancy(requestBody:GetPriceDiscrepancy_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPriceDiscrepancy_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetPriceDiscrepancy", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPriceDiscrepancy_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReadyToProcess
   Description: Method to remove the Error Flag to the Demand PO records identified by the IntQueID.
   OperationID: ReadyToProcess
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReadyToProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadyToProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReadyToProcess(requestBody:ReadyToProcess_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReadyToProcess_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ReadyToProcess", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ReadyToProcess_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportEDIb4Tran
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIb4Tran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportEDIb4Tran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIb4Tran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportEDIb4Tran(requestBody:ImportEDIb4Tran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportEDIb4Tran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ImportEDIb4Tran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportEDIb4Tran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportEDIb4Val
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIb4Val
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportEDIb4Val_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIb4Val_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportEDIb4Val(requestBody:ImportEDIb4Val_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportEDIb4Val_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ImportEDIb4Val", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportEDIb4Val_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportEDIPreProcessDemand
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIPreProcessDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportEDIPreProcessDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIPreProcessDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportEDIPreProcessDemand(requestBody:ImportEDIPreProcessDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportEDIPreProcessDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ImportEDIPreProcessDemand", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportEDIPreProcessDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportEDIPostProcessDemand
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIPostProcessDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportEDIPostProcessDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIPostProcessDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportEDIPostProcessDemand(requestBody:ImportEDIPostProcessDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportEDIPostProcessDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ImportEDIPostProcessDemand", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportEDIPostProcessDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportEDIOnUDImport
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIOnUDImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportEDIOnUDImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIOnUDImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportEDIOnUDImport(requestBody:ImportEDIOnUDImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportEDIOnUDImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ImportEDIOnUDImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportEDIOnUDImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOTSTaxID
   Description: OTS Tax Id validation
   OperationID: ValidateOTSTaxID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOTSTaxID(requestBody:ValidateOTSTaxID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateOTSTaxID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/ValidateOTSTaxID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateOTSTaxID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportGrp(requestBody:GetNewImportGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewImportGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDemandHeadImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandHeadImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDemandHeadImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandHeadImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandHeadImport(requestBody:GetNewDemandHeadImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDemandHeadImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewDemandHeadImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDemandHeadImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPkgControlLabelValueImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlLabelValueImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlLabelValueImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlLabelValueImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPkgControlLabelValueImport(requestBody:GetNewPkgControlLabelValueImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPkgControlLabelValueImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewPkgControlLabelValueImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPkgControlLabelValueImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDemandDetailImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandDetailImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDemandDetailImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandDetailImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandDetailImport(requestBody:GetNewDemandDetailImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDemandDetailImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewDemandDetailImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDemandDetailImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDemandMiscChgImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChgImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChgImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChgImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandMiscChgImport(requestBody:GetNewDemandMiscChgImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDemandMiscChgImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewDemandMiscChgImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDemandMiscChgImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDemandScheduleImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandScheduleImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDemandScheduleImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandScheduleImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandScheduleImport(requestBody:GetNewDemandScheduleImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDemandScheduleImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewDemandScheduleImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDemandScheduleImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDemandMiscChgImportDH
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChgImportDH
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChgImportDH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChgImportDH_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDemandMiscChgImportDH(requestBody:GetNewDemandMiscChgImportDH_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDemandMiscChgImportDH_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetNewDemandMiscChgImportDH", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewDemandMiscChgImportDH_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandDetailImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandHeadImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportDHRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandMiscChgImportDHRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandMiscChgImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DemandScheduleImportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ImportGrpListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ImportGrpRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PkgControlLabelValueImportRow,
}

export interface Erp_Tablesets_DemandDetailImportRow{
      /**  Company  */  
   "Company":string,
      /**  DemandContractNum  */  
   "DemandContractNum":number,
      /**  DemandHeadSeq  */  
   "DemandHeadSeq":number,
      /**  DemandDtlSeq  */  
   "DemandDtlSeq":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  DemandContractLine  */  
   "DemandContractLine":number,
      /**  TestRecord  */  
   "TestRecord":boolean,
      /**  OrderNum  */  
   "OrderNum":number,
      /**  OrderLine  */  
   "OrderLine":number,
      /**  DoNotShipBeforeDate  */  
   "DoNotShipBeforeDate":string,
      /**  DoNotShipAfterDate  */  
   "DoNotShipAfterDate":string,
      /**  DemandReference  */  
   "DemandReference":string,
      /**  LineDesc  */  
   "LineDesc":string,
      /**  IUM  */  
   "IUM":string,
      /**  SalesUM  */  
   "SalesUM":string,
      /**  DiscountPercent  */  
   "DiscountPercent":number,
      /**  UnitPrice  */  
   "UnitPrice":number,
      /**  PricePerCode  */  
   "PricePerCode":string,
      /**  ProjectID  */  
   "ProjectID":string,
      /**  PriceGroupCode  */  
   "PriceGroupCode":string,
      /**  QuoteNum  */  
   "QuoteNum":number,
      /**  QuoteLine  */  
   "QuoteLine":number,
      /**  POType  */  
   "POType":string,
      /**  AcknowledgementType  */  
   "AcknowledgementType":string,
      /**  ScheduleType  */  
   "ScheduleType":string,
      /**  SellingFactor  */  
   "SellingFactor":number,
      /**  SellingFactorDirection  */  
   "SellingFactorDirection":string,
      /**  CustNum  */  
   "CustNum":number,
      /**  PONum  */  
   "PONum":string,
      /**  RejectedByUser  */  
   "RejectedByUser":boolean,
      /**  PartNum  */  
   "PartNum":string,
      /**  XPartNum  */  
   "XPartNum":string,
      /**  UsePriceList  */  
   "UsePriceList":boolean,
      /**  Posted  */  
   "Posted":boolean,
      /**  RejectedBySystem  */  
   "RejectedBySystem":boolean,
      /**  OverrideSystemReject  */  
   "OverrideSystemReject":boolean,
      /**  Plant  */  
   "Plant":string,
      /**  OpenLine  */  
   "OpenLine":boolean,
      /**  POLine  */  
   "POLine":string,
      /**  DemandCharacter01  */  
   "DemandCharacter01":string,
      /**  DemandCharacter02  */  
   "DemandCharacter02":string,
      /**  DemandCharacter03  */  
   "DemandCharacter03":string,
      /**  DemandCharacter04  */  
   "DemandCharacter04":string,
      /**  DemandNumber01  */  
   "DemandNumber01":number,
      /**  DemandNumber02  */  
   "DemandNumber02":number,
      /**  DemandNumber03  */  
   "DemandNumber03":number,
      /**  DemandNumber04  */  
   "DemandNumber04":number,
      /**  DemandDate01  */  
   "DemandDate01":string,
      /**  DemandDate02  */  
   "DemandDate02":string,
      /**  DemandDate03  */  
   "DemandDate03":string,
      /**  DemandDate04  */  
   "DemandDate04":string,
      /**  DemandLogical01  */  
   "DemandLogical01":boolean,
      /**  DemandLogical02  */  
   "DemandLogical02":boolean,
      /**  DemandLogical03  */  
   "DemandLogical03":boolean,
      /**  DemandLogical04  */  
   "DemandLogical04":boolean,
      /**  DeleteCurrentReleases  */  
   "DeleteCurrentReleases":boolean,
      /**  MktgCampaignID  */  
   "MktgCampaignID":string,
      /**  MktgEvntSeq  */  
   "MktgEvntSeq":number,
      /**  XRefPartNum  */  
   "XRefPartNum":string,
      /**  XRefPartType  */  
   "XRefPartType":string,
      /**  XRefCustNum  */  
   "XRefCustNum":number,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  XRevisionNum  */  
   "XRevisionNum":string,
      /**  EDIUnitPrice  */  
   "EDIUnitPrice":number,
      /**  CumulativeQty  */  
   "CumulativeQty":number,
      /**  CumulativeDate  */  
   "CumulativeDate":string,
      /**  StartCumQty  */  
   "StartCumQty":number,
      /**  StartCumDate  */  
   "StartCumDate":string,
      /**  LastShipmentID  */  
   "LastShipmentID":number,
      /**  LastShipmentQty  */  
   "LastShipmentQty":number,
      /**  LastShipmentDate  */  
   "LastShipmentDate":string,
      /**  ScheduleNumber  */  
   "ScheduleNumber":string,
      /**  LastMasterPack  */  
   "LastMasterPack":number,
      /**  DocUnitPrice  */  
   "DocUnitPrice":number,
      /**  DocEDIUnitPrice  */  
   "DocEDIUnitPrice":number,
      /**  InternalPrice  */  
   "InternalPrice":number,
      /**  DocInternalPrice  */  
   "DocInternalPrice":number,
      /**  SmartStringProcessed  */  
   "SmartStringProcessed":boolean,
      /**  SmartString  */  
   "SmartString":string,
      /**  BasePartNum  */  
   "BasePartNum":string,
      /**  LastConfigDate  */  
   "LastConfigDate":string,
      /**  LastConfigTime  */  
   "LastConfigTime":number,
      /**  LastConfigUserID  */  
   "LastConfigUserID":string,
      /**  ConfigUnitPrice  */  
   "ConfigUnitPrice":number,
      /**  ConfigBaseUnitPrice  */  
   "ConfigBaseUnitPrice":number,
      /**  BaseRevisionNum  */  
   "BaseRevisionNum":string,
      /**  TPQuoteNum  */  
   "TPQuoteNum":number,
      /**  TPQuoteLine  */  
   "TPQuoteLine":number,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Rpt1UnitPrice  */  
   "Rpt1UnitPrice":number,
      /**  Rpt2UnitPrice  */  
   "Rpt2UnitPrice":number,
      /**  Rpt3UnitPrice  */  
   "Rpt3UnitPrice":number,
      /**  Rpt1InternalPrice  */  
   "Rpt1InternalPrice":number,
      /**  Rpt2InternalPrice  */  
   "Rpt2InternalPrice":number,
      /**  Rpt3InternalPrice  */  
   "Rpt3InternalPrice":number,
      /**  Rpt1EDIUnitPrice  */  
   "Rpt1EDIUnitPrice":number,
      /**  Rpt2EDIUnitPrice  */  
   "Rpt2EDIUnitPrice":number,
      /**  Rpt3EDIUnitPrice  */  
   "Rpt3EDIUnitPrice":number,
      /**  ErrorList  */  
   "ErrorList":string,
      /**  EDICustom01  */  
   "EDICustom01":string,
      /**  EDICustom02  */  
   "EDICustom02":string,
      /**  EDICustom03  */  
   "EDICustom03":string,
      /**  EDICustom04  */  
   "EDICustom04":string,
      /**  EDICustom05  */  
   "EDICustom05":string,
      /**  EDICustom06  */  
   "EDICustom06":string,
      /**  EDICustom07  */  
   "EDICustom07":string,
      /**  EDICustom08  */  
   "EDICustom08":string,
      /**  EDICustom09  */  
   "EDICustom09":string,
      /**  EDICustom10  */  
   "EDICustom10":string,
      /**  BlockProcLine  */  
   "BlockProcLine":boolean,
      /**  POLineRef  */  
   "POLineRef":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
   "Configured":string,
   "DmdContractNum":number,
   "MultipleXRef":boolean,
   "PriceDiscrepancy":boolean,
   "BitFlag":number,
   "DemandContractDtlSalesUM":string,
   "MktgCampaignIDCampDescription":string,
   "MktgEvntEvntDescription":string,
   "PlantName":string,
   "PriceGroupDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandHeadImportRow{
      /**  Company  */  
   "Company":string,
      /**  DemandContractNum  */  
   "DemandContractNum":number,
      /**  DemandHeadSeq  */  
   "DemandHeadSeq":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  OrderNum  */  
   "OrderNum":number,
      /**  CustNum  */  
   "CustNum":number,
      /**  PONum  */  
   "PONum":string,
      /**  DoNotShipBeforeDate  */  
   "DoNotShipBeforeDate":string,
      /**  DoNotShipAfterDate  */  
   "DoNotShipAfterDate":string,
      /**  CancelAfterDate  */  
   "CancelAfterDate":string,
      /**  FOB  */  
   "FOB":string,
      /**  ShipViaCode  */  
   "ShipViaCode":string,
      /**  TermsCode  */  
   "TermsCode":string,
      /**  AllocPriorityCode  */  
   "AllocPriorityCode":string,
      /**  ReservePriorityCode  */  
   "ReservePriorityCode":string,
      /**  ShipOrderComplete  */  
   "ShipOrderComplete":boolean,
      /**  OrderComment  */  
   "OrderComment":string,
      /**  InvoiceComment  */  
   "InvoiceComment":string,
      /**  AutoOrderBasedDisc  */  
   "AutoOrderBasedDisc":boolean,
      /**  TestRecord  */  
   "TestRecord":boolean,
      /**  POType  */  
   "POType":string,
      /**  AcknowledgementType  */  
   "AcknowledgementType":string,
      /**  AcceptType  */  
   "AcceptType":string,
      /**  ScheduleNumber  */  
   "ScheduleNumber":string,
      /**  ScheduleNumberSeq  */  
   "ScheduleNumberSeq":number,
      /**  CurrencyCode  */  
   "CurrencyCode":string,
      /**  LockRate  */  
   "LockRate":boolean,
      /**  Accepted  */  
   "Accepted":boolean,
      /**  RejectedByUser  */  
   "RejectedByUser":boolean,
      /**  OpenDemand  */  
   "OpenDemand":boolean,
      /**  Posted  */  
   "Posted":boolean,
      /**  RejectedBySystem  */  
   "RejectedBySystem":boolean,
      /**  OverrideSystemReject  */  
   "OverrideSystemReject":boolean,
      /**  DemandCharacter01  */  
   "DemandCharacter01":string,
      /**  DemandCharacter02  */  
   "DemandCharacter02":string,
      /**  DemandCharacter03  */  
   "DemandCharacter03":string,
      /**  DemandCharacter04  */  
   "DemandCharacter04":string,
      /**  DemandNumber01  */  
   "DemandNumber01":number,
      /**  DemandNumber02  */  
   "DemandNumber02":number,
      /**  DemandNumber03  */  
   "DemandNumber03":number,
      /**  DemandNumber04  */  
   "DemandNumber04":number,
      /**  DemandDate01  */  
   "DemandDate01":string,
      /**  DemandDate02  */  
   "DemandDate02":string,
      /**  DemandDate03  */  
   "DemandDate03":string,
      /**  DemandDate04  */  
   "DemandDate04":string,
      /**  DemandLogical01  */  
   "DemandLogical01":boolean,
      /**  DemandLogical02  */  
   "DemandLogical02":boolean,
      /**  DemandLogical03  */  
   "DemandLogical03":boolean,
      /**  DemandLogical04  */  
   "DemandLogical04":boolean,
      /**  BTCustNum  */  
   "BTCustNum":number,
      /**  EDIOrder  */  
   "EDIOrder":boolean,
      /**  SelectedForProcessing  */  
   "SelectedForProcessing":boolean,
      /**  SCProcessing  */  
   "SCProcessing":boolean,
      /**  ShipToNum  */  
   "ShipToNum":string,
      /**  ReadyToProcess  */  
   "ReadyToProcess":boolean,
      /**  ResetCums  */  
   "ResetCums":boolean,
      /**  ERSOrder  */  
   "ERSOrder":boolean,
      /**  CancelPO  */  
   "CancelPO":boolean,
      /**  CreateNewOrder  */  
   "CreateNewOrder":boolean,
      /**  LinkedOrders  */  
   "LinkedOrders":string,
      /**  TCtrlNum  */  
   "TCtrlNum":string,
      /**  BatchNum  */  
   "BatchNum":string,
      /**  QuoteNum  */  
   "QuoteNum":number,
      /**  DemandProcessDate  */  
   "DemandProcessDate":string,
      /**  DemandProcessTime  */  
   "DemandProcessTime":number,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
      /**  CustomerTradingPartnerName  */  
   "CustomerTradingPartnerName":string,
      /**  TranType  */  
   "TranType":string,
      /**  DemandContract  */  
   "DemandContract":string,
      /**  CustomerCustID  */  
   "CustomerCustID":string,
      /**  BTCustomerCustID  */  
   "BTCustomerCustID":string,
      /**  ShipToCustID  */  
   "ShipToCustID":string,
      /**  UseOTS  */  
   "UseOTS":boolean,
      /**  OTSName  */  
   "OTSName":string,
      /**  OTSAddress1  */  
   "OTSAddress1":string,
      /**  OTSAddress2  */  
   "OTSAddress2":string,
      /**  OTSAddress3  */  
   "OTSAddress3":string,
      /**  OTSCity  */  
   "OTSCity":string,
      /**  OTSResaleID  */  
   "OTSResaleID":string,
      /**  OTSState  */  
   "OTSState":string,
      /**  OTSZIP  */  
   "OTSZIP":string,
      /**  EDIOTSCountry  */  
   "EDIOTSCountry":string,
      /**  OTSFaxNum  */  
   "OTSFaxNum":string,
      /**  OTSPhoneNum  */  
   "OTSPhoneNum":string,
      /**  OTSContact  */  
   "OTSContact":string,
      /**  OTSSaveCustID  */  
   "OTSSaveCustID":string,
      /**  OTSSaveAs  */  
   "OTSSaveAs":string,
      /**  ErrorList  */  
   "ErrorList":string,
      /**  EDICustom01  */  
   "EDICustom01":string,
      /**  EDICustom02  */  
   "EDICustom02":string,
      /**  EDICustom03  */  
   "EDICustom03":string,
      /**  EDICustom04  */  
   "EDICustom04":string,
      /**  EDICustom05  */  
   "EDICustom05":string,
      /**  EDICustom06  */  
   "EDICustom06":string,
      /**  EDICustom07  */  
   "EDICustom07":string,
      /**  EDICustom08  */  
   "EDICustom08":string,
      /**  EDICustom09  */  
   "EDICustom09":string,
      /**  EDICustom10  */  
   "EDICustom10":string,
      /**  ShipByTime  */  
   "ShipByTime":number,
      /**  OTSCountryNum  */  
   "OTSCountryNum":number,
      /**  OTSTaxRegionCode  */  
   "OTSTaxRegionCode":string,
      /**  OTSCustSaved  */  
   "OTSCustSaved":boolean,
      /**  OTSSaved  */  
   "OTSSaved":boolean,
      /**  OTSShipToNum  */  
   "OTSShipToNum":string,
      /**  ShipToCustNum  */  
   "ShipToCustNum":number,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
   "AvailBTCustList":string,
   "EDI_OTSCountry":string,
   "ERSOverride":boolean,
   "OpenContract":boolean,
   "OTSCountryDescription":string,
   "ShipToAddressList":string,
      /**  Tran_Type  */  
   "Tran_Type":string,
   "CustAddrList":string,
   "DmdContractNum":number,
   "DocumentName":string,
   "CustAddrFormatted":string,
   "ShipToAddressFormatted":string,
   "BitFlag":number,
   "BTCustomerBTName":string,
   "BTCustomerCustID_":string,
   "BTCustomerName":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrDesc":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerZip":string,
   "CustomerState":string,
   "CustomerCountry":string,
   "CustomerCity":string,
   "CustomerTradingPartnerName_":string,
   "CustomerAddress1":string,
   "CustomerAddress2":string,
   "CustomerAddress3":string,
   "CustomerAllowShipTo3":boolean,
   "CustomerAllowOTS":boolean,
   "FOBDescription":string,
   "OTSCountryEUMember":boolean,
   "OTSCountryISOCode":string,
   "ReservePriDescription":string,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "TermsDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandMiscChgImportDHRow{
      /**  Company  */  
   "Company":string,
      /**  DemandContractNum  */  
   "DemandContractNum":number,
      /**  DemandHeadSeq  */  
   "DemandHeadSeq":number,
      /**  DemandDtlSeq  */  
   "DemandDtlSeq":number,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  MiscCode  */  
   "MiscCode":string,
      /**  Description  */  
   "Description":string,
      /**  MiscAmt  */  
   "MiscAmt":number,
      /**  DocMiscAmt  */  
   "DocMiscAmt":number,
      /**  FreqCode  */  
   "FreqCode":string,
      /**  Quoting  */  
   "Quoting":string,
      /**  Rpt1MiscAmt  */  
   "Rpt1MiscAmt":number,
      /**  Rpt2MiscAmt  */  
   "Rpt2MiscAmt":number,
      /**  Rpt3MiscAmt  */  
   "Rpt3MiscAmt":number,
      /**  Percentage  */  
   "Percentage":number,
      /**  Type  */  
   "Type":string,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorList  */  
   "ErrorList":string,
   "CurrencyCode":string,
   "BitFlag":number,
   "MiscCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandMiscChgImportRow{
      /**  Company  */  
   "Company":string,
      /**  DemandContractNum  */  
   "DemandContractNum":number,
      /**  DemandHeadSeq  */  
   "DemandHeadSeq":number,
      /**  DemandDtlSeq  */  
   "DemandDtlSeq":number,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  MiscCode  */  
   "MiscCode":string,
      /**  Description  */  
   "Description":string,
      /**  MiscAmt  */  
   "MiscAmt":number,
      /**  DocMiscAmt  */  
   "DocMiscAmt":number,
      /**  FreqCode  */  
   "FreqCode":string,
      /**  Quoting  */  
   "Quoting":string,
      /**  Rpt1MiscAmt  */  
   "Rpt1MiscAmt":number,
      /**  Rpt2MiscAmt  */  
   "Rpt2MiscAmt":number,
      /**  Rpt3MiscAmt  */  
   "Rpt3MiscAmt":number,
      /**  Percentage  */  
   "Percentage":number,
      /**  Type  */  
   "Type":string,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorList  */  
   "ErrorList":string,
   "CurrencyCode":string,
   "BitFlag":number,
   "MiscCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DemandScheduleImportRow{
      /**  Company  */  
   "Company":string,
      /**  DemandContractNum  */  
   "DemandContractNum":number,
      /**  DemandHeadSeq  */  
   "DemandHeadSeq":number,
      /**  DemandDtlSeq  */  
   "DemandDtlSeq":number,
      /**  DemandScheduleSeq  */  
   "DemandScheduleSeq":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  GroupID  */  
   "GroupID":string,
      /**  OurReqQty  */  
   "OurReqQty":number,
      /**  ShipToNum  */  
   "ShipToNum":string,
      /**  ShipViaCode  */  
   "ShipViaCode":string,
      /**  SellingReqQty  */  
   "SellingReqQty":number,
      /**  ReqDate  */  
   "ReqDate":string,
      /**  NeedByDate  */  
   "NeedByDate":string,
      /**  MarkForNum  */  
   "MarkForNum":string,
      /**  DeliveryDays  */  
   "DeliveryDays":number,
      /**  ScheduleNumber  */  
   "ScheduleNumber":string,
      /**  DemandType  */  
   "DemandType":string,
      /**  OrderNum  */  
   "OrderNum":number,
      /**  OrderLine  */  
   "OrderLine":number,
      /**  OrderRelNum  */  
   "OrderRelNum":number,
      /**  RejectedByUser  */  
   "RejectedByUser":boolean,
      /**  RAN  */  
   "RAN":string,
      /**  DemandReference  */  
   "DemandReference":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  RejectedBySystem  */  
   "RejectedBySystem":boolean,
      /**  OverrideSystemReject  */  
   "OverrideSystemReject":boolean,
      /**  Plant  */  
   "Plant":string,
      /**  OpenSchedule  */  
   "OpenSchedule":boolean,
      /**  DemandCharacter01  */  
   "DemandCharacter01":string,
      /**  DemandCharacter02  */  
   "DemandCharacter02":string,
      /**  DemandCharacter03  */  
   "DemandCharacter03":string,
      /**  DemandCharacter04  */  
   "DemandCharacter04":string,
      /**  DemandNumber01  */  
   "DemandNumber01":number,
      /**  DemandNumber02  */  
   "DemandNumber02":number,
      /**  DemandNumber03  */  
   "DemandNumber03":number,
      /**  DemandNumber04  */  
   "DemandNumber04":number,
      /**  DemandDate01  */  
   "DemandDate01":string,
      /**  DemandDate02  */  
   "DemandDate02":string,
      /**  DemandDate03  */  
   "DemandDate03":string,
      /**  DemandDate04  */  
   "DemandDate04":string,
      /**  DemandLogical01  */  
   "DemandLogical01":boolean,
      /**  DemandLogical02  */  
   "DemandLogical02":boolean,
      /**  DemandLogical03  */  
   "DemandLogical03":boolean,
      /**  DemandLogical04  */  
   "DemandLogical04":boolean,
      /**  DocumentName  */  
   "DocumentName":string,
      /**  ForecastEndDate  */  
   "ForecastEndDate":string,
      /**  DockingStation  */  
   "DockingStation":string,
      /**  Location  */  
   "Location":string,
      /**  TransportID  */  
   "TransportID":string,
      /**  ShipbyTime  */  
   "ShipbyTime":number,
      /**  UseOTS  */  
   "UseOTS":boolean,
      /**  OTSName  */  
   "OTSName":string,
      /**  OTSAddress1  */  
   "OTSAddress1":string,
      /**  OTSAddress2  */  
   "OTSAddress2":string,
      /**  OTSAddress3  */  
   "OTSAddress3":string,
      /**  OTSCity  */  
   "OTSCity":string,
      /**  OTSState  */  
   "OTSState":string,
      /**  OTSZIP  */  
   "OTSZIP":string,
      /**  OTSResaleID  */  
   "OTSResaleID":string,
      /**  OTSContact  */  
   "OTSContact":string,
      /**  OTSFaxNum  */  
   "OTSFaxNum":string,
      /**  OTSPhoneNum  */  
   "OTSPhoneNum":string,
      /**  OTSCountryNum  */  
   "OTSCountryNum":number,
      /**  SubShipTo  */  
   "SubShipTo":string,
      /**  ShipRouting  */  
   "ShipRouting":string,
      /**  ShipToCustNum  */  
   "ShipToCustNum":number,
      /**  OTSTaxRegionCode  */  
   "OTSTaxRegionCode":string,
      /**  CreateDate  */  
   "CreateDate":string,
      /**  ProcessDate  */  
   "ProcessDate":string,
      /**  ProcessTime  */  
   "ProcessTime":number,
      /**  MFCustNum  */  
   "MFCustNum":number,
      /**  UseOTMF  */  
   "UseOTMF":boolean,
      /**  OTMFName  */  
   "OTMFName":string,
      /**  OTMFAddress1  */  
   "OTMFAddress1":string,
      /**  OTMFAddress2  */  
   "OTMFAddress2":string,
      /**  OTMFAddress3  */  
   "OTMFAddress3":string,
      /**  OTMFCity  */  
   "OTMFCity":string,
      /**  OTMFState  */  
   "OTMFState":string,
      /**  OTMFZIP  */  
   "OTMFZIP":string,
      /**  OTMFContact  */  
   "OTMFContact":string,
      /**  OTMFFaxNum  */  
   "OTMFFaxNum":string,
      /**  OTMFPhoneNum  */  
   "OTMFPhoneNum":string,
      /**  OTMFCountryNum  */  
   "OTMFCountryNum":number,
      /**  QuoteNum  */  
   "QuoteNum":number,
      /**  QuoteLine  */  
   "QuoteLine":number,
      /**  QuoteRelNum  */  
   "QuoteRelNum":number,
      /**  CTPNeedByDate  */  
   "CTPNeedByDate":string,
      /**  CTPShipDate  */  
   "CTPShipDate":string,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SalesUM  */  
   "SalesUM":string,
      /**  ShipToCustomerCustID  */  
   "ShipToCustomerCustID":string,
      /**  MFCustomerCustID  */  
   "MFCustomerCustID":string,
      /**  OTSCountryDescription  */  
   "OTSCountryDescription":string,
      /**  OTSSaveCustID  */  
   "OTSSaveCustID":string,
      /**  OTSSaveAs  */  
   "OTSSaveAs":string,
      /**  OTMFCountryDescription  */  
   "OTMFCountryDescription":string,
      /**  IUM  */  
   "IUM":string,
      /**  ErrorList  */  
   "ErrorList":string,
      /**  EDICustom01  */  
   "EDICustom01":string,
      /**  EDICustom02  */  
   "EDICustom02":string,
      /**  EDICustom03  */  
   "EDICustom03":string,
      /**  EDICustom04  */  
   "EDICustom04":string,
      /**  EDICustom05  */  
   "EDICustom05":string,
      /**  EDICustom06  */  
   "EDICustom06":string,
      /**  EDICustom07  */  
   "EDICustom07":string,
      /**  EDICustom08  */  
   "EDICustom08":string,
      /**  EDICustom09  */  
   "EDICustom09":string,
      /**  EDICustom10  */  
   "EDICustom10":string,
      /**  OTSCustSaved  */  
   "OTSCustSaved":boolean,
      /**  OTSSaved  */  
   "OTSSaved":boolean,
      /**  OTSShipToNum  */  
   "OTSShipToNum":string,
      /**  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  */  
   "CTPManualConfirm":boolean,
      /**  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  */  
   "CTPSource":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
   "DmdContractNum":number,
   "MarkForAddrList":string,
   "ShipToAddrList":string,
   "MarkForAddrFormatted":string,
   "ShipToAddrFormatted":string,
   "BitFlag":number,
   "MFCustomerBTName":string,
   "MFCustomerCustID_":string,
   "MFCustomerName":string,
   "OTMFCountryDescription_":string,
   "OTSCountryEUMember":boolean,
   "OTSCountryDescription_":string,
   "OTSCountryISOCode":string,
   "OTSTaxRegionCodeDescription":string,
   "ShipToCustomerName":string,
   "ShipToCustomerCustID_":string,
   "ShipToCustomerBTName":string,
   "ShipViaWebDesc":string,
   "ShipViaDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ImportGrpListRow{
      /**  Company  */  
   "Company":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  ImportType  */  
   "ImportType":string,
      /**  ErrorFlag  */  
   "ErrorFlag":boolean,
      /**  Status  */  
   "Status":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DisplayImportID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ImportGrpRow{
      /**  Company  */  
   "Company":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  ImportType  */  
   "ImportType":string,
      /**  ErrorFlag  */  
   "ErrorFlag":boolean,
      /**  Status  */  
   "Status":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "IntError":boolean,
   "DisplayImportID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PkgControlLabelValueImportRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The CustID associated with this Ship To.  */  
   "ShipToCustID":string,
      /**  The Ship To number.  */  
   "ShipToNum":string,
      /**  The PartNum field identifies the Part.  */  
   "PartNum":string,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   "DemandHeadSeq":number,
      /**  The Import ID.  */  
   "ImportID":number,
      /**  Value to display on package control label.  */  
   "LabelValue01":string,
      /**  Value to display on package control label.  */  
   "LabelValue02":string,
      /**  Value to display on package control label.  */  
   "LabelValue03":string,
      /**  Value to display on package control label.  */  
   "LabelValue04":string,
      /**  Value to display on package control label.  */  
   "LabelValue05":string,
      /**  Value to display on package control label.  */  
   "LabelValue06":string,
      /**  Value to display on package control label.  */  
   "LabelValue07":string,
      /**  Value to display on package control label.  */  
   "LabelValue08":string,
      /**  Value to display on package control label.  */  
   "LabelValue09":string,
      /**  Value to display on package control label.  */  
   "LabelValue10":string,
      /**  Value to display on package control label.  */  
   "LabelValue11":string,
      /**  Value to display on package control label.  */  
   "LabelValue12":string,
      /**  Value to display on package control label.  */  
   "LabelValue13":string,
      /**  Value to display on package control label.  */  
   "LabelValue14":string,
      /**  Value to display on package control label.  */  
   "LabelValue15":string,
      /**  Value to display on package control label.  */  
   "LabelValue16":string,
      /**  Value to display on package control label.  */  
   "LabelValue17":string,
      /**  Value to display on package control label.  */  
   "LabelValue18":string,
      /**  Value to display on package control label.  */  
   "LabelValue19":string,
      /**  Value to display on package control label.  */  
   "LabelValue20":string,
      /**  Value to display on package control label.  */  
   "LabelValue21":string,
      /**  Value to display on package control label.  */  
   "LabelValue22":string,
      /**  Value to display on package control label.  */  
   "LabelValue23":string,
      /**  Value to display on package control label.  */  
   "LabelValue24":string,
      /**  Value to display on package control label.  */  
   "LabelValue25":string,
      /**  Value to display on package control label.  */  
   "LabelValue26":string,
      /**  Value to display on package control label.  */  
   "LabelValue27":string,
      /**  Value to display on package control label.  */  
   "LabelValue28":string,
      /**  Value to display on package control label.  */  
   "LabelValue29":string,
      /**  Value to display on package control label.  */  
   "LabelValue30":string,
      /**  Date that record was created.  */  
   "CreatedDate":string,
      /**  The user ID for the user who created this record.  */  
   "CreatedBy":string,
      /**  Date that record was last updated.  */  
   "UpdatedDate":string,
      /**  The user ID for the user who last updated this record.  */  
   "UpdatedBy":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
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
      @param proposedDemandContractLine
      @param ds
   */  
export interface ChangeDemandDetailDemandContractLine_input{
      /**  The proposed Demand Contract Line  */  
   proposedDemandContractLine:number,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandDetailDemandContractLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param iMktgCampaignID
      @param ds
   */  
export interface ChangeDemandDetailMktgCamp_input{
      /**  The Marketing Campaign ID  */  
   iMktgCampaignID:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandDetailMktgCamp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param iPartNum
      @param ds
      @param sysRowID
      @param rowType
   */  
export interface ChangeDemandDetailPartNum_input{
      /**  The part  */  
   iPartNum:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface ChangeDemandDetailPartNum_output{
parameters : {
      /**  output parameters  */  
   iPartNum:string,
   ds:Erp_Tablesets_DemandImportEntryTableset,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandDetailRevisionNum_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandDetailRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ipCustID
      @param ds
   */  
export interface ChangeDemandHeadCustID_input{
      /**  The proposed Customer ID  */  
   ipCustID:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandHeadCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedDemandContract
      @param ds
   */  
export interface ChangeDemandHeadDemandContract_input{
      /**  The proposed Demand Contract  */  
   proposedDemandContract:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandHeadDemandContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedERSOrder
      @param ds
   */  
export interface ChangeDemandHeadERSOrder_input{
      /**  The proposed ERS Order  */  
   proposedERSOrder:boolean,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandHeadERSOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ipShipToCustID
      @param ds
   */  
export interface ChangeDemandHeadShipToCustID_input{
      /**  The proposed ShipTo Customer ID  */  
   ipShipToCustID:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandHeadShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedShipToNum
      @param ds
   */  
export interface ChangeDemandHeadShipToNum_input{
      /**  The proposed Ship To Num  */  
   proposedShipToNum:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandHeadShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandHeadUseOTS_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandHeadUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ipMFCustID
      @param ds
   */  
export interface ChangeDemandScheduleMFCustID_input{
      /**  The proposed Mark For Customer ID  */  
   ipMFCustID:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleMFCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedMarkForNum
      @param ds
   */  
export interface ChangeDemandScheduleMarkForNum_input{
      /**  The Proposed ShipToNum  */  
   proposedMarkForNum:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleMarkForNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandScheduleOTSDetails_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleOTSDetails_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedPlant
      @param ds
   */  
export interface ChangeDemandSchedulePlant_input{
      /**  The Proposed Plant  */  
   proposedPlant:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandSchedulePlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedSellingReqQty
      @param ds
   */  
export interface ChangeDemandScheduleSellingReqQty_input{
      /**  The proposed Selling Req Quantity  */  
   proposedSellingReqQty:number,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleSellingReqQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ipShipToCustID
      @param ds
   */  
export interface ChangeDemandScheduleShipToCustID_input{
      /**  The proposed ShipTo Customer ID  */  
   ipShipToCustID:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param proposedShipToNum
      @param ds
   */  
export interface ChangeDemandScheduleShipToNum_input{
      /**  The Proposed ShipToNum  */  
   proposedShipToNum:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleShipToNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandScheduleUseOTMF_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleUseOTMF_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDemandScheduleUseOTS_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeDemandScheduleUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface ChangeMiscCode_input{
      /**  name of table being passed in  */  
   tableName:string,
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ChangeMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param iDemandDtlSeq
      @param cFieldName
      @param cPartNum
   */  
export interface CheckPartRevisionChange_input{
      /**  The current IMDemandDetail.DemandContractNum field  */  
   iDemandContractNum:number,
      /**  The current IMDemandDetail.DemandHeadSeq field  */  
   iDemandHeadSeq:number,
      /**  The current IMDemandDetail.DemandDtlSeq field  */  
   iDemandDtlSeq:number,
      /**  The name of the field you are leaving  */  
   cFieldName:string,
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part  */  
   cPartNum:string,
}

export interface CheckPartRevisionChange_output{
parameters : {
      /**  output parameters  */  
   cPartNum:string,
   cConfigPartMessage:string,
}
}

   /** Required : 
      @param company
      @param importID
   */  
export interface DeleteByID_input{
   company:string,
   importID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DemandDetailImportRow{
      /**  Company  */  
   Company:string,
      /**  DemandContractNum  */  
   DemandContractNum:number,
      /**  DemandHeadSeq  */  
   DemandHeadSeq:number,
      /**  DemandDtlSeq  */  
   DemandDtlSeq:number,
      /**  ImportID  */  
   ImportID:number,
      /**  DemandContractLine  */  
   DemandContractLine:number,
      /**  TestRecord  */  
   TestRecord:boolean,
      /**  OrderNum  */  
   OrderNum:number,
      /**  OrderLine  */  
   OrderLine:number,
      /**  DoNotShipBeforeDate  */  
   DoNotShipBeforeDate:string,
      /**  DoNotShipAfterDate  */  
   DoNotShipAfterDate:string,
      /**  DemandReference  */  
   DemandReference:string,
      /**  LineDesc  */  
   LineDesc:string,
      /**  IUM  */  
   IUM:string,
      /**  SalesUM  */  
   SalesUM:string,
      /**  DiscountPercent  */  
   DiscountPercent:number,
      /**  UnitPrice  */  
   UnitPrice:number,
      /**  PricePerCode  */  
   PricePerCode:string,
      /**  ProjectID  */  
   ProjectID:string,
      /**  PriceGroupCode  */  
   PriceGroupCode:string,
      /**  QuoteNum  */  
   QuoteNum:number,
      /**  QuoteLine  */  
   QuoteLine:number,
      /**  POType  */  
   POType:string,
      /**  AcknowledgementType  */  
   AcknowledgementType:string,
      /**  ScheduleType  */  
   ScheduleType:string,
      /**  SellingFactor  */  
   SellingFactor:number,
      /**  SellingFactorDirection  */  
   SellingFactorDirection:string,
      /**  CustNum  */  
   CustNum:number,
      /**  PONum  */  
   PONum:string,
      /**  RejectedByUser  */  
   RejectedByUser:boolean,
      /**  PartNum  */  
   PartNum:string,
      /**  XPartNum  */  
   XPartNum:string,
      /**  UsePriceList  */  
   UsePriceList:boolean,
      /**  Posted  */  
   Posted:boolean,
      /**  RejectedBySystem  */  
   RejectedBySystem:boolean,
      /**  OverrideSystemReject  */  
   OverrideSystemReject:boolean,
      /**  Plant  */  
   Plant:string,
      /**  OpenLine  */  
   OpenLine:boolean,
      /**  POLine  */  
   POLine:string,
      /**  DemandCharacter01  */  
   DemandCharacter01:string,
      /**  DemandCharacter02  */  
   DemandCharacter02:string,
      /**  DemandCharacter03  */  
   DemandCharacter03:string,
      /**  DemandCharacter04  */  
   DemandCharacter04:string,
      /**  DemandNumber01  */  
   DemandNumber01:number,
      /**  DemandNumber02  */  
   DemandNumber02:number,
      /**  DemandNumber03  */  
   DemandNumber03:number,
      /**  DemandNumber04  */  
   DemandNumber04:number,
      /**  DemandDate01  */  
   DemandDate01:string,
      /**  DemandDate02  */  
   DemandDate02:string,
      /**  DemandDate03  */  
   DemandDate03:string,
      /**  DemandDate04  */  
   DemandDate04:string,
      /**  DemandLogical01  */  
   DemandLogical01:boolean,
      /**  DemandLogical02  */  
   DemandLogical02:boolean,
      /**  DemandLogical03  */  
   DemandLogical03:boolean,
      /**  DemandLogical04  */  
   DemandLogical04:boolean,
      /**  DeleteCurrentReleases  */  
   DeleteCurrentReleases:boolean,
      /**  MktgCampaignID  */  
   MktgCampaignID:string,
      /**  MktgEvntSeq  */  
   MktgEvntSeq:number,
      /**  XRefPartNum  */  
   XRefPartNum:string,
      /**  XRefPartType  */  
   XRefPartType:string,
      /**  XRefCustNum  */  
   XRefCustNum:number,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  XRevisionNum  */  
   XRevisionNum:string,
      /**  EDIUnitPrice  */  
   EDIUnitPrice:number,
      /**  CumulativeQty  */  
   CumulativeQty:number,
      /**  CumulativeDate  */  
   CumulativeDate:string,
      /**  StartCumQty  */  
   StartCumQty:number,
      /**  StartCumDate  */  
   StartCumDate:string,
      /**  LastShipmentID  */  
   LastShipmentID:number,
      /**  LastShipmentQty  */  
   LastShipmentQty:number,
      /**  LastShipmentDate  */  
   LastShipmentDate:string,
      /**  ScheduleNumber  */  
   ScheduleNumber:string,
      /**  LastMasterPack  */  
   LastMasterPack:number,
      /**  DocUnitPrice  */  
   DocUnitPrice:number,
      /**  DocEDIUnitPrice  */  
   DocEDIUnitPrice:number,
      /**  InternalPrice  */  
   InternalPrice:number,
      /**  DocInternalPrice  */  
   DocInternalPrice:number,
      /**  SmartStringProcessed  */  
   SmartStringProcessed:boolean,
      /**  SmartString  */  
   SmartString:string,
      /**  BasePartNum  */  
   BasePartNum:string,
      /**  LastConfigDate  */  
   LastConfigDate:string,
      /**  LastConfigTime  */  
   LastConfigTime:number,
      /**  LastConfigUserID  */  
   LastConfigUserID:string,
      /**  ConfigUnitPrice  */  
   ConfigUnitPrice:number,
      /**  ConfigBaseUnitPrice  */  
   ConfigBaseUnitPrice:number,
      /**  BaseRevisionNum  */  
   BaseRevisionNum:string,
      /**  TPQuoteNum  */  
   TPQuoteNum:number,
      /**  TPQuoteLine  */  
   TPQuoteLine:number,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Rpt1UnitPrice  */  
   Rpt1UnitPrice:number,
      /**  Rpt2UnitPrice  */  
   Rpt2UnitPrice:number,
      /**  Rpt3UnitPrice  */  
   Rpt3UnitPrice:number,
      /**  Rpt1InternalPrice  */  
   Rpt1InternalPrice:number,
      /**  Rpt2InternalPrice  */  
   Rpt2InternalPrice:number,
      /**  Rpt3InternalPrice  */  
   Rpt3InternalPrice:number,
      /**  Rpt1EDIUnitPrice  */  
   Rpt1EDIUnitPrice:number,
      /**  Rpt2EDIUnitPrice  */  
   Rpt2EDIUnitPrice:number,
      /**  Rpt3EDIUnitPrice  */  
   Rpt3EDIUnitPrice:number,
      /**  ErrorList  */  
   ErrorList:string,
      /**  EDICustom01  */  
   EDICustom01:string,
      /**  EDICustom02  */  
   EDICustom02:string,
      /**  EDICustom03  */  
   EDICustom03:string,
      /**  EDICustom04  */  
   EDICustom04:string,
      /**  EDICustom05  */  
   EDICustom05:string,
      /**  EDICustom06  */  
   EDICustom06:string,
      /**  EDICustom07  */  
   EDICustom07:string,
      /**  EDICustom08  */  
   EDICustom08:string,
      /**  EDICustom09  */  
   EDICustom09:string,
      /**  EDICustom10  */  
   EDICustom10:string,
      /**  BlockProcLine  */  
   BlockProcLine:boolean,
      /**  POLineRef  */  
   POLineRef:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
   Configured:string,
   DmdContractNum:number,
   MultipleXRef:boolean,
   PriceDiscrepancy:boolean,
   BitFlag:number,
   DemandContractDtlSalesUM:string,
   MktgCampaignIDCampDescription:string,
   MktgEvntEvntDescription:string,
   PlantName:string,
   PriceGroupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandHeadImportRow{
      /**  Company  */  
   Company:string,
      /**  DemandContractNum  */  
   DemandContractNum:number,
      /**  DemandHeadSeq  */  
   DemandHeadSeq:number,
      /**  ImportID  */  
   ImportID:number,
      /**  OrderNum  */  
   OrderNum:number,
      /**  CustNum  */  
   CustNum:number,
      /**  PONum  */  
   PONum:string,
      /**  DoNotShipBeforeDate  */  
   DoNotShipBeforeDate:string,
      /**  DoNotShipAfterDate  */  
   DoNotShipAfterDate:string,
      /**  CancelAfterDate  */  
   CancelAfterDate:string,
      /**  FOB  */  
   FOB:string,
      /**  ShipViaCode  */  
   ShipViaCode:string,
      /**  TermsCode  */  
   TermsCode:string,
      /**  AllocPriorityCode  */  
   AllocPriorityCode:string,
      /**  ReservePriorityCode  */  
   ReservePriorityCode:string,
      /**  ShipOrderComplete  */  
   ShipOrderComplete:boolean,
      /**  OrderComment  */  
   OrderComment:string,
      /**  InvoiceComment  */  
   InvoiceComment:string,
      /**  AutoOrderBasedDisc  */  
   AutoOrderBasedDisc:boolean,
      /**  TestRecord  */  
   TestRecord:boolean,
      /**  POType  */  
   POType:string,
      /**  AcknowledgementType  */  
   AcknowledgementType:string,
      /**  AcceptType  */  
   AcceptType:string,
      /**  ScheduleNumber  */  
   ScheduleNumber:string,
      /**  ScheduleNumberSeq  */  
   ScheduleNumberSeq:number,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  LockRate  */  
   LockRate:boolean,
      /**  Accepted  */  
   Accepted:boolean,
      /**  RejectedByUser  */  
   RejectedByUser:boolean,
      /**  OpenDemand  */  
   OpenDemand:boolean,
      /**  Posted  */  
   Posted:boolean,
      /**  RejectedBySystem  */  
   RejectedBySystem:boolean,
      /**  OverrideSystemReject  */  
   OverrideSystemReject:boolean,
      /**  DemandCharacter01  */  
   DemandCharacter01:string,
      /**  DemandCharacter02  */  
   DemandCharacter02:string,
      /**  DemandCharacter03  */  
   DemandCharacter03:string,
      /**  DemandCharacter04  */  
   DemandCharacter04:string,
      /**  DemandNumber01  */  
   DemandNumber01:number,
      /**  DemandNumber02  */  
   DemandNumber02:number,
      /**  DemandNumber03  */  
   DemandNumber03:number,
      /**  DemandNumber04  */  
   DemandNumber04:number,
      /**  DemandDate01  */  
   DemandDate01:string,
      /**  DemandDate02  */  
   DemandDate02:string,
      /**  DemandDate03  */  
   DemandDate03:string,
      /**  DemandDate04  */  
   DemandDate04:string,
      /**  DemandLogical01  */  
   DemandLogical01:boolean,
      /**  DemandLogical02  */  
   DemandLogical02:boolean,
      /**  DemandLogical03  */  
   DemandLogical03:boolean,
      /**  DemandLogical04  */  
   DemandLogical04:boolean,
      /**  BTCustNum  */  
   BTCustNum:number,
      /**  EDIOrder  */  
   EDIOrder:boolean,
      /**  SelectedForProcessing  */  
   SelectedForProcessing:boolean,
      /**  SCProcessing  */  
   SCProcessing:boolean,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  ReadyToProcess  */  
   ReadyToProcess:boolean,
      /**  ResetCums  */  
   ResetCums:boolean,
      /**  ERSOrder  */  
   ERSOrder:boolean,
      /**  CancelPO  */  
   CancelPO:boolean,
      /**  CreateNewOrder  */  
   CreateNewOrder:boolean,
      /**  LinkedOrders  */  
   LinkedOrders:string,
      /**  TCtrlNum  */  
   TCtrlNum:string,
      /**  BatchNum  */  
   BatchNum:string,
      /**  QuoteNum  */  
   QuoteNum:number,
      /**  DemandProcessDate  */  
   DemandProcessDate:string,
      /**  DemandProcessTime  */  
   DemandProcessTime:number,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  CustomerTradingPartnerName  */  
   CustomerTradingPartnerName:string,
      /**  TranType  */  
   TranType:string,
      /**  DemandContract  */  
   DemandContract:string,
      /**  CustomerCustID  */  
   CustomerCustID:string,
      /**  BTCustomerCustID  */  
   BTCustomerCustID:string,
      /**  ShipToCustID  */  
   ShipToCustID:string,
      /**  UseOTS  */  
   UseOTS:boolean,
      /**  OTSName  */  
   OTSName:string,
      /**  OTSAddress1  */  
   OTSAddress1:string,
      /**  OTSAddress2  */  
   OTSAddress2:string,
      /**  OTSAddress3  */  
   OTSAddress3:string,
      /**  OTSCity  */  
   OTSCity:string,
      /**  OTSResaleID  */  
   OTSResaleID:string,
      /**  OTSState  */  
   OTSState:string,
      /**  OTSZIP  */  
   OTSZIP:string,
      /**  EDIOTSCountry  */  
   EDIOTSCountry:string,
      /**  OTSFaxNum  */  
   OTSFaxNum:string,
      /**  OTSPhoneNum  */  
   OTSPhoneNum:string,
      /**  OTSContact  */  
   OTSContact:string,
      /**  OTSSaveCustID  */  
   OTSSaveCustID:string,
      /**  OTSSaveAs  */  
   OTSSaveAs:string,
      /**  ErrorList  */  
   ErrorList:string,
      /**  EDICustom01  */  
   EDICustom01:string,
      /**  EDICustom02  */  
   EDICustom02:string,
      /**  EDICustom03  */  
   EDICustom03:string,
      /**  EDICustom04  */  
   EDICustom04:string,
      /**  EDICustom05  */  
   EDICustom05:string,
      /**  EDICustom06  */  
   EDICustom06:string,
      /**  EDICustom07  */  
   EDICustom07:string,
      /**  EDICustom08  */  
   EDICustom08:string,
      /**  EDICustom09  */  
   EDICustom09:string,
      /**  EDICustom10  */  
   EDICustom10:string,
      /**  ShipByTime  */  
   ShipByTime:number,
      /**  OTSCountryNum  */  
   OTSCountryNum:number,
      /**  OTSTaxRegionCode  */  
   OTSTaxRegionCode:string,
      /**  OTSCustSaved  */  
   OTSCustSaved:boolean,
      /**  OTSSaved  */  
   OTSSaved:boolean,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  ShipToCustNum  */  
   ShipToCustNum:number,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   AvailBTCustList:string,
   EDI_OTSCountry:string,
   ERSOverride:boolean,
   OpenContract:boolean,
   OTSCountryDescription:string,
   ShipToAddressList:string,
      /**  Tran_Type  */  
   Tran_Type:string,
   CustAddrList:string,
   DmdContractNum:number,
   DocumentName:string,
   CustAddrFormatted:string,
   ShipToAddressFormatted:string,
   BitFlag:number,
   BTCustomerBTName:string,
   BTCustomerCustID_:string,
   BTCustomerName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrDesc:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerZip:string,
   CustomerState:string,
   CustomerCountry:string,
   CustomerCity:string,
   CustomerTradingPartnerName_:string,
   CustomerAddress1:string,
   CustomerAddress2:string,
   CustomerAddress3:string,
   CustomerAllowShipTo3:boolean,
   CustomerAllowOTS:boolean,
   FOBDescription:string,
   OTSCountryEUMember:boolean,
   OTSCountryISOCode:string,
   ReservePriDescription:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TermsDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandImportEntryTableset{
   ImportGrp:Erp_Tablesets_ImportGrpRow[],
   DemandHeadImport:Erp_Tablesets_DemandHeadImportRow[],
   PkgControlLabelValueImport:Erp_Tablesets_PkgControlLabelValueImportRow[],
   DemandDetailImport:Erp_Tablesets_DemandDetailImportRow[],
   DemandMiscChgImport:Erp_Tablesets_DemandMiscChgImportRow[],
   DemandScheduleImport:Erp_Tablesets_DemandScheduleImportRow[],
   DemandMiscChgImportDH:Erp_Tablesets_DemandMiscChgImportDHRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandMiscChgImportDHRow{
      /**  Company  */  
   Company:string,
      /**  DemandContractNum  */  
   DemandContractNum:number,
      /**  DemandHeadSeq  */  
   DemandHeadSeq:number,
      /**  DemandDtlSeq  */  
   DemandDtlSeq:number,
      /**  SeqNum  */  
   SeqNum:number,
      /**  ImportID  */  
   ImportID:number,
      /**  MiscCode  */  
   MiscCode:string,
      /**  Description  */  
   Description:string,
      /**  MiscAmt  */  
   MiscAmt:number,
      /**  DocMiscAmt  */  
   DocMiscAmt:number,
      /**  FreqCode  */  
   FreqCode:string,
      /**  Quoting  */  
   Quoting:string,
      /**  Rpt1MiscAmt  */  
   Rpt1MiscAmt:number,
      /**  Rpt2MiscAmt  */  
   Rpt2MiscAmt:number,
      /**  Rpt3MiscAmt  */  
   Rpt3MiscAmt:number,
      /**  Percentage  */  
   Percentage:number,
      /**  Type  */  
   Type:string,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorList  */  
   ErrorList:string,
   CurrencyCode:string,
   BitFlag:number,
   MiscCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandMiscChgImportRow{
      /**  Company  */  
   Company:string,
      /**  DemandContractNum  */  
   DemandContractNum:number,
      /**  DemandHeadSeq  */  
   DemandHeadSeq:number,
      /**  DemandDtlSeq  */  
   DemandDtlSeq:number,
      /**  SeqNum  */  
   SeqNum:number,
      /**  ImportID  */  
   ImportID:number,
      /**  MiscCode  */  
   MiscCode:string,
      /**  Description  */  
   Description:string,
      /**  MiscAmt  */  
   MiscAmt:number,
      /**  DocMiscAmt  */  
   DocMiscAmt:number,
      /**  FreqCode  */  
   FreqCode:string,
      /**  Quoting  */  
   Quoting:string,
      /**  Rpt1MiscAmt  */  
   Rpt1MiscAmt:number,
      /**  Rpt2MiscAmt  */  
   Rpt2MiscAmt:number,
      /**  Rpt3MiscAmt  */  
   Rpt3MiscAmt:number,
      /**  Percentage  */  
   Percentage:number,
      /**  Type  */  
   Type:string,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorList  */  
   ErrorList:string,
   CurrencyCode:string,
   BitFlag:number,
   MiscCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandScheduleImportRow{
      /**  Company  */  
   Company:string,
      /**  DemandContractNum  */  
   DemandContractNum:number,
      /**  DemandHeadSeq  */  
   DemandHeadSeq:number,
      /**  DemandDtlSeq  */  
   DemandDtlSeq:number,
      /**  DemandScheduleSeq  */  
   DemandScheduleSeq:number,
      /**  ImportID  */  
   ImportID:number,
      /**  GroupID  */  
   GroupID:string,
      /**  OurReqQty  */  
   OurReqQty:number,
      /**  ShipToNum  */  
   ShipToNum:string,
      /**  ShipViaCode  */  
   ShipViaCode:string,
      /**  SellingReqQty  */  
   SellingReqQty:number,
      /**  ReqDate  */  
   ReqDate:string,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  MarkForNum  */  
   MarkForNum:string,
      /**  DeliveryDays  */  
   DeliveryDays:number,
      /**  ScheduleNumber  */  
   ScheduleNumber:string,
      /**  DemandType  */  
   DemandType:string,
      /**  OrderNum  */  
   OrderNum:number,
      /**  OrderLine  */  
   OrderLine:number,
      /**  OrderRelNum  */  
   OrderRelNum:number,
      /**  RejectedByUser  */  
   RejectedByUser:boolean,
      /**  RAN  */  
   RAN:string,
      /**  DemandReference  */  
   DemandReference:string,
      /**  Posted  */  
   Posted:boolean,
      /**  RejectedBySystem  */  
   RejectedBySystem:boolean,
      /**  OverrideSystemReject  */  
   OverrideSystemReject:boolean,
      /**  Plant  */  
   Plant:string,
      /**  OpenSchedule  */  
   OpenSchedule:boolean,
      /**  DemandCharacter01  */  
   DemandCharacter01:string,
      /**  DemandCharacter02  */  
   DemandCharacter02:string,
      /**  DemandCharacter03  */  
   DemandCharacter03:string,
      /**  DemandCharacter04  */  
   DemandCharacter04:string,
      /**  DemandNumber01  */  
   DemandNumber01:number,
      /**  DemandNumber02  */  
   DemandNumber02:number,
      /**  DemandNumber03  */  
   DemandNumber03:number,
      /**  DemandNumber04  */  
   DemandNumber04:number,
      /**  DemandDate01  */  
   DemandDate01:string,
      /**  DemandDate02  */  
   DemandDate02:string,
      /**  DemandDate03  */  
   DemandDate03:string,
      /**  DemandDate04  */  
   DemandDate04:string,
      /**  DemandLogical01  */  
   DemandLogical01:boolean,
      /**  DemandLogical02  */  
   DemandLogical02:boolean,
      /**  DemandLogical03  */  
   DemandLogical03:boolean,
      /**  DemandLogical04  */  
   DemandLogical04:boolean,
      /**  DocumentName  */  
   DocumentName:string,
      /**  ForecastEndDate  */  
   ForecastEndDate:string,
      /**  DockingStation  */  
   DockingStation:string,
      /**  Location  */  
   Location:string,
      /**  TransportID  */  
   TransportID:string,
      /**  ShipbyTime  */  
   ShipbyTime:number,
      /**  UseOTS  */  
   UseOTS:boolean,
      /**  OTSName  */  
   OTSName:string,
      /**  OTSAddress1  */  
   OTSAddress1:string,
      /**  OTSAddress2  */  
   OTSAddress2:string,
      /**  OTSAddress3  */  
   OTSAddress3:string,
      /**  OTSCity  */  
   OTSCity:string,
      /**  OTSState  */  
   OTSState:string,
      /**  OTSZIP  */  
   OTSZIP:string,
      /**  OTSResaleID  */  
   OTSResaleID:string,
      /**  OTSContact  */  
   OTSContact:string,
      /**  OTSFaxNum  */  
   OTSFaxNum:string,
      /**  OTSPhoneNum  */  
   OTSPhoneNum:string,
      /**  OTSCountryNum  */  
   OTSCountryNum:number,
      /**  SubShipTo  */  
   SubShipTo:string,
      /**  ShipRouting  */  
   ShipRouting:string,
      /**  ShipToCustNum  */  
   ShipToCustNum:number,
      /**  OTSTaxRegionCode  */  
   OTSTaxRegionCode:string,
      /**  CreateDate  */  
   CreateDate:string,
      /**  ProcessDate  */  
   ProcessDate:string,
      /**  ProcessTime  */  
   ProcessTime:number,
      /**  MFCustNum  */  
   MFCustNum:number,
      /**  UseOTMF  */  
   UseOTMF:boolean,
      /**  OTMFName  */  
   OTMFName:string,
      /**  OTMFAddress1  */  
   OTMFAddress1:string,
      /**  OTMFAddress2  */  
   OTMFAddress2:string,
      /**  OTMFAddress3  */  
   OTMFAddress3:string,
      /**  OTMFCity  */  
   OTMFCity:string,
      /**  OTMFState  */  
   OTMFState:string,
      /**  OTMFZIP  */  
   OTMFZIP:string,
      /**  OTMFContact  */  
   OTMFContact:string,
      /**  OTMFFaxNum  */  
   OTMFFaxNum:string,
      /**  OTMFPhoneNum  */  
   OTMFPhoneNum:string,
      /**  OTMFCountryNum  */  
   OTMFCountryNum:number,
      /**  QuoteNum  */  
   QuoteNum:number,
      /**  QuoteLine  */  
   QuoteLine:number,
      /**  QuoteRelNum  */  
   QuoteRelNum:number,
      /**  CTPNeedByDate  */  
   CTPNeedByDate:string,
      /**  CTPShipDate  */  
   CTPShipDate:string,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SalesUM  */  
   SalesUM:string,
      /**  ShipToCustomerCustID  */  
   ShipToCustomerCustID:string,
      /**  MFCustomerCustID  */  
   MFCustomerCustID:string,
      /**  OTSCountryDescription  */  
   OTSCountryDescription:string,
      /**  OTSSaveCustID  */  
   OTSSaveCustID:string,
      /**  OTSSaveAs  */  
   OTSSaveAs:string,
      /**  OTMFCountryDescription  */  
   OTMFCountryDescription:string,
      /**  IUM  */  
   IUM:string,
      /**  ErrorList  */  
   ErrorList:string,
      /**  EDICustom01  */  
   EDICustom01:string,
      /**  EDICustom02  */  
   EDICustom02:string,
      /**  EDICustom03  */  
   EDICustom03:string,
      /**  EDICustom04  */  
   EDICustom04:string,
      /**  EDICustom05  */  
   EDICustom05:string,
      /**  EDICustom06  */  
   EDICustom06:string,
      /**  EDICustom07  */  
   EDICustom07:string,
      /**  EDICustom08  */  
   EDICustom08:string,
      /**  EDICustom09  */  
   EDICustom09:string,
      /**  EDICustom10  */  
   EDICustom10:string,
      /**  OTSCustSaved  */  
   OTSCustSaved:boolean,
      /**  OTSSaved  */  
   OTSSaved:boolean,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  */  
   CTPManualConfirm:boolean,
      /**  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  */  
   CTPSource:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   DmdContractNum:number,
   MarkForAddrList:string,
   ShipToAddrList:string,
   MarkForAddrFormatted:string,
   ShipToAddrFormatted:string,
   BitFlag:number,
   MFCustomerBTName:string,
   MFCustomerCustID_:string,
   MFCustomerName:string,
   OTMFCountryDescription_:string,
   OTSCountryEUMember:boolean,
   OTSCountryDescription_:string,
   OTSCountryISOCode:string,
   OTSTaxRegionCodeDescription:string,
   ShipToCustomerName:string,
   ShipToCustomerCustID_:string,
   ShipToCustomerBTName:string,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportGrpListRow{
      /**  Company  */  
   Company:string,
      /**  ImportID  */  
   ImportID:number,
      /**  ImportType  */  
   ImportType:string,
      /**  ErrorFlag  */  
   ErrorFlag:boolean,
      /**  Status  */  
   Status:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DisplayImportID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportGrpListTableset{
   ImportGrpList:Erp_Tablesets_ImportGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ImportGrpRow{
      /**  Company  */  
   Company:string,
      /**  ImportID  */  
   ImportID:number,
      /**  ImportType  */  
   ImportType:string,
      /**  ErrorFlag  */  
   ErrorFlag:boolean,
      /**  Status  */  
   Status:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   IntError:boolean,
   DisplayImportID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlLabelValueImportRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The CustID associated with this Ship To.  */  
   ShipToCustID:string,
      /**  The Ship To number.  */  
   ShipToNum:string,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  The sequence from the DemandHead record this DemandSchedule is related to.  */  
   DemandHeadSeq:number,
      /**  The Import ID.  */  
   ImportID:number,
      /**  Value to display on package control label.  */  
   LabelValue01:string,
      /**  Value to display on package control label.  */  
   LabelValue02:string,
      /**  Value to display on package control label.  */  
   LabelValue03:string,
      /**  Value to display on package control label.  */  
   LabelValue04:string,
      /**  Value to display on package control label.  */  
   LabelValue05:string,
      /**  Value to display on package control label.  */  
   LabelValue06:string,
      /**  Value to display on package control label.  */  
   LabelValue07:string,
      /**  Value to display on package control label.  */  
   LabelValue08:string,
      /**  Value to display on package control label.  */  
   LabelValue09:string,
      /**  Value to display on package control label.  */  
   LabelValue10:string,
      /**  Value to display on package control label.  */  
   LabelValue11:string,
      /**  Value to display on package control label.  */  
   LabelValue12:string,
      /**  Value to display on package control label.  */  
   LabelValue13:string,
      /**  Value to display on package control label.  */  
   LabelValue14:string,
      /**  Value to display on package control label.  */  
   LabelValue15:string,
      /**  Value to display on package control label.  */  
   LabelValue16:string,
      /**  Value to display on package control label.  */  
   LabelValue17:string,
      /**  Value to display on package control label.  */  
   LabelValue18:string,
      /**  Value to display on package control label.  */  
   LabelValue19:string,
      /**  Value to display on package control label.  */  
   LabelValue20:string,
      /**  Value to display on package control label.  */  
   LabelValue21:string,
      /**  Value to display on package control label.  */  
   LabelValue22:string,
      /**  Value to display on package control label.  */  
   LabelValue23:string,
      /**  Value to display on package control label.  */  
   LabelValue24:string,
      /**  Value to display on package control label.  */  
   LabelValue25:string,
      /**  Value to display on package control label.  */  
   LabelValue26:string,
      /**  Value to display on package control label.  */  
   LabelValue27:string,
      /**  Value to display on package control label.  */  
   LabelValue28:string,
      /**  Value to display on package control label.  */  
   LabelValue29:string,
      /**  Value to display on package control label.  */  
   LabelValue30:string,
      /**  Date that record was created.  */  
   CreatedDate:string,
      /**  The user ID for the user who created this record.  */  
   CreatedBy:string,
      /**  Date that record was last updated.  */  
   UpdatedDate:string,
      /**  The user ID for the user who last updated this record.  */  
   UpdatedBy:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtDemandImportEntryTableset{
   ImportGrp:Erp_Tablesets_ImportGrpRow[],
   DemandHeadImport:Erp_Tablesets_DemandHeadImportRow[],
   PkgControlLabelValueImport:Erp_Tablesets_PkgControlLabelValueImportRow[],
   DemandDetailImport:Erp_Tablesets_DemandDetailImportRow[],
   DemandMiscChgImport:Erp_Tablesets_DemandMiscChgImportRow[],
   DemandScheduleImport:Erp_Tablesets_DemandScheduleImportRow[],
   DemandMiscChgImportDH:Erp_Tablesets_DemandMiscChgImportDHRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param company
      @param importID
   */  
export interface GetByID_input{
   company:string,
   importID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DemandImportEntryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DemandImportEntryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DemandImportEntryTableset[],
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
   returnObj:Erp_Tablesets_ImportGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param importID
      @param demandContractNum
      @param demandHeadSeq
   */  
export interface GetNewDemandDetailImport_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
   importID:number,
   demandContractNum:number,
   demandHeadSeq:number,
}

export interface GetNewDemandDetailImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param importID
      @param demandContractNum
   */  
export interface GetNewDemandHeadImport_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
   importID:number,
   demandContractNum:number,
}

export interface GetNewDemandHeadImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param importID
      @param demandContractNum
      @param demandHeadSeq
      @param demandDtlSeq
   */  
export interface GetNewDemandMiscChgImportDH_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
   importID:number,
   demandContractNum:number,
   demandHeadSeq:number,
   demandDtlSeq:number,
}

export interface GetNewDemandMiscChgImportDH_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param importID
      @param demandContractNum
      @param demandHeadSeq
      @param demandDtlSeq
   */  
export interface GetNewDemandMiscChgImport_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
   importID:number,
   demandContractNum:number,
   demandHeadSeq:number,
   demandDtlSeq:number,
}

export interface GetNewDemandMiscChgImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param importID
      @param demandContractNum
      @param demandHeadSeq
      @param demandDtlSeq
   */  
export interface GetNewDemandScheduleImport_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
   importID:number,
   demandContractNum:number,
   demandHeadSeq:number,
   demandDtlSeq:number,
}

export interface GetNewDemandScheduleImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewImportGrp_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
}

export interface GetNewImportGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param plant
      @param shipToCustID
      @param shipToNum
      @param partNum
      @param demandContractNum
      @param demandHeadSeq
   */  
export interface GetNewPkgControlLabelValueImport_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   company:string,
   plant:string,
   shipToCustID:string,
   shipToNum:string,
   partNum:string,
   demandContractNum:number,
   demandHeadSeq:number,
}

export interface GetNewPkgControlLabelValueImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ipCustNum
      @param ipPONum
      @param ipUnitPrice
      @param ipEDIUnitPrice
      @param ipDemandDtlSeq
   */  
export interface GetPriceDiscrepancy_input{
      /**  CustNum  */  
   ipCustNum:number,
      /**  PONum  */  
   ipPONum:string,
      /**  UnitPrice  */  
   ipUnitPrice:number,
      /**  EDIUnitPrice  */  
   ipEDIUnitPrice:number,
      /**  DemandDtlSeq  */  
   ipDemandDtlSeq:number,
}

export interface GetPriceDiscrepancy_output{
parameters : {
      /**  output parameters  */  
   opPriceDiscrepancy:boolean,
}
}

   /** Required : 
      @param whereClauseImportGrp
      @param whereClauseDemandHeadImport
      @param whereClausePkgControlLabelValueImport
      @param whereClauseDemandDetailImport
      @param whereClauseDemandMiscChgImport
      @param whereClauseDemandScheduleImport
      @param whereClauseDemandMiscChgImportDH
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseImportGrp:string,
   whereClauseDemandHeadImport:string,
   whereClausePkgControlLabelValueImport:string,
   whereClauseDemandDetailImport:string,
   whereClauseDemandMiscChgImport:string,
   whereClauseDemandScheduleImport:string,
   whereClauseDemandMiscChgImportDH:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DemandImportEntryTableset[],
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
      @param udLine
      @param tableName
      @param SysRowID
   */  
export interface ImportEDIOnUDImport_input{
   udLine:string,
   tableName:string,
   SysRowID:string,
}

export interface ImportEDIOnUDImport_output{
   returnObj:string,
}

   /** Required : 
      @param DemandHeadRowid
   */  
export interface ImportEDIPostProcessDemand_input{
   DemandHeadRowid:string,
}

export interface ImportEDIPostProcessDemand_output{
   returnObj:string,
}

   /** Required : 
      @param DemandHeadRowid
   */  
export interface ImportEDIPreProcessDemand_input{
   DemandHeadRowid:string,
}

export interface ImportEDIPreProcessDemand_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface ImportEDIb4Tran_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ImportEDIb4Tran_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface ImportEDIb4Val_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface ImportEDIb4Val_output{
   returnObj:string,
}

   /** Required : 
      @param importID
   */  
export interface ReadyToProcess_input{
      /**  The IntQueID of a Demand PO records  */  
   importID:number,
}

export interface ReadyToProcess_output{
   returnObj:Erp_Tablesets_DemandImportEntryTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDemandImportEntryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDemandImportEntryTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
}
}

   /** Required : 
      @param ds
      @param manualValidation
      @param hmrcFraudPrevHeader
   */  
export interface ValidateOTSTaxID_input{
   ds:Erp_Tablesets_DemandImportEntryTableset[],
   manualValidation:boolean,
   hmrcFraudPrevHeader:string,
}

export interface ValidateOTSTaxID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandImportEntryTableset,
   opMessage:string,
}
}

