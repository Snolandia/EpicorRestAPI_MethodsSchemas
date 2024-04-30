import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.ImportMgmtSvc
// Description: ImportMgmtSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/$metadata", {
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
   Description: Get ImportMgmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportMgmts
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportGroupRow
   */  
export function get_ImportMgmts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportMgmts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportMgmts(requestBody:Ice_Tablesets_ImportGroupRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportMgmt item
   Description: Calls GetByID to retrieve the ImportMgmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportMgmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportGroupRow
   */  
export function get_ImportMgmts_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportGroupRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")", {
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
         resolve(data as Ice_Tablesets_ImportGroupRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportMgmt for the service
   Description: Calls UpdateExt to update ImportMgmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportMgmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportMgmts_Company_GroupID(Company:string, GroupID:string, requestBody:Ice_Tablesets_ImportGroupRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete ImportMgmt item
   Description: Call UpdateExt to delete ImportMgmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportMgmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportMgmts_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")", {
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
   Description: Get ImportFiles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportFiles1
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportFileRow
   */  
export function get_ImportMgmts_Company_GroupID_ImportFiles(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")/ImportFiles", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportFile item
   Description: Calls GetByID to retrieve the ImportFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportFile1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportFileRow
   */  
export function get_ImportMgmts_Company_GroupID_ImportFiles_Company_GroupID_FileID(Company:string, GroupID:string, FileID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")", {
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
         resolve(data as Ice_Tablesets_ImportFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ImportFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportFiles
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportFileRow
   */  
export function get_ImportFiles(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportFiles
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportFiles(requestBody:Ice_Tablesets_ImportFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportFile item
   Description: Calls GetByID to retrieve the ImportFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportFile
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportFileRow
   */  
export function get_ImportFiles_Company_GroupID_FileID(Company:string, GroupID:string, FileID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")", {
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
         resolve(data as Ice_Tablesets_ImportFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportFile for the service
   Description: Calls UpdateExt to update ImportFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportFile
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportFiles_Company_GroupID_FileID(Company:string, GroupID:string, FileID:string, requestBody:Ice_Tablesets_ImportFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")", {
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
   Summary: Call UpdateExt to delete ImportFile item
   Description: Call UpdateExt to delete ImportFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportFile
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportFiles_Company_GroupID_FileID(Company:string, GroupID:string, FileID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")", {
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
   Description: Get ImportDocuments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportDocuments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportDocumentRow
   */  
export function get_ImportFiles_Company_GroupID_FileID_ImportDocuments(Company:string, GroupID:string, FileID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportDocumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportDocuments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportDocumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportDocument item
   Description: Calls GetByID to retrieve the ImportDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportDocument1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportDocumentRow
   */  
export function get_ImportFiles_Company_GroupID_FileID_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company:string, GroupID:string, FileID:string, DocumentNumber:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportDocumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")", {
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
         resolve(data as Ice_Tablesets_ImportDocumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ImportExecutionPlans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportExecutionPlans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanRow
   */  
export function get_ImportFiles_Company_GroupID_FileID_ImportExecutionPlans(Company:string, GroupID:string, FileID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportExecutionPlans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportExecutionPlan item
   Description: Calls GetByID to retrieve the ImportExecutionPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlan1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   */  
export function get_ImportFiles_Company_GroupID_FileID_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportExecutionPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")", {
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
         resolve(data as Ice_Tablesets_ImportExecutionPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ImportDocuments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportDocuments
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportDocumentRow
   */  
export function get_ImportDocuments(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportDocumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportDocumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportDocuments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportDocumentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportDocuments(requestBody:Ice_Tablesets_ImportDocumentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportDocument item
   Description: Calls GetByID to retrieve the ImportDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportDocument
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportDocumentRow
   */  
export function get_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company:string, GroupID:string, FileID:string, DocumentNumber:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportDocumentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")", {
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
         resolve(data as Ice_Tablesets_ImportDocumentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportDocument for the service
   Description: Calls UpdateExt to update ImportDocument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportDocument
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company:string, GroupID:string, FileID:string, DocumentNumber:string, requestBody:Ice_Tablesets_ImportDocumentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")", {
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
   Summary: Call UpdateExt to delete ImportDocument item
   Description: Call UpdateExt to delete ImportDocument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportDocument
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company:string, GroupID:string, FileID:string, DocumentNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")", {
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
   Description: Get ImportTasks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportTasks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskRow
   */  
export function get_ImportDocuments_Company_GroupID_FileID_DocumentNumber_ImportTasks(Company:string, GroupID:string, FileID:string, DocumentNumber:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")/ImportTasks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportTask item
   Description: Calls GetByID to retrieve the ImportTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTask1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportTaskRow
   */  
export function get_ImportDocuments_Company_GroupID_FileID_DocumentNumber_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")", {
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
         resolve(data as Ice_Tablesets_ImportTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ImportTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportTasks
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskRow
   */  
export function get_ImportTasks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportTasks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportTasks(requestBody:Ice_Tablesets_ImportTaskRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportTask item
   Description: Calls GetByID to retrieve the ImportTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTask
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportTaskRow
   */  
export function get_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportTaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")", {
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
         resolve(data as Ice_Tablesets_ImportTaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportTask for the service
   Description: Calls UpdateExt to update ImportTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportTask
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, requestBody:Ice_Tablesets_ImportTaskRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")", {
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
   Summary: Call UpdateExt to delete ImportTask item
   Description: Call UpdateExt to delete ImportTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportTask
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")", {
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
   Description: Get ImportTaskLogs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportTaskLogs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskLogRow
   */  
export function get_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_ImportTaskLogs(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")/ImportTaskLogs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportTaskLog item
   Description: Calls GetByID to retrieve the ImportTaskLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTaskLog1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param LogID Desc: LogID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportTaskLogRow
   */  
export function get_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, LogID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportTaskLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")", {
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
         resolve(data as Ice_Tablesets_ImportTaskLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ImportTaskLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportTaskLogs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskLogRow
   */  
export function get_ImportTaskLogs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportTaskLogs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportTaskLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportTaskLogs(requestBody:Ice_Tablesets_ImportTaskLogRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportTaskLog item
   Description: Calls GetByID to retrieve the ImportTaskLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTaskLog
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param LogID Desc: LogID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportTaskLogRow
   */  
export function get_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, LogID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportTaskLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")", {
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
         resolve(data as Ice_Tablesets_ImportTaskLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportTaskLog for the service
   Description: Calls UpdateExt to update ImportTaskLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportTaskLog
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param LogID Desc: LogID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, LogID:string, requestBody:Ice_Tablesets_ImportTaskLogRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")", {
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
   Summary: Call UpdateExt to delete ImportTaskLog item
   Description: Call UpdateExt to delete ImportTaskLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportTaskLog
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param LogID Desc: LogID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, TaskID:string, LogID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")", {
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
   Description: Get ImportExecutionPlans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportExecutionPlans
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanRow
   */  
export function get_ImportExecutionPlans(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportExecutionPlans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportExecutionPlans(requestBody:Ice_Tablesets_ImportExecutionPlanRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportExecutionPlan item
   Description: Calls GetByID to retrieve the ImportExecutionPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlan
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   */  
export function get_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportExecutionPlanRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")", {
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
         resolve(data as Ice_Tablesets_ImportExecutionPlanRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportExecutionPlan for the service
   Description: Calls UpdateExt to update ImportExecutionPlan. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportExecutionPlan
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, requestBody:Ice_Tablesets_ImportExecutionPlanRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")", {
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
   Summary: Call UpdateExt to delete ImportExecutionPlan item
   Description: Call UpdateExt to delete ImportExecutionPlan item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportExecutionPlan
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")", {
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
   Description: Get ImportExecutionPlanDependencies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportExecutionPlanDependencies1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanDependencyRow
   */  
export function get_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_ImportExecutionPlanDependencies(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanDependencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")/ImportExecutionPlanDependencies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanDependencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ImportExecutionPlanDependency item
   Description: Calls GetByID to retrieve the ImportExecutionPlanDependency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlanDependency1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param DependsOn Desc: DependsOn   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   */  
export function get_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, DependsOn:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportExecutionPlanDependencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")", {
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
         resolve(data as Ice_Tablesets_ImportExecutionPlanDependencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ImportExecutionPlanDependencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportExecutionPlanDependencies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanDependencyRow
   */  
export function get_ImportExecutionPlanDependencies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanDependencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanDependencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportExecutionPlanDependencies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportExecutionPlanDependencies(requestBody:Ice_Tablesets_ImportExecutionPlanDependencyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ImportExecutionPlanDependency item
   Description: Calls GetByID to retrieve the ImportExecutionPlanDependency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlanDependency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param DependsOn Desc: DependsOn   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   */  
export function get_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, DependsOn:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ImportExecutionPlanDependencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")", {
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
         resolve(data as Ice_Tablesets_ImportExecutionPlanDependencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportExecutionPlanDependency for the service
   Description: Calls UpdateExt to update ImportExecutionPlanDependency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportExecutionPlanDependency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param DependsOn Desc: DependsOn   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, DependsOn:string, requestBody:Ice_Tablesets_ImportExecutionPlanDependencyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")", {
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
   Summary: Call UpdateExt to delete ImportExecutionPlanDependency item
   Description: Call UpdateExt to delete ImportExecutionPlanDependency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportExecutionPlanDependency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param FileID Desc: FileID   Required: True   Allow empty value : True
      @param DocumentNumber Desc: DocumentNumber   Required: True   Allow empty value : True
      @param ExecutionPlanID Desc: ExecutionPlanID   Required: True   Allow empty value : True
      @param DependsOn Desc: DependsOn   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company:string, GroupID:string, FileID:string, DocumentNumber:string, ExecutionPlanID:string, DependsOn:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportGroupListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupListRow)
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
export function get_GetRows(whereClauseImportGroup:string, whereClauseImportFile:string, whereClauseImportDocument:string, whereClauseImportTask:string, whereClauseImportTaskLog:string, whereClauseImportExecutionPlan:string, whereClauseImportExecutionPlanDependency:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseImportGroup!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportGroup=" + whereClauseImportGroup
   }
   if(typeof whereClauseImportFile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportFile=" + whereClauseImportFile
   }
   if(typeof whereClauseImportDocument!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportDocument=" + whereClauseImportDocument
   }
   if(typeof whereClauseImportTask!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportTask=" + whereClauseImportTask
   }
   if(typeof whereClauseImportTaskLog!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportTaskLog=" + whereClauseImportTaskLog
   }
   if(typeof whereClauseImportExecutionPlan!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportExecutionPlan=" + whereClauseImportExecutionPlan
   }
   if(typeof whereClauseImportExecutionPlanDependency!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportExecutionPlanDependency=" + whereClauseImportExecutionPlanDependency
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGroup
   Description: GetNewGroup - generates a new group
   OperationID: GetNewGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGroup(requestBody:GetNewGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFile
   Description: creates a new file and a Group if needed
   OperationID: GetNewFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFile(requestBody:GetNewFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UploadFilesAndImport
   Description: Upload files And launches the import proces
   OperationID: UploadFilesAndImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UploadFilesAndImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFilesAndImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadFilesAndImport(requestBody:UploadFilesAndImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UploadFilesAndImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/UploadFilesAndImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UploadFilesAndImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIntQueID
   Description: get IntQueID for the Document we want to edit in Workbench
   OperationID: GetIntQueID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetIntQueID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIntQueID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIntQueID(requestBody:GetIntQueID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetIntQueID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetIntQueID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetIntQueID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelImport
   Description: CancelImport method - this method calls cancel method from Import BO
   OperationID: CancelImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CancelImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelImport(requestBody:CancelImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CancelImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/CancelImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CancelImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PauseImport
   Description: PauseImport method - this method calls pause method from Import BO
   OperationID: PauseImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PauseImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PauseImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PauseImport(requestBody:PauseImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PauseImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/PauseImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PauseImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RestartImport
   Description: RestartImport method - this method calls restart method from Import BO
   OperationID: RestartImport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RestartImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestartImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RestartImport(requestBody:RestartImport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RestartImport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/RestartImport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RestartImport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportGroup(requestBody:GetNewImportGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportFile(requestBody:GetNewImportFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportDocument
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportDocument(requestBody:GetNewImportDocument_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportDocument_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportDocument", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportDocument_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportTask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportTask(requestBody:GetNewImportTask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportTask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportTask", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportTask_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportTaskLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportTaskLog
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportTaskLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportTaskLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportTaskLog(requestBody:GetNewImportTaskLog_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportTaskLog_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportTaskLog", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportTaskLog_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportExecutionPlan
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportExecutionPlan
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportExecutionPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportExecutionPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportExecutionPlan(requestBody:GetNewImportExecutionPlan_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportExecutionPlan_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportExecutionPlan", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportExecutionPlan_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewImportExecutionPlanDependency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportExecutionPlanDependency
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewImportExecutionPlanDependency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportExecutionPlanDependency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportExecutionPlanDependency(requestBody:GetNewImportExecutionPlanDependency_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewImportExecutionPlanDependency_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetNewImportExecutionPlanDependency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewImportExecutionPlanDependency_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportDocumentRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportDocumentRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanDependencyRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportExecutionPlanDependencyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportExecutionPlanRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportFileRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportFileRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportGroupListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportGroupRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskLogRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportTaskLogRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ImportTaskRow,
}

export interface Ice_Tablesets_ImportDocumentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the identification number of the group of the imported files.  */  
   "GroupID":number,
      /**  Displays the identification number of the imported file.  */  
   "FileID":number,
      /**  Displays the sequence number of the document.  */  
   "DocumentNumber":number,
      /**  Displays the Epicor system group used for the selected program. Epicor programs either belong to the application system (ERP) or the tools system (ICE).  */  
   "SystemCode":string,
      /**  Defines the class of the document, such Sales Order, Purchase Order, AR Invoice, etc.  */  
   "ClassName":string,
      /**  Specifies the document type name that describes a particular shape of a document of the current class name, i.e. a Contract Sales Order from the class name Sales Order.  */  
   "DocumentType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The number of rows contained in the document.  */  
   "NumOfInputRows":number,
      /**  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  */  
   "Status":string,
      /**  Time spent on executing all document import calls.  */  
   "Duration":number,
      /**  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  */  
   "PrimaryKey":string,
      /**  column used only to be displayed on navigation controls.  */  
   "NavDescription":string,
      /**  column used only to be displayed on navigation controls.  */  
   "NavFullDescription":string,
   "ExistsIntQueIn":boolean,
   "CancelledTasks":number,
   "FailedTasks":number,
   "PausedTasks":number,
   "RowsPerMinute":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportExecutionPlanDependencyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the identification number of the group of the imported files.  */  
   "GroupID":number,
      /**  Displays the identification number of the imported file.  */  
   "FileID":number,
      /**  Displays the sequence number of the document.  */  
   "DocumentNumber":number,
      /**  ExecutionPlanID  */  
   "ExecutionPlanID":number,
      /**  Defines if the execution plan depends on other execution plans  */  
   "DependsOn":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportExecutionPlanRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the identification number of the group of the imported files.  */  
   "GroupID":number,
      /**  Displays the identification number of the imported file.  */  
   "FileID":number,
      /**  Displays the sequence number of the document.  */  
   "DocumentNumber":number,
      /**  Defines a unique identifier for the current execution plan row  */  
   "ExecutionPlanID":number,
      /**  Defines a block of execution plans that will run together in an isolated way, if multiple blocks exist per file they can potentially run in parallel  */  
   "ExecutionBlockID":number,
      /**  Defines the name of the method that would be executed on the current file and document combination  */  
   "ExecutionAction":string,
      /**  Defines the sequence on which the tasks of a block can potentially run as, ordered always in ascending order  */  
   "TaskSeq":number,
      /**  defines the status of the current execution plan row, valid statuses are Pending, Processing, Completed, Paused, Cancelled and Error  */  
   "Status":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "FileName":string,
   "StartedEnded":string,
   "BitFlag":number,
   "ImportTaskLinkStartedOn":string,
   "ImportTaskLinkDuration":number,
   "ImportTaskLinkEndedOn":string,
   "ImportTaskLinkNumOfInputRows":number,
   "ImportTaskLinkPrimaryKey":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportFileRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the identification number of the group of the imported files.  */  
   "GroupID":number,
      /**  Displays the identification number of the imported file.  */  
   "FileID":number,
      /**  Available if specified in the imported file, this field displays additional comments that defines importing needs about this file. These comments might include special file instructions, comments to the imported sales order sales order or other information that needs to be included.  */  
   "Comments":string,
      /**  Displays the directory path and filename for the imported file. By default, the file format is limited to JavaScript Object Notation (*.json) and Extensible Markup Language (*.xml).  */  
   "FileName":string,
      /**  Displays the size of the imported file in megabytes (MB).  */  
   "Size":number,
      /**  Displays the current status of a file, valid statuses are PENDING,ERROR,COMPLETE.  */  
   "UploadStatus":string,
      /**  Specifies the total number of documents in the imported file. A file may contain one or more documents. Each document must include a header (i.e. sales order header) and details (i.e. sales order lines).  */  
   "NumberOfDocuments":number,
      /**  Determines how the process should proceed when an error is caught during the import process. Select this check box to skip the error entry and continue processing.  */  
   "ContinueProcessingOnError":boolean,
      /**  Select this check box to roll back parent on child error.  */  
   "RollbackParentOnChildError":boolean,
      /**  Select this check box to toggle between synchronous and asynchronous file execution. If you run the file synchronously, this file is processed immediately when the remaining files you have uploaded in the Upload sheet execute. Asynchronous execution means the call is executed immediately, but the action does not wait until the remaining files are finished and the results are processed.  */  
   "RunSynchronously":boolean,
      /**  Overrides the default company retrieved from the imported file that displays in the Company field in the Company Maintenance program.  */  
   "OverrideCompany":string,
      /**  Overrides the default plant retrieved from the imported file.  */  
   "OverridePlant":string,
      /**  Overrides the default language retrieved from the imported file that displays in the Language ID field in the Language Maintenance program.  */  
   "OverrideLanguage":string,
      /**  Overrides the default format culture retrieved from the imported file. Use the Format Culture drop-down list to select the culture code you want to define for this user. The culture code defines the interface and data format for a specific world culture. When you select a culture code for a user account, this specific user views and enters data in the method appropriate for the selected culture.  */  
   "OverrideFormatCulture":string,
      /**  Override the default schema name of the imported file.  */  
   "OverrideSchemaName":string,
      /**  Contains a copy of the ImportSettings used by the current import file, describes the alternate settings that a user can override.  */  
   "ImportSettings":string,
      /**  Describes the current specialized formatter used to parse the current file contents, by default GenericJSON and GenericXML are the valid values, customized formatters will be described in this field.  */  
   "Formatter":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  FormatName  */  
   "FormatName":string,
   "FilePath":string,
   "FileExtension":string,
      /**  the number of imported doucments  */  
   "ImportedDocuments":number,
   "FailedDocuments":number,
      /**  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  */  
   "Status":string,
   "StartedEnded":string,
   "TimeLeft":number,
   "ProgressPercent":number,
   "RowsPerMinute":number,
   "Duration":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportGroupListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  identification number of the group of the imported files  */  
   "GroupID":number,
      /**  Further identifies each group.  */  
   "Description":string,
      /**  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  */  
   "Status":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportGroupRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  identification number of the group of the imported files  */  
   "GroupID":number,
      /**  Further identifies each group.  */  
   "Description":string,
      /**  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  */  
   "Status":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportTaskLogRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the identification number of the group of the imported files.  */  
   "GroupID":number,
      /**  Displays the identification number of the imported file.  */  
   "FileID":number,
      /**  Displays the sequence number of the document.  */  
   "DocumentNumber":number,
      /**  Defines a unique identifier for the current execution plan row  */  
   "ExecutionPlanID":number,
      /**  Displays the sequence number of the task.  */  
   "TaskID":number,
      /**  Displays the sequence number of the log  */  
   "LogID":number,
      /**  Displays the date and time on which the task was started.  */  
   "EnteredOn":string,
      /**  When selected, specifies an error occurred during document import processing. Click the Message field to display additional information about the error.  */  
   "Error":boolean,
      /**  Displays the name of the system table where the error occurred.  */  
   "ErrorTableName":string,
      /**  Displays the row number where the import failed  */  
   "ErrorRowNum":number,
      /**  this identifier should match with RowGuid field from  ice.ImportKeyValueStore, it is used to display the rows on Integration Workbench  */  
   "ErrorSysRowID":string,
      /**  An import process passes through different statuses during its lifecycle. Message information displays as the document is processing.  */  
   "Message":string,
      /**  Displays the type of the message. The following types are available are Informational and Error  */  
   "MessageType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "FileName":string,
   "BitFlag":number,
   "ImportExecutionPlanLinkExecutionAction":string,
   "PrimaryKeyPrimaryKey":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ImportTaskRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Displays the identification number of the group of the imported files.  */  
   "GroupID":number,
      /**  Displays the identification number of the imported file.  */  
   "FileID":number,
      /**  Displays the sequence number of the document.  */  
   "DocumentNumber":number,
      /**  Defines a unique identifier for the current execution plan row  */  
   "ExecutionPlanID":number,
      /**  Displays the sequence number of the task.  */  
   "TaskID":number,
      /**  Displays the date and time on which the task was started.  */  
   "StartedOn":string,
      /**  Displays the date and time on which the task finished.  */  
   "EndedOn":string,
      /**  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  */  
   "Status":string,
      /**  The number of rows contained in the document.  */  
   "NumOfInputRows":number,
      /**  Identifies the user who submitted, or launched the import task.  */  
   "UserID":string,
      /**  Displays the identification number of the process.  */  
   "ProcessID":string,
      /**  Indicates which thread from the application server was used to run the call.  */  
   "ThreadID":number,
      /**  Defines the specific name for the server from which you capture the logs.  */  
   "ServerName":string,
      /**  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  */  
   "PrimaryKey":string,
      /**  Time spent on executing a document import call.  */  
   "Duration":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  field to shorten the link field ExecutionAction and display it on UI bavigation  */  
   "DspTaskName":string,
   "BitFlag":number,
   "ActionNameExecutionAction":string,
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
      @param Company
      @param GroupID
   */  
export interface CancelImport_input{
   Company:string,
   GroupID:number,
}

export interface CancelImport_output{
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:number,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ImportMgmtTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ImportMgmtTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ImportMgmtTableset[],
}

   /** Required : 
      @param company
      @param groupID
      @param fileID
      @param documentNumber
   */  
export interface GetIntQueID_input{
   company:string,
   groupID:string,
   fileID:string,
   documentNumber:string,
}

export interface GetIntQueID_output{
   returnObj:number,
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
   returnObj:Ice_Tablesets_ImportMgmtListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param FilePath
      @param GroupID
      @param ds
   */  
export interface GetNewFile_input{
   FilePath:string,
   GroupID:number,
   ds:Ice_Tablesets_ImportMgmtTableset[],
}

export interface GetNewFile_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGroup_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
}

export interface GetNewGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param fileID
   */  
export interface GetNewImportDocument_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
   groupID:number,
   fileID:number,
}

export interface GetNewImportDocument_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param fileID
      @param documentNumber
      @param executionPlanID
   */  
export interface GetNewImportExecutionPlanDependency_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
   groupID:number,
   fileID:number,
   documentNumber:number,
   executionPlanID:number,
}

export interface GetNewImportExecutionPlanDependency_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param fileID
      @param documentNumber
   */  
export interface GetNewImportExecutionPlan_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
   groupID:number,
   fileID:number,
   documentNumber:number,
}

export interface GetNewImportExecutionPlan_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewImportFile_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
   groupID:number,
}

export interface GetNewImportFile_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewImportGroup_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
}

export interface GetNewImportGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param fileID
      @param documentNumber
      @param executionPlanID
      @param taskID
   */  
export interface GetNewImportTaskLog_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
   groupID:number,
   fileID:number,
   documentNumber:number,
   executionPlanID:number,
   taskID:number,
}

export interface GetNewImportTaskLog_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param fileID
      @param documentNumber
      @param executionPlanID
   */  
export interface GetNewImportTask_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
   groupID:number,
   fileID:number,
   documentNumber:number,
   executionPlanID:number,
}

export interface GetNewImportTask_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param whereClauseImportGroup
      @param whereClauseImportFile
      @param whereClauseImportDocument
      @param whereClauseImportTask
      @param whereClauseImportTaskLog
      @param whereClauseImportExecutionPlan
      @param whereClauseImportExecutionPlanDependency
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseImportGroup:string,
   whereClauseImportFile:string,
   whereClauseImportDocument:string,
   whereClauseImportTask:string,
   whereClauseImportTaskLog:string,
   whereClauseImportExecutionPlan:string,
   whereClauseImportExecutionPlanDependency:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ImportMgmtTableset[],
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

export interface Ice_Tablesets_ImportDocumentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the identification number of the group of the imported files.  */  
   GroupID:number,
      /**  Displays the identification number of the imported file.  */  
   FileID:number,
      /**  Displays the sequence number of the document.  */  
   DocumentNumber:number,
      /**  Displays the Epicor system group used for the selected program. Epicor programs either belong to the application system (ERP) or the tools system (ICE).  */  
   SystemCode:string,
      /**  Defines the class of the document, such Sales Order, Purchase Order, AR Invoice, etc.  */  
   ClassName:string,
      /**  Specifies the document type name that describes a particular shape of a document of the current class name, i.e. a Contract Sales Order from the class name Sales Order.  */  
   DocumentType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The number of rows contained in the document.  */  
   NumOfInputRows:number,
      /**  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  */  
   Status:string,
      /**  Time spent on executing all document import calls.  */  
   Duration:number,
      /**  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  */  
   PrimaryKey:string,
      /**  column used only to be displayed on navigation controls.  */  
   NavDescription:string,
      /**  column used only to be displayed on navigation controls.  */  
   NavFullDescription:string,
   ExistsIntQueIn:boolean,
   CancelledTasks:number,
   FailedTasks:number,
   PausedTasks:number,
   RowsPerMinute:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportExecutionPlanDependencyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the identification number of the group of the imported files.  */  
   GroupID:number,
      /**  Displays the identification number of the imported file.  */  
   FileID:number,
      /**  Displays the sequence number of the document.  */  
   DocumentNumber:number,
      /**  ExecutionPlanID  */  
   ExecutionPlanID:number,
      /**  Defines if the execution plan depends on other execution plans  */  
   DependsOn:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportExecutionPlanRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the identification number of the group of the imported files.  */  
   GroupID:number,
      /**  Displays the identification number of the imported file.  */  
   FileID:number,
      /**  Displays the sequence number of the document.  */  
   DocumentNumber:number,
      /**  Defines a unique identifier for the current execution plan row  */  
   ExecutionPlanID:number,
      /**  Defines a block of execution plans that will run together in an isolated way, if multiple blocks exist per file they can potentially run in parallel  */  
   ExecutionBlockID:number,
      /**  Defines the name of the method that would be executed on the current file and document combination  */  
   ExecutionAction:string,
      /**  Defines the sequence on which the tasks of a block can potentially run as, ordered always in ascending order  */  
   TaskSeq:number,
      /**  defines the status of the current execution plan row, valid statuses are Pending, Processing, Completed, Paused, Cancelled and Error  */  
   Status:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   FileName:string,
   StartedEnded:string,
   BitFlag:number,
   ImportTaskLinkStartedOn:string,
   ImportTaskLinkDuration:number,
   ImportTaskLinkEndedOn:string,
   ImportTaskLinkNumOfInputRows:number,
   ImportTaskLinkPrimaryKey:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportFileRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the identification number of the group of the imported files.  */  
   GroupID:number,
      /**  Displays the identification number of the imported file.  */  
   FileID:number,
      /**  Available if specified in the imported file, this field displays additional comments that defines importing needs about this file. These comments might include special file instructions, comments to the imported sales order sales order or other information that needs to be included.  */  
   Comments:string,
      /**  Displays the directory path and filename for the imported file. By default, the file format is limited to JavaScript Object Notation (*.json) and Extensible Markup Language (*.xml).  */  
   FileName:string,
      /**  Displays the size of the imported file in megabytes (MB).  */  
   Size:number,
      /**  Displays the current status of a file, valid statuses are PENDING,ERROR,COMPLETE.  */  
   UploadStatus:string,
      /**  Specifies the total number of documents in the imported file. A file may contain one or more documents. Each document must include a header (i.e. sales order header) and details (i.e. sales order lines).  */  
   NumberOfDocuments:number,
      /**  Determines how the process should proceed when an error is caught during the import process. Select this check box to skip the error entry and continue processing.  */  
   ContinueProcessingOnError:boolean,
      /**  Select this check box to roll back parent on child error.  */  
   RollbackParentOnChildError:boolean,
      /**  Select this check box to toggle between synchronous and asynchronous file execution. If you run the file synchronously, this file is processed immediately when the remaining files you have uploaded in the Upload sheet execute. Asynchronous execution means the call is executed immediately, but the action does not wait until the remaining files are finished and the results are processed.  */  
   RunSynchronously:boolean,
      /**  Overrides the default company retrieved from the imported file that displays in the Company field in the Company Maintenance program.  */  
   OverrideCompany:string,
      /**  Overrides the default plant retrieved from the imported file.  */  
   OverridePlant:string,
      /**  Overrides the default language retrieved from the imported file that displays in the Language ID field in the Language Maintenance program.  */  
   OverrideLanguage:string,
      /**  Overrides the default format culture retrieved from the imported file. Use the Format Culture drop-down list to select the culture code you want to define for this user. The culture code defines the interface and data format for a specific world culture. When you select a culture code for a user account, this specific user views and enters data in the method appropriate for the selected culture.  */  
   OverrideFormatCulture:string,
      /**  Override the default schema name of the imported file.  */  
   OverrideSchemaName:string,
      /**  Contains a copy of the ImportSettings used by the current import file, describes the alternate settings that a user can override.  */  
   ImportSettings:string,
      /**  Describes the current specialized formatter used to parse the current file contents, by default GenericJSON and GenericXML are the valid values, customized formatters will be described in this field.  */  
   Formatter:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  FormatName  */  
   FormatName:string,
   FilePath:string,
   FileExtension:string,
      /**  the number of imported doucments  */  
   ImportedDocuments:number,
   FailedDocuments:number,
      /**  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  */  
   Status:string,
   StartedEnded:string,
   TimeLeft:number,
   ProgressPercent:number,
   RowsPerMinute:number,
   Duration:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportGroupListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  identification number of the group of the imported files  */  
   GroupID:number,
      /**  Further identifies each group.  */  
   Description:string,
      /**  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  */  
   Status:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportGroupRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  identification number of the group of the imported files  */  
   GroupID:number,
      /**  Further identifies each group.  */  
   Description:string,
      /**  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  */  
   Status:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportMgmtListTableset{
   ImportGroupList:Ice_Tablesets_ImportGroupListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ImportMgmtTableset{
   ImportGroup:Ice_Tablesets_ImportGroupRow[],
   ImportFile:Ice_Tablesets_ImportFileRow[],
   ImportDocument:Ice_Tablesets_ImportDocumentRow[],
   ImportTask:Ice_Tablesets_ImportTaskRow[],
   ImportTaskLog:Ice_Tablesets_ImportTaskLogRow[],
   ImportExecutionPlan:Ice_Tablesets_ImportExecutionPlanRow[],
   ImportExecutionPlanDependency:Ice_Tablesets_ImportExecutionPlanDependencyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ImportTaskLogRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the identification number of the group of the imported files.  */  
   GroupID:number,
      /**  Displays the identification number of the imported file.  */  
   FileID:number,
      /**  Displays the sequence number of the document.  */  
   DocumentNumber:number,
      /**  Defines a unique identifier for the current execution plan row  */  
   ExecutionPlanID:number,
      /**  Displays the sequence number of the task.  */  
   TaskID:number,
      /**  Displays the sequence number of the log  */  
   LogID:number,
      /**  Displays the date and time on which the task was started.  */  
   EnteredOn:string,
      /**  When selected, specifies an error occurred during document import processing. Click the Message field to display additional information about the error.  */  
   Error:boolean,
      /**  Displays the name of the system table where the error occurred.  */  
   ErrorTableName:string,
      /**  Displays the row number where the import failed  */  
   ErrorRowNum:number,
      /**  this identifier should match with RowGuid field from  ice.ImportKeyValueStore, it is used to display the rows on Integration Workbench  */  
   ErrorSysRowID:string,
      /**  An import process passes through different statuses during its lifecycle. Message information displays as the document is processing.  */  
   Message:string,
      /**  Displays the type of the message. The following types are available are Informational and Error  */  
   MessageType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   FileName:string,
   BitFlag:number,
   ImportExecutionPlanLinkExecutionAction:string,
   PrimaryKeyPrimaryKey:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ImportTaskRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the identification number of the group of the imported files.  */  
   GroupID:number,
      /**  Displays the identification number of the imported file.  */  
   FileID:number,
      /**  Displays the sequence number of the document.  */  
   DocumentNumber:number,
      /**  Defines a unique identifier for the current execution plan row  */  
   ExecutionPlanID:number,
      /**  Displays the sequence number of the task.  */  
   TaskID:number,
      /**  Displays the date and time on which the task was started.  */  
   StartedOn:string,
      /**  Displays the date and time on which the task finished.  */  
   EndedOn:string,
      /**  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  */  
   Status:string,
      /**  The number of rows contained in the document.  */  
   NumOfInputRows:number,
      /**  Identifies the user who submitted, or launched the import task.  */  
   UserID:string,
      /**  Displays the identification number of the process.  */  
   ProcessID:string,
      /**  Indicates which thread from the application server was used to run the call.  */  
   ThreadID:number,
      /**  Defines the specific name for the server from which you capture the logs.  */  
   ServerName:string,
      /**  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  */  
   PrimaryKey:string,
      /**  Time spent on executing a document import call.  */  
   Duration:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  field to shorten the link field ExecutionAction and display it on UI bavigation  */  
   DspTaskName:string,
   BitFlag:number,
   ActionNameExecutionAction:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtImportMgmtTableset{
   ImportGroup:Ice_Tablesets_ImportGroupRow[],
   ImportFile:Ice_Tablesets_ImportFileRow[],
   ImportDocument:Ice_Tablesets_ImportDocumentRow[],
   ImportTask:Ice_Tablesets_ImportTaskRow[],
   ImportTaskLog:Ice_Tablesets_ImportTaskLogRow[],
   ImportExecutionPlan:Ice_Tablesets_ImportExecutionPlanRow[],
   ImportExecutionPlanDependency:Ice_Tablesets_ImportExecutionPlanDependencyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param Company
      @param GroupID
   */  
export interface PauseImport_input{
   Company:string,
   GroupID:number,
}

export interface PauseImport_output{
}

   /** Required : 
      @param Company
      @param GroupID
      @param FileID
      @param DocumentNumber
   */  
export interface RestartImport_input{
   Company:string,
   GroupID:number,
      /**  If left as 0 complete group gets restarted  */  
   FileID:number,
      /**  if left as 0 complete file gets restarted  */  
   DocumentNumber:number,
}

export interface RestartImport_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtImportMgmtTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtImportMgmtTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ImportMgmtTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ImportMgmtTableset,
}
}

   /** Required : 
      @param stream
      @param groupID
      @param fileID
   */  
export interface UploadFilesAndImport_input{
   stream:string,
   groupID:number,
   fileID:number,
}

export interface UploadFilesAndImport_output{
}

