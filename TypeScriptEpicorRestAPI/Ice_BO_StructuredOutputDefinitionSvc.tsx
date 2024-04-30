import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.StructuredOutputDefinitionSvc
// Description: BO for the Structured Output Definition UI.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get StructuredOutputDefinitions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_StructuredOutputDefinitions
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputDefRow
   */  
export function get_StructuredOutputDefinitions(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_StructuredOutputDefinitions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StructuredOutputDefinitions(requestBody:Ice_Tablesets_RptStructuredOutputDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the StructuredOutputDefinition item
   Description: Calls GetByID to retrieve the StructuredOutputDefinition item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_StructuredOutputDefinition
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
   */  
export function get_StructuredOutputDefinitions_RptStructuredOutputDefID(RptStructuredOutputDefID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update StructuredOutputDefinition for the service
   Description: Calls UpdateExt to update StructuredOutputDefinition. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_StructuredOutputDefinition
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_StructuredOutputDefinitions_RptStructuredOutputDefID(RptStructuredOutputDefID:string, requestBody:Ice_Tablesets_RptStructuredOutputDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")", {
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
   Summary: Call UpdateExt to delete StructuredOutputDefinition item
   Description: Call UpdateExt to delete StructuredOutputDefinition item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_StructuredOutputDefinition
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_StructuredOutputDefinitions_RptStructuredOutputDefID(RptStructuredOutputDefID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")", {
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
   Description: Get RptStructuredOutputFiles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStructuredOutputFiles1
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileRow
   */  
export function get_StructuredOutputDefinitions_RptStructuredOutputDefID_RptStructuredOutputFiles(RptStructuredOutputDefID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")/RptStructuredOutputFiles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFile item
   Description: Calls GetByID to retrieve the RptStructuredOutputFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFile1
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   */  
export function get_StructuredOutputDefinitions_RptStructuredOutputDefID_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/StructuredOutputDefinitions(" + RptStructuredOutputDefID + ")/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RptStructuredOutputFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStructuredOutputFiles
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileRow
   */  
export function get_RptStructuredOutputFiles(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStructuredOutputFiles
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptStructuredOutputFiles(requestBody:Ice_Tablesets_RptStructuredOutputFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptStructuredOutputFile item
   Description: Calls GetByID to retrieve the RptStructuredOutputFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFile
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   */  
export function get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputFileRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputFileRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptStructuredOutputFile for the service
   Description: Calls UpdateExt to update RptStructuredOutputFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStructuredOutputFile
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, requestBody:Ice_Tablesets_RptStructuredOutputFileRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")", {
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
   Summary: Call UpdateExt to delete RptStructuredOutputFile item
   Description: Call UpdateExt to delete RptStructuredOutputFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStructuredOutputFile
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")", {
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
   Description: Get RptStructuredOutputFileElements items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStructuredOutputFileElements1
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileElementRow
   */  
export function get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileElements(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileElementRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileElements", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileElementRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileElement item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileElement item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileElement1
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param ElementID Desc: ElementID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   */  
export function get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, ElementID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputFileElementRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputFileElementRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RptStructuredOutputFileXMLNS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStructuredOutputFileXMLNS1
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   */  
export function get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileXMLNS(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileXMLNSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileXMLNS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileXMLNSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileXMLN1
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileNamespaceID Desc: RptStructuredOutputFileNamespaceID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   */  
export function get_RptStructuredOutputFiles_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, RptStructuredOutputFileNamespaceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputFileXMLNSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFiles(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + ")/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputFileXMLNSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RptStructuredOutputFileElements items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStructuredOutputFileElements
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileElementRow
   */  
export function get_RptStructuredOutputFileElements(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileElementRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileElementRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStructuredOutputFileElements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptStructuredOutputFileElements(requestBody:Ice_Tablesets_RptStructuredOutputFileElementRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileElement item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileElement item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileElement
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param ElementID Desc: ElementID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   */  
export function get_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, ElementID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputFileElementRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputFileElementRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptStructuredOutputFileElement for the service
   Description: Calls UpdateExt to update RptStructuredOutputFileElement. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStructuredOutputFileElement
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param ElementID Desc: ElementID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileElementRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, ElementID:string, requestBody:Ice_Tablesets_RptStructuredOutputFileElementRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")", {
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
   Summary: Call UpdateExt to delete RptStructuredOutputFileElement item
   Description: Call UpdateExt to delete RptStructuredOutputFileElement item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStructuredOutputFileElement
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param ElementID Desc: ElementID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptStructuredOutputFileElements_RptStructuredOutputDefID_RptStructuredOutputFileID_ElementID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, ElementID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileElements(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + ElementID + ")", {
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
   Description: Get RptStructuredOutputFileXMLNS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStructuredOutputFileXMLNS
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   */  
export function get_RptStructuredOutputFileXMLNS(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileXMLNSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileXMLNSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStructuredOutputFileXMLNS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptStructuredOutputFileXMLNS(requestBody:Ice_Tablesets_RptStructuredOutputFileXMLNSRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item
   Description: Calls GetByID to retrieve the RptStructuredOutputFileXMLN item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStructuredOutputFileXMLN
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileNamespaceID Desc: RptStructuredOutputFileNamespaceID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   */  
export function get_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, RptStructuredOutputFileNamespaceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStructuredOutputFileXMLNSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptStructuredOutputFileXMLNSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptStructuredOutputFileXMLN for the service
   Description: Calls UpdateExt to update RptStructuredOutputFileXMLN. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStructuredOutputFileXMLN
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileNamespaceID Desc: RptStructuredOutputFileNamespaceID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStructuredOutputFileXMLNSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, RptStructuredOutputFileNamespaceID:string, requestBody:Ice_Tablesets_RptStructuredOutputFileXMLNSRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")", {
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
   Summary: Call UpdateExt to delete RptStructuredOutputFileXMLN item
   Description: Call UpdateExt to delete RptStructuredOutputFileXMLN item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStructuredOutputFileXMLN
      @param RptStructuredOutputDefID Desc: RptStructuredOutputDefID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileID Desc: RptStructuredOutputFileID   Required: True   Allow empty value : True
      @param RptStructuredOutputFileNamespaceID Desc: RptStructuredOutputFileNamespaceID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptStructuredOutputFileXMLNS_RptStructuredOutputDefID_RptStructuredOutputFileID_RptStructuredOutputFileNamespaceID(RptStructuredOutputDefID:string, RptStructuredOutputFileID:string, RptStructuredOutputFileNamespaceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/RptStructuredOutputFileXMLNS(" + RptStructuredOutputDefID + "," + RptStructuredOutputFileID + "," + RptStructuredOutputFileNamespaceID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStructuredOutputDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefListRow)
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
export function get_GetRows(whereClauseRptStructuredOutputDef:string, whereClauseRptStructuredOutputFile:string, whereClauseRptStructuredOutputFileElement:string, whereClauseRptStructuredOutputFileXMLNS:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRptStructuredOutputDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptStructuredOutputDef=" + whereClauseRptStructuredOutputDef
   }
   if(typeof whereClauseRptStructuredOutputFile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptStructuredOutputFile=" + whereClauseRptStructuredOutputFile
   }
   if(typeof whereClauseRptStructuredOutputFileElement!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptStructuredOutputFileElement=" + whereClauseRptStructuredOutputFileElement
   }
   if(typeof whereClauseRptStructuredOutputFileXMLNS!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptStructuredOutputFileXMLNS=" + whereClauseRptStructuredOutputFileXMLNS
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(rptStructuredOutputDefID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rptStructuredOutputDefID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rptStructuredOutputDefID=" + rptStructuredOutputDefID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method OnChangeReportDataDefinition
   Description: Called when user changes the report data definition for the structured output definition.
   OperationID: OnChangeReportDataDefinition
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeReportDataDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReportDataDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeReportDataDefinition(requestBody:OnChangeReportDataDefinition_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeReportDataDefinition_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/OnChangeReportDataDefinition", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeReportDataDefinition_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteAllOutputFileElements
   Description: Deletes all output file elements.
   OperationID: DeleteAllOutputFileElements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteAllOutputFileElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAllOutputFileElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAllOutputFileElements(requestBody:DeleteAllOutputFileElements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteAllOutputFileElements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/DeleteAllOutputFileElements", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteAllOutputFileElements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOutputLocation
   Description: Called when user changes the output location for the structured output file.
   OperationID: OnChangeOutputLocation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOutputLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOutputLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOutputLocation(requestBody:OnChangeOutputLocation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOutputLocation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/OnChangeOutputLocation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOutputLocation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataSourceList
   Description: Get data source list (for data source combo box). Column table will be empty.
   OperationID: GetDataSourceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDataSourceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataSourceList(requestBody:GetDataSourceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataSourceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetDataSourceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDataSourceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataSourceColumns
   Description: Get columns for data source (for data column combo box). Data source table will be empty.
   OperationID: GetDataSourceColumns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDataSourceColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataSourceColumns(requestBody:GetDataSourceColumns_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataSourceColumns_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetDataSourceColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDataSourceColumns_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataSourceListWithIsUsedSet
   Description: Get data source list with IsUsed set
   OperationID: GetDataSourceListWithIsUsedSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDataSourceListWithIsUsedSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceListWithIsUsedSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataSourceListWithIsUsedSet(requestBody:GetDataSourceListWithIsUsedSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataSourceListWithIsUsedSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetDataSourceListWithIsUsedSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDataSourceListWithIsUsedSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataSourceColumnType
   Description: Get data source column data type.
   OperationID: GetDataSourceColumnType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDataSourceColumnType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceColumnType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataSourceColumnType(requestBody:GetDataSourceColumnType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataSourceColumnType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetDataSourceColumnType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDataSourceColumnType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOutputFileElements
   Description: Validate structured output file elements.
   OperationID: ValidateOutputFileElements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateOutputFileElements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOutputFileElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOutputFileElements(requestBody:ValidateOutputFileElements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateOutputFileElements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/ValidateOutputFileElements", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateOutputFileElements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateOutputFileElement
   Description: Validate structured output file element.
   OperationID: ValidateOutputFileElement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateOutputFileElement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOutputFileElement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateOutputFileElement(requestBody:ValidateOutputFileElement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateOutputFileElement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/ValidateOutputFileElement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateOutputFileElement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportFile
   Description: Imports file with XML data or json schema.
   OperationID: ImportFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportFile(requestBody:ImportFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/ImportFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportJSONSchema
   Description: Imports the json schema.
   OperationID: ImportJSONSchema
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportJSONSchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportJSONSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportJSONSchema(requestBody:ImportJSONSchema_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportJSONSchema_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/ImportJSONSchema", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportJSONSchema_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateStructuredOutputDef
   Description: Duplicates a Structured Output Definition
   OperationID: DuplicateStructuredOutputDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DuplicateStructuredOutputDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateStructuredOutputDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateStructuredOutputDef(requestBody:DuplicateStructuredOutputDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DuplicateStructuredOutputDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/DuplicateStructuredOutputDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DuplicateStructuredOutputDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateStructuredOutputFile
   Description: Duplicates a Structured Output File
   OperationID: DuplicateStructuredOutputFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DuplicateStructuredOutputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateStructuredOutputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateStructuredOutputFile(requestBody:DuplicateStructuredOutputFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DuplicateStructuredOutputFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/DuplicateStructuredOutputFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DuplicateStructuredOutputFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportXmlDataWithValues
   Description: Imports the XML data.
   OperationID: ImportXmlDataWithValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportXmlDataWithValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportXmlDataWithValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportXmlDataWithValues(requestBody:ImportXmlDataWithValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportXmlDataWithValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/ImportXmlDataWithValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportXmlDataWithValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportXmlDataWithNoValues
   Description: Imports the XML data.
   OperationID: ImportXmlDataWithNoValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportXmlDataWithNoValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportXmlDataWithNoValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportXmlDataWithNoValues(requestBody:ImportXmlDataWithNoValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportXmlDataWithNoValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/ImportXmlDataWithNoValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportXmlDataWithNoValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEICalculators
   Description: Get Electronic Interface Calculator Names in tilde-separated string (for calculation name combo box)
   OperationID: GetEICalculators
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEICalculators_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEICalculators_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEICalculators(requestBody:GetEICalculators_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEICalculators_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetEICalculators", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetEICalculators_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAncestorDataSource
   Description: Get the DataSource value from the most immediate ancestor of the file element
   OperationID: GetAncestorDataSource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAncestorDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAncestorDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAncestorDataSource(requestBody:GetAncestorDataSource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAncestorDataSource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetAncestorDataSource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAncestorDataSource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DescendantsWithDataSourceIdExist
   Description: Check if descendants with DataSourceId = original DataSourceId value exist
   OperationID: DescendantsWithDataSourceIdExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DescendantsWithDataSourceIdExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DescendantsWithDataSourceIdExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DescendantsWithDataSourceIdExist(requestBody:DescendantsWithDataSourceIdExist_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DescendantsWithDataSourceIdExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/DescendantsWithDataSourceIdExist", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DescendantsWithDataSourceIdExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateDescendantsWithNewDataSourceId
   Description: Update descendants having DataSourceId = original DataSourceId value with new DataSourceID value
   OperationID: UpdateDescendantsWithNewDataSourceId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateDescendantsWithNewDataSourceId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDescendantsWithNewDataSourceId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDescendantsWithNewDataSourceId(requestBody:UpdateDescendantsWithNewDataSourceId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateDescendantsWithNewDataSourceId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/UpdateDescendantsWithNewDataSourceId", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateDescendantsWithNewDataSourceId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptStructuredOutputDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptStructuredOutputDef(requestBody:GetNewRptStructuredOutputDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptStructuredOutputDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetNewRptStructuredOutputDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptStructuredOutputDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptStructuredOutputFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptStructuredOutputFile(requestBody:GetNewRptStructuredOutputFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptStructuredOutputFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetNewRptStructuredOutputFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptStructuredOutputFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptStructuredOutputFileElement
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputFileElement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputFileElement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputFileElement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptStructuredOutputFileElement(requestBody:GetNewRptStructuredOutputFileElement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptStructuredOutputFileElement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetNewRptStructuredOutputFileElement", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptStructuredOutputFileElement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptStructuredOutputFileXMLNS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStructuredOutputFileXMLNS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptStructuredOutputFileXMLNS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStructuredOutputFileXMLNS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptStructuredOutputFileXMLNS(requestBody:GetNewRptStructuredOutputFileXMLNS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptStructuredOutputFileXMLNS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetNewRptStructuredOutputFileXMLNS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptStructuredOutputFileXMLNS_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.StructuredOutputDefinitionSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptStructuredOutputDefListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputDefRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptStructuredOutputDefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileElementRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptStructuredOutputFileElementRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptStructuredOutputFileRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStructuredOutputFileXMLNSRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptStructuredOutputFileXMLNSRow,
}

export interface Ice_Tablesets_RptStructuredOutputDefListRow{
      /**  Company  */  
   "Company":string,
      /**  RptStructuredOutputDefID  */  
   "RptStructuredOutputDefID":string,
      /**  RptStructuredOutputDescription  */  
   "RptStructuredOutputDescription":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  ConfirmedCompliance  */  
   "ConfirmedCompliance":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "RptDataDefRptDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptStructuredOutputDefRow{
      /**  Company  */  
   "Company":string,
      /**  RptStructuredOutputDefID  */  
   "RptStructuredOutputDefID":string,
      /**  RptStructuredOutputDescription  */  
   "RptStructuredOutputDescription":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  ConfirmedCompliance  */  
   "ConfirmedCompliance":boolean,
      /**  ComplianceRule  */  
   "ComplianceRule":string,
      /**  InternalComments  */  
   "InternalComments":string,
      /**  DateFormat  */  
   "DateFormat":string,
      /**  DecimalSymbol  */  
   "DecimalSymbol":string,
      /**  DigitGroupingSymbol  */  
   "DigitGroupingSymbol":string,
      /**  NegativeSignSymbol  */  
   "NegativeSignSymbol":string,
      /**  Encoding  */  
   "Encoding":string,
      /**  Delimiter  */  
   "Delimiter":string,
      /**  EndOfRecordSymbol  */  
   "EndOfRecordSymbol":string,
      /**  QuotationMark  */  
   "QuotationMark":string,
      /**  QuoteAllValues  */  
   "QuoteAllValues":boolean,
      /**  BooleanTrue  */  
   "BooleanTrue":string,
      /**  BooleanFalse  */  
   "BooleanFalse":string,
      /**  PrePostProcessingEFTHeadCompany  */  
   "PrePostProcessingEFTHeadCompany":string,
      /**  PrePostProcessingEFTHeadUID  */  
   "PrePostProcessingEFTHeadUID":number,
      /**  AdditionalSettings  */  
   "AdditionalSettings":string,
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
      /**  Description for the PrePostProcessingEFTHeadUID  */  
   "PrePostProcessingDescription":string,
      /**  Name of the PrePostProcessingEFTHeadUID  */  
   "PrePostProcessingName":string,
   "BitFlag":number,
   "RptDataDefSystemRpt":boolean,
   "RptDataDefRptDescription":string,
   "RptDataDefDuplicateOf":string,
   "RptDataDefRptTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptStructuredOutputFileElementRow{
      /**  Company  */  
   "Company":string,
      /**  RptStructuredOutputDefID  */  
   "RptStructuredOutputDefID":string,
      /**  RptStructuredOutputFileID  */  
   "RptStructuredOutputFileID":string,
      /**  ElementID  */  
   "ElementID":number,
      /**  ElementName  */  
   "ElementName":string,
      /**  ParentElementID  */  
   "ParentElementID":number,
      /**  ChildSequence  */  
   "ChildSequence":number,
      /**  Namespace  */  
   "Namespace":string,
      /**  Prefix  */  
   "Prefix":string,
      /**  XMLAttribute  */  
   "XMLAttribute":boolean,
      /**  AggregationType  */  
   "AggregationType":number,
      /**  DecimalScale  */  
   "DecimalScale":number,
      /**  DataSourceID  */  
   "DataSourceID":string,
      /**  DataSourceColumn  */  
   "DataSourceColumn":string,
      /**  IsConstant  */  
   "IsConstant":boolean,
      /**  ConstantValue  */  
   "ConstantValue":string,
      /**  CalculationEFTHeadCompany  */  
   "CalculationEFTHeadCompany":string,
      /**  CalculationEFTHeadUID  */  
   "CalculationEFTHeadUID":number,
      /**  CalculationName  */  
   "CalculationName":string,
      /**  AdditionalSettings  */  
   "AdditionalSettings":string,
      /**  DateFormat  */  
   "DateFormat":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  JSONObject  */  
   "JSONObject":boolean,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ElementDataType  */  
   "ElementDataType":string,
      /**  ElementDescription  */  
   "ElementDescription":string,
      /**  EmptyStringGenerateEmptyElement  */  
   "EmptyStringGenerateEmptyElement":boolean,
      /**  EmptyStringSuppressOrNullElement  */  
   "EmptyStringSuppressOrNullElement":boolean,
      /**  EmptyStringSubsituteElement  */  
   "EmptyStringSubsituteElement":boolean,
      /**  EmptyStringSubsituteValue  */  
   "EmptyStringSubsituteValue":string,
      /**  ZeroNumericSuppress  */  
   "ZeroNumericSuppress":boolean,
      /**  NeedSign  */  
   "NeedSign":boolean,
      /**  CalculationEFTHeadName  */  
   "CalculationEFTHeadName":string,
      /**  .NET Data type for the datasource column.  */  
   "DataSourceColumnDataType":string,
      /**  Element name including the prefix. Prefix:ElementName or ElementName if Prefix=""  */  
   "ElementFullName":string,
      /**  List of table columns with validation rules.  */  
   "ValidationErrorColumns":string,
      /**  Validation message from all columns.  */  
   "ValidationMessage":string,
      /**  Is Doc Level Prefix  */  
   "IsDocLevelPrefix":boolean,
      /**  Doc Level Namespace  */  
   "DocLevelNamespace":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptStructuredOutputFileRow{
      /**  Company  */  
   "Company":string,
      /**  RptStructuredOutputDefID  */  
   "RptStructuredOutputDefID":string,
      /**  RptStructuredOutputFileID  */  
   "RptStructuredOutputFileID":string,
      /**  RptStructuredOutputFileDesc  */  
   "RptStructuredOutputFileDesc":string,
      /**  Enabled  */  
   "Enabled":boolean,
      /**  StructuredOutputFileType  */  
   "StructuredOutputFileType":number,
      /**  OutputLocation  */  
   "OutputLocation":string,
      /**  OutputColumnHeaders  */  
   "OutputColumnHeaders":boolean,
      /**  AdditionalSettings  */  
   "AdditionalSettings":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
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
      /**  AttachToPDFA3  */  
   "AttachToPDFA3":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptStructuredOutputFileXMLNSRow{
      /**  Company  */  
   "Company":string,
      /**  RptStructuredOutputDefID  */  
   "RptStructuredOutputDefID":string,
      /**  RptStructuredOutputFileID  */  
   "RptStructuredOutputFileID":string,
      /**  RptStructuredOutputFileNamespaceID  */  
   "RptStructuredOutputFileNamespaceID":number,
      /**  Namespace  */  
   "Namespace":string,
      /**  Prefix  */  
   "Prefix":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
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




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param structuredDefID
      @param structuredDefFileID
   */  
export interface DeleteAllOutputFileElements_input{
      /**  The structured definition identifier.  */  
   structuredDefID:string,
      /**  The structured definition file identifier.  */  
   structuredDefFileID:string,
}

export interface DeleteAllOutputFileElements_output{
}

   /** Required : 
      @param rptStructuredOutputDefID
   */  
export interface DeleteByID_input{
   rptStructuredOutputDefID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param structuredDefTS
      @param structuredDefID
      @param structuredDefFileID
      @param elementID
      @param originalDataSourceId
   */  
export interface DescendantsWithDataSourceIdExist_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  RptStructuredOutputDefID value.  */  
   structuredDefID:string,
      /**  RptStructuredOutputFileID value.  */  
   structuredDefFileID:string,
      /**  ElementID value.  */  
   elementID:number,
      /**  original DataSourceId value  */  
   originalDataSourceId:string,
}

export interface DescendantsWithDataSourceIdExist_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param sourceSOutputDefID
      @param targetSOutputDefID
      @param targetSOutputDefDesc
   */  
export interface DuplicateStructuredOutputDef_input{
   sourceSOutputDefID:string,
   targetSOutputDefID:string,
   targetSOutputDefDesc:string,
}

export interface DuplicateStructuredOutputDef_output{
}

   /** Required : 
      @param sourceSOutputDefID
      @param sourceSOutputFileID
      @param targetSOutputDefID
      @param targetSOutputFileID
      @param targetSOutputFileDesc
   */  
export interface DuplicateStructuredOutputFile_input{
   sourceSOutputDefID:string,
   sourceSOutputFileID:string,
   targetSOutputDefID:string,
   targetSOutputFileID:string,
   targetSOutputFileDesc:string,
}

export interface DuplicateStructuredOutputFile_output{
}

   /** Required : 
      @param structuredDefID
      @param structuredDefFileID
      @param elementID
   */  
export interface GetAncestorDataSource_input{
      /**  RptStructuredOutputDefID value.  */  
   structuredDefID:string,
      /**  RptStructuredOutputFileID value.  */  
   structuredDefFileID:string,
      /**  ElementID value.  */  
   elementID:number,
}

export interface GetAncestorDataSource_output{
   returnObj:string,
}

   /** Required : 
      @param rptStructuredOutputDefID
   */  
export interface GetByID_input{
   rptStructuredOutputDefID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_RptStructuredOutputDefTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_RptStructuredOutputDefTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_RptStructuredOutputDefTableset[],
}

   /** Required : 
      @param rptDefID
      @param dataSourceId
      @param columnName
   */  
export interface GetDataSourceColumnType_input{
      /**  Report data definition id.  */  
   rptDefID:string,
      /**  Data source id.  */  
   dataSourceId:string,
      /**  Data source column name.  */  
   columnName:string,
}

export interface GetDataSourceColumnType_output{
   returnObj:string,
}

   /** Required : 
      @param structuredDefID
      @param dataSourceID
   */  
export interface GetDataSourceColumns_input{
      /**  RptStructuredOutputDefID value.  */  
   structuredDefID:string,
      /**  Data source id.  */  
   dataSourceID:string,
}

export interface GetDataSourceColumns_output{
   returnObj:Ice_Tablesets_RptDataSourceTableset[],
}

   /** Required : 
      @param structuredDefID
      @param structuredDefFileID
      @param elementID
   */  
export interface GetDataSourceListWithIsUsedSet_input{
      /**  RptStructuredOutputDefID value.  */  
   structuredDefID:string,
      /**  RptStructuredOutputFileID value.  */  
   structuredDefFileID:string,
      /**  ElementID value.  */  
   elementID:number,
}

export interface GetDataSourceListWithIsUsedSet_output{
   returnObj:Ice_Tablesets_RptDataSourceTableset[],
}

   /** Required : 
      @param structuredDefID
      @param structuredDefFileID
      @param elementID
   */  
export interface GetDataSourceList_input{
      /**  RptStructuredOutputDefID value.  */  
   structuredDefID:string,
      /**  RptStructuredOutputFileID value.  */  
   structuredDefFileID:string,
      /**  ElementID value.  */  
   elementID:number,
}

export interface GetDataSourceList_output{
   returnObj:Ice_Tablesets_RptDataSourceTableset[],
}

   /** Required : 
      @param eFTHeadCompany
      @param eFTHeadUID
      @param currentCalculationName
   */  
export interface GetEICalculators_input{
   eFTHeadCompany:string,
   eFTHeadUID:number,
      /**  Current CalculationName value  */  
   currentCalculationName:string,
}

export interface GetEICalculators_output{
   returnObj:string,
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
   returnObj:Ice_Tablesets_RptStructuredOutputDefListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRptStructuredOutputDef_input{
   ds:Ice_Tablesets_RptStructuredOutputDefTableset[],
}

export interface GetNewRptStructuredOutputDef_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptStructuredOutputDefID
      @param rptStructuredOutputFileID
   */  
export interface GetNewRptStructuredOutputFileElement_input{
   ds:Ice_Tablesets_RptStructuredOutputDefTableset[],
   rptStructuredOutputDefID:string,
   rptStructuredOutputFileID:string,
}

export interface GetNewRptStructuredOutputFileElement_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptStructuredOutputDefID
      @param rptStructuredOutputFileID
   */  
export interface GetNewRptStructuredOutputFileXMLNS_input{
   ds:Ice_Tablesets_RptStructuredOutputDefTableset[],
   rptStructuredOutputDefID:string,
   rptStructuredOutputFileID:string,
}

export interface GetNewRptStructuredOutputFileXMLNS_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptStructuredOutputDefID
   */  
export interface GetNewRptStructuredOutputFile_input{
   ds:Ice_Tablesets_RptStructuredOutputDefTableset[],
   rptStructuredOutputDefID:string,
}

export interface GetNewRptStructuredOutputFile_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param whereClauseRptStructuredOutputDef
      @param whereClauseRptStructuredOutputFile
      @param whereClauseRptStructuredOutputFileElement
      @param whereClauseRptStructuredOutputFileXMLNS
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRptStructuredOutputDef:string,
   whereClauseRptStructuredOutputFile:string,
   whereClauseRptStructuredOutputFileElement:string,
   whereClauseRptStructuredOutputFileXMLNS:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_RptStructuredOutputDefTableset[],
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

export interface Ice_Tablesets_RptDataSourceColumnRow{
   RptDefID:string,
   DataSourceID:string,
   ColumnName:string,
   DataType:string,
   ColumnAlias:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptDataSourceRow{
   RptDefID:string,
   DataSourceID:string,
   IsUsed:boolean,
   NeedSign:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptDataSourceTableset{
   RptDataSource:Ice_Tablesets_RptDataSourceRow[],
   RptDataSourceColumn:Ice_Tablesets_RptDataSourceColumnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptStructuredOutputDefListRow{
      /**  Company  */  
   Company:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  RptStructuredOutputDescription  */  
   RptStructuredOutputDescription:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  ConfirmedCompliance  */  
   ConfirmedCompliance:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   RptDataDefRptDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptStructuredOutputDefListTableset{
   RptStructuredOutputDefList:Ice_Tablesets_RptStructuredOutputDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptStructuredOutputDefRow{
      /**  Company  */  
   Company:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  RptStructuredOutputDescription  */  
   RptStructuredOutputDescription:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  ConfirmedCompliance  */  
   ConfirmedCompliance:boolean,
      /**  ComplianceRule  */  
   ComplianceRule:string,
      /**  InternalComments  */  
   InternalComments:string,
      /**  DateFormat  */  
   DateFormat:string,
      /**  DecimalSymbol  */  
   DecimalSymbol:string,
      /**  DigitGroupingSymbol  */  
   DigitGroupingSymbol:string,
      /**  NegativeSignSymbol  */  
   NegativeSignSymbol:string,
      /**  Encoding  */  
   Encoding:string,
      /**  Delimiter  */  
   Delimiter:string,
      /**  EndOfRecordSymbol  */  
   EndOfRecordSymbol:string,
      /**  QuotationMark  */  
   QuotationMark:string,
      /**  QuoteAllValues  */  
   QuoteAllValues:boolean,
      /**  BooleanTrue  */  
   BooleanTrue:string,
      /**  BooleanFalse  */  
   BooleanFalse:string,
      /**  PrePostProcessingEFTHeadCompany  */  
   PrePostProcessingEFTHeadCompany:string,
      /**  PrePostProcessingEFTHeadUID  */  
   PrePostProcessingEFTHeadUID:number,
      /**  AdditionalSettings  */  
   AdditionalSettings:string,
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
      /**  Description for the PrePostProcessingEFTHeadUID  */  
   PrePostProcessingDescription:string,
      /**  Name of the PrePostProcessingEFTHeadUID  */  
   PrePostProcessingName:string,
   BitFlag:number,
   RptDataDefSystemRpt:boolean,
   RptDataDefRptDescription:string,
   RptDataDefDuplicateOf:string,
   RptDataDefRptTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptStructuredOutputDefTableset{
   RptStructuredOutputDef:Ice_Tablesets_RptStructuredOutputDefRow[],
   RptStructuredOutputFile:Ice_Tablesets_RptStructuredOutputFileRow[],
   RptStructuredOutputFileElement:Ice_Tablesets_RptStructuredOutputFileElementRow[],
   RptStructuredOutputFileXMLNS:Ice_Tablesets_RptStructuredOutputFileXMLNSRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptStructuredOutputFileElementRow{
      /**  Company  */  
   Company:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  RptStructuredOutputFileID  */  
   RptStructuredOutputFileID:string,
      /**  ElementID  */  
   ElementID:number,
      /**  ElementName  */  
   ElementName:string,
      /**  ParentElementID  */  
   ParentElementID:number,
      /**  ChildSequence  */  
   ChildSequence:number,
      /**  Namespace  */  
   Namespace:string,
      /**  Prefix  */  
   Prefix:string,
      /**  XMLAttribute  */  
   XMLAttribute:boolean,
      /**  AggregationType  */  
   AggregationType:number,
      /**  DecimalScale  */  
   DecimalScale:number,
      /**  DataSourceID  */  
   DataSourceID:string,
      /**  DataSourceColumn  */  
   DataSourceColumn:string,
      /**  IsConstant  */  
   IsConstant:boolean,
      /**  ConstantValue  */  
   ConstantValue:string,
      /**  CalculationEFTHeadCompany  */  
   CalculationEFTHeadCompany:string,
      /**  CalculationEFTHeadUID  */  
   CalculationEFTHeadUID:number,
      /**  CalculationName  */  
   CalculationName:string,
      /**  AdditionalSettings  */  
   AdditionalSettings:string,
      /**  DateFormat  */  
   DateFormat:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  JSONObject  */  
   JSONObject:boolean,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ElementDataType  */  
   ElementDataType:string,
      /**  ElementDescription  */  
   ElementDescription:string,
      /**  EmptyStringGenerateEmptyElement  */  
   EmptyStringGenerateEmptyElement:boolean,
      /**  EmptyStringSuppressOrNullElement  */  
   EmptyStringSuppressOrNullElement:boolean,
      /**  EmptyStringSubsituteElement  */  
   EmptyStringSubsituteElement:boolean,
      /**  EmptyStringSubsituteValue  */  
   EmptyStringSubsituteValue:string,
      /**  ZeroNumericSuppress  */  
   ZeroNumericSuppress:boolean,
      /**  NeedSign  */  
   NeedSign:boolean,
      /**  CalculationEFTHeadName  */  
   CalculationEFTHeadName:string,
      /**  .NET Data type for the datasource column.  */  
   DataSourceColumnDataType:string,
      /**  Element name including the prefix. Prefix:ElementName or ElementName if Prefix=""  */  
   ElementFullName:string,
      /**  List of table columns with validation rules.  */  
   ValidationErrorColumns:string,
      /**  Validation message from all columns.  */  
   ValidationMessage:string,
      /**  Is Doc Level Prefix  */  
   IsDocLevelPrefix:boolean,
      /**  Doc Level Namespace  */  
   DocLevelNamespace:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptStructuredOutputFileRow{
      /**  Company  */  
   Company:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  RptStructuredOutputFileID  */  
   RptStructuredOutputFileID:string,
      /**  RptStructuredOutputFileDesc  */  
   RptStructuredOutputFileDesc:string,
      /**  Enabled  */  
   Enabled:boolean,
      /**  StructuredOutputFileType  */  
   StructuredOutputFileType:number,
      /**  OutputLocation  */  
   OutputLocation:string,
      /**  OutputColumnHeaders  */  
   OutputColumnHeaders:boolean,
      /**  AdditionalSettings  */  
   AdditionalSettings:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
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
      /**  AttachToPDFA3  */  
   AttachToPDFA3:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptStructuredOutputFileXMLNSRow{
      /**  Company  */  
   Company:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  RptStructuredOutputFileID  */  
   RptStructuredOutputFileID:string,
      /**  RptStructuredOutputFileNamespaceID  */  
   RptStructuredOutputFileNamespaceID:number,
      /**  Namespace  */  
   Namespace:string,
      /**  Prefix  */  
   Prefix:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
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

export interface Ice_Tablesets_UpdExtRptStructuredOutputDefTableset{
   RptStructuredOutputDef:Ice_Tablesets_RptStructuredOutputDefRow[],
   RptStructuredOutputFile:Ice_Tablesets_RptStructuredOutputFileRow[],
   RptStructuredOutputFileElement:Ice_Tablesets_RptStructuredOutputFileElementRow[],
   RptStructuredOutputFileXMLNS:Ice_Tablesets_RptStructuredOutputFileXMLNSRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param structuredDefTS
      @param structuredDefID
      @param structuredDefFileID
      @param method
      @param filePath
   */  
export interface ImportFile_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  The structured definition identifier.  */  
   structuredDefID:string,
      /**  The structured definition file identifier.  */  
   structuredDefFileID:string,
      /**  The import method name.  */  
   method:string,
      /**  The file path.  */  
   filePath:string,
}

export interface ImportFile_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param structuredDefTS
      @param structuredDefID
      @param structuredDefFileID
      @param jsonSchema
   */  
export interface ImportJSONSchema_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  The structured definition identifier.  */  
   structuredDefID:string,
      /**  The structured definition file identifier.  */  
   structuredDefFileID:string,
      /**  The json schema.  */  
   jsonSchema:string,
}

export interface ImportJSONSchema_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param structuredDefTS
      @param structuredDefID
      @param structuredDefFileID
      @param xmlData
   */  
export interface ImportXmlDataWithNoValues_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  The structured definition identifier.  */  
   structuredDefID:string,
      /**  The structured definition file identifier.  */  
   structuredDefFileID:string,
      /**  The XML data.  */  
   xmlData:string,
}

export interface ImportXmlDataWithNoValues_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param structuredDefTS
      @param structuredDefID
      @param structuredDefFileID
      @param xmlData
   */  
export interface ImportXmlDataWithValues_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  The structured definition identifier.  */  
   structuredDefID:string,
      /**  The structured definition file identifier.  */  
   structuredDefFileID:string,
      /**  The XML data.  */  
   xmlData:string,
}

export interface ImportXmlDataWithValues_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param reportId
      @param proposedOutputLocation
   */  
export interface OnChangeOutputLocation_input{
      /**  The report ID.  */  
   reportId:string,
      /**  The proposed output location.  */  
   proposedOutputLocation:string,
}

export interface OnChangeOutputLocation_output{
}

   /** Required : 
      @param structuredDefTS
      @param proposedRptDefId
   */  
export interface OnChangeReportDataDefinition_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  The proposed Report Data Definition identifier.  */  
   proposedRptDefId:string,
}

export interface OnChangeReportDataDefinition_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param structuredDefTS
      @param structuredDefID
      @param structuredDefFileID
      @param elementID
      @param originalDataSourceId
      @param newDataSourceID
   */  
export interface UpdateDescendantsWithNewDataSourceId_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  RptStructuredOutputDefID value.  */  
   structuredDefID:string,
      /**  RptStructuredOutputFileID value.  */  
   structuredDefFileID:string,
      /**  ElementID value.  */  
   elementID:number,
      /**  original DataSourceId value  */  
   originalDataSourceId:string,
      /**  new DataSourceID value  */  
   newDataSourceID:string,
}

export interface UpdateDescendantsWithNewDataSourceId_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtRptStructuredOutputDefTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtRptStructuredOutputDefTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_RptStructuredOutputDefTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param structuredDefTS
      @param elementToValidate
   */  
export interface ValidateOutputFileElement_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
      /**  >ElementID of output file element row to validate.  */  
   elementToValidate:number,
}

export interface ValidateOutputFileElement_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

   /** Required : 
      @param structuredDefTS
   */  
export interface ValidateOutputFileElements_input{
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset[],
}

export interface ValidateOutputFileElements_output{
parameters : {
      /**  output parameters  */  
   structuredDefTS:Ice_Tablesets_RptStructuredOutputDefTableset,
}
}

